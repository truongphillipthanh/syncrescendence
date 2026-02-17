# TASK: Create proactive_orchestrator.sh — autonomous work generation

**Status**: IN_PROGRESS
**Priority**: P0
**Claimed-At**: 2026-02-17T15:38:49Z
**Claimed-By**: commander-Lisas-MacBook-Air
**Kanban**: IN_PROGRESS
**Reply-To**: commander
**CC**: commander
**To**: commander
**Timeout**: 600

## Objective

Create a new script `00-ORCHESTRATION/scripts/proactive_orchestrator.sh` that runs periodically (via launchd, every 5 minutes) and generates work for idle agents. This is the missing "brain" — currently agents only work when Commander dispatches. After this, the constellation generates its own tasks.

IMPORTANT: Create a NEW script. Do NOT modify auto_ingest_loop.sh or constellation_watchdog.sh (other agents are editing those).

### Script Structure

```bash
#!/usr/bin/env bash
# proactive_orchestrator.sh — Autonomous work generation for idle agents
# Runs every 5 minutes via launchd. Scans for:
#   1. Retryable failed tasks → moves them back to INBOX0
#   2. Stale IN_PROGRESS tasks → moves to FAILED after timeout
#   3. Idle agents → dispatches health/maintenance tasks
#   4. Deferred commitments → generates tasks for overdue items

set -u

REPO_DIR="${HOME}/Desktop/syncrescendence"
STATE_DIR="${REPO_DIR}/00-ORCHESTRATION/state"
HEALTH_FILE="${STATE_DIR}/DYN-CONSTELLATION_HEALTH.md"
ORCHESTRATOR_LOG="${HOME}/Library/Logs/syncrescendence-orchestrator.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

log() { echo "[${TIMESTAMP}] $*" >> "$ORCHESTRATOR_LOG" 2>/dev/null || true; }
```

### Feature 1: Stale IN_PROGRESS Cleanup

Scan all agents' 10-IN_PROGRESS/ folders. If a task file hasn't been modified in >30 minutes, move it to 50_FAILED with Failure-Reason "stale_in_progress_timeout":

```bash
cleanup_stale_inprogress() {
    for agent_dir in "$REPO_DIR"/-INBOX/*/10-IN_PROGRESS; do
        [ -d "$agent_dir" ] || continue
        local agent=$(basename "$(dirname "$agent_dir")")
        for task in "$agent_dir"/TASK-*.md; do
            [ -f "$task" ] || continue
            local age=$(( $(date +%s) - $(stat -f %m "$task") ))
            if [ "$age" -gt 1800 ]; then
                local failed_dir="$(dirname "$agent_dir")/50_FAILED"
                mkdir -p "$failed_dir"
                # Add failure metadata
                echo "**Failure-Reason**: stale_in_progress_timeout (${age}s)" >> "$task"
                echo "**Failed-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')" >> "$task"
                mv "$task" "$failed_dir/"
                log "STALE_CLEANUP: $agent — $(basename "$task") (${age}s old)"
            fi
        done
    done
}
```

### Feature 2: Cross-Agent Awareness State File

Write a shared state file that any agent can read to understand the constellation:

```bash
write_constellation_state() {
    local state_file="${STATE_DIR}/DYN-CONSTELLATION_STATE.md"
    {
        echo "# Constellation State"
        echo "Generated: ${TIMESTAMP}"
        echo ""
        echo "| Agent | Inbox0 | InProgress | Failed | Done (24h) | Health |"
        echo "|-------|--------|------------|--------|------------|--------|"
        
        for agent in commander adjudicator cartographer psyche ajna; do
            local inbox0=$(ls "$REPO_DIR/-INBOX/$agent/00-INBOX0"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            local inprog=$(ls "$REPO_DIR/-INBOX/$agent/10-IN_PROGRESS"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            local failed=$(ls "$REPO_DIR/-INBOX/$agent/50_FAILED"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
            # Count tasks done in last 24h
            local done24=$(find "$REPO_DIR/-INBOX/$agent/40-DONE" -name "TASK-*.md" -mtime -1 2>/dev/null | wc -l | tr -d ' ')
            # Get health from watchdog report
            local health=$(grep "| ${agent^}" "$HEALTH_FILE" 2>/dev/null | awk -F'|' '{print $5}' | xargs || echo "UNKNOWN")
            echo "| $agent | $inbox0 | $inprog | $failed | $done24 | $health |"
        done
        
        echo ""
        echo "## Queued Work"
        for agent in commander adjudicator cartographer psyche ajna; do
            local tasks=$(ls "$REPO_DIR/-INBOX/$agent/00-INBOX0"/TASK-*.md 2>/dev/null)
            if [ -n "$tasks" ]; then
                echo "### $agent"
                for t in $tasks; do echo "- $(basename "$t")"; done
            fi
        done
    } > "$state_file"
    log "STATE: Written constellation state to $state_file"
}
```

### Feature 3: Idle Agent Work Generation

If an agent has empty INBOX0 and no IN_PROGRESS tasks, and its health is IDLE or STALE, dispatch a lightweight maintenance task:

```bash
dispatch_idle_work() {
    for agent in commander adjudicator cartographer psyche; do
        local inbox0_count=$(ls "$REPO_DIR/-INBOX/$agent/00-INBOX0"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
        local inprog_count=$(ls "$REPO_DIR/-INBOX/$agent/10-IN_PROGRESS"/TASK-*.md 2>/dev/null | wc -l | tr -d ' ')
        
        # Skip if agent has work
        [ "$inbox0_count" -gt 0 ] || [ "$inprog_count" -gt 0 ] && continue
        
        # Check cooldown (don't dispatch more than once per 30 minutes)
        local cooldown_file="/tmp/orchestrator-${agent}-last-dispatch"
        if [ -f "$cooldown_file" ]; then
            local last=$(cat "$cooldown_file")
            local elapsed=$(( $(date +%s) - last ))
            [ "$elapsed" -lt 1800 ] && continue
        fi
        
        # Dispatch a health check / status report task
        local task_file="$REPO_DIR/-INBOX/$agent/00-INBOX0/TASK-$(date +%Y%m%d)-idle_health_report.md"
        cat > "$task_file" << EOF
# TASK: Idle health report

**Status**: PENDING
**Priority**: P2
**Reply-To**: commander
**CC**: commander
**To**: $agent
**Timeout**: 120

## Objective

You are idle. Run a quick health self-check: verify your CLI is responsive, check git status, report any issues. Write a brief status to your RESULT file. If everything is fine, just confirm you're operational.
EOF
        date +%s > "$cooldown_file"
        log "IDLE_DISPATCH: Sent health report task to $agent"
    done
}
```

### Main Function

```bash
main() {
    log "Orchestrator cycle starting"
    cleanup_stale_inprogress
    write_constellation_state
    dispatch_idle_work
    log "Orchestrator cycle complete"
}

main "$@"
```

### Also Create: launchd plist

Create `~/Library/LaunchAgents/com.syncrescendence.proactive-orchestrator.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.syncrescendence.proactive-orchestrator</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/home/Desktop/syncrescendence/00-ORCHESTRATION/scripts/proactive_orchestrator.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>/Users/home/Desktop/syncrescendence</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
        <key>HOME</key>
        <string>/Users/home</string>
        <key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA</key>
        <string>macbook-air</string>
        <key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER</key>
        <string>local</string>
        <key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR</key>
        <string>local</string>
        <key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER</key>
        <string>local</string>
        <key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE</key>
        <string>local</string>
    </dict>
    <key>StandardOutPath</key>
    <string>/Users/home/Library/Logs/syncrescendence-orchestrator.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/home/Library/Logs/syncrescendence-orchestrator.log</string>
</dict>
</plist>
```

Load it: `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.proactive-orchestrator.plist`

### Verification

1. Script exists and is executable: `ls -la ~/Desktop/syncrescendence/00-ORCHESTRATION/scripts/proactive_orchestrator.sh`
2. Run it manually: `bash ~/Desktop/syncrescendence/00-ORCHESTRATION/scripts/proactive_orchestrator.sh` — verify no errors
3. State file created: `cat ~/Desktop/syncrescendence/00-ORCHESTRATION/state/DYN-CONSTELLATION_STATE.md`
4. Plist loaded: `launchctl list | grep proactive`
5. Commit: `git add 00-ORCHESTRATION/scripts/proactive_orchestrator.sh && git commit -m 'feat(orchestration): proactive orchestrator — stale cleanup, constellation state, idle dispatch'`

**Reply-To**: commander
**CC**: commander
