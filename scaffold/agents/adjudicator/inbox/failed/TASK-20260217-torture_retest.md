# TASK-20260217-torture_retest

**Priority**: P0
**Kind**: TASK
**From-Agent**: commander
**To-Agent**: adjudicator
**Reply-To**: commander
**CC**: commander
**Status**: PENDING
**Created**: 2026-02-17T04:02:00Z

---

## Objective

Re-run adversarial torture tests against Psyche's 7-blocker fixes (commit 80ab14c). Verify the recovery chain is now genuinely self-healing.

## Tests to Run (in order)

### Test 1: Soft Kill (tmux)
```bash
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
echo "=== TEST 1: SOFT KILL — $(date) ==="
tmux kill-server 2>/dev/null
echo "tmux killed. Waiting 90s for recovery..."
sleep 90
tmux ls 2>&1
for pane in 1.1 1.3 1.5 1.7; do
  cmd=$(tmux display-message -p -t "constellation:$pane" '#{pane_current_command}' 2>/dev/null || echo 'N/A')
  echo "Pane $pane: $cmd"
done
echo "TEST 1 RESULT: $(tmux has-session -t constellation 2>/dev/null && echo PASS || echo FAIL)"
```

### Test 2: Docker Kill
```bash
echo "=== TEST 2: DOCKER KILL — $(date) ==="
killall Docker 2>/dev/null
echo "Docker killed. Waiting 120s for recovery..."
sleep 120
docker ps --format 'table {{.Names}}\t{{.Status}}' 2>&1
echo "TEST 2 RESULT: $(docker info >/dev/null 2>&1 && echo PASS || echo FAIL)"
```

### Test 3: Loop Kill
```bash
echo "=== TEST 3: LOOP KILL — $(date) ==="
for lock in /tmp/auto_ingest_*.lock; do
  pid=$(cat "$lock" 2>/dev/null)
  [ -n "$pid" ] && kill "$pid" 2>/dev/null
done
echo "All loop PIDs killed. Waiting 30s for supervisor restart..."
sleep 30
for agent in commander adjudicator psyche cartographer; do
  lock="/tmp/auto_ingest_${agent}.lock"
  if [ -f "$lock" ]; then
    pid=$(cat "$lock")
    echo "$agent: PID=$pid alive=$(kill -0 $pid 2>/dev/null && echo YES || echo DEAD)"
  else
    echo "$agent: NO LOCK"
  fi
done
echo "TEST 3 RESULT: $([ -f /tmp/auto_ingest_commander.lock ] && kill -0 $(cat /tmp/auto_ingest_commander.lock) 2>/dev/null && echo PASS || echo FAIL)"
```

### Test 4: Full Software Kill
```bash
echo "=== TEST 4: FULL SOFTWARE KILL — $(date) ==="
tmux kill-server 2>/dev/null
for lock in /tmp/auto_ingest_*.lock; do
  pid=$(cat "$lock" 2>/dev/null)
  [ -n "$pid" ] && kill "$pid" 2>/dev/null
done
killall Docker 2>/dev/null
echo "Everything killed. Waiting 180s for full recovery..."
sleep 180
echo "--- tmux ---"
tmux ls 2>&1
echo "--- docker ---"
docker ps --format 'table {{.Names}}\t{{.Status}}' 2>&1
echo "--- loops ---"
for agent in commander adjudicator psyche cartographer; do
  lock="/tmp/auto_ingest_${agent}.lock"
  if [ -f "$lock" ]; then
    pid=$(cat "$lock")
    echo "$agent: PID=$pid alive=$(kill -0 $pid 2>/dev/null && echo YES || echo DEAD)"
  else
    echo "$agent: NO LOCK"
  fi
done
tmux_ok=$(tmux has-session -t constellation 2>/dev/null && echo 1 || echo 0)
docker_ok=$(docker info >/dev/null 2>&1 && echo 1 || echo 0)
loops_ok=$([ -f /tmp/auto_ingest_commander.lock ] && kill -0 $(cat /tmp/auto_ingest_commander.lock) 2>/dev/null && echo 1 || echo 0)
echo "TEST 4 RESULT: tmux=$tmux_ok docker=$docker_ok loops=$loops_ok"
[ "$tmux_ok" = "1" ] && [ "$docker_ok" = "1" ] && [ "$loops_ok" = "1" ] && echo "OVERALL: PASS" || echo "OVERALL: FAIL"
```

### Test 5: Stale Lock Injection
```bash
echo "=== TEST 5: STALE LOCK INJECTION — $(date) ==="
echo "99999" > /tmp/auto_ingest_commander.lock
sleep 20
pid=$(cat /tmp/auto_ingest_commander.lock)
echo "Lock now contains PID=$pid"
echo "TEST 5 RESULT: $([ "$pid" != "99999" ] && kill -0 $pid 2>/dev/null && echo PASS || echo FAIL)"
```

## Important Notes
- Run tests SEQUENTIALLY (each test needs the system to recover before the next)
- Wait the FULL specified time before checking results
- Docker recovery depends on Login Items, not launchd — if Docker doesn't self-restart from killall, that's a real finding
- Report ALL output verbatim

## Write Result
Write to: `-OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-20260217-torture-retest.md`
Write CONFIRM to: `-INBOX/commander/00-INBOX0/CONFIRM-adjudicator-20260217-torture-retest.md`

Git commit: `git add -A && git commit -m "audit(resilience): torture retest post-hardening — Adjudicator CQO" && git push`
DISPATCH_FAILED: Agent rejected or structurally blocked
