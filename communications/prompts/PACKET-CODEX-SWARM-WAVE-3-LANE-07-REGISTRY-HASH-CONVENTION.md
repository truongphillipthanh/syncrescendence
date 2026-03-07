# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-wave-3-lane-07-registry-hash-convention`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-06`
**Objective**: ratify the exact `source_relpath_hash` serialization in the schema and state the remaining gate before live registry population
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-3-LANE-07-REGISTRY-HASH-CONVENTION.md`

## Decision Envelope

- **Trigger**: Wave 2 Lane 03 proposed an exact hash serialization, but the live schema still describes it only generically
- **Selected approach**: patch the schema doc narrowly so later registry population does not rest on implicit local convention
- **Alternatives considered**:
  - leaving the convention implicit until row insertion — rejected because later workers would have to guess at a normative delimiter
- **Assumptions**:
  - no enum, state-transition, or CSV-header changes are needed
- **Inherited constraints**:
  - edit only the assigned file plus your response artifact
  - do not insert live rows into the registry CSV
  - do not write ledger events

## Assigned Live Files

- [orchestration/state/registry/tributary-disposition-schema-v1.md](/Users/system/syncrescendence/orchestration/state/registry/tributary-disposition-schema-v1.md)

## Anchors

- [WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-03-REGISTRY-SEED-NORMALIZATION.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-06-VALIDATOR-NORMALIZATION.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-06-VALIDATOR-NORMALIZATION.md)

## Required Output

1. patch the schema so `source_relpath_hash` has one exact serialization rule
2. preserve all existing enums, header order, and transition rules
3. add only the narrow explanatory text needed to support later live row insertion
4. write a short response artifact listing the schema change and validation run
5. run `git diff --check`
6. report `complete / partial / blocked`
