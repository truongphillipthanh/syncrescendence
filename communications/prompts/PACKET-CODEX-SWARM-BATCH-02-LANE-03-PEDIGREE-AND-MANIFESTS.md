# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-batch-02-lane-03-pedigree-and-manifests`  
**Surface**: `codex_parallel_session`  
**Role**: `analysis`  
**Date**: `2026-03-06`  
**Objective**: define the contract for preserved originals, archive manifests, and rehousing receipts inside `pedigree/`  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-03-PEDIGREE-AND-MANIFESTS.md`

## Decision Envelope

- **Trigger**: Batch 01 identified `pedigree/` as necessary but under-specified
- **Selected approach**: define sublanes, artifact classes, and minimum manifest/receipt requirements
- **Alternatives considered**:
  - treating pedigree as a generic archive shelf — rejected because it obscures provenance and cautionary status
- **Assumptions**:
  - preserved ancestry must remain legible without quietly acting as live law
- **Inherited constraints**:
  - write only to your assigned response file
  - do not edit shared files
- **Prior lineage**:
  - [TRIBUTARY-UNIFICATION-SWARM-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/TRIBUTARY-UNIFICATION-SWARM-SYNTHESIS-v1.md)
  - [ARCHIVE-FIT-TRANCHE-01.md](/Users/system/syncrescendence/orchestration/state/impl/ARCHIVE-FIT-TRANCHE-01.md)
  - [ARCHIVE-FIT-TRANCHE-02-SOURCES-SIGMA.md](/Users/system/syncrescendence/orchestration/state/impl/ARCHIVE-FIT-TRANCHE-02-SOURCES-SIGMA.md)

## Anchors

- [pedigree](/Users/system/syncrescendence/pedigree)
- [RETROFIT-TRANCHE-01-HIGH-VALUE-DOCS.md](/Users/system/syncrescendence/orchestration/state/impl/RETROFIT-TRANCHE-01-HIGH-VALUE-DOCS.md)
- [RETROFIT-TRANCHE-02-OFFICE-CONTRACTS.md](/Users/system/syncrescendence/orchestration/state/impl/RETROFIT-TRANCHE-02-OFFICE-CONTRACTS.md)
- Batch 01 lanes 01, 05, and 06 response artifacts

## Required Output

1. a proposed physical layout for preserved originals, manifests, receipts, and cautionary material
2. minimum metadata requirements for a pedigree manifest
3. minimum metadata requirements for a rehousing receipt
4. rules for when a preserved artifact also needs a cautionary tag
5. top failure modes if pedigree remains semantically soft

## Constraints

- write only to `communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-03-PEDIGREE-AND-MANIFESTS.md`
- do not propose restoring predecessor topology
- keep the result legible for future automation

## Return Path

`communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-03-PEDIGREE-AND-MANIFESTS.md`

## Assessment Path

`communications/assessments/ASSESSMENT-CODEX-SWARM-BATCH-02-LANE-03-PEDIGREE-AND-MANIFESTS.md`
