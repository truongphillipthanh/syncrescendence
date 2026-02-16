# TASK-20260216-research_corpus_multipass_sensing

**From**: Commander (Claude Code Opus)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Issued**: 2026-02-16 10:59:04
**Fingerprint**: 8e97caf
**Kind**: TASK
**Priority**: P1
**Status**: IN_PROGRESS
**Kanban**: IN_PROGRESS
**Claimed-By**: cartographer-Lisas-MacBook-Air
**Claimed-At**: 2026-02-16T18:59:05Z
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/cartographer/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

Execute a 5-pass deep sensing inspection of the 14 partitioned research notebook directories at 04-SOURCES/research-notebooks/. This reinforces Commander's research partitioning operation (SESSION 17, DA-RESEARCH-PARTITION-001).

**CONTEXT**: Commander partitioned 267 research files into 14 NotebookLM-ready directories per RESEARCH-CORPUS-CHUNKING-TAXONOMY.md. 59 articles were deep-read yielding 46 insights. Your job is to SENSE what was missed, miscategorized, or undervalued.

**REQUIRED READS**:
- 04-SOURCES/research-notebooks/MANIFEST.md (partition inventory)
- 00-ORCHESTRATION/state/impl/clarescence/RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md (28 insights)
- 00-ORCHESTRATION/state/impl/clarescence/RESEARCH-INSIGHTS-HIGH-SIGNAL.md (18 insights)
- 00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-16-research-partitioning-insights.md (operation record)

**FIVE PASSES**:

Pass 1 (Inventory Verification): For each of the 14 notebook directories, count files and compare against MANIFEST.md. Flag any count discrepancies. List any files that appear in multiple directories.

Pass 2 (Taxonomy Accuracy): Sample 5 files per directory (70 total). Read each file's title and first 500 words. Score whether it belongs in its assigned notebook category. Flag miscategorizations and propose corrections.

Pass 3 (Cross-Notebook Connections): Identify themes, authors, concepts, or frameworks that span 3+ notebooks. These are integration opportunities — they represent the corpus's emergent structure. Map at least 10 cross-cutting threads.

Pass 4 (Quality Gradient): Rank the top 15 highest-value articles across the entire corpus by insight density. Compare your ranking against Commander's VERY HIGH signal list. Flag any articles Commander rated highly that you disagree with, and any unrated articles you believe deserve VERY HIGH.

Pass 5 (Gap Detection): Given the corpus's coverage, what critical topics are MISSING? What should the Sovereign save next? Identify at least 5 gaps with recommended search queries.

**OUTPUT FORMAT**: Structured markdown with clear pass headers, tables where appropriate, and a SUMMARY section at the end with: (1) miscategorization count, (2) top cross-cutting themes, (3) your top 15 vs Commander's top 28, (4) gaps identified.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260216-research_corpus_multipass_sensing.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: research_corpus_multipass_sensing complete" && git push`
