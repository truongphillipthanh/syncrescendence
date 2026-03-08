# Dispatch Packet

**Packet ID**: `PKT-20260308-codex-swarm-wave-7-lane-01-hazel-live-caller-cutover`  
**Surface**: `codex_parallel_session`  
**Role**: `direct_write`  
**Date**: `2026-03-08`  
**Objective**: cut over the confirmed live Hazel caller from the root wrapper path to the operator path and remove unsupported `--project-ontology`, then capture repo-native evidence of what changed  
**Priority**: `highest`  
**Target**: `the confirmed live Hazel blocker`  
**Origin lane**: `communications/prompts`  
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-7-LANE-01-HAZEL-LIVE-CALLER-CUTOVER.md`

## Decision Envelope

- **Trigger**: Wave 6 confirmed one live Hazel rule still invokes `/Users/system/syncrescendence/finalize_cowork_relay_job.py --project-ontology`
- **Selected approach**: perform the smallest safe cutover on the confirmed live caller, then record the exact before/after state in a repo-native receipt
- **Alternatives considered**:
  - deleting the wrapper before cutover — rejected because the caller is confirmed live
  - leaving the caller untouched and continuing to tolerate the warning — rejected because the blocker is now concrete and narrow
- **Assumptions**:
  - the live rule storage can be safely edited once the exact command location is confirmed
- **Inherited constraints**:
  - do not delete the wrapper in this lane
  - do not guess at unsupported Hazel storage formats; if safe mutation cannot be proven, stop and report `blocked`
  - do not widen edits beyond the confirmed caller surface

## Assigned Live Files

- [16777231-58660320.hazelrules](/Users/system/Library/Application%20Support/Hazel/16777231-58660320.hazelrules)
- [16777231-58660320.hazellocalrulesdb](/Users/system/Library/Application%20Support/Hazel/16777231-58660320.hazellocalrulesdb)
- [16777231-58660320.hazeldb](/Users/system/Library/Application%20Support/Hazel/16777231-58660320.hazeldb)
- [com.noodlesoft.Hazel.plist](/Users/system/Library/Preferences/com.noodlesoft.Hazel.plist)
- [HAZEL-LIVE-CALLER-CUTOVER-RECEIPT-v1.md](/Users/system/syncrescendence/orchestration/state/HAZEL-LIVE-CALLER-CUTOVER-RECEIPT-v1.md)

## Anchors

- [ROOT-WRAPPER-EDGE-AUDIT-v1.md](/Users/system/syncrescendence/orchestration/state/ROOT-WRAPPER-EDGE-AUDIT-v1.md)
- [TRANSITIONAL-ROOT-OPERATOR-INTERNALIZATION-PLAN-v1.md](/Users/system/syncrescendence/orchestration/state/TRANSITIONAL-ROOT-OPERATOR-INTERNALIZATION-PLAN-v1.md)
- [finalize_cowork_relay_job.py](/Users/system/syncrescendence/finalize_cowork_relay_job.py)
- [operators/cli-web-gap/finalize_cowork_relay_job.py](/Users/system/syncrescendence/operators/cli-web-gap/finalize_cowork_relay_job.py)

## Required Output

1. confirm the exact active caller string in Hazel storage
2. if safe, repoint the caller from:
   - `/Users/system/syncrescendence/finalize_cowork_relay_job.py`
   to:
   - `/Users/system/syncrescendence/operators/cli-web-gap/finalize_cowork_relay_job.py`
3. remove unsupported `--project-ontology` from the same live caller
4. record the exact before/after command and evidence paths in the repo-native receipt
5. if cutover cannot be safely applied, leave external files untouched and report the exact blocker
6. write a short response artifact summarizing whether cutover landed or blocked
7. run `git diff --check`
8. report `complete / partial / blocked`
