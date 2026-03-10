# Response

**Response ID**: `RSP-20260310-codex-campaign-07-lane-02-office-harness-exocortex-projection-contract`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-10`
**Dispatch packet**: `communications/prompts/PACKET-CODEX-CAMPAIGN-07-LANE-02-OFFICE-HARNESS-EXOCORTEX-PROJECTION-CONTRACT.md`
**Result state**: `complete`
**Receipt artifacts**:
  - `orchestration/state/impl/OFFICE-HARNESS-EXOCORTEX-PROJECTION-CONTRACT-v1.md`

## Returned Content

Created the first lawful office-harness exocortex projection contract as:

- `orchestration/state/impl/OFFICE-HARNESS-EXOCORTEX-PROJECTION-CONTRACT-v1.md`

What it does:

- narrows the first projection family to the exocortex-facing runtime offices only
- binds the family to the existing repo-native proof chain behind `office-harness-bindings.effective.json`
- requires joins against the existing `EXOCORTEX-SURFACE-REGISTRY-CC90.json`, `EXOCORTEX-TELEOLOGY-REGISTRY-CC90.json`, and `EXOCORTEX-CONTROL-PLANE-STATUS-CC91.json`
- defines the required pointer fields that projected rows must carry from the source office-harness binding
- freezes derivative-only obligations so the emitted rows cannot become a hidden second control plane
- defines a deterministic rebuild path from repo-native proof state with no exocortex API dependency

The v1 family is intentionally narrow:

- scope is `surface_class: persistent-runtime`
- scope is `harness_family: openclaw`
- current lawful members are `ajna` and `psyche`
- v1 provider mapping is `anthropic -> claude_anthropic_surface` and `openai-codex -> chatgpt_openai_surface`

This gives lane 03 a precise target artifact family without widening office-harness state into an unratified topology.

## Verification

- ran `git diff --check`
- result: clean

## Status

`complete`
