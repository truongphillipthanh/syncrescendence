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
- **Event**: DISPATCH | CLAIM | COMPLETE | FAILED | DECISION
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
| 2026-02-06T00:00:00 | DISPATCH | system | — | DYN-GLOBAL_LEDGER.md | — | — | — | — |
| 2026-02-02T22:45:21 | DECISION | sovereign | commander | SOVEREIGN-008 | 64de3f4 | 64de3f4 | — | INT-1202 |
| 2026-02-02T22:46:04 | COMPLETE | commander | sovereign | TASK-20260206-sovereign008-approval.md | 64de3f4 | 64de3f4 | — | — |
| 2026-02-02T22:46:04 | COMPLETE | commander | sovereign | TASK-20260206-outgoing-bypass-question.md | 64de3f4 | 64de3f4 | — | — |
| 2026-02-02T22:46:04 | COMPLETE | commander | sovereign | TASK-20260206-io_model_v2_and_claim_locking.md | 64de3f4 | 64de3f4 | — | INT-1202 |
