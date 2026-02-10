# TASK-20260209-claresce3v2_pass1_scaffold_audit

**From**: Commander (Claude Code Opus)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Issued**: 2026-02-09 23:51:14
**Fingerprint**: a3ee285
**Kind**: TASK
**Priority**: P1
**Status**: IN_PROGRESS
**Kanban**: IN_PROGRESS
**Claimed-By**: cartographer-M1-Mac-mini
**Claimed-At**: 2026-02-10T07:51:15Z
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/cartographer/RESULTS

---

## Objective

Full scaffold file-by-file audit across 00-ORCHESTRATION, 02-ENGINE, 04-SOURCES, 05-SIGMA, -SOVEREIGN, -INBOX, root files. For EACH file: (a) when last meaningfully updated, (b) what other files reference it, (c) value classification: VITAL (critical infrastructure), USEFUL (active reference), STALE (outdated, not referenced), ZOMBIE (infrastructure built but never operationalized), PROMOTE-TO-CANON (wisdom deserving canonical status). Output as a flat table. Exclude 01-CANON entirely (separate pass). Focus on: hook-generated state files, -OUTBOX vs -OUTGOING naming, 04-SOURCES/processed stagnation, 05-SIGMA empty directories, -SOVEREIGN decision aging.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260209-claresce3v2_pass1_scaffold_audit.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: claresce3v2_pass1_scaffold_audit complete" && git push`
