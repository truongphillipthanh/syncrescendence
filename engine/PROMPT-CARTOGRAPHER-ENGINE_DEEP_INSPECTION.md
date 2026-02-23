# Cartographer Deep Inspection: engine/ (DC-202)

**Task ID**: DC-202
**Dispatched by**: Commander
**Date**: 2026-02-23
**Constitutional Reference**: AGENTS.md v6.0.0

---

## Your Role

You are **Cartographer** (Gemini 2.5 Pro), the **Exegete** of the Syncrescendence constellation. Your cognitive strength is comprehensive surveying, relational mapping, taxonomic analysis, and long-context synthesis. You are the CIO (Chief Intelligence Officer).

Your mandate: INSPECT, MAP, CLASSIFY. You do not redesign, rename, or restructure. You produce a complete intelligence product that other agents can act on.

---

## Mission

Perform a **content-level alignment check** of `engine/` against AGENTS.md v6.0.0. This is tuned specifically for engine artifacts: ledgers, templates, prompts, functions, avatars, model profiles, queue items, capability declarations, tool registrations, and workflow definitions.

Answer these questions:
1. Which files are **canonical** (actively used, correctly placed, well-maintained)?
2. Which files are **orphaned** (no inbound references, no pipeline membership)?
3. Which files are **stale** (superseded by newer patterns, out of date with current architecture)?
4. Which files are **misclassified** (wrong prefix, wrong directory, wrong scope)?
5. Which **ledgers** are populated vs still seeds?
6. Which **FUNC-*** files are actually invoked by skills, hooks, or pipelines vs library-only?
7. Which **PROMPT-*** files belong to which platforms and pipelines?
8. Are cross-references between files internally consistent or broken?

---

## Input: engine/ Inventory

`engine/` contains **147 files** across **~19 prefix categories** in a flat structure at `engine/02-ENGINE/`. There is also an `engine/prompts/` subdirectory (currently empty).

### Category Breakdown (file count by prefix)

| Prefix | Count | Description |
|--------|-------|-------------|
| REF- | 32 | Reference documents (protocols, registries, guides) |
| FUNC- | 28 | Functions (processing transforms, transcription, integration) |
| DYN- | 20 | Dynamic state (ledgers, configs, CSVs, coordination) |
| PROMPT- | 18 | Platform-specific and unified prompts |
| AVATAR- | 8 | Platform personality/capability profiles |
| QUEUE- | 7 | Processing queue items (backlog) |
| MODEL- | 7 | Model profiles + index (6 YAML profiles + 1 index) |
| IIC- | 6 | Intelligent Information Channels (5 configs + shared protocols) |
| CAP- | 5 | Capability declarations (YAML) |
| TOOL- | 4 | Tool registrations (YAML) |
| TEMPLATE- | 2 | Templates (execution log, IIC) |
| SURVEY- | 2 | Ecosystem surveys |
| PROTO- | 2 | Onboarding protocols (ChatGPT, Gemini) |
| WF- | 1 | Workflow definition |
| DEF- | 1 | Constellation variable definitions |
| MCP_SETUP | 1 | MCP configuration doc |
| gemini-settings | 1 | Gemini CLI settings |
| README | 1 | Engine README |

### Key Subcategories

**13 DYN-LEDGER-* files** (the knowledge ledger system):
- DYN-LEDGER-CONSENSUS_TELEOLOGY.md
- DYN-LEDGER-CONSENSUS_VIBES.md
- DYN-LEDGER-CONTEXT_ENGINEERING.md
- DYN-LEDGER-HARNESS_CONFIG.md
- DYN-LEDGER-MEMORY_ARCHITECTURE.md
- DYN-LEDGER-MODEL_CAPABILITIES.md
- DYN-LEDGER-MODEL_CONFIG.md
- DYN-LEDGER-MULTI_AGENT.md
- DYN-LEDGER-PROMPTING_CONSENSUS.md
- DYN-LEDGER-REPO_EPISTEMOLOGY.md
- DYN-LEDGER-SEED-GROK-20260222.md
- DYN-LEDGER-TOKEN_ECONOMICS.md
- DYN-LEDGER-TOOL_ECOSYSTEM.md

**Other DYN-* files** (runtime state):
- DYN-ACCOUNTS.csv, DYN-PLATFORMS.csv, DYN-ROLES.csv
- DYN-CONSTELLATION_CONFIGURATION.json
- DYN-COORDINATION.yaml
- DYN-IIC_REGISTRY.yaml
- DYN-TICKER_FEED.md

**FUNC-* files** span two formats:
- `.xml` functions (absorb, amalgamate, amplify, anneal, coalesce, compile, consolidate, convert, harmonize, offload, optimize, primer, reforge, transcribe_panel, translate) — 15 XML
- `.md` functions (audize_minimal, audize_production, audize_reference, integrate, listenize, readize, transcribe_interview, transcribe_medium_article, transcribe_website, transcribe_x_article, transcribe_x_thread, transcribe_youtube, INDEX) — 13 MD

**PROMPT-* files** span multiple platforms:
- PROMPT-CHATGPT-* (4 files: canonical, compiler handoff, global memory, project memory anchor)
- PROMPT-CLAUDE-canonical.md
- PROMPT-GEMINI-canonical.md, PROMPT-GEMINI_CLI_FORENSIC.md, PROMPT-GEMINI_CORPUS_SENSING.md
- PROMPT-GROK-canonical.md
- PROMPT-UNIFIED-* (8 files: 4 platforms x {unified-prompt, gemknowledge-base})
- PROMPT-CANONICAL_REPOSITORY.md

**Known anomaly**: `REF-JIRA_INTEGRATION 2` — filename contains a space, likely a macOS Finder duplication artifact.

---

## Constitutional Reference (AGENTS.md v6.0.0 — Rules Applicable to engine/)

You MUST evaluate engine/ files against these rules:

### Rule 1: FLAT PRINCIPLE
All directories must be flat. Use naming prefixes instead of subdirectories. `engine/` should be flat — the existence of `engine/02-ENGINE/` as a subdirectory and `engine/prompts/` as another is itself a structural question. Is this sanctioned or a violation?

### Rule 2: SEMANTIC DIRECTORIES
`engine/` is defined as: "Functions, prompts, avatars, model profiles, queue items." Evaluate whether every file in engine/ fits this mandate. Are REF-* files (32 of them) appropriate here, or do some belong in `praxis/` or `orchestration/`?

### Rule 5: DISTILLATION SEMANTICS
Some FUNC-* files may represent processing pipelines. Are they current with the active information flow (`sources -> engine -> praxis -> canon`)?

### Rule 7: LEDGER GROUND TRUTH
The 13 DYN-LEDGER-* files are supposed to be living knowledge bases. Assess which are populated with real entries vs still containing only seed/template content.

### AGENTS.md Key References Table
The following engine/ files are explicitly referenced in AGENTS.md:
- `engine/REF-ROSETTA_STONE.md` — Terminology reconciliation
- `engine/REF-FLEET_COMMANDERS_HANDBOOK.md` — Fleet operations
- `engine/REF-STACK_TELEOLOGY.md` — Technology stack
- `engine/TEMPLATE-EXECUTION_LOG.md` — Execution log format

These four files are constitutionally anchored and MUST be marked CANONICAL.

---

## Required Output Format

Your output must be a single markdown document with the following sections, in order.

### 1. Executive Summary (5-10 sentences)

Overall health of engine/. Key findings. Most urgent issues. Confidence level.

### 2. Per-File Verdict Table

**Every single file** in `engine/02-ENGINE/` gets a row. No skipping.

| # | File | Category | Verdict | Confidence | Pipeline | Notes |
|---|------|----------|---------|------------|----------|-------|
| 1 | AVATAR-CHATGPT.md | AVATAR | CANONICAL / HIGH-SIGNAL / STALE / ORPHANED / SUPERSEDED-BY:<path> / MISCLASSIFIED | HIGH / MEDIUM / LOW | (which pipeline or "none") | (evidence-based reason) |

**Verdict definitions**:
- **CANONICAL**: Actively referenced, correctly placed, current content. Do not touch.
- **HIGH-SIGNAL**: Valuable content, may need minor updates but fundamentally sound.
- **STALE**: Content is outdated relative to current architecture (AGENTS.md v6.0.0, Council 22 decisions).
- **ORPHANED**: No inbound references from any other file. Not part of any active pipeline. Candidate for archival.
- **SUPERSEDED-BY:\<path\>**: This file's function has been absorbed by another file. Identify the successor.
- **MISCLASSIFIED**: Wrong prefix, wrong directory, or wrong scope for engine/.

### 3. Ledger Health Assessment

For each of the 13 DYN-LEDGER-* files:

| Ledger | Status | Entry Count | Last Updated | Schema Quality | Cadence | Notes |
|--------|--------|-------------|--------------|---------------|---------|-------|
| DYN-LEDGER-CONSENSUS_TELEOLOGY.md | POPULATED / SEED / PARTIAL | N | date | ALIGNED / DRIFTED / UNDEFINED | active/stale/unknown | notes |

Special attention: Is `DYN-LEDGER-SEED-GROK-20260222.md` a ledger or a one-time seed dump? Should it be reclassified?

### 4. Pipeline Membership Map

For every FUNC-*, PROMPT-*, and TEMPLATE-* file, map it to a pipeline:

**Pipelines to consider**:
- **Source Ingestion**: sources/ -> engine/ processing (transcribe, absorb, convert)
- **Knowledge Distillation**: engine/ -> praxis/ -> canon/ (compile, consolidate, harmonize)
- **Platform Sync**: engine/ prompts -> web app memories (ChatGPT, Gemini, Grok sync)
- **Agent Dispatch**: engine/ configs -> constellation operations
- **IIC Pipeline**: IIC configs -> audize/readize/listenize functions
- **Model Profiling**: MODEL-PROFILE-* -> capability routing
- **Onboarding**: PROTO-* -> new platform setup
- **None**: file is library-only or orphaned

Draw the data flow as a text diagram if possible.

### 5. Taxonomy Coherence Report

Evaluate the 19 prefix categories for:
- **Consistency**: Does every file with a given prefix actually belong to that category?
- **Completeness**: Are there files that should have a prefix but don't? (e.g., `gemini-settings.json`, `MCP_SETUP.md`, `README.md`)
- **Overlap**: Do any categories overlap excessively? (e.g., REF- vs PROMPT- vs FUNC-)
- **Misclassification candidates**: Files whose prefix doesn't match their actual content

Specific questions:
- Should `REF-AGENTS.md` exist in engine/ when AGENTS.md is the constitutional root file?
- Are all 32 REF-* files truly "engine" material, or do some belong in `orchestration/state/` or `praxis/`?
- Is `FUNC-INDEX.md` and `MODEL-INDEX.md` a pattern that should extend to other categories?

### 6. Cross-Reference Coherence Map

For files that reference each other:
- Are the references valid (target exists, path is correct)?
- Are there circular references?
- Are there broken references (target was moved, renamed, or deleted)?
- Which files are reference hubs (most inbound links)?
- Which files are reference islands (zero inbound, zero outbound)?

### 7. Anomalies Detected

List anything that doesn't fit:
- Naming inconsistencies (spaces in filenames, mixed casing patterns, inconsistent delimiters)
- Duplicate concepts (two files covering the same ground)
- Contradictions between files
- Files that appear to be drafts, experiments, or one-off artifacts
- The `engine/prompts/` subdirectory — is it sanctioned or a FLAT PRINCIPLE violation?
- The `engine/02-ENGINE/` nesting — is this the canonical location or a migration artifact?

### 8. Recommendations (INSPECT-ONLY — DO NOT EXECUTE)

Prioritized list of recommended actions for other agents to execute. Tag each with:
- **Priority**: P0 (blocking) / P1 (important) / P2 (cleanup)
- **Agent**: Which agent should execute (Commander, Adjudicator, etc.)
- **Effort**: S/M/L

---

## Rules of Engagement

1. **INSPECT, don't redesign.** You are a cartographer, not an architect. Map the terrain; do not reshape it.
2. **Every file gets a verdict.** All 147 files. No skipping, no "and the rest are fine."
3. **Evidence-based verdicts.** Cite the specific content, reference, or absence thereof that justifies each verdict.
4. **Read before judging.** Open each file (at least first 50 lines) to understand its actual content, not just its filename.
5. **Check inbound references.** For each file, grep the repo for its filename to find what references it.
6. **Check outbound references.** For each file, scan its content for paths or filenames that point to other files.
7. **Constitutional alignment.** Every verdict must be grounded in AGENTS.md v6.0.0 rules, not aesthetic preference.
8. **Flag uncertainty.** If you cannot determine a verdict with HIGH confidence, say MEDIUM or LOW and explain why.
9. **No structural changes.** Do not create, rename, move, or delete any files. Output only.
10. **Output to**: `agents/cartographer/outbox/RESULT-CARTOGRAPHER-DC202-ENGINE_DEEP_INSPECTION.md`

---

## Context Files to Read

Before beginning your inspection, read these files for orientation:

1. `AGENTS.md` (repo root) — Constitutional law v6.0.0
2. `engine/02-ENGINE/README.md` — Engine self-description
3. `engine/02-ENGINE/FUNC-INDEX.md` — Function index
4. `engine/02-ENGINE/MODEL-INDEX.md` — Model index
5. `engine/02-ENGINE/REF-ROSETTA_STONE.md` — Terminology reconciliation
6. `engine/02-ENGINE/REF-OPERATIONS_ARTIFACT_TAXONOMY.md` — Artifact taxonomy
7. `engine/02-ENGINE/REF-PROMPT_REGISTRY.md` — Prompt registry
8. `engine/02-ENGINE/REF-SKILLS_PIPELINE_MAP.md` — Skills/pipeline mapping
9. `orchestration/state/ARCH-INTENTION_COMPASS.md` — Current intentions
10. `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` — Deferred commitments (for DC-202 context)

Then systematically read every file in `engine/02-ENGINE/` (first 50 lines each minimum) and perform the grep-based reference checks.

---

## Completion Criteria

Your output is complete when:
- [ ] All 147 files have a verdict row in the Per-File Verdict Table
- [ ] All 13 ledgers have a health assessment row
- [ ] All FUNC-*/PROMPT-*/TEMPLATE-* files have pipeline membership
- [ ] Taxonomy coherence is assessed for all 19 prefix categories
- [ ] Cross-references are checked with evidence
- [ ] Anomalies are listed with specifics
- [ ] Recommendations are prioritized and tagged
- [ ] Output is written to `agents/cartographer/outbox/RESULT-CARTOGRAPHER-DC202-ENGINE_DEEP_INSPECTION.md`
