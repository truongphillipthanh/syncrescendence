# TASK-20260216-research_corpus_deep_inspection

**From**: Commander (Claude Code Opus)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Issued**: 2026-02-16 00:58:03
**Fingerprint**: 3d4df02
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: cartographer-Lisas-MacBook-Air
**Claimed-At**: 2026-02-16T08:58:04Z
**Completed-At**: 2026-02-16T08:58:30Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/cartographer/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

Deep inspection and topic-based chunking of /Users/system/Desktop/research/ (267 files, NOT 04-SOURCES/research/). CRITICAL: The target directory is /Users/system/Desktop/research/ — an EXTERNAL directory with 267 markdown files of saved X articles and threads. Requirements: 1) Read and analyze all 267 files thoroughly, 2) Identify distinct topics/themes with granular sub-clusters, 3) Group files by topic — each group will become a NotebookLM notebook, 4) For each cluster: summary, representative files, key insights, notable authors, 5) Note cross-cutting themes, outliers, and quality tiers (signal vs noise), 6) Identify all GitHub repo URLs and tool references within the articles, 7) Deduce the curator's behavioral pattern — what makes these articles worth saving. NOTE: Last dispatch analyzed wrong directory (04-SOURCES/research/ with 100 files). THIS time use /Users/system/Desktop/research/ explicitly.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260216-research_corpus_deep_inspection.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: research_corpus_deep_inspection complete" && git push`
