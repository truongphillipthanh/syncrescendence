# Acumen Portfolio Policy And Registry Enforcement v1

**Status**: operative  
**Purpose**: keep Acumen portfolio widening lawful by binding registry admission to curated manifests, explicit portfolio role, downstream chain consumer role, and bounded cadence / budget while preserving Acumen as the only raw intake plane

## Core Law

Widening into `runtime/acumen/registry.json` is lawful only through this chain:

`curated inbound manifest -> Acumen admission binding -> portfolio role -> downstream chain consumer role -> bounded poll budget -> normal Acumen poll / triage`

A followed source is not active intake merely because it appears in a browser account or in a capture artifact.
It becomes active intake only after Acumen admits it into the registry under explicit policy.

## Sovereignty Rule

Acumen remains the only raw intake plane.

- curated manifests may originate from `acumen`, `coherence`, `efficacy`, `mastery`, or `transcendence`
- those chain accounts are upstream curation surfaces, not parallel raw intake machines
- downstream chains may consume Acumen outputs
- downstream chains may not self-author raw source admission
- Augur / verification / assessment remain downstream of Acumen triage and do not nominate new raw feeds

## Required Registry Binding For Widened Rows

Every widened registry row must carry these policy fields:

```json
{
  "admission": {
    "source_account": "coherence",
    "intake_plane": "acumen",
    "curated_manifest_refs": [
      "runtime/acumen/inbound-feed-manifests/20260313-coherence-youtube-subscriptions-source.json"
    ]
  },
  "portfolio_role": "selective_monitored",
  "downstream_chain_consumer_roles": [
    "coherence_synthesis",
    "efficacy_execution"
  ],
  "poll_budget": {
    "max_items_per_poll": 3,
    "monthly_new_item_budget": 16,
    "event_window_active": false
  }
}
```

The existing structural channel fields remain authoritative for feed identity and operating defaults:

- `channel_id`
- `name`
- `cadence`
- `priority_band`
- `signal_density`
- `visual_dependency`
- `triage_hit_rate`
- `default_compression`
- `default_polish`

## Portfolio Roles

### `core_monitored`

Use only for routine feeds that have already proven they can justify recurring Acumen load.

- expected profile: `medium` or `high` signal density, `none` or `low` visual dependency, proven hit rate
- cadence ceiling: `daily`
- max items per poll: `5`
- monthly new-item budget: `40`
- strict risk failures:
- `low` signal density
- `high` visual dependency
- `triage_hit_rate < 0.35`

### `selective_monitored`

Use for feeds that matter, but not enough to deserve steady-state core cost.

- cadence ceiling: `weekly`
- max items per poll: `3`
- monthly new-item budget: `16`
- strict risk failures:
- `daily` cadence
- budget beyond selective cap

### `event_surge`

Use for launch, hearing, incident, or temporary-window feeds.

- cadence ceiling: `weekly` while the event window is active
- inactive event-surge rows must stay `monthly` or `irregular`
- max items per poll: `2`
- monthly new-item budget: `8`
- `poll_budget.event_window_active` must be explicit

### `primary_only_witness`

Use for feeds where compression is usually misleading.

- expected profile: `high` visual dependency
- cadence ceiling: `monthly`
- max items per poll: `1`
- monthly new-item budget: `4`
- required default compression: `Treatment` or `Transcript`
- these rows are witness inventory, not routine compression inventory

## Downstream Chain Consumer Roles

At least one downstream consumer role must be declared for every widened row:

- `coherence_synthesis`
- `efficacy_execution`
- `mastery_curriculum`
- `transcendence_governance`

This field explains why the source exists inside the current cycle.
It is not enough to say the source is generally interesting.

## Strict Enforcement

`operators/acumen/validate_registry.py --strict` must fail when:

- a widened row lacks curated inbound manifest refs
- `admission.intake_plane` is anything other than `acumen`
- `portfolio_role` is missing or invalid
- downstream consumer roles are missing or invalid
- poll budget is missing or unbounded
- cadence is more aggressive than the role ceiling
- a row claims a risky role / signal combination such as:
- `core_monitored` with low density
- `core_monitored` with high visual dependency
- inactive `event_surge` on aggressive cadence
- `primary_only_witness` without high visual dependency
- high-visual sources admitted as ordinary monitored feeds

`operators/acumen/poll_registry.py` must enforce the same policy at runtime:

- policy-declared but invalid rows are blocked
- `event_surge` rows are suppressed when the event window is inactive unless the operator forces the run
- `primary_only_witness` rows are suppressed from routine polling unless the operator forces the run
- per-role item caps apply even when a caller requests a higher channel limit
- legacy rows may continue in non-strict runtime mode, but they are not lawful widening proof

## Admission Frontier

Current implication:

- new feeds should default to `selective_monitored` or `event_surge`
- promotion to `core_monitored` requires observed yield from the present Acumen cycle
- portfolio widening is blocked when Dawn Brief, verification, assessment, or primary-source routing cannot metabolize the added load

This policy layer exists to keep widening subordinate to intelligence production rather than letting source count outrun chain utility.
