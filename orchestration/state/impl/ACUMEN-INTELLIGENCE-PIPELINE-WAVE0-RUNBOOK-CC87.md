# Acumen Intelligence Pipeline Wave0 Runbook — CC87

**Date**: 2026-03-11
**Status**: active  
**Class**: execution runbook

## Goal

Run the repeatable repo-native Acumen flow that currently exists, with explicit separation between:

1. code that is landed
2. fixture-safe behavior that is locally proven
3. live external behavior that still requires repo-external credentials and separate proof

## Preconditions

1. repo root available at `/Users/system/syncrescendence`
2. Python 3 available
3. for strict identity enforcement, local `gcloud` and macOS `security` tooling available
3. PRD feedstock intake present:
   - [20260305-prd-acumen-intelligence-pipeline-v2.md](/Users/system/syncrescendence/knowledge/feedstock/inbox/20260305-prd-acumen-intelligence-pipeline-v2.md)

## Execution Boundary

This runbook is intentionally limited to what the repo can execute today.

1. supported and locally proven:
   - registry generation and validation
   - canonical identity probe
   - fixture poll and cursor advancement through `poll_registry.py`
   - triage prompt rendering from existing video metadata JSON
   - heuristic triage
   - deterministic transcript processing
   - Dawn Brief compilation
   - sequential pipeline status capture
   - evidence-family validation against the current ledgers
2. supported in code but not proven here as live external execution:
   - YouTube polling through `poll_youtube_registry.py`
   - Gemini invocation through `run_gemini_triage.py` or `run_triage.py --mode gemini`
3. landed and now part of the mainline:
   - append-only evidence writes through `record_evidence.py` with runtime rematerialization
   - promoted-item dossier and Augur verification packet generation

## Required Environment Variables

1. `make acumen-sample-run` does not require `GEMINI_API_KEY` or `ACUMEN_YOUTUBE_API_KEY` because it forces `POLL_MODE=fixture` and `TRIAGE_MODE=heuristic`.
2. `ACUMEN_YOUTUBE_API_KEY` is required for live polling through `make acumen-poll-youtube` or `make acumen-pipeline-run POLL_MODE=live ...`.
3. `GEMINI_API_KEY` is required for live Gemini invocation through `make acumen-run-gemini-triage`, `make acumen-run-triage MODE=gemini`, or `make acumen-pipeline-run TRIAGE_MODE=gemini ...`.
4. Strict identity checks use local account state instead of env vars.

## Step 1: Preflight

```bash
make acumen-preflight
```

Expected:

1. `runtime/acumen/registry.json` exists
2. validator returns `registry=valid`
3. `orchestration/state/ACUMEN-IDENTITY-STATUS.json` is refreshed
4. non-strict preflight records identity observations even when `gcloud` or keychain state is absent

Strict variant:

```bash
make acumen-preflight STRICT=1
```

Strict identity passes only when detected account state matches `syncrescendence@gmail.com`.

If strict identity fails due active gcloud mismatch, run:

```bash
gcloud auth login syncrescendence@gmail.com
gcloud config set account syncrescendence@gmail.com
make acumen-preflight STRICT=1
```

Failure modes:

1. `registry missing` or `registry=invalid`
2. strict identity mismatch recorded in `ACUMEN-IDENTITY-STATUS.json`

## Step 2: Repeatable Sample Run

```bash
make acumen-sample-run
```

This single target executes the local repeatable path:

1. preflight
2. sample triage prompt render
3. sample deterministic transcript artifact
4. sample Dawn Brief compile
5. sequential pipeline wrapper with fixture polling and heuristic triage over `runtime/acumen/triage-decisions.jsonl`

Primary outputs:

1. `runtime/acumen/out/triage-packet.sample.json`
2. `runtime/acumen/out/deterministic-sample.md`
3. `runtime/acumen/out/DAWN-BRIEF-sample.md`
4. `runtime/acumen/out/DAWN-BRIEF-YYYYMMDD.md`
5. `orchestration/state/ACUMEN-IDENTITY-STATUS.json`
6. `orchestration/state/ACUMEN-PIPELINE-STATUS.json`
7. `runtime/acumen/out/poll-latest.jsonl`
8. `runtime/acumen/poll-status.json`
9. `runtime/acumen/triage-status.json`

Useful overrides:

1. `STRICT=1`
2. `POLISH=charitable`
3. `STATUS_JSON=/abs/path/custom-status.json`
4. `QUEUE=/abs/path/triage-decisions.jsonl`

## Step 3: Build Triage Packet From Real Metadata

Create a local video metadata JSON with:

1. `title`
2. `duration`
3. `description`
4. `initial_transcript`

Then run:

```bash
make acumen-build-triage-packet CHANNEL_ID=UC_x5XG1OV2P6uZZ5FSM9Ttw VIDEO_JSON=/abs/path/video.json OUTPUT=/Users/system/syncrescendence/runtime/acumen/out/triage-packet.md
```

Expected output:

1. packet JSON artifact at the requested `OUTPUT`
2. optional prompt preview only when `PROMPT_OUTPUT` is supplied

Failure modes:

1. `channel not found in registry`
2. `video metadata missing required keys`

## Step 4: Run Deterministic Track

```bash
make acumen-deterministic-track INPUT_TEXT=/abs/path/transcript.txt GENRE=Commentary DEPTH=Precis POLISH=charitable OUTPUT=/Users/system/syncrescendence/runtime/acumen/out/deterministic-sample.md
```

Expected output:

1. deterministic artifact written to the requested path
2. if `POLISH=charitable` or `POLISH=editorial`, the artifact explicitly states `Intelligent Track Required`

## Step 5: Compile Dawn Brief

Prepare or supply a triage decision queue. The queue can come from:

1. `run_triage.py`
2. a prior pipeline run
3. rematerialized runtime evidence from the Acumen ledgers

Example:

```bash
make acumen-build-dawn-brief INPUT_JSONL=/Users/system/syncrescendence/runtime/acumen/triage-decisions.jsonl OUTPUT=/Users/system/syncrescendence/runtime/acumen/out/DAWN-BRIEF.md
```

## Step 6: Run Sequential Pipeline Wrapper

Repeatable local proof:

```bash
make acumen-pipeline-run QUEUE=/Users/system/syncrescendence/runtime/acumen/triage-decisions.jsonl OUT=/Users/system/syncrescendence/runtime/acumen/out POLL_MODE=fixture FIXTURE_FEED=/Users/system/syncrescendence/runtime/acumen/poll-fixture.sample.json TRIAGE_MODE=heuristic STRICT_IDENTITY=1
```

Live external variant when credentials exist:

```bash
ACUMEN_YOUTUBE_API_KEY=... GEMINI_API_KEY=... make acumen-pipeline-run QUEUE=/Users/system/syncrescendence/runtime/acumen/triage-decisions.jsonl OUT=/Users/system/syncrescendence/runtime/acumen/out POLL_MODE=live TRIAGE_MODE=gemini STRICT_IDENTITY=1
```

Expected from the repeatable local proof path:

1. identity probe is rerun against the configured binding
2. fixture poll status is captured
3. heuristic triage status is captured
4. dated Dawn Brief artifact is generated under the chosen `OUT` directory
5. status is written to `orchestration/state/ACUMEN-PIPELINE-STATUS.json`
6. evidence is written through append-only ledgers and rematerialized back into the runtime current-state views

Failure modes:

1. missing queue file
2. missing binding file
3. Dawn Brief compile failure
4. strict identity mismatch returns non-zero even when Dawn Brief compilation succeeded
5. live mode fails if `ACUMEN_YOUTUBE_API_KEY` is absent
6. live Gemini mode fails if `GEMINI_API_KEY` is absent or the adapter exhausts retries

## Step 7: Build Verification Bridge For Promoted Items

```bash
make acumen-build-verification-bridge VIDEO_IDS=deepmind-gemini-31-architecture
make acumen-validate-verification-bridge
```

Expected output:

1. `runtime/acumen/out/verification-dossiers/*.json`
2. `communications/prompts/PACKET-PERPLEXITY-acumen-*.md`
3. `orchestration/state/ACUMEN-AUGUR-VERIFICATION-BRIDGE.json`
4. `orchestration/state/ACUMEN-AUGUR-VERIFICATION-BRIDGE-REPORT.md`

Boundary:

1. this bridge is downstream of Acumen triage
2. it is lawful only for `Promote` and `Flag-for-Primary` items
3. it creates verification inputs, not final doctrine

## Guardrails

1. deterministic track always runs before any intelligent-track adapter
2. canonical Google identity for Acumen surfaces is `syncrescendence@gmail.com`
3. strict runs must fail on identity drift
4. no secrets stored in repo artifacts
5. append-only evidence ledgers outrank `runtime/acumen/*.jsonl` current-state views
6. live polling and live Gemini are code-present but remain separate proof classes until a committed live run lands
