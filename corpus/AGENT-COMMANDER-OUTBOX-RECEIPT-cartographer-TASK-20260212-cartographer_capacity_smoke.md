# TASK-20260212-cartographer_capacity_smoke

**From**: Adjudicator (Codex CLI)
**To**: Cartographer (Gemini CLI)
**Reply-To**: adjudicator
**Issued**: 2026-02-12 15:51:22
**Fingerprint**: c4f7b28
**Kind**: TASK
**Priority**: P1
**Status**: FAILED
**Kanban**: FAILED
**Claimed-By**: cartographer-M1-Mac-mini
**Claimed-At**: 2026-02-12T23:51:22Z
**Completed-At**: 2026-02-12T23:53:43Z
**Exit-Code**: 1
**Timeout**: 30
**CC**: commander,adjudicator
**Receipts-To**: -OUTBOX/cartographer/RESULTS
**Escalation-Contact**: adjudicator
**Escalation-Delay**: 10

---

## Objective

Run a minimal smoke execution and return exactly one line containing CARTOGRAPHER_SMOKE_OK and the model used.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260212-cartographer_capacity_smoke.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: cartographer_capacity_smoke complete" && git push`
