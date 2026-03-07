# Response

**Response ID**: `RSP-20260306-codex-swarm-wave-3-lane-07-registry-hash-convention`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-06`
**Dispatch packet**: `PKT-20260306-codex-swarm-wave-3-lane-07-registry-hash-convention`
**Result state**: `complete`

## Schema Change

Patched `orchestration/state/registry/tributary-disposition-schema-v1.md` so `source_relpath_hash` now has one exact serialization rule:

- `source_relpath_hash = "sha256:" + lowercase_hex(sha256(UTF-8("<source_tributary>|<source_path>")))`
- `|` is the required delimiter.
- `source_tributary` and `source_path` are hashed exactly as stored in the CSV row, with no extra whitespace and no additional path rewriting.

No enum set, CSV header order, or state-transition rule changed.

## Remaining Gate

Live registry population should still wait until the custody artifacts are real and joinable, so row insertion does not point at hypothetical manifests or receipts.

## Validation Run

- Ran `git diff --check`

## Status

`complete`
