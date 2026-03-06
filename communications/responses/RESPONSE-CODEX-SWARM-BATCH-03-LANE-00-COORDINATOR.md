# Response

**Response ID**: `RSP-20260306-codex-swarm-batch-03-lane-00-coordinator`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-06`
**Dispatch packet**: `PKT-20260306-codex-swarm-batch-03-lane-00-coordinator`
**Result state**: `partial`

## 1. Convergence Map Across Batch 03 Draft Lanes

| Lane | Draft contribution | Converged use |
| --- | --- | --- |
| 01 `REGISTRY-ARTIFACTS` | defines the control-plane shape for schema, current-state CSV, and append-only JSONL ledger | this is the canonical contract and all later drafting should import its field names, state machine, and repo-relative path rules |
| 02 `SIGMA-RATIFICATION` | restores `knowledge/sigma/`, treats bare `knowledge/references/` as temporary compatibility housing, and provides a full replacement for `KNOWLEDGE-LANE-LAW-v1.md` | safe for immediate integration as the governing knowledge-lane update |
| 03 `PEDIGREE-CUSTODY` | defines `pedigree/` as custody rather than live authority, makes cautionary status semantic-first, and routes migration receipts to `pedigree/rehousing-receipts/` | safe for immediate integration at the law layer |
| 04 `PROMOTION-AND-DISPATCH` | restates the two promotion thresholds and physicalizes `communications/dispatches/` as the durable routing lane | safe for immediate integration as a compact addendum plus new dispatch lane README |
| 05 `WITNESS-EXTERNALIZATION-LAW` | combines witness precedence, collision recording, externalization gating, and repo/exocortex/ontology lineage | safe in substance; its local enum block must defer to Lane 01 vocabulary before write-through |
| 06 `FIRST-MIGRATION-SEED-SET` | identifies the first doctrinal families, compatibility-safe Sigma rehousings, and candidate manifests/receipts | useful sequencing input, but not yet safe for direct write as live registry population |
| 07 `VALIDATOR-TEMPLATES` | proposes thin validators and reusable field blocks | useful only after its field names, enum values, and path rules are normalized to Lane 01 and the ratified law files |

## 2. Collision Map

| Collision | Impacted lanes | Why material | Coordinator adjudication |
| --- | --- | --- | --- |
| Registry vocabulary mismatch | 01, 05, 06, 07 | Lane 01 uses `tdc-*` ids, repo-relative paths, and `chosen_disposition` values such as `promote_sigma` and `promote_sigma_reference`; Lanes 05-07 still use `promote_reference`, `retain_pedigree`, `merge-promote`, `dual-witness retain`, `CAND-*`, and absolute paths | Lane 01 wins. No seed rows, validator templates, or shared enum lists should be written until they import Lane 01 names verbatim. |
| Seed rows point at non-ratified destination artifacts | 06 | several planned destination files in `knowledge/canon/` and `orchestration/state/impl/` do not yet exist in the live tree, so writing these rows now would overstate execution state | defer Lane 06 from the immediate pass; only bring it forward after the law files exist and the row shape is normalized |
| Sigma ratification versus live `knowledge/references/` path reality | 02 plus live tree | the live repo still has many non-response references to `knowledge/references/`, and `knowledge/sigma/` does not yet exist | ratify Sigma language now, keep compatibility semantics explicit, and defer bulk path rewrites and subtree sync to a later wave |
| Scope inflation beyond the minimum write set | 03, 04, 07 | Lane 03 proposes README rewrites for `pedigree/archive-manifests/` and `pedigree/rehousing-receipts/`, but those files already exist; Lane 07 adds templates before the canonical schema is settled in tooling form | keep Wave 1 to new law/control-plane artifacts only; defer README cleanup and templates |

## 3. Exact Smallest Direct-Write Pass Safe To Integrate Immediately

This pass should stop at the control plane and law layer. It should not write invented registry population, subtree-sync copies, or tooling that redefines the schema.

### Wave 1 write set

1. Create `orchestration/state/registry/`.
2. Write `orchestration/state/registry/tributary-disposition-schema-v1.md` from Lane 01.
3. Write `orchestration/state/registry/tributary-disposition-registry.csv` as header-only using the exact Lane 01 header.
4. Write `orchestration/state/registry/tributary-disposition-ledger.jsonl` empty.
5. Write `orchestration/state/impl/WITNESS-EXTERNALIZATION-LAW-v1.md` from Lane 05, but replace its local disposition and witness enumeration block with references back to the Lane 01 schema instead of redefining incompatible values.
6. Replace `orchestration/state/impl/KNOWLEDGE-LANE-LAW-v1.md` with the Lane 02 replacement.
7. Create `knowledge/sigma/README.md` from Lane 02.
8. Write `pedigree/PEDIGREE-CUSTODY-LAW-v1.md` from Lane 03.
9. Write `orchestration/state/impl/PROMOTION-THRESHOLDS-v1.md` from Lane 04.
10. Create `communications/dispatches/README.md` from Lane 04.

### Explicit exclusions from Wave 1

- do not write Lane 01 illustrative CSV rows or JSONL examples as live records
- do not write Lane 06 seed rows until ids, enums, and path forms match Lane 01
- do not subtree-sync `knowledge/references/*` into `knowledge/sigma/references/*` yet
- do not rewrite existing `pedigree/archive-manifests/README.md` or `pedigree/rehousing-receipts/README.md` yet
- do not ship Lane 07 templates until they import the canonical schema vocabulary

## 4. Recommended Order For Subsequent Write Waves

### Wave 2: compatibility and top-level lane cleanup

- add the Lane 02 compatibility note to the legacy `knowledge/references/` surface
- update top-level readmes that still describe bare `knowledge/references/` as the sovereign secondary lane
- update communications lane docs to include `communications/dispatches/`

### Wave 3: first lawful registry population

- normalize Lane 06 candidate ids to the `tdc-*` pattern
- convert all source and destination paths to repo-relative form
- convert all proposed dispositions to Lane 01 `chosen_disposition` values
- only then seed the first registry rows, manifests, and receipts

### Wave 4: Sigma subtree sync and compatibility-safe rehousing

- create `knowledge/sigma/references/` only when the compatibility note, receipts, and first bounded subtree sync are ready together
- keep the current `knowledge/references/` tree readable until the sync receipts exist

### Wave 5: validator and template pack

- rewrite Lane 07 templates to import the ratified schema and law files
- then add validator checks for registry rows, manifests, receipts, cautionary metadata, and promotion metadata

## 5. Status

`partial`

Batch 03 is sufficient to support an immediate direct-write pass, but only for the law/control-plane layer.

The batch is not yet fully merge-ready as a populated write set because:

- Lane 06 seed rows are still examples rather than schema-valid live rows
- Lane 05 and Lane 07 still redefine vocabulary that Lane 01 already settled
- the live repo still contains unresolved `knowledge/references/` path reality that requires staged compatibility handling rather than immediate mass rehousing

The safe outcome is therefore:

- Wave 1: integrate the law and empty control-plane artifacts now
- later waves: normalize and populate
