# Office-Harness Ledger Rematerialization v1

**Status**: live-v1
**Class**: implementation law
**Purpose**: define the minimal office-harness rebinding event and the deterministic rule that rematerializes the effective registry from append-only ledger history

## Compact Rule

- office-harness rebinding history lives in `orchestration/state/registry/office-harness-binding-ledger.jsonl`
- `orchestration/state/registry/office-harness-bindings.effective.json` is a disposable read model
- per-office metadata remains higher precedence than both ledger and effective registry

The effective registry may be deleted and rebuilt at any time from the ledger.
It must never become a hand-authored constitutional surface.

## 1. Minimal Rebinding Event Shape

Each ledger line is one JSON object with the following minimum fields:

- `schema_version`
- `event_id`
- `event_type`
- `occurred_at`
- `actor`
- `office_id`
- `office_binding_version`
- `metadata_path`
- `binding_state_before`
- `binding_state_after`
- `ratification_pointer`
- `ratified_by_artifact_path`
- `ratified_by_artifact_id`
- `ratified_at`
- `effective_record`
- `reason`

Allowed `event_type` values in v1:

- `binding_seeded`
- `binding_rebound`

Field law:

- `office_id` is the stable office key from `AGENTS.md`
- `office_binding_version` is monotonically increasing per office
- `binding_seeded` is the first repo-native witness for an office binding and may use `binding_state_before: null`
- `binding_rebound` records a later lawful change without rewriting prior lines, even when the office stays `active`
- `effective_record` is the full post-event effective row that should appear in `office-harness-bindings.effective.json`
- `effective_record` must repeat the ratification pointer family and the effective binding state

## 2. Rematerialization Rule

`office-harness-bindings.effective.json` is rebuilt with this deterministic rule:

1. read every non-empty JSONL line in ledger order
2. reject any event that fails the v1 field contract
3. group events by `office_id`
4. choose the latest lawful event for each office by `office_binding_version`, then `occurred_at`, then `event_id`
5. emit that event's `effective_record`
6. sort the output rows by the federal office order declared in `AGENTS.md`

No renderer-time fields belong in the effective rows.
Report timestamps stay in validator report artifacts, not in the effective registry.

## 3. Subordination And Replaceability

The precedence chain remains:

1. `AGENTS.md`
2. `orchestration/state/impl/OFFICE-HARNESS-BINDING-CONTRACT-v1.md`
3. per-office `OFFICE-HARNESS-METADATA.v1.yaml`
4. `office-harness-binding-ledger.jsonl`
5. `office-harness-bindings.effective.json`

Consequences:

- the ledger is append-only witness, not a license to outrank metadata
- the effective registry is replaceable and may be regenerated after deletion
- metadata and contract drift must be repaired by new ledger events or metadata correction, not by editing old ledger lines

## 4. Operator

The repo-native rematerializer for v1 is:

- `operators/validators/rematerialize_office_harness_bindings.py`

It writes only the effective registry read model.
It does not ratify office identity, invent new offices, or supersede metadata law.
