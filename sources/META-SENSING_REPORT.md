I will start by creating the necessary directories and saving the prompt file as requested. Then, I will list the files in the repository to begin the corpus analysis.

I will begin by listing the files in the repository to assess the corpus structure and volume.

I will read a set of files to investigate duplication, strays, overlaps, and identify potential issues for the corpus report.

# Corpus Sensing Report
**Generated**: Monday, February 2, 2026
**Files Analyzed**: 516
**Agent**: Cartographer (Gemini CLI)

## Executive Summary
The Syncrescendence corpus exhibits a highly matured "crystalline" structure with clear separation of concerns between Constitution (`canon`), Operations (`orchestration`), and Capability (`engine`). The system is currently in a "Foundation" phase (Modal 1), transitioning to "Amphitheatre" stage.

**Critical Findings**:
1.  **Intentional Duplication Architecture**: The `canon/sn/` directory mirrors the main Canon in "Semantic Notation" (SN), creating a persistent "Semantic Mirror" cluster. This is a feature, not a bug, but requires strict sync protocols.
2.  **Skill/Engine Redundancy**: A functional duplication exists between `engine/FUNC-*.md` and `.claude/skills/*.md`. The content for `readize` is identical. This suggests a deployment pattern where `engine` is the source of truth and `.claude/skills` is the runtime target, but this relationship needs formalization to prevent drift.
3.  **Intention Centralization**: `ARCH-INTENTION_COMPASS.md` is successfully functioning as the central registry for system intent, containing 50+ tracked items.
4.  **Nomenclature Discipline**: High adherence to `[PREFIX]-[ID]-[NAME]` convention, with minor drift in Sovereign workspace and legacy skill definitions.

**Recommended Priority Actions**:
1.  **Formalize Skill Deployment**: Define the relationship between `engine` and `.claude/skills`. If one is generated from the other, automate it. If not, consolidate.
2.  **Sovereign Filename Hygiene**: Rename `-SOVEREIGN/SOVEREIGN-007 PROJ-006 Ontology.md` to remove spaces.
3.  **Archive Protocol**: Move completed tasks (like `-INBOX/commander/TASK-20260202...`) to `orchestration/archive` post-completion.

---

## 1. Semantic Clusters Identified

### Cluster: The Semantic Mirror (Canon vs. SN)
-   **Core Document**: `canon/CANON-00000-SCHEMA-cosmos.md` (Human Readable, v2.3)
-   **Related**:
    -   `canon/sn/CANON-00000-SCHEMA-cosmos.md` (Machine Optimized, v1.0, 68% compression)
    -   Entire `canon/sn/` directory.
-   **Relationship**: **Semantic Duplicate (Intentional)**. The `sn/` folder contains Semantic Notation versions of the canonical documents for context-constrained agents.
-   **Recommendation**: **Keep Separate**. Maintain strict version lock. Ensure `sn/` files are updated whenever `canon` files change.

### Cluster: Agent Capability Definitions
-   **Core Document**: `engine/FUNC-readize.md` (Readability Transformer)
-   **Related**:
    -   `.claude/skills/readize.md` (Exact duplicate)
    -   `.claude/skills/audize.md` vs `engine/FUNC-audize_production.md` (Naming variance, likely similar content)
-   **Relationship**: **Deployment Redundancy**. `engine` appears to be the repository definition, while `.claude/skills` is the active configuration for the Claude CLI.
-   **Recommendation**: **Consolidate or Automate**. Treat `engine` as Source of Truth. Automate the generation of `.claude/skills` to ensure they never drift.

### Cluster: System Orientation
-   **Core Document**: `COCKPIT.md` (The "30,000ft View")
-   **Related**:
    -   `AGENTS.md` (Persona definitions)
    -   `orchestration/README.md`
    -   `CLAUDE.md` (Claude-specific config)
-   **Relationship**: **Elaboration**. `COCKPIT.md` is the entry point. `AGENTS.md` operationalizes the roles defined in Cockpit.
-   **Recommendation**: **Keep**. These root files are essential for agent context anchoring.

---

## 2. Strays & Orphans

| File | Location | Issue | Recommendation |
| :--- | :--- | :--- | :--- |
| `SOVEREIGN-007 PROJ-006 Ontology.md` | `-SOVEREIGN/` | **Filename Violation**. Contains spaces. | **Rename** to `SOVEREIGN-007-PROJ_006_Ontology.md` |
| `METRICS-STREAM-A.md` | `canon/sn/` | **Prefix Mismatch**. Lacks `CANON-` prefix common in this folder. | **Investigate**. Is this Canon or a transient stream log? If Canon, rename `CANON-METRICS_STREAM_A`. |
| `GEMINI-CORPUS-SENSING-PROMPT.md` | `orchestration/scripts/` | **Prefix Drift**. `GEMINI-` is not a standard script prefix. | **Rename** to `PROMPT-GEMINI_CORPUS_SENSING.md` and move to `engine` or keep in scripts with `SCIPT-` prefix. |

---

## 3. Scaffold Residue (Archive Candidates)

| File | Location | Evidence | Action |
| :--- | :--- | :--- | :--- |
| `TASK-20260202-plumbing_hardening.md` | `-INBOX/commander/` | Task file. Once `STATUS: COMPLETE`, it becomes residue. | **Archive** -> `orchestration/archive/TASK-20260202-plumbing_hardening.md` |
| `PROTO-Gemini-Onboarding.md` | `engine/` | `PROTO-` prefix suggests prototype/draft status. | **Review**. If fully implemented, canonize to `REF-` or `CANON-`. If abandoned, archive. |
| `PROTO-ChatGPT-Onboarding.md` | `engine/` | `PROTO-` prefix. | **Review**. Same as above. |

---

## 4. Canonization Candidates

| File | Current Location | Proposed Destination | Rationale |
| :--- | :--- | :--- | :--- |
| `ARCH-INTENTION_COMPASS.md` | `orchestration/state/` | `engine/REF-INTENTION_COMPASS.md` | This file has become the "Central Brain" of the operation. It is less "Archive" (dead) and more "Reference" (living). |
| `research/claude_code/*.md` | `sources/research/` | `praxis/practice/PRAC-CLAUDE_CODE_MASTERY.md` | Extensive research on "Claude Code" exists. Synthesize into a single "Practice" document. |
| `research/agents/*.md` | `sources/research/` | `canon/CANON-30420-MULTI_AGENT_ORCHESTRATION` | Sourced material should flow into the existing Multi-Agent Orchestration Canon. |

---

## 5. Hidden Intentions (Surfaced from `ARCH-INTENTION_COMPASS.md`)

| File | Location | Intention Found | Status |
| :--- | :--- | :--- | :--- |
| `ARCH-INTENTION_COMPASS.md` | `orchestration/state/` | **INT-MI19**: "Palantir-like ontology—the FINAL BOSS" | **Active (P1)**. High priority unexecuted strategic goal. |
| `ARCH-INTENTION_COMPASS.md` | `orchestration/state/` | **INT-MI15**: "Offload transcripts to Google ecosystem" | **Active (P2)**. Infrastructure task for "Account 2". |
| `ARCH-INTENTION_COMPASS.md` | `orchestration/state/` | **INT-1214**: "Deep Research: Claude Code + Anthropic Ecosystem" | **Deferred (P2)**. Ready for execution but stalled. |
| `ARCH-INTENTION_COMPASS.md` | `orchestration/state/` | **INT-1207**: "Manus before Perplexity" | **Deferred (P3)**. Platform prioritization decision. |

---

## 6. Nomenclature Violations

| File | Current Name | Issue | Suggested Fix |
| :--- | :--- | :--- | :--- |
| `SOVEREIGN-007 PROJ-006 Ontology.md` | [Spaces in Name] | Spaces break CLI ease-of-use. | `SOVEREIGN-007-PROJ_006_Ontology.md` |
| `.claude/skills/audize.md` | `audize.md` | Inconsistent with `engine/FUNC-audize_production.md`. | Align names if they represent the same function. |
| `engine/CAP-001...` | `CAP-001-context_management.yaml` | Lowercase after ID. Most CANONs use `CANON-XXXXX-UPPERCASE`. | `CAP-001-CONTEXT_MANAGEMENT.yaml` (Consistency check). |

---

## 7. Duplication Clusters

### Duplicate Set: Readability Transformer
-   **Keep (Source)**: `engine/FUNC-readize.md`
-   **Sync Target**: `.claude/skills/readize.md`
-   **Analysis**: exact content match. This is a "Deployment Copy". Ensure `engine` remains the master.

### Duplicate Set: Canon vs. SN
-   **Keep (Human)**: `canon/CANON-*.md`
-   **Keep (Machine)**: `canon/sn/CANON-*.md`
-   **Analysis**: Semantic duplicates. Required for system architecture. Do not delete.

---

## 8. Token Economics (Oversized Documents)

| File | Size (Est) | Issue | Recommendation |
| :--- | :--- | :--- | :--- |
| `canon/CANON-00000-SCHEMA-cosmos.md` | ~8.3k words | Large foundational document. | **Keep**. Essential for orientation. Compression exists in `sn/`. |
| `orchestration/state/DYN-SESSION_LOG.md` | Unknown (Log) | Unbounded growth. | **Rotate**. Implement a log rotation strategy (e.g., `DYN-SESSION_LOG-2026-Q1.md`). |
| `sources/TRANSCRIPT_RECONCILIATION.md` | Potentially Large | Accumulator file. | **Process & Clear**. If this accumulates raw text, process into `processed/` and clear. |

---

## 9. -INBOX Deep Dive

| File | Apparent Purpose | Recommended Action | Confidence |
| :--- | :--- | :--- | :--- |
| `commander/TASK-20260202-plumbing_hardening.md` | Directs infrastructure hardening. | **Execute & Archive**. Instructions are clear (P0 priority). | High |

---

## 10. Recommended Immediate Actions

1.  **[Priority 1] Infrastructure Hardening**: Execute the contents of `TASK-20260202-plumbing_hardening.md` (found in -INBOX). This addresses "plumbing" issues (lint, verify, watchers) that underpin all other work.
2.  **[Priority 2] Nomenclature Fix**: Rename `-SOVEREIGN/SOVEREIGN-007 PROJ-006 Ontology.md` to prevent script failures due to spaces.
3.  **[Priority 3] Skill Sync Definition**: Create a `REF-SKILL_DEPLOYMENT.md` in `engine` that explicitly states: "Source of Truth is engine/FUNC-*. `.claude/skills` are derived artifacts." This prevents "split brain" where we edit the skill file but forget the source function.

## Appendix: File Inventory Summary
-   **orchestration**: 30+ files (State, Scripts, Archive)
-   **canon**: 70+ files (Constitutional definitions) + `sn/` mirror
-   **engine**: 40+ files (Functions, Prompts, Configs)
-   **sources**: 100+ files (Research, Processed inputs)
-   **praxis**: 20+ files (Operational Knowledge)
-   **-INBOX/-OUTGOING**: Active transit zones.

*End of Report*
