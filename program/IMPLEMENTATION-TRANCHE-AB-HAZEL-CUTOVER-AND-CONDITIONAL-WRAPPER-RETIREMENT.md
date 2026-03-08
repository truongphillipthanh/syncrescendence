# Implementation Tranche AB — Hazel Cutover And Conditional Wrapper Retirement

**Tranche**: AB  
**Intent bindings**: `INT-SHELL-001`, `INT-SHELL-003`, `INT-SHELL-005`

## Purpose

Resolve the final live blocker to constitutional wrapper retirement by cutting over the confirmed Hazel caller and preparing the repo-side retirement patch.

This tranche is the bridge between:

- Wave 6 external caller confirmation
- successful edge cutover
- later wrapper deletion and report cleanup

## Tasks

1. cut over the confirmed live Hazel rule from `/Users/system/syncrescendence/finalize_cowork_relay_job.py` to `/Users/system/syncrescendence/operators/cli-web-gap/finalize_cowork_relay_job.py`
2. remove unsupported `--project-ontology` from that live caller
3. capture repo-native evidence of the cutover result
4. prepare or execute the repo-side wrapper retirement patch only after cutover evidence is sufficient

## Promotion / Completion Criteria

- [WAVE-6-STRICT-READY-NAMING-AND-EDGE-AUDIT-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-6-STRICT-READY-NAMING-AND-EDGE-AUDIT-SYNTHESIS-v1.md) exists as the binding Wave 6 synthesis
- the Wave 7 swarm packets exist for Hazel cutover, retirement patch preparation, and residual naming mapping
- wrapper deletion is still conditional on successful cutover evidence rather than assumed

## Receipts

- [WAVE-6-STRICT-READY-NAMING-AND-EDGE-AUDIT-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-6-STRICT-READY-NAMING-AND-EDGE-AUDIT-SYNTHESIS-v1.md)
- [CODEX-SWARM-WAVE-7-HAZEL-CUTOVER-AND-RETIREMENT-PREP-v1.md](/Users/system/syncrescendence/orchestration/state/impl/CODEX-SWARM-WAVE-7-HAZEL-CUTOVER-AND-RETIREMENT-PREP-v1.md)
- [IMPLEMENTATION-BACKLOG.live.md](/Users/system/syncrescendence/program/IMPLEMENTATION-BACKLOG.live.md)
