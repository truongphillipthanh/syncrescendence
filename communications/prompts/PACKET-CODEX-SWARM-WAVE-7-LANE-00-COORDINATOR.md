# Dispatch Packet

**Packet ID**: `PKT-20260308-codex-swarm-wave-7-lane-00-coordinator`  
**Surface**: `codex_parallel_session`  
**Role**: `synthesis`  
**Date**: `2026-03-08`  
**Objective**: synthesize the Hazel cutover evidence and retirement preparation, then decide whether the wrapper can be deleted in the following wave  
**Priority**: `high`  
**Target**: `post-wave-7 wrapper-retirement frontier`  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-7-LANE-00-COORDINATOR.md`

## Decision Envelope

- **Trigger**: Wave 6 reduced the blocker to one concrete Hazel caller and one bounded repo-side retirement patch
- **Selected approach**: synthesize only after the worker evidence lands and keep deletion conditional on real cutover evidence
- **Alternatives considered**:
  - assuming retirement is now safe — rejected because the live cutover has not yet been proven
  - reopening broader naming or migration questions — rejected because they are not the live frontier
- **Assumptions**:
  - Lane 01 determines the live caller state
  - Lane 02 determines whether repo-side retirement can proceed immediately after successful cutover
- **Inherited constraints**:
  - do not edit repo state in this lane
  - stage the next wave only from what materially landed

## Anchors

- [WAVE-6-STRICT-READY-NAMING-AND-EDGE-AUDIT-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-6-STRICT-READY-NAMING-AND-EDGE-AUDIT-SYNTHESIS-v1.md)
- [CODEX-SWARM-WAVE-7-HAZEL-CUTOVER-AND-RETIREMENT-PREP-v1.md](/Users/system/syncrescendence/orchestration/state/impl/CODEX-SWARM-WAVE-7-HAZEL-CUTOVER-AND-RETIREMENT-PREP-v1.md)
- all landed Wave 7 worker response artifacts

## Required Output

1. assess whether Hazel cutover landed, blocked, or remains ambiguous
2. assess whether repo-side wrapper retirement is ready
3. assess whether the remaining naming debt map changes any immediate enforcement decision
4. state what is:
   - complete
   - partial
   - blocked
5. stage the next wave only if the landed evidence justifies it
