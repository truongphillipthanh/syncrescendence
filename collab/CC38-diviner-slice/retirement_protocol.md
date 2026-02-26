# Retirement Protocol — Competitive Exclusion with Enforced Pruning

**Version**: 1.0.0
**Status**: canonical
**Created**: 2026-02-26
**Authority**: Sovereign directive

---

## Purpose and Scope

This protocol governs the lifecycle of **platforms, tools, and backlogs** — non-canon operational capabilities. For every 1 new capability activated, 2 existing legacy capabilities must be retired. This is competitive exclusion with enforced pruning.

Canon axiom lifecycle (promotion, deprecation, apoptosis of canonical knowledge artifacts) is handled separately by `apoptosis_protocol.md`. This document does not apply to canon artifacts.

---

## The 2:1 Ratio Rule

- **Trigger**: Any capability status transition from `proposed` to `active`.
- **Requirement**: 2 retirements must be completed and archived before 1 new activation is permitted.
- **Enforcement mode**: Automatic pre-check against the Retirement Ledger. Sovereign override waiver available (logged as a `waiver` event in the ledger).

No exceptions without a waiver. A waiver is not forgiveness — it is a debt that accrues.

---

## Capability Registry

**Location**: `orchestration/00-ORCHESTRATION/state/ARCH-TOOL_NICHE_REGISTRY.yaml`

Each entry tracks a single capability (platform, tool, or backlog item).

### Schema

| Field | Type | Description |
|-------|------|-------------|
| `capability_id` | string | Unique identifier (e.g., `CAP-0042`) |
| `name` | string | Human-readable name |
| `class` | enum | `platform`, `tool`, `backlog` |
| `status` | enum | `proposed`, `active`, `retire_pending`, `retired`, `resurrection_pending`, `pilot` |
| `niche` | string | The ecological niche this capability occupies |
| `owner` | string | Responsible agent or Sovereign |
| `introduced_at` | ISO date | When the capability entered the registry |
| `retired_at` | ISO date or null | When the capability was archived |
| `supersedes` | array of capability_id | Which prior capabilities this one replaces |

**Lock order**: `capability_id` is single-writer through registry lock. No concurrent mutations to the same capability entry.

---

## State Machine

```
PROPOSED ──────────────► RATIO_PENDING
                              │
              ┌───────────────┼───────────────┐
              ▼               │               ▼
          REJECTED            │            ACTIVE
     (ratio unsatisfied,      │               │
      no waiver)              │               ▼
                              │         RETIRE_PENDING
                              │               │
                              │               ▼
                              │           RETIRED
                              │               │
                              │               ▼
                              │      RESURRECTION_PENDING
                              │               │
                              │               ▼
                              │            PILOT
                              │            │    │
                              │            ▼    ▼
                              │        ACTIVE  RETIRED
                              │    (success)  (fail)
```

### Transitions

| From | To | Condition |
|------|----|-----------|
| `PROPOSED` | `RATIO_PENDING` | Activation requested |
| `RATIO_PENDING` | `ACTIVE` | 2 retirements linked and archived in ledger |
| `RATIO_PENDING` | `REJECTED` | Ratio not satisfied and no Sovereign waiver |
| `ACTIVE` | `RETIRE_PENDING` | Retirement initiated |
| `RETIRE_PENDING` | `RETIRED` | Archive manifest complete (paths, restore_instructions, metadata_hash) |
| `RETIRED` | `RESURRECTION_PENDING` | Resurrection requested |
| `RESURRECTION_PENDING` | `PILOT` | All 4 activation-energy artifacts present |
| `PILOT` | `ACTIVE` | Pilot success + ratio satisfied |
| `PILOT` | `RETIRED` | Pilot failure |

---

## Retirement Ledger

**Location**: `orchestration/00-ORCHESTRATION/state/DYN-RETIREMENT_LEDGER.jsonl`

Append-only event log. Every activation, retirement, resurrection, and waiver is recorded.

### Schema (one JSON object per line)

| Field | Type | Description |
|-------|------|-------------|
| `event_id` | string | Unique event identifier |
| `event_type` | enum | `activate`, `retire`, `resurrect`, `waiver` |
| `capability_id` | string | The capability this event concerns |
| `paired_retirements` | array of capability_id | For `activate` events: the 2 capabilities retired to satisfy the ratio |
| `ratio_check_passed` | boolean | Whether the 2:1 ratio was satisfied at event time |
| `evidence_refs` | array of string | Paths to supporting artifacts (archive manifests, waiver approvals, pilot reports) |

---

## Archive Destination

**Location**: `sources/icebox/`

Retired capabilities are archived here. Nothing is deleted — everything is frozen with restore metadata.

### Manifest

**Location**: `sources/icebox/ICEBOX-MANIFEST.jsonl`

One JSON object per line, one entry per archived capability.

| Field | Type | Description |
|-------|------|-------------|
| `archive_id` | string | Unique archive identifier |
| `capability_id` | string | Links to the registry entry |
| `archived_paths` | array of string | All file paths moved to icebox |
| `archived_at` | ISO date | When the archive was completed |
| `reason` | string | Why this capability was retired |
| `restore_instructions` | string | Exact steps to resurrect this capability |
| `metadata_hash` | string | Integrity hash of archived content |

A retirement is **incomplete** (stays `RETIRE_PENDING`) if `restore_instructions` or `metadata_hash` is missing.

---

## Resurrection Protocol — Activation Energy

Bringing back a retired capability is intentionally expensive. Four artifacts are required, minimum, before a retired capability can enter `PILOT` status.

### Required Artifacts

1. **Problem statement**: What gap does the resurrected tool fill that no active tool addresses?
2. **Niche gap proof**: Demonstrate that no currently active capability covers the niche. Evidence, not assertion.
3. **Two retirements plan**: Identify 2 active or retire_pending capabilities to retire, maintaining the 2:1 ratio.
4. **7-day pilot plan**: Define success criteria, monitoring approach, and rollback trigger for a trial period before permanent activation.

All 4 artifacts must be filed in the resurrection request before the transition from `RESURRECTION_PENDING` to `PILOT` is permitted. The pilot period is 7 days minimum. Pilot success transitions to `ACTIVE` (with the 2 planned retirements executed). Pilot failure transitions back to `RETIRED`.

---

## Failure Modes

| ID | Severity | Condition | Response |
|----|----------|-----------|----------|
| `RET-F001` | **FATAL** | New capability activated without 2 retirements | Block activation. Revert to `RATIO_PENDING`. |
| `RET-F002` | **FATAL** | Archive missing `restore_instructions` or `metadata_hash` | Mark retirement incomplete. Capability stays `RETIRE_PENDING`. |
| `RET-F003` | **DEGRADED** | Niche overlap conflict — two active tools occupy the same niche | Force one to `RETIRE_PENDING`. Sovereign selects which. |
| `RET-F004` | **FATAL** | Resurrection bypasses activation-energy steps | Deny transition to `PILOT`. Capability stays `RESURRECTION_PENDING`. |
| `RET-F005` | **COSMETIC** | Registry state drifts from ledger state | Nightly reconciliation: ledger is source of truth, registry is corrected. |

---

## Verification Contract

Five tests. All must pass for protocol compliance.

| Test ID | Description | Pass Condition |
|---------|-------------|----------------|
| `RET-T01` | Block activation without 2 retirements | `RATIO_PENDING` with 0 or 1 paired retirements cannot transition to `ACTIVE` |
| `RET-T02` | Allow activation with 2 completed archive events | `RATIO_PENDING` with 2 archived retirements in ledger transitions to `ACTIVE` |
| `RET-T03` | Enforce archive metadata completeness | Retirement without `restore_instructions` stays `RETIRE_PENDING` |
| `RET-T04` | Resurrection requires all 4 activation-energy artifacts | `RESURRECTION_PENDING` without all 4 cannot transition to `PILOT` |
| `RET-T05` | Niche uniqueness enforcement | Two capabilities with `status: active` and identical `niche` triggers `RET-F003` conflict event |

---

## Integration Points

| System | Integration |
|--------|-------------|
| Capability Registry (`ARCH-TOOL_NICHE_REGISTRY.yaml`) | Source of truth for capability status and niche assignments |
| Retirement Ledger (`DYN-RETIREMENT_LEDGER.jsonl`) | Append-only event log for all lifecycle transitions |
| Icebox Archive (`sources/icebox/`) | Destination for retired capability artifacts with restore metadata |
| Icebox Manifest (`sources/icebox/ICEBOX-MANIFEST.jsonl`) | Index of all archived capabilities |
| Apoptosis Protocol (`apoptosis_protocol.md`) | Governs canon axiom lifecycle — complementary, non-overlapping scope |
| Intention Compass (`ARCH-INTENTION_COMPASS.md`) | Retirement decisions may generate new intentions or resolve existing ones |
| Deferred Commitments (`DYN-DEFERRED_COMMITMENTS.md`) | Waiver events create deferred debt entries |
