# TASK-20260209-claresce3v2_pass2_canon_standards

**From**: Commander (Claude Code Opus)
**To**: Adjudicator (Codex CLI)
**Reply-To**: commander
**Issued**: 2026-02-09 23:58:48
**Fingerprint**: c197198
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: adjudicator-Lisas-MacBook-Air
**Claimed-At**: 2026-02-10T07:59:01Z
**Completed-At**: 2026-02-10T07:59:18Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/adjudicator/RESULTS

---

## Objective

Canon standards audit: (a) frontmatter schema compliance across all 79 CANON files — check for id, title, domain, status, created, verified fields, (b) investigate CANON-00008 gap (missing file in sequence), (c) SN mirror completeness in sn/ vs main CANON files, (d) SN system health — do sn_encode.py/sn_decode.py/sn_expand.py work? Are DEF blocks complete? (e) dead internal links within canon. Output structured report.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-20260209-claresce3v2_pass2_canon_standards.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: claresce3v2_pass2_canon_standards complete" && git push`
