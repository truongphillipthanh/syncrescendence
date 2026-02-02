# 00-ORCHESTRATION/state/

## Structure (FLAT)

All files at root level. Prefix conventions indicate category:

| Prefix | Category | Purpose | Mutability |
|--------|----------|---------|------------|
| `DYN-` | Dynamic | Real-time operational state | High (updates frequently) |
| `ARCH-` | Archaeology | Historical decisions, living frameworks | Append-only |
| `REF-` | Reference | Stable protocols and schemas | Low (deliberate updates only) |

## Files (21)

### Dynamic State (DYN-)
- `DYN-BACKLOG.md` — Operational backlog and project status
- `DYN-PROJECTS.csv` — Project registry
- `DYN-TASKS.csv` — Task tracking
- `DYN-SYSTEM_STATE.json` — System state snapshot
- `DYN-TWIN_COORDINATION_PROTOCOL.md` — Twin machine coordination

### Archaeological Records (ARCH-)
- `ARCH-INTENTION_COMPASS.md` — Sovereign intention archaeology (INT-MI entries)
- `ARCH-LIVE_CANON_TICKER.md` — Dynamic model/capability tracking design
- `ARCH-SOVEREIGNTY_STRATA.md` — Sovereignty strata framework

### Reference Documents (REF-) — Processing Pipeline
- `REF-PROCESSING_PATTERN.md` — Master source-to-synthesis workflow
- `REF-PROCESSING_ROUTING.md` — Function routing by platform/format
- `REF-TRIAGE_PROTOCOL.md` — Source qualification funnel
- `REF-SOURCES_SCHEMA.md` — Eight-dimensional source classification
- `REF-FOUR_SYSTEMS.md` — Four operational modes (Auto-Push, Curation, On-Demand, Triage)

### Reference Documents (REF-) — Standards and Governance
- `REF-STANDARDS.md` — 18 Evaluative Lenses (constitutional)
- `REF-DECISION_ATOMS.md` — Decision atom schema
- `REF-LENS_GOVERNANCE.md` — Lens application governance

### Reference Documents (REF-) — Operations
- `REF-NEO_BLITZKRIEG_BUILDOUT.md` — Active buildout protocol
- `REF-MULTI_ACCOUNT_SYNC.md` — PROJ-014 IIC synchronization
- `REF-REPO_VALIDATION_PROTOCOL.md` — Repository validation checks
- `REF-ONTOLOGY_REGISTRY.md` — PROJ-006 ontology proposal

## Sibling Directories

- `00-ORCHESTRATION/archive/` — 9 files (compacted wisdom, deep references)
- `00-ORCHESTRATION/scripts/` — Operational scripts and automation
