# Dispatch Packet

**Packet ID**: `PKT-20260310-codex-campaign-08-lane-01-family-register-phase-advancement`  
**Surface**: `codex_parallel_session`  
**Role**: `direct_write`  
**Date**: `2026-03-10`  
**Objective**: reconcile the family register and its ledger with the corrected Campaign 07 frontier  
**Priority**: `extra_high`  
**Target**: `live-ledger family phase truth`  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-08-LANE-01-FAMILY-REGISTER-PHASE-ADVANCEMENT.md`

## Required Output

1. update `orchestration/state/registry/live-ledger-domain-register.csv` and its ledger only where gate law now clearly justifies advancement
2. preserve conservative phase discipline where widening law is not yet landed
3. bind every advancement to the strongest available receipts and validators
4. rerun the live-ledger domain register auditor
5. run `git diff --check`
6. report `complete / partial / blocked`
