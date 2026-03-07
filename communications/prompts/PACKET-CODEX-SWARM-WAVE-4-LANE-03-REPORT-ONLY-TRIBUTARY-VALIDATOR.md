# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-wave-4-lane-03-report-only-tributary-validator`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-06`
**Objective**: materialize a thin report-only validator for the tributary control plane and its custody joins without turning it into an adjudication engine
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-4-LANE-03-REPORT-ONLY-TRIBUTARY-VALIDATOR.md`

## Decision Envelope

- **Trigger**: the next wave is the earliest point where the registry, ledger, manifests, and receipts may all exist together as live control-plane artifacts
- **Selected approach**: add one report-only validator that checks structural legality and joins, not semantic wisdom
- **Alternatives considered**:
  - hard-fail validation now — rejected because `verified` state and `dest_artifact_hash` are still future work
  - leaving validation entirely prose-only — rejected because the control plane now has enough structure to support a thin automated check
- **Assumptions**:
  - the validator should live under `operators/validators/`
- **Inherited constraints**:
  - edit only the assigned files plus your response artifact
  - do not mutate live registry or ledger state in this lane
  - keep the validator report-only and deterministic

## Assigned Live Files

- [operators/validators/validate_tributary_disposition.py](/Users/system/syncrescendence/operators/validators/validate_tributary_disposition.py)
- [operators/README.md](/Users/system/syncrescendence/operators/README.md)

## Anchors

- [WAVE-3-DIRECT-WRITE-COMPATIBILITY-AND-CUSTODY-EXECUTION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-3-DIRECT-WRITE-COMPATIBILITY-AND-CUSTODY-EXECUTION-SYNTHESIS-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-06-VALIDATOR-NORMALIZATION.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-06-VALIDATOR-NORMALIZATION.md)
- [tributary-disposition-schema-v1.md](/Users/system/syncrescendence/orchestration/state/registry/tributary-disposition-schema-v1.md)
- [PEDIGREE-CUSTODY-LAW-v1.md](/Users/system/syncrescendence/pedigree/PEDIGREE-CUSTODY-LAW-v1.md)

## Required Output

1. create a deterministic report-only validator script
2. validate:
   - CSV header exactness
   - enum legality
   - `source_relpath_hash` serialization
   - required path fields by disposition/state
   - manifest and receipt path existence
   - latest ledger parity with CSV current state
3. keep the validator non-mutating and non-blocking
4. add a short entry to `operators/README.md`
5. write a short response artifact listing created files and validation run
6. run `git diff --check`
7. report `complete / partial / blocked`
