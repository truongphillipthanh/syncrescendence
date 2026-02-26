# Ascertescence Incident Taxonomy
**Version**: 1.0.0
**Authority**: Adjudicator Specification S7 (CC35)
**Status**: operational
**Generated**: 2026-02-26

---

## Incident Classes

| Class | Description | Example |
|-------|-------------|---------|
| race | Concurrent access to shared state | Apoptosis + annealer on same node |
| cascade | Failure in one deliverable triggers failures in others | High gate rejects inflate DAG tension |
| deadlock | Two deliverables waiting on each other | Annealer needs model bandwidth during constrained day |
| starvation | Valid inputs systematically rejected | Dynamic threshold too strict (autoimmune) |
| integrity | Data corruption or missing references | Tombstone redirect target missing |
| observability | Logging/monitoring gaps | Partial logging causes inconsistent triage |

---

## Severity Levels

- **FATAL**: System cannot proceed safely. Requires immediate halt + recovery.
- **DEGRADED**: System continues with reduced capability. Requires attention within 24h.
- **COSMETIC**: No operational impact. Fix at convenience.

---

## Canonical Cross-Deliverable Failure IDs

| ID | Severity | Interaction | Detection | Recovery | Prevention |
|----|----------|-------------|-----------|----------|------------|
| XFM-RACE-001 | FATAL | Apoptosis retires node while annealer scoring candidate edge to same node | annealer index version mismatch | abort anneal, refresh index, rerun | lock order LOCK_CANON_PROMOTION -> LOCK_LATTICE_INDEX |
| XFM-RACE-002 | DEGRADED | Tension monitor and gate v2 write conflicting DAG signal timestamps | duplicate run id | keep first write, second retries with backoff | single-writer signal lock |
| XFM-CASCADE-001 | DEGRADED | Tension monitor fires during constrained stress-test day | FIRE + constrained_day=true | emergency override path; annotate exception | stress multiplier on threshold during test |
| XFM-CASCADE-002 | FATAL | High gate rejects inflate DAG tension causing perpetual FIRE loop | FIRE frequency > max | enter cooldown hard-stop; require threshold audit | max fires/day cap + hysteresis |
| XFM-DEADLOCK-001 | FATAL | Annealer requests ADJUST but no model bandwidth in constrained day | repair queue age > SLA | defer candidate, mark blocked, auto-retry next window | repair budget reserved in stress config |
| XFM-DEADLOCK-002 | FATAL | Retirement ratio blocks new capability while stress test needs emergency replacement | activation blocked + critical dep missing | sovereign emergency waiver with expiry | reserved emergency capability class |
| XFM-STARVE-001 | DEGRADED | Dynamic threshold too strict despite high coherence (autoimmune) | reject rate >35% and coherence>0.8 | lower threshold within clamp + re-evaluate | threshold guardrails + weekly calibration |
| XFM-INTEGRITY-001 | FATAL | Tombstone exists but redirect target missing | redirect resolution fail | rollback retirement or create successor placeholder | pre-commit redirect validator |
| XFM-OBS-001 | COSMETIC | Partial logging causes inconsistent incident triage | expected log count mismatch | reconstruct from primary JSON logs | schema-validated appenders |

---

## Per-Deliverable Failure IDs

Each deliverable maintains its own failure registry. Cross-deliverable failures (XFM-*) above are the interaction points between them.

| Deliverable | Component | Failure ID Range |
|-------------|-----------|-----------------|
| D1 | dag_tension_monitor | DTM-F001 through DTM-F006 |
| D2 | lattice_annealer | LAN-F001 through LAN-F006 |
| D3 | apoptosis_protocol | APO-F001 through APO-F005 |
| D4 | retirement_protocol | RET-F001 through RET-F005 |
| D5 | stress_test_sim | STR-F001 through STR-F005 |
| D6 | ontology_gate_v2 | GAT-F001 through GAT-F005 |

---

## State Machine for Incidents

```
DETECTED -> TRIAGED -> MITIGATING -> RESOLVED -> CLOSED
                                  \-> ESCALATED -> CLOSED
```

**Transitions**:
- DETECTED: Automated detection rule fires or manual report filed.
- TRIAGED: Severity and class assigned. Owner identified.
- MITIGATING: Active recovery underway.
- RESOLVED: Recovery complete. Artifact committed.
- ESCALATED: Severity exceeded owner authority. Sovereign or Adjudicator required.
- CLOSED: Post-mortem filed. Prevention control verified or updated.

---

## Global Lock Hierarchy Reference

See `ARCH-LOCK_HIERARCHY.yaml` for full specification. Summary of the 10-level ordering:

| Level | Lock Name |
|-------|-----------|
| 1 | LOCK_CANON_PROMOTION |
| 2 | LOCK_LATTICE_INDEX |
| 3 | LOCK_DAG_SIGNAL |
| 4 | LOCK_TENSION_MONITOR |
| 5 | LOCK_ANNEALER_STATE |
| 6 | LOCK_APOPTOSIS_QUEUE |
| 7 | LOCK_RETIREMENT_LEDGER |
| 8 | LOCK_STRESS_CONFIG |
| 9 | LOCK_GATE_THRESHOLD |
| 10 | LOCK_INCIDENT_LOG |

**Rule**: Always acquire locks in ascending level order. Never hold a higher-numbered lock while requesting a lower-numbered one. Violation of this ordering is the root cause of XFM-RACE-001.

---

## Chaos Test Suite

| Test ID | Inject | Expect |
|---------|--------|--------|
| XFM-T01 | Kill annealer mid-scoring while apoptosis retires target node | XFM-RACE-001 detected; anneal aborted and restarted cleanly |
| XFM-T02 | Flood gate v2 with reject decisions to inflate DAG tension | XFM-CASCADE-002 detected; cooldown hard-stop engages before loop threshold |
| XFM-T03 | Set constrained_day=true then trigger annealer ADJUST request | XFM-DEADLOCK-001 detected; candidate deferred, not stuck |
| XFM-T04 | Set dynamic threshold to reject >50% while coherence is 0.9 | XFM-STARVE-001 detected; threshold auto-corrects within clamp bounds |
| XFM-T05 | Delete tombstone redirect target after retirement completes | XFM-INTEGRITY-001 detected; rollback or placeholder created before next read |

---

## Falsification Criteria

An incident taxonomy is operationally valid only if the following never occur without being caught:

1. **Any deadlock with no timeout and no escalation record.** If a DEADLOCK-class incident persists beyond its SLA window without transitioning to ESCALATED, the taxonomy has failed to enforce its own state machine.

2. **Any FATAL incident resolved without a recovery artifact.** Every FATAL -> RESOLVED transition must produce a committed artifact (log, rollback record, or post-mortem). Resolution without evidence is indistinguishable from suppression.
