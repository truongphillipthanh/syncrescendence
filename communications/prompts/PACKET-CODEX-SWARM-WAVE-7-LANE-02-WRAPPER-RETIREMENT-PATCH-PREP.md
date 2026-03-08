# Dispatch Packet

**Packet ID**: `PKT-20260308-codex-swarm-wave-7-lane-02-wrapper-retirement-patch-prep`  
**Surface**: `codex_parallel_session`  
**Role**: `assessment`  
**Date**: `2026-03-08`  
**Objective**: prepare the exact repo-side retirement patch set so wrapper deletion can happen immediately once cutover evidence is sufficient  
**Priority**: `high`  
**Target**: `post-cutover wrapper retirement readiness`  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-7-LANE-02-WRAPPER-RETIREMENT-PATCH-PREP.md`

## Decision Envelope

- **Trigger**: Wave 6 proved the wrapper is blocked by one live Hazel caller, not by repo ambiguity
- **Selected approach**: derive the exact repo-side deletion and cleanup set now so the shell can retire the wrapper quickly once the cutover is real
- **Alternatives considered**:
  - deleting the wrapper now — rejected because cutover evidence does not yet exist
  - waiting to think about repo cleanup until after cutover — rejected because the patch set is already derivable from current repo state
- **Assumptions**:
  - repo-side retirement still consists primarily of wrapper deletion, validator allowlist removal, inventory allowlist removal, and report refresh
- **Inherited constraints**:
  - do not delete the wrapper in this lane
  - keep the output patch-oriented and exact

## Assigned Live Files

- [ROOT-WRAPPER-RETIREMENT-PATCHSET-v1.md](/Users/system/syncrescendence/orchestration/state/ROOT-WRAPPER-RETIREMENT-PATCHSET-v1.md)

## Anchors

- [TRANSITIONAL-ROOT-OPERATOR-INTERNALIZATION-PLAN-v1.md](/Users/system/syncrescendence/orchestration/state/TRANSITIONAL-ROOT-OPERATOR-INTERNALIZATION-PLAN-v1.md)
- [ROOT-WRAPPER-EDGE-AUDIT-v1.md](/Users/system/syncrescendence/orchestration/state/ROOT-WRAPPER-EDGE-AUDIT-v1.md)
- [validate_constitution.py](/Users/system/syncrescendence/operators/validators/validate_constitution.py)
- [artifact_law_inventory.py](/Users/system/syncrescendence/operators/validators/artifact_law_inventory.py)

## Required Output

1. enumerate the exact repo-side file changes needed after successful Hazel cutover
2. separate:
   - required runtime or validator cleanup
   - report regeneration steps
   - documentation-only follow-on cleanup
3. make clear which items are safe immediately after cutover and which can wait
4. write a short response artifact summarizing the prepared patch set
5. run `git diff --check`
6. report `complete / partial / blocked`
