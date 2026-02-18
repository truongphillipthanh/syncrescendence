#!/usr/bin/env bash
# auto_ingest_loop.sh - Agent auto-ingest wrapper for Syncrescendence constellation
# Usage: ./auto_ingest_loop.sh <agent_name> <repo_path> [tmux_session] [tmux_pane]

# NOTE: set -e deliberately omitted — loop must survive transient failures.
set -u

AGENT_NAME="${1:?Agent name required (commander|adjudicator|cartographer|psyche|ajna)}"
REPO_PATH="${2:?Repo path required}"
TMUX_SESSION="${3:-constellation}"
TMUX_PANE="${4:-}"

INBOX_DIR="${REPO_PATH}/-INBOX/${AGENT_NAME}/00-INBOX0"
IN_PROGRESS_DIR="${REPO_PATH}/-INBOX/${AGENT_NAME}/10-IN_PROGRESS"
DONE_DIR="${REPO_PATH}/-INBOX/${AGENT_NAME}/40-DONE"
FAILED_DIR="${REPO_PATH}/-INBOX/${AGENT_NAME}/50_FAILED"
OUTBOX_DIR="${REPO_PATH}/-OUTBOX/${AGENT_NAME}/RESULTS"
TMP_LOCKFILE="/tmp/auto_ingest_${AGENT_NAME}.lock"
LEGACY_LOCKFILE="${REPO_PATH}/-INBOX/${AGENT_NAME}/.auto_ingest.lock"
LOGFILE="${REPO_PATH}/-INBOX/${AGENT_NAME}/auto_ingest.log"
STATE_FILE="${REPO_PATH}/-INBOX/${AGENT_NAME}/.current_task"

STATE_ROOT="${REPO_PATH}/00-ORCHESTRATION/state"
BREAKER_DIR="${STATE_ROOT}/breakers"
BREAKER_FILE="${BREAKER_DIR}/orchestration.breaker"
HEARTBEAT_DIR="${STATE_ROOT}/heartbeat"
HEARTBEAT_FILE="${HEARTBEAT_DIR}/${AGENT_NAME}.heartbeat"
BUDGET_DIR="${STATE_ROOT}/budgets"
INTEGRITY_GATE_SCRIPT="${REPO_PATH}/00-ORCHESTRATION/scripts/repo_integrity_gate.sh"

POLL_INTERVAL=30
TASK_TIMEOUT=1800
RETRY_SCAN_INTERVAL=60
MAX_RETRIES=3
MAX_RETRIES_PER_HOUR="${SYNCRESCENDENCE_MAX_RETRIES_PER_HOUR:-20}"
INTEGRITY_CHECK_INTERVAL="${SYNCRESCENDENCE_INTEGRITY_CHECK_INTERVAL:-120}"
TRANSIENT_FAILURE_REGEX='rate[[:space:]._-]*limit|timeout|quota|capacity|RESOURCE_EXHAUSTED|usage[[:space:]._-]*limit|EXEC_TIMEOUT|network|connection reset|temporarily unavailable'

TMUX_BIN="/opt/homebrew/bin/tmux"
GEMINI_BIN="/opt/homebrew/bin/gemini"

LAST_FAILURE_REASON=""
LAST_FAILURE_CODE=""
LAST_FAILURE_CLASS=""
LAST_FAILURE_RETRYABLE=""
LAST_KNOWN_STATE="IDLE"
LAST_INTEGRITY_CHECK=0
INTEGRITY_OK_CACHE=1

VALID_AGENTS="commander adjudicator cartographer psyche ajna dispatch"
BRIDGE_ENV_KEYS="SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$AGENT_NAME] $*" | tee -a "$LOGFILE"
}

cleanup() {
    rm -f "$TMP_LOCKFILE" "$LEGACY_LOCKFILE"
    update_heartbeat "STOPPED" "shutdown"
    log "Shutdown signal received, cleaning up"
    exit 0
}

trap cleanup INT TERM

set_bridge_var_if_unset() {
    key="$1"
    value="$2"
    [ -z "$value" ] && return 0

    case "$key" in
        SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA)
            [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA="$value"
            ;;
        SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER)
            [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER="$value"
            ;;
        SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR)
            [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR="$value"
            ;;
        SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER)
            [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER="$value"
            ;;
        SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE)
            [ -z "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE:-}" ] && SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE="$value"
            ;;
    esac
}

load_bridge_env_from_launchctl() {
    command -v launchctl >/dev/null 2>&1 || return 0
    for key in $BRIDGE_ENV_KEYS; do
        value=$(launchctl getenv "$key" 2>/dev/null || true)
        set_bridge_var_if_unset "$key" "$value"
    done
}

load_bridge_env_from_supervisor_plist() {
    plist="${HOME}/Library/LaunchAgents/com.syncrescendence.auto-ingest-supervisor.plist"
    [ -f "$plist" ] || return 0
    [ -x /usr/libexec/PlistBuddy ] || return 0

    for key in $BRIDGE_ENV_KEYS; do
        value=$(/usr/libexec/PlistBuddy -c "Print :EnvironmentVariables:${key}" "$plist" 2>/dev/null || true)
        set_bridge_var_if_unset "$key" "$value"
    done
}

load_bridge_env_from_zshrc() {
    [ -f "${HOME}/.zshrc" ] || return 0
    while IFS= read -r line; do
        case "$line" in
            export\ SYNCRESCENDENCE_REMOTE_AGENT_HOST_*=*)
                key=$(printf '%s' "$line" | sed -E 's/^export[[:space:]]+([^=]+)=.*/\1/')
                val=$(printf '%s' "$line" | sed -E 's/^export[[:space:]]+[^=]+=//; s/^"//; s/"$//')
                set_bridge_var_if_unset "$key" "$val"
                ;;
        esac
    done < "${HOME}/.zshrc"
}

ensure_bridge_env() {
    load_bridge_env_from_launchctl
    load_bridge_env_from_supervisor_plist
    load_bridge_env_from_zshrc

    : "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA:=macbook-air}"
    : "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER:=local}"
    : "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR:=local}"
    : "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER:=local}"
    : "${SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE:=local}"

    export SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA
    export SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER
    export SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR
    export SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER
    export SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE
}

acquire_lock() {
    for lock in "$TMP_LOCKFILE" "$LEGACY_LOCKFILE"; do
        if [ -f "$lock" ]; then
            existing_pid=$(cat "$lock" 2>/dev/null || echo "")
            if [ -n "$existing_pid" ] && kill -0 "$existing_pid" 2>/dev/null; then
                log "ERROR: Another instance running (PID: $existing_pid via $lock)"
                exit 1
            fi
            log "Removing stale lockfile $lock (PID $existing_pid gone)"
            rm -f "$lock"
        fi
    done

    echo $$ > "$TMP_LOCKFILE"
    echo $$ > "$LEGACY_LOCKFILE"
}

ensure_directories() {
    mkdir -p "$INBOX_DIR" "$IN_PROGRESS_DIR" "$DONE_DIR" "$FAILED_DIR" "$OUTBOX_DIR"
    mkdir -p "$BREAKER_DIR" "$HEARTBEAT_DIR" "$BUDGET_DIR"
}

update_heartbeat() {
    state="$1"
    detail="${2:-}"
    LAST_KNOWN_STATE="$state"

    cat > "$HEARTBEAT_FILE" <<HB
timestamp_unix=$(date +%s)
timestamp_iso=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
agent=${AGENT_NAME}
pid=$$
state=${state}
detail=${detail}
current_task=${CURRENT_TASK_ID:-none}
tmux_pane=${TMUX_SESSION}:${TMUX_PANE}
HB
}

extract_objective() {
    task_file="$1"
    awk '
        /^## Objective/ { in_section=1; next }
        /^---$/ { if (in_section) exit }
        /^## / { if (in_section) exit }
        in_section && NF { print }
    ' "$task_file" | sed 's/^[[:space:]]*//' | sed '/^$/d'
}

extract_reply_to() {
    task_file="$1"
    raw=$(grep '^\*\*Reply-To\*\*:' "$task_file" 2>/dev/null | head -n1 | sed 's/.*: *//')
    for valid in $VALID_AGENTS; do
        if [ "$raw" = "$valid" ]; then
            echo "$raw"
            return
        fi
    done
    [ -n "$raw" ] && log "WARN: reply_to '$raw' not in allowlist, ignoring"
    echo ""
}

extract_task_id() {
    basename "$1" .md
}

read_markdown_field() {
    task_file="$1"
    field_name="$2"
    sed -n "s/^\*\*${field_name}\*\*:[[:space:]]*//p" "$task_file" 2>/dev/null | head -n1
}

upsert_markdown_field() {
    task_file="$1"
    field_name="$2"
    field_value="$3"

    if grep -q "^\*\*${field_name}\*\*:" "$task_file" 2>/dev/null; then
        sed -i '' "s|^\*\*${field_name}\*\*:[[:space:]]*.*|**${field_name}**: ${field_value}|" "$task_file"
    elif grep -q '^\*\*Status\*\*:' "$task_file" 2>/dev/null; then
        sed -i '' "/^\*\*Status\*\*:/a\\
**${field_name}**: ${field_value}
" "$task_file"
    else
        printf "\n**%s**: %s\n" "$field_name" "$field_value" >> "$task_file"
    fi
}

get_retry_count() {
    task_file="$1"
    retry_count=$(read_markdown_field "$task_file" "Retry-Count" | tr -cd '0-9')
    [ -z "$retry_count" ] && retry_count=0
    echo "$retry_count"
}

get_failure_reason() {
    task_file="$1"
    failure_reason=$(read_markdown_field "$task_file" "Failure-Reason")
    if [ -z "$failure_reason" ]; then
        failure_reason=$(grep -E '^(DISPATCH_FAILED|TIMEOUT|EXEC_TIMEOUT):' "$task_file" 2>/dev/null | tail -n1 | sed 's/^[^:]*:[[:space:]]*//')
    fi
    echo "$failure_reason"
}

get_failure_retryable() {
    task_file="$1"
    v=$(read_markdown_field "$task_file" "Failure-Retryable" | tr '[:upper:]' '[:lower:]')
    case "$v" in
        true|yes|1) echo "true" ;;
        false|no|0) echo "false" ;;
        *)
            reason=$(get_failure_reason "$task_file")
            if echo "$reason" | grep -qiE "$TRANSIENT_FAILURE_REGEX"; then
                echo "true"
            else
                echo "false"
            fi
            ;;
    esac
}

set_failure_envelope() {
    task_file="$1"
    code="$2"
    klass="$3"
    retryable="$4"
    reason="$5"

    [ -f "$task_file" ] || return 0

    upsert_markdown_field "$task_file" "Status" "FAILED"
    upsert_markdown_field "$task_file" "Failure-Code" "$code"
    upsert_markdown_field "$task_file" "Failure-Class" "$klass"
    upsert_markdown_field "$task_file" "Failure-Retryable" "$retryable"
    upsert_markdown_field "$task_file" "Failure-Reason" "$reason"
    upsert_markdown_field "$task_file" "Failed-At" "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"

    if ! grep -q '^\*\*Retry-Count\*\*:' "$task_file" 2>/dev/null; then
        upsert_markdown_field "$task_file" "Retry-Count" "0"
    fi
}

current_hour_key() {
    date -u '+%Y%m%d%H'
}

retry_budget_allows() {
    hour_key=$(current_hour_key)
    budget_file="${BUDGET_DIR}/retry-${AGENT_NAME}-${hour_key}.count"
    count=0
    [ -f "$budget_file" ] && count=$(cat "$budget_file" 2>/dev/null | tr -cd '0-9')
    [ -z "$count" ] && count=0
    [ "$count" -lt "$MAX_RETRIES_PER_HOUR" ]
}

record_retry_budget() {
    hour_key=$(current_hour_key)
    budget_file="${BUDGET_DIR}/retry-${AGENT_NAME}-${hour_key}.count"
    count=0
    [ -f "$budget_file" ] && count=$(cat "$budget_file" 2>/dev/null | tr -cd '0-9')
    [ -z "$count" ] && count=0
    count=$((count + 1))
    echo "$count" > "$budget_file"
}

breaker_is_open() {
    [ -f "$BREAKER_FILE" ] || return 1
    state=$(grep '^state=' "$BREAKER_FILE" 2>/dev/null | head -n1 | cut -d'=' -f2)
    [ "$state" = "OPEN" ]
}

integrity_allows_writes() {
    now=$(date +%s)
    if [ "$((now - LAST_INTEGRITY_CHECK))" -lt "$INTEGRITY_CHECK_INTERVAL" ]; then
        [ "$INTEGRITY_OK_CACHE" -eq 1 ]
        return
    fi

    LAST_INTEGRITY_CHECK="$now"
    if [ -x "$INTEGRITY_GATE_SCRIPT" ]; then
        if "$INTEGRITY_GATE_SCRIPT" --repo "$REPO_PATH" --context "auto_ingest_${AGENT_NAME}" --quiet; then
            INTEGRITY_OK_CACHE=1
            return 0
        fi
        INTEGRITY_OK_CACHE=0
        log "INTEGRITY_GUARD: fail-closed active for this cycle"
        return 1
    fi

    INTEGRITY_OK_CACHE=1
    return 0
}

is_transient_failure() {
    failure_reason="$1"
    echo "$failure_reason" | grep -qiE "$TRANSIENT_FAILURE_REGEX"
}

retry_failed_tasks() {
    if ! integrity_allows_writes; then
        return 0
    fi
    if breaker_is_open; then
        log "BREAKER_OPEN: retry scan skipped"
        return 0
    fi

    for task_file in "$FAILED_DIR"/TASK-*.md; do
        [ -f "$task_file" ] || continue

        retry_count=$(get_retry_count "$task_file")
        [ "$retry_count" -ge "$MAX_RETRIES" ] && continue

        retryable=$(get_failure_retryable "$task_file")
        [ "$retryable" = "true" ] || continue

        if ! retry_budget_allows; then
            log "RETRY_BUDGET: hourly cap reached (${MAX_RETRIES_PER_HOUR}), deferring retries"
            break
        fi

        new_count=$((retry_count + 1))
        upsert_markdown_field "$task_file" "Retry-Count" "$new_count"
        upsert_markdown_field "$task_file" "Attempt" "$((new_count + 1))"
        upsert_markdown_field "$task_file" "Status" "PENDING"

        task_base=$(basename "$task_file")
        if mv "$task_file" "${INBOX_DIR}/${task_base}" 2>/dev/null; then
            record_retry_budget
            rm -f "${FAILED_DIR}/.escalated-${task_base}" 2>/dev/null || true
            log "RETRY (${new_count}/${MAX_RETRIES}): ${task_base}"
        else
            upsert_markdown_field "$task_file" "Status" "FAILED"
            log "WARN: RETRY move failed for ${task_base}"
        fi
    done
}

escalate_exhausted_tasks() {
    if ! integrity_allows_writes; then
        return 0
    fi

    sovereign_dir="${REPO_PATH}/-SOVEREIGN"
    mkdir -p "$sovereign_dir" 2>/dev/null || true

    for task_file in "$FAILED_DIR"/TASK-*.md; do
        [ -f "$task_file" ] || continue

        retry_count=$(get_retry_count "$task_file")
        [ "$retry_count" -lt "$MAX_RETRIES" ] && continue

        base=$(basename "$task_file")
        esc_marker="${FAILED_DIR}/.escalated-${base}"
        [ -f "$esc_marker" ] && continue

        failure_reason=$(get_failure_reason "$task_file")
        failure_code=$(read_markdown_field "$task_file" "Failure-Code")
        failure_class=$(read_markdown_field "$task_file" "Failure-Class")
        [ -z "$failure_reason" ] && failure_reason="unknown"
        [ -z "$failure_code" ] && failure_code="UNKNOWN"
        [ -z "$failure_class" ] && failure_class="unknown"

        esc_file="${sovereign_dir}/ESCALATION-${AGENT_NAME}-$(date +%Y%m%d)-${base}"
        cat > "$esc_file" <<ESC
# ESCALATION: Task exhausted retries

**Kind**: ESCALATION
**Agent**: ${AGENT_NAME}
**Task**: ${base}
**Retries**: ${retry_count}
**Failure-Code**: ${failure_code}
**Failure-Class**: ${failure_class}
**Failure-Reason**: ${failure_reason}
**Escalated-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')

This task exhausted retry budget and requires Sovereign intervention.
ESC

        touch "$esc_marker"
        log "ESCALATION: ${base} → -SOVEREIGN/"
    done
}

check_pane_for_rate_limit() {
    if [ -z "$TMUX_PANE" ]; then
        return 1
    fi
    recent=$($TMUX_BIN capture-pane -t "${TMUX_SESSION}:${TMUX_PANE}" -p -S -10 2>/dev/null || echo "")
    echo "$recent" | grep -qiE "rate limit|usage limit|high demand|quota exceeded"
}

is_gemini_agent() {
    [ "$AGENT_NAME" = "cartographer" ]
}

check_pane_exists() {
    if [ -z "$TMUX_PANE" ]; then
        return 1
    fi
    $TMUX_BIN has-session -t "${TMUX_SESSION}" 2>/dev/null || return 1
    target_window=$(echo "$TMUX_PANE" | cut -d. -f1)
    target_pane=$(echo "$TMUX_PANE" | cut -d. -f2)
    $TMUX_BIN list-panes -t "${TMUX_SESSION}:${target_window}" -F '#{pane_index}' 2>/dev/null | grep -q "^${target_pane}$" 2>/dev/null
}

send_prompt() {
    prompt="$1"
    LAST_FAILURE_REASON=""
    LAST_FAILURE_CODE=""
    LAST_FAILURE_CLASS=""
    LAST_FAILURE_RETRYABLE=""

    if is_gemini_agent; then
        log "Gemini headless dispatch: running gemini -p -y -o text"
        result_slug=$(echo "$CURRENT_TASK_ID" | sed 's/^TASK-//')
        result_path="${OUTBOX_DIR}/RESULT-${AGENT_NAME}-${result_slug}.md"
        ( cd "${REPO_PATH}" && ${GEMINI_BIN} -p "$prompt" -y -o text > "${result_path}" 2>>"${LOGFILE}" ) &
        GEMINI_PID=$!
        log "Gemini headless PID: ${GEMINI_PID}"
        return 0
    fi

    if [ -z "$TMUX_PANE" ]; then
        LAST_FAILURE_REASON="TMUX pane not specified"
        LAST_FAILURE_CODE="DISPATCH_TMUX_PANE_MISSING"
        LAST_FAILURE_CLASS="configuration"
        LAST_FAILURE_RETRYABLE="false"
        log "ERROR: No tmux pane specified"
        return 1
    fi

    if ! check_pane_exists; then
        LAST_FAILURE_REASON="TMUX pane not found"
        LAST_FAILURE_CODE="DISPATCH_TMUX_PANE_NOT_FOUND"
        LAST_FAILURE_CLASS="infrastructure"
        LAST_FAILURE_RETRYABLE="true"
        log "ERROR: tmux pane ${TMUX_SESSION}:${TMUX_PANE} not found"
        return 1
    fi

    retry=0
    while check_pane_for_rate_limit; do
        retry=$((retry + 1))
        if [ "$retry" -gt 10 ]; then
            LAST_FAILURE_REASON="rate limit persisted after retries"
            LAST_FAILURE_CODE="RATE_LIMIT"
            LAST_FAILURE_CLASS="quota"
            LAST_FAILURE_RETRYABLE="true"
            log "ERROR: Rate limit persists after 10 retries"
            return 1
        fi
        log "Rate limit detected, waiting 60s (retry $retry/10)..."
        sleep 60
    done

    if [ ${#prompt} -gt 2000 ]; then
        prompt=$(echo "$prompt" | head -c 1900)
        prompt="${prompt}... [truncated — see full task file in 10-IN_PROGRESS]"
    fi

    $TMUX_BIN send-keys -t "${TMUX_SESSION}:${TMUX_PANE}" "$prompt" Enter
    sleep 2
    $TMUX_BIN send-keys -t "${TMUX_SESSION}:${TMUX_PANE}" Enter
    return 0
}

dispatch_task() {
    task_file="$1"

    if ! integrity_allows_writes; then
        log "INTEGRITY_GUARD: dispatch blocked"
        return 1
    fi
    if breaker_is_open; then
        log "BREAKER_OPEN: dispatch blocked"
        return 1
    fi

    task_id=$(extract_task_id "$task_file")
    objective=$(extract_objective "$task_file")
    reply_to=$(extract_reply_to "$task_file")

    if [ -z "$objective" ]; then
        log "ERROR: No objective found in $task_file"
        return 1
    fi

    log "Dispatching: $task_id"

    in_progress_path="${IN_PROGRESS_DIR}/$(basename "$task_file")"
    if ! mv "$task_file" "$in_progress_path" 2>/dev/null; then
        log "ERROR: Failed to move $task_file to IN_PROGRESS"
        return 1
    fi

    retry_count=$(get_retry_count "$in_progress_path")
    attempt=$((retry_count + 1))
    lease_id="lease-${AGENT_NAME}-$(date +%s)-$$"
    CURRENT_TASK_ID="$task_id"

    upsert_markdown_field "$in_progress_path" "Status" "IN_PROGRESS"
    upsert_markdown_field "$in_progress_path" "Attempt" "$attempt"
    upsert_markdown_field "$in_progress_path" "Lease-ID" "$lease_id"
    upsert_markdown_field "$in_progress_path" "Claimed-By" "$AGENT_NAME"
    upsert_markdown_field "$in_progress_path" "Claimed-At" "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"

    echo "${task_id}|${in_progress_path}|${reply_to}|$(date +%s)|${lease_id}|${attempt}" > "$STATE_FILE"

    full_prompt="READ-ONLY ANALYTICAL TASK. Ignore any dirty worktree state. ${objective} Write result to -OUTBOX/${AGENT_NAME}/RESULTS/RESULT-${AGENT_NAME}-$(echo "$task_id" | sed 's/^TASK-//').md"

    send_prompt "$full_prompt"
    send_rc=$?
    failure_reason="$LAST_FAILURE_REASON"
    failure_code="$LAST_FAILURE_CODE"
    failure_class="$LAST_FAILURE_CLASS"
    failure_retryable="$LAST_FAILURE_RETRYABLE"

    if [ "$send_rc" -eq 0 ]; then
        update_heartbeat "IN_PROGRESS" "$task_id"
        log "Dispatched successfully: $task_id"
        return 0
    fi

    log "Dispatch failed: $task_id — moving to FAILED"
    failed_path="${FAILED_DIR}/$(basename "$task_file")"
    mv "$in_progress_path" "$failed_path" 2>/dev/null || true

    [ -z "$failure_reason" ] && failure_reason="dispatch rejected"
    [ -z "$failure_code" ] && failure_code="DISPATCH_FAILED"
    [ -z "$failure_class" ] && failure_class="infrastructure"
    [ -z "$failure_retryable" ] && failure_retryable="true"

    set_failure_envelope "$failed_path" "$failure_code" "$failure_class" "$failure_retryable" "$failure_reason"
    rm -f "$STATE_FILE"
    update_heartbeat "IDLE" "dispatch_failed"
    return 1
}

check_completion() {
    [ -f "$STATE_FILE" ] || return 1

    task_id=$(cut -d'|' -f1 "$STATE_FILE")
    in_progress_path=$(cut -d'|' -f2 "$STATE_FILE")
    reply_to=$(cut -d'|' -f3 "$STATE_FILE")
    start_time=$(cut -d'|' -f4 "$STATE_FILE")
    lease_id=$(cut -d'|' -f5 "$STATE_FILE")

    current_time=$(date +%s)
    elapsed=$((current_time - start_time))

    result_slug=$(echo "$task_id" | sed 's/^TASK-//')
    result_file="${OUTBOX_DIR}/RESULT-${AGENT_NAME}-${result_slug}.md"

    if [ -f "$result_file" ]; then
        result_size=$(wc -c < "$result_file" 2>/dev/null || echo 0)
        [ "$result_size" -lt 100 ] && log "WARN: Result file suspiciously small (${result_size} bytes)"
        log "Task completed: $task_id (${elapsed}s, ${result_size} bytes, lease=${lease_id})"

        mv "$in_progress_path" "${DONE_DIR}/$(basename "$in_progress_path")" 2>/dev/null || log "WARN: Could not move to DONE"

        if [ -n "$reply_to" ] && [ "$reply_to" != "dispatch" ]; then
            confirm_dir="${REPO_PATH}/-INBOX/${reply_to}/00-INBOX0"
            mkdir -p "$confirm_dir"
            confirm_file="${confirm_dir}/CONFIRM-${AGENT_NAME}-${result_slug}.md"

            cat > "$confirm_file" <<CONFIRM_EOF
# CONFIRM-${AGENT_NAME}-${result_slug}

**Kind**: CONFIRM
**Task**: ${task_id}.md
**From-Agent**: ${AGENT_NAME}
**To-Agent**: ${reply_to}
**Status**: COMPLETE
**Exit-Code**: 0
**Lease-ID**: ${lease_id}
**Completed-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')
**Result-Path**: ${result_file}
CONFIRM_EOF
            log "Sent CONFIRM to ${reply_to}"

            REPLY_UPPER=$(echo "$reply_to" | tr '[:lower:]' '[:upper:]')
            REMOTE_VAR="SYNCRESCENDENCE_REMOTE_AGENT_HOST_${REPLY_UPPER}"
            REMOTE_HOST="${!REMOTE_VAR:-local}"
            if [ -n "$REMOTE_HOST" ] && [ "$REMOTE_HOST" != "local" ] && [ "$REMOTE_HOST" != "localhost" ]; then
                if scp -q -o BatchMode=yes -o ConnectTimeout=5 "$confirm_file" "$REMOTE_HOST:~/Desktop/syncrescendence/-INBOX/${reply_to}/00-INBOX0/" 2>/dev/null; then
                    log "Neural Bridge: CONFIRM routed to ${REMOTE_HOST} for ${reply_to}"
                else
                    log "WARN: Neural Bridge SCP failed for CONFIRM to ${REMOTE_HOST}"
                fi
            fi
        fi

        rm -f "$STATE_FILE"
        CURRENT_TASK_ID=""
        update_heartbeat "IDLE" "task_complete"
        return 0
    fi

    if [ "$elapsed" -gt "$TASK_TIMEOUT" ]; then
        log "TIMEOUT: $task_id (${elapsed}s exceeded ${TASK_TIMEOUT}s)"
        failed_path="${FAILED_DIR}/$(basename "$in_progress_path")"
        mv "$in_progress_path" "$failed_path" 2>/dev/null || true
        set_failure_envelope "$failed_path" "EXEC_TIMEOUT" "timeout" "true" "Exceeded ${TASK_TIMEOUT}s"
        rm -f "$STATE_FILE"
        CURRENT_TASK_ID=""
        update_heartbeat "IDLE" "task_timeout"
        return 0
    fi

    return 1
}

recover_state() {
    [ -f "$STATE_FILE" ] || return 0
    task_id=$(cut -d'|' -f1 "$STATE_FILE")
    in_progress_path=$(cut -d'|' -f2 "$STATE_FILE")
    if [ ! -f "$in_progress_path" ]; then
        log "WARN: Stale state for missing task file, clearing"
        rm -f "$STATE_FILE"
        return 0
    fi
    CURRENT_TASK_ID="$task_id"
    log "Recovered in-progress task: $task_id"
    update_heartbeat "IN_PROGRESS" "recovered_${task_id}"
    return 0
}

main() {
    log "=== Starting auto-ingest loop ==="
    log "Agent: $AGENT_NAME | Repo: $REPO_PATH | Pane: ${TMUX_SESSION}:${TMUX_PANE}"

    ensure_bridge_env
    log "Neural Bridge env: AJNA=${SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA} CMD=${SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER} ADJ=${SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR} CART=${SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER} PSY=${SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE}"

    acquire_lock
    ensure_directories
    recover_state
    last_retry_scan=0

    update_heartbeat "IDLE" "startup"

    while true; do
        sleep_duration="$POLL_INTERVAL"

        if [ -f "$STATE_FILE" ]; then
            check_completion
            sleep_duration=5
            update_heartbeat "IN_PROGRESS" "waiting_result"
        else
            update_heartbeat "IDLE" "polling"
            if integrity_allows_writes && ! breaker_is_open; then
                task_file=$(find "$INBOX_DIR" -maxdepth 1 -name "TASK-*.md" -type f 2>/dev/null | sort | head -n1)
                if [ -n "$task_file" ]; then
                    dispatch_task "$task_file" || true
                fi
            else
                log "WRITE_GUARD: dispatch paused (integrity or breaker)"
            fi
        fi

        now=$(date +%s)
        if [ $((now - last_retry_scan)) -ge "$RETRY_SCAN_INTERVAL" ]; then
            retry_failed_tasks
            escalate_exhausted_tasks
            last_retry_scan="$now"
        fi

        sleep "$sleep_duration"
    done
}

main
