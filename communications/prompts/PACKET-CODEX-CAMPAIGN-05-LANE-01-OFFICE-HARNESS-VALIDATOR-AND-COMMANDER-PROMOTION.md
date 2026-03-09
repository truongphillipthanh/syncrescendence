# Dispatch Packet

**Packet ID**: `PKT-20260309-codex-campaign-05-lane-01-office-harness-validator-and-commander-promotion`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-09`
**Objective**: create the office-harness coherence validator and promote `commander` into the first validated operative specimen
**Priority**: `highest`
**Target**: `the first executable office-harness coherence system`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-05-LANE-01-OFFICE-HARNESS-VALIDATOR-AND-COMMANDER-PROMOTION.md`

## Required Output

1. create `operators/validators/validate_office_harness_coherence.py`
2. ensure `offices/commander/platform/contracts/OFFICE-HARNESS-METADATA.v1.yaml` is treated as operative and validator-backed rather than merely reference
3. keep the validator report-first
4. run `git diff --check`
5. report `complete / partial / blocked`
