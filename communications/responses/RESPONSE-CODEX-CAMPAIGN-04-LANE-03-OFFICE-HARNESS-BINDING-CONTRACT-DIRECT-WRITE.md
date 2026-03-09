# Response

**Response ID**: `RSP-20260309-codex-campaign-04-lane-03-office-harness-binding-contract-direct-write`
**Surface**: `codex_parallel_session`
**Date**: `2026-03-09`
**Date received**: `2026-03-09`
**Dispatch packet**: `communications/prompts/PACKET-CODEX-CAMPAIGN-04-LANE-03-OFFICE-HARNESS-BINDING-CONTRACT-DIRECT-WRITE.md`
**Result state**: `complete`
**Receipt artifacts**:
  - `orchestration/state/impl/OFFICE-HARNESS-BINDING-CONTRACT-v1.md`
  - `communications/responses/RESPONSE-CODEX-CAMPAIGN-04-LANE-03-OFFICE-HARNESS-BINDING-CONTRACT-DIRECT-WRITE.md`

## Returned Content

Created:

- `orchestration/state/impl/OFFICE-HARNESS-BINDING-CONTRACT-v1.md`

The landed law defines:

- stable office identity as repo law keyed by office id, path, and federal burden
- mutable harness binding as repo-resident current-state metadata
- precedence from `AGENTS.md` through contract, per-office metadata, derived registries, validators, and downstream projections
- rebinding as metadata change plus derived-surface refresh without office renaming
- ratification-pointer obligations for any authority-bearing binding row, event, or projection
- compatibility with the governing split: repo ratifies, exocortex coordinates, ontology projects

The file stays focused on law. Validator language is limited to minimum obligations for drift reporting and precedence enforcement.

## `git diff --check`

`git diff --check` ran clean.

## Status

`complete`
