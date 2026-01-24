# REF-METHODOLOGY
## Sprint-Bounded Kanban with Review/Retrospective Separation

**Version**: 1.0
**Adopted**: Oracle 11 (2026-01-09)

---

## Framework Overview

Syncrescendence adopts a hybrid methodology synthesized from Scrum, Kanban, XP, and Lean principles:

| Component | Source | Implementation |
|-----------|--------|----------------|
| Sprint boundaries | Scrum | Oracle sessions = Sprint |
| Kanban visualization | Kanban | Ledger-based flow tracking |
| Atomic feedback | XP | make verify + TDD-like ledger checks |
| Continuous improvement | Lean/Kaizen | Built into Oracle transitions |

---

## Structural Mapping

```
ORACLE SESSION = Sprint
├── BLITZKRIEG = Sprint Increment
│   └── Parallel A/B streams (XP-like pairing concept)
├── ORACLE CONTEXT VERSIONING = Continuous Documentation
├── ORACLE CULMINATION = Sprint Review (product validation)
└── ORACLE INIT (next) = Sprint Retrospective (process optimization)
```

---

## Review vs Retrospective

### Sprint Review (Oracle Culmination)
**Function**: Product validation - "Are we building the right thing?"
**Focus**: Deliverables, outcomes, CANON quality
**Participants**: Sovereign + Oracle
**Output**: Updated backlog, validated deliverables

### Sprint Retrospective (Oracle Init)
**Function**: Process optimization - "Are we building it right?"
**Focus**: Methodology, efficiency, bottleneck removal
**Participants**: Sovereign + Oracle (informed by execution logs)
**Output**: Process improvements, methodology refinements

---

## Operational Cadence

### Daily (When Active)
- Blitzkrieg execution
- Ledger updates
- make verify before commits

### Per-Blitzkrieg
- Parallel A/B execution
- Execution log creation
- Context versioning

### Per-Oracle
- Culmination (Review)
- Init (Retrospective)
- Backlog refinement

### Quarterly
- 18-lens strategic review
- Project prioritization
- Chain development assessment

---

## 18-Lens Integration

All significant decisions evaluated against 18 lenses. Key lenses for methodology:

| Lens | Methodology Implication |
|------|------------------------|
| #12 Industrial Engineering | Identifies bottleneck (Sovereign relay) |
| #14 Permaculture | Self-sustaining patterns via automation |
| #16 Agile | Minimum viable increments |
| #17 Lean | Waste elimination |

---

## Feedback Granularity

| Type | Frequency | Trigger |
|------|-----------|---------|
| Atomic (ledger check) | Per commit | make verify |
| Incremental (blitzkrieg) | Per directive | Execution log |
| Sprint (Oracle) | Per session | Culmination + Init |
| Strategic (18-lens) | Quarterly | Review session |

---

*Adopted Oracle 11 | Source: additions.md synthesis + 18-lens evaluation*
