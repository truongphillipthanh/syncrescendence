# RESPONSE-CODEX-CAMPAIGN-13-LANE-04-PORTFOLIO-POLICY-AND-REGISTRY-ENFORCEMENT

## Result

The portfolio policy layer is now written directly into repo law and into the Acumen registry enforcement path.

Delivered surfaces:

- `orchestration/state/impl/ACUMEN-PORTFOLIO-POLICY-AND-REGISTRY-ENFORCEMENT-v1.md`
- `orchestration/state/ACUMEN-PORTFOLIO-REPORT.md`
- `operators/acumen/validate_registry.py`
- `operators/acumen/poll_registry.py`

## What Changed

The new policy law binds widening to:

- curated inbound manifest refs
- explicit `portfolio_role`
- explicit downstream chain consumer roles
- bounded poll budget
- `admission.intake_plane = acumen`

The admitted portfolio roles are now:

- `core_monitored`
- `selective_monitored`
- `event_surge`
- `primary_only_witness`

Strict registry validation now fails not only on structural breakage, but also on widening-risk combinations such as:

- missing manifest / source-account / downstream-consumer / budget bindings
- non-Acumen intake plane
- core feeds with low density or high visual dependency
- inactive `event_surge` rows on aggressive cadence
- `primary_only_witness` rows that are not actually witness-shaped

Runtime polling now enforces the same policy shape:

- policy-declared but invalid rows are blocked
- `event_surge` rows are suppressed when inactive unless forced
- `primary_only_witness` rows are suppressed from routine polling unless forced
- role-based item caps are applied even when a higher per-channel limit is requested
- legacy rows still run in non-strict mode so the current two-channel registry does not hard-stop

## Current Portfolio Reading

The new portfolio report records that the present two registry rows are still legacy rows, not strict-bound admissions.
That means the current registry can operate, but the widening budget is effectively zero until those rows are backfilled with manifest, role, consumer, and budget fields.

## Verification

Executed:

- `python3 -m py_compile operators/acumen/registry_contract.py operators/acumen/validate_registry.py operators/acumen/poll_registry.py`
- `python3 operators/acumen/validate_registry.py --registry runtime/acumen/registry.json`
- `python3 operators/acumen/validate_registry.py --registry runtime/acumen/registry.json --strict`
- `python3 operators/acumen/poll_registry.py --registry runtime/acumen/registry.json --output runtime/acumen/out/poll-latest.jsonl --status-json runtime/acumen/poll-status.json --fixture-feed runtime/acumen/poll-fixture.sample.json --mode fixture`
- `git diff --check`

Observed behavior:

- non-strict registry validation passes on the current legacy registry
- strict registry validation now fails, as intended, because the existing rows do not yet carry explicit policy bindings
- fixture polling still runs in non-strict mode against the legacy rows
- `git diff --check` passes
