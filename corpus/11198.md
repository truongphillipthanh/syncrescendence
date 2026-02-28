# TASK-20260217-neural_bridge_infrastructure

**Priority**: P0
**Kind**: TASK
**From-Agent**: commander
**To-Agent**: psyche
**Reply-To**: commander
**CC**: commander
**Status**: PENDING
**Created**: 2026-02-17T04:25:00Z

---

## Objective

Genetically embed the SSH Neural Bridge into every infrastructure layer on the Mac mini. This is the Great Filter — the MBA↔Mac mini link is a vital organ. Every script, every config, every agent must know about it, use it, and monitor it.

## Phase 1: Fix Mac mini Environment Variables

The current Mac mini ~/.zshrc has WRONG env vars (self-referencing `mac-mini` for local agents):

```bash
# CURRENT (WRONG):
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER=mac-mini
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR=mac-mini
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE=mac-mini
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER=mac-mini
```

Replace with:

```bash
# Syncrescendence Neural Bridge — cross-machine dispatch env vars
# Mac mini agents that live on MBA:
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA="macbook-air"
# Mac mini agents that live locally (no SCP needed):
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER="local"
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR="local"
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER="local"
export SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE="local"
```

## Phase 2: Add CONFIRM SCP-back to auto_ingest_loop.sh

When a task completes and a CONFIRM is written to the Reply-To agent's INBOX0, check if that agent lives on another machine. If so, SCP the CONFIRM there.

In auto_ingest_loop.sh, after the CONFIRM file is written, add:

```bash
# Route CONFIRM to originating agent's machine via Neural Bridge
REPLY_TO_UPPER=$(echo "$REPLY_TO" | tr '[:lower:]' '[:upper:]')
REMOTE_VAR="SYNCRESCENDENCE_REMOTE_AGENT_HOST_${REPLY_TO_UPPER}"
REMOTE_HOST="${!REMOTE_VAR:-local}"
if [ -n "$REMOTE_HOST" ] && [ "$REMOTE_HOST" != "local" ] && [ "$REMOTE_HOST" != "localhost" ]; then
  scp -q -o BatchMode=yes -o ConnectTimeout=5 "$CONFIRM_FILE" \
    "$REMOTE_HOST:~/Desktop/syncrescendence/-INBOX/$REPLY_TO/00-INBOX0/" 2>/dev/null && \
    echo "[$(date)] CONFIRM routed to $REMOTE_HOST for $REPLY_TO" >> "$LOG" || \
    echo "[$(date)] WARN: CONFIRM SCP to $REMOTE_HOST failed" >> "$LOG"
fi
```

This ensures CONFIRMs from Mac mini agents reach Commander/Ajna on MBA automatically.

## Phase 3: Add SSH Health Check to Watchdog

In constellation_watchdog.sh, add a Neural Bridge health check:

```bash
# Neural Bridge health check
if ssh -o BatchMode=yes -o ConnectTimeout=5 macbook-air hostname >/dev/null 2>&1; then
  NEURAL_BRIDGE="HEALTHY"
else
  NEURAL_BRIDGE="DOWN"
fi
```

Write the Neural Bridge status into DYN-CONSTELLATION_HEALTH.md alongside agent health.

## Phase 4: Update OpenClaw Psyche Personality Files

In /Users/home/.openclaw/ — update these files:

### SOUL.md
Add after machine topology section:
```
### Neural Bridge (MBA ↔ Mac mini — VITAL ORGAN)
The SSH bidirectional link is the constellation's circulatory system.
| Direction | SSH Alias | Key |
|-----------|-----------|-----|
| Mac mini → MBA | macbook-air | ~/.ssh/id_ed25519_ajna_to_psyche |
| MBA → Mac mini | mini | ~/.ssh/id_ed25519_ajna (on MBA) |
Health check: ssh -o ConnectTimeout=5 macbook-air hostname
If bridge fails: continue local ops, git sync as fallback, alert Sovereign
```

### HEARTBEAT.md
Add SSH health check to Tier 4:
```
12. Test SSH to MBA: ssh -o ConnectTimeout=5 macbook-air hostname — must return MacBook Air hostname
13. If SSH fails: alert immediately — vital organ failure
```

### MEMORY.md
Add Neural Bridge state section:
```
## Neural Bridge State (2026-02-17)
- Mac mini → MBA: ssh macbook-air (key: id_ed25519_ajna_to_psyche)
- MBA → Mac mini: ssh mini (key: id_ed25519_ajna, on MBA)
- Established: 2026-02-17, all 5 torture tests PASSED
- Physical unplug test: PASSED after 7-blocker hardening
- ICMP blocked by Stealth Mode — always use SSH for health checks
```

## Phase 5: Update dispatch.sh

Verify dispatch.sh handles the `local` value correctly. The SCP sling should skip delivery when REMOTE_HOST is `local`:

```bash
if [ -n "$REMOTE_HOST" ] && [ "$REMOTE_HOST" != "local" ] && [ "$REMOTE_HOST" != "localhost" ]; then
```

This already exists — just verify it works with our new env var values.

## Phase 6: Verify Everything

```bash
echo "=== NEURAL BRIDGE VERIFICATION ==="
echo "--- Env vars ---"
source ~/.zshrc
env | grep SYNCRESCENDENCE_REMOTE
echo "--- SSH to MBA ---"
ssh -o ConnectTimeout=5 macbook-air hostname
echo "--- dispatch.sh test (dry run) ---"
echo "Test: dispatch to ajna should SCP to macbook-air"
echo "Test: dispatch to commander should stay local"
echo "--- Watchdog bridge check ---"
ssh -o ConnectTimeout=5 macbook-air hostname && echo "BRIDGE: HEALTHY" || echo "BRIDGE: DOWN"
echo "--- CONFIRM routing test ---"
echo "Create dummy CONFIRM, verify SCP logic"
```

## Write Result
Write to: `-OUTBOX/psyche/RESULTS/RESULT-psyche-20260217-neural-bridge-infrastructure.md`
Write CONFIRM to: `-INBOX/commander/00-INBOX0/CONFIRM-psyche-20260217-neural-bridge-infrastructure.md`

Git commit: `git add -A && git commit -m "feat(bridge): genetic embedding of Neural Bridge — Psyche CTO" && git push`
