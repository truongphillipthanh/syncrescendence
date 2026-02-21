# TASK-20260221-corpus_freshness

**From**: orchestrator
**To**: Cartographer (Gemini CLI)
**Reply-To**: orchestrator
**Issued**: 2026-02-21 12:40:37
**Fingerprint**: ace2d24
**Kind**: TASK
**Priority**: P1
**Failure-Reason**: No capacity available for model
**Status**: FAILED
**Kanban**: FAILED
**Claimed-By**: cartographer-M1-Mac-mini
**Claimed-At**: 2026-02-21T20:40:39Z
**Completed-At**: 2026-02-21T20:52:17Z
**Exit-Code**: 75
**Timeout**: 30
**CC**: —
**Receipts-To**: -OUTBOX/cartographer/RESULTS
**Escalation-Contact**: orchestrator
**Escalation-Delay**: 10

---

## Objective

Survey corpus freshness and broken references. Report stale files and missing links.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260221-corpus_freshness.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: corpus_freshness complete" && git push`
