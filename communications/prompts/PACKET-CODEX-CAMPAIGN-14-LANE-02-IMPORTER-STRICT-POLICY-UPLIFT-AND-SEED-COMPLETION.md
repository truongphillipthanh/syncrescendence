# Packet — Codex Campaign 14 Lane 02 — Importer Strict-Policy Uplift And Seed Completion

**Reasoning level**: `extra high`

Close the importer gap identified by Campaign 13.

Write or patch:

1. `/Users/system/syncrescendence/operators/acumen/import_inbound_feed_manifests.py`
2. any minimal helper or schema surface needed
3. regenerate:
   - `/Users/system/syncrescendence/orchestration/state/ACUMEN-INBOUND-FEED-PORTFOLIO.json`
   - `/Users/system/syncrescendence/orchestration/state/ACUMEN-INBOUND-FEED-PORTFOLIO.md`
   - `/Users/system/syncrescendence/runtime/acumen/inbound-feed-import-seed.json`

Requirements:

1. emitted seed rows must carry the strict policy bindings now required by admission:
   - `admission.source_account`
   - `admission.intake_plane`
   - `admission.curated_manifest_refs`
   - `portfolio_role`
   - `downstream_chain_consumer_roles`
   - `poll_budget`
2. importer must stay derivative and not mutate the registry directly
3. match-state output should remain explicit and truthful

Write your receipt:

- `/Users/system/syncrescendence/communications/responses/RESPONSE-CODEX-CAMPAIGN-14-LANE-02-IMPORTER-STRICT-POLICY-UPLIFT-AND-SEED-COMPLETION.md`

Run `git diff --check`.
