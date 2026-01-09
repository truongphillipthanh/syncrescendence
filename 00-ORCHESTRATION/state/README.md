# 00-ORCHESTRATION/state/

## Structure (FLAT)

All files are at root level. Prefix conventions indicate category:

| Prefix | Category | Purpose | Mutability |
|--------|----------|---------|------------|
| `DYN-` | Dynamic | Real-time operational state | High (updates frequently) |
| `ARCH-` | Archaeology | Historical decisions and characteristics | Frozen (append-only) |
| `REF-` | Reference | Stable protocols and schemas | Low (deliberate updates only) |
| *(none)* | Ledgers | CSV mechanical tracking | Medium (task/sprint updates) |

## Files

### Dynamic State (DYN-)
- `DYN-ACTUAL_TREE.md` — Current repository tree structure
- `DYN-BACKLOG.md` — Pending work items
- `DYN-DASHBOARD.md` — Operational status dashboard

### Archaeological Records (ARCH-)
- `ARCH-CRYSTALLINE_CHARACTERISTICS.md` — System identity characteristics
- `ARCH-DESIGN_DECISIONS.md` — Documented design decisions
- `ARCH-ORACLE_ARC_SUMMARY.md` — Oracle history summary
- `ARCH-ORACLE_DECISIONS.md` — Key decisions per Oracle

### Reference Documents (REF-)
- `REF-FOUR_SYSTEMS.md` — Four systems framework
- `REF-PROCESSING_PATTERN.md` — Source processing patterns
- `REF-PROCESSING_ROUTING.md` — Content routing decisions
- `REF-QUEUE_ROADMAP_MAPPING.md` — Queue to roadmap mapping
- `REF-SOURCES_SCHEMA.md` — Sources metadata schema
- `REF-STANDARDS.md` — Quality standards
- `REF-TRIAGE_PROTOCOL.md` — Triage decision protocol

### Ledgers (CSV)
- `burndown.csv` — Sprint burndown tracking
- `projects.csv` — Project registry
- `sprints.csv` — Sprint definitions
- `tasks.csv` — Task tracking

## Note

Oracle contexts are in `00-ORCHESTRATION/oracle_contexts/` as peer directory.
Directives and execution logs are also peer directories at 00-ORCHESTRATION/ level.
