# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-batch-02-lane-04-promotion-thresholds`  
**Surface**: `codex_parallel_session`  
**Role**: `analysis`  
**Date**: `2026-03-06`  
**Objective**: define promotion thresholds between `offices/`, `communications/`, and `executive/` so authority does not silently drift  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-04-PROMOTION-THRESHOLDS.md`

## Decision Envelope

- **Trigger**: Batch 01 established the broad burden split but left promotion thresholds under-specified
- **Selected approach**: define the smallest possible decision rules for cross-lane promotion
- **Alternatives considered**:
  - case-by-case taste adjudication — rejected because it recreates hidden sovereign memory
- **Assumptions**:
  - local work should stay local unless authority, lineage, or steering requires promotion
- **Inherited constraints**:
  - write only to your assigned response file
  - do not edit shared files
- **Prior lineage**:
  - [OFFICE-LAW-v1.md](/Users/system/syncrescendence/orchestration/state/impl/OFFICE-LAW-v1.md)
  - [OFFICE-ARTIFACT-LAW-v1.md](/Users/system/syncrescendence/orchestration/state/impl/OFFICE-ARTIFACT-LAW-v1.md)
  - [COMMUNICATIONS-LAW-v1.md](/Users/system/syncrescendence/orchestration/state/impl/COMMUNICATIONS-LAW-v1.md)
  - [EXECUTIVE-LANE-LAW-v1.md](/Users/system/syncrescendence/orchestration/state/impl/EXECUTIVE-LANE-LAW-v1.md)

## Anchors

- Batch 01 lane 05 response artifact
- [offices](/Users/system/syncrescendence/offices)
- [communications](/Users/system/syncrescendence/communications)
- [executive](/Users/system/syncrescendence/executive)

## Required Output

1. explicit promotion thresholds for office-local -> communications
2. explicit promotion thresholds for communications -> executive
3. explicit non-promotion rules for artifacts that must remain local or communications-only
4. example classification of TASK / RECEIPT / RESULT / CONFIRM / ALERT / BRIEFING / EXECLOG
5. top hidden-authority failure modes if the thresholds are vague

## Constraints

- write only to `communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-04-PROMOTION-THRESHOLDS.md`
- prefer crisp decision rules over broad philosophy
- do not collapse executive into a generic importance lane

## Return Path

`communications/responses/RESPONSE-CODEX-SWARM-BATCH-02-LANE-04-PROMOTION-THRESHOLDS.md`

## Assessment Path

`communications/assessments/ASSESSMENT-CODEX-SWARM-BATCH-02-LANE-04-PROMOTION-THRESHOLDS.md`
