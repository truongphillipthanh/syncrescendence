# Corpus Sensing Report
Generated: 2026-01-19
Files Analyzed: 808
Total Size: ~18 MB

## Executive Summary
The Syncrescendence repository is a highly structured distributed cognition system exhibiting both "crystalline" order in its Canon and "organic" growth in its active working zones. **Critical finding**: A significant "Shadow Canon" has emerged in `-INBOX` and `00-ORCHESTRATION/state`, containing architectural teleology that has not yet been codified into `01-CANON`. The system is successfully transitioning from a monolithic interaction model to a multi-agent "Constellation" architecture, but this transition has left substantial "scaffold residue" and "nomenclature drift" (specifically casing inconsistencies). **Priority Action**: Canonize the `-INBOX` architectural specs immediately to stabilize the new multi-agent paradigm, then perform a "Flat Principle" enforcement sweep to clean up directory nesting violations.

## 1. Semantic Clusters Identified

### Cluster: Architectural Teleology (Constellation)
- **Core Document**: `01-CANON/CANON-25200-CONSTELLATION_ARCH-lattice.md` — The canonical definition.
- **Related**:
  - `-INBOX/constellation-teleology.md` — **Elaboration**: Detailed philosophical underpinning, likely newer than Canon.
  - `-INBOX/constellation-architecture-v1.md` — **Outdated Version?**: Needs diff against Canon.
  - `-INBOX/constellation-bifurcated-architecture.jsx` — **Fragment**: Code/Diagram representation.
- **Recommendation**: **Consolidate** all `-INBOX` constellation artifacts into updated `CANON-25200` or new `CANON-252xx` series.

### Cluster: Memory Architecture
- **Core Document**: `01-CANON/CANON-25000-MEMORY_ARCH-lattice.md`.
- **Related**:
  - `-INBOX/memory-architecture-teleology.md` — **Elaboration**: The "why" behind the structure.
  - `-INBOX/memory-architecture-matrix.md` — **Elaboration**: The operational rules.
  - `02-ENGINE/memory/acumen-memory-config.md` — **Implementation**: Specific instance config.
- **Recommendation**: **Canonize** the `-INBOX` items into `01-CANON/CANON-250xx` series to formalize the new memory tiering.

### Cluster: Evaluative Lenses (18 Lenses)
- **Core Document**: `00-ORCHESTRATION/state/REF-STANDARDS.md` — The constitutional definition of the 18 lenses.
- **Related**:
  - `01-CANON/CANON-00007-EVALUATION-cosmos.md` — **Canonical Reference**: High-level principles.
  - `01-CANON/CANON-00015-MACROSCOPIC_NARRATIVES-cosmos.md` — **Expansion**: Narrative lenses (19-30).
  - `00-ORCHESTRATION/lens_governance.md` — **Fragment**: Potential duplicate or orphaned governance note.
- **Recommendation**: **Consolidate** `lens_governance.md` into `REF-STANDARDS.md`. Ensure `CANON-00015` is explicitly linked as the expansion set.

## 2. Strays & Orphans

| File | Location | Issue | Recommendation |
|------|----------|-------|----------------|
| `AGENTS.md` | (root) | Orphan at root; should be in `02-ENGINE` or `01-CANON`. | **Move** to `02-ENGINE/registries/` |
| `lens_governance.md` | `00-ORCHESTRATION/` | Unprefixed, small (2.1K). Likely redundant to `REF-STANDARDS.md`. | **Absorb** into `REF-STANDARDS.md` then **Delete** |
| `model_orchestration.md` | `00-ORCHESTRATION/` | Unprefixed, small (1.4K). | **Archive** or **Canonize** into `CANON-30420` |
| `cognitive_core.md` | `00-ORCHESTRATION/` | Unprefixed. "Cognitive Core" is a key concept. | **Canonize** to `CANON-00018-COGNITIVE_CORE` or **Delete** if obsolete |
| `decision_atoms.md` | `00-ORCHESTRATION/` | Unprefixed. | **Investigate** content, likely merge to `REF-DECISION_MAKING` |
| `mcp.json.template` | `06-EXEMPLA/` | Lowercase name. | **Rename** to `TEMPLATE-MCP_CONFIG.json` |

## 3. Scaffold Residue (Archive Candidates)

| File | Location | Evidence | Action |
|------|----------|----------|--------|
| `SCAFF-IIC_RECONNAISSANCE.md` | `00-ORCHESTRATION/state/` | "SCAFF-" prefix denotes temporary scaffolding. | ARCHIVE → `05-MEMORY/SCAFF-IIC_RECONNAISSANCE.md` |
| `DIRECTIVE-017` through `DIRECTIVE-030` | `00-ORCHESTRATION/directives/` | Old directives (Oracle 9 era). | **Batch Archive** to `05-MEMORY/DIRECTIVES/` (if folder permitted) or leave as historical record if policy dictates |
| `EXECUTION_LOG-2025-*` | `00-ORCHESTRATION/execution_logs/` | Last year's execution logs. | **Consider Archiving** to `05-MEMORY/LOGS-2025/` to reduce clutter |

## 4. Canonization Candidates

| File | Current Location | Proposed Destination | Rationale |
|------|------------------|---------------------|-----------|
| `constellation-teleology.md` | `-INBOX/` | `01-CANON/CANON-25210-CONSTELLATION_TELEOLOGY-lattice.md` | Foundational architectural philosophy for the current phase. |
| `memory-architecture-teleology.md` | `-INBOX/` | `01-CANON/CANON-25010-MEMORY_TELEOLOGY-lattice.md` | Defines the "why" of the new memory system. |
| `INTERACTION_DYNAMICS_SPECIFICATION.md` | `-INBOX/` | `01-CANON/CANON-30460-INTERACTION_DYNAMICS-comet.md` | High-value spec (40KB) defining agent interaction rules. |
| `COCKPIT.md` | `-INBOX/` | `02-ENGINE/DYN-COCKPIT.md` | Duplicate of root COCKPIT? If newer, update root. |
| `CONFIGURATION_REGISTRY.md` | `-INBOX/` | `02-ENGINE/registries/REF-CONFIGURATION_REGISTRY.md` | Operational registry belonging in active context. |

## 5. Hidden Intentions (Surfaced from Archive)

| File | Location | Intention Found | Status |
|------|----------|-----------------|--------|
| `SCAFF-ORACLE09_FINAL_CULMINATION.md` | `05-MEMORY/` | "Transcript Ingestion: 184 raw sources... Only 8 processed." | **FAILED MISSION**. This debt is still unpaid. Sources need processing. |
| `SCAFF-ORACLE09_FINAL_CULMINATION.md` | `05-MEMORY/` | "Flat Principle: All directories must be FLAT." | **VIOLATED**. Nested dirs exist in `-OUTGOING`, `04-SOURCES/raw/claudecode`, etc. |
| `ARCH-ORACLE10_CONTEXT_v4.md` | `05-MEMORY/` | "Claude 2/3 web app utilization... Scheduled utilization." | **UNEXECUTED**. No evidence of systematic Web App usage in current logs. |
| `RESEARCH-20260108-claude_code_optimization.md` | `05-MEMORY/` | "Deep research outputs... Distill unique value into CANON." | **PENDING**. Check if this 28KB file has been distilled. |

## 6. Nomenclature Violations

| File | Current Name | Issue | Suggested Fix |
|------|--------------|-------|---------------|
| `blitzkrieg_finalize.sh` | `00-ORCHESTRATION/scripts/` | Lowercase. | `BLITZKRIEG_FINALIZE.sh` (or accept lowercase for scripts?) |
| `coordination.yaml` | `02-ENGINE/` | Lowercase. Critical config. | `COORDINATION.yaml` (match `MCP_SETUP.md`) |
| `burndown.csv` | `00-ORCHESTRATION/state/` | Lowercase. | `DYN-BURNDOWN.csv` |
| `projects.csv` | `00-ORCHESTRATION/state/` | Lowercase. | `DYN-PROJECTS.csv` |
| `tasks.csv` | `00-ORCHESTRATION/state/` | Lowercase. | `DYN-TASKS.csv` |
| `creator_bios.md` | `04-SOURCES/` | Lowercase. | `REF-CREATOR_BIOS.md` |
| `filename_mapping.csv` | `04-SOURCES/` | Lowercase. | `REF-FILENAME_MAPPING.csv` |
| `sources.csv` | `04-SOURCES/` | Lowercase. | `DYN-SOURCES.csv` |

## 7. Duplication Clusters

### Duplicate Set: Cockpit
- **Keep**: `COCKPIT.md` (Root) — The entry point.
- **Archive/Delete**:
  - `-INBOX/COCKPIT.md` — **Duplicate**. Check for diffs, merge updates to root, then delete.

### Duplicate Set: Context Handoff
- **Keep**: `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_FINAL.md` — Looks definitive.
- **Archive/Delete**:
  - `00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT.md` — Older version?
  - `00-ORCHESTRATION/ORACLE12_CONTEXT.md` — Why is this at root of orchestration? Move to `oracle_contexts/`.

## 8. Token Economics (Oversized Documents)

| File | Size | Issue | Recommendation |
|------|------|-------|----------------|
| `CANON-00005-SYNCRESCENDENCE-cosmos.md` | 111KB | >100KB is critical context risk. | **Split** into `00005-A-THEORY` and `00005-B-PRACTICE`. |
| `CANON-00012-MODAL_SEQUENCE-cosmos.md` | 104KB | Exceeds safe context injection. | **Compress** verbose examples into `06-EXEMPLA`. |
| `CANON-31141-FIVE_ACCOUNT...md` | 117KB | Massive monolithic doc. | **Atomize** into per-account specs. |
| `CANON-31143-FEED_CURATION...md` | 116KB | Massive monolithic doc. | **Extract** lists/taxonomies to `REF-` documents. |
| `creator_bios.md` | 114KB | Pure reference data. | **Keep** but ensure agents only read relevant sections (grep/search). |

## 9. -INBOX Deep Dive

Current -INBOX contents requiring Principal decision:

| File | Size | Apparent Purpose | Recommended Action | Confidence |
|------|------|------------------|-------------------|------------|
| `INTERACTION_DYNAMICS_SPECIFICATION.md` | 40KB | Protocol definition for agent interaction. | **CANONIZE** to `01-CANON/` | High |
| `constellation-teleology.md` | 32KB | Architectural philosophy. | **CANONIZE** to `01-CANON/` | High |
| `memory-architecture-teleology.md` | 34KB | Architectural philosophy. | **CANONIZE** to `01-CANON/` | High |
| `constellation-bifurcated-architecture.jsx` | 34KB | React component/Diagram. | **MOVE** to `04-SOURCES/assets/` or `06-EXEMPLA/` | Medium |
| `last_5_interactions.zip` | 20KB | Context capture. | **ARCHIVE** to `05-MEMORY/` | High |
| `state-fingerprint-solution.md` | 19KB | Solution proposal. | **OPERATIONALIZE** or **ARCHIVE** | Medium |
| `DIR-20260120-EXECUTION-LOG-INFRASTRUCTURE.md` | 8.9KB | Forward-dated Directive? | **MOVE** to `00-ORCHESTRATION/directives/` | High |
| `GEMINI-CORPUS-SENSING-PROMPT.md` | 6.7KB | This prompt. | **MOVE** to `00-ORCHESTRATION/scripts/` or `02-ENGINE/prompts/` | High |

## 10. Recommended Immediate Actions

1. **[Priority 1]**: **Absorb -INBOX Canon**. The `teleology` and `specification` documents in `-INBOX` are heavy architecture that belongs in `01-CANON`. Moving them clears `-INBOX` and stabilizes the "Constellation" definition.
2. **[Priority 2]**: **Token Decompresion**. `CANON-00005`, `CANON-31141`, and `CANON-31143` are too large (100KB+). They risk truncating context. Split them logically immediately.
3. **[Priority 3]**: **Flat Principle Sweep**. `04-SOURCES/raw/claudecode` has 3 levels of nesting. `00-ORCHESTRATION/state` is flat (good), but `-OUTGOING` contains uncompressed folders. Enforce flattening or zipping of old `-OUTGOING` bundles.

## Appendix: File Inventory by Directory

- **-INBOX**: 28 files (High signal density, needs triage)
- **-OUTGOING**: 66 files (Mostly reports and zips)
- **00-ORCHESTRATION**: 182 files (Directives and Logs dominate)
- **01-CANON**: 79 files (Massive token weight here)
- **02-ENGINE**: 83 files (Functional execution layer)
- **03-QUEUE**: 7 files (Light load)
- **04-SOURCES**: 279 files (Bulk of storage, `raw/` has 199 items)
- **05-MEMORY**: 81 files (Historical record)
- **06-EXEMPLA**: 5 files (Templates)
- **Root**: 4 files (Clean)

**Total**: 808 Files
