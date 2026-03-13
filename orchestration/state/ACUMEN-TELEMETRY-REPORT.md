# Acumen Telemetry Report

- Generated at: `2026-03-13T20:21:26Z`
- Contract: `orchestration/state/impl/ACUMEN-TELEMETRY-FAMILY-CONTRACT-v1.md`
- Receipt: A real admitted inbound system is observable, but only at the current registry-backed Acumen intake layer. The broader admitted inbound system is still incomplete, so this family stays minimal and marks five-account constellation telemetry unavailable instead of fabricating authority.

## Admitted Inbound System

- `system kind`: observed | `registry_backed_acumen_youtube_intake`
- `real system observed`: observed | `True`
- `completeness`: observed | `minimal_registry_only`
  - Registry admission and traversal exist, but broader constellation admission is not part of this observed family.
- `pipeline profile`: observed | `fixture_safe`
- `poll mode`: observed | `fixture`
- `triage mode`: observed | `heuristic`
- `broader constellation telemetry`: unavailable | `n/a`
  - The five-account constellation/import spine is not part of the admitted observed input set for this report.

## Registry Surface

- `channels total`: observed | `2`
- `channel names`: observed | `Google DeepMind, Andrej Karpathy`
- `generated at`: observed | `2026-03-13T04:37:46Z`
- `seed source`: observed | `/Users/system/syncrescendence/operators/acumen/channel_seed.example.json`

## Poll Surface

- `captured at`: observed | `2026-03-13T04:37:48Z`
- `channels total`: observed | `2`
- `channels in registry seen`: observed | `2`
- `new uploads`: observed | `0`
- `failures`: observed | `0`
- `channel status lines`: observed | `UC_x5XG1OV2P6uZZ5FSM9Ttw:Google DeepMind:status=ok:mode=fixture:new=0, UCv83tO5cePwHMt1952IVVHw:Andrej Karpathy:status=ok:mode=fixture:new=0`
- `live upstream counts`: unavailable | `n/a`
  - The committed poll snapshot is fixture-backed, so upstream live discovery counts are not directly observed here.

## Triage Surface

- `current batch processed`: observed | `0`
- `current batch training records`: observed | `0`
- `current batch skipped existing`: observed | `0`
- `current batch failures`: observed | `0`
- `cumulative triage events`: observed | `2`
- `cumulative training events`: observed | `2`
- `decision mix`: observed | `Compress=1, Promote=1`
- `promotion eligible events`: observed | `1`
- `promotion eligible ratio`: observed | `0.5`
- `evidence status`: observed | `PASS`
- `evidence findings`: observed | `0`

## Verification-Ready Surface

- `eligible items total`: observed | `1`
- `selected batch items`: observed | `1`
- `awaiting response`: observed | `1`
- `dossiers written`: observed | `1`
- `augur packets written`: observed | `1`
- `verification ready ratio`: observed | `1.0`
- `bridge validation ok`: observed | `True`
- `bridge validation findings`: observed | `0`
- `verification complete ratio`: unavailable | `n/a`
  - No ingested verification return is present in the current bridge state.

## Cost And Proof Surface

- `provider mix`: observed | `local=2`
- `model mix`: observed | `deterministic-heuristic=2`
- `gemini calls used`: observed | `0`
- `estimated cost usd`: estimated | `0.0`
  - The current cost surface is explicitly estimated, not provider-billed truth.
- `estimated cost per call usd`: estimated | `0.0`
  - The current cost surface is explicitly estimated, not provider-billed truth.
- `observed provider billing usd`: unavailable | `n/a`
  - No committed live provider billing evidence exists in the admitted observed system.
- `live batch proof present`: observed | `False`
- `latest proof outcome`: observed | `blocked`
- `latest failure domain`: observed | `credential`
- `latest failure code`: observed | `missing_credentials`
- `proof gate reason code`: observed | `missing_pipeline_status`
- `proof validator findings`: observed | `0`

## Five-Account Constellation Surface

- `constellation telemetry`: unavailable | `n/a`
  - Unavailable by design in this report. The family only observes the current registry-backed Acumen intake; five-account constellation/import telemetry remains outside the admitted observed boundary.

## Derivative Boundary

- Telemetry is derivative of admitted registry, poll, triage, evidence, bridge, and proof surfaces only.
- No telemetry ledger is created by this family.
