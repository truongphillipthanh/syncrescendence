# Acumen Inbound Feed Portfolio

- Generated at: `2026-03-13T21:06:24Z`
- Source manifest dir: `runtime/acumen/inbound-feed-manifests`
- Current registry: `runtime/acumen/registry.json`
- Portfolio JSON: `orchestration/state/ACUMEN-INBOUND-FEED-PORTFOLIO.json`
- Portfolio markdown: `orchestration/state/ACUMEN-INBOUND-FEED-PORTFOLIO.md`
- Seed output: `runtime/acumen/inbound-feed-import-seed.json`
- Intake authority: `Acumen remains the sole shared intake authority; this portfolio and seed are preview surfaces only.`
- Manifests discovered: `0`
- Entries discovered: `0`
- Valid manifests: `0`
- Invalid manifests: `0`
- Registry-ready entries: `0`
- Portfolio-only entries: `0`
- Blocked identity entries: `0`
- Ambiguous target entries: `0`
- Unresolved platform IDs: `0`
- Seed rows emitted: `0`

## Merge Discipline

- The inbound portfolio is a preview surface only. It does not replace `runtime/acumen/registry.json`.
- Seed rows are emitted only for current-registry-compatible entries and are revalidated through the existing Acumen registry contract before merge.
- Merge path: `python3 operators/acumen/init_registry.py --seed runtime/acumen/inbound-feed-import-seed.json --output runtime/acumen/registry.json --merge`
- Strict validation path: `python3 operators/acumen/validate_registry.py --registry runtime/acumen/registry.json --strict`

## Manifests

- no manifests discovered

## Entries

- no manifest entries discovered
