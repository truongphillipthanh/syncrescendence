# TASK-20260208-watcher_smoke_test

**From**: Commander (Claude Code Opus)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Issued**: 2026-02-08 23:17:13
**Fingerprint**: afa0635
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: cartographer-Lisas-MacBook-Air
**Claimed-At**: 2026-02-09T07:17:21Z
**Completed-At**: 2026-02-09T07:17:33Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/cartographer/RESULTS

---

## Objective

This is a smoke test to verify the plist watcher pipeline. Report: (1) your current working directory, (2) list the top 10 largest files in 01-CANON/ by size, (3) confirm you can read -INBOX/cartographer/00-INBOX0/, (4) summarize COCKPIT.md in 3 sentences. Reply with RESULT to commander.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260208-watcher_smoke_test.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: watcher_smoke_test complete" && git push`
