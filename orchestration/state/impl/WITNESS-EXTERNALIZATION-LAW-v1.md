# Witness Externalization Law v1

**Status**: ratified compact law
**Purpose**: define witness precedence, collision recording, externalization gating, and lineage requirements without reopening Batch 02 contract law

## 1. Core Rule

Repo ratifies.

Live witness governs present behavior.

`neo` supplies the default successor wording when no live-shell ratification already controls.

`old` remains explicit whenever removing it would erase burden-bearing rationale, thresholds, cautions, or exceptions that still matter to practice.

Unresolved incompatibility stays explicit.

Externalization follows classification and compaction judgment rather than convenience.

Ontology may project only traceable authority.

## 2. Witness Precedence

1. Evaluate each governing claim against the present live shell, the `neo` witness, and the `old` witness.
2. If a live-shell artifact already ratifies the claim, that live artifact controls present behavior.
3. If no live witness controls, `neo` is the default promotion base.
4. `old` must remain explicit whenever dropping it would erase a protocol, threshold, rationale, exception, or caution that changes practice.
5. No claim may be promoted by prose quality, convenience, or schema fit alone.
6. If `neo` and `old` cannot be reconciled without flattening a real difference, the family must be recorded as a collision rather than silently merged.

## 3. Collision Recording

A collision must be recorded when any of the following is true:

- the witnesses encode incompatible topology
- the witnesses govern different scopes and no live translation law exists
- the witnesses imply different enforcement thresholds or termination conditions
- the live shell has fragments of the family but not enough authority to claim a unified successor doctrine

Minimum collision record:

- `law_family_id`
- `governing_claim`
- `witnesses`
- `conflict_class`
- `collision_status`
- `notes_on_ambiguity`
- `ratification_pointer` or explicit `none` if not yet ratified

While a collision remains open, downstream artifacts may reference it, summarize it, or route around it, but they may not pretend it has already been lawfully unified.

## 4. Externalization Gating

Every bulky source, log, notebook, or duplicate family must follow this sequence:

1. classify and bound
2. compact or designate residue
3. externalize or cull
4. ratify and register

Advancement rules:

- no family may leave repo residence before a compacted derivative, a named stronger authority, or an explicit no-yield finding exists
- externalization is allowed only when reserve access still matters
- culling is allowed only when epistemic yield, operational yield, and provenance sensitivity are already captured or judged low
- after externalization or culling, the repo must still retain reviewable residue

Minimum repo-native residue:

- `original_path` or family path pattern
- `tributary`
- `artifact_class`
- `chosen_disposition`
- `count_size_snapshot`
- `rationale`
- `replacement_artifact` if one exists
- `external_pointer` when the body leaves the repo

## 5. Lineage Requirements

Boundary law:

- repo ratifies
- exocortex coordinates
- ontology projects

Direction-changing meaning must return to the repo before the shell treats it as truth. Every shell-relevant projection or externalized record must preserve lineage back to authority.

Required lineage fields:

- `source_artifact_path`
- `source_artifact_id`
- `source_artifact_class`
- `ratification_pointer` for any direction-bearing claim
- `projection_timestamp`
- `upstream_snapshot_timestamp`

Lineage constraints:

- repo-ratified artifacts may carry authority within the meaning of the ratifying artifact
- exocortex snapshots may inform operations but may not self-ratify doctrine or legitimacy
- derived projections must point back to their upstream repo or snapshot witnesses and may not become hidden sovereigns
- projected entities must preserve explicit conflict when upstream witnesses disagree

## 6. Control-Plane Alignment

The migration control plane under `orchestration/state/registry/` is the canonical source for:

- `chosen_disposition` values
- `record_state` values
- current-state registry fields
- append-only ledger event vocabulary

This law does not redefine those enums locally.

When a witness or externalization decision is registered, the relevant control-plane artifacts must use the exact field names and allowed values from [tributary-disposition-schema-v1.md](/Users/system/syncrescendence/orchestration/state/registry/tributary-disposition-schema-v1.md).

Witness classes in this law are semantic ordering categories, not a competing registry enum block.

## 7. Out Of Scope For First Write Pass

The first ratification pass keeps the following out of scope:

- full family-by-family disposition tables
- storage-vendor or transport-specific exocortex implementation rules
- secret handling, credentials, and access-control law
- retention durations, quotas, or service-level targets
- exhaustive ontology schemas beyond the minimum lineage fields above
- detailed emergency exception doctrine beyond the rule that temporary action remains non-ratified until repo receipt exists

## 8. Failure Modes

If written too broadly:

1. The law starts swallowing topic-specific doctrine that should remain local.
2. Every upstream disagreement gets frozen as constitutional machinery, slowing practical ratification.
3. Exocortex or ontology implementation details harden prematurely into false law.

If written too narrowly:

1. Witness order becomes advisory and style-based merges return.
2. Raw families get externalized before compacted residue or receipts exist.
3. Control-plane state or schema convenience begins masquerading as authority because lineage minimums are missing.
