#!/usr/bin/env bash
# proactive_orchestrator.sh — Autonomous work generation for idle agents
# =====================================================================
# Runs every 5 minutes via launchd (com.syncrescendence.proactive-orchestrator).
# This is the constellation's "prefrontal cortex" — the missing brain that
# generates work when agents are idle instead of waiting for Commander dispatch.
#
# Features:
#   1. Stale IN_PROGRESS cleanup   → moves timed-out tasks to 50_FAILED
#   2. Cross-agent awareness state → DYN-CONSTELLATION_STATE.md
#   3. Retryable failed tasks      → moves eligible failures back to INBOX0
#   4. Idle agent work generation   → dispatches health/maintenance tasks
#   5. Deferred commitment scanning → generates tasks for overdue items
#   6. Inbox hygiene               → detects stale receipts, orphaned state
#
# Safety:
#   - Idempotent: checks for existing pending/in-progress tasks before dispatching
#   - Non-destructive: only moves files between kanban folders, never deletes
#   - Lock-guarded: single instance via PID lockfile
#   - Read-only on scripts: does NOT modify auto_ingest_loop.sh or watchdog
#
# IMPORTANT: This is a NEW script. Does NOT modify auto_ingest_loop.sh or
# constellation_watchdog.sh. Operates independently.
#
# Dependencies: dispatch.sh (for task creation), DYN-CONSTELLATION_HEALTH.md
# =====================================================================

set -euo pipefail

# === CONSTANTS ===
REPO_DIR="${HOME}/Desktop/syncrescendence"
INBOX_ROOT="${REPO_DIR}/-INBOX"
STATE_DIR="${REPO_DIR}/00-ORCHESTRATION/state"
SCRIPTS_DIR="${REPO_DIR}/00-ORCHESTRATION/scripts"
HEALTH_FILE="${STATE_DIR}/DYN-CONSTELLATION_HEALTH.md"
DEFERRED_FILE="${STATE_DIR}/DYN-DEFERRED_COMMITMENTS.md"
ORCHESTRATOR_LOG="${HOME}/Library/Logs/syncrescendence-orchestrator.log"
LOCKFILE="/tmp/proactive_orchestrator.lock"

# Thresholds
STALE_THRESHOLD=1800       # 30 minutes — task in-progress timeout
RETRY_MAX_AGE=86400        # 24 hours — don't retry tasks older than this
RETRY_COOLDOWN=600         # 10 minutes — minimum time before retrying a failed task
MAX_DISPATCHES_PER_CYCLE=3 # Cap work generation to prevent flooding
IDLE_TASK_COOLDOWN=900     # 15 minutes — don't re-dispatch idle tasks too quickly

# Agents known to the constellation
AGENTS=(commander adjudicator psyche cartographer ajna)

# Agent → role mapping for task generation
declare -A AGENT_ROLES=(
    [adjudicator]="CQO"
    [cartographer]="CIO"
    [psyche]="CTO"
    [commander]="COO"
    [ajna]="CSO"
)

# === LOGGING ===
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

# === LOCK MANAGEMENT ===
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

# === UTILITY ===
now_epoch() {
    date +%s
}

file_age_seconds() {
    local file="$1"
    local file_mtime
    file_mtime=$(stat -f %m "$file" 2>/dev/null || echo "0")
    echo $(( $(now_epoch) - file_mtime ))
}

today_date() {
    date '+%Y%m%d'
}

# Check if a task with a given slug already exists in an agent's pipeline
task_exists_for_agent() {
    local agent="$1"
    local slug="$2"
    local agent_dir="${INBOX_ROOT}/${agent}"

    # Check INBOX0, IN_PROGRESS, and recent DONE (last 24h)
    for folder in "00-INBOX0" "10-IN_PROGRESS"; do
        if ls "${agent_dir}/${folder}/"*"${slug}"* 2>/dev/null | head -1 | grep -q .; then
            return 0
        fi
    done

    # Check DONE from today (avoid re-dispatching recently completed work)
    local today
    today=$(today_date)
    if ls "${agent_dir}/40-DONE/TASK-${today}-"*"${slug}"* 2>/dev/null | head -1 | grep -q .; then
        return 0
    fi

    return 1
}

# Count pending tasks for an agent
count_pending() {
    local agent="$1"
    local inbox="${INBOX_ROOT}/${agent}/00-INBOX0"
    [ -d "$inbox" ] || { echo 0; return; }
    find "$inbox" -maxdepth 1 -name "TASK-*.md" 2>/dev/null | wc -l | tr -d ' '
}

# Count in-progress tasks for an agent
count_inprogress() {
    local agent="$1"
    local dir="${INBOX_ROOT}/${agent}/10-IN_PROGRESS"
    [ -d "$dir" ] || { echo 0; return; }
    find "$dir" -maxdepth 1 -name "TASK-*.md" 2>/dev/null | wc -l | tr -d ' '
}

# === FEATURE 1: STALE IN_PROGRESS CLEANUP ===
cleanup_stale_inprogress() {
    log "--- Checking stale IN_PROGRESS tasks ---"
    local moved=0

    for agent in "${AGENTS[@]}"; do
        local inprogress_dir="${INBOX_ROOT}/${agent}/10-IN_PROGRESS"
        [ -d "$inprogress_dir" ] || continue

        for task in "$inprogress_dir"/TASK-*.md; do
            [ -f "$task" ] || continue

            local age
            age=$(file_age_seconds "$task")
            local task_name
            task_name=$(basename "$task")

            if [ "$age" -gt "$STALE_THRESHOLD" ]; then
                local failed_dir="${INBOX_ROOT}/${agent}/50_FAILED"
                mkdir -p "$failed_dir"

                # Append failure metadata to the task file before moving
                {
                    echo ""
                    echo "---"
                    echo "**Failure-Reason**: stale_in_progress_timeout"
                    echo "**Failed-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
                    echo "**Stale-Duration**: ${age}s (threshold: ${STALE_THRESHOLD}s)"
                    echo "**Moved-By**: proactive_orchestrator.sh"
                } >> "$task"

                mv "$task" "$failed_dir/"
                log_action "STALE_TIMEOUT: ${agent}/${task_name} (age: ${age}s) → 50_FAILED"

                # Clean up state file if it references this task
                local state_file="${INBOX_ROOT}/${agent}/.current_task"
                if [ -f "$state_file" ] && grep -q "$task_name" "$state_file" 2>/dev/null; then
                    rm -f "$state_file"
                    log_action "Cleaned state file for ${agent} (stale task removed)"
                fi

                moved=$((moved + 1))
            fi
        done
    done

    log "Stale cleanup complete: ${moved} tasks moved to FAILED"
}

# === FEATURE 2: CROSS-AGENT AWARENESS STATE FILE ===
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
            inbox0=$(ls "$INBOX_ROOT/$agent/00-INBOX0"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            inprog=$(ls "$INBOX_ROOT/$agent/10-IN_PROGRESS"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            failed=$(ls "$INBOX_ROOT/$agent/50_FAILED"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            done24=$(find "$INBOX_ROOT/$agent/40-DONE" -name "TASK-*.md" -mtime -1 2>/dev/null | wc -l | tr -d ' ')
            health=$(grep -i "| ${agent}" "$HEALTH_FILE" 2>/dev/null | head -1 | awk -F'|' '{print $5}' | xargs 2>/dev/null || echo "UNKNOWN")
            [ -z "$health" ] && health="UNKNOWN"
            echo "| $agent | $inbox0 | $inprog | $failed | $done24 | $health |"
        done

        echo ""
        echo "## Queued Work"
        local has_queued=0
        for agent in "${AGENTS[@]}"; do
            local tasks
            tasks=$(ls "$INBOX_ROOT/$agent/00-INBOX0"/TASK-*.md 2>/dev/null || true)
            if [ -n "$tasks" ]; then
                has_queued=1
                echo "### $agent"
                for t in $tasks; do echo "- $(basename "$t")"; done
            fi
        done
        [ "$has_queued" -eq 0 ] && echo "_No queued tasks._"
    } > "$tmp_file"
    mv "$tmp_file" "$state_file"
    log "STATE: Written constellation state to $state_file"
}

# === FEATURE 3: RETRYABLE FAILED TASKS ===
retry_failed_tasks() {
    log "--- Checking retryable failed tasks ---"
    local retried=0

    for agent in "${AGENTS[@]}"; do
        local failed_dir="${INBOX_ROOT}/${agent}/50_FAILED"
        [ -d "$failed_dir" ] || continue

        # Don't retry if agent already has work queued
        local pending
        pending=$(count_pending "$agent")
        local inprog
        inprog=$(count_inprogress "$agent")
        if [ "$pending" -gt 2 ] || [ "$inprog" -gt 0 ]; then
            continue
        fi

        for task in "$failed_dir"/TASK-*.md; do
            [ -f "$task" ] || continue

            local task_name
            task_name=$(basename "$task")
            local age
            age=$(file_age_seconds "$task")

            # Skip tasks too old to retry
            if [ "$age" -gt "$RETRY_MAX_AGE" ]; then
                continue
            fi

            # Skip tasks that failed too recently (cooldown)
            if [ "$age" -lt "$RETRY_COOLDOWN" ]; then
                continue
            fi

            # Skip tasks already retried 3+ times
            if grep -q "Retry-Count: [3-9]" "$task" 2>/dev/null; then
                log "Skipping ${task_name}: max retries reached"
                continue
            fi

            # Skip tasks with non-retryable failure reasons
            if grep -q "Failure-Reason: policy_violation\|Failure-Reason: manual_cancel" "$task" 2>/dev/null; then
                continue
            fi

            # Eligible for retry — move back to INBOX0
            local inbox_dir="${INBOX_ROOT}/${agent}/00-INBOX0"
            mkdir -p "$inbox_dir"

            # Increment retry counter
            local retry_count=0
            if grep -q "Retry-Count:" "$task" 2>/dev/null; then
                retry_count=$(grep "Retry-Count:" "$task" | tail -1 | sed 's/.*Retry-Count: //' | tr -d ' ')
            fi
            retry_count=$((retry_count + 1))

            {
                echo ""
                echo "**Retry-Count**: ${retry_count}"
                echo "**Retried-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
                echo "**Retried-By**: proactive_orchestrator.sh"
            } >> "$task"

            # Reset status to PENDING
            if command -v sed &>/dev/null; then
                sed -i '' 's/^\*\*Status\*\*: .*/\*\*Status\*\*: PENDING/' "$task" 2>/dev/null || true
                sed -i '' 's/^\*\*Kanban\*\*: .*/\*\*Kanban\*\*: INBOX0/' "$task" 2>/dev/null || true
            fi

            mv "$task" "$inbox_dir/"
            log_action "RETRY: ${agent}/${task_name} (attempt ${retry_count}) → 00-INBOX0"
            retried=$((retried + 1))

            # Limit retries per cycle
            if [ "$retried" -ge 2 ]; then
                break 2
            fi
        done
    done

    log "Retry scan complete: ${retried} tasks moved back to INBOX0"
}

# === FEATURE 4: IDLE AGENT WORK GENERATION ===
get_agent_status() {
    local agent="$1"
    [ -f "$HEALTH_FILE" ] || { echo "UNKNOWN"; return; }

    local status
    status=$(grep -i "| ${agent}" "$HEALTH_FILE" 2>/dev/null \
        | head -1 \
        | awk -F'|' '{print $5}' \
        | tr -d ' ' \
        | tr '[:upper:]' '[:lower:]')

    echo "${status:-unknown}"
}

dispatch_idle_work() {
    log "--- Checking for idle agents ---"
    local dispatched=0

    # Read health file age — if too old, watchdog may be down
    if [ -f "$HEALTH_FILE" ]; then
        local health_age
        health_age=$(file_age_seconds "$HEALTH_FILE")
        if [ "$health_age" -gt 300 ]; then
            log "WARN: Health file is ${health_age}s old (watchdog may be stale)"
        fi
    else
        log "WARN: Health file missing — cannot determine agent status"
        return
    fi

    for agent in "${AGENTS[@]}"; do
        # Skip Commander — it self-directs via Sovereign
        [ "$agent" = "commander" ] && continue

        local status
        status=$(get_agent_status "$agent")

        # Only dispatch to IDLE or STALE agents
        if [ "$status" != "idle" ] && [ "$status" != "stale" ]; then
            continue
        fi

        # Skip if agent already has pending work
        local pending
        pending=$(count_pending "$agent")
        if [ "$pending" -gt 0 ]; then
            log "${agent} is ${status} but has ${pending} pending tasks — skipping"
            continue
        fi

        # Skip if agent has in-progress work
        local inprog
        inprog=$(count_inprogress "$agent")
        if [ "$inprog" -gt 0 ]; then
            continue
        fi

        # Check cooldown — don't spam idle tasks
        local last_dispatch_marker="/tmp/orchestrator_last_idle_${agent}"
        if [ -f "$last_dispatch_marker" ]; then
            local marker_age
            marker_age=$(file_age_seconds "$last_dispatch_marker")
            if [ "$marker_age" -lt "$IDLE_TASK_COOLDOWN" ]; then
                log "${agent} idle task cooldown active (${marker_age}s < ${IDLE_TASK_COOLDOWN}s)"
                continue
            fi
        fi

        # Generate appropriate work based on agent role
        local task_dispatched=false

        case "$agent" in
            adjudicator)
                if ! task_exists_for_agent "$agent" "ecosystem_health"; then
                    dispatch_task "$agent" "ecosystem_health" \
                        "Run ecosystem health audit: verify all launchd agents are loaded and running, Docker containers are healthy, tmux constellation has all expected panes, auto-ingest loops are active with valid PIDs, and no stale lockfiles exist. Check disk space and report any anomalies. Write concise health report."
                    task_dispatched=true
                fi
                ;;
            cartographer)
                if ! task_exists_for_agent "$agent" "corpus_freshness"; then
                    dispatch_task "$agent" "corpus_freshness" \
                        "Survey the 05-SIGMA corpus for freshness. Identify any mechanics/ or practice/ files not updated in the last 14 days. Check for orphaned references (files mentioned in indexes but missing). Report corpus health metrics: total files, average age, stalest file, any broken cross-references."
                    task_dispatched=true
                fi
                ;;
            psyche)
                if ! task_exists_for_agent "$agent" "infrastructure_audit"; then
                    dispatch_task "$agent" "infrastructure_audit" \
                        "Run infrastructure coherence audit: verify launchd plists match template copies in 00-ORCHESTRATION/scripts/launchd-mini/, check that watchdog is running and reporting, verify Docker container restart policies, confirm auto-ingest supervisor is active. Report any drift between deployed and template configurations."
                    task_dispatched=true
                fi
                ;;
            ajna)
                if ! task_exists_for_agent "$agent" "mba_health"; then
                    dispatch_task "$agent" "mba_health" \
                        "Run MBA health self-check: verify SSH connectivity to Mac mini (ssh mini hostname), check git sync status, confirm OpenClaw is responsive, verify launchd agents are loaded. Report any issues."
                    task_dispatched=true
                fi
                ;;
        esac

        if [ "$task_dispatched" = true ]; then
            touch "$last_dispatch_marker"
            dispatched=$((dispatched + 1))
            log_action "IDLE_DISPATCH: ${agent} (status: ${status}) → maintenance task"
        fi

        # Cap dispatches per cycle
        if [ "$dispatched" -ge "$MAX_DISPATCHES_PER_CYCLE" ]; then
            break
        fi
    done

    log "Idle dispatch complete: ${dispatched} tasks generated"
}

dispatch_task() {
    local agent="$1"
    local slug="$2"
    local description="$3"

    # Use dispatch.sh if available (canonical path)
    if [ -f "${SCRIPTS_DIR}/dispatch.sh" ]; then
        bash "${SCRIPTS_DIR}/dispatch.sh" "$agent" "$slug" "$description" "" "TASK" "orchestrator" 2>/dev/null
        log "Dispatched via dispatch.sh: ${agent}/${slug}"
    else
        # Fallback: create task file directly
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

---

## Objective

${description}

---

## Context Files

- COCKPIT.md
- CLAUDE.md
- 00-ORCHESTRATION/state/DYN-CONSTELLATION_HEALTH.md

## Expected Output

Write results to: -OUTBOX/${agent}/RESULTS/RESULT-${agent}-${today}-${slug}.md

## Completion Protocol

1. Write output to specified location
2. Update Status to COMPLETE or FAILED
TASK_EOF

        log "Created task directly: ${task_file}"
    fi
}

# === FEATURE 5: DEFERRED COMMITMENTS SCANNING ===
scan_deferred_commitments() {
    log "--- Scanning deferred commitments ---"

    [ -f "$DEFERRED_FILE" ] || { log "No deferred commitments file found"; return; }

    local today_iso
    today_iso=$(date '+%Y-%m-%d')
    local overdue_count=0
    local dispatched=0

    # Parse the Active Commitments table for OPEN items past their target date
    # Table format: | ID | Source | Commitment | Pri | Status | Target | Notes |
    while IFS='|' read -r _ id _ commitment pri status target _; do
        # Clean whitespace
        id=$(echo "$id" | tr -d ' ')
        status=$(echo "$status" | tr -d ' ')
        target=$(echo "$target" | tr -d ' ')
        pri=$(echo "$pri" | tr -d ' ')
        commitment=$(echo "$commitment" | sed 's/^ *//;s/ *$//')

        # Only process OPEN items
        [ "$status" = "OPEN" ] || continue

        # Check if target date is past
        if [ -n "$target" ] && [[ "$target" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
            if [[ "$target" < "$today_iso" ]] || [[ "$target" = "$today_iso" ]]; then
                overdue_count=$((overdue_count + 1))
                log "OVERDUE: ${id} — ${commitment} (target: ${target}, pri: ${pri})"

                # Only auto-dispatch P0 overdue items, and only to adjudicator (for validation)
                if [ "$pri" = "P0" ] && [ "$dispatched" -lt 1 ]; then
                    local slug
                    slug=$(echo "$id" | tr '[:upper:]' '[:lower:]' | tr -c '[:alnum:]' '_')
                    slug="deferred_${slug}_followup"

                    if ! task_exists_for_agent "adjudicator" "$slug"; then
                        dispatch_task "adjudicator" "$slug" \
                            "OVERDUE DEFERRED COMMITMENT: ${id} — ${commitment}. Target date was ${target}. Priority: ${pri}. Assess current status: has this been addressed? If partially done, document what remains. If blocked, identify the blocker. Write assessment to result file."
                        dispatched=$((dispatched + 1))
                        log_action "DEFERRED_DISPATCH: ${id} → adjudicator for assessment"
                    fi
                fi
            fi
        fi
    done < <(grep "^|" "$DEFERRED_FILE" 2>/dev/null | grep -v "^| ID\|^| --\|^|-")

    log "Deferred scan complete: ${overdue_count} overdue items found, ${dispatched} tasks dispatched"
}

# === FEATURE 6: INBOX HYGIENE ===
inbox_hygiene() {
    log "--- Running inbox hygiene ---"

    for agent in "${AGENTS[@]}"; do
        local inbox="${INBOX_ROOT}/${agent}/00-INBOX0"
        [ -d "$inbox" ] || continue

        # Count stale CONFIRM/RESULT files in INBOX0 (older than 48 hours)
        local stale_confirms=0
        for file in "$inbox"/CONFIRM-*.md "$inbox"/RESULT-*.md "$inbox"/EXECLOG-*.log; do
            [ -f "$file" ] || continue
            local age
            age=$(file_age_seconds "$file")
            if [ "$age" -gt 172800 ]; then
                stale_confirms=$((stale_confirms + 1))
            fi
        done

        if [ "$stale_confirms" -gt 10 ]; then
            log "WARN: ${agent} INBOX0 has ${stale_confirms} stale CONFIRM/RESULT/EXECLOG files (>48h old)"
        fi

        # Check for orphaned state files (state references task not in IN_PROGRESS)
        local state_file="${INBOX_ROOT}/${agent}/.current_task"
        if [ -f "$state_file" ]; then
            local task_path
            task_path=$(cut -d'|' -f2 "$state_file" 2>/dev/null || echo "")
            if [ -n "$task_path" ] && [ ! -f "$task_path" ]; then
                log "WARN: ${agent} has orphaned state file (task missing: ${task_path})"
            fi
        fi
    done

    log "Inbox hygiene complete"
}

# === STATUS REPORT ===
write_status_summary() {
    local summary_file="${STATE_DIR}/.orchestrator_last_run"
    cat > "$summary_file" <<EOF
# Proactive Orchestrator — Last Run
timestamp: $(date -u '+%Y-%m-%dT%H:%M:%SZ')
pid: $$
cycle_duration_s: ${1:-0}
EOF
}

# === MAIN ===
main() {
    acquire_lock

    local start_time
    start_time=$(now_epoch)

    log "=== Proactive Orchestrator cycle start ==="

    mkdir -p "$STATE_DIR"

    # Feature 1: Clean up stale in-progress tasks
    cleanup_stale_inprogress

    # Feature 2: Write cross-agent awareness state
    write_constellation_state

    # Feature 3: Retry eligible failed tasks
    retry_failed_tasks

    # Feature 4: Generate work for idle agents
    dispatch_idle_work

    # Feature 5: Scan deferred commitments for overdue items
    scan_deferred_commitments

    # Feature 6: Inbox hygiene checks
    inbox_hygiene

    local end_time
    end_time=$(now_epoch)
    local duration=$(( end_time - start_time ))

    write_status_summary "$duration"

    log "=== Proactive Orchestrator cycle complete (${duration}s) ==="
}

main "$@"
