# Pedigree Custody Law v1

**Status**: ratified compact law
**Scope**: `pedigree/` custody, manifests, receipts, and cautionary status
**Purpose**: preserve ancestry, prove movement, and prevent preserved material from silently regaining live authority

## 1. Law

`pedigree/` is a custody lane, not a live authority lane.

Artifacts in `pedigree/` exist to preserve provenance, demonstrate movement, retain evidence, and warn against reenactment. Presence in `pedigree/` does not grant present operational authority.

The lane is divided by burden:

- `pedigree/originals/` preserves thin exact-form evidence whose original wording, layout, or file body matters
- `pedigree/rehoused/` preserves inspectable predecessor material copied into the successor shell for ancestry and study
- `pedigree/archive-manifests/` preserves family-level, tranche-level, or root-level inventory records
- `pedigree/rehousing-receipts/` preserves event-level custody proofs for moves, syncs, extractions, compactions, externalizations, and culls
- `pedigree/cautionary/` may exist physically, but cautionary status must exist semantically even when the folder is deferred

## 2. Binding Rules

1. Every preserved subtree or preserved artifact class must be covered by either:
   - a manifest plus one or more linked receipts, or
   - an artifact-local receipt when the event is genuinely atomic

2. Every artifact preserved under `pedigree/rehoused/` must be explicitly marked `authority_status: not-live-authority`.

3. Every event recorded in `pedigree/rehousing-receipts/` must state:
   - what moved
   - why it moved
   - what custody class it entered
   - whether the body is exact, normalized, partial, compacted, or manifest-only

4. Cautionary status is mandatory metadata.
   The physical `pedigree/cautionary/` lane is optional in the first write set, but `cautionary_status` and `cautionary_reason` are not optional when risk exists.

5. `pedigree/originals/` is a thin authenticity reserve.
   It must not become the bulk holding area for all predecessor material.

6. `pedigree/archive-manifests/` describes bounded custody scope.
   A manifest must not be a vague shelf label. It must identify source scope, disposition, and linked receipts or pointers.

7. `pedigree/rehousing-receipts/` is chain-of-custody evidence.
   A receipt must not merely say that a copy occurred. It must state lawful reason, result, and reconstructability.

8. Manifest-only retention is lawful.
   When a body is externalized or intentionally not retained in-repo, the manifest and receipt pair must still preserve source scope, disposition, and retrieval pointer.

9. Preserved negative exemplars must not be silently reusable.
   If an artifact is kept partly or primarily as a warning, it must carry cautionary metadata that automation can test.

10. Promotion lineage must remain joinable.
    If a live artifact is derived from a pedigree source, the relevant manifest and/or receipt must link the derived artifact path.

## 3. Minimum Required Metadata

### 3.1 Manifest minimums

Every manifest must include:

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

Allowed `manifest_type` values:

- `shell`
- `family`
- `tranche`
- `manifest_only`

Allowed `authority_status` values:

- `not-live-authority`
- `mixed-authority-risk`

Allowed `cautionary_status` values:

- `none`
- `partial`
- `full`

Additional fields become required by circumstance:

- `external_pointers` when any covered body is externalized or retained only by pointer
- `notes_on_ambiguity` when classification or family boundaries remain unresolved
- `retained_derivatives` when live artifacts were produced from the covered source

### 3.2 Receipt minimums

Every receipt must include:

- `receipt_id`
- `receipt_type`
- `label`
- `timestamp_utc`
- `actor`
- `source_path` or `source_root`
- `destination_path`, `destination_root`, or `external_pointer`
- `artifact_class`
- `reason`
- `disposition`
- `authority_status`
- `cautionary_status`
- `content_integrity`

Allowed `receipt_type` values:

- `preserve-copy`
- `subtree-sync`
- `compact-then-promote`
- `externalize-with-manifest`
- `cull-with-receipt`

Allowed `content_integrity` values:

- `exact-copy`
- `normalized-copy`
- `partial-extract`
- `compacted-derivative`
- `family-move`
- `manifest-only`

Additional fields become required by circumstance:

- `related_manifest` for subtree-level, family-level, and externalization events
- `related_derivatives` when live derivatives were produced
- `replacement_artifact` for culls and compactions
- `reconstructability` for externalization and cull events
- `deletion_scope` when the event removes in-repo body material

## 4. Cautionary Status

Cautionary status exists to stop historical preservation from being mistaken for present endorsement.

An artifact, manifest, or receipt must carry cautionary metadata when any of the following is true:

- it encodes a rejected topology
- it records hidden-authority behavior
- it is superseded doctrine still easy to misread as live law
- it contains unsafe runtime assumptions or stale environment bindings
- it is preserved mainly as a negative exemplar

Allowed `cautionary_reason` values:

- `hidden_authority`
- `rejected_topology`
- `superseded_doctrine`
- `unsafe_runtime_assumption`
- `negative_exemplar`
- `mixed_reuse_risk`

Interpretation:

- `cautionary_status: full` means warning value is primary
- `cautionary_status: partial` means the artifact mixes durable signal with operational risk
- `cautionary_status: none` means no meaningful reenactment risk is known

## 5. Naming and Join Rules

- manifests should be named with stable bounded scope, for example: `MANIFEST-<tributary>-<family>-<date>.md`
- receipts should be named with one custody event per file, for example: `RECEIPT-<event-class>-<date>-<seq>.md`
- `manifest_id` and `receipt_id` must be globally unique within the repo
- receipts may link multiple source paths only when they are one bounded event under one reason and one disposition
- a manifest may summarize many artifacts, but it must resolve to bounded scope rather than broad narrative prose

## 6. Prohibitions

- do not treat preserved pedigree files as live authority by location alone
- do not store unresolved debris in `pedigree/` without manifest or receipt coverage
- do not externalize a family without leaving manifest plus receipt evidence
- do not preserve hazardous exemplars without machine-readable cautionary status
- do not use `pedigree/rehousing-receipts/` for ordinary inter-office routing receipts

## 7. Operational Effect

If custody is uncertain, preserve the source with explicit `not-live-authority` status, write the receipt, and record ambiguity in the manifest. Ambiguity is lawful if declared. Silent status is not lawful.
