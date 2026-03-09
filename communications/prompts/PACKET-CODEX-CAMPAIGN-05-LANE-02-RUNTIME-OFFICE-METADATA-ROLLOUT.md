# Dispatch Packet

**Packet ID**: `PKT-20260309-codex-campaign-05-lane-02-runtime-office-metadata-rollout`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-09`
**Objective**: add the next high-burden office-harness metadata specimens for `ajna` and `psyche`
**Priority**: `highest`
**Target**: `the runtime-heavy office tier`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-05-LANE-02-RUNTIME-OFFICE-METADATA-ROLLOUT.md`

## Required Output

1. create `offices/ajna/platform/contracts/OFFICE-HARNESS-METADATA.v1.yaml`
2. create `offices/psyche/platform/contracts/OFFICE-HARNESS-METADATA.v1.yaml`
3. keep fields lawful, typed, and free of secrets or speculative runtime claims
4. bind each specimen to the office-harness contract rather than to response artifacts
5. run `git diff --check`
6. report `complete / partial / blocked`
