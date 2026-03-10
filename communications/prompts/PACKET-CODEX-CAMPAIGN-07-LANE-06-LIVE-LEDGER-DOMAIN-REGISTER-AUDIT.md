# Dispatch Packet

**Packet ID**: `PKT-20260310-codex-campaign-07-lane-06-live-ledger-domain-register-audit`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-10`
**Objective**: make the family-of-families control surface less likely to go stale again
**Priority**: `high`
**Target**: `a narrow audit or validator around live-ledger-domain-register coherence`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-06-LIVE-LEDGER-DOMAIN-REGISTER-AUDIT.md`

## Required Output

1. create a narrow audit or validator for `live-ledger-domain-register.csv` coherence against landed family artifacts
2. keep the first pass report-first
3. focus on phase drift, missing append-only surfaces, and mismatched family-state claims
4. run `git diff --check`
5. report `complete / partial / blocked`
