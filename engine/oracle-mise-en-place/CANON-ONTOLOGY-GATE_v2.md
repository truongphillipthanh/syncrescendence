---
id: CANON-ONTOLOGY-GATE-V2
canonical_name: Ontology Gate v2
title: "Runtime Contract — Layer 2 Enforcement"

tier: immune
chain: null
celestial_type: policy
volatility_band: moderate
refresh_cadence: quarterly

parent: null
requires: []
siblings: []
synthesizes: []

status: canonical
operational_status: operational
version: 1.0.0
created: 2026-02-27
updated: 2026-02-27
last_verified: 

element: null
ooda_phase: null
volatile_sections: []
---
# CANON-ONTOLOGY-GATE_v2.md
## Runtime Contract — Layer 1 Enforcement Extension (σ₂ Ontology of Self)

**Authority**: CANON-ONTOLOGY-GATE_v1.md (preserved in full) + Adjudicator Specification §6
**Extends**: CANON-ONTOLOGY-GATE_v1.md — all v1 rules remain in force without modification
**Effective**: 2026-02-26
**Enforced by**: pre-commit hook (extended), `protease_promote.py`, `lattice_annealer.py`

---

## Preamble

This document is a constitutional extension of `CANON-ONTOLOGY-GATE_v1.md`. Every rule, field, threshold, and failure class defined in v1 remains binding. v2 adds three capabilities:

1. **Mandatory lattice annealing** — no promotion without `lattice_annealer.py` decision.
2. **Dynamic coherence threshold** — gate threshold adjusts proportionally to measured Lattice coherence.
3. **Iterative self-repair** — atoms that pass v1 validation but fail annealing receive up to 3 adjustment attempts before rejection.

v1 hard-failures (drift >0.1, missing metadata, axiom violation) are never subject to self-repair. They proceed directly to REJECT as defined in v1.

---

## Schema Fields

### v1 Fields (unchanged, mandatory)

| Field | Type | Constraint |
|-------|------|------------|
| `origin_hash` | SHA-256 | Source atom hash |
| `axiom_alignment_score` | float | [0.0, 1.0] via Rosetta category match |
| `terminal_domain` | string | 3-char code from `ontology.db` |
| `matched_intention` | string | INT-XXXX from ARCH-INTENTION_COMPASS.md |
| `drift_score` | float | < 0.10 required |

### v2 Fields (mandatory on all atoms processed after effective date)

| Field | Type | Constraint |
|-------|------|------------|
| `gate_version` | string | `"v2"` |
| `lattice_coherence_score` | float | [0.0, 1.0] — global coherence at time of evaluation |
| `lattice_threshold_required` | float | [0.0, 1.0] — computed dynamic threshold |
| `annealer_decision` | enum | `PROMOTE` \| `ADJUST` \| `REJECT` |
| `anneal_iteration_count` | integer | [0, 3] |
| `self_repair_attempted` | boolean | `true` if any ADJUST iteration occurred |

---

## State Machine

```
INGEST
  │
  ▼
V1_VALIDATE ──── v1 hard-fail ──► REJECT_LYSATE (missing metadata / noise)
  │                            └─► REJECT_QUARANTINE (axiom violation / mimicry)
  │
  │ v1 pass
  ▼
ANNEAL_PRECHECK
  │
  ├── annealer unavailable ──► FATAL (GAT-F002), batch aborts
  │
  ├── annealer returns PROMOTE ──► PASS_PROMOTION
  │
  ├── annealer returns ADJUST ──► ADJUST_LOOP (iteration 1)
  │     │
  │     ├── annealer returns PROMOTE ──► PASS_PROMOTION
  │     ├── annealer returns ADJUST ──► ADJUST_LOOP (iteration 2)
  │     │     │
  │     │     ├── annealer returns PROMOTE ──► PASS_PROMOTION
  │     │     ├── annealer returns ADJUST ──► ADJUST_LOOP (iteration 3)
  │     │     │     │
  │     │     │     ├── annealer returns PROMOTE ──► PASS_PROMOTION
  │     │     │     └── annealer returns ADJUST or REJECT ──► REJECT_QUARANTINE
  │     │     │
  │     │     └── annealer returns REJECT ──► REJECT_QUARANTINE
  │     │
  │     └── annealer returns REJECT ──► REJECT_QUARANTINE
  │
  └── annealer returns REJECT ──► REJECT_QUARANTINE
```

**Invariant**: No path from INGEST to PASS_PROMOTION bypasses both V1_VALIDATE and ANNEAL_PRECHECK.

---

## Validation Rules

### v1 Rules (preserved verbatim)

1. `∀ atom: exists Rosetta term with Similarity(atom, term) > 0.85`
2. Intention must be active (not DEFERRED or PARKED in DYN-DEFERRED_COMMITMENTS)
3. No promotion if any field undefined or score fails

### v2 Rules (additive)

4. **Mandatory annealer**: `lattice_annealer.py` must execute and return a decision before any promotion. Promotion without annealer output is a fatal error (GAT-F002).

5. **Dynamic coherence threshold**: The gate threshold for `axiom_alignment_score` relaxes proportionally to measured Lattice coherence.

   ```
   required = clamp(0.60, 0.78, 0.70 + 0.25 * (global_coherence - 0.70))
   ```

   Where:
   - `global_coherence` is read from `DYN-LATTICE_HEALTH.json`
   - `clamp(min, max, value)` = `max(min, min(max, value))`
   - Floor: 0.60 (threshold never drops below this)
   - Ceiling: 0.78 (threshold never exceeds this)

6. **Iterative self-repair**: Atoms that pass v1 validation but receive an ADJUST decision from the annealer enter the adjustment loop. Maximum 3 iterations. After 3 failed adjustments, the atom is quarantined.

7. **ADJUST before REJECT**: If an atom passes v1 validation, the annealer MUST attempt ADJUST before issuing REJECT, unless the atom's coherence score is below the dynamic threshold by more than 0.20 (catastrophic incoherence).

---

## Failure Modes

| ID | Condition | Severity | Action |
|----|-----------|----------|--------|
| GAT-F001 | v1 rule bypassed in v2 pipeline | FATAL | Abort batch. Alert Sovereign. No atoms from batch promoted. |
| GAT-F002 | Annealer unavailable but promotion attempted | FATAL | Abort batch. No promotion without annealer decision. |
| GAT-F003 | Dynamic threshold causes starvation: reject rate >35% while global coherence >0.70 | DEGRADED | Log warning to `DYN-ONTOLOGY_GATE_V2_LOG.jsonl`. Investigate threshold calibration. |
| GAT-F004 | Dynamic threshold over-relaxation: reject rate <1% with rising contradiction count | DEGRADED | Log warning. Consider tightening floor parameter. |
| GAT-F005 | Legacy audit index incomplete (pre-v2 atoms not yet indexed) | COSMETIC | Background task. Does not block operations. |

---

## Backward Compatibility

1. **Atoms promoted before v2 effective date remain valid** unless explicitly re-opened by Sovereign decision.
2. Legacy items are marked `legacy_v1_pass=true` in the audit index.
3. v1 validation rules are not weakened, relaxed, or made optional by v2. They remain the first gate in the pipeline.
4. Systems that read atom headers must tolerate the absence of v2 fields on pre-v2 atoms.

---

## Verification Contract

| Test ID | Description | Expected Outcome |
|---------|-------------|-----------------|
| GAT-T01 | v1 hard-fail remains REJECT | Atom with `drift_score=0.15` is REJECT. No ADJUST loop entered. |
| GAT-T02 | ADJUST before REJECT on v1-passing atom | Atom passes v1 but has low coherence. Annealer issues ADJUST up to 3 times before REJECT_QUARANTINE. |
| GAT-T03 | Mandatory annealer enforcement | Promotion attempted without annealer output. Pipeline aborts with GAT-F002. |
| GAT-T04 | Backward compatibility | Pre-v2 atom with no v2 fields remains valid in canon. No retroactive rejection. |
| GAT-T05 | Dynamic threshold bounds | With `global_coherence=0.90`, threshold relaxes but stays >= 0.60. With `global_coherence=0.50`, threshold tightens but stays <= 0.78. |

### Antigen Challenge (extended from v1)

Inject test atom "Use Agile Scrum":
- v1 gate: immediate REJECT (axiom violation / mimicry).
- v2 pipeline: no ADJUST loop entered (v1 hard-fail).
- Pass = gate blocks at V1_VALIDATE. Fail = `integration_gate.py` aborts batch.

---

## Integration Points

### Reads
- `CANON-ONTOLOGY-GATE_v1.md` — authoritative v1 contract
- `DYN-LATTICE_ANNEAL_LOG.jsonl` — annealer decision history
- `DYN-LATTICE_HEALTH.json` — global coherence score for dynamic threshold

### Writes
- `DYN-ONTOLOGY_GATE_V2_LOG.jsonl` — all v2 gate decisions, thresholds, iteration counts
- `DYN-ONTOLOGY_REJECTION_LEDGER.jsonl` — rejected atoms with failure class and mode

### Composition
```
v1_validate -> anneal -> promote -> apoptosis accounting
```

### Enforcement
- **pre-commit hook**: Extended from v1 to include annealer availability check.
- **protease_promote.py**: Reads annealer decision before executing promotion.
- **lattice_annealer.py**: New mandatory dependency. Must be callable before any promotion batch.

---

## Termination Artifact

This file, together with `CANON-ONTOLOGY-GATE_v1.md`, constitutes the complete ontology gate contract. Every future OL-5 batch must reference both v1 and v2. Neither document supersedes the other; v2 extends v1.
