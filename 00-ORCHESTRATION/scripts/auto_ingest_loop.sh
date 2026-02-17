#!/bin/sh
# auto_ingest_loop.sh - Agent auto-ingest wrapper for Syncrescendence constellation
# Usage: ./auto_ingest_loop.sh <agent_name> <repo_path> [tmux_session] [tmux_pane]
# Solves: CLI agents don't automatically pick up task files from their inbox
# IMPL-Q-0029 | INT-1804

# NOTE: set -e deliberately omitted — loop must survive transient failures
# (Adjudicator audit: set -e causes full loop termination on failed mv/send)

AGENT_NAME="${1:?Agent name required (commander|adjudicator|cartographer|psyche|ajna)}"
REPO_PATH="${2:?Repo path required}"
TMUX_SESSION="${3:-constellation}"
TMUX_PANE="${4:-}"

INBOX_DIR="${REPO_PATH}/-INBOX/${AGENT_NAME}/00-INBOX0"
IN_PROGRESS_DIR="${REPO_PATH}/-INBOX/${AGENT_NAME}/10-IN_PROGRESS"
DONE_DIR="${REPO_PATH}/-INBOX/${AGENT_NAME}/40-DONE"
FAILED_DIR="${REPO_PATH}/-INBOX/${AGENT_NAME}/50_FAILED"
OUTBOX_DIR="${REPO_PATH}/-OUTBOX/${AGENT_NAME}/RESULTS"
# Primary lock moved to /tmp for reboot resilience and easy global health checks.
TMP_LOCKFILE="/tmp/auto_ingest_${AGENT_NAME}.lock"
# Legacy lock retained for compatibility with existing tooling.
LEGACY_LOCKFILE="${REPO_PATH}/-INBOX/${AGENT_NAME}/.auto_ingest.lock"
LOGFILE="${REPO_PATH}/-INBOX/${AGENT_NAME}/auto_ingest.log"
STATE_FILE="${REPO_PATH}/-INBOX/${AGENT_NAME}/.current_task"

POLL_INTERVAL=30
TASK_TIMEOUT=1800  # 30 minutes

TMUX_BIN="/opt/homebrew/bin/tmux"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$AGENT_NAME] $*" | tee -a "$LOGFILE"
}

load_bridge_env_from_zshrc() {
    [ -f "${HOME}/.zshrc" ] || return 0
    while IFS= read -r line; do
        case "$line" in
            export\ SYNCRESCENDENCE_REMOTE_AGENT_HOST_*=*)
                key=$(printf '%s' "$line" | sed -E 's/^export[[:space:]]+([^=]+)=.*/\1/')
                val=$(printf '%s' "$line" | sed -E 's/^export[[:space:]]+[^=]+=//; s/^"//; s/"$//')
                case "$key" in
                    SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA|SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER|SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR|SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER|SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE)
                        eval "$key=\"$val\""
                        ;;
                esac
                ;;
        esac
    done < "${HOME}/.zshrc"
}

ensure_bridge_env() {
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

cleanup() {
    rm -f "$TMP_LOCKFILE" "$LEGACY_LOCKFILE"
    log "Shutdown signal received, cleaning up"
    exit 0
}

trap cleanup INT TERM

acquire_lock() {
    # Check both lock locations, preferring /tmp lock as authoritative.
    for lock in "$TMP_LOCKFILE" "$LEGACY_LOCKFILE"; do
        if [ -f "$lock" ]; then
            existing_pid=$(cat "$lock" 2>/dev/null || echo "")
            if [ -n "$existing_pid" ] && kill -0 "$existing_pid" 2>/dev/null; then
                log "ERROR: Another instance running (PID: $existing_pid via $lock)"
                exit 1
            else
                log "Removing stale lockfile $lock (PID $existing_pid gone)"
                rm -f "$lock"
            fi
        fi
    done

    echo $$ > "$TMP_LOCKFILE"
    echo $$ > "$LEGACY_LOCKFILE"
}

ensure_directories() {
    mkdir -p "$INBOX_DIR" "$IN_PROGRESS_DIR" "$DONE_DIR" "$FAILED_DIR" "$OUTBOX_DIR"
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

VALID_AGENTS="commander adjudicator cartographer psyche ajna dispatch"

extract_reply_to() {
    task_file="$1"
    raw=$(grep '^\*\*Reply-To\*\*:' "$task_file" 2>/dev/null | head -n1 | sed 's/.*: *//')
    # Validate against allowlist to prevent path traversal (Adjudicator audit)
    for valid in $VALID_AGENTS; do
        if [ "$raw" = "$valid" ]; then
            echo "$raw"
            return
        fi
    done
    if [ -n "$raw" ]; then
        log "WARN: reply_to '$raw' not in allowlist, ignoring"
    fi
    echo ""
}

extract_task_id() {
    basename "$1" .md
}

check_pane_for_rate_limit() {
    if [ -z "$TMUX_PANE" ]; then
        return 1
    fi
    recent=$($TMUX_BIN capture-pane -t "${TMUX_SESSION}:${TMUX_PANE}" -p -S -10 2>/dev/null || echo "")
    echo "$recent" | grep -qiE "rate limit|usage limit|high demand|quota exceeded" && return 0
    return 1
}

# Gemini CLI supports headless mode via -p/--prompt flag
is_gemini_agent() {
    [ "$AGENT_NAME" = "cartographer" ] && return 0
    return 1
}

GEMINI_BIN="/opt/homebrew/bin/gemini"

# Verify tmux pane exists before attempting dispatch (Adjudicator audit)
check_pane_exists() {
    if [ -z "$TMUX_PANE" ]; then
        return 1
    fi
    $TMUX_BIN has-session -t "${TMUX_SESSION}" 2>/dev/null || return 1
    # Target the specific window (e.g., "1" from "1.5"), not the active window
    local target_window; target_window=$(echo "$TMUX_PANE" | cut -d. -f1)
    local target_pane; target_pane=$(echo "$TMUX_PANE" | cut -d. -f2)
    $TMUX_BIN list-panes -t "${TMUX_SESSION}:${target_window}" -F '#{pane_index}' 2>/dev/null | grep -q "^${target_pane}$" 2>/dev/null
    return $?
}

send_prompt() {
    prompt="$1"

    # Gemini headless dispatch — doesn't need tmux pane at all
    if is_gemini_agent; then
        # Gemini uses headless mode (-p) instead of tmux send-keys
        # task_id is set by dispatch_task() in outer scope
        log "Gemini headless dispatch: running gemini -p -y -o text"
        local result_slug; result_slug=$(echo "$task_id" | sed 's/^TASK-//')
        local result_path="${OUTBOX_DIR}/RESULT-${AGENT_NAME}-${result_slug}.md"
        ( cd "${REPO_PATH}" && ${GEMINI_BIN} -p "$prompt" -y -o text > "${result_path}" 2>>"${LOGFILE}" ) &
        GEMINI_PID=$!
        log "Gemini headless PID: ${GEMINI_PID}"
        return 0
    fi

    # --- tmux-based agents below this point ---
    if [ -z "$TMUX_PANE" ]; then
        log "ERROR: No tmux pane specified"
        return 1
    fi

    # Check pane exists before attempting send (Adjudicator audit)
    if ! check_pane_exists; then
        log "ERROR: tmux pane ${TMUX_SESSION}:${TMUX_PANE} not found — transient failure"
        return 1
    fi

    # Wait for rate limit to clear
    retry=0
    while check_pane_for_rate_limit; do
        retry=$((retry + 1))
        if [ "$retry" -gt 10 ]; then
            log "ERROR: Rate limit persists after 10 retries (10 min)"
            return 1
        fi
        log "Rate limit detected, waiting 60s (retry $retry/10)..."
        sleep 60
    done

    # Truncate prompt if too long for tmux (safe limit ~2000 chars)
    if [ ${#prompt} -gt 2000 ]; then
        prompt=$(echo "$prompt" | head -c 1900)
        prompt="${prompt}... [truncated — see full task file in 10-IN_PROGRESS]"
    fi

    $TMUX_BIN send-keys -t "${TMUX_SESSION}:${TMUX_PANE}" "$prompt" Enter
    sleep 2
    # Some CLIs need a second Enter to submit pasted content
    $TMUX_BIN send-keys -t "${TMUX_SESSION}:${TMUX_PANE}" Enter
    return 0
}

dispatch_task() {
    task_file="$1"
    task_id=$(extract_task_id "$task_file")
    objective=$(extract_objective "$task_file")
    reply_to=$(extract_reply_to "$task_file")

    if [ -z "$objective" ]; then
        log "ERROR: No objective found in $task_file"
        return 1
    fi

    log "Dispatching: $task_id"

    # Move to IN_PROGRESS (resilient — Adjudicator audit)
    in_progress_path="${IN_PROGRESS_DIR}/$(basename "$task_file")"
    if ! mv "$task_file" "$in_progress_path" 2>/dev/null; then
        log "ERROR: Failed to move $task_file to IN_PROGRESS"
        return 1
    fi

    # Record state
    echo "${task_id}|${in_progress_path}|${reply_to}|$(date +%s)" > "$STATE_FILE"

    # Prefix with "IGNORE WORKTREE STATE" to prevent dirty-worktree panic
    full_prompt="READ-ONLY ANALYTICAL TASK. Ignore any dirty worktree state. ${objective} Write result to -OUTBOX/${AGENT_NAME}/RESULTS/RESULT-${AGENT_NAME}-$(echo "$task_id" | sed 's/^TASK-//').md"

    send_prompt "$full_prompt"
    send_rc=$?

    if [ "$send_rc" -eq 0 ]; then
        log "Dispatched successfully: $task_id"
        return 0
    elif [ "$send_rc" -eq 2 ]; then
        # Structural block (e.g. Gemini TUI) — re-queue instead of failing (Adjudicator audit)
        log "REQUEUE: $task_id — structural dispatch block, returning to INBOX"
        mv "$in_progress_path" "$task_file" 2>/dev/null || true
        rm -f "$STATE_FILE"
        return 1
    else
        # Transient failure — move to FAILED
        log "Dispatch failed: $task_id — moving to FAILED"
        mv "$in_progress_path" "${FAILED_DIR}/$(basename "$task_file")" 2>/dev/null || true
        echo "DISPATCH_FAILED: Agent rejected or structurally blocked" >> "${FAILED_DIR}/$(basename "$task_file")" 2>/dev/null || true
        rm -f "$STATE_FILE"
        return 1
    fi
}

check_completion() {
    if [ ! -f "$STATE_FILE" ]; then
        return 1
    fi

    task_id=$(cut -d'|' -f1 "$STATE_FILE")
    in_progress_path=$(cut -d'|' -f2 "$STATE_FILE")
    reply_to=$(cut -d'|' -f3 "$STATE_FILE")
    start_time=$(cut -d'|' -f4 "$STATE_FILE")

    current_time=$(date +%s)
    elapsed=$((current_time - start_time))

    # Check for RESULT file in outbox
    result_slug=$(echo "$task_id" | sed 's/^TASK-//')
    result_file="${OUTBOX_DIR}/RESULT-${AGENT_NAME}-${result_slug}.md"

    if [ -f "$result_file" ]; then
        result_size=$(wc -c < "$result_file" 2>/dev/null || echo 0)
        if [ "$result_size" -lt 100 ]; then
            log "WARN: Result file exists but is suspiciously small (${result_size} bytes) — may be stub"
        fi
        log "Task completed: $task_id (${elapsed}s, ${result_size} bytes)"

        mv "$in_progress_path" "${DONE_DIR}/$(basename "$in_progress_path")" 2>/dev/null || log "WARN: Could not move to DONE (file may already be moved)"

        # Send CONFIRM to Reply-To agent
        if [ -n "$reply_to" ] && [ "$reply_to" != "dispatch" ]; then
            confirm_dir="${REPO_PATH}/-INBOX/${reply_to}/00-INBOX0"
            mkdir -p "$confirm_dir"
            cat > "${confirm_dir}/CONFIRM-${AGENT_NAME}-${result_slug}.md" <<CONFIRM_EOF
# CONFIRM-${AGENT_NAME}-${result_slug}

**Kind**: CONFIRM
**Task**: ${task_id}.md
**From-Agent**: ${AGENT_NAME}
**To-Agent**: ${reply_to}
**Status**: COMPLETE
**Exit-Code**: 0
**Completed-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')
**Result-Path**: ${result_file}
CONFIRM_EOF
            log "Sent CONFIRM to ${reply_to}"

            # Neural Bridge: SCP CONFIRM to originator's machine if remote
            REPLY_UPPER=$(echo "$reply_to" | tr '[:lower:]' '[:upper:]')
            REMOTE_VAR="SYNCRESCENDENCE_REMOTE_AGENT_HOST_${REPLY_UPPER}"
            REMOTE_HOST="${!REMOTE_VAR:-local}"
            if [ -n "$REMOTE_HOST" ] && [ "$REMOTE_HOST" != "local" ] && [ "$REMOTE_HOST" != "localhost" ]; then
                confirm_file="${confirm_dir}/CONFIRM-${AGENT_NAME}-${result_slug}.md"
                if scp -q -o BatchMode=yes -o ConnectTimeout=5 "$confirm_file"                     "$REMOTE_HOST:~/Desktop/syncrescendence/-INBOX/${reply_to}/00-INBOX0/" 2>/dev/null; then
                    log "Neural Bridge: CONFIRM routed to ${REMOTE_HOST} for ${reply_to}"
                else
                    log "WARN: Neural Bridge SCP failed for CONFIRM to ${REMOTE_HOST}"
                fi
            fi
        fi

        rm -f "$STATE_FILE"
        return 0
    fi

    # Check timeout
    if [ "$elapsed" -gt "$TASK_TIMEOUT" ]; then
        log "TIMEOUT: $task_id (${elapsed}s exceeded ${TASK_TIMEOUT}s limit)"
        mv "$in_progress_path" "${FAILED_DIR}/$(basename "$in_progress_path")" 2>/dev/null || true
        echo "TIMEOUT: Exceeded ${TASK_TIMEOUT}s" >> "${FAILED_DIR}/$(basename "$in_progress_path")" 2>/dev/null || true
        rm -f "$STATE_FILE"
        return 0
    fi

    return 1
}

recover_state() {
    if [ ! -f "$STATE_FILE" ]; then
        return 0
    fi
    task_id=$(cut -d'|' -f1 "$STATE_FILE")
    in_progress_path=$(cut -d'|' -f2 "$STATE_FILE")
    if [ ! -f "$in_progress_path" ]; then
        log "WARN: Stale state for missing task file, clearing"
        rm -f "$STATE_FILE"
        return 0
    fi
    log "Recovered in-progress task: $task_id"
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

    while true; do
        # If a task is in progress, check for completion
        if [ -f "$STATE_FILE" ]; then
            check_completion
            sleep 5
            continue
        fi

        # Look for oldest pending task
        task_file=$(find "$INBOX_DIR" -maxdepth 1 -name "TASK-*.md" -type f 2>/dev/null | sort | head -n1)

        if [ -n "$task_file" ]; then
            dispatch_task "$task_file" || true
        fi

        sleep "$POLL_INTERVAL"
    done
}

main
