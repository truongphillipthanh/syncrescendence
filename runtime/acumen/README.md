# Acumen Runtime Lane

Runtime lane for Acumen Intelligence Pipeline generated artifacts and operator outputs.

## Current Scope

This lane stores files produced by the repo-native Acumen flow that actually exists today.

1. registry generation and validation
2. YouTube poll cursor state and poll-candidate output
3. identity probe status
4. triage packet artifacts and prompt previews
5. deterministic transcript artifacts
6. Dawn Brief compilation from an existing JSONL queue
7. sequential status snapshots

This lane carries three different truth classes that should not be merged:

1. code presence:
   - live YouTube polling exists in repo
   - live Gemini triage exists in repo
   - append-only evidence ledgers and rematerialization exist in repo
2. fixture-safe proof:
   - the committed repeatable path on disk is fixture polling plus heuristic triage
   - current local status files show that local path succeeding
3. live external proof:
   - absent here unless a committed run captures successful live YouTube and Gemini status artifacts

## Environment Variables

1. `make acumen-sample-run` does not require `ACUMEN_YOUTUBE_API_KEY` or `GEMINI_API_KEY` because it runs fixture polling and heuristic triage.
2. `ACUMEN_YOUTUBE_API_KEY` is required by `operators/acumen/poll_youtube_registry.py` unless `--api-key-env` points at a different env var.
3. `GEMINI_API_KEY` is consumed only by the Gemini triage adapter or batch runner when live Gemini surfaces are used.
4. Strict identity checks still rely on local `gcloud` state and the macOS keychain entry `syncrescendence/gcloud-account`, not on repo env vars.
5. Model credentials must stay external and may not be copied into Acumen evidence surfaces.

## Expected Local Artifacts

1. `registry.json`
2. `poll_cursor.json`
3. `poll-candidates.jsonl` for live poll batches
4. `intake/youtube/*.json` for Acumen-owned YouTube bridge handoffs
5. `intake/triage-packets/*.json` when a handoff includes enough metadata to build a triage packet
6. `intake/triage-prompts/*.md` for optional prompt previews
7. `out/triage-packet.sample.json` and `out/triage-prompt.sample.md` or equivalent packet outputs
8. `out/triage-decision*.json` for single-packet Gemini runs
9. `out/deterministic-*.md` and optional `out/*.debug.json`
10. `out/DAWN-BRIEF-*.md`
11. `out/poll-latest.jsonl` for the repeatable fixture-safe sequential run
12. `poll-status.json` and `triage-status.json` for the repeatable local proof path
13. sample or real decision queues such as `triage-decisions.sample.jsonl`
14. runtime current-state evidence surfaces:
   - `triage-decisions.jsonl`
   - `training-corpus.jsonl`
15. verification bridge artifacts:
   - `out/verification-dossiers/*.json`
16. status files under `/Users/system/syncrescendence/orchestration/state/`:
   - `ACUMEN-IDENTITY-STATUS.json`
   - `ACUMEN-PIPELINE-STATUS.json`
   - `ACUMEN-YOUTUBE-POLL-STATUS.json` when the live poller is used directly
   - `ACUMEN-AUGUR-VERIFICATION-BRIDGE.json`
17. sample fixtures:
   - `sample-video.json`
   - `sample-transcript.txt`
   - `triage-decisions.sample.jsonl`
   - `poll-fixture.sample.json`

## Repo-Sovereign Evidence

Append-only evidence for the runtime files lives at:

1. `orchestration/state/registry/acumen-triage-decision-ledger.jsonl`
2. `orchestration/state/registry/acumen-training-corpus-ledger.jsonl`

Those ledgers are the witness surfaces.
`runtime/acumen/triage-decisions.jsonl` and `runtime/acumen/training-corpus.jsonl` are derivative current-state views only.
`runtime/acumen/out/verification-dossiers/*.json` are sanitized downstream handoff artifacts generated from those witness surfaces.

Current repo-local witness examples on disk:

1. [acumen-triage-decision-ledger.jsonl](/Users/system/syncrescendence/orchestration/state/registry/acumen-triage-decision-ledger.jsonl)
2. [acumen-training-corpus-ledger.jsonl](/Users/system/syncrescendence/orchestration/state/registry/acumen-training-corpus-ledger.jsonl)
3. [ACUMEN-TRIAGE-EVIDENCE-REPORT.md](/Users/system/syncrescendence/orchestration/state/ACUMEN-TRIAGE-EVIDENCE-REPORT.md)

Important boundary:

1. the current ledgers prove that sanitized evidence recording and rematerialization work
2. the normal `run_triage.py` and `pipeline_flow.py` path is now ledger-first and rematerializes runtime current-state views from the append-only ledgers
3. live external proof still remains a distinct truth class until a credentialed run lands and is preserved

## Repeatable Entry Point

From repo root:

```bash
make acumen-sample-run
```

This is the repeatable local proof path.
It proves fixture polling and heuristic triage, not live external API execution.

For real registry polling:

```bash
ACUMEN_YOUTUBE_API_KEY=... make acumen-poll-youtube STRICT=1
```

For the narrow one-command live batch path:

```bash
ACUMEN_YOUTUBE_API_KEY=... GEMINI_API_KEY=... make acumen-live-batch
```

Useful overrides:

1. `STRICT=1` to fail on canonical-identity mismatch during preflight and pipeline run
2. `POLISH=charitable` or `POLISH=editorial` to mark the deterministic artifact as needing an intelligent follow-up pass
3. `STATUS_JSON=/abs/path/status.json` to redirect pipeline status output
4. `FORCE_POLL=0` to respect the stored cadence cursor instead of forcing the first live poll
5. `MAX_LIVE_CALLS=<n>` to tighten or widen the first Gemini batch guardrail

## Failure Modes

1. `registry missing` or `registry=invalid`: seed or registry contract issue
2. `missing_api_key`: the poll worker's configured API key env var is unset
3. `partial`: one or more registry channels failed poll while the rest completed and advanced cursor state
4. `channel not found in registry`: `CHANNEL_ID` does not exist in the registry passed to triage packet rendering
5. `video metadata missing required keys`: video JSON omitted one of `title`, `duration`, `description`, `initial_transcript`
6. identity probe mismatch in strict mode: active `gcloud` account or stored keychain account differs from canonical Acumen identity
7. queue or binding file missing: pipeline wrapper cannot compile Dawn Brief or perform identity preflight
8. deterministic artifact with `Intelligent Track Required`: requested polish exceeds current deterministic operator capability
9. live external proof remains absent even when the code exists, if no committed successful live status artifacts are captured

For `make acumen-live-batch`, the intended failure boundary is narrower:

1. `credential`: missing `ACUMEN_YOUTUBE_API_KEY` or `GEMINI_API_KEY`
2. `identity`: strict mismatch against the canonical Acumen identity
3. `external_service`: YouTube API or Gemini transport / HTTP / provider-response failure

`/Users/system/syncrescendence/orchestration/state/ACUMEN-PIPELINE-STATUS.json` now mirrors that boundary with top-level `failure_domain`, `failure_code`, `failure_message`, and embedded poll / triage status snapshots.

This lane is operational output, not constitutional source.
Augur / Perplexity packet markdown lands under `communications/prompts/` only after Acumen has already produced an eligible promoted or primary-flagged decision.
