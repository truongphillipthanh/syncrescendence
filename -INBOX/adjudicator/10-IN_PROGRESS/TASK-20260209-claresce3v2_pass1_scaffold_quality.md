# TASK-20260209-claresce3v2_pass1_scaffold_quality

**From**: Commander (Claude Code Opus)
**To**: Adjudicator (Codex CLI)
**Reply-To**: commander
**Issued**: 2026-02-09 23:51:14
**Fingerprint**: a3ee285
**Kind**: TASK
**Priority**: P1
**Status**: IN_PROGRESS
**Kanban**: IN_PROGRESS
**Claimed-By**: adjudicator-Lisas-MacBook-Air
**Claimed-At**: 2026-02-10T07:51:29Z
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/adjudicator/RESULTS

---

## Objective

Scaffold quality standards check across 00-ORCHESTRATION, 02-ENGINE, 04-SOURCES, 05-SIGMA, -SOVEREIGN, -INBOX, root files. Assess: (a) naming convention compliance — are prefixes (ARCH-, DYN-, REF-, SCAFF-, FUNC-, PROMPT-) used consistently? (b) header/frontmatter consistency — do files follow a standard template? (c) broken internal links — grep for references to files that do not exist (e.g. ARCH-TECH_TREE_AUDIT.md is cited 3 times but does not exist), (d) orphan files — files referenced by nothing else, (e) duplicate/overlapping content between files. Output findings as categorized lists with file paths and line numbers. Exclude 01-CANON entirely.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-20260209-claresce3v2_pass1_scaffold_quality.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: claresce3v2_pass1_scaffold_quality complete" && git push`
