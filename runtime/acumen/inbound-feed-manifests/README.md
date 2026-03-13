# Inbound Feed Manifests

This directory holds the normalized manifest family for curated upstream feed captures before import into any Acumen portfolio or registry surface.

## Governing Sequence

Every run in this directory must remain subordinate to the upstream chain:

`browser/session recon -> raw capture witness -> normalized manifest -> validation -> inbound portfolio -> registry-ready seed`

The files here are the normalized manifest stage only.
They are not the raw witness and they are not the live registry.

## Raw Witness Prerequisite

Before a manifest is written here, the raw capture must be preserved through the existing feedstock witness lanes:

1. [knowledge/feedstock/inbox](/Users/system/syncrescendence/knowledge/feedstock/inbox)
2. [knowledge/feedstock/receipts](/Users/system/syncrescendence/knowledge/feedstock/receipts)

Each manifest must point back to those preserved artifacts through `raw_capture_refs`.

## Identity Rule

Do not normalize an import-eligible manifest when account identity is ambiguous.

Blocking cases include:

1. the active account cannot be proven from the browser session
2. multiple logged-in accounts make the captured owner unclear
3. the claimed chain account disagrees with the captured UI evidence
4. session switching occurs during the same capture run

If ambiguity exists, stop the run and record the block in the feedstock receipt or operator notes instead of advancing a manifest toward validation or import.

## File Naming

Use one manifest pair per account, platform, and capture run:

1. `YYYYMMDD-<account>-<platform>-subscriptions-source.json`
2. `YYYYMMDD-<account>-<platform>-subscriptions-source.md`

Example:

1. `20260313-acumen-youtube-subscriptions-source.json`
2. `20260313-acumen-youtube-subscriptions-source.md`

Recommended `<account>` values:

1. `acumen`
2. `coherence`
3. `efficacy`
4. `mastery`
5. `transcendence`

The `<platform>` segment should be explicit and lowercase, for example `youtube`, `x`, `substack`, or `github`.

Do not merge multiple accounts or multiple platforms into one source manifest.

## Minimum JSON Fields

Each source manifest JSON should include at least:

1. `manifest_id`
2. `capture_account`
3. `claimed_chain`
4. `platform`
5. `capture_started_at`
6. `capture_completed_at`
7. `identity_status`
8. `identity_evidence`
9. `ambiguity_status`
10. `entry_count`
11. `entries`
12. `raw_capture_refs`
13. `notes`

Recommended meanings:

1. `manifest_id`
   - stable run identifier such as `20260313-acumen-youtube-subscriptions-source`
2. `capture_account`
   - the specific chain account captured
3. `claimed_chain`
   - the role-bound chain identity for that account
4. `platform`
   - the upstream platform surface being captured
5. `identity_status`
   - `confirmed` only when the active account is proven
6. `identity_evidence`
   - brief structured evidence describing the active session, profile, or visible account proof
7. `ambiguity_status`
   - `none` for a clean run; any other value blocks validation
8. `entry_count`
   - the number of captured entries after any explicit dedupe within the manifest
9. `entries`
   - the per-source normalized rows
10. `raw_capture_refs`
   - references to the feedstock inbox artifact and feedstock receipt
11. `notes`
   - caveats, missing fields, or deferred follow-up

## Entry Guidance

Each `entries[]` row should preserve the best stable platform identity available from the raw witness.

Recommended fields include:

1. `display_name`
2. `platform_id`
3. `platform_handle`
4. `source_url`
5. `capture_position`
6. `dedupe_key`
7. `notes`

Platform-specific rule:

1. YouTube rows should preserve stable channel identity when it is available, such as `channel_id`.
2. Rows without the stable identifier required by the current worker may remain manifest-known but should be expected to fail validation or remain import-deferred.

## Markdown Companion

The Markdown companion should summarize:

1. manifest identity and capture date
2. source account and platform
3. capture method
4. raw capture witness references
5. counts and major caveats
6. identity proof status
7. ambiguity or lineage risks
8. import eligibility preview

The Markdown file is for fast operator review.
The JSON file remains the structured normalized source surface.

## Portfolio And Registry Boundary

Manifest files here do not admit sources directly into the live registry.

Current import expectation:

1. validated manifests may become inbound portfolio rows
2. only registry-compatible rows become registry-ready seed rows
3. YouTube may be registry-ready when stable channel identity is present
4. non-YouTube captures stay portfolio-visible but registry-deferred until matching workers exist

## What Does Not Belong Here

Do not use this directory for:

1. raw browser dumps or direct exports
2. outbound follow or subscription mutation plans
3. merged cross-account master files
4. operator receipts that belong in feedstock
5. direct edits to `runtime/acumen/registry.json`
