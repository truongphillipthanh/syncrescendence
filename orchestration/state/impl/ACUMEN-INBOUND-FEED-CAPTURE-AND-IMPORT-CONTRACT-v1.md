# Acumen Inbound Feed Capture And Import Contract v1

**Status**: staged  
**Class**: repo-local contract  
**Purpose**: govern curated upstream feed capture before mutation so the five-account constellation can widen Acumen without creating a shadow intake authority

## Why This Contract Exists

Acumen already has a lawful downstream cycle for:

`registry -> poll -> triage -> verification -> assessment -> product family`

What the repo still needs upstream is a governed way to capture curated follow or subscription state from the five chain accounts before any import or mutation occurs.

This contract establishes that upstream chain as:

`browser/session recon -> raw capture witness -> normalized manifest -> validation -> inbound portfolio -> registry-ready seed`

That ordering is mandatory.
If it is skipped, browser state, repo witnesses, and later import surfaces collapse into one another and feed governance stops being auditable.

## Governing Boundary

This contract governs:

1. browser-visible reconnaissance over curated follow or subscription state
2. preservation of the first repo-side raw witness for that state
3. normalization into a manifest family that can later be validated
4. later import into an inbound portfolio surface and a registry-ready seed

This contract does not govern:

1. outbound follow, unfollow, subscribe, or unsubscribe mutation
2. account cloning or parity mutation between chain accounts
3. downstream dissemination or posting strategy
4. direct widening of `runtime/acumen/registry.json` without the manifest path

## Truth Classes

The upstream capture path contains distinct truth classes that must remain separate:

1. browser/session state
   - the live platform surface currently visible for one account on one platform
2. raw capture witness
   - the preserved export, page dump, copied table, HTML, CSV, or JSON staged through:
   - [knowledge/feedstock/inbox](/Users/system/syncrescendence/knowledge/feedstock/inbox)
   - [knowledge/feedstock/receipts](/Users/system/syncrescendence/knowledge/feedstock/receipts)
3. normalized manifest
   - the account/platform/run-specific JSON and Markdown pair under [runtime/acumen/inbound-feed-manifests](/Users/system/syncrescendence/runtime/acumen/inbound-feed-manifests)
4. validated import surfaces
   - the later inbound portfolio preview and registry-ready seed
5. live Acumen intake surfaces
   - `runtime/acumen/registry.json` and the normal poll or triage path

No later truth class may overwrite or silently stand in for an earlier one.
The raw capture witness stays authoritative for what was observed.
The normalized manifest stays authoritative for repo-side translation of that capture.
The inbound portfolio and registry-ready seed remain derivative import products.

## Identity Law

Feed capture is lawful only when the active account identity is known.

The operator must confirm, before capture:

1. which chain account is active
2. which platform surface is being inspected
3. which browser session or profile produced the view
4. what evidence confirms that identity

If the active account cannot be confirmed, capture stops.
Identity ambiguity is a hard block, not a warning.

Examples of blocking ambiguity include:

1. multiple signed-in accounts with no clear active identity
2. silent session switching during capture
3. a visible feed list whose owning account cannot be proven
4. disagreement between claimed account, session evidence, and captured platform UI

When ambiguity occurs, the run may leave a staging receipt explaining the block, but it may not produce an import-eligible normalized manifest and it may not advance to validation, portfolio import, or registry seeding.

## Raw Witness Law

Raw captures must be preserved through the existing feedstock witness lanes.
This contract does not create a second raw-authority surface inside runtime or communications lanes.

Required preservation rule:

1. stage the raw capture artifact into [knowledge/feedstock/inbox](/Users/system/syncrescendence/knowledge/feedstock/inbox)
2. write or update the staging receipt in [knowledge/feedstock/receipts](/Users/system/syncrescendence/knowledge/feedstock/receipts)
3. reference those preserved raw artifacts from the normalized manifest

The manifest is not the first witness.
The feedstock artifact is.

## Manifest Law

Each normalized manifest run must stay narrow:

1. one account per manifest run
2. one platform per manifest run
3. one capture event per manifest run

The normalized manifest pair lives under [runtime/acumen/inbound-feed-manifests](/Users/system/syncrescendence/runtime/acumen/inbound-feed-manifests) and translates the raw witness into a stable repo-side structure for later validation and import.

The manifest pair must preserve:

1. capture account and claimed chain role
2. platform and capture timing
3. identity evidence and ambiguity status
4. raw capture lineage back to feedstock
5. entry count and per-entry platform identity where available
6. unresolved caveats that block or defer import

## Validation And Import Boundary

Validation sits between normalization and any downstream import.
The validator should reject manifests that fail identity proof, lineage proof, or platform-ID readiness where the current worker requires a stable identifier.

The import boundary remains:

`validated manifest -> inbound portfolio -> registry-ready seed`

Those later surfaces are allowed to classify entries differently, but they may not erase the original capture distinctions.

## Platform Admissibility Rule

The inbound portfolio may preserve captures from any supported curated platform surface.
The live Acumen registry may admit only sources that match a landed worker and contract.

Current rule:

1. YouTube captures may become registry-ready when they resolve to stable channel identity and satisfy current Acumen registry requirements.
2. Non-YouTube captures remain portfolio-visible but registry-deferred until a matching worker, contract, and validation path exist.

Registry deferral is not data loss.
It is a truthful statement that the source is known upstream but not yet actionable by the live intake machinery.

## Runtime Identity Boundary

Chain-account browser capture is upstream reconnaissance.
It does not replace the current repo-executed Acumen runtime identity bound through [ACUMEN-IDENTITY-BINDING-CC87.json](/Users/system/syncrescendence/orchestration/state/ACUMEN-IDENTITY-BINDING-CC87.json).

The browser-visible account being captured may be `acumen`, `coherence`, `efficacy`, `mastery`, or `transcendence`.
The repo-native Acumen runtime remains separately governed by the existing identity-binding and strict-identity rules.

## Out Of Scope

The following remain out of scope for this contract:

1. mass follow or unsubscribe synchronization
2. account-to-account parity mutation
3. browser automation that changes platform state
4. any new authority surface for raw feed captures outside feedstock
5. non-manifest shortcuts that mutate `runtime/acumen/registry.json` directly from browser observations

## Bottom Line

The lawful upstream shape is:

`browser/session recon -> raw capture witness -> normalized manifest -> validation -> inbound portfolio -> registry-ready seed`

It must stop on identity ambiguity, preserve raw captures through the existing feedstock witness lanes, keep non-YouTube captures visible but registry-deferred, and keep outbound follow or subscription mutation outside scope.
