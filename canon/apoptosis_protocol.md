---
id: CANON-APOPTOSIS-PROTOCOL
canonical_name: Apoptosis Protocol — 5:1 Nucleosynthesis Ratio
title: "Apoptosis Protocol — 5:1 Nucleosynthesis Ratio"

tier: chain
chain: null
celestial_type: policy
volatility_band: stable
refresh_cadence: semi-annual

parent: null
requires: []
siblings: []
synthesizes: []

status: canonical
operational_status: operational
version: 1.0.0
created: 2026-02-26
updated: 2026-02-26
last_verified: 2026-02-26

element: null
ooda_phase: null
volatile_sections: []
entities_defined:
  - "5:1 Nucleosynthesis Ratio (CON)"
  - "Tombstone Schema (STR)"
  - "Recycling Schema (STR)"
  - "Young-System Exception (PROTO)"
  - "Apoptosis State Machine (STR)"
  - "Apoptosis Failure Modes (REF)"
  - "Apoptosis Verification Contract (PROTO)"
---
# CANON-APOPTOSIS-PROTOCOL: APOPTOSIS PROTOCOL

## 5:1 Nucleosynthesis Ratio for Canon Axioms

> **Date**: February 26, 2026
> **Status**: Canonical Policy
> **Source**: Adjudicator Engineering Spec (Deliverable 3)

---

## 1. Purpose

Stars that accumulate mass without fusion collapse under their own gravity. Canon is no exception. Every axiom admitted without a corresponding fusion evaluation adds mass without releasing binding energy. This protocol enforces a constitutional nucleosynthesis ratio: for every 5 atoms condensed into canon, 1 existing axiom or sutra must be re-evaluated and either fused into a denser successor, retired as spent fuel, or explicitly reaffirmed as load-bearing.

This is the **stellar nucleosynthesis** of the canon — 5 atoms condense into 1 denser axiom, releasing epistemic binding energy (reduced fragmentation, freed context, resolved contradictions). The canon is a stellar core, not a garden.

### Enforcement Scope

This protocol governs **canon axioms and sutras ONLY**. Tools, platforms, backlogs, and operational infrastructure are governed by `retirement_protocol.md` (separate document). Do not conflate the two scopes.

---

## 2. Ratio Rule

**Core invariant**: For every 5 atoms condensed into canon, 1 existing axiom/sutra must undergo fusion evaluation — to be fused into a denser successor, retired as spent fuel, or reaffirmed.

```
retirements_required = floor(new_axioms_promoted / 5)
```

- **Accounting window**: Rolling. Promotions accumulate across sessions until the threshold fires.
- **Trigger events**:
  - `promotion_batch_close` — canonical trigger, fires when a promotion batch is committed.
  - `weekly_backstop_audit` — safety net, fires weekly regardless of promotion activity to catch drift.

The ratio is a **floor**, not a ceiling. More frequent fusion evaluations are welcome. The protocol enforces a minimum, not a maximum.

---

## 3. State Machine

```
                    ┌──────────────────────────────┐
                    │                              │
                    ▼                              │
               NOT_DUE ──────────► DUE            │
           (promotions < 5)   (promotions % 5 == 0)│
                    ▲                  │           │
                    │                  ▼           │
                    │          CANDIDATE_SCAN      │
                    │           /          \       │
                    │          ▼            ▼      │
                    │  RETIREMENT    WAIVED        │
                    │  _EXECUTED     (no candidates)│
                    │      │           │           │
                    │      │      ┌────┴────┐     │
                    │      │      │         │     │
                    │      │  debt ≤ 2   debt > 2 │
                    │      │      │         │     │
                    │      ▼      ▼         ▼     │
                    └── NOT_DUE  NOT_DUE  DEBT_LOCK
                                          (FATAL)
```

### State Transitions

| From | To | Condition |
|------|----|-----------|
| `NOT_DUE` | `DUE` | `new_axioms_promoted % 5 == 0` |
| `DUE` | `CANDIDATE_SCAN` | Automatic on entering DUE |
| `CANDIDATE_SCAN` | `RETIREMENT_EXECUTED` | >= 1 qualified candidate retired |
| `CANDIDATE_SCAN` | `WAIVED` | No candidate qualifies for retirement |
| `RETIREMENT_EXECUTED` | `NOT_DUE` | Cycle complete |
| `WAIVED` | `NOT_DUE` | `apoptosis_debt <= 2` |
| `WAIVED` | `DEBT_LOCK` | `apoptosis_debt > 2` |

### Terminal States Per Cycle

| State | Meaning |
|-------|---------|
| `COMPLIANT` | Retirement executed successfully |
| `WAIVED` | Young-system exception applied, debt incremented |
| `NONCOMPLIANT` | `DEBT_LOCK` or `FAILED` — all new promotions blocked |

---

## 4. State Ledgers

### Operational Ledgers

| Ledger | Path | Format |
|--------|------|--------|
| Apoptosis Ledger | `orchestration/00-ORCHESTRATION/state/DYN-APOPTOSIS_LEDGER.jsonl` | Append-only JSONL, one record per cycle |
| Apoptosis Debt | `orchestration/00-ORCHESTRATION/state/DYN-APOPTOSIS_DEBT.json` | Single JSON object tracking current debt state |

### Canonical Trace

| Ledger | Path | Format |
|--------|------|--------|
| Tombstones | `canon/01-CANON/CANON-APOPTOSIS_TOMBSTONES.sn.md` | Human-readable markdown with structured tombstone records |

---

## 5. Tombstone Schema

Every retired artifact receives exactly one tombstone record. Tombstones are permanent — they are never deleted, only appended.

```jsonc
{
  "tombstone_id": "TOMB-XXXX",            // Sequential identifier
  "retired_artifact_id": "CANON-NNNNN",   // ID of the retired canon artifact
  "retired_artifact_path": "canon/01-CANON/...",  // Full path at time of retirement
  "retired_at": "2026-02-26T00:00:00Z",   // ISO 8601 timestamp
  "reason_class": "merged",               // enum: merged | redundant | falsified | superseded
  "successor_ids": ["CANON-NNNNN"],       // Array of successor artifact IDs (may be empty)
  "redirect_to": "CANON-NNNNN",           // Primary successor for reference lookups (null if none)
  "retained_insights": [                   // Insights extracted before retirement
    "Insight text preserved verbatim"
  ],
  "falsified_claims": [                    // Claims proven wrong (reason_class = falsified)
    "Claim text that was disproven"
  ],
  "triggered_by_batch": "BATCH-CC34-001"   // Promotion batch that triggered this retirement
}
```

### Reason Classes

| Class | Meaning | Requires |
|-------|---------|----------|
| `merged` | Content absorbed into another axiom | `successor_ids` non-empty |
| `redundant` | Duplicates existing axiom with no unique value | `redirect_to` non-null |
| `falsified` | Claims proven incorrect by evidence | `falsified_claims` non-empty |
| `superseded` | Replaced by a strictly better formulation | `successor_ids` non-empty |

---

## 6. Recycling Schema

Epistemic binding energy released during fusion is tracked separately to ensure no knowledge is silently lost.

```jsonc
{
  "recycle_record_id": "RECY-XXXX",        // Sequential identifier
  "tombstone_id": "TOMB-XXXX",             // Parent tombstone
  "insight_text": "The extracted insight",  // Verbatim preserved insight
  "destination": "successor_axiom",         // enum: successor_axiom | lattice_note | deferred_queue
  "destination_ref": "CANON-NNNNN",        // Where the insight was routed
  "status": "integrated"                    // enum: integrated | pending | rejected
}
```

### Destination Types

| Destination | Meaning |
|-------------|---------|
| `successor_axiom` | Insight folded into the successor artifact |
| `lattice_note` | Insight preserved as a lattice annotation (no axiom home) |
| `deferred_queue` | Insight requires further evaluation before placement |

---

## 7. Young-System Exception

A new canon system may not yet have fusion candidates — the stellar core has not accumulated enough mass for ignition. The protocol accounts for this without disabling enforcement.

### Condition

`retirable_candidates == 0` — no existing axiom qualifies for retirement evaluation (system too young, all axioms still load-bearing with no redundancy).

### Behavior

- State transitions to `WAIVED`.
- `apoptosis_debt` incremented by 1.
- Cycle logged with `reason: young_system_waiver`.

### Hard Lock

```
if apoptosis_debt > 2:
    state = DEBT_LOCK
    # ALL new canon promotions BLOCKED until debt cleared
```

Three consecutive waivers without a single fusion triggers `DEBT_LOCK`. This prevents indefinite mass accumulation under the excuse of system youth. At some point, the core is massive enough to fuse — it is avoiding ignition.

**Clearing debt**: Each retirement executed decrements `apoptosis_debt` by 1. Debt must reach 0 before `DEBT_LOCK` is lifted.

---

## 8. Failure Modes

| ID | Severity | Condition | Effect |
|----|----------|-----------|--------|
| `APO-F001` | **FATAL** | 5:1 ratio violated with no waiver | Block all new canon promotions |
| `APO-F002` | **FATAL** | Tombstone missing redirect or metadata | Reject the retirement commit |
| `APO-F003` | **DEGRADED** | Young-system repeated waivers (debt > 2) | Enforce debt lock |
| `APO-F004` | **FATAL** | Retirement breaks downstream lattice dependencies | Rollback retirement OR attach successor mapping before proceeding |
| `APO-F005` | **COSMETIC** | Tombstone markdown out of sync with JSON ledger | Regenerate markdown from JSONL source |

### Failure Handling

- **APO-F001**: No bypass. The ratio is constitutional. Clear the retirement debt before promoting.
- **APO-F002**: Commit hook rejects incomplete tombstones. Fix metadata, re-commit.
- **APO-F003**: System alert. Sovereign must either identify retirement candidates or explicitly reaffirm all existing axioms (reaffirmation counts as evaluation, not retirement).
- **APO-F004**: Check `dependent_node_ids` before retiring. If dependents exist, either map them to successors or defer the retirement.
- **APO-F005**: Non-blocking. Regeneration script reconciles markdown from the JSONL ledger (JSONL is source of truth).

---

## 9. Verification Contract

Five tests constitute the verification contract for this protocol. All must pass for the protocol to be considered operational.

| Test ID | Description | Assertion |
|---------|-------------|-----------|
| `APO-T01` | No enforcement before 5 promotions | Promoting axioms 1-4 does not trigger retirement evaluation |
| `APO-T02` | Enforce on 5th promotion with tombstone | 5th promotion triggers `DUE` state; cycle does not complete without a tombstone written or waiver logged |
| `APO-T03` | Young-system waiver when no candidates | If `CANDIDATE_SCAN` finds 0 retirable candidates, state transitions to `WAIVED` and debt increments |
| `APO-T04` | Debt lock after 3 consecutive waivers | After 3 waivers with 0 retirements, `apoptosis_debt == 3`, state = `DEBT_LOCK`, new promotions rejected |
| `APO-T05` | Reanneal triggered on retirement | Retiring an axiom with `dependent_node_ids` queues each dependent into `lattice_annealer.py --mode reanneal` |

---

## 10. Integration with lattice_annealer

Fusion is not an isolated event. Condensing an axiom into a denser successor may shift downstream dependencies. The nucleosynthesis protocol integrates with the lattice annealer to ensure structural coherence.

### Retirement Emission

When an axiom is retired, the tombstone emits `dependent_node_ids` — the set of lattice nodes that reference the retired artifact.

### Reanneal Queue

Each dependent node is queued into:

```bash
lattice_annealer.py --mode reanneal --node <dependent_node_id>
```

The reanneal evaluates whether the dependent node:
- Can redirect to the successor axiom (automatic if `redirect_to` is set).
- Requires manual review (queued for Sovereign evaluation).
- Is itself a fusion candidate (recursive nucleosynthesis).

### Promotion Block During Reanneal

**New promotions are blocked while the dependent reanneal queue contains fatal items.** A fatal reanneal item is one where no successor mapping exists and the dependent node cannot stand alone. This prevents the lattice from accumulating broken references — unresolved fusion byproducts that destabilize the core.

---

## 11. Lock Order

Concurrent operations on canon, apoptosis ledgers, and the reanneal queue must acquire locks in the following order to prevent deadlocks:

```
LOCK_CANON_PROMOTION → LOCK_APOPTOSIS_LEDGER → LOCK_LATTICE_REANNEAL_QUEUE
```

- **LOCK_CANON_PROMOTION**: Acquired before writing any new axiom to canon.
- **LOCK_APOPTOSIS_LEDGER**: Acquired before updating the apoptosis ledger or debt tracker.
- **LOCK_LATTICE_REANNEAL_QUEUE**: Acquired before modifying the reanneal queue.

Acquiring locks out of order is a protocol violation. If a lower lock is needed without the higher lock, the operation must release and reacquire in the correct order.

---

## 12. Operational Summary

```
Condense 5 atoms  →  Evaluate 1 existing  →  Fuse / Retire / Reaffirm
                            │
                   No candidates? → WAIVE (debt + 1)
                            │
                   Debt > 2? → LOCK all promotions
                            │
                   Fusion executed? → Emit dependents → Reanneal → Clear
```

The canon condenses. The canon fuses. The ratio holds. This is nucleosynthesis.
