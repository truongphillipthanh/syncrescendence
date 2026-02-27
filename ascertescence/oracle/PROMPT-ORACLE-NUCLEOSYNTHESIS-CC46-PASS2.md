# ORACLE NUCLEOSYNTHESIS — CC46 PASS 2 OF 4: TOPOLOGY

**Date**: 2026-02-27
**From**: Commander (Claude Opus 4.6)
**To**: Oracle (Grok 4.2)
**Repo**: https://github.com/truongphillipthanh/syncrescendence/tree/main/corpus

---

## WHO YOU ARE

You are **Oracle** — the Recon agent of the Syncrescendence constellation. Your cognitive function is cultural divination: reconnaissance, thesis generation, grounding in human reality. You traverse GitHub with legendary capability.

## WHAT YOU ALREADY KNOW (from Pass 1)

In your previous pass, you identified the substance of this corpus — what kinds of things are in the pile. Here's what you found:

[COMMANDER INSERTS PASS 1 RESPONSE HERE]

## THE CORPUS

13,364 files in a single flat directory (`corpus/`). Full context from Pass 1 applies — the same project (Syncrescendence), the same 5-agent constellation, the same knowledge pipeline. See the Pass 1 prompt for prefix distribution, file types, and representative sample if needed.

**Key context for this pass**: The project has extensive internal referencing. Scripts import from each other. Configs reference file paths. Markdown documents mention other documents by name. The directory flattening broke many of these references (paths like `orchestration/state/DYN-TASKS.csv` became `DYN-TASKS.csv` in the flat corpus, but internal references still point to the old paths).

## YOUR TASK — PASS 2: TOPOLOGY

**What connects to what?**

You've seen what's in the pile. Now trace the wiring. Read files and follow their internal references:

1. **Import chains in Python files**: Open `.py` files (there are 126). What do they import from each other? What external libraries do they use? Which scripts are entry points vs. which are libraries?
   - Start with: `atom_cluster.py`, `auto_ingest_loop.sh`, `_write_configs.py`, `state_vector.py`, `batch_enrich.py`

2. **Config → process dependencies**: Open `.yaml`, `.json`, `.plist` files. What processes do they configure? Which scripts do they invoke? Which files do they reference?
   - Start with: `ENGINE-CAP-001-context_management.yaml`, `ARCH-LOCK_HIERARCHY.yaml`, `com.syncrescendence.auto-ingest-supervisor.plist`

3. **Document cross-references**: Open markdown files and find references to other files. Which documents are hubs (referenced by many)? Which are islands (referenced by nothing)?
   - Start with: `AGENTS.md` (in repo root, not corpus), `ARCH-AUTOMATION_MASTER_PLAN.md`, `REF-AGENTS.md`

4. **The SOURCE→META→EXTRACT pipeline**: These three prefixes account for 8,723 files (65% of the corpus). How do they relate to each other? Is there a 1:1:1 mapping? Open a few triplets (e.g., `SOURCE-20260203-*`, `META-EXTRACT-SOURCE-20260203-*`, `EXTRACT-SOURCE-20260203-*`) and trace the pipeline.

5. **Broken links**: What internal references point to paths that no longer exist? The flattening destroyed the directory structure but left all internal references intact. How bad is the breakage?

For each connection you find:
- **Quote the specific reference** from the file (the import line, the path string, the filename mention)
- **Say whether the reference is live or broken**
- **Rate the file as hub, spoke, or island**

**Write at maximum length.** What's the backbone — the 20-30 files that everything else depends on? What's the periphery — the mass that connects to nothing? What's the most connected file you found?
