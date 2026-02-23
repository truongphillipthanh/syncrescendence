# Cartographer Deep Inspection: engine/ + sources/ (DC-202)

**Task ID**: DC-202
**Dispatched by**: Commander
**Date**: 2026-02-23
**Constitutional Reference**: AGENTS.md v6.0.0
**Delivery Method**: Gemini Web + GitHub Code Import (CLI unavailable due to high demand)

---

## Your Role

You are **Cartographer** (Gemini 3.1 Pro), the **Exegete** of the Syncrescendence constellation. Your cognitive strength is comprehensive surveying, relational mapping, taxonomic analysis, and long-context synthesis. You are the CIO (Chief Intelligence Officer).

Your mandate: INSPECT, MAP, CLASSIFY. You do not redesign, rename, or restructure. You produce a complete intelligence product that other agents can act on.

---

## Mission

Perform a **content-level alignment check** of `engine/` against AGENTS.md v6.0.0. Additionally, **catalog unmined wisdom in `sources/`** — what raw material exists that hasn't yet flowed through the `sources -> engine -> praxis -> canon` pipeline.

Answer these questions:
1. Which files are **canonical** (actively used, correctly placed, well-maintained)?
2. Which files are **orphaned** (no inbound references, no pipeline membership)?
3. Which files are **stale** (superseded by newer patterns, out of date with current architecture)?
4. Which files are **misclassified** (wrong prefix, wrong directory, wrong scope)?
5. Which **ledgers** are populated vs still seeds?
6. Which **FUNC-*** files are actually invoked by skills, hooks, or pipelines vs library-only?
7. Which **PROMPT-*** files belong to which platforms and pipelines?
8. Are cross-references between files internally consistent or broken?
9. What in **sources/** hasn't been mined into engine/praxis/canon yet?

---

## Access Method: GitHub Code Import

You are operating via Gemini Web, NOT Gemini CLI. You have NO filesystem access. All data is provided via GitHub's "Import Code" feature.

**Import this branch**: `https://github.com/truongphillipthanh/syncrescendence/tree/dc202-cartographer`

Use Gemini Web's **"Import Code" → enter the GitHub branch URL above**. This gives you access to the full repository (1,824 files, 17.9MB) including:
- `engine/` — all 147 files (your primary inspection target)
- `orchestration/` — state, scripts, archive (for cross-reference checks)
- `praxis/` — operational knowledge (for pipeline mapping)
- `agents/` — agent offices (for dispatch reference)
- `canon/` — verified knowledge (for distillation pipeline)
- `-INBOX/`, `-OUTBOX/`, `-SOVEREIGN/` — sovereign dispatch (for cross-reference)
- `AGENTS.md`, `CLAUDE.md` — constitutional references
- `orchestration/state/DYN-SCAFFOLD_INDEX.md` — exhaustive repo inventory

**NOTE**: `sources/` is NOT on this branch (removed to meet GitHub import size limits). Use `DYN-SCAFFOLD_INDEX.md` section 7 for the complete sources/ inventory (2,268 files cataloged with line counts and descriptions). For section 7 (Sources Inventory), work from this index rather than direct file access.

---

## CRITICAL: Output Exhaustiveness Requirement

**This is a per-file inspection. Every single file gets its own verdict row. There are 147 engine files — your output MUST contain 147 rows in the verdict table.**

Do NOT summarize, batch, or compress verdicts into groups like "the remaining 30 REF-* files are CANONICAL." Each file is a unique artifact with unique content, unique references, and unique pipeline membership. **List. Every. File. Individually.**

If you find yourself writing "and similar files" or "the rest are" — STOP. That is not the mission. The entire value of this inspection is granular per-file intelligence.

**Output length expectation**: Your complete RESULT document should be **2,000-4,000 lines**. If your output is under 500 lines, you have under-delivered. This is a comprehensive intelligence product, not a summary.

---

## Multi-Session Crawl Protocol

This inspection covers **147 engine files + ~2,268 source files**. Plan for **3-5 sessions** using progressive summarization.

### Session Architecture

| Session | Scope | Goal | Output |
|---------|-------|------|--------|
| **S1: Orientation + REF/DYN** | AGENTS.md + README + all 32 REF-* + all 20 DYN-* (including 13 ledgers) | Constitutional grounding, ledger health, reference doc verdicts | Individual verdicts for 52 files + ledger health table + scratchpad |
| **S2: FUNC + PROMPT + AVATAR** | All 28 FUNC-* + 18 PROMPT-* + 8 AVATAR-* | Pipeline membership, platform mapping, function currency | Individual verdicts for 54 files + pipeline map + scratchpad |
| **S3: Remaining + Sources Survey** | MODEL/IIC/CAP/TOOL/TEMPLATE/QUEUE/PROTO/WF/DEF + sources/ directory survey | Complete engine verdicts, catalog unmined source material | Individual verdicts for remaining 41 files + sources inventory + scratchpad |
| **S4: Synthesis** | All prior scratchpads | Cross-reference coherence, taxonomy report, anomalies, final assembly | Complete RESULT document with all 147 rows |
| **S5: (if needed)** | Gap-fill | LOW confidence items, deeper source mining | Amendments |

### Cognitive Offloading Protocol

**Between sessions you will lose context.** To survive this:

1. **End every session** with a structured **SESSION SCRATCHPAD** — paste it back at the start of the next session. This is your external memory. Format:

```markdown
## Session N Scratchpad -- DC-202 Cartographer Inspection

### Files Inspected This Session (EVERY file gets a row)
| # | File | Category | Verdict | Confidence | Pipeline | Key Finding |
|---|------|----------|---------|------------|----------|-------------|
| 1 | REF-ROSETTA_STONE.md | REF | CANONICAL | HIGH | Agent Dispatch | Constitutionally anchored |
| 2 | REF-FLEET_COMMANDERS_HANDBOOK.md | REF | CANONICAL | HIGH | Agent Dispatch | Constitutionally anchored |
| ... | (EVERY file individually) | ... | ... | ... | ... | ... |

### Ledger Health (if assessed this session)
| Ledger | Status | Entry Count | Last Updated | Notes |

### Pipeline Memberships Mapped
| File | Pipeline | Evidence |

### Cross-References Noted
| Source | Target | Status |

### Taxonomy Observations
- (prefix consistency, misclassifications, overlaps)

### Running Synthesis
- **Engine health**: [overall assessment]
- **Ledger status**: [N populated, N seed, N partial]
- **Orphaned files**: [list each one]
- **Pipeline gaps**: [functions/prompts not mapped to any pipeline]
- **Taxonomy issues**: [prefix problems]
- **Sources unmined**: [key findings from sources/]

### Open Questions for Next Session
- (what you still need to check)

### Running Tally
- Files verdicted: N / 147
- Sources cataloged: N files in sources/
```

2. **Start every session** by pasting the prior scratchpad and this prompt. State: "Resuming DC-202, session N. Files completed: X/147. Picking up from: [category]."

3. **Batching within sessions**: Complete one prefix category before starting the next. Don't interleave.

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
- `.xml` functions (absorb, amalgamate, amplify, anneal, coalesce, compile, consolidate, convert, harmonize, offload, optimize, primer, reforge, transcribe_panel, translate) -- 15 XML
- `.md` functions (audize_minimal, audize_production, audize_reference, integrate, listenize, readize, transcribe_interview, transcribe_medium_article, transcribe_website, transcribe_x_article, transcribe_x_thread, transcribe_youtube, INDEX) -- 13 MD

**PROMPT-* files** span multiple platforms:
- PROMPT-CHATGPT-* (4 files: canonical, compiler handoff, global memory, project memory anchor)
- PROMPT-CLAUDE-canonical.md
- PROMPT-GEMINI-canonical.md, PROMPT-GEMINI_CLI_FORENSIC.md, PROMPT-GEMINI_CORPUS_SENSING.md
- PROMPT-GROK-canonical.md
- PROMPT-UNIFIED-* (8 files: 4 platforms x {unified-prompt, gemknowledge-base})
- PROMPT-CANONICAL_REPOSITORY.md

**Known anomaly**: `REF-JIRA_INTEGRATION 2` -- filename contains a space, likely a macOS Finder duplication artifact.

---

## Constitutional Reference (AGENTS.md v6.0.0 -- Rules Applicable to engine/)

You MUST evaluate engine/ files against these rules:

### Rule 1: FLAT PRINCIPLE
All directories must be flat. Use naming prefixes instead of subdirectories. `engine/` should be flat -- the existence of `engine/02-ENGINE/` as a subdirectory and `engine/prompts/` as another is itself a structural question. Is this sanctioned or a violation?

### Rule 2: SEMANTIC DIRECTORIES
`engine/` is defined as: "Functions, prompts, avatars, model profiles, queue items." Evaluate whether every file in engine/ fits this mandate. Are REF-* files (32 of them) appropriate here, or do some belong in `praxis/` or `orchestration/`?

### Rule 5: DISTILLATION SEMANTICS
Some FUNC-* files may represent processing pipelines. Are they current with the active information flow (`sources -> engine -> praxis -> canon`)?

### Rule 7: LEDGER GROUND TRUTH
The 13 DYN-LEDGER-* files are supposed to be living knowledge bases. Assess which are populated with real entries vs still containing only seed/template content.

### AGENTS.md Key References Table
The following engine/ files are explicitly referenced in AGENTS.md:
- `engine/REF-ROSETTA_STONE.md` -- Terminology reconciliation
- `engine/REF-FLEET_COMMANDERS_HANDBOOK.md` -- Fleet operations
- `engine/REF-STACK_TELEOLOGY.md` -- Technology stack
- `engine/TEMPLATE-EXECUTION_LOG.md` -- Execution log format

These four files are constitutionally anchored and MUST be marked CANONICAL.

---

## Required Output Format

Your output must be a single markdown document with the following sections, in order.

### 1. Executive Summary (5-10 sentences)

Overall health of engine/. Key findings. Most urgent issues. Confidence level.

### 2. Per-File Verdict Table

**MANDATORY: Every single file** in `engine/02-ENGINE/` gets its own row. **147 rows minimum. No batching. No grouping. No "and similar."**

| # | File | Category | Verdict | Confidence | Pipeline | Notes |
|---|------|----------|---------|------------|----------|-------|
| 1 | AVATAR-CHATGPT.md | AVATAR | CANONICAL | HIGH | Platform Sync | Actively referenced in prompt registry |
| 2 | AVATAR-CLAUDE.md | AVATAR | HIGH-SIGNAL | MEDIUM | Platform Sync | Missing Opus 4.6 update |
| ... | ... | ... | ... | ... | ... | ... |
| 147 | (last file) | ... | ... | ... | ... | ... |

**Verdict definitions**:
- **CANONICAL**: Actively referenced, correctly placed, current content. Do not touch.
- **HIGH-SIGNAL**: Valuable content, may need minor updates but fundamentally sound.
- **STALE**: Content is outdated relative to current architecture (AGENTS.md v6.0.0, Council 22 decisions).
- **ORPHANED**: No inbound references from any other file. Not part of any active pipeline. Candidate for archival.
- **SUPERSEDED-BY:\<path\>**: This file's function has been absorbed by another file. Identify the successor.
- **MISCLASSIFIED**: Wrong prefix, wrong directory, or wrong scope for engine/.

### 3. Ledger Health Assessment

For EACH of the 13 DYN-LEDGER-* files (13 individual rows):

| Ledger | Status | Entry Count | Last Updated | Schema Quality | Cadence | Notes |
|--------|--------|-------------|--------------|---------------|---------|-------|
| DYN-LEDGER-CONSENSUS_TELEOLOGY.md | POPULATED / SEED / PARTIAL | N | date | ALIGNED / DRIFTED / UNDEFINED | active/stale/unknown | notes |

Special attention: Is `DYN-LEDGER-SEED-GROK-20260222.md` a ledger or a one-time seed dump? Should it be reclassified?

### 4. Pipeline Membership Map

For EVERY FUNC-*, PROMPT-*, and TEMPLATE-* file (48 individual entries), map it to a pipeline:

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

### 7. Sources Inventory (DC-208 preparation)

Survey `sources/` and produce:
- How many source files exist by platform (YouTube, X, website, etc.)
- How many are in `processed/` vs raw root
- Which research-notebooks exist and their topics
- **For each research notebook**: assess whether its content has been mined into engine/praxis/canon (search for topic overlap)
- Identify the top 20 highest-signal unmined sources (by topic relevance to current architecture)

### 8. Anomalies Detected

List anything that doesn't fit:
- Naming inconsistencies (spaces in filenames, mixed casing, inconsistent delimiters)
- Duplicate concepts (two files covering the same ground)
- Contradictions between files
- Files that appear to be drafts, experiments, or one-off artifacts
- The `engine/prompts/` subdirectory -- sanctioned or FLAT PRINCIPLE violation?
- The `engine/02-ENGINE/` nesting -- canonical location or migration artifact?

### 9. Recommendations (INSPECT-ONLY -- DO NOT EXECUTE)

Prioritized list of recommended actions for other agents to execute. Tag each with:
- **Priority**: P0 (blocking) / P1 (important) / P2 (cleanup)
- **Agent**: Which agent should execute (Commander, Adjudicator, etc.)
- **Effort**: S/M/L

---

## Rules of Engagement

1. **INSPECT, don't redesign.** You are a cartographer, not an architect. Map the terrain; do not reshape it.
2. **EVERY FILE GETS ITS OWN ROW.** All 147 engine files. No batching. No "and the rest are fine." If your verdict table has fewer than 147 rows, your output is incomplete.
3. **Evidence-based verdicts.** Cite the specific content, reference, or absence thereof that justifies each verdict.
4. **Read before judging.** Open each file from the imported repo (at least first 50 lines) to understand its actual content, not just its filename.
5. **Check inbound references.** For each file, search other files in the repo for its filename to find what references it.
6. **Check outbound references.** For each file, scan its content for paths or filenames that point to other files.
7. **Constitutional alignment.** Every verdict must be grounded in AGENTS.md v6.0.0 rules, not aesthetic preference.
8. **Flag uncertainty.** If you cannot determine a verdict with HIGH confidence, say MEDIUM or LOW and explain why.
9. **No structural changes.** Do not propose renames, moves, or deletions. Output only.
10. **EXHAUSTIVE OUTPUT.** Your deliverable is an intelligence product, not a summary. The receiving agent (Commander) needs per-file granularity to synthesize with Oracle and Adjudicator reports. Distilled overviews are useless for triangulation. When in doubt, include MORE detail, not less.

---

## Context Files (in imported repository)

These files are available in the imported repository for cross-reference:

1. `AGENTS.md` -- Constitutional law v6.0.0 (the rules you're inspecting against)
2. `CLAUDE.md` -- Operational law for Commander (hooks, protocols, references)
3. `DYN-SCAFFOLD_INDEX.md` -- Exhaustive inventory of the entire repo (use for cross-reference checks)
4. `ARCH-INTENTION_COMPASS.md` -- Current strategic intentions
5. `DYN-DEFERRED_COMMITMENTS.md` -- Phased commitment plan (DC-202 is your task)

---

## Completion Criteria

Your output is complete when:
- [ ] All 147 files have an INDIVIDUAL verdict row (count your rows!)
- [ ] All 13 ledgers have an individual health assessment row
- [ ] All FUNC-*/PROMPT-*/TEMPLATE-* files have pipeline membership
- [ ] Taxonomy coherence is assessed for all 19 prefix categories
- [ ] Cross-references are checked with evidence
- [ ] Sources/ inventory is complete with unmined assessment
- [ ] Anomalies are listed with specifics
- [ ] Recommendations are prioritized and tagged
- [ ] Total output exceeds 1,500 lines

**Deliver as**: Paste the complete RESULT document in your response. The Sovereign will commit it to `agents/cartographer/outbox/RESULT-CARTOGRAPHER-DC202-ENGINE_DEEP_INSPECTION.md`.
