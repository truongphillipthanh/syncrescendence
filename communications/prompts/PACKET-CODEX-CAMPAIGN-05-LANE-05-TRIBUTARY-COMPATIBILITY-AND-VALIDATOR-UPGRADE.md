# Dispatch Packet

**Packet ID**: `PKT-20260309-codex-campaign-05-lane-05-tributary-compatibility-and-validator-upgrade`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-09`
**Objective**: operationalize the ratification-pointer transition on the live tributary proof family without breaking the proof
**Priority**: `highest`
**Target**: `tributary compatibility receipt and validator upgrade`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-05-LANE-05-TRIBUTARY-COMPATIBILITY-AND-VALIDATOR-UPGRADE.md`

## Required Output

1. create the first compatibility receipt keyed by `candidate_id` for the current authority-bearing tributary rows
2. update `operators/validators/validate_tributary_disposition.py` to distinguish `authority_bound` from `informative_only` without changing the live CSV header
3. preserve the existing live proof baseline
4. run `git diff --check`
5. report `complete / partial / blocked`
