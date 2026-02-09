---
name: claresce
description: Run a clarescence cycle — value-guided progressive refinement
---

# /claresce — Clarescence Skill

You are invoking the **clarescence** meta-operation: value-guided progressive refinement (Rosetta #169).

## When invoked

The user wants to claresce a decision, path, or configuration. This means running a structured multi-pass analysis to converge on the best path forward.

## Procedure

### 1. Gather inputs
Ask (or infer from context):
- **Topic**: What decision/path is being claresced?
- **Current state**: Read relevant files, check `git status`, identify drift/conflicts
- **Options**: What are the available paths? (if not obvious)
- **Constraints**: Time, energy, cost, policies

### 2. Determine fidelity
- **Partial clarescence (passes 1-3)**: Local tactical decisions, low blast radius
- **Full clarescence (passes 1-10)**: Substrate-affecting decisions, irreversible coupling

### 3. Run the passes

**Pass 1: Triumvirate Calibration**
- Destination / why now
- Current state / what's broken
- Fit-to-destination verdict

**Pass 2: 18+ Lenses**
- Quick scorecard: which lenses pass/fail (aim >=12/18)

**Pass 3: CANON Coherence**
- What canonical docs say
- Where reality diverges

*For full clarescence, continue:*

**Pass 4: Omni-Qualities** — Omniscience/Omnipresence/Omnipotence/Omnibenevolence impact

**Pass 5: Five Faces** — Sensing / Meaning / Intention / Embodiment / Harmony alignment

**Pass 6: Rosetta Precision** — Term alignment; propose updates if terms drift

**Pass 7: Backlog Coherence** — What it unblocks; what it creates; priority

**Pass 8: nth-order effects** — What breaks; what compounds; new dependencies

**Pass 9: Energy state** — Sustainable to implement now? If not, stage it.

**Pass 10: Authenticity gate** — Preserves sovereignty + optionality? Sovereign-at-peak-clarity approved?

### 4. Produce output

Write the clarescence record to `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-YYYY-MM-DD-<slug>.md` with:

```
CLARESCENCE: <topic>
Fidelity: partial|full
Passes run: 1-3 | 1-10
Convergent Path: <single best path>
Rationale (digest): <3-7 bullets>
Dependencies created/updated: <ids>
Falsifier: <what would make this wrong>
Confidence: low|medium|high
```

If a binding decision is made, produce a **DecisionAtom** with:
- Decision statement
- Canonical truth surface
- Reversibility + rollback path
- Falsifier

### 5. Update backlog
- Add/adjust tasks in `IMPLEMENTATION-MAP.md`
- Append to `DYN-GLOBAL_LEDGER.md` with event `DECISION`

## Reference
Full runbook: `02-ENGINE/REF-CLARESCENCE_RUNBOOK.md`
