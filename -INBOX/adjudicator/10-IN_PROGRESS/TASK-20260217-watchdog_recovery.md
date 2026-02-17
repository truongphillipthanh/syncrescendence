# TASK: Health-triggered recovery actions in constellation_watchdog.sh

**Status**: PENDING
**Retry-Count**: 1
**Failure-Reason**: EXEC_TIMEOUT: Exceeded 1800s
**Priority**: P0
**Reply-To**: commander
**CC**: commander
**To**: adjudicator
**Timeout**: 600

## Objective

Enhance constellation_watchdog.sh so that when it detects degraded health states, it takes AUTOMATIC RECOVERY ACTIONS instead of just reporting. Currently the watchdog writes a health report but does nothing about problems. After this change, it actively heals the constellation.

IMPORTANT: Do NOT touch auto_ingest_loop.sh or auto_ingest_supervisor.sh. Only modify constellation_watchdog.sh. Other agents are working on other files in parallel.

### Recovery Actions to Add

Add a function `attempt_agent_recovery()` that takes agent name, pane, and status. Call it after analyzing each agent in the main loop.

Recovery logic by status:

1. **STALE** (no change for >300s):
   - Send a heartbeat prompt to the agent's tmux pane: `tmux send-keys -t "constellation:${pane}" "" Enter`
   - This sends an empty Enter which prompts most CLIs to show their prompt, confirming they're alive
   - Log: "RECOVERY: Sent heartbeat to ${name} (${pane}) — stale ${elapsed}s"

2. **STALE** (no change for >1800s / 30 minutes):
   - The agent is likely truly stuck. Kill and restart the pane's process:
   - `tmux send-keys -t "constellation:${pane}" C-c C-c` (send two Ctrl-C to break out)
   - Wait 3 seconds
   - Log: "RECOVERY: Sent interrupt to ${name} (${pane}) — stale ${elapsed}s"

3. **ERROR**:
   - Log the error but do NOT auto-recover (errors need human review)
   - Write an alert to -SOVEREIGN/: `ALERT-${name}-$(date +%Y%m%d%H%M).md`
   - Contents: agent name, error detail, timestamp, "requires investigation"

4. **RATE_LIMITED** (stuck for >900s):
   - Log but do NOT retry — rate limits need time to clear
   - If >3600s (1 hour): write alert to -SOVEREIGN/

### Docker Recovery

Add a Docker health check to the main function. After the agent loop:

```bash
# Docker health check
if ! docker info >/dev/null 2>&1; then
    log "CRITICAL: Docker is DOWN"
    # Try to restart Docker Desktop
    open -a "Docker Desktop" 2>/dev/null || true
    log "RECOVERY: Attempted Docker Desktop restart"
fi
```

### Implementation Notes

- The watchdog already has `$TMUX_BIN` configured for tmux commands
- Use the existing `analyze()` function output (status|detail|hash) to determine action
- Add recovery AFTER the health report is written (so the report always reflects pre-recovery state)
- Recovery actions should be idempotent (safe to run every 60s)
- Add a cooldown mechanism: don't send more than 1 heartbeat per agent per 5 minutes. Use a file-based timestamp: `${WATCHDOG_STATE}.${agent}.last_recovery`

### Verification

1. `grep -c 'attempt_agent_recovery\|RECOVERY:' ~/Desktop/syncrescendence/00-ORCHESTRATION/scripts/constellation_watchdog.sh` — must be >= 5
2. `grep -c 'Docker is DOWN\|Docker Desktop' ~/Desktop/syncrescendence/00-ORCHESTRATION/scripts/constellation_watchdog.sh` — must be >= 2
3. Run the watchdog manually: `bash ~/Desktop/syncrescendence/00-ORCHESTRATION/scripts/constellation_watchdog.sh` — verify it completes without errors and health report is written
4. Commit: `git add 00-ORCHESTRATION/scripts/constellation_watchdog.sh && git commit -m 'feat(watchdog): health-triggered recovery — heartbeat, interrupt, Docker restart, Sovereign alerts'`

**Reply-To**: commander
**CC**: commander
