# TASK: Autonomous retry + escalation in auto_ingest_loop.sh

**Status**: PENDING
**Priority**: P0
**Reply-To**: commander
**CC**: commander
**To**: psyche
**Timeout**: 600

## Objective

Add two capabilities to auto_ingest_loop.sh: (1) automatic retry of failed tasks with transient errors, and (2) automatic escalation when retries are exhausted. Currently, failed tasks die silently in 50_FAILED/. After this change, transient failures retry automatically, and permanent failures escalate to the Sovereign.

IMPORTANT: Do NOT touch constellation_watchdog.sh or create new scripts. Only modify auto_ingest_loop.sh. Other agents are working on other files in parallel.

### Feature 1: Retry Logic

Add a periodic scan (every 60s, in the main polling loop) that checks 50_FAILED/ for retryable tasks:

```bash
retry_failed_tasks() {
    local failed_dir="${INBOX_ROOT}/50_FAILED"
    for task_file in "$failed_dir"/TASK-*.md; do
        [ -f "$task_file" ] || continue
        
        # Extract retry count (default 0 if not set)
        local retry_count
        retry_count=$(grep -oP '(?<=\*\*Retry-Count\*\*: )\d+' "$task_file" 2>/dev/null || echo "0")
        [ -z "$retry_count" ] && retry_count=0
        
        # Max 3 retries
        [ "$retry_count" -ge 3 ] && continue
        
        # Only retry transient failures (rate limit, timeout, resource exhaustion)
        local failure_reason
        failure_reason=$(grep -oP '(?<=\*\*Failure-Reason\*\*: ).+' "$task_file" 2>/dev/null || echo "")
        
        # Check if failure is transient (retryable)
        if echo "$failure_reason" | grep -qiE "rate.limit|timeout|quota|capacity|RESOURCE_EXHAUSTED|usage.limit|EXEC_TIMEOUT"; then
            # Increment retry count
            local new_count=$((retry_count + 1))
            # Update retry count in file (or add it)
            if grep -q '\*\*Retry-Count\*\*:' "$task_file"; then
                sed -i '' "s/\*\*Retry-Count\*\*: [0-9]*/\*\*Retry-Count\*\*: $new_count/" "$task_file"
            else
                sed -i '' "/\*\*Status\*\*:/a\\
**Retry-Count**: $new_count" "$task_file"
            fi
            # Reset status to PENDING
            sed -i '' 's/\*\*Status\*\*: FAILED/\*\*Status\*\*: PENDING/' "$task_file"
            # Move back to INBOX0
            mv "$task_file" "${INBOX_ROOT}/00-INBOX0/" 2>/dev/null || true
            log "RETRY ($new_count/3): $(basename "$task_file") — $failure_reason"
        fi
    done
}
```

Call `retry_failed_tasks` at the end of each polling cycle (after the INBOX0 scan).

### Feature 2: Escalation on Exhausted Retries

Add a function that runs after retry_failed_tasks. For tasks in 50_FAILED with Retry-Count >= 3, write an ESCALATION file to -SOVEREIGN/:

```bash
escalate_exhausted_tasks() {
    local failed_dir="${INBOX_ROOT}/50_FAILED"
    local sovereign_dir="${REPO_DIR}/-SOVEREIGN"
    mkdir -p "$sovereign_dir" 2>/dev/null || true
    
    for task_file in "$failed_dir"/TASK-*.md; do
        [ -f "$task_file" ] || continue
        local retry_count
        retry_count=$(grep -oP '(?<=\*\*Retry-Count\*\*: )\d+' "$task_file" 2>/dev/null || echo "0")
        [ -z "$retry_count" ] && retry_count=0
        [ "$retry_count" -lt 3 ] && continue
        
        # Check if already escalated (prevent duplicate escalations)
        local base=$(basename "$task_file")
        local esc_marker="${failed_dir}/.escalated-${base}"
        [ -f "$esc_marker" ] && continue
        
        # Write escalation
        local esc_file="${sovereign_dir}/ESCALATION-${AGENT_NAME}-$(date +%Y%m%d)-${base}"
        cat > "$esc_file" << EOF
# ESCALATION: Task exhausted retries

**Kind**: ESCALATION
**Agent**: ${AGENT_NAME}
**Task**: ${base}
**Retries**: ${retry_count}
**Failure-Reason**: $(grep -oP '(?<=\*\*Failure-Reason\*\*: ).+' "$task_file" 2>/dev/null || echo "unknown")
**Escalated-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')

This task failed ${retry_count} times with transient errors and requires Sovereign intervention.
Original task is in: -INBOX/${AGENT_NAME}/50_FAILED/${base}
EOF
        touch "$esc_marker"
        log "ESCALATION: ${base} → -SOVEREIGN/ (${retry_count} retries exhausted)"
    done
}
```

Call `escalate_exhausted_tasks` right after `retry_failed_tasks`.

### Verification

After implementing, verify:
1. `grep -c 'retry_failed_tasks\|escalate_exhausted_tasks' ~/Desktop/syncrescendence/orchestration/scripts/auto_ingest_loop.sh` — must be >= 4 (2 function defs + 2 calls)
2. Create a test task in 50_FAILED with Failure-Reason containing "rate limit" and Retry-Count: 0, verify it moves back to INBOX0 within 60s
3. Commit: `git add orchestration/scripts/auto_ingest_loop.sh && git commit -m 'feat(orchestration): auto-retry transient failures + escalation to Sovereign'`

**Reply-To**: commander
**CC**: commander
