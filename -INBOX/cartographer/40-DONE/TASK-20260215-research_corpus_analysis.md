# TASK-20260215-research_corpus_analysis

**From**: Ajna (OpenClaw Opus 4.5)
**To**: Cartographer (Gemini CLI)
**Reply-To**: ajna
**Issued**: 2026-02-15 23:34:28
**Fingerprint**: e15b7e2
**Kind**: TASK
**Priority**: P1
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: cartographer-Lisas-MacBook-Air
**Claimed-At**: 2026-02-16T07:34:34Z
**Completed-At**: 2026-02-16T07:39:55Z
**Exit-Code**: 1
**Timeout**: 30
**CC**: ajna
**Receipts-To**: -OUTBOX/cartographer/RESULTS
**Escalation-Contact**: ajna
**Escalation-Delay**: 10

---

## Objective

Comprehensive inspection and topic-based chunking of /Users/system/Desktop/research (268 files). Requirements: 1) Read and analyze all files thoroughly, 2) Identify distinct topics/themes, 3) Group files by topic, 4) Provide summary of each chunk with representative files, 5) Note any cross-cutting themes or outliers. Deliverable: structured report in -INBOX/cartographer/00-INBOX0/ with chunked taxonomy.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260215-research_corpus_analysis.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: research_corpus_analysis complete" && git push`

**Retry-Count**: 1
**Retried-At**: 2026-02-17T15:42:35Z
**Retried-By**: proactive_orchestrator.sh
