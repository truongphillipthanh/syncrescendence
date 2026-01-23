# CANON FORENSIC AUDIT: EVIDENCE PACK
**Date**: 2026-01-20
**Surveyor**: Gemini CLI
**Scope**: 01-CANON/ (71 files), 02-ENGINE/ (Shadow Canon check)

---

## 1. CRITICAL MISALIGNMENTS (Top 10)

1.  **Perishable Strategy in Eternal Scripture**: `CANON-00005` (Syncrescendence) contains a "Current Strategic Position" section dated Jan 2026. **Violation**: Canon is for *what is true*, not *what is current*. This belongs in `00-ORCHESTRATION/state/DYN-STRATEGY.md`.
2.  **Tech Stack Volatility**: `CANON-30000` (Intelligence Chain) embeds specific model versions ("Claude 4.x, GPT-5.x") and current capabilities. **Violation**: Model specifics age in weeks; Canon should define *capabilities* abstractly, while `02-ENGINE/models/` tracks versions.
3.  **Shadow Canon - Memory Architecture**: `02-ENGINE/memory/REF-MEMORY_ARCHITECTURE_MATRIX.md` is a 5KB+ foundational architecture document. **Violation**: This defines the "Memory Lattice" behavior and belongs in `01-CANON/CANON-25000-MEMORY_ARCH-lattice.md` or as a satellite `CANON-25010`.
4.  **Shadow Canon - Agent Configuration**: `02-ENGINE/registries/REF-AGENTS.md` defines "Constitutional Rules" and directory structure. **Violation**: Constitutional definitions belong in `CANON-00010-OPERATIONS` or `CANON-00017-AGENTIC_CONSTITUTION`.
5.  **Monolithic Overload**: `CANON-00005` is >1000 lines (>100KB tokens). **Violation**: Exceeds safe context injection limits for most agents, risking truncation of core axioms.
6.  **Redundant Schema Definitions**: `CANON-00000` defines the entire hierarchy, but individual files (e.g., `CANON-30000`) repeat generic definitions of "What is a Chain?" before getting to specific content.
7.  **Orphaned "Comet"**: `CANON-30460-INTERACTION_DYNAMICS-comet.md` exists but isn't referenced in the `CANON-00000` schema manifest (based on sampled content).
8.  **Inconsistent "Context" Anchoring**: `CANON-20000` anchors to `Syncrescendence-complete.md (v1.0)`, a file that no longer exists in the file listing. **Violation**: Broken provenance chain.
9.  **Mixed Modes**: `CANON-00005` explicitly toggles between "Mythopoetic" and "Operational" modes within the same text. **Violation**: While intentional, it bloats tokens. Operational protocols should likely split to `CANON-00010`.
10. **Unifying "Cognitive Core"**: `00-ORCHESTRATION/cognitive_core.md` exists as a stray file but describes a central canonical concept. **Violation**: Should be `CANON-10000` or integrated into `CANON-00005`.

---

## 2. CONSOLIDATION CANDIDATES

| Primary File | Absorb From | Rationale |
|--------------|-------------|-----------|
| `CANON-00010-OPERATIONS` | `02-ENGINE/registries/REF-AGENTS.md` | The "Constitutional Rules" in REF-AGENTS are operational canon. |
| `CANON-25000-MEMORY_ARCH` | `02-ENGINE/memory/REF-MEMORY_ARCHITECTURE_MATRIX.md` | The matrix is the architectural definition of the memory lattice. |
| `CANON-00005-SYNCRESCENDENCE` | `00-ORCHESTRATION/cognitive_core.md` | The "Cognitive Core" is the central hypergiant described in 00005. |
| `CANON-30300-TECH_STACK` | `02-ENGINE/models/MODEL_INDEX.md` | Absorb the *taxonomy* of models, leave the *profiles* in Operational. |

---

## 3. SPLIT CANDIDATES

| Monolith | Split Into | Rationale |
|----------|------------|-----------|
| `CANON-00005-SYNCRESCENDENCE` | `CANON-00005-PRIMER` (Theory)<br>`CANON-00005-MANUAL` (Practice) | Theory/Practice separation saves tokens. "Preamble" alone is massive. |
| `CANON-31141-FIVE_ACCOUNT` | `CANON-31141-ACCOUNT_STRATEGY`<br>`02-ENGINE/specs/REF-ACCOUNT_SPECS` | High-level strategy vs. perishable platform configuration details. |
| `CANON-34110-CURRICULUM` | `CANON-34110-PEDAGOGY`<br>`CANON-34120-SYLLABUS` | Separate the "How we teach" from the "What we teach" (content vs. method). |

---

## 4. EXPULSION CANDIDATES (Content to Move)

| Content Segment | Current Location | Destination |
|-----------------|------------------|-------------|
| "Current Strategic Position" | `CANON-00005` | `00-ORCHESTRATION/state/DYN-STRATEGY.md` |
| "Current Strategic Position" | `CANON-30000` | `00-ORCHESTRATION/state/DYN-TECH_STRATEGY.md` |
| "Model Version Specifics" | `CANON-30000` | `02-ENGINE/models/MODEL_INDEX.md` |
| "Maintenance Log" | All CANON files | `00-ORCHESTRATION/blackboard/audits/` (Link only) |

---

## 5. MISSING ELEMENTS (Cosmology Gaps)

1.  **CANON-12000**: Core/Facet bridge. We have `10000` (Body) and `11000` (Facets), but no cohesive binding for the "Core" tier.
2.  **CANON-25010**: Memory Teleology. We have `25000` (Arch), but `25010` is visible in file list (good), need to confirm `25020` (Memory Dynamics).
3.  **CANON-90000**: Future History. We have `99000` (Historical/Past), but no "Eschatology" or "Future Trajectory" canon beyond the strategic plan.
4.  **Operational Genesis**: `CANON-00010` exists but is referenced as "Operational Genesis" in schemas—needs to be robust enough to replace the stray `BLITZKRIEG_PROTOCOL.md` concepts.

---

## 6. TOKEN WASTE ESTIMATE

| Category | Est. Waste per File | Total Waste (71 files) |
|----------|---------------------|------------------------|
| Perishable "Status" Sections | ~500 tokens | ~35,000 tokens |
| Redundant "Preamble" | ~200 tokens | ~14,000 tokens |
| "Maintenance Log" History | ~300 tokens | ~21,000 tokens |
| Mythopoetic/Operational Duplication | ~1000 tokens (in top 5 files) | ~5,000 tokens |
| **TOTAL** | | **~75,000 tokens** |

*Equivalent to ~2 full context windows of a standard LLM, or 10% of the entire CANON.*

---

## 7. RECOMMENDED RESTRUCTURE

### A. Immediate Hygiene (Blitzkrieg 43)
1.  **Strip "Current Strategic Position"** sections from 00005, 30000, and others. Move to `DYN-STRATEGY`.
2.  **Strip "Maintenance Logs"**. Replace with a single "Last Updated: YYYY-MM-DD" line.
3.  **Move Shadow Canon**. Relocate `REF-MEMORY_ARCHITECTURE_MATRIX.md` to `CANON-25020-MEMORY_MATRIX-lattice.md`.

### B. Structural Bifurcation (The "Testament" Split)
Split the CANON into two distinct sub-directories to manage context loading:

1.  `01-CANON/TESTAMENT-THEORY/`: The eternal "Why" and "What". (Cosmos, Lattice, Chains - Theory).
2.  `01-CANON/TESTAMENT-PRAXIS/`: The enduring "How". (Operations, Protocols, Methods).

### C. Celestial Tier Reinforcement
Rename files to strictly enforce the tier hierarchy in filenames for easier sorting/filtering:
- `CANON-30100-ASA-comet.md` -> `CANON-30100-COMET-ASA.md`
- `CANON-31100-ACUMEN-planetary.md` -> `CANON-31100-PLANET-ACUMEN.md`

*This aligns the filesystem sort order with the cosmological descent.*
