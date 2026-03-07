# Tributary Disposition Schema v1

**Version**: `v1`
**Canonical location**: `orchestration/state/registry/tributary-disposition-schema-v1.md`

## Purpose

This schema defines the canonical current-state registry and append-only mutation ledger for tributary artifact disposition.

The contract is:

- one CSV row per source artifact identity
- one JSONL event per meaningful mutation to that row
- receipts, manifests, and promoted artifacts remain separate artifacts joined by explicit fields

Canonical artifacts:

- `orchestration/state/registry/tributary-disposition-schema-v1.md`
- `orchestration/state/registry/tributary-disposition-registry.csv`
- `orchestration/state/registry/tributary-disposition-ledger.jsonl`

## Encoding and serialization

- All three files must be UTF-8 with LF line endings.
- CSV must have a single header row and no embedded newlines in any cell.
- JSONL must contain exactly one JSON object per line with no pretty-print wrapping.
- Repo-relative paths must not begin with `/`.
- The literal token `none` is the only null sentinel for optional string and path fields.
- Timestamps must be ISO-8601 UTC with a trailing `Z`.
- `source_relpath_hash` must be serialized as `sha256:` plus the lowercase hex digest of the UTF-8 bytes of `<source_tributary>|<source_path>`, where `|` is the literal delimiter and both fields are taken exactly from the CSV row with no extra whitespace or path rewriting.

## Current-state CSV contract

The CSV column order is normative and must match this exact header:

`candidate_id,schema_version,source_tributary,source_path,source_relpath_hash,artifact_class,artifact_format,lineage_witness,provenance_sensitivity,authority_score,present_relevance,compaction_yield,duplication_status,review_basis,chosen_disposition,destination_lane,destination_artifact_path,archive_manifest_path,receipt_path,external_pointer,merge_family_id,justification,record_state,intake_batch_id,last_action_at,last_action_by,dest_artifact_hash,supersedes_candidate_id,notes`

Field contract:

| Column | Type | Rule |
| --- | --- | --- |
| `candidate_id` | string | Unique row identity. Pattern: `^tdc-[a-z0-9-]+-[0-9]{4}$` |
| `schema_version` | string | Must be `v1` |
| `source_tributary` | enum | `live_shell`, `syncrescendence_old`, `syncrescendence_pre_schematic_design` |
| `source_path` | path | Repo-relative source artifact path |
| `source_relpath_hash` | string | Must equal `sha256:` plus the lowercase hex digest of the UTF-8 bytes of `<source_tributary>|<source_path>` using the exact row values and the literal `|` delimiter |
| `artifact_class` | enum | `law`, `reference`, `playbook`, `operator`, `executive`, `office_state`, `manifest`, `source`, `log`, `other` |
| `artifact_format` | enum | `md`, `json`, `yaml`, `py`, `sh`, `directory_manifest`, `binary`, `mixed`, `other` |
| `lineage_witness` | string | Witness family or source note. Use `none` if not needed |
| `provenance_sensitivity` | enum | `low`, `medium`, `high`, `restricted` |
| `authority_score` | integer | Integer `0` through `5` |
| `present_relevance` | integer | Integer `0` through `5` |
| `compaction_yield` | integer | Integer `0` through `5` |
| `duplication_status` | enum | `unique`, `duplicate_family`, `superseded`, `derived`, `unknown` |
| `review_basis` | enum | `manual_read`, `family_sample`, `validator_scan`, `merged_adjudication`, `other` |
| `chosen_disposition` | enum | `none`, `promote_live_law`, `promote_sigma`, `promote_sigma_reference`, `promote_playbook`, `promote_operator`, `retain_pedigree_rehoused`, `retain_archive_manifest_only`, `externalize_to_exocortex`, `cull_with_receipt` |
| `destination_lane` | string | Repo-relative lane root or `none` |
| `destination_artifact_path` | path | Repo-relative destination artifact path or `none` |
| `archive_manifest_path` | path | Repo-relative manifest path or `none` |
| `receipt_path` | path | Repo-relative custody receipt path or `none` |
| `external_pointer` | string | External pointer such as `exocortex://...` or `none` |
| `merge_family_id` | string | `mf-...` family id or `none` |
| `justification` | string | Single-line disposition reason |
| `record_state` | enum | `intake_pending`, `triaged`, `adjudicated`, `scheduled`, `executed`, `verified`, `closed`, `exception` |
| `intake_batch_id` | string | Batch or packet identifier that first enrolled the row |
| `last_action_at` | timestamp | Latest mutation time |
| `last_action_by` | string | Latest actor id |
| `dest_artifact_hash` | string | `sha256:` hash of the final destination artifact or `none` |
| `supersedes_candidate_id` | string | Prior row replaced by an intake correction or `none` |
| `notes` | string | Single-line narrow clarification or `none` |

## Controlled state transitions

Allowed forward transitions:

- `intake_pending -> triaged`
- `triaged -> adjudicated`
- `adjudicated -> scheduled`
- `scheduled -> executed`
- `executed -> verified`
- `verified -> closed`

Allowed exception transitions:

- `intake_pending -> exception`
- `triaged -> exception`
- `adjudicated -> exception`
- `scheduled -> exception`
- `executed -> exception`
- `verified -> exception`
- `exception -> triaged`
- `exception -> adjudicated`

Illegal transitions include:

- `triaged -> executed`
- `adjudicated -> verified`
- `closed -> *`

## Disposition requirements

- `promote_live_law`, `promote_sigma`, `promote_sigma_reference`, `promote_playbook`, and `promote_operator` require populated `destination_lane`, `destination_artifact_path`, and `receipt_path` no later than `executed`.
- `retain_pedigree_rehoused` requires `destination_lane=pedigree/rehoused`, populated `destination_artifact_path`, and populated `receipt_path` no later than `executed`.
- `retain_archive_manifest_only` requires populated `archive_manifest_path` and `receipt_path`, with `destination_lane=none` and `destination_artifact_path=none`.
- `externalize_to_exocortex` requires populated `external_pointer` and `receipt_path`, with `destination_lane=none` and `destination_artifact_path=none`.
- `cull_with_receipt` requires populated `receipt_path`, with `destination_lane=none`, `destination_artifact_path=none`, `archive_manifest_path=none`, and `external_pointer=none`.

## Ledger JSONL contract

Each line in `tributary-disposition-ledger.jsonl` must be a JSON object with this shape:

| Key | Type | Rule |
| --- | --- | --- |
| `schema_version` | string | Must be `v1` |
| `event_id` | string | Unique ledger event id. Pattern: `^tdl-[0-9]{8}-[0-9]{4}$` |
| `event_type` | enum | `row_intake`, `row_triaged`, `row_adjudicated`, `row_scheduled`, `row_executed`, `row_verified`, `row_closed`, `row_exception`, `row_corrected` |
| `occurred_at` | timestamp | Event timestamp in UTC |
| `actor` | string | Office, agent, or operator id |
| `candidate_id` | string | Must match an existing or newly-created row id |
| `row_version` | integer | Starts at `1` and increments by `1` for each event for the same `candidate_id` |
| `record_state_before` | string or null | Prior row state |
| `record_state_after` | string | New row state |
| `field_changes` | object | Only mutated fields. Each key maps to `{ "before": <value>, "after": <value> }` |
| `reason` | string | Single-line reason for the mutation |
| `receipt_path` | path | Repo-relative receipt path or `none` |
| `notes` | string | Single-line note or `none` |

Event semantics:

- `field_changes` must only include fields that changed in that event.
- `last_action_at` in the CSV row must equal the latest ledger `occurred_at` for that `candidate_id`.
- `last_action_by` in the CSV row must equal the latest ledger `actor` for that `candidate_id`.
- The latest ledger event for a `candidate_id` must reproduce the CSV row's current `record_state`.
- Intake may create a row in `intake_pending` or `triaged`.
- `row_corrected` is for non-state corrections that still change current-state data and must not delete prior events.

## Minimal invariants

- `candidate_id` is unique in the CSV.
- `source_relpath_hash` is unique in the CSV unless `supersedes_candidate_id` is populated on the newer row.
- Each CSV row represents exactly one source artifact identity.
- Exactly one current `record_state` exists per `candidate_id`.
- `chosen_disposition=none` is allowed only in `intake_pending`, `triaged`, or `exception`.
- `receipt_path` must be populated for all rows in `executed`, `verified`, or `closed`.
- `destination_artifact_path` must be populated for promotion and rehousing dispositions by `executed`.
- `dest_artifact_hash` must be populated for promotion and rehousing dispositions by `verified`.
- `merge_family_id` may be shared across rows, but `candidate_id` may not.
- Ledger history is append-only. Prior ledger lines must never be edited in place.

## Minimal validator checks

1. CSV header matches the normative header exactly.
2. Every enum value is inside its allowed set.
3. Every score is an integer in `0..5`.
4. Every path field is repo-relative or `none`.
5. Every timestamp is parseable UTC ISO-8601 with `Z`.
6. Every `candidate_id` is unique in the CSV.
7. Every `event_id` is unique in the JSONL.
8. `row_version` is contiguous per `candidate_id`.
9. Ledger state transitions are legal under the transition table.
10. Latest ledger state and actor match the CSV row.
11. Disposition-specific required fields are populated by the required state.
12. Rows in `closed` must previously pass through `verified`.
