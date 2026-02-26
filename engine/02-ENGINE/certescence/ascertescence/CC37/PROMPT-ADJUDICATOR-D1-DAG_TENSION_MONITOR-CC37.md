# PROMPT — Adjudicator: Implement `dag_tension_monitor.py` (D1, Lane C)

**From**: Commander (CC37)
**To**: Adjudicator (Codex Desktop App)
**Reply-To**: Commander
**CC**: Commander
**Date**: 2026-02-26
**Build Phase**: Phase 2 — Core Scripts
**Lane**: C (Adjudicator-owned)

## Objective

Implement `orchestration/00-ORCHESTRATION/scripts/dag_tension_monitor.py` (~240 LOC) per your own engineering specification (Section 1 of RESPONSE-ADJUDICATOR-ASCERTESCENCE-CC35.md).

## Specification Reference

Your spec is at `engine/02-ENGINE/certescence/ascertescence/CC35/RESPONSE-ADJUDICATOR-ASCERTESCENCE-CC35.md`, Section 1. You wrote it — implement it faithfully.

## Key Requirements

1. **CLI interface**: `python3 orchestration/00-ORCHESTRATION/scripts/dag_tension_monitor.py --repo-root <path> [--dag-state <path>] [--dag-fallback-md <path>] [--lattice-health <path>] [--threshold-config <path>] [--ambient-op-log <path>] [--mode monitor|audit-only] [--now <iso8601>]`

2. **Inputs**:
   - `engine/02-ENGINE/certescence/DYN-DAG_STATE.json` (primary — 13 nodes, tiers, statuses)
   - `engine/02-ENGINE/certescence/PROTOCOL-ASCERTESCENCE.md` (fallback parse)
   - `orchestration/00-ORCHESTRATION/state/DYN-LATTICE_HEALTH.json`
   - `orchestration/00-ORCHESTRATION/state/DYN-ASCERTESCENCE_THRESHOLDS.yaml`
   - `orchestration/00-ORCHESTRATION/state/DYN-COWORK_AMBIENT_OPS.jsonl`

3. **Tension formula**: `T = NodeCount * AgeDaysP75 * UnresolvedStatus * LatticeInterferenceScore`
   - NodeCount: count of unresolved nodes (OPEN, PARTIAL, BLOCKED)
   - AgeDaysP75: 75th percentile of days since last_state_change for unresolved nodes (min 1)
   - UnresolvedStatus: weighted sum using status_weights (OPEN=1.0, PARTIAL=0.6, BLOCKED=1.2)
   - LatticeInterferenceScore: `clamp(0.5, 2.0, 1.0 + fragmentation_index + max(0, global_drift - 0.05))`

4. **Signal decision**:
   - FIRE if T >= threshold AND cooldown satisfied
   - HOLD otherwise
   - Add reason_codes explaining the decision

5. **Conservation of Epistemic Energy** (critical):
   - Read DYN-COWORK_AMBIENT_OPS.jsonl
   - Check: `net_new_nodes = open_nodes_after - open_nodes_before`
   - If `net_new_nodes > 0` from ambient ops: REJECT operation, emit HOLD regardless, append reason ENERGY_VIOLATION
   - Write audit to DYN-EPISTEMIC_ENERGY_AUDIT.jsonl

6. **State machine**: INIT -> LOAD_INPUTS -> COMPUTE_TENSION -> AUDIT_AMBIENT -> DECIDE_SIGNAL -> (FIRE_EMITTED | HOLD_EMITTED | AMBIENT_REJECTED | ERROR_FATAL)

7. **Outputs** (stdout JSON): signal (FIRE|HOLD), tension (float), threshold (float), node_count_unresolved (int), reason_codes (array), energy_audit_status (PASS|REJECT)

8. **Writes**:
   - `orchestration/00-ORCHESTRATION/state/DYN-DAG_TENSION_HISTORY.jsonl` (append)
   - `orchestration/00-ORCHESTRATION/state/DYN-EPISTEMIC_ENERGY_AUDIT.jsonl` (append)
   - `orchestration/00-ORCHESTRATION/state/DYN-DAG_SIGNAL.json` (overwrite — latest signal)

9. **Lock order** (from ARCH-LOCK_HIERARCHY.yaml): LOCK_DAG_STATE (order 4). Also reads LOCK_LATTICE_HEALTH (order 3) — acquire in order. Use fcntl.flock() on .lock files in `orchestration/00-ORCHESTRATION/state/locks/`.

10. **Degraded paths** (Bid Amendments):
    - DAG source unavailable (no JSON + no MD fallback): ERROR_FATAL, abort
    - Lattice health stale (>24h): run with last-known values + add STALE_LATTICE_HEALTH reason
    - Lattice health absent: use defaults (global_coherence=0.70, global_drift=0.0, fragmentation_index=0.0) + add MISSING_LATTICE_HEALTH reason
    - Threshold config invalid: fallback to safe defaults (fire_threshold_base=30.0, cooldown_hours=12)
    - Concurrent monitor race: enforce file lock, second instance exits HOLD

11. **Cooldown**: After a FIRE, no re-FIRE within cooldown_hours (from threshold config). Check DYN-DAG_TENSION_HISTORY.jsonl for last FIRE timestamp.

12. **State versioning** (Bid Amendment #2): All written state files must include `schema_version` and `generated_at`.

## Verification

Implement the 5 test cases from your spec (DTM-T01 through DTM-T05) as a `--self-test` mode with synthetic fixtures. Runnable standalone: `python3 dag_tension_monitor.py --self-test --repo-root .`

## Constraints

- Python 3.11+ stdlib only (no pip dependencies)
- Single file, ~240 LOC
- Must be runnable standalone with `--help`
- YAML parsing: use a simple key-value parser or expect pre-converted JSON (stdlib has no YAML parser). Alternatively, read threshold config as JSON fallback.
- Follow existing script conventions in `orchestration/00-ORCHESTRATION/scripts/`

## Composition

- Reads DYN-LATTICE_HEALTH.json written by D2 (lattice_annealer.py) — if D2 hasn't run yet, use defaults
- Signal output (DYN-DAG_SIGNAL.json) is read by pre-triangulation gate to decide if ascertescence cycle should fire
- Scheduled via launchd/cron every 6h (not Cowork — concrete scheduler per Bid Amendment #4)
