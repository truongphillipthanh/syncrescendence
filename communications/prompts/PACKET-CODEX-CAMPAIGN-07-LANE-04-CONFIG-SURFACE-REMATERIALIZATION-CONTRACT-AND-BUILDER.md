# Dispatch Packet

**Packet ID**: `PKT-20260310-codex-campaign-07-lane-04-config-surface-rematerialization-contract-and-builder`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-10`
**Objective**: lift `config_surface_state` from receipt-seeded state toward true proof-family status
**Priority**: `extra high`
**Target**: `config-surface rematerialization law and builder`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-04-CONFIG-SURFACE-REMATERIALIZATION-CONTRACT-AND-BUILDER.md`

## Required Output

1. create rematerialization law for `config_surface_state`
2. add a builder or equivalent deterministic rematerializer that can rebuild current state from append-only history if now justified
3. update validation or receipt surfaces only as needed to support that uplift
4. run `git diff --check`
5. report `complete / partial / blocked`
