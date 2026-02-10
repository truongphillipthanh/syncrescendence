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
| 2026-02-10T07:52:49 | COMPLETE | cartographer | — | TASK-20260209-claresce3v2_pass1_scaffold_audit.md | 3e301bf | 3e301bf | — | — |
| 2026-02-10T07:58:44 | DISPATCH | dispatch | cartographer | TASK-20260209-claresce3v2_pass2_canon_coherence.md | c197198 | c197198 | — | — |
| 2026-02-10T07:58:45 | CLAIM | cartographer | cartographer | TASK-20260209-claresce3v2_pass2_canon_coherence.md | c197198 | c197198 | — | — |
| 2026-02-10T07:58:48 | DISPATCH | dispatch | adjudicator | TASK-20260209-claresce3v2_pass2_canon_standards.md | c197198 | c197198 | — | — |
| 2026-02-10T07:59:18 | COMPLETE | adjudicator | — | TASK-20260209-claresce3v2_pass2_canon_standards.md | c197198 | c197198 | — | — |
| 2026-02-10T07:59:37 | COMPLETE | cartographer | — | TASK-20260209-claresce3v2_pass2_canon_coherence.md | c197198 | c197198 | — | — |
