# Response

**Response ID**: `RSP-20260310-codex-campaign-07-lane-04-config-surface-rematerialization-contract-and-builder`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-10`
**Dispatch packet**: `PKT-20260310-codex-campaign-07-lane-04-config-surface-rematerialization-contract-and-builder`
**Result state**: `complete`
**Receipt artifacts**:
- `orchestration/state/impl/CONFIG-SURFACE-LEDGER-REMATERIALIZATION-v1.md`
- `operators/validators/rematerialize_config_surface_state.py`
- `orchestration/state/registry/config-surface-state-ledger.jsonl`
- `orchestration/state/registry/live-ledger-domain-register.csv`
- `orchestration/state/registry/live-ledger-domain-register-ledger.jsonl`

## Returned Content

Created the config-surface rematerialization law at `orchestration/state/impl/CONFIG-SURFACE-LEDGER-REMATERIALIZATION-v1.md`.

The v1 rule now binds `config-surface-state-ledger.jsonl` as the append-only substrate and treats the current-state pair:

- `orchestration/state/registry/CONFIG-SURFACE-REGISTRY-v1.json`
- `orchestration/state/registry/CONFIG-SURFACE-PROJECTION-MATRIX-v1.json`

as replaceable derivative records that may be rebuilt from the latest lawful materializable ledger event.

Created the deterministic rebuild operator at `operators/validators/rematerialize_config_surface_state.py`.

The rebuild rule is:

1. read ledger events in order
2. preserve legacy receipt-only events as witness but ignore them for rebuild
3. validate materializable events with embedded `effective_state`
4. choose the latest lawful materializable event by `config_state_version`, then timestamp, then event id
5. write the embedded registry and projection-matrix payloads back out as the current-state pair

Updated supporting surfaces only where needed:

- widened `validate_config_surface_state.py` so it now checks rematerialization parity in addition to structural joins and latest-receipt alignment
- self-registered the rematerializer in the config registry and projection matrix
- appended `csl-20260310-0003` as the first materializable config-surface receipt refresh
- promoted `config_surface_state` to `phase1_repo_proof` in the live-ledger family register via `lldr-20260310-0008`

## Verification

- ran `python3 operators/validators/rematerialize_config_surface_state.py --ledger orchestration/state/registry/config-surface-state-ledger.jsonl --registry-out /tmp/CONFIG-SURFACE-REGISTRY-v1.json --projection-matrix-out /tmp/CONFIG-SURFACE-PROJECTION-MATRIX-v1.json`
- rebuilt from `csl-20260310-0003`
- ran `python3 operators/validators/validate_config_surface_state.py`
- validation report stayed clean and recorded rematerialization parity
- ran `git diff --check`

## Status

`complete`
