# Cognitive Core v1

Purpose: a minimal interface contract + evaluation governors + retention doctrine that all future work must route through.

This nucleus is intentionally small. It governs how decisions are formed, justified, and retained. Details live elsewhere; this file only points.

## Scope of the nucleus
- `00-ORCHESTRATION/cognitive_core.md` (this file)
- `00-ORCHESTRATION/decision_atoms.md`
- `00-ORCHESTRATION/lens_governance.md`
- `00-ORCHESTRATION/model_orchestration.md`

## Memory doctrine

### Tiers
- **Core**: irreducible invariants that must survive system evolution. This nucleus + constitution (see `CLAUDE.md`).
- **Evidence**: facts, observations, or analyses that justify decisions. Stored as outgoing packs and source references.
- **Pointers**: links to canonical or operational detail (e.g., `00-ORCHESTRATION/state/REF-STANDARDS.md`, `01-CANON/CANON-00015-MACROSCOPIC_NARRATIVES-cosmos.md`).

### Retention rules
- **Forgetting is default**: if it does not directly govern future decisions, it becomes a pointer or is dropped.
- **Evidence is time-bounded**: keep only the smallest evidence set that preserves falsifiability and traceability.
- **Core never duplicates**: this nucleus must not restate canonical detail. It only points to it.

### Token rent policy
Every token must pay rent by doing one of:
- **Governing** (decision rules, boundaries, required fields)
- **Falsifying** (conditions that would overturn a choice)
- **Routing** (where to look next, with explicit pointers)

Anything else is eviction-eligible. Duplication incurs a tax: if content exists elsewhere, replace with a pointer.

## Evaluation governors
- **18 evaluative lenses are mandatory** for strategic decisions (see `00-ORCHESTRATION/state/REF-STANDARDS.md`).
- **Narrative lenses (19-30)** apply when a decision affects civilizational framing or long-horizon direction (see `00-ORCHESTRATION/lens_governance.md` and `01-CANON/CANON-00015-MACROSCOPIC_NARRATIVES-cosmos.md`).
- Any decision must be captured as a decision atom (see `00-ORCHESTRATION/decision_atoms.md`).

## Decision routing
All new policies, structures, or integrations must:
1. Produce a decision atom with falsifier + reversibility.
2. Pass lens governance thresholds.
3. Link to evidence (outgoing pack or canonical source).

If any of the above is missing, the change is not accepted as core.
