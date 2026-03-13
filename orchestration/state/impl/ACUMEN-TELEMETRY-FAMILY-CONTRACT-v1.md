# Acumen Telemetry Family Contract v1

**Status**: minimal derivative family  
**Date**: 2026-03-13

## Purpose

Expose a lawful telemetry readout over the real admitted inbound system that currently exists in repo truth.

Telemetry remains derivative.
It does not become a new authority plane.

## Current Admission Boundary

The only admitted inbound system this family may currently observe is the existing registry-backed Acumen intake:

- `runtime/acumen/registry.json`
- `runtime/acumen/poll-status.json`
- `runtime/acumen/triage-status.json`
- `orchestration/state/ACUMEN-PIPELINE-STATUS.json`
- `orchestration/state/ACUMEN-TRIAGE-EVIDENCE-REPORT.json`
- `orchestration/state/ACUMEN-AUGUR-VERIFICATION-BRIDGE.json`
- `orchestration/state/ACUMEN-AUGUR-VERIFICATION-BRIDGE-REPORT.json`
- `orchestration/state/ACUMEN-LIVE-BATCH-PROOF-STATUS.json`
- `orchestration/state/ACUMEN-LIVE-BATCH-PROOF-REPORT.json`
- `orchestration/state/registry/acumen-triage-decision-ledger.jsonl`
- `orchestration/state/registry/acumen-training-corpus-ledger.jsonl`

The five-account inbound constellation and import spine are not yet part of the admitted observed system for this family.
Until that spine is landed and observable, constellation telemetry must remain explicitly unavailable.

## Telemetry Law

1. telemetry must remain derivative of admitted runtime, evidence, bridge, and proof artifacts
2. every telemetry datum must be labeled `observed`, `estimated`, or `unavailable`
3. `unavailable` is preferred over invention whenever the admitted system is incomplete
4. cost fields may be `estimated`, but must not be restated as observed billing truth
5. telemetry may summarize admitted channels, traversal, triage yield, verification-ready state, and proof posture
6. telemetry must not claim five-account feed admission, manifest import readiness, or browser-bound execution unless those surfaces are materially landed and observed

## Datum Envelope

Every report datum must use this envelope:

```json
{
  "label": "observed | estimated | unavailable",
  "value": "scalar | list | object | null",
  "sources": ["repo-relative/path"],
  "reason": "optional explanatory boundary"
}
```

If `value` is an object, its child fields must also be datum envelopes.

## Forbidden Content

The telemetry family must not capture or restate:

- raw prompts
- raw model responses
- secrets or credential values
- fabricated live metrics
- fabricated admission state

## Required Surfaces

This family writes only current-state derivative surfaces:

- `orchestration/state/ACUMEN-TELEMETRY-REPORT.json`
- `orchestration/state/ACUMEN-TELEMETRY-REPORT.md`

Validation is performed by:

- `operators/validators/validate_acumen_telemetry.py`

## Explicit Non-Goal

Do not create a telemetry ledger.

The admitted witnesses already live in the registry, status, evidence, bridge, and proof families.
This telemetry family exists only to compose them into a truthful current-state readout.
