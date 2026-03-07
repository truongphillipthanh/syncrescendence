# Dispatch Packet

**Packet ID**: `PKT-20260306-codex-swarm-wave-3-lane-01-knowledge-compatibility-direct-write`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-06`
**Objective**: directly patch the knowledge front doors so the repo stops teaching bare `knowledge/references/` as the sovereign secondary lane
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-SWARM-WAVE-3-LANE-01-KNOWLEDGE-COMPATIBILITY-DIRECT-WRITE.md`

## Decision Envelope

- **Trigger**: Wave 2 converged on an exact knowledge compatibility patch set that is ready for live application
- **Selected approach**: directly edit only the three knowledge-facing readmes assigned below
- **Alternatives considered**:
  - waiting until registry population — rejected because live-facing docs still teach the wrong ontology now
- **Assumptions**:
  - Sigma ratification from Wave 1 remains binding
  - Wave 2 Lane 01 and Lane 07 wording are both available as source material
- **Inherited constraints**:
  - edit only the assigned files plus your response artifact
  - do not touch `README.md`; that belongs to Lane 02
  - do not touch communications or constitutional files; they belong to other lanes

## Assigned Live Files

- [knowledge/README.md](/Users/system/syncrescendence/knowledge/README.md)
- [knowledge/feedstock/README.md](/Users/system/syncrescendence/knowledge/feedstock/README.md)
- [knowledge/references/README.md](/Users/system/syncrescendence/knowledge/references/README.md)

## Anchors

- [WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/WAVE-2-COMPATIBILITY-AND-SEED-NORMALIZATION-SYNTHESIS-v1.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-01-KNOWLEDGE-COMPATIBILITY.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-01-KNOWLEDGE-COMPATIBILITY.md)
- [RESPONSE-CODEX-SWARM-WAVE-2-LANE-07-MACRO-DRIFT-SCAN.md](/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-SWARM-WAVE-2-LANE-07-MACRO-DRIFT-SCAN.md)

## Required Output

1. patch the three assigned readmes directly
2. teach `knowledge/sigma/` as the live secondary doctrine tier
3. describe `knowledge/references/` as compatibility housing for `knowledge/sigma/references/`
4. route feedstock compaction toward `knowledge/sigma/references/` and `knowledge/sigma/`
5. write a short response artifact listing changed files, key wording decisions, and validation run
6. run `git diff --check`
7. report `complete / partial / blocked`
