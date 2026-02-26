# RESPONSE-ADJUDICATOR-INTEGRATION_REVIEW-CC37
Date: 2026-02-26
Author: Adjudicator (Codex GPT-5)
Phase: CC37 Phase 4 — Integration

## Executive Verdict
**Overall: CONDITIONAL**

The integration is directionally correct and mostly functional, but two issues should be fixed before full production confidence:
1. `source_atom_ids` lineage is collapsed to a single ID in `run_annealer_gate()` input construction.
2. `LOCK_CANON_PROMOTION` is declared in global hierarchy but not acquired by this promotion path.

## Findings (Ordered by Severity)

1. **[P1] Adapter lineage fidelity loss (contract divergence)**  
   In `protease_promote.py`, `adapter_input.atom_id` is set to only `block["source_atom_ids"][0]` and the rest of lineage is dropped before adaptation. `candidate_adapter.py` then emits `source_atom_ids: [atom_id]`, so a multi-atom axiom loses provenance for annealer context/logging. This diverges from `ARCH-CANDIDATE_ADAPTER_CONTRACT.yaml` intent to preserve lineage.  
   Evidence: `protease_promote.py` lines 340-349, `candidate_adapter.py` lines 105-107, contract lines 41-44.

2. **[P1] Lock hierarchy gap for canon promotion transaction**  
   `ARCH-LOCK_HIERARCHY.yaml` defines `LOCK_CANON_PROMOTION` as order 1 for this pipeline, but `protease_promote.py` does not acquire it and `lattice_annealer.py` acquires only `LOCK_LATTICE_INDEX -> LOCK_LATTICE_HEALTH -> LOCK_ANNEAL_LOG`. This leaves cross-process race space for concurrent canon promotions (duplicate check / append / index transition interleaving).  
   Evidence: lock hierarchy lines 7-15; `lattice_annealer.py` line 39; no canon-promotion lock acquisition in `protease_promote.py`.

3. **[P2] Error diagnostics lose annealer stdout on non-zero exits**  
   `run_annealer_gate()` reports `lattice_annealer failed: {stderr}` only. Some annealer errors are printed on stdout; those details are dropped, reducing debuggability.  
   Evidence: `protease_promote.py` lines 374-375; `lattice_annealer.py` lines 1008, 1015 (stdout prints).

## GO / CONDITIONAL / REJECT by Integration Point

| Integration Point | Verdict | Adjudication |
|---|---|---|
| 1) Annealer gate wiring in `protease_promote.py` | **CONDITIONAL** | Mandatory pre-promotion gate is correctly wired for `--target canon` with fail-closed behavior on missing scripts, timeout, invalid JSON, ADJUST/REJECT. Keep. |
| 2) Lock order compliance (adapter no locks; annealer lock sequence) | **CONDITIONAL** | Annealer lock acquisition order is internally correct (`INDEX -> HEALTH -> ANNEAL_LOG`) and compatible with monitor ordering. But canonical transaction lock (`LOCK_CANON_PROMOTION`) is missing from this integration path. |
| 3) Subprocess isolation / orphaned locks | **GO** | Child-process locking model is acceptable. If parent dies, OS-level fd close + PID stale-lock checks provide recovery behavior consistent with architecture notes. |
| 4) Adapter input fidelity vs `ARCH-CANDIDATE_ADAPTER_CONTRACT.yaml` | **REJECT** | Current construction is shape-valid but semantically incomplete for lineage (`source_atom_ids` collapse). This should be corrected before calling the integration complete. |
| 5) Batch atomicity (3 axioms, one blocked) | **GO (with note)** | Promotion writes are atomic at batch level: if any block is gated, atom transitions/SN append do not execute. Note: annealer health/log side effects for earlier items still persist, which is acceptable if interpreted as gate-attempt telemetry. |
| 6) launchd plist (`com.syncrescendence.dag-tension-monitor.plist`) | **CONDITIONAL** | XML is valid (`plutil -lint` OK), command and working directory are correct, env is sufficient for current stdlib-only script. Recommend explicit decision on `RunAtLoad` (true if immediate baseline required) and log rotation plan for stdout/stderr files. Optional: add `LANG=en_US.UTF-8` for consistency across tooling. |

## Specific Answers to Commander Checks

1. **Lock inversion risk from subprocess call**: No direct inversion observed in current call path; risk is missing outer canon lock, not inversion.  
2. **Killed mid-gate orphan locks**: Acceptable; lock handling + PID staleness strategy is coherent.  
3. **`adapter_input` mapping correctness**: Partially correct; schema shape is valid, lineage fidelity is not.  
4. **Batch atomicity behavior**: Correct for promotion side effects (all-or-nothing).  
5. **Plist + env + RunAtLoad + LANG**: Valid plist; env sufficient now; add `LANG` optionally; set `RunAtLoad=true` only if immediate baseline is operationally required.

## Required Remediations Before Unconditional GO

1. Preserve full axiom lineage through adapter path (not only first `source_atom_id`).
2. Add `LOCK_CANON_PROMOTION` around the full canon promotion critical section (duplicate check + gate pass set + transition + SN append), with hierarchy-consistent ordering.
3. Include annealer stdout in failure messages when return code is non-zero.
