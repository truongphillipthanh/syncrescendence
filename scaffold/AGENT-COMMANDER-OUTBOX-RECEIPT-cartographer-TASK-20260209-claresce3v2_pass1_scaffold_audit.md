# TASK-20260209-claresce3v2_pass1_scaffold_audit

**From**: Commander (Claude Code Opus)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Issued**: 2026-02-09 23:52:23
**Fingerprint**: 3e301bf
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: cartographer-M1-Mac-mini
**Claimed-At**: 2026-02-10T07:52:24Z
**Completed-At**: 2026-02-10T07:52:48Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/cartographer/RESULTS

---

## Objective

Full scaffold file-by-file audit across orchestration, engine, sources, praxis. For EACH file: last meaningful update, active references from other files, value classification (VITAL/USEFUL/STALE/ZOMBIE/PROMOTE-TO-CANON). Output as table. Exclude canon.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260209-claresce3v2_pass1_scaffold_audit.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: claresce3v2_pass1_scaffold_audit complete" && git push`
