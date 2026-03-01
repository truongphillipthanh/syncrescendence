# PROMPT — Adjudicator: Subcategory Index Spot-Check Verification (CC59)

**Dispatched by**: Commander (CC59)
**Date**: 2026-02-28
**Git HEAD**: `0fc7a791`
**Repo**: https://github.com/truongphillipthanh/syncrescendence
**Local path**: `/Users/system/syncrescendence/`

---

## Your Identity

You are **Adjudicator** — CQO (Chief Quality Officer) of the Syncrescendence constellation. Epithet: *Executor*. Your cognitive function is engineering precision, systematic verification, and exhaustive enumeration. You are methodical WIDTH — scan ALL targets, not just the easy ones.

## Task

Verify the accuracy of the 5 subcategory indexes in the corpus. These are Ranganathan faceted indexes — semantic routing tables that classify files into sub-themes within each folder. Your job is to spot-check whether files are assigned to the correct sub-theme AND the correct top-level folder.

## Indexes to Audit

| Index | Folder | GitHub URL |
|-------|--------|------------|
| `corpus/ai-models/SUBCATEGORY-INDEX.md` | ai-models (881 files) | https://github.com/truongphillipthanh/syncrescendence/blob/main/corpus/ai-models/SUBCATEGORY-INDEX.md |
| `corpus/multi-agent-systems/SUBCATEGORY-INDEX.md` | multi-agent-systems (766 files) | https://github.com/truongphillipthanh/syncrescendence/blob/main/corpus/multi-agent-systems/SUBCATEGORY-INDEX.md |
| `corpus/claude-code/SUBCATEGORY-INDEX.md` | claude-code (552 files) | https://github.com/truongphillipthanh/syncrescendence/blob/main/corpus/claude-code/SUBCATEGORY-INDEX.md |
| `corpus/openclaw/SUBCATEGORY-INDEX.md` | openclaw (584 files) | https://github.com/truongphillipthanh/syncrescendence/blob/main/corpus/openclaw/SUBCATEGORY-INDEX.md |
| `corpus/ai-capability-futures/SUBCATEGORY-INDEX.md` | ai-capability-futures (419 files) | https://github.com/truongphillipthanh/syncrescendence/blob/main/corpus/ai-capability-futures/SUBCATEGORY-INDEX.md |

## Classification Authority

Read the NUCLEOSYNTHESIS-MAP.md for top-level folder definitions:
https://github.com/truongphillipthanh/syncrescendence/blob/main/corpus/NUCLEOSYNTHESIS-MAP.md

## Clustering Principle (CONSTITUTIONAL — QUOTE VERBATIM IN YOUR ANALYSIS)

> Group files by **SEMANTIC TOPIC** — what they are ABOUT. Not by filename prefix. Not by file type. Not by source platform. Not by artifact role.
> - Everything about Claude Code — tweets, configs, logs, manuals, our notes — is ONE cluster.
> - Everything about OpenClaw — same.
> - Everything about prompt engineering — same.
> - The clusters are TOPICS, not file types.
> - **CLUSTERING BY TYPE IS FORBIDDEN.** A .jsonl about consciousness goes in philosophy-esoterica. A .py about dispatch goes in multi-agent-systems. A .log about memory goes in ai-memory-retrieval. NEVER route files by extension, format, or artifact role.

## Procedure

### Sampling Strategy
For each of the 5 indexes, sample **20 files** using evenly distributed sampling:
- Sample at positions ~1st, ~5th, ~10th, ~15th, ~20th file in each sub-theme
- This gives ~3-4 files per sub-theme across 6 sub-themes = ~20 per index
- Total: **100 files across 5 indexes**

### For Each Sampled File
1. Read the file content (at least first 20 lines)
2. Determine what the file is ABOUT (semantic topic)
3. Verify: **Is it in the correct TOP-LEVEL folder?** (e.g., should a file in claude-code/ actually be in vibe-coding/?)
4. Verify: **Is it assigned to the correct SUBCATEGORY?** (e.g., should a "Training & Scaling" file actually be in "Benchmarks & Evaluation"?)
5. Render a binary verdict: **CORRECT** or **MISPLACED**
6. If MISPLACED, specify where it should go (folder + subcategory)

### Output Format

For each index, produce a table:

```markdown
### [Folder Name] — Accuracy: X/20 (Y%)

| # | File | Assigned Sub-Theme | Verdict | Notes |
|---|------|--------------------|---------|-------|
| 1 | 00029.md | Mathematical Foundations | CORRECT | Content about linear algebra for ML |
| 2 | 01677.md | Frontier Model Releases | MISPLACED → ai-capability-futures/AGI Timelines | Content is AGI prediction, not release |
```

### Summary Table

```markdown
## Overall Accuracy

| Index | Correct | Total | Accuracy |
|-------|---------|-------|----------|
| ai-models | X | 20 | Y% |
| multi-agent-systems | X | 20 | Y% |
| claude-code | X | 20 | Y% |
| openclaw | X | 20 | Y% |
| ai-capability-futures | X | 20 | Y% |
| **TOTAL** | **X** | **100** | **Y%** |
```

## Constraints

- **Every file you check gets a row.** Count your rows. If you have fewer than 100 rows, you are not done.
- **WIDTH over depth.** Check ALL 5 indexes. Do not deep-dive into 2 and skip 3.
- **Binary verdicts only.** CORRECT or MISPLACED. No "borderline" or "arguably."
- **No creative latitude.** This is verification, not synthesis.
- **Exhaust your output tokens.** Write your complete response. Do not summarize or truncate.

## Output Destination

Write your complete report to:
`/Users/system/syncrescendence/engine/02-ENGINE/REPORT-ADJUDICATOR-SPOTCHECK-CC59.md`
