# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-wave-3-lane-04-boot-executive-macro-cleanup`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-06`
**Objective**: patch `BOOT.md` and `executive/README.md` so stateless rehydration front doors name the macro doctrine and successor-shell role cleanly
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-3-LANE-04-BOOT-EXECUTIVE-MACRO-CLEANUP.md`

## Decision Envelope

- **Trigger**: these front doors are secondary drift surfaces that become worth fixing once the main root and lane readmes are already being patched
- **Selected approach**: directly patch only the two entry surfaces named below
- **Alternatives considered**:
  - leaving them stale until a later orientation pass — acceptable, but lower quality for stateless rehydration
- **Assumptions**:
  - the macro doctrine anchor is already authoritative
- **Inherited constraints**:
  - edit only the assigned files plus your response artifact
  - if you do not have a clean faux-worktree or this lane is not dispatched, the wave may still complete without it

## Assigned Live Files

- [BOOT.md](/Users/system/syncrescendence/BOOT.md)
- [executive/README.md](/Users/system/syncrescendence/executive/README.md)

## Anchors

- [SYNCRESCENDENCE-HOLISTIC-STRATEGIC-ENDEAVOR-v1.md](/Users/system/syncrescendence/knowledge/canon/SYNCRESCENDENCE-HOLISTIC-STRATEGIC-ENDEAVOR-v1.md)
- [WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-07-MACRO-DRIFT-SCAN.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-07-MACRO-DRIFT-SCAN.md)

## Required Output

1. patch the two assigned files directly
2. teach the macro doctrine anchor at session entry
3. remove stale `sandbox shell` wording from `executive/README.md`
4. preserve the concise boot posture while improving anti-drift value
5. write a short response artifact listing changed files and validation run
6. run `git diff --check`
7. report `complete / partial / blocked`
