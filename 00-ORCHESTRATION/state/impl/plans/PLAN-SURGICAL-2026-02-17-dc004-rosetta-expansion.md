# SURGICAL PLAN — DC-004: Rosetta Stone Ontological Term Expansion
## Issued: 2026-02-17 | Fingerprint: 3cc50bd

---

### Issue

DC-004 (P0, OPEN, target 2026-02-18): ~25 ontological terms were intellectually resolved across
multiple clarescences (sessions 10-11, the metacharacterization exercise) but never formally
committed to `02-ENGINE/REF-ROSETTA_STONE.md`. The annealment v2 verification (ANNEAL-V2-PATCHES.md)
explicitly flagged this as a scope-boundary item deferred to this commitment.

Current state: REF-ROSETTA_STONE.md v2.7.0 — 1,012 lines, 311 entries, 24 categories (17 internal
scaffold + 7 convergence). The ~25 missing terms are from the ontology metacharacterization work:
Palantir-inspired primitives, sovereign stack architecture concepts, and personal ontology kernel types.

### Root Cause Hypothesis

The convergence synthesis agent (ARCH-ONTOLOGY_ANNEALMENT_v2.md) discovered ~25 terms during
synthesis that resolved ontological concepts but were excluded from the Rosetta Stone because the
scope boundary was "annealment document only." No follow-up task was dispatched at the time.

### Minimal Change Set

- [ ] **Agent task**: Read CLARESCE-MASTER-DIGEST.md + ANNEAL-V2-PATCHES.md + ARCH-ONTOLOGY_ANNEALMENT_v2.md
      → identify all ontological terms that are defined/resolved but absent from REF-ROSETTA_STONE.md
      → produce a candidate list with proposed category assignments
- [ ] **Commander review**: Approve candidate list, assign to existing or new categories
- [ ] **File update**: Append approved terms to REF-ROSETTA_STONE.md, bump version to v2.8.0
- [ ] **Commit**: `feat(rosetta): v2.8.0 — ~25 ontological terms from metacharacterization + annealment`
- [ ] **DC-004 closure**: Update DYN-DEFERRED_COMMITMENTS.md status to DONE

### Assigned To

Commander (Sonnet subagent) — single-file update, well-defined source material, no cross-agent
coordination required. Content is in the digests we just completed.

### Source Material

| File | Path | Purpose |
|------|------|---------|
| Master digest | `impl/clarescence/.scratch/CLARESCE-MASTER-DIGEST.md` | Compressed ontological decisions |
| Annealment v2 | `00-ORCHESTRATION/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md` | Primary source (787 lines) — delegate |
| Patch file | `impl/.scratch/ANNEAL-V2-PATCHES.md` | Tier 3 object types (PATCH-001), references to ~25 terms |
| Rosetta Stone | `02-ENGINE/REF-ROSETTA_STONE.md` | Target file (v2.7.0, 1,012 lines) — delegate reads |
| F digest | `impl/clarescence/.scratch/CLARESCE-DIGEST-F.md` | DA-01..07, Palantir primitives |
| J digest | `impl/clarescence/.scratch/CLARESCE-DIGEST-J.md` | DEC-01..13, convergence terms |

### Candidate Term Sources (Known)

From ANNEAL-V2-PATCHES.md (PATCH-001 — Tier 3 object types):
- Memory (as ontological object)
- Policy/Rule (governance kernel)
- Health State (biological state as first-class object)
- Environment/Context (situational hydration surface)

From Digest-F (4-Layer Ontology Kernel, DA-01..07):
- CMT (Commitment object type)
- GOAL (Goal object type)
- RISK (Risk object type)
- REL (Relationship object type)
- RES (Resource object type)
- ENV (Environment object type)
- Governed Verb (first-class primitive)

From Digest-F (Palantir tripartite):
- Semantic Layer (ontological term)
- Kinetic Layer (operational execution)
- Dynamic Layer / Physics Layer (simulation/prediction)
- Schema Capture (threat surface — PATCH-002)
- Coherence (as scarce resource — PATCH-003)
- Event Sourcing (versioned history mechanism)
- Directionality Test (skeleton vs organ evaluation)
- Semantic Authority
- Headless Architecture
- Impedance Mismatch
- Database Administrator of the Self

From Digest-J / Convergence injection:
- Maximal Consensus Insight (Sovereign curation principle)
- Tool-Shaped Object (trap category — from research)
- Judgment Engineering (core value proposition)
- Context Window as Bottleneck (architectural constraint naming)

Estimated total: ~25-30 terms. Some may already exist in v2.7.0 — agent must diff against existing.

### Success Criteria

- [ ] All ~25 terms identified and diffed against existing 311 entries
- [ ] No duplicates introduced (exact term match check)
- [ ] Terms assigned to appropriate existing categories OR new category proposed
- [ ] REF-ROSETTA_STONE.md bumped to v2.8.0 with updated entry count
- [ ] Commit created with semantic prefix `feat(rosetta):`
- [ ] DC-004 status updated to DONE in DYN-DEFERRED_COMMITMENTS.md

### Risk

- **Blast radius**: Single file (REF-ROSETTA_STONE.md) + one state file (DYN-DEFERRED_COMMITMENTS.md)
- **Rollback**: `git revert` — trivially reversible
- **False duplicate risk**: Low — categories 18-24 added 2026-02-16; terms from metacharacterization
  are distinct domain (ontology kernel types vs convergence vision vocabulary)
- **Scope creep risk**: Agent may want to add more than ~25 terms. Hard cap: 35 additions maximum.
  If more are found, flag as DC-016 for next session.

---

*PLAN-SURGICAL-2026-02-17-dc004-rosetta-expansion.md | Commander | 2026-02-17*
