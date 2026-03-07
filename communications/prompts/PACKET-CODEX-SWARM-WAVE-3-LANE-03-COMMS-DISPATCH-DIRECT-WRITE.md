# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-wave-3-lane-03-comms-dispatch-direct-write`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-06`
**Objective**: patch the communications front doors and constitutional summaries so dispatches and communications lineage are taught correctly
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-3-LANE-03-COMMS-DISPATCH-DIRECT-WRITE.md`

## Decision Envelope

- **Trigger**: Wave 1 physicalized `communications/dispatches/`, but live-facing docs still omit or underdescribe that lane
- **Selected approach**: directly patch the lane README, constitutional summary, and work-loop metabolic rule in one bounded pass
- **Alternatives considered**:
  - leaving dispatches implicit in law only — rejected because new sessions still learn the wrong filing topology
- **Assumptions**:
  - `COMMUNICATIONS-LAW-v1.md` already carries the correct lane semantics
- **Inherited constraints**:
  - edit only the assigned files plus your response artifact
  - do not touch `README.md`; that belongs to Lane 02

## Assigned Live Files

- [communications/README.md](/Users/system/syncrescendence/communications/README.md)
- [AGENTS.md](/Users/system/syncrescendence/AGENTS.md)
- [WORK-LOOP.md](/Users/system/syncrescendence/WORK-LOOP.md)

## Anchors

- [WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md)
- [COMMUNICATIONS-LAW-v1.md](/Users/system/syncrescendence/orchestration/state/impl/COMMUNICATIONS-LAW-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-02-COMMS-DISPATCH-CLEANUP.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-02-COMMS-DISPATCH-CLEANUP.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-07-MACRO-DRIFT-SCAN.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-07-MACRO-DRIFT-SCAN.md)

## Required Output

1. patch the three assigned files directly
2. add `dispatches` to live-facing lane summaries and sub-lane lists
3. replace stale `neosyncrescendence`, `future-lane`, or incomplete communications framing
4. update the work-loop metabolic rule so dispatches are explicit communications lineage
5. keep the constitutional summary compact and consistent with current law
6. write a short response artifact listing changed files, wording decisions, and validation run
7. run `git diff --check`
8. report `complete / partial / blocked`
