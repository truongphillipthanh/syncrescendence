# SIEGE CC28 — Lane 7: Intention Pruning + Threshold Fix

**Agent**: Commander (Claude Code)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## OBJECTIVE

Two small, high-impact changes:
1. Apply the approved intention pruning (97 → 35 active intentions)
2. Lower the auto_promote threshold in atom_cluster.py to allow 1-3% auto_promote

## TASK 1: Apply Intention Pruning

Read `agents/commander/outbox/RESULT-CLAUDE-CC28-INTENTION_PRUNING_DRAFT.md` for the full cut list.

In `orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md`:
- Mark DONE intentions with `✅ DONE` status and move to an archive section at the bottom
- Mark STALE intentions with `⏸️ STALE` and move to archive section
- Mark MERGED intentions with `🔀 MERGED into INT-XXXX` and move to archive section
- Keep ACTIVE intentions in the main table
- Add a header comment: `<!-- Pruned CC28 2026-02-24: 97 → 35 active. 38 DONE, 14 STALE, 10 MERGED archived below. -->`

The archive section should be:
```markdown
## Archived Intentions (CC28 Pruning — 2026-02-24)

| INT-ID | Title | Status | Evidence |
```

## TASK 2: Lower Auto-Promote Threshold

In `orchestration/00-ORCHESTRATION/scripts/atom_cluster.py`:
- Find the auto_promote threshold/scoring logic
- The current run produced 0% auto_promote (too aggressive)
- Lower the threshold to produce approximately 1-3% auto_promote
- This is likely a score threshold or percentile cutoff — adjust appropriately
- Add a CLI flag `--auto-promote-percentile N` (default: 3) to make it tunable

## CONSTRAINTS
- Only modify: `ARCH-INTENTION_COMPASS.md` and `atom_cluster.py`
- Commit separately:
  1. `chore: CC28-L7 prune intentions 97→35 (Sovereign-approved)`
  2. `fix: CC28-L7 lower auto_promote threshold for 1-3% yield`
- Verify: after pruning, count active intentions (should be ~35)
- Verify: after threshold fix, describe the change in commit message
- Do NOT modify any files outside your lane
