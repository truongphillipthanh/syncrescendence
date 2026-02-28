---
id: CANON-ONTOLOGY-GATE-V1
canonical_name: Ontology Gate v1
title: "Runtime Contract — Layer 1 Enforcement"

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
# CANON-ONTOLOGY-GATE_v1.md
## Runtime Contract — Layer 1 Enforcement (σ₂ Ontology of Self)
**Authority**: ARCH-ONTOLOGY_ANNEALMENT_v1.md (9-step protocol) + REF-ROSETTA_STONE.md v2.7.0
**Enforced by**: pre-commit hook + protease_check.sh

### Schema Fields (mandatory header on every atom)
- origin_hash: SHA-256 of source atom
- axiom_alignment_score: float [0.0-1.0] computed via Rosetta category match
- terminal_domain: 3-char code (STR/CON/PROTO/... from ontology.db)
- matched_intention: INT-XXXX from ARCH-INTENTION_COMPASS.md
- drift_score: <0.1 required

### Validation Rules
1. ∀ atom: exists Rosetta term with Similarity(atom, term) > 0.85
2. Intention must be active (not DEFERRED or PARKED in DYN-DEFERRED_COMMITMENTS)
3. No promotion if any field undefined or score fails

### Failure Classes & Action
- Drift (>0.1): REJECT + log to rejection_ledger.md
- Noise (missing metadata): LYSATE (delete from queue)
- Mimicry (violates core axioms): QUARANTINE to sources/icebox/

### Falsifiable Test (Antigen Challenge)
Inject test atom "Use Agile Scrum". Expected: immediate REJECT.
Pass = gate blocks; Fail = integration_gate.py aborts batch.

**Termination Artifact**: This file itself. Every future OL-5 batch must reference it.
