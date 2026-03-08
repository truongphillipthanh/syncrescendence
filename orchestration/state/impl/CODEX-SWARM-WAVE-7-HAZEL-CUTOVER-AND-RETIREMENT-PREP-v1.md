# Codex Swarm — Wave 7 Hazel Cutover And Retirement Prep v1

**Date**: 2026-03-08  
**Status**: staged  
**Purpose**: cut over the confirmed live Hazel caller, prepare conditional wrapper retirement, and map the smaller remaining naming debt without widening enforcement

## 0. Why Wave 7 Exists

Wave 6 proved that the wrapper blocker is one concrete Hazel caller.

That means the next honest move is:

- cut over that caller
- record the result
- prepare repo-side retirement

not:

- widen naming strictness
- delete the wrapper speculatively

Primary anchors:

- [WAVE-6-STRICT-READY-NAMING-AND-EDGE-AUDIT-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-6-STRICT-READY-NAMING-AND-EDGE-AUDIT-SYNTHESIS-v1.md)
- [ROOT-WRAPPER-EDGE-AUDIT-v1.md](/Users/system/syncrescendence/orchestration/state/ROOT-WRAPPER-EDGE-AUDIT-v1.md)
- [TRANSITIONAL-ROOT-OPERATOR-INTERNALIZATION-PLAN-v1.md](/Users/system/syncrescendence/orchestration/state/TRANSITIONAL-ROOT-OPERATOR-INTERNALIZATION-PLAN-v1.md)
- [COMMUNICATIONS-NAMING-REPORT.md](/Users/system/syncrescendence/orchestration/state/COMMUNICATIONS-NAMING-REPORT.md)

## 1. Recommended Parallelism

Recommended:

- `2` core worker lanes
- `1` optional worker lane
- `1` coordinator lane

## 2. Wave 7 Swarm Law

All sessions must obey:

1. edit only the files explicitly assigned to your lane plus your response artifact
2. do not delete the wrapper in this wave unless concrete cutover evidence exists in your lane or a binding anchor produced by another landed lane
3. do not widen naming strictness or rename communications artifacts in this wave
4. keep the work bounded to Hazel cutover, retirement preparation, and residual naming mapping
5. run `git diff --check` before closing

## 3. Lane Set

### Lane 01 — Hazel Live Caller Cutover

Goal:

- cut over the confirmed live Hazel caller from the root wrapper path to the operator path and remove unsupported `--project-ontology`, then capture repo-native evidence of what changed

Recommended reasoning:

- `extra high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-7-LANE-01-HAZEL-LIVE-CALLER-CUTOVER.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-7-LANE-01-HAZEL-LIVE-CALLER-CUTOVER.md)

### Lane 02 — Wrapper Retirement Patch Preparation

Goal:

- prepare the exact repo-side retirement patch set so wrapper deletion can happen immediately once cutover evidence is sufficient

Recommended reasoning:

- `high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-7-LANE-02-WRAPPER-RETIREMENT-PATCH-PREP.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-7-LANE-02-WRAPPER-RETIREMENT-PATCH-PREP.md)

### Optional Lane 03 — Remaining Naming Debt Mapping

Goal:

- map the `7` remaining active communications findings into a later rename tranche versus permanent report-only legacy hold

Recommended reasoning:

- `medium`

Packet:

- [PACKET-CODEX-SWARM-WAVE-7-LANE-03-REMAINING-NAMING-DEBT-MAP.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-7-LANE-03-REMAINING-NAMING-DEBT-MAP.md)

### Lane 00 — Coordinator

Goal:

- synthesize the Hazel cutover evidence and retirement preparation, then decide whether the wrapper can be deleted in the following wave

Recommended reasoning:

- `high`

Packet:

- [PACKET-CODEX-SWARM-WAVE-7-LANE-00-COORDINATOR.md](/Users/system/syncrescendence/communications/prompts/PACKET-CODEX-SWARM-WAVE-7-LANE-00-COORDINATOR.md)

## 4. Launch Order

Recommended launch order:

1. Lane 01
2. Lane 02
3. optional Lane 03
4. Lane 00 last

## 5. Success Criteria

Wave 7 succeeds when:

- the confirmed live Hazel caller is either cut over cleanly or bounded with explicit technical evidence of why not
- the repo-side wrapper retirement patch set is ready
- the remaining naming debt is smaller and better mapped, without widening strictness
- the next wave can decide wrapper deletion from concrete cutover evidence instead of ambiguity
