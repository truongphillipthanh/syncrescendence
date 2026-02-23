#!/usr/bin/env bash
# proactive_orchestrator.sh — Autonomous work generation for idle agents
# Hardened with Layer-0 integrity gate, circuit breaker, and hard budgets.

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${SYNCRESCENDENCE_PATH:-$(cd "${SCRIPT_DIR}/../.." && pwd)}"
INBOX_ROOT="${REPO_DIR}/-INBOX"
STATE_DIR="${REPO_DIR}/orchestration/state"
SCRIPTS_DIR="${REPO_DIR}/orchestration/scripts"
HEALTH_FILE="${STATE_DIR}/DYN-CONSTELLATION_HEALTH.md"
DEFERRED_FILE="${STATE_DIR}/DYN-DEFERRED_COMMITMENTS.md"
ORCHESTRATOR_LOG="${HOME}/Library/Logs/syncrescendence-orchestrator.log"
LOCKFILE="/tmp/proactive_orchestrator.lock"
INTEGRITY_GATE_SCRIPT="${SCRIPTS_DIR}/repo_integrity_gate.sh"

BREAKER_DIR="${STATE_DIR}/breakers"
BREAKER_FILE="${BREAKER_DIR}/orchestration.breaker"
BUDGET_DIR="${STATE_DIR}/budgets"

# Thresholds
STALE_THRESHOLD="${SYNCRESCENDENCE_STALE_THRESHOLD_S:-1800}"
RETRY_MAX_AGE="${SYNCRESCENDENCE_RETRY_MAX_AGE_S:-86400}"
RETRY_COOLDOWN="${SYNCRESCENDENCE_RETRY_COOLDOWN_S:-600}"
MAX_DISPATCHES_PER_CYCLE_BASE="${SYNCRESCENDENCE_MAX_DISPATCHES_PER_CYCLE:-3}"
MAX_NET_NEW_TASKS_PER_DAY="${SYNCRESCENDENCE_MAX_NEW_TASKS_PER_DAY:-18}"
MAX_FAILED_TASKS_TOTAL="${SYNCRESCENDENCE_MAX_FAILED_TASKS_TOTAL:-25}"
IDLE_TASK_COOLDOWN="${SYNCRESCENDENCE_IDLE_TASK_COOLDOWN_S:-900}"
BREAKER_COOLDOWN_S="${SYNCRESCENDENCE_BREAKER_COOLDOWN_S:-300}"

AGENTS=(commander adjudicator psyche cartographer ajna)

log() {
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[${timestamp}] [orchestrator] $*" >> "$ORCHESTRATOR_LOG" 2>/dev/null || true
}

log_action() {
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[${timestamp}] [orchestrator] ACTION: $*" >> "$ORCHESTRATOR_LOG" 2>/dev/null || true
}

acquire_lock() {
    if [ -f "$LOCKFILE" ]; then
        local existing_pid
        existing_pid=$(cat "$LOCKFILE" 2>/dev/null || echo "")
        if [ -n "$existing_pid" ] && kill -0 "$existing_pid" 2>/dev/null; then
            log "Another instance running (PID: ${existing_pid}), exiting"
            exit 0
        fi
        log "Stale lockfile found (PID: ${existing_pid}), removing"
        rm -f "$LOCKFILE"
    fi
    echo $$ > "$LOCKFILE"
}

release_lock() {
    rm -f "$LOCKFILE"
}

trap release_lock EXIT

now_epoch() {
    date +%s
}

today_date() {
    date '+%Y%m%d'
}

file_age_seconds() {
    local file="$1"
    local file_mtime
    file_mtime=$(stat -f %m "$file" 2>/dev/null || echo "0")
    echo $(( $(now_epoch) - file_mtime ))
}

ensure_state_dirs() {
    mkdir -p "$STATE_DIR" "$BREAKER_DIR" "$BUDGET_DIR"
}

write_breaker_state() {
    local state="$1"
    local reason="$2"
    local cooldown_until="${3:-0}"

    cat > "$BREAKER_FILE" <<BRK
state=${state}
reason=${reason}
changed_at_unix=$(now_epoch)
changed_at_iso=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
cooldown_until=${cooldown_until}
BRK
    log_action "BREAKER_${state}: ${reason} [caller=${FUNCNAME[1]:-unknown} pid=$$]"
}

load_breaker_state() {
    BREAKER_STATE="CLOSED"
    BREAKER_REASON=""
    BREAKER_COOLDOWN_UNTIL=0

    [ -f "$BREAKER_FILE" ] || return 0
    BREAKER_STATE=$(grep '^state=' "$BREAKER_FILE" 2>/dev/null | head -n1 | cut -d'=' -f2)
    BREAKER_REASON=$(grep '^reason=' "$BREAKER_FILE" 2>/dev/null | head -n1 | cut -d'=' -f2-)
    BREAKER_COOLDOWN_UNTIL=$(grep '^cooldown_until=' "$BREAKER_FILE" 2>/dev/null | head -n1 | cut -d'=' -f2)
    [ -z "$BREAKER_STATE" ] && BREAKER_STATE="CLOSED"
    [ -z "$BREAKER_COOLDOWN_UNTIL" ] && BREAKER_COOLDOWN_UNTIL=0
}

integrity_gate_ok() {
    if [ ! -x "$INTEGRITY_GATE_SCRIPT" ]; then
        log "WARN: integrity gate script missing, skipping hard gate"
        return 0
    fi

    # Pre-clean Finder artifacts from git ref namespace before gate runs
    find "${REPO_DIR}/.git/refs" "${REPO_DIR}/.git/logs/refs" -name '.DS_Store' -delete 2>/dev/null || true

    bash "$INTEGRITY_GATE_SCRIPT" --repo "$REPO_DIR" --context orchestrator --no-incident >/dev/null 2>&1
}

enforce_integrity() {
    if integrity_gate_ok; then
        return 0
    fi

    cooldown_until=$(( $(now_epoch) + BREAKER_COOLDOWN_S ))
    write_breaker_state "OPEN" "integrity_gate_failed" "$cooldown_until"
    return 1
}

failed_task_count_total() {
    local total=0
    local c
    for agent in "${AGENTS[@]}"; do
        c=$(find "${INBOX_ROOT}/${agent}/50_FAILED" -maxdepth 1 -name 'TASK-*.md' 2>/dev/null | wc -l | tr -d ' ')
        [ -z "$c" ] && c=0
        total=$((total + c))
    done
    echo "$total"
}

current_daily_dispatch_count() {
    local key
    key=$(today_date)
    local f="${BUDGET_DIR}/dispatch-${key}.count"
    if [ -f "$f" ]; then
        cat "$f" 2>/dev/null | tr -cd '0-9'
    else
        echo 0
    fi
}

increment_daily_dispatch_count() {
    local key
    key=$(today_date)
    local f="${BUDGET_DIR}/dispatch-${key}.count"
    local n
    n=$(current_daily_dispatch_count)
    [ -z "$n" ] && n=0
    n=$((n + 1))
    echo "$n" > "$f"
}

capacity_allows_dispatch() {
    local current
    current=$(current_daily_dispatch_count)
    [ -z "$current" ] && current=0
    [ "$current" -lt "$MAX_NET_NEW_TASKS_PER_DAY" ]
}

transition_breaker_for_cycle() {
    local now
    now=$(now_epoch)

    case "$BREAKER_STATE" in
        OPEN)
            if [ "$now" -ge "$BREAKER_COOLDOWN_UNTIL" ]; then
                write_breaker_state "HALF_OPEN" "cooldown_elapsed" 0
                BREAKER_STATE="HALF_OPEN"
            fi
            ;;
    esac
}

max_dispatches_for_state() {
    case "$BREAKER_STATE" in
        OPEN)
            echo 0
            ;;
        HALF_OPEN)
            echo 1
            ;;
        *)
            echo "$MAX_DISPATCHES_PER_CYCLE_BASE"
            ;;
    esac
}

task_exists_for_agent() {
    local agent="$1"
    local slug="$2"
    local agent_dir="${INBOX_ROOT}/${agent}"

    for folder in "00-INBOX0" "10-IN_PROGRESS"; do
        if find "${agent_dir}/${folder}" -maxdepth 1 -name "*${slug}*" 2>/dev/null | head -1 | grep -q .; then
            return 0
        fi
    done

    local today
    today=$(today_date)
    if find "${agent_dir}/40-DONE" -maxdepth 1 -name "TASK-${today}-*${slug}*" 2>/dev/null | head -1 | grep -q .; then
        return 0
    fi

    return 1
}

count_pending() {
    local agent="$1"
    local inbox="${INBOX_ROOT}/${agent}/00-INBOX0"
    [ -d "$inbox" ] || { echo 0; return; }
    find "$inbox" -maxdepth 1 -name 'TASK-*.md' 2>/dev/null | wc -l | tr -d ' '
}

count_inprogress() {
    local agent="$1"
    local dir="${INBOX_ROOT}/${agent}/10-IN_PROGRESS"
    [ -d "$dir" ] || { echo 0; return; }
    find "$dir" -maxdepth 1 -name 'TASK-*.md' 2>/dev/null | wc -l | tr -d ' '
}

cleanup_stale_inprogress() {
    log "--- Checking stale IN_PROGRESS tasks ---"
    local moved=0

    for agent in "${AGENTS[@]}"; do
        local inprogress_dir="${INBOX_ROOT}/${agent}/10-IN_PROGRESS"
        [ -d "$inprogress_dir" ] || continue

        while IFS= read -r -d '' task; do
            local age
            age=$(file_age_seconds "$task")
            local task_name
            task_name=$(basename "$task")

            if [ "$age" -gt "$STALE_THRESHOLD" ]; then
                local failed_dir="${INBOX_ROOT}/${agent}/50_FAILED"
                mkdir -p "$failed_dir"

                {
                    echo ""
                    echo "---"
                    echo "**Failure-Code**: STALE_TIMEOUT"
                    echo "**Failure-Class**: timeout"
                    echo "**Failure-Retryable**: true"
                    echo "**Failure-Reason**: stale_in_progress_timeout"
                    echo "**Failed-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
                    echo "**Stale-Duration**: ${age}s (threshold: ${STALE_THRESHOLD}s)"
                    echo "**Moved-By**: proactive_orchestrator.sh"
                } >> "$task"

                mv "$task" "$failed_dir/"
                log_action "STALE_TIMEOUT: ${agent}/${task_name} (age ${age}s)"

                local state_file="${INBOX_ROOT}/${agent}/.current_task"
                if [ -f "$state_file" ] && grep -q "$task_name" "$state_file" 2>/dev/null; then
                    rm -f "$state_file"
                fi

                moved=$((moved + 1))
            fi
        done < <(find "$inprogress_dir" -maxdepth 1 -name 'TASK-*.md' -type f -print0 2>/dev/null)
    done

    log "Stale cleanup complete: ${moved} tasks moved to FAILED"
}

write_constellation_state() {
    local state_file="${STATE_DIR}/DYN-CONSTELLATION_STATE.md"
    local tmp_file="${state_file}.tmp"
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    {
        echo "# Constellation State"
        echo "Generated: ${timestamp}"
        echo ""
        echo "| Agent | Inbox0 | InProgress | Failed | Done (24h) | Health |"
        echo "|-------|--------|------------|--------|------------|--------|"

        for agent in "${AGENTS[@]}"; do
            local inbox0 inprog failed done24 health
            inbox0=$(find "$INBOX_ROOT/$agent/00-INBOX0" -maxdepth 1 -name 'TASK-*.md' 2>/dev/null | wc -l | tr -d ' ')
            inprog=$(find "$INBOX_ROOT/$agent/10-IN_PROGRESS" -maxdepth 1 -name 'TASK-*.md' 2>/dev/null | wc -l | tr -d ' ')
            failed=$(find "$INBOX_ROOT/$agent/50_FAILED" -maxdepth 1 -name 'TASK-*.md' 2>/dev/null | wc -l | tr -d ' ')
            done24=$(find "$INBOX_ROOT/$agent/40-DONE" -maxdepth 1 -name 'TASK-*.md' -mtime -1 2>/dev/null | wc -l | tr -d ' ')
            health=$(grep -i "| ${agent}" "$HEALTH_FILE" 2>/dev/null | head -1 | awk -F'|' '{print $5}' | xargs 2>/dev/null || echo "UNKNOWN")
            [ -z "$health" ] && health="UNKNOWN"
            echo "| $agent | $inbox0 | $inprog | $failed | $done24 | $health |"
        done

        echo ""
        echo "## Queued Work"
        local has_queued=0
        for agent in "${AGENTS[@]}"; do
            local queue_dir="${INBOX_ROOT}/${agent}/00-INBOX0"
            [ -d "$queue_dir" ] || continue
            local listed=0

            while IFS= read -r -d '' t; do
                if [ "$listed" -eq 0 ]; then
                    has_queued=1
                    listed=1
                    echo "### $agent"
                fi
                echo "- $(basename "$t")"
            done < <(find "$queue_dir" -maxdepth 1 -name 'TASK-*.md' -type f -print0 2>/dev/null)
        done
        [ "$has_queued" -eq 0 ] && echo "_No queued tasks._"
    } > "$tmp_file"

    mv "$tmp_file" "$state_file"
    log "STATE: Written constellation state"
}

retry_failed_tasks() {
    log "--- Checking retryable failed tasks ---"
    local retried=0

    for agent in "${AGENTS[@]}"; do
        local failed_dir="${INBOX_ROOT}/${agent}/50_FAILED"
        [ -d "$failed_dir" ] || continue

        local pending
        pending=$(count_pending "$agent")
        local inprog
        inprog=$(count_inprogress "$agent")
        if [ "$pending" -gt 2 ] || [ "$inprog" -gt 0 ]; then
            continue
        fi

        while IFS= read -r -d '' task; do
            local task_name age retry_count retryable
            task_name=$(basename "$task")
            age=$(file_age_seconds "$task")

            [ "$age" -gt "$RETRY_MAX_AGE" ] && continue
            [ "$age" -lt "$RETRY_COOLDOWN" ] && continue

            retry_count=$(sed -n 's/^\*\*Retry-Count\*\*:[[:space:]]*//p' "$task" 2>/dev/null | tail -1 | tr -cd '0-9')
            [ -z "$retry_count" ] && retry_count=0
            [ "$retry_count" -ge 3 ] && continue

            retryable=$(sed -n 's/^\*\*Failure-Retryable\*\*:[[:space:]]*//p' "$task" 2>/dev/null | tail -1 | tr '[:upper:]' '[:lower:]')
            [ "$retryable" != "true" ] && [ "$retryable" != "yes" ] && continue

            local inbox_dir="${INBOX_ROOT}/${agent}/00-INBOX0"
            mkdir -p "$inbox_dir"
            retry_count=$((retry_count + 1))

            {
                echo ""
                echo "**Retry-Count**: ${retry_count}"
                echo "**Retried-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
                echo "**Retried-By**: proactive_orchestrator.sh"
            } >> "$task"

            sed -i '' 's/^\*\*Status\*\*: .*/**Status**: PENDING/' "$task" 2>/dev/null || true
            sed -i '' 's/^\*\*Kanban\*\*: .*/**Kanban**: INBOX0/' "$task" 2>/dev/null || true

            mv "$task" "$inbox_dir/"
            retried=$((retried + 1))
            log_action "RETRY: ${agent}/${task_name} (attempt ${retry_count})"

            [ "$retried" -ge 2 ] && break 2
        done < <(find "$failed_dir" -maxdepth 1 -name 'TASK-*.md' -type f -print0 2>/dev/null)
    done

    log "Retry scan complete: ${retried} tasks moved back to INBOX0"
}

get_agent_status() {
    local agent="$1"
    [ -f "$HEALTH_FILE" ] || { echo "unknown"; return; }

    local status
    status=$(grep -i "| ${agent}" "$HEALTH_FILE" 2>/dev/null | head -1 | awk -F'|' '{print $5}' | tr -d ' ' | tr '[:upper:]' '[:lower:]')
    echo "${status:-unknown}"
}

agent_capability_allows() {
    local agent="$1"
    local class="$2"

    case "$agent:$class" in
        cartographer:sensing|cartographer:survey) return 0 ;;
        cartographer:implementation|cartographer:coding) return 1 ;;
        adjudicator:verification|adjudicator:audit|adjudicator:sensing) return 0 ;;
        psyche:implementation|psyche:coding|psyche:infra) return 0 ;;
        commander:implementation|commander:infra|commander:coordination) return 0 ;;
        ajna:sensing|ajna:coordination) return 0 ;;
        *) return 0 ;;
    esac
}

dispatch_task() {
    local agent="$1"
    local slug="$2"
    local description="$3"
    local class="${4:-coordination}"

    if ! capacity_allows_dispatch; then
        log "DISPATCH_BUDGET: daily cap reached (${MAX_NET_NEW_TASKS_PER_DAY})"
        return 1
    fi

    if ! agent_capability_allows "$agent" "$class"; then
        log "ROUTING_POLICY: blocked ${agent}/${slug} class=${class}"
        return 1
    fi

    if [ -f "${SCRIPTS_DIR}/dispatch.sh" ]; then
        if bash "${SCRIPTS_DIR}/dispatch.sh" "$agent" "$slug" "$description" "" "TASK" "orchestrator" >/dev/null 2>&1; then
            increment_daily_dispatch_count
            log_action "DISPATCH: ${agent}/${slug} class=${class}"
            return 0
        fi
        log "WARN: dispatch.sh failed for ${agent}/${slug}"
        return 1
    fi

    local today
    today=$(today_date)
    local task_file="${INBOX_ROOT}/${agent}/00-INBOX0/TASK-${today}-${slug}.md"
    local fingerprint
    fingerprint=$(git -C "$REPO_DIR" rev-parse --short HEAD 2>/dev/null || echo "unknown")

    cat > "$task_file" <<TASK_EOF
# TASK-${today}-${slug}

**From**: Proactive Orchestrator (automated)
**To**: ${agent}
**Reply-To**: commander
**CC**: commander
**Issued**: $(date '+%Y-%m-%d %H:%M:%S')
**Fingerprint**: ${fingerprint}
**Kind**: TASK
**Priority**: P2
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: —
**Claimed-At**: —
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**Receipts-To**: -OUTBOX/${agent}/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10
**Generated-By**: proactive_orchestrator.sh
**Task-Class**: ${class}

---

## Objective

${description}
TASK_EOF

    increment_daily_dispatch_count
    log_action "DISPATCH_FALLBACK: ${agent}/${slug} class=${class}"
    return 0
}

dispatch_idle_work() {
    log "--- Checking for idle agents ---"
    local dispatched=0
    local max_dispatch
    max_dispatch=$(max_dispatches_for_state)

    [ "$max_dispatch" -le 0 ] && {
        log "BREAKER_OPEN: idle dispatch disabled"
        echo 0
        return
    }

    if [ ! -f "$HEALTH_FILE" ]; then
        log "WARN: Health file missing — cannot determine agent status"
        echo 0
        return
    fi

    local health_age
    health_age=$(file_age_seconds "$HEALTH_FILE")
    if [ "$health_age" -gt 300 ]; then
        log "WARN: Health file stale (${health_age}s old)"
    fi

    for agent in "${AGENTS[@]}"; do
        [ "$agent" = "commander" ] && continue

        local status
        status=$(get_agent_status "$agent")
        if [ "$status" != "idle" ] && [ "$status" != "stale" ]; then
            continue
        fi

        local pending inprog
        pending=$(count_pending "$agent")
        inprog=$(count_inprogress "$agent")
        [ "$pending" -gt 0 ] && continue
        [ "$inprog" -gt 0 ] && continue

        local last_dispatch_marker="/tmp/orchestrator_last_idle_${agent}"
        if [ -f "$last_dispatch_marker" ]; then
            local marker_age
            marker_age=$(file_age_seconds "$last_dispatch_marker")
            [ "$marker_age" -lt "$IDLE_TASK_COOLDOWN" ] && continue
        fi

        local ok=1
        case "$agent" in
            adjudicator)
                task_exists_for_agent "$agent" "ecosystem_health" || dispatch_task "$agent" "ecosystem_health" "Run ecosystem health audit: verify launchd agents, Docker containers, tmux panes, auto-ingest loop PIDs, and stale locks. Report anomalies with evidence." "audit" || ok=0
                ;;
            cartographer)
                task_exists_for_agent "$agent" "corpus_freshness" || dispatch_task "$agent" "corpus_freshness" "Survey corpus freshness and broken references. Report stale files and missing links." "sensing" || ok=0
                ;;
            psyche)
                task_exists_for_agent "$agent" "infrastructure_audit" || dispatch_task "$agent" "infrastructure_audit" "Run infrastructure coherence audit: launchd templates vs deployed, watchdog status, Docker restart policies, auto-ingest supervisor status." "infra" || ok=0
                ;;
            ajna)
                task_exists_for_agent "$agent" "mba_health" || dispatch_task "$agent" "mba_health" "Run MBA health self-check: ssh mini hostname, git sync status, launchd agents, and orchestration drift report." "coordination" || ok=0
                ;;
        esac

        if [ "$ok" -eq 1 ]; then
            touch "$last_dispatch_marker"
            dispatched=$((dispatched + 1))
        fi

        [ "$dispatched" -ge "$max_dispatch" ] && break
    done

    log "Idle dispatch complete: ${dispatched} tasks generated"
    echo "$dispatched"
}

scan_deferred_commitments() {
    log "--- Scanning deferred commitments ---"
    [ -f "$DEFERRED_FILE" ] || { log "No deferred commitments file"; return; }

    local today_iso
    today_iso=$(date '+%Y-%m-%d')
    local overdue_count=0
    local dispatched=0

    while IFS='|' read -r _ id _ commitment pri status target _; do
        id=$(echo "$id" | tr -d ' ')
        status=$(echo "$status" | tr -d ' ')
        target=$(echo "$target" | tr -d ' ')
        pri=$(echo "$pri" | tr -d ' ')
        commitment=$(echo "$commitment" | sed 's/^ *//;s/ *$//')

        [ "$status" = "OPEN" ] || continue
        [[ "$target" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || continue

        if [[ "$target" < "$today_iso" ]] || [[ "$target" = "$today_iso" ]]; then
            overdue_count=$((overdue_count + 1))
            if [ "$pri" = "P0" ] && [ "$dispatched" -lt 1 ]; then
                slug=$(echo "$id" | tr '[:upper:]' '[:lower:]' | tr -c '[:alnum:]' '_')
                slug="deferred_${slug}_followup"
                if ! task_exists_for_agent "adjudicator" "$slug"; then
                    if dispatch_task "adjudicator" "$slug" "OVERDUE DEFERRED COMMITMENT: ${id} — ${commitment}. Target ${target}. Assess status, blockers, and next concrete action." "verification"; then
                        dispatched=$((dispatched + 1))
                    fi
                fi
            fi
        fi
    done < <(grep '^|' "$DEFERRED_FILE" 2>/dev/null | grep -v '^| ID\|^| --\|^-')

    log "Deferred scan complete: ${overdue_count} overdue items, ${dispatched} tasks dispatched"
}

inbox_hygiene() {
    log "--- Running inbox hygiene ---"

    for agent in "${AGENTS[@]}"; do
        local inbox="${INBOX_ROOT}/${agent}/00-INBOX0"
        [ -d "$inbox" ] || continue

        local stale_confirms=0
        while IFS= read -r -d '' file; do
            local age
            age=$(file_age_seconds "$file")
            [ "$age" -gt 172800 ] && stale_confirms=$((stale_confirms + 1))
        done < <(find "$inbox" -maxdepth 1 \( -name 'CONFIRM-*.md' -o -name 'RESULT-*.md' -o -name 'EXECLOG-*.log' \) -type f -print0 2>/dev/null)

        if [ "$stale_confirms" -gt 10 ]; then
            log "WARN: ${agent} INBOX0 has ${stale_confirms} stale confirmation artifacts"
        fi

        local state_file="${INBOX_ROOT}/${agent}/.current_task"
        if [ -f "$state_file" ]; then
            local task_path
            task_path=$(cut -d'|' -f2 "$state_file" 2>/dev/null || echo "")
            if [ -n "$task_path" ] && [ ! -f "$task_path" ]; then
                log "WARN: ${agent} has orphaned state file"
            fi
        fi
    done

    log "Inbox hygiene complete"
}

write_status_summary() {
    local duration="$1"
    local summary_file="${STATE_DIR}/.orchestrator_last_run"
    local failed_total
    failed_total=$(failed_task_count_total)

    cat > "$summary_file" <<EOF_SUM
# Proactive Orchestrator — Last Run
timestamp: $(date -u '+%Y-%m-%dT%H:%M:%SZ')
pid: $$
cycle_duration_s: ${duration}
breaker_state: ${BREAKER_STATE}
failed_tasks_total: ${failed_total}
daily_dispatch_count: $(current_daily_dispatch_count)
EOF_SUM
}

main() {
    acquire_lock
    ensure_state_dirs

    local start_time
    start_time=$(now_epoch)

    log "=== Proactive Orchestrator cycle start ==="

    load_breaker_state
    transition_breaker_for_cycle

    if ! enforce_integrity; then
        write_constellation_state
        write_status_summary "$(( $(now_epoch) - start_time ))"
        log "Cycle terminated by integrity gate"
        return 1
    fi

    local failed_total
    failed_total=$(failed_task_count_total)
    if [ "$failed_total" -gt "$MAX_FAILED_TASKS_TOTAL" ]; then
        write_breaker_state "OPEN" "failed_task_backlog_${failed_total}" "$(( $(now_epoch) + BREAKER_COOLDOWN_S ))"
        BREAKER_STATE="OPEN"
        log "Breaker opened due to failed backlog (${failed_total} > ${MAX_FAILED_TASKS_TOTAL})"
    fi

    cleanup_stale_inprogress
    write_constellation_state
    retry_failed_tasks

    dispatched_count=0
    if [ "$BREAKER_STATE" != "OPEN" ]; then
        dispatched_count=$(dispatch_idle_work)
        scan_deferred_commitments
    else
        log "BREAKER_OPEN: skipping dispatch and deferred scans"
    fi

    inbox_hygiene

    if [ "$BREAKER_STATE" = "HALF_OPEN" ] && [ "$dispatched_count" -ge 0 ]; then
        write_breaker_state "CLOSED" "half_open_cycle_passed" 0
        BREAKER_STATE="CLOSED"
    fi

    local end_time
    end_time=$(now_epoch)
    local duration=$(( end_time - start_time ))

    write_status_summary "$duration"
    log "=== Proactive Orchestrator cycle complete (${duration}s) ==="
}

main "$@"
