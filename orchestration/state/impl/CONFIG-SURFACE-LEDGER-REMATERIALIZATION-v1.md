# Config-Surface Ledger Rematerialization v1

**Status**: live-v1
**Class**: implementation law
**Purpose**: define the minimal config-surface ledger event needed for proof-grade rebuilds and the deterministic rule that rematerializes the current-state pair from append-only history

## Compact Rule

- config-surface mutation history lives in `orchestration/state/registry/config-surface-state-ledger.jsonl`
- `orchestration/state/registry/CONFIG-SURFACE-REGISTRY-v1.json` is a replaceable current-state record
- `orchestration/state/registry/CONFIG-SURFACE-PROJECTION-MATRIX-v1.json` is a replaceable current-state record
- Sigma doctrine remains higher precedence than both the ledger and the rematerialized current-state pair

The current-state pair may be deleted and rebuilt at any time from the ledger.
Neither file may become a hidden sovereign layer.

## 1. Minimal Event Shape

Every config-surface ledger line remains one JSON object.
Receipt-only seed events may still exist, but proof-grade rematerialization requires a materializable event with the following minimum fields:

- `schema_version`
- `event_id`
- `event_type`
- `recorded_at`
- `actor`
- `family_id`
- `config_state_version`
- `registry_path`
- `projection_matrix_path`
- `registry_sha256`
- `projection_matrix_sha256`
- `joint_sha256`
- `effective_state`

Allowed `event_type` values in v1 remain:

- `seed_receipt`
- `receipt_refresh`
- `drift_receipt`
- `supersession_receipt`

Field law:

- `family_id` is always `config_surface_state`
- `config_state_version` is monotonically increasing across materializable events
- `effective_state.registry` is the full post-event registry payload
- `effective_state.projection_matrix` is the full post-event matrix payload
- the event digests must match the canonical bytes of those embedded payloads
- legacy receipt-only events may omit `schema_version`, `config_state_version`, and `effective_state`, but they do not by themselves justify `phase1_repo_proof`

## 2. Rematerialization Rule

`CONFIG-SURFACE-REGISTRY-v1.json` and `CONFIG-SURFACE-PROJECTION-MATRIX-v1.json` are rebuilt with this deterministic rule:

1. read every non-empty JSONL line in ledger order
2. validate the common receipt envelope on every event
3. ignore receipt-only legacy events for rebuild purposes while preserving them as append-only witness
4. reject any materializable event that fails the v1 field contract
5. choose the latest lawful materializable event by `config_state_version`, then `recorded_at`, then `event_id`
6. write that event's `effective_state.registry` to `CONFIG-SURFACE-REGISTRY-v1.json`
7. write that event's `effective_state.projection_matrix` to `CONFIG-SURFACE-PROJECTION-MATRIX-v1.json`

No out-of-band renderer state may be required to rebuild the current-state pair.
If the pair cannot be rebuilt from the ledger alone, the family falls back below proof-grade status until repaired.

## 3. Subordination And Replaceability

The precedence chain is:

1. `knowledge/sigma/CONFIG-SOURCE-OF-TRUTH-ARCHITECTURE-v1.md`
2. `knowledge/sigma/CONFIG-BEHAVIOR-ATOMS-AND-SURFACE-PROFILES-v1.md`
3. `orchestration/state/impl/CONFIG-SURFACE-LEDGER-REMATERIALIZATION-v1.md`
4. `orchestration/state/registry/config-surface-state-ledger.jsonl`
5. `CONFIG-SURFACE-REGISTRY-v1.json`
6. `CONFIG-SURFACE-PROJECTION-MATRIX-v1.json`

Consequences:

- the ledger is append-only witness and rebuild substrate, not a license to outrank Sigma doctrine
- the current-state pair is disposable and may be regenerated after deletion
- repairs happen by new ledger events, not by rewriting historical lines

## 4. Operator

The repo-native rematerializer for v1 is:

- `operators/validators/rematerialize_config_surface_state.py`

It writes only the current-state pair.
It does not invent new atom families, new surface classes, or new sovereign doctrine.
