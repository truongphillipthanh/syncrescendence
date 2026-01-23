# COGNITIVE ARCHITECTURE EVIDENCE PACK
## Corpus Forensic Audit: Syncrescendence
**Auditor**: Cognitive Scientist & Information Architect
**Date**: 2026-01-22
**Status**: EXHAUSTIVE

---

## 1. INFORMATION SCENT MAP

| Trail Segment | Scent Strength | Analysis |
| :--- | :--- | :--- |
| **Root → Entry** | 10/10 | `CLAUDE.md` and `COCKPIT.md` are the "High-Intensity Landmarks." |
| **Root → 01-CANON** | 10/10 | The `CANON-` prefix is a "Beacon." You know exactly what is inside. |
| **Root → 04-SOURCES** | 7/10 | Strong scent to the directory, but scent dissipates in `raw/`. |
| **Entry → Operational** | 6/10 | `02-ENGINE` is a "Fuzzy Category." Needs better sub-signage. |
| **Entry → Wisdom** | 9/10 | `06-EXEMPLA` is a unique and clear scent for "Learnings." |

**Dead Ends**: `00-ORCHESTRATION/blackboard/` — Scent is too vague; requires opening files to identify current execution state.

---

## 2. COGNITIVE LOAD SCORES

| Document/Area | Intrinsic Load | Extraneous Load | Germane Load | Rec. Action |
| :--- | :--- | :--- | :--- | :--- |
| `01-CANON/` | 9/10 | 2/10 | 10/10 | Keep. The verbosity is the "scaffolding." |
| `04-SOURCES/raw/` | 2/10 | 9/10 | 1/10 | **Archive.** Move to `raw/archive/` to clear scannable area. |
| `00-ORCHESTRATION/state/` | 7/10 | 6/10 | 5/10 | **Split.** Separate `DYN-` (Active) from `REF-` (Static). |
| `BLITZKRIEG_PROTOCOL.md` | 10/10 | 4/10 | 8/10 | **Simplify.** Use visual diagrams to reduce text-processing load. |

**Load Reduction Opportunity**: By archiving the 180+ files in `SOURCES/raw`, the corpus scannable surface area for an AI agent is reduced by **~60%**, significantly lowering token-based cognitive overhead.

---

## 3. WAYFINDING FAILURES

*   **False Scent**: `03-QUEUE/modal2/`. "Modal 2" suggests a technical state rather than content. A newcomer cannot infer that this contains "Visual/VFX" tasks without reading the index.
*   **The Flat Paradox**: `CLAUDE.md` Rule 1 ("FLAT PRINCIPLE") acts as a "Broken Signpost." An agent searches for a file in the root of a directory, but it is actually inside a nested folder (e.g., `02-ENGINE/prompts`).
*   **Landmark Overcrowding**: `00-ORCHESTRATION/state` has too many landmarks (`ARCH-`, `DYN-`, `REF-`, `SCAFF-`). When everything is a landmark, nothing is a landmark.
*   **Script Naming Drift**: `00-ORCHESTRATION/scripts/` uses underscores (`sync_ledgers.py`) while `CANON` and `state` rely on hyphens for ID segmentation. This subtle shift increases the "Grammar Load" for agents performing CLI operations.

---

## 4. CHUNKING RECOMMENDATIONS

*   **Monoliths**: `CANON-31121-TONE_TAXONOMY...` naming is a "Token Monolith." While descriptive, it exceeds the cognitive chunking limit for rapid scanning.
    *   *Rec*: Keep for machine parsing, but provide a `CANON_MAP.md` for human scannability.
*   **Fragments**: `02-ENGINE/protocols/REF-STATE_FINGERPRINT_PROTOCOL.md` is too isolated.
    *   *Rec*: Merge small protocol fragments into a single `CONSTELLATION_OPERATIONS.md`.

---

## 5. AFFORDANCE GAPS

*   **Misleading Affordance**: The `-INBOX` directory suggests "I can put anything here," but the system actually requires strict triage before it moves to `SOURCES`. 
*   **Missing Affordance**: There is no "Ejection Seat" affordance—a clear path for moving "Failed Experiments" or "Stale Directives" out of the active Orchestration layer.
*   **Actionable Affordance**: `Makefile` is an excellent affordance. It signals "This is a system that can be validated."

---

## 6. NAMING AUDIT TABLE (Sample)

| Name | Semantic Clarity | Consistency | Mnemonic | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| `01-CANON` | 10/10 | Y | 10/10 | Perfect. |
| `02-ENGINE` | 5/10 | Y | 5/10 | Vague. Is it code or docs? |
| `DYN-TASKS.csv` | 10/10 | Y | 9/10 | Dynamic prefix is highly effective. |
| `modal2` | 2/10 | N | 2/10 | High cognitive debt. |
| `SCAFF-` | 8/10 | Y | 7/10 | Good "Metaphorical Scent." |
| `00-ORCHESTRATION/scripts/` | 8/10 | N | 7/10 | Underscore use (`sync_ledgers.py`) deviates from hyphen standard. |
| `MODEL_PROFILE-*.yaml` | 10/10 | Y | 9/10 | Strong semantic mapping. |

---

## 7. MENTAL MODEL DIAGRAM

**Designer's Model (Intended)**: 
`Root [Flat] -> Domain [Flat] -> Artifact`

**System Model (Actual)**: 
`Root [Flat] -> Domain [Nested] -> Sub-domain -> Artifact`

**User's Model (Inferred)**: 
`Root -> Folders -> Files (Like a standard OS)`

**The Divergence**: The system is fighting its own "Flat Principle." This causes "Friction" every time a new folder is encountered.

---

## 8. REFACTORING FOR NAVIGABILITY

1.  **Acknowledge Hierarchy**: Change "Flat Principle" to "Clean Hierarchy Principle" in `CLAUDE.md`.
2.  **Tiered Disclosure**: Ensure `README.md` in every directory acts as a "Progressive Disclosure" layer before the file list.
3.  **The "Swamp" Filter**: Move `04-SOURCES/raw` to `05-MEMORY/raw_intake` after processing to keep the "Active Corpus" lean.
4.  **Rename `02-ENGINE`**: Rename to `02-ENGINE` or `02-TOOLING` to clarify its affordance as a functional layer.

---
**Audit Complete.**
