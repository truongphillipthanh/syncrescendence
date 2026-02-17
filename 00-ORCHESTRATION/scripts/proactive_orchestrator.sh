#!/usr/bin/env bash
# proactive_orchestrator.sh — Autonomous work generation for idle agents
# Runs every 5 minutes via launchd. Scans for:
#   1. Stale IN_PROGRESS tasks → moves to 50_FAILED after timeout
#   2. Cross-agent awareness state file → DYN-CONSTELLATION_STATE.md
#   3. Idle agents → dispatches lightweight health/maintenance tasks
#
# IMPORTANT: This is a NEW script. Does NOT modify auto_ingest_loop.sh or
# constellation_watchdog.sh. Operates independently.

# No set -e — monitoring scripts must degrade gracefully (Adjudicator pattern)
set -u

REPO_DIR="${HOME}/Desktop/syncrescendence"
STATE_DIR="${REPO_DIR}/00-ORCHESTRATION/state"
HEALTH_FILE="${STATE_DIR}/DYN-CONSTELLATION_HEALTH.md"
ORCHESTRATOR_LOG="${HOME}/Library/Logs/syncrescendence-orchestrator.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

AGENTS="commander adjudicator cartographer psyche ajna"

log() { echo "[${TIMESTAMP}] $*" >> "$ORCHESTRATOR_LOG" 2>/dev/null || true; }

# ============================================================================
# Feature 1: Stale IN_PROGRESS Cleanup
# ============================================================================
cleanup_stale_inprogress() {
    for agent_dir in "$REPO_DIR"/-INBOX/*/10-IN_PROGRESS; do
        [ -d "$agent_dir" ] || continue
        local agent
        agent=$(basename "$(dirname "$agent_dir")")
        echo "$AGENTS" | grep -qw "$agent" || continue

        for task in "$agent_dir"/TASK-*.md; do
            [ -f "$task" ] || continue
            local age
            age=$(( $(date +%s) - $(stat -f %m "$task") ))
            if [ "$age" -gt 1800 ]; then
                local failed_dir
                failed_dir="$(dirname "$agent_dir")/50_FAILED"
                mkdir -p "$failed_dir"
                {
                    echo ""
                    echo "---"
                    echo "**Failure-Reason**: stale_in_progress_timeout (${age}s)"
                    echo "**Failed-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
                    echo "**Failed-By**: proactive_orchestrator"
                } >> "$task"
                mv "$task" "$failed_dir/"
                log "STALE_CLEANUP: $agent — $(basename "$task") (${age}s old)"
            fi
        done
    done
}

# ============================================================================
# Feature 2: Cross-Agent Awareness State File
# ============================================================================
write_constellation_state() {
    local state_file="${STATE_DIR}/DYN-CONSTELLATION_STATE.md"
    local tmp_file="${state_file}.tmp"
    {
        echo "# Constellation State"
        echo "Generated: ${TIMESTAMP}"
        echo ""
        echo "| Agent | Inbox0 | InProgress | Failed | Done (24h) | Health |"
        echo "|-------|--------|------------|--------|------------|--------|"

        for agent in $AGENTS; do
            local inbox0 inprog failed done24 health
            inbox0=$(ls "$REPO_DIR/-INBOX/$agent/00-INBOX0"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            inprog=$(ls "$REPO_DIR/-INBOX/$agent/10-IN_PROGRESS"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            failed=$(ls "$REPO_DIR/-INBOX/$agent/50_FAILED"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            done24=$(find "$REPO_DIR/-INBOX/$agent/40-DONE" -name "TASK-*.md" -mtime -1 2>/dev/null | wc -l | tr -d ' ')
            health=$(grep -i "| ${agent}" "$HEALTH_FILE" 2>/dev/null | head -1 | awk -F'|' '{print $5}' | xargs 2>/dev/null || echo "UNKNOWN")
            [ -z "$health" ] && health="UNKNOWN"
            echo "| $agent | $inbox0 | $inprog | $failed | $done24 | $health |"
        done

        echo ""
        echo "## Queued Work"
        local has_queued=0
        for agent in $AGENTS; do
            local tasks
            tasks=$(ls "$REPO_DIR/-INBOX/$agent/00-INBOX0"/TASK-*.md 2>/dev/null)
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

# ============================================================================
# Feature 3: Idle Agent Work Generation
# ============================================================================
dispatch_idle_work() {
    for agent in $AGENTS; do
        local inbox0_count inprog_count
        inbox0_count=$(ls "$REPO_DIR/-INBOX/$agent/00-INBOX0"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
        inprog_count=$(ls "$REPO_DIR/-INBOX/$agent/10-IN_PROGRESS"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')

        if [ "$inbox0_count" -gt 0 ] || [ "$inprog_count" -gt 0 ]; then
            continue
        fi

        local cooldown_file="/tmp/orchestrator-${agent}-last-dispatch"
        if [ -f "$cooldown_file" ]; then
            local last elapsed
            last=$(cat "$cooldown_file" 2>/dev/null || echo "0")
            elapsed=$(( $(date +%s) - last ))
            if [ "$elapsed" -lt 1800 ]; then
                continue
            fi
        fi

        local inbox0_dir="$REPO_DIR/-INBOX/$agent/00-INBOX0"
        mkdir -p "$inbox0_dir"

        local task_date
        task_date=$(date +%Y%m%d)
        local task_file="$inbox0_dir/TASK-${task_date}-idle_health_report.md"

        if [ -f "$task_file" ]; then
            continue
        fi

        cat > "$task_file" << TASK_EOF
# TASK: Idle health report

**Status**: PENDING
**Priority**: P2
**Reply-To**: commander
**CC**: commander
**To**: $agent
**Timeout**: 120
**From**: Proactive Orchestrator (automated)
**Kind**: TASK
**Kanban**: INBOX0

## Objective

You are idle. Run a quick health self-check:
1. Verify your CLI is responsive
2. Check git status for uncommitted work
3. Check your INBOX for any missed tasks
4. Report any issues found

Write a brief status to your RESULT file. If everything is fine, just confirm you're operational.

## Expected Output

- Write results to \`-OUTBOX/${agent}/RESULTS/RESULT-${agent}-${task_date}-idle_health_report.md\`
- Or commit directly if you have write access
TASK_EOF
        date +%s > "$cooldown_file"
        log "IDLE_DISPATCH: Sent health report task to $agent"
    done
}

# ============================================================================
# Main
# ============================================================================
main() {
    log "Orchestrator cycle starting"
    mkdir -p "$STATE_DIR"
    cleanup_stale_inprogress
    write_constellation_state
    dispatch_idle_work
    log "Orchestrator cycle complete"
}

main "$@"
