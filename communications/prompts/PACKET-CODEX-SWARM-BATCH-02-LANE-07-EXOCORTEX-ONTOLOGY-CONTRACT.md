# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-batch-02-lane-07-exocortex-ontology-contract`  
**Surface**: `codex_parallel_session`  
**Role**: `analysis`  
**Date**: `2026-03-06`  
**Objective**: define the non-duplication contract between repo authority, exocortex coordination state, and ontology projection  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-07-EXOCORTEX-ONTOLOGY-CONTRACT.md`

## Decision Envelope

- **Trigger**: Batch 01 converged on the repo/exocortex/ontology split but left the contract under-specified
- **Selected approach**: define which classes of truth belong in each layer and what may never migrate silently between them
- **Alternatives considered**:
  - letting ontology act as semantic authority — rejected because projection must not become doctrine
- **Assumptions**:
  - the repo remains the sole ratification surface
- **Inherited constraints**:
  - write only to your assigned response file
  - do not edit shared files
- **Prior lineage**:
  - [EXOCORTEX-ONTOLOGY-UNIFICATION-CC90.md](/Users/system/syncrescendence/orchestration/state/impl/EXOCORTEX-ONTOLOGY-UNIFICATION-CC90.md)
  - [TRIBUTARY-UNIFICATION-SWARM-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/TRIBUTARY-UNIFICATION-SWARM-SYNTHESIS-v1.md)

## Anchors

- [EXOCORTEX-CONTROL-PLANE-CC91.md](/Users/system/syncrescendence/orchestration/state/impl/EXOCORTEX-CONTROL-PLANE-CC91.md)
- [EXOCORTEX-SURFACE-REGISTRY-CC90.md](/Users/system/syncrescendence/orchestration/state/impl/EXOCORTEX-SURFACE-REGISTRY-CC90.md)
- [EXOCORTEX-TELEOLOGY-REGISTRY-CC90.md](/Users/system/syncrescendence/orchestration/state/impl/EXOCORTEX-TELEOLOGY-REGISTRY-CC90.md)
- [CLOUDFLARED-ONTOLOGY-STAGE1.md](/Users/system/syncrescendence/orchestration/state/impl/CLOUDFLARED-ONTOLOGY-STAGE1.md)
- [ONTOLOGY-DOMAIN-STAGE1.md](/Users/system/syncrescendence/orchestration/state/impl/ONTOLOGY-DOMAIN-STAGE1.md)
- Batch 01 lane 07 response artifact

## Required Output

1. a three-column contract mapping what belongs in repo, exocortex, and ontology
2. non-duplication rules for each layer
3. promotion rules for direction-changing outputs
4. required lineage links between projected entities and repo ratification artifacts
5. top failure modes if control-plane convenience outruns authority law

## Constraints

- write only to `communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-07-EXOCORTEX-ONTOLOGY-CONTRACT.md`
- do not redesign the whole exocortex
- stay focused on authority, projection, and non-duplication

## Return Path

`communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-07-EXOCORTEX-ONTOLOGY-CONTRACT.md`

## Assessment Path

`communications/assessments/ASSESSMENT-CODEX-SWARM-BATCH-02-LANE-07-EXOCORTEX-ONTOLOGY-CONTRACT.md`
