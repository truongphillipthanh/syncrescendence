# Response

**Response ID**: `RSP-20260306-codex-swarm-wave-2-lane-06-validator-normalization`  
**Surface**: `codex_parallel_session`  
**Role**: `drafting`  
**Date**: `2026-03-06`  
**Dispatch packet**: `PKT-20260306-codex-swarm-wave-2-lane-06-validator-normalization`  
**Result state**: `complete`

## Returned Content

The validator/template pack should remain optional and thin. The normalization target is the ratified disposition schema, the pedigree custody law, and the promotion-threshold minimums. It should validate current contract fields and joins; it should not yet become a migration engine, adjudicator, or auto-repair layer.

## 1. Normalized Validator Rule Set

Use current schema vocabulary only.

### 1.1 Registry CSV rules

Enforce immediately:

1. Header must exactly match the normative v1 header:
   `candidate_id,schema_version,source_tributary,source_path,source_relpath_hash,artifact_class,artifact_format,lineage_witness,provenance_sensitivity,authority_score,present_relevance,compaction_yield,duplication_status,review_basis,chosen_disposition,destination_lane,destination_artifact_path,archive_manifest_path,receipt_path,external_pointer,merge_family_id,justification,record_state,intake_batch_id,last_action_at,last_action_by,dest_artifact_hash,supersedes_candidate_id,notes`
2. `schema_version` must be `v1`.
3. Enum fields must stay inside ratified sets:
   - `source_tributary`: `live_shell`, `syncrescendence_old`, `syncrescendence_pre_schematic_design`
   - `artifact_class`: `law`, `reference`, `playbook`, `operator`, `executive`, `office_state`, `manifest`, `source`, `log`, `other`
   - `artifact_format`: `md`, `json`, `yaml`, `py`, `sh`, `directory_manifest`, `binary`, `mixed`, `other`
   - `provenance_sensitivity`: `low`, `medium`, `high`, `restricted`
   - `duplication_status`: `unique`, `duplicate_family`, `superseded`, `derived`, `unknown`
   - `review_basis`: `manual_read`, `family_sample`, `validator_scan`, `merged_adjudication`, `other`
   - `chosen_disposition`: `none`, `promote_live_law`, `promote_sigma`, `promote_sigma_reference`, `promote_playbook`, `promote_operator`, `retain_pedigree_rehoused`, `retain_archive_manifest_only`, `externalize_to_exocortex`, `cull_with_receipt`
   - `record_state`: `intake_pending`, `triaged`, `adjudicated`, `scheduled`, `executed`, `verified`, `closed`, `exception`
4. Score fields must be integers in `0..5`:
   - `authority_score`
   - `present_relevance`
   - `compaction_yield`
5. Path fields must be repo-relative or literal `none`:
   - `source_path`
   - `destination_artifact_path`
   - `archive_manifest_path`
   - `receipt_path`
6. `candidate_id` must match `^tdc-[a-z0-9-]+-[0-9]{4}$`.
7. `source_relpath_hash` and `dest_artifact_hash` must use `sha256:` form when populated.
8. `last_action_at` must be ISO-8601 UTC with trailing `Z`.
9. `candidate_id` must be unique.
10. `source_relpath_hash` must be unique unless the newer row populates `supersedes_candidate_id`.
11. `chosen_disposition=none` is lawful only while `record_state` is `intake_pending`, `triaged`, or `exception`.
12. Disposition-specific field requirements must be met by `executed`:
   - promotion dispositions require populated `destination_lane`, `destination_artifact_path`, and `receipt_path`
   - `retain_pedigree_rehoused` requires `destination_lane=pedigree/rehoused`, populated `destination_artifact_path`, and populated `receipt_path`
   - `retain_archive_manifest_only` requires populated `archive_manifest_path` and `receipt_path`, with `destination_lane=none` and `destination_artifact_path=none`
   - `externalize_to_exocortex` requires populated `external_pointer` and `receipt_path`, with `destination_lane=none` and `destination_artifact_path=none`
   - `cull_with_receipt` requires populated `receipt_path`, with `destination_lane=none`, `destination_artifact_path=none`, `archive_manifest_path=none`, and `external_pointer=none`
13. `receipt_path` must be populated for every row in `executed`, `verified`, or `closed`.
14. `destination_artifact_path` must be populated for promotion and rehousing dispositions by `executed`.
15. `dest_artifact_hash` must be populated for promotion and rehousing dispositions by `verified`.

Defer:

- duplicate-family semantic adjudication
- score calibration beyond type/range
- path existence checks outside explicit receipt/manifest joins
- automatic correction or rewrite behavior

### 1.2 Ledger JSONL rules

Enforce immediately:

1. Every line must be one JSON object.
2. `schema_version` must be `v1`.
3. `event_id` must match `^tdl-[0-9]{8}-[0-9]{4}$` and be unique.
4. `event_type` must be one of:
   `row_intake`, `row_triaged`, `row_adjudicated`, `row_scheduled`, `row_executed`, `row_verified`, `row_closed`, `row_exception`, `row_corrected`
5. `occurred_at` must be ISO-8601 UTC with trailing `Z`.
6. `row_version` must start at `1` and be contiguous per `candidate_id`.
7. State transitions must obey the ratified transition table.
8. The latest ledger event for each `candidate_id` must match CSV `record_state`, `last_action_at`, and `last_action_by`.
9. `field_changes` must contain only mutated fields.
10. `closed` rows must have previously passed through `verified`.

Defer:

- cross-event semantic sufficiency of `reason`
- automated reconstruction of missing ledger history
- deep audit of whether every meaningful mutation was captured

### 1.3 Pedigree manifest rules

Enforce immediately against custody-law minimums:

1. Required manifest fields must exist:
   - `manifest_id`
   - `manifest_type`
   - `label`
   - `source_tributary`
   - `source_root`
   - `source_scope`
   - `created_at_utc`
   - `created_by`
   - `disposition_status`
   - `authority_status`
   - `cautionary_status`
   - `summary`
   - `artifact_classes`
   - `receipt_links`
2. `manifest_type` must be one of:
   `shell`, `family`, `tranche`, `manifest_only`
3. `authority_status` must be one of:
   `not-live-authority`, `mixed-authority-risk`
4. `cautionary_status` must be one of:
   `none`, `partial`, `full`
5. If any covered body is externalized or retained only by pointer, `external_pointers` must be present.
6. If classification or family boundaries remain unresolved, `notes_on_ambiguity` must be present.
7. If live artifacts were produced from covered source, `retained_derivatives` must be present.
8. If `cautionary_status` is `partial` or `full`, `cautionary_reason` must be present and lawful.
9. `receipt_links` must point to one or more receipt artifacts.

Defer:

- full subtree coverage completeness
- whether bounded scope was optimally chosen
- manifest-level semantic judgment about family boundaries

### 1.4 Pedigree receipt rules

Enforce immediately against custody-law minimums:

1. Required receipt fields must exist:
   - `receipt_id`
   - `receipt_type`
   - `label`
   - `timestamp_utc`
   - `actor`
   - `artifact_class`
   - `reason`
   - `disposition`
   - `authority_status`
   - `cautionary_status`
   - `content_integrity`
2. A receipt must include `source_path` or `source_root`.
3. A receipt must include `destination_path`, `destination_root`, or `external_pointer`.
4. `receipt_type` must be one of:
   `preserve-copy`, `subtree-sync`, `compact-then-promote`, `externalize-with-manifest`, `cull-with-receipt`
5. `content_integrity` must be one of:
   `exact-copy`, `normalized-copy`, `partial-extract`, `compacted-derivative`, `family-move`, `manifest-only`
6. `authority_status` must be one of:
   `not-live-authority`, `mixed-authority-risk`
7. `cautionary_status` must be one of:
   `none`, `partial`, `full`
8. `related_manifest` is required for subtree-level, family-level, and externalization events.
9. `related_derivatives` is required when live derivatives were produced.
10. `replacement_artifact` is required for culls and compactions.
11. `reconstructability` is required for externalization and cull events.
12. `deletion_scope` is required when the event removes in-repo body material.
13. If `cautionary_status` is `partial` or `full`, `cautionary_reason` must be present and lawful.

Defer:

- cryptographic body verification
- content-diff classification beyond declared enum values
- normalization of multi-source events beyond the bounded-event minimum

### 1.5 Cautionary-status rules

Enforce immediately:

1. `cautionary_status` may only be `none`, `partial`, or `full`.
2. `cautionary_reason` may only be:
   `hidden_authority`, `rejected_topology`, `superseded_doctrine`, `unsafe_runtime_assumption`, `negative_exemplar`, `mixed_reuse_risk`
3. Any manifest or receipt with `cautionary_status` of `partial` or `full` must declare `cautionary_reason`.
4. Any artifact preserved under `pedigree/rehoused/` must explicitly carry `authority_status: not-live-authority`.

Defer:

- automatic inference of cautionary status from body text
- policy heuristics that infer `partial` versus `full`
- repo-wide scans for hidden-authority patterns

### 1.6 Promotion-threshold enforcement rules

Enforce immediately:

1. No direct `offices/` to `executive/` filing.
2. Nothing under `executive/` may be treated as lawful unless classed as `briefing`, `escalation`, or `summit`.
3. Dispatch records must not be filed as responses or logs merely because a dispatch lane is missing.
4. Prompts belong in `communications/prompts/`.
5. Responses belong in `communications/responses/`.
6. Dispatch records belong in `communications/dispatches/`.
7. Chronological operational traces belong in `communications/logs/`.

Defer:

- semantic judgment that a given artifact truly merits sovereign steering
- automatic relocation or synthesis of executive derivatives

## 2. Normalized Template Blocks

Use current path forms and enum forms only.

### 2.1 Registry row block

```yaml
candidate_id: tdc-syncold-law-0001
schema_version: v1
source_tributary: syncrescendence_old
source_path: syncrescendence_old/example/source.md
source_relpath_hash: sha256:EXAMPLEHASH
artifact_class: law
artifact_format: md
lineage_witness: none
provenance_sensitivity: medium
authority_score: 4
present_relevance: 4
compaction_yield: 3
duplication_status: unique
review_basis: manual_read
chosen_disposition: retain_pedigree_rehoused
destination_lane: pedigree/rehoused
destination_artifact_path: pedigree/rehoused/example/source.md
archive_manifest_path: none
receipt_path: pedigree/rehousing-receipts/RECEIPT-preserve-copy-20260306-0001.md
external_pointer: none
merge_family_id: none
justification: Preserve predecessor material as inspectable lineage, not live authority.
record_state: executed
intake_batch_id: PKT-20260306-codex-swarm-wave-2-lane-06-validator-normalization
last_action_at: 2026-03-06T12:00:00Z
last_action_by: codex_parallel_session
dest_artifact_hash: sha256:DESTHASH
supersedes_candidate_id: none
notes: none
```

### 2.2 Ledger event block

```yaml
schema_version: v1
event_id: tdl-20260306-0001
event_type: row_executed
occurred_at: 2026-03-06T12:00:00Z
actor: codex_parallel_session
candidate_id: tdc-syncold-law-0001
row_version: 4
record_state_before: scheduled
record_state_after: executed
field_changes:
  record_state:
    before: scheduled
    after: executed
  receipt_path:
    before: none
    after: pedigree/rehousing-receipts/RECEIPT-preserve-copy-20260306-0001.md
reason: Rehousing receipt written and custody event executed.
receipt_path: pedigree/rehousing-receipts/RECEIPT-preserve-copy-20260306-0001.md
notes: none
```

### 2.3 Manifest block

```yaml
manifest_id: MANIFEST-syncold-example-20260306
manifest_type: family
label: Example family manifest
source_tributary: syncrescendence_old
source_root: syncrescendence_old/example
source_scope:
  - syncrescendence_old/example/**
created_at_utc: 2026-03-06T12:00:00Z
created_by: codex_parallel_session
disposition_status: retained_pedigree
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason: superseded_doctrine
summary: Preserved bounded predecessor family for lineage and study.
artifact_classes:
  - law
receipt_links:
  - pedigree/rehousing-receipts/RECEIPT-subtree-sync-20260306-0001.md
retained_derivatives:
  - communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-06-VALIDATOR-NORMALIZATION.md
notes_on_ambiguity: none
```

### 2.4 Receipt block

```yaml
receipt_id: RECEIPT-subtree-sync-20260306-0001
receipt_type: subtree-sync
label: Example subtree sync receipt
timestamp_utc: 2026-03-06T12:05:00Z
actor: codex_parallel_session
source_root: syncrescendence_old/example
destination_root: pedigree/rehoused/example
artifact_class: law
reason: Preserve predecessor family in successor shell with explicit non-live status.
disposition: retain_pedigree_rehoused
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason: superseded_doctrine
content_integrity: family-move
related_manifest: pedigree/archive-manifests/MANIFEST-syncold-example-20260306.md
related_derivatives:
  - communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-06-VALIDATOR-NORMALIZATION.md
```

### 2.5 Externalization receipt block

```yaml
receipt_id: RECEIPT-externalize-with-manifest-20260306-0001
receipt_type: externalize-with-manifest
label: Example externalization receipt
timestamp_utc: 2026-03-06T12:10:00Z
actor: codex_parallel_session
source_root: syncrescendence_old/example-large-family
external_pointer: exocortex://example-large-family
artifact_class: source
reason: Remove in-repo body while preserving bounded retrieval evidence.
disposition: externalize_to_exocortex
authority_status: not-live-authority
cautionary_status: none
content_integrity: manifest-only
related_manifest: pedigree/archive-manifests/MANIFEST-syncold-example-large-family-20260306.md
reconstructability: manifest-plus-pointer
deletion_scope: syncrescendence_old/example-large-family/**
```

### 2.6 Cautionary metadata block

```yaml
authority_status: not-live-authority
cautionary_status: full
cautionary_reason: negative_exemplar
```

## 3. Recommended Immediate Versus Deferred Enforcement Split

Immediate enforcement should be hard-fail for machine-checkable contract breaks only:

- exact CSV and JSONL structural compliance
- enum-set compliance
- state-transition legality
- required field presence
- disposition-specific conditional fields
- required receipt and manifest joins
- cautionary and authority metadata minimums
- promotion-threshold minimums from the addendum

Deferred enforcement should remain advisory until more law is ratified:

- family completeness and scope sufficiency
- substantive adjudication of promotion versus preservation
- duplicate-family resolution quality
- semantic review of `reason`, `justification`, or `summary`
- auto-repair, auto-relocation, or generalized migration logic
- heuristics that infer cautionary status from content

Recommended posture:

- `error` now for schema breakage, illegal transitions, missing required joins, and unlawful filing
- `warn` now for ambiguity, probable under-documentation, and likely family-coverage gaps
- `defer` for any rule that would require the validator to invent doctrine rather than test it

## 4. Top Failure Modes If Validator Rollout Outruns Law Maturity

1. The validator becomes a shadow constitution.
   It starts enforcing invented metadata, invented states, or invented routing burdens that are not ratified.

2. Optional tooling quietly becomes mandatory.
   Teams begin blocking lawful migration work on validator completeness instead of on manifests, receipts, and schema compliance.

3. Vocabulary drift reappears under a stricter surface.
   Old terms such as unratified dispositions or path conventions leak back in through templates and create non-joinable records.

4. Auto-fix behavior mutates authority without lawful review.
   Repair logic can reclassify artifacts, rewrite destinations, or imply promotion decisions the law has not delegated to tooling.

5. False negatives hide real custody risk.
   A validator that checks invented fields more aggressively than receipt/manifest joins can pass cosmetically rich records that still break chain of custody.

6. False positives push work into side channels.
   If the thin pack demands semantic certainty before the law allows it, operators will keep ad hoc notes and bypass the canonical registry.

7. Promotion checks become overbroad.
   Tooling may start treating ordinary communications artifacts as executive candidates without the addendum's steering threshold actually being met.

## 5. Status

- `complete`: normalized rule set, normalized template blocks, and immediate-versus-deferred split are defined against current schema vocabulary and law
- `partial`: no repository-wide implementation or validator code was produced in this lane
- `blocked`: none
