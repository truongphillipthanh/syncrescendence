# Dispatch Packet

**Packet ID**: `PKT-20260308-codex-swarm-wave-7-lane-03-remaining-naming-debt-map`  
**Surface**: `codex_parallel_session`  
**Role**: `assessment`  
**Date**: `2026-03-08`  
**Objective**: map the `7` remaining active communications findings into a later rename tranche versus permanent report-only legacy hold  
**Priority**: `medium`  
**Target**: `post-wrapper naming remainder map`  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-7-LANE-03-REMAINING-NAMING-DEBT-MAP.md`

## Decision Envelope

- **Trigger**: Wave 6 reduced the communications naming surface to `7` active warnings
- **Selected approach**: map the remainder cleanly without acting on renames or strictness in the same wave
- **Alternatives considered**:
  - widening strictness now — rejected because the wrapper cutover remains the dominant live blocker
  - ignoring the remainder entirely — rejected because the smaller surface is now tractable enough to map precisely
- **Assumptions**:
  - the remainder consists of `4` rename-required and `3` acceptable legacy-debt items
- **Inherited constraints**:
  - do not rename files in this lane
  - do not alter validator logic in this lane

## Assigned Live Files

- [COMMUNICATIONS-NAMING-REMAINING-DEBT-v1.md](/Users/system/syncrescendence/orchestration/state/COMMUNICATIONS-NAMING-REMAINING-DEBT-v1.md)

## Anchors

- [COMMUNICATIONS-NAMING-REPORT.md](/Users/system/syncrescendence/orchestration/state/COMMUNICATIONS-NAMING-REPORT.md)
- [COMMUNICATIONS-NAMING-TRIAGE-v1.md](/Users/system/syncrescendence/orchestration/state/COMMUNICATIONS-NAMING-TRIAGE-v1.md)

## Required Output

1. map each of the `7` remaining warnings to:
   - later rename tranche
   - permanent report-only legacy hold
2. identify any future reference-update risk for the rename-required group
3. keep the output bounded to planning, not execution
4. write a short response artifact summarizing the map
5. run `git diff --check`
6. report `complete / partial / blocked`
