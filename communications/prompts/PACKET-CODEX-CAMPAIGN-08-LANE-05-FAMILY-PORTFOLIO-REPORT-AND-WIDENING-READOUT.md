# Dispatch Packet

**Packet ID**: `PKT-20260310-codex-campaign-08-lane-05-family-portfolio-report-and-widening-readout`  
**Surface**: `codex_parallel_session`  
**Role**: `direct_write`  
**Date**: `2026-03-10`  
**Objective**: create one portfolio-level report over family maturity and widening readiness  
**Priority**: `high`  
**Target**: `family portfolio truth surface`  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-08-LANE-05-FAMILY-PORTFOLIO-REPORT-AND-WIDENING-READOUT.md`

## Required Output

1. create one derivative report over the current live family portfolio
2. distinguish seed, proof, default-ready, and projection-open states without outranking the family register
3. surface the current widening posture and blockers for each active family
4. keep the report derived from ratified family surfaces and validators
5. run `git diff --check`
6. report `complete / partial / blocked`
