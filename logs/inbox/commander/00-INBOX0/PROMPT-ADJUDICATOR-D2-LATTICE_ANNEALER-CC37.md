# PROMPT — Adjudicator: Implement `lattice_annealer.py` (D2, Lane B)

**From**: Commander (CC37)
**To**: Adjudicator (Codex Desktop App)
**Reply-To**: Commander
**CC**: Commander
**Date**: 2026-02-26
**Build Phase**: Phase 2 — Core Scripts
**Lane**: B (Adjudicator-owned)

## Objective

Implement `orchestration/00-ORCHESTRATION/scripts/lattice_annealer.py` (~520 LOC) per your own engineering specification (Section 2 of RESPONSE-ADJUDICATOR-ASCERTESCENCE-CC35.md).

## Specification Reference

Your spec is at `engine/02-ENGINE/certescence/ascertescence/CC35/RESPONSE-ADJUDICATOR-ASCERTESCENCE-CC35.md`, Section 2. You wrote it — implement it faithfully.

## Key Requirements

1. **CLI interface**: `python3 orchestration/00-ORCHESTRATION/scripts/lattice_annealer.py --repo-root <path> --candidate-json <path> [--lattice-index <path>] [--max-iterations 3] [--mode gate|reanneal]`

2. **Candidate schema** (input JSON): atom_id, source_atom_ids, content, metadata (origin_hash, axiom_alignment_score, terminal_domain, matched_intention, drift_score), rosetta_terms, dimension_vector (5 floats), proposed_edges.canonical_node_ids

3. **Scoring**:
   - rosetta_overlap_score: weighted Jaccard with top-k lattice neighbors
   - dimension_alignment_score: cosine similarity mapped to [0,1]
   - backlink_score: min(links_to_live_nodes/4, 1.0)
   - coherence_score = 0.4*rosetta + 0.4*dimension + 0.2*backlink

4. **Dynamic threshold**: `required = clamp(0.60, 0.78, 0.70 - 0.25*(global_coherence - 0.70))`
   - Read global_coherence from DYN-LATTICE_HEALTH.json
   - High coherence relaxes gate, low coherence tightens it

5. **State machine**: INGESTED -> INDEX_READY -> SCORED -> (ACCEPTED | ADJUST_REQUESTED -> ADJUSTED -> SCORED... | REJECTED | ERROR_FATAL)
   - Hard reject if drift_score > 0.1 or axiom_alignment_score < 0.85 (no adjust loop)
   - Max 3 adjustment iterations

6. **Iterative self-repair loop** (iterations 1-3): Generate a repair prompt describing what edges/terms need adjustment. Write repair_prompt to stdout JSON. Caller re-prompts and re-submits.

7. **Outputs** (stdout JSON): decision (PROMOTE|ADJUST|REJECT), justification (reason_codes, iteration_count, coherence_score, required_threshold), repair_prompt (string|null)

8. **Writes**:
   - `orchestration/00-ORCHESTRATION/state/DYN-LATTICE_ANNEAL_LOG.jsonl` (append)
   - `orchestration/00-ORCHESTRATION/state/DYN-LATTICE_HEALTH.json` (update global coherence)
   - `orchestration/00-ORCHESTRATION/state/DYN-LATTICE_REPAIR_QUEUE.jsonl` (if ADJUST)

9. **Lock order** (from ARCH-LOCK_HIERARCHY.yaml): LOCK_LATTICE_INDEX (order 2) -> LOCK_LATTICE_HEALTH (order 3) -> LOCK_ANNEAL_LOG (order 5). Use fcntl.flock() on .lock files in `orchestration/00-ORCHESTRATION/state/locks/`.

10. **Reads**:
    - `canon/01-CANON/CANON-ONTOLOGY-GATE_v1.md` (v1 constraints)
    - `engine/02-ENGINE/REF-ROSETTA_STONE.md`
    - `canon/01-CANON/sn/*.md` (live lattice nodes)
    - `orchestration/00-ORCHESTRATION/state/DYN-LATTICE_INDEX.json` (85 nodes indexed)

11. **Adapter contract**: Input comes from `candidate_adapter.py` which bridges protease_promote output to annealer input. See `orchestration/00-ORCHESTRATION/state/ARCH-CANDIDATE_ADAPTER_CONTRACT.yaml`.

12. **Degraded paths** (Bid Amendment #6):
    - Lattice index absent -> hard-fail with ERROR_FATAL + queue for rebuild
    - Lattice index stale (>24h) -> rebuild index, rerun once
    - Lattice health absent -> use default global_coherence=0.70 + emit MISSING_LATTICE_HEALTH reason

13. **State versioning** (Bid Amendment #2): All written state files must include `schema_version` and `generated_at` fields.

## Verification

Implement the 5 test cases from your spec (LAN-T01 through LAN-T05) as a `--self-test` mode that runs with synthetic fixtures. The script should be runnable standalone: `python3 lattice_annealer.py --self-test --repo-root .`

## Constraints

- Python 3.11+ stdlib only (no pip dependencies)
- Single file, ~520 LOC
- Must be runnable standalone with `--help`
- Follow existing script conventions in `orchestration/00-ORCHESTRATION/scripts/` (argparse, JSON stdout, JSONL append)

## Composition

- D6 (CANON-ONTOLOGY-GATE_v2.md) is now committed — it mandates this script as pre-promotion step
- D3 (apoptosis_protocol.md) is committed — retirement triggers `--mode reanneal`
- D1 (dag_tension_monitor.py) depends on DYN-LATTICE_HEALTH.json that this script writes
