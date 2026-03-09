# Dispatch Packet

**Packet ID**: `PKT-20260309-codex-campaign-05-lane-04-office-harness-registry-and-reports`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-09`
**Objective**: render the effective office-harness registry and first coherence reports
**Priority**: `high`
**Target**: `subordinate read-model and report surfaces for office-harness state`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-05-LANE-04-OFFICE-HARNESS-REGISTRY-AND-REPORTS.md`

## Required Output

1. create `orchestration/state/registry/office-harness-bindings.effective.json`
2. create `orchestration/state/OFFICE-HARNESS-COHERENCE-REPORT.json`
3. create `orchestration/state/OFFICE-HARNESS-COHERENCE-REPORT.md`
4. keep these surfaces explicitly subordinate to repo law and metadata
5. run `git diff --check`
6. report `complete / partial / blocked`
