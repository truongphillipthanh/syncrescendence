# TASK-20260217-neural_bridge_verification

**Priority**: P1
**Kind**: TASK
**From-Agent**: commander-mba
**To-Agent**: commander
**Reply-To**: commander
**CC**: commander
**Status**: PENDING
**Created**: 2026-02-17T04:25:00Z

---

## Objective

After Psyche and Cartographer complete their Neural Bridge tasks, run comprehensive verification and commit everything. You are the coordination point.

## Phase 1: Wait for Psyche and Cartographer

Monitor their progress:
```bash
# Check for completion signals
ls -la -INBOX/commander/00-INBOX0/CONFIRM-psyche-20260217-neural-bridge*.md 2>/dev/null
ls -la -INBOX/commander/00-INBOX0/CONFIRM-cartographer-20260217-neural-bridge*.md 2>/dev/null
```

If both are done, proceed. If not, wait and re-check every 60s.

## Phase 2: Comprehensive Verification

Run the full Neural Bridge verification suite:

```bash
echo "=== NEURAL BRIDGE FULL VERIFICATION — $(date) ==="

echo "--- 1. Env Vars (Mac mini) ---"
source ~/.zshrc
env | grep SYNCRESCENDENCE_REMOTE | sort

echo "--- 2. SSH Config ---"
cat ~/.ssh/config

echo "--- 3. SSH to MBA ---"
ssh -o ConnectTimeout=5 macbook-air "echo 'BRIDGE_HEALTHY'; hostname" 2>&1

echo "--- 4. dispatch.sh SCP test (Ajna = remote) ---"
# Verify dispatch.sh would SCP to macbook-air for Ajna
AGENT_UPPER="AJNA"
REMOTE_HOST_VAR="SYNCRESCENDENCE_REMOTE_AGENT_HOST_${AGENT_UPPER}"
echo "AJNA remote host: ${!REMOTE_HOST_VAR:-NOT_SET}"

echo "--- 5. dispatch.sh local test (Commander = local) ---"
AGENT_UPPER="COMMANDER"
REMOTE_HOST_VAR="SYNCRESCENDENCE_REMOTE_AGENT_HOST_${AGENT_UPPER}"
echo "COMMANDER remote host: ${!REMOTE_HOST_VAR:-NOT_SET}"

echo "--- 6. Watchdog SSH check ---"
ssh -o BatchMode=yes -o ConnectTimeout=5 macbook-air hostname >/dev/null 2>&1 && echo "WATCHDOG: BRIDGE HEALTHY" || echo "WATCHDOG: BRIDGE DOWN"

echo "--- 7. CONFIRM routing test ---"
# Create a test CONFIRM and verify SCP logic would fire for Ajna (remote)
echo "CONFIRM routing for reply-to=ajna: would SCP to $(echo ${SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA:-local})"
echo "CONFIRM routing for reply-to=commander: would stay $(echo ${SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER:-local})"

echo "--- 8. Constellation state ---"
tmux ls 2>&1
docker ps --format 'table {{.Names}}\t{{.Status}}' 2>&1
for agent in commander adjudicator psyche cartographer; do
  lock="/tmp/auto_ingest_${agent}.lock"
  if [ -f "$lock" ]; then
    pid=$(cat "$lock")
    echo "$agent: PID=$pid alive=$(kill -0 $pid 2>/dev/null && echo YES || echo DEAD)"
  else
    echo "$agent: NO LOCK"
  fi
done

echo "--- 9. New architecture docs ---"
ls -la orchestration/state/ARCH-NEURAL_BRIDGE.md 2>/dev/null
ls -la orchestration/state/ARCH-UNPLUG_RECOVERY_ARCHITECTURE.md 2>/dev/null

echo "=== VERIFICATION COMPLETE ==="
```

## Phase 3: Git Commit and Push

Ensure all Neural Bridge changes are committed:

```bash
cd ~/Desktop/syncrescendence
git add -A
git status
git commit -m "feat(bridge): Neural Bridge genetic embedding — full constellation verification" 
git push
```

## Write Result
Write to: `-OUTBOX/commander/RESULTS/RESULT-commander-20260217-neural-bridge-verification.md`

Include: full verification output, PASS/FAIL for each check, any remaining issues.
