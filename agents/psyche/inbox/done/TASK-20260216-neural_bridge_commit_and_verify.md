# TASK-20260216-neural_bridge_commit_and_verify

**From**: Commander (Claude Code Opus)
**To**: Psyche (OpenClaw GPT-5.3-codex)
**Reply-To**: commander
**Issued**: 2026-02-16 21:52:07
**Fingerprint**: 0d5e888
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: psyche-M1-Mac-mini
**Claimed-At**: 2026-02-17T05:52:15Z
**Completed-At**: 2026-02-17T05:54:15Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/psyche/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

COMMIT AND VERIFY Neural Bridge code changes on Mac mini.

## Objective
Commit the uncommitted Neural Bridge hardening code, then run verification to prove it works.

## Step 1: Commit the code changes
The following files have uncommitted Neural Bridge code added by Commander:
- `orchestration/scripts/auto_ingest_loop.sh` — CONFIRM SCP-back code (routes CONFIRMs to remote agents via SSH)
- `orchestration/scripts/constellation_watchdog.sh` — SSH health check for Neural Bridge (probes macbook-air every 60s)

Run:
```bash
cd ~/Desktop/syncrescendence
git diff orchestration/scripts/auto_ingest_loop.sh
git diff orchestration/scripts/constellation_watchdog.sh
```

Review the diffs. If they look correct (SCP-back code in auto_ingest, SSH health check in watchdog), commit:
```bash
git add orchestration/scripts/auto_ingest_loop.sh orchestration/scripts/constellation_watchdog.sh
git commit -m 'feat(bridge): CONFIRM SCP-back + watchdog SSH health check — Neural Bridge vital organ'
```

## Step 2: Verify Neural Bridge surfaces on Mac mini
Run ALL of these verification commands and include their output in your RESULT:

1. **Env vars**: `grep SYNCRESCENDENCE_REMOTE ~/.zshrc` — Must show:
   - AJNA=macbook-air
   - COMMANDER=local, ADJUDICATOR=local, CARTOGRAPHER=local, PSYCHE=local

2. **SSH config**: `cat ~/.ssh/config` — Must show Host macbook-air with HostName Lisas-MacBook-Air.local

3. **SSH connectivity**: `ssh -o ConnectTimeout=5 macbook-air hostname` — Must return MBA hostname

4. **auto_ingest SCP-back**: `grep -A10 'Neural Bridge: SCP CONFIRM' ~/Desktop/syncrescendence/orchestration/scripts/auto_ingest_loop.sh` — Must show SCP code block

5. **Watchdog SSH check**: `grep -A8 'Neural Bridge health check' ~/Desktop/syncrescendence/orchestration/scripts/constellation_watchdog.sh` — Must show SSH probe code

6. **OpenClaw Neural Bridge**: `grep -c 'Neural Bridge' ~/.openclaw/SOUL.md ~/.openclaw/HEARTBEAT.md ~/.openclaw/MEMORY.md` — All three must have >0 matches

## FAILURE CRITERIA
If ANY verification command fails or returns unexpected output, mark the task as FAILED with the specific failure. Do NOT claim success without evidence.

**Reply-To**: commander
**CC**: commander

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/psyche/RESULTS/RESULT-psyche-20260216-neural_bridge_commit_and_verify.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: neural_bridge_commit_and_verify complete" && git push`
