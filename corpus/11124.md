# TASK-20260206-ghostty_spacing

**From**: dispatch
**To**: Ajna (OpenClaw Opus 4.5)
**Issued**: 2026-02-06 14:46:09
**Fingerprint**: f090d45
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: ajna-M1-Mac-mini
**Claimed-At**: 2026-02-07T05:30:42Z
**Completed-At**: 2026-02-07T05:30:47Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: psyche
**Receipts-To**: -OUTBOX/ajna/RESULTS

---

## Objective

Update Ghostty config to match requested GUI spacing: interpret iTerm letter spacing=101 and line spacing=130 as Ghostty adjustments: add to ~/.config/ghostty/config (and symlink ~/.ghostty/config):\n\nadjust-cell-width = 1%\nadjust-cell-height = 30%\n\nThen restart Ghostty / open new window to verify. Write RESULT receipt with what changed + host confirmation.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/ajna/RESULTS/RESULT-ajna-20260206-ghostty_spacing.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: ghostty_spacing complete" && git push`
