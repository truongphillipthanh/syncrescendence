# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-wave-3-lane-02-root-readme-macro-cleanup`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-06`
**Objective**: patch the root README so it names Sigma correctly, includes dispatches, and exposes the macro doctrine anchor
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-3-LANE-02-ROOT-README-MACRO-CLEANUP.md`

## Decision Envelope

- **Trigger**: the root README remains one of the highest-yield macro drift surfaces in the repo
- **Selected approach**: edit only the root README and merge the Sigma, dispatch, and macro-anchor corrections into one coherent front-door patch
- **Alternatives considered**:
  - leaving root orientation stale while patching only local lane readmes — rejected because stateless rehydration enters here
- **Assumptions**:
  - the macro doctrine artifact is already authoritative
- **Inherited constraints**:
  - edit only `README.md` plus your response artifact
  - do not touch `BOOT.md` or `executive/README.md`; those belong to Lane 04

## Assigned Live Files

- [README.md](/Users/system/syncrescendence/README.md)

## Anchors

- [SYNCRESCENDENCE-HOLISTIC-STRATEGIC-ENDEAVOR-v1.md](/Users/system/syncrescendence/knowledge/canon/SYNCRESCENDENCE-HOLISTIC-STRATEGIC-ENDEAVOR-v1.md)
- [WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-01-KNOWLEDGE-COMPATIBILITY.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-01-KNOWLEDGE-COMPATIBILITY.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-02-COMMS-DISPATCH-CLEANUP.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-02-COMMS-DISPATCH-CLEANUP.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-07-MACRO-DRIFT-SCAN.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-07-MACRO-DRIFT-SCAN.md)

## Required Output

1. patch `README.md` directly
2. add the macro doctrine anchor explicitly
3. teach `communications/` with dispatches and retros
4. teach `knowledge/` with Sigma and compatibility-housed references
5. preserve the root README's existing shell-identity tone while removing stale lane semantics
6. write a short response artifact listing the final changed sections and validation run
7. run `git diff --check`
8. report `complete / partial / blocked`
