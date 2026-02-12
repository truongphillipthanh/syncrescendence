# DYN-GLOBAL_LEDGER.md
## Append-Only Event Log for Task Lifecycle + Sovereign Decisions

**Created**: 2026-02-06
**Protocol**: Append only. Never edit existing entries. One entry per event.
**Script**: `00-ORCHESTRATION/scripts/append_ledger.sh`

---

## Schema

```
| Timestamp | Event | From | To | Task ID | Fingerprint | Commit | DecisionAtom | IntentionLink |
```

- **Timestamp**: ISO 8601 (YYYY-MM-DDTHH:MM:SS)
- **Event**: DISPATCH | CLAIM | COMPLETE | FAILED | DECISION | COMPACT | REGEN
- **From**: Originating agent or Sovereign
- **To**: Target agent or platform
- **Task ID**: TASK filename (without path)
- **Fingerprint**: Git short hash at event time
- **Commit**: Commit hash if event produced a commit (else `—`)
- **DecisionAtom**: Reference to REF-DECISION_ATOMS.md entry (if applicable)
- **IntentionLink**: Reference to ARCH-INTENTION_COMPASS.md entry (if applicable)

---

## Ledger

| Timestamp | Event | From | To | Task ID | Fingerprint | Commit | DecisionAtom | IntentionLink |
|-----------|-------|------|----|---------|-------------|--------|--------------|---------------|
| 2026-02-12T02:14:38 | COMMIT | commander | repo | fix(DA-09): correct stale state — COCKPIT watcher, BACKLOG PROJ-006b, MEMORY.m | 6b519e7 | 6b519e7 | — | — |
| 2026-02-12T02:14:59 | COMMIT | commander | repo | feat(DA-10,INT-MI19): ontology strategic enrichment — 29→142 records, 20 que | ba2c836 | ba2c836 | — | — |
| 2026-02-12T02:15:09 | COMMIT | commander | repo | chore: sync operational state — dispatch artifacts, DYN hooks, Adjudicator tas | 2a8148e | 2a8148e | — | — |
