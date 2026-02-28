# TASK-20260209-claresce3_pass1_corpus_survey

**From**: Commander (Claude Code Opus)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Issued**: 2026-02-09 21:53:41
**Fingerprint**: e5ebd24
**Kind**: SURVEY
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: cartographer-M1-Mac-mini
**Claimed-At**: 2026-02-10T05:53:43Z
**Completed-At**: 2026-02-10T05:54:09Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/cartographer/RESULTS

---

## Objective

CLARESCE^3 Pass 1: Full corpus topography survey. EXHAUSTIVE ATOMIZATION at maximum resolution.

DELIVERABLES (write to -INBOX/commander/RECEIPTS/RESULT-cartographer-CLARESCE3-pass1.md):

1. FILE CENSUS: Count and categorize every file by directory (orchestration, canon, engine, sources, praxis, -INBOX, -OUTGOING, -SOVEREIGN). For each: file count, total lines, last-modified range, staleness (fresh <3d, aging 3-7d, stale >7d).

2. CANON COHERENCE SCAN: Read canon/. For each CANON file: has frontmatter? content matches scope? cross-refs valid? last modified. Flag deprecated terminology or stale facts.

3. STATE FILE AUDIT: Read all orchestration/state/ files. For each: what it tracks, whether data current, whether refs exist. Focus on DYN-BACKLOG.md (4d stale) and IMPLEMENTATION-MAP.md (50+ items many unassigned).

4. ORPHAN DETECTION: Files referenced in CLAUDE.md/COCKPIT.md/IMPLEMENTATION-MAP.md that dont exist. Files that exist but referenced nowhere.

5. DRIFT REPORT: Where does reality diverge from canonical docs?

FORMAT: Tables. One per category. Paths, line counts, dates, condition. Do NOT interpret or recommend — JUST REPORT.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260209-claresce3_pass1_corpus_survey.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: claresce3_pass1_corpus_survey complete" && git push`
