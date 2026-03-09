# Dispatch Packet

**Packet ID**: `PKT-20260309-codex-campaign-05-lane-03-remaining-office-metadata-rollout`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-09`
**Objective**: add the next office-harness metadata specimens for `adjudicator` and `cartographer`
**Priority**: `high`
**Target**: `the lighter federal office tier`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-05-LANE-03-REMAINING-OFFICE-METADATA-ROLLOUT.md`

## Required Output

1. create `offices/adjudicator/platform/contracts/OFFICE-HARNESS-METADATA.v1.yaml`
2. create `offices/cartographer/platform/contracts/OFFICE-HARNESS-METADATA.v1.yaml`
3. keep all bindings compatible with `AGENTS.md` and the office-harness contract
4. run `git diff --check`
5. report `complete / partial / blocked`
