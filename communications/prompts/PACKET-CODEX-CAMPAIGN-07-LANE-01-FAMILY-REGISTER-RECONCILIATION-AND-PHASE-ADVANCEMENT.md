# Dispatch Packet

**Packet ID**: `PKT-20260310-codex-campaign-07-lane-01-family-register-reconciliation-and-phase-advancement`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-10`
**Objective**: reconcile the family register and its ledger with the newly true office-harness proof state
**Priority**: `highest`
**Target**: `accurate family-of-families phase state`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-01-FAMILY-REGISTER-RECONCILIATION-AND-PHASE-ADVANCEMENT.md`

## Required Output

1. update `orchestration/state/registry/live-ledger-domain-register.csv`
2. append the corresponding event(s) to `orchestration/state/registry/live-ledger-domain-register-ledger.jsonl`
3. promote `office_harness_state` to the lawful phase justified by current landed proof
4. keep `config_surface_state` conservative unless its proof uplift is landed in the same campaign
5. run `git diff --check`
6. report `complete / partial / blocked`
