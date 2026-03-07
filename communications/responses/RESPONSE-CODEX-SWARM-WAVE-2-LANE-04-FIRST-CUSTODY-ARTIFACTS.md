# Response

**Response ID**: `RSP-20260306-first-custody-artifacts`  
**Surface**: `codex_parallel_session`  
**Date received**: `2026-03-06`  
**Dispatch packet**: `PKT-20260306-codex-swarm-wave-2-lane-04-first-custody-artifacts`  
**Result state**: `partial`  
**Receipt artifacts**:
- `communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-04-FIRST-CUSTODY-ARTIFACTS.md`

## Returned Content

This packet drafts the smallest bounded custody set that can support the first seed tranche without reopening broad migration:

- `3` manifests
- `5` receipts
- explicit cautionary metadata on all preserved doctrinal and lineage witnesses

Why `partial` rather than `complete`:

- the expected Wave 2 Lane 03 normalization response is not present in the repo
- the `tdc-*` ids, `merge_family_id` values, and row-level joins below are therefore inferred from the ratified schema plus the first seed draft
- these joins should be treated as the required alignment target for Lane 03, not as already-confirmed landed rows

## 1. Join Fields That Must Match The Normalized Registry Rows

These are the custody join fields that should be copied verbatim into the first normalized registry tranche.

| candidate_id | source_tributary | source_path | chosen_disposition | destination_artifact_path | archive_manifest_path | receipt_path | merge_family_id | record_state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `tdc-old-artifact-protocol-0001` | `syncrescendence_old` | `syncrescendence_old/01-CANON/CANON-00011-ARTIFACT_PROTOCOL-cosmos.md` | `promote_live_law` | `orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md` | `pedigree/archive-manifests/MANIFEST-old-first-seed-tranche-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md` | `mf-artifact-protocol-v1` | `scheduled` |
| `tdc-neo-artifact-protocol-0002` | `syncrescendence_pre_schematic_design` | `syncrescendence_pre_schematic_design/neocanon/CANON-1003-ARTIFACT_PROTOCOL.md` | `promote_live_law` | `orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md` | `pedigree/archive-manifests/MANIFEST-neo-first-seed-tranche-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md` | `mf-artifact-protocol-v1` | `scheduled` |
| `tdc-old-memory-architecture-0003` | `syncrescendence_old` | `syncrescendence_old/01-CANON/CANON-25000-MEMORY_ARCH-lattice.md` | `promote_live_law` | `knowledge/canon/MEMORY-ARCHITECTURE-v1.md` | `pedigree/archive-manifests/MANIFEST-old-first-seed-tranche-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-memory-architecture-20260306-02.md` | `mf-memory-architecture-v1` | `scheduled` |
| `tdc-neo-memory-architecture-0004` | `syncrescendence_pre_schematic_design` | `syncrescendence_pre_schematic_design/neocanon/CANON-3004-MEMORY_ARCHITECTURE.md` | `promote_live_law` | `knowledge/canon/MEMORY-ARCHITECTURE-v1.md` | `pedigree/archive-manifests/MANIFEST-neo-first-seed-tranche-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-memory-architecture-20260306-02.md` | `mf-memory-architecture-v1` | `scheduled` |
| `tdc-old-context-transition-0005` | `syncrescendence_old` | `syncrescendence_old/01-CANON/CANON-25100-CONTEXT_TRANS-lattice.md` | `promote_live_law` | `knowledge/canon/CONTEXT-TRANSITION-v1.md` | `pedigree/archive-manifests/MANIFEST-old-first-seed-tranche-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-context-transition-20260306-03.md` | `mf-context-transition-v1` | `scheduled` |
| `tdc-neo-context-transition-0006` | `syncrescendence_pre_schematic_design` | `syncrescendence_pre_schematic_design/neocanon/CANON-3005-CONTEXT_TRANSITION.md` | `promote_live_law` | `knowledge/canon/CONTEXT-TRANSITION-v1.md` | `pedigree/archive-manifests/MANIFEST-neo-first-seed-tranche-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-context-transition-20260306-03.md` | `mf-context-transition-v1` | `scheduled` |
| `tdc-old-research-protocols-0007` | `syncrescendence_old` | `syncrescendence_old/01-CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md` | `promote_sigma` | `knowledge/sigma/RESEARCH-PROTOCOLS-v1.md` | `pedigree/archive-manifests/MANIFEST-old-first-seed-tranche-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-research-protocols-20260306-04.md` | `mf-research-protocols-v1` | `scheduled` |
| `tdc-neo-research-protocols-0008` | `syncrescendence_pre_schematic_design` | `syncrescendence_pre_schematic_design/neocanon/CANON-3006-RESEARCH_PROTOCOLS.md` | `promote_sigma` | `knowledge/sigma/RESEARCH-PROTOCOLS-v1.md` | `pedigree/archive-manifests/MANIFEST-neo-first-seed-tranche-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-research-protocols-20260306-04.md` | `mf-research-protocols-v1` | `scheduled` |
| `tdc-old-lineage-0009` | `syncrescendence_old` | `syncrescendence_old/01-CANON/CANON-00002-LINEAGE-cosmos.md` | `retain_pedigree_rehoused` | `pedigree/rehoused/syncrescendence_old/01-CANON/CANON-00002-LINEAGE-cosmos.md` | `pedigree/archive-manifests/MANIFEST-lineage-dual-witness-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-preserve-copy-lineage-dual-witness-20260306-05.md` | `mf-lineage-dual-witness-v1` | `scheduled` |
| `tdc-neo-lineage-0010` | `syncrescendence_pre_schematic_design` | `syncrescendence_pre_schematic_design/neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md` | `retain_pedigree_rehoused` | `pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md` | `pedigree/archive-manifests/MANIFEST-lineage-dual-witness-20260306.md` | `pedigree/rehousing-receipts/RECEIPT-preserve-copy-lineage-dual-witness-20260306-05.md` | `mf-lineage-dual-witness-v1` | `scheduled` |

Normalization cautions embedded in the table:

- repo-relative source paths are required; the absolute `/Users/system/Desktop/...` forms from the earlier seed draft are not lawful row values
- `merge_family_id` must stay `mf-*`; the earlier `dwf-lineage-v1` form is not schema-valid
- the lineage witnesses join to preserved copies under `pedigree/rehoused/`, while `pedigree/ROSETTA-STONE.live.md` is tracked as a retained derivative rather than the preserved destination body

## 2. Patch-Ready Drafts For The First Bounded Manifest Set

### A. `pedigree/archive-manifests/MANIFEST-old-first-seed-tranche-20260306.md`

````md
# MANIFEST-old-first-seed-tranche-20260306

```yaml
manifest_id: MANIFEST-old-first-seed-tranche-20260306-01
manifest_type: tranche
label: "Old tributary doctrinal witnesses for the first seed tranche"
source_tributary: syncrescendence_old
source_root: syncrescendence_old/01-CANON
source_scope:
  - syncrescendence_old/01-CANON/CANON-00011-ARTIFACT_PROTOCOL-cosmos.md
  - syncrescendence_old/01-CANON/CANON-25000-MEMORY_ARCH-lattice.md
  - syncrescendence_old/01-CANON/CANON-25100-CONTEXT_TRANS-lattice.md
  - syncrescendence_old/01-CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md
created_at_utc: "2026-03-06T00:00:00Z"
created_by: codex_parallel_session
disposition_status: mixed
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - superseded_doctrine
  - mixed_reuse_risk
summary: "Bounded old-tributary doctrinal witnesses preserved for ancestry while compact derivatives are prepared elsewhere."
artifact_classes:
  - law
receipt_links:
  - pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md
  - pedigree/rehousing-receipts/RECEIPT-compact-then-promote-memory-architecture-20260306-02.md
  - pedigree/rehousing-receipts/RECEIPT-compact-then-promote-context-transition-20260306-03.md
  - pedigree/rehousing-receipts/RECEIPT-compact-then-promote-research-protocols-20260306-04.md
external_pointers: []
retained_derivatives:
  - orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md
  - knowledge/canon/MEMORY-ARCHITECTURE-v1.md
  - knowledge/canon/CONTEXT-TRANSITION-v1.md
  - knowledge/sigma/RESEARCH-PROTOCOLS-v1.md
notes_on_ambiguity: []
registry_join_fields:
  candidate_ids:
    - tdc-old-artifact-protocol-0001
    - tdc-old-memory-architecture-0003
    - tdc-old-context-transition-0005
    - tdc-old-research-protocols-0007
  merge_family_ids:
    - mf-artifact-protocol-v1
    - mf-memory-architecture-v1
    - mf-context-transition-v1
    - mf-research-protocols-v1
```
````

### B. `pedigree/archive-manifests/MANIFEST-neo-first-seed-tranche-20260306.md`

````md
# MANIFEST-neo-first-seed-tranche-20260306

```yaml
manifest_id: MANIFEST-neo-first-seed-tranche-20260306-01
manifest_type: tranche
label: "Pre-schematic doctrinal witnesses for the first seed tranche"
source_tributary: syncrescendence_pre_schematic_design
source_root: syncrescendence_pre_schematic_design/neocanon
source_scope:
  - syncrescendence_pre_schematic_design/neocanon/CANON-1003-ARTIFACT_PROTOCOL.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-3004-MEMORY_ARCHITECTURE.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-3005-CONTEXT_TRANSITION.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-3006-RESEARCH_PROTOCOLS.md
created_at_utc: "2026-03-06T00:00:00Z"
created_by: codex_parallel_session
disposition_status: mixed
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - superseded_doctrine
  - mixed_reuse_risk
summary: "Bounded pre-schematic doctrinal witnesses preserved as the default successor-wording reserve for the first seed tranche."
artifact_classes:
  - law
receipt_links:
  - pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md
  - pedigree/rehousing-receipts/RECEIPT-compact-then-promote-memory-architecture-20260306-02.md
  - pedigree/rehousing-receipts/RECEIPT-compact-then-promote-context-transition-20260306-03.md
  - pedigree/rehousing-receipts/RECEIPT-compact-then-promote-research-protocols-20260306-04.md
external_pointers: []
retained_derivatives:
  - orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md
  - knowledge/canon/MEMORY-ARCHITECTURE-v1.md
  - knowledge/canon/CONTEXT-TRANSITION-v1.md
  - knowledge/sigma/RESEARCH-PROTOCOLS-v1.md
notes_on_ambiguity: []
registry_join_fields:
  candidate_ids:
    - tdc-neo-artifact-protocol-0002
    - tdc-neo-memory-architecture-0004
    - tdc-neo-context-transition-0006
    - tdc-neo-research-protocols-0008
  merge_family_ids:
    - mf-artifact-protocol-v1
    - mf-memory-architecture-v1
    - mf-context-transition-v1
    - mf-research-protocols-v1
```
````

### C. `pedigree/archive-manifests/MANIFEST-lineage-dual-witness-20260306.md`

````md
# MANIFEST-lineage-dual-witness-20260306

```yaml
manifest_id: MANIFEST-lineage-dual-witness-20260306-01
manifest_type: family
label: "Dual-witness lineage preservation for the first seed tranche"
source_tributary: mixed
source_root: mixed
source_scope:
  - syncrescendence_old/01-CANON/CANON-00002-LINEAGE-cosmos.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md
created_at_utc: "2026-03-06T00:00:00Z"
created_by: codex_parallel_session
disposition_status: retained_pedigree
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - mixed_reuse_risk
summary: "The lineage family remains explicitly plural. Preserve both witnesses in pedigree rehoused form and link them to the live Rosetta derivative without laundering them into a single source body."
artifact_classes:
  - law
receipt_links:
  - pedigree/rehousing-receipts/RECEIPT-preserve-copy-lineage-dual-witness-20260306-05.md
external_pointers: []
retained_derivatives:
  - pedigree/ROSETTA-STONE.live.md
notes_on_ambiguity:
  - "Neo is the preferred live-facing summary witness, but old remains burden-bearing for ancestry and debt."
registry_join_fields:
  candidate_ids:
    - tdc-old-lineage-0009
    - tdc-neo-lineage-0010
  merge_family_ids:
    - mf-lineage-dual-witness-v1
```
````

## 3. Patch-Ready Drafts For The First Bounded Receipt Set

These four compaction receipts are intentionally drafted as artifact-local atomic events under the custody law.

That matters because:

- each receipt covers exactly one bounded dual-witness compaction
- all covered sources share one reason, one disposition, and one replacement artifact
- the tranche manifests provide inventory coverage, while the receipts prove the event itself

### A. `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-artifact-protocol-20260306-01.md`

````md
# RECEIPT-compact-then-promote-artifact-protocol-20260306-01

```yaml
receipt_id: RECEIPT-compact-then-promote-artifact-protocol-20260306-01
receipt_type: compact-then-promote
label: "Compact artifact protocol witnesses into live artifact law"
timestamp_utc: "2026-03-06T00:00:00Z"
actor: codex_parallel_session
source_path:
  - syncrescendence_old/01-CANON/CANON-00011-ARTIFACT_PROTOCOL-cosmos.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-1003-ARTIFACT_PROTOCOL.md
destination_path: orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md
artifact_class: law
reason: "Compact the highest-authority artifact protocol witnesses into one live law surface while keeping both sources explicitly non-live."
disposition: promote_live_law
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - superseded_doctrine
  - mixed_reuse_risk
content_integrity: compacted-derivative
related_derivatives:
  - orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md
replacement_artifact: orchestration/state/impl/SYNCRESCENDENT-ARTIFACT-LAW-v1.md
registry_join_fields:
  candidate_ids:
    - tdc-old-artifact-protocol-0001
    - tdc-neo-artifact-protocol-0002
  merge_family_id: mf-artifact-protocol-v1
```
````

### B. `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-memory-architecture-20260306-02.md`

````md
# RECEIPT-compact-then-promote-memory-architecture-20260306-02

```yaml
receipt_id: RECEIPT-compact-then-promote-memory-architecture-20260306-02
receipt_type: compact-then-promote
label: "Compact memory architecture witnesses into canon"
timestamp_utc: "2026-03-06T00:00:00Z"
actor: codex_parallel_session
source_path:
  - syncrescendence_old/01-CANON/CANON-25000-MEMORY_ARCH-lattice.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-3004-MEMORY_ARCHITECTURE.md
destination_path: knowledge/canon/MEMORY-ARCHITECTURE-v1.md
artifact_class: law
reason: "Compact the old burden witness and the neo successor witness into one bind-on-default memory doctrine."
disposition: promote_live_law
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - superseded_doctrine
  - mixed_reuse_risk
content_integrity: compacted-derivative
related_derivatives:
  - knowledge/canon/MEMORY-ARCHITECTURE-v1.md
replacement_artifact: knowledge/canon/MEMORY-ARCHITECTURE-v1.md
registry_join_fields:
  candidate_ids:
    - tdc-old-memory-architecture-0003
    - tdc-neo-memory-architecture-0004
  merge_family_id: mf-memory-architecture-v1
```
````

### C. `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-context-transition-20260306-03.md`

````md
# RECEIPT-compact-then-promote-context-transition-20260306-03

```yaml
receipt_id: RECEIPT-compact-then-promote-context-transition-20260306-03
receipt_type: compact-then-promote
label: "Compact context transition witnesses into canon"
timestamp_utc: "2026-03-06T00:00:00Z"
actor: codex_parallel_session
source_path:
  - syncrescendence_old/01-CANON/CANON-25100-CONTEXT_TRANS-lattice.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-3005-CONTEXT_TRANSITION.md
destination_path: knowledge/canon/CONTEXT-TRANSITION-v1.md
artifact_class: law
reason: "Compact the two context-transition witnesses into one live continuity doctrine while preserving both tributary forms as non-live ancestry."
disposition: promote_live_law
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - superseded_doctrine
  - mixed_reuse_risk
content_integrity: compacted-derivative
related_derivatives:
  - knowledge/canon/CONTEXT-TRANSITION-v1.md
replacement_artifact: knowledge/canon/CONTEXT-TRANSITION-v1.md
registry_join_fields:
  candidate_ids:
    - tdc-old-context-transition-0005
    - tdc-neo-context-transition-0006
  merge_family_id: mf-context-transition-v1
```
````

### D. `pedigree/rehousing-receipts/RECEIPT-compact-then-promote-research-protocols-20260306-04.md`

````md
# RECEIPT-compact-then-promote-research-protocols-20260306-04

```yaml
receipt_id: RECEIPT-compact-then-promote-research-protocols-20260306-04
receipt_type: compact-then-promote
label: "Compact research protocols witnesses into Sigma"
timestamp_utc: "2026-03-06T00:00:00Z"
actor: codex_parallel_session
source_path:
  - syncrescendence_old/01-CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-3006-RESEARCH_PROTOCOLS.md
destination_path: knowledge/sigma/RESEARCH-PROTOCOLS-v1.md
artifact_class: law
reason: "Compact the two research-protocol witnesses into a repeated-use Sigma derivative without overstating it as bind-on-default canon."
disposition: promote_sigma
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - superseded_doctrine
  - mixed_reuse_risk
content_integrity: compacted-derivative
related_derivatives:
  - knowledge/sigma/RESEARCH-PROTOCOLS-v1.md
replacement_artifact: knowledge/sigma/RESEARCH-PROTOCOLS-v1.md
registry_join_fields:
  candidate_ids:
    - tdc-old-research-protocols-0007
    - tdc-neo-research-protocols-0008
  merge_family_id: mf-research-protocols-v1
```
````

### E. `pedigree/rehousing-receipts/RECEIPT-preserve-copy-lineage-dual-witness-20260306-05.md`

````md
# RECEIPT-preserve-copy-lineage-dual-witness-20260306-05

```yaml
receipt_id: RECEIPT-preserve-copy-lineage-dual-witness-20260306-05
receipt_type: preserve-copy
label: "Preserve dual-witness lineage sources in pedigree rehoused form"
timestamp_utc: "2026-03-06T00:00:00Z"
actor: codex_parallel_session
source_path:
  - syncrescendence_old/01-CANON/CANON-00002-LINEAGE-cosmos.md
  - syncrescendence_pre_schematic_design/neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md
destination_path:
  - pedigree/rehoused/syncrescendence_old/01-CANON/CANON-00002-LINEAGE-cosmos.md
  - pedigree/rehoused/syncrescendence_pre_schematic_design/neocanon/CANON-2009-INTELLECTUAL_LINEAGE.md
artifact_class: law
reason: "Retain both lineage witnesses as inspectable ancestry because the family should remain plural rather than silently compacted into one cleaned paragraph."
disposition: retain_pedigree_rehoused
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - mixed_reuse_risk
content_integrity: exact-copy
related_manifest: pedigree/archive-manifests/MANIFEST-lineage-dual-witness-20260306.md
related_derivatives:
  - pedigree/ROSETTA-STONE.live.md
registry_join_fields:
  candidate_ids:
    - tdc-old-lineage-0009
    - tdc-neo-lineage-0010
  merge_family_id: mf-lineage-dual-witness-v1
```
````

## 4. Explicit Cautionary Usage Required In This First Set

Use `cautionary_status: partial` on:

- both doctrinal tranche manifests
- all four `compact-then-promote` receipts
- the lineage family manifest
- the lineage preserve-copy receipt

Use `cautionary_reason` values as follows:

- `superseded_doctrine` plus `mixed_reuse_risk` for the compacted doctrinal witness set
- `mixed_reuse_risk` for the preserved lineage family

Do not use `cautionary_status: none` for these witnesses, because the whole point of the custody layer is to stop preserved predecessor doctrine from reacquiring live authority by path mystique or silent reuse.

Do not use `cautionary_status: full` in this first tranche, because none of these artifacts are being preserved primarily as negative exemplars. They are burden-bearing witnesses with reuse risk, not warning-only specimens.

## 5. Top Failure Modes If Custody Artifacts Drift From The Schema

1. `merge-promote`, `dual-witness retain`, or `dwf-*` vocabulary leaks into the registry layer.
   That breaks joins against the ratified `chosen_disposition` enum and the `mf-*` family-id rule.

2. Absolute filesystem paths survive into custody or registry joins.
   The first seed draft used `/Users/system/Desktop/...`; the schema requires repo-relative paths only.

3. The lineage rows point at `pedigree/ROSETTA-STONE.live.md` as their `destination_artifact_path`.
   That would collapse preserved source custody into a live derivative and erase the distinction between retained witness and promoted artifact.

4. Sibling rows in one family do not share the same `receipt_path`.
   The family compaction event is one bounded act; drifting receipt paths would create false multiplicity and break later ledger reasoning.

5. `archive_manifest_path` is omitted on the drafted rows even though manifests exist.
   The registry would lose the inventory join that explains tranche scope and preserved witness coverage.

6. Draft-only custody artifacts are marked `executed` or `verified`.
   Until the actual manifest and receipt files exist outside this response, the lawful row state is `scheduled`.

7. Cautionary metadata is dropped because the artifacts feel familiar or respected.
   That is exactly how preserved doctrine silently regains live authority.

## 6. Status

- `partial`: the first bounded manifest and receipt drafts are written, cautionary rules are explicit, and the required row joins are specified
- remaining blocker: the repo does not currently contain `communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md`, so final alignment against a landed normalized-row artifact cannot yet be verified
