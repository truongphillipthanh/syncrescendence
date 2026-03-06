# Tributary Ratification Writeset Synthesis v1

**Date**: 2026-03-06
**Class**: assessment + adjudication + implementation handoff
**Scope**: Batch 03 Codex swarm on tributary ratification writes

## 1. Executive Synthesis

Batch 03 is sufficient for a first direct-write pass.

The safe boundary is now clear:

- ratify the control plane under `orchestration/state/registry/`
- ratify the narrow law files that Batch 02 already settled in principle
- physicalize the missing `communications/dispatches/` lane
- defer registry population, subtree sync, and validator rollout until their vocabularies are normalized to the new control plane

The batch should not be read as permission to start broad migration.

It should be read as permission to stop carrying the contract layer only in chat and turn it into repo-native law.

## 2. Stable Convergences

### 2.1 Registry control plane

Lane 01 provides the canonical registry and ledger contract.

The authoritative control-plane set is:

- `orchestration/state/registry/tributary-disposition-schema-v1.md`
- `orchestration/state/registry/tributary-disposition-registry.csv`
- `orchestration/state/registry/tributary-disposition-ledger.jsonl`

The schema wins on:

- field names
- allowed `chosen_disposition` values
- `record_state` values
- repo-relative path form
- append-only ledger behavior

### 2.2 Sigma ratification

Lane 02 correctly restores the missing middle rung:

- `knowledge/canon/` = bind-on-default doctrine
- `knowledge/sigma/` = repeated-use secondary doctrine
- `knowledge/sigma/references/` = housed reference subtype under Sigma
- `knowledge/feedstock/` = intake floor

The live `knowledge/references/` tree remains temporarily in place only as a compatibility form of `knowledge/sigma/references/`.

### 2.3 Pedigree custody

Lane 03 correctly defines `pedigree/` as custody, not soft authority.

The immediate law surface is:

- preserve ancestry
- prove movement through manifests and receipts
- keep cautionary status semantic even if `pedigree/cautionary/` is not yet physicalized
- forbid preserved material from silently regaining live authority

### 2.4 Promotion thresholds and dispatch lane

Lane 04 closes a real physical gap.

The shell already needed a distinct dispatch lane, but `communications/dispatches/` did not exist.

The ratified routing thresholds are:

- `offices/` -> `communications/` when lineage becomes durable
- `communications/` -> `executive/` only when steering burden exists
- never `offices/` -> `executive/` directly

### 2.5 Witness, externalization, and lineage law

Lane 05 is substantively correct:

- live shell controls present behavior
- `neo` is the default successor witness
- `old` remains explicit when burden-bearing rationale would otherwise be lost
- externalization follows classification and compaction
- repo ratifies, exocortex coordinates, ontology projects

Its only required correction was vocabulary discipline: the registry schema, not the local draft, defines the canonical disposition and state enums.

## 3. Adjudicated Collisions

### 3.1 Lane 01 versus Lanes 05-07 vocabulary drift

Lane 01 wins.

No live law, seed row, or validator template should reintroduce incompatible disposition names such as `promote_reference` or path forms that rely on absolute filesystem paths.

### 3.2 Lane 06 is sequencing input, not Wave 1 write material

The first migration seed set is useful, but not yet safe as live registry population.

It still needs:

- `tdc-*` candidate ids
- repo-relative path normalization
- exact `chosen_disposition` values from the schema
- destination paths that refer only to already-ratified artifacts

### 3.3 Lane 07 remains subordinate

Validator templates are desirable, but they must follow ratified law and schema rather than compete with them.

Wave 1 should therefore ratify the law first and defer template enforcement.

## 4. Smallest Safe Direct-Write Pass

Write now:

1. `orchestration/state/registry/tributary-disposition-schema-v1.md`
2. `orchestration/state/registry/tributary-disposition-registry.csv` as header-only
3. `orchestration/state/registry/tributary-disposition-ledger.jsonl` as empty
4. `orchestration/state/impl/WITNESS-EXTERNALIZATION-LAW-v1.md`
5. `orchestration/state/impl/KNOWLEDGE-LANE-LAW-v1.md`
6. `knowledge/sigma/README.md`
7. `pedigree/PEDIGREE-CUSTODY-LAW-v1.md`
8. `orchestration/state/impl/PROMOTION-THRESHOLDS-v1.md`
9. `communications/dispatches/README.md`

Defer:

- live registry rows
- ledger example events
- `knowledge/references/` subtree sync into `knowledge/sigma/references/`
- pedigree README rewrites outside the core law artifact
- validator templates and automated enforcement

## 5. Next Waves

The next lawful waves are:

1. compatibility notes and lane README cleanup
2. normalized first registry population
3. bounded Sigma subtree sync with receipts
4. validator and template rollout

Those waves should proceed only after the Wave 1 control plane and law files are present in the repo.

## 6. Inputs

Primary response artifacts:

- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-BATCH-03-LANE-00-COORDINATOR.md`
- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-BATCH-03-LANE-01-REGISTRY-ARTIFACTS.md`
- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-BATCH-03-LANE-02-SIGMA-RATIFICATION.md`
- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-BATCH-03-LANE-03-PEDIGREE-CUSTODY.md`
- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-BATCH-03-LANE-04-PROMOTION-AND-DISPATCH.md`
- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-BATCH-03-LANE-05-WITNESS-EXTERNALIZATION-LAW.md`
- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-BATCH-03-LANE-06-FIRST-MIGRATION-SEED-SET.md`
- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-BATCH-03-LANE-07-VALIDATOR-TEMPLATES.md`
