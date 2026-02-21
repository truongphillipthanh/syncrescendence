# TASK-20260221-infrastructure_audit

**From**: orchestrator
**To**: Psyche (OpenClaw GPT-5.3-codex)
**Reply-To**: orchestrator
**Issued**: 2026-02-21 12:40:36
**Fingerprint**: ace2d24
**Kind**: TASK
**Priority**: P1
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: psyche-M1-Mac-mini
**Claimed-At**: 2026-02-21T21:10:54Z
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: —
**Receipts-To**: -OUTBOX/psyche/RESULTS
**Escalation-Contact**: orchestrator
**Escalation-Delay**: 10

---

## Objective

Run infrastructure coherence audit: launchd templates vs deployed, watchdog status, Docker restart policies, auto-ingest supervisor status.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/psyche/RESULTS/RESULT-psyche-20260221-infrastructure_audit.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: infrastructure_audit complete" && git push`

---
**Failure-Code**: STALE_TIMEOUT
**Failure-Class**: timeout
**Failure-Retryable**: true
**Failure-Reason**: stale_in_progress_timeout
**Failed-At**: 2026-02-21T22:09:44Z
**Stale-Duration**: 3530s (threshold: 1800s)
**Moved-By**: proactive_orchestrator.sh

**Retry-Count**: 1
**Retried-At**: 2026-02-21T22:20:02Z
**Retried-By**: proactive_orchestrator.sh
