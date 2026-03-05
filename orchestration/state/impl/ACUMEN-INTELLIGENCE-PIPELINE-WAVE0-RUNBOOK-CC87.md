# Acumen Intelligence Pipeline Wave0 Runbook — CC87

**Date**: 2026-03-04  
**Status**: active  
**Class**: execution runbook

## Goal

Stand up deterministic extraction and delivery scaffolding with no external API dependency.

## Preconditions

1. repo root available at `/Users/system/syncrescendence`
2. Python 3 available
3. PRD feedstock intake present:
   - [20260305-prd-acumen-intelligence-pipeline-v2.md](/Users/system/syncrescendence/knowledge/feedstock/inbox/20260305-prd-acumen-intelligence-pipeline-v2.md)

## Step 1: Initialize Registry

```bash
make acumen-init-registry
make acumen-validate-registry
make acumen-identity-probe STRICT=1
```

Expected:

1. `runtime/acumen/registry.json` exists
2. validator returns `registry=valid`
3. strict identity probe passes only when active gcloud account is `syncrescendence@gmail.com`

If strict identity fails due active gcloud mismatch, run:

```bash
gcloud auth login syncrescendence@gmail.com
gcloud config set account syncrescendence@gmail.com
make acumen-identity-probe STRICT=1
```

## Step 2: Build Triage Packet (sample)

Create a local video metadata JSON with:

1. `title`
2. `duration`
3. `description`
4. `initial_transcript`

Then run:

```bash
make acumen-build-triage-packet CHANNEL_ID=UC_x5XG1OV2P6uZZ5FSM9Ttw VIDEO_JSON=/abs/path/video.json OUTPUT=/Users/system/syncrescendence/runtime/acumen/out/triage-packet.md
```

## Step 3: Run Deterministic Track (sample)

```bash
make acumen-deterministic-track INPUT_TEXT=/abs/path/transcript.txt GENRE=Commentary DEPTH=Precis POLISH=charitable OUTPUT=/Users/system/syncrescendence/runtime/acumen/out/deterministic-sample.md
```

## Step 4: Compile Dawn Brief

Prepare `runtime/acumen/triage-decisions.jsonl`, then:

```bash
make acumen-build-dawn-brief INPUT_JSONL=/Users/system/syncrescendence/runtime/acumen/triage-decisions.jsonl OUTPUT=/Users/system/syncrescendence/runtime/acumen/out/DAWN-BRIEF.md
```

## Step 5: Run Flow Scaffold

```bash
make acumen-pipeline-run QUEUE=/Users/system/syncrescendence/runtime/acumen/triage-decisions.jsonl OUT=/Users/system/syncrescendence/runtime/acumen/out
```

Expected:

1. Dawn brief artifact generated
2. status written to:
   - `orchestration/state/ACUMEN-PIPELINE-STATUS.json`

## Guardrails

1. deterministic track always runs before any intelligent-track adapter
2. canonical Google identity for Acumen surfaces is `syncrescendence@gmail.com`
3. strict runs must fail on identity drift
4. no secrets stored in repo artifacts
5. all external model calls must be logged into a training corpus in later waves
