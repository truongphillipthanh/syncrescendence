# Linear ↔ Repository Sync Protocol
## SYN-30 — Design Specification

**Version**: 1.0.0
**Created**: 2026-02-10
**Status**: DRAFT (awaiting Sovereign ratification)
**Linear**: SYN-30
**Related**: SYN-16 (IMPL-A-0012), PROJ-LINEAR
**Author**: Commander (COO)

---

## Architecture

```
                    ┌──────────────────────┐
                    │      SOVEREIGN       │
                    │   (Decision Gate)    │
                    └──────────┬───────────┘
                               │ ratify/override
                               ▼
┌───────────────┐    ┌──────────────────┐    ┌───────────────────┐
│   LINEAR      │◄──►│   SYNC ENGINE    │◄──►│   REPOSITORY      │
│   (T1a)       │    │  (CLI/launchd)   │    │   (Ground Truth)  │
├───────────────┤    ├──────────────────┤    ├───────────────────┤
│ SYN issues    │    │ linear_sync.py   │    │ DYN-BACKLOG.md    │
│ Projects      │    │ GraphQL API      │    │ DYN-PROJECTS.csv  │
│ Labels/States │    │ MCP Linear       │    │ IMPL-MAP.md       │
│ Comments      │    │ claudecron job    │    │ DYN-TASKS.csv     │
└───────────────┘    └──────────────────┘    └───────────────────┘
```

**Principle**: Repository is ground truth (Invariant #5). Linear is an execution surface, not a source of truth. Sync flows primarily repo → Linear, with Linear providing velocity data back.

---

## Data Flow Direction

### Tier 1: Repo → Linear (Authoritative Push)
| Repo Artifact | Linear Entity | Direction | Trigger |
|---------------|---------------|-----------|---------|
| DYN-PROJECTS.csv | Projects | repo → Linear | On CSV change |
| IMPLEMENTATION-MAP.md | Issues (IMPL→SYN) | repo → Linear | On IMPL status change |
| DYN-BACKLOG.md | Issue descriptions | repo → Linear | On backlog update |
| SOVEREIGN decisions | Issue state changes | repo → Linear | On SOVEREIGN resolution |

### Tier 2: Linear → Repo (Velocity Feedback)
| Linear Data | Repo Artifact | Direction | Trigger |
|-------------|---------------|-----------|---------|
| Issue state changes | DYN-BACKLOG.md notes | Linear → repo | Scheduled pull |
| New issues (ad-hoc) | IMPLEMENTATION-MAP.md | Linear → repo | Manual triage |
| Comments | agents/commander/inbox/ | Linear → repo | claudecron check |
| Cycle metrics | DYN-EXECUTION_STAGING.md | Linear → repo | Weekly pull |

### Tier 3: Bidirectional (Reconciliation)
| Entity | Resolution | Precedence |
|--------|-----------|------------|
| Issue status | Latest timestamp wins | Repo overrides on conflict |
| Issue description | Repo authoritative | Linear as draft surface |
| Priority labels | Linear authoritative | P0-P3 managed in Linear |
| Cycle/sprint data | Linear authoritative | Not tracked in repo |

---

## State Machine

```
                 ┌─────────────┐
                 │  IDENTIFIED  │  Source: IMPL-MAP entry, intention, ad-hoc
                 └──────┬──────┘
                        │ create_issue()
                        ▼
                 ┌─────────────┐
                 │  IN LINEAR   │  SYN-xxx issue exists, IMPL linked
                 └──────┬──────┘
                        │ sync_to_backlog()
                        ▼
                 ┌─────────────┐
                 │   TRACKED    │  In DYN-BACKLOG.md + Linear + IMPL-MAP
                 └──────┬──────┘
                        │ work begins
                        ▼
                 ┌─────────────┐
                 │ IN PROGRESS  │  Linear state = In Progress
                 └──────┬──────┘
                        │ work completes
                        ▼
                 ┌─────────────┐
                 │    DONE      │  Linear state = Done
                 │              │  IMPL status = done + notes
                 │              │  DYN-BACKLOG updated
                 └──────────────┘
```

---

## API Operations

### Read Operations (Linear → Local)
```python
# Get all open issues with status
query = """
{
  issues(filter: {
    team: {key: {eq: "SYN"}},
    state: {type: {nin: ["completed", "canceled"]}}
  }, first: 100) {
    nodes {
      number, title, priority, description
      state { name, type }
      labels { nodes { name } }
      project { name }
      updatedAt
    }
  }
}
"""
```

### Write Operations (Local → Linear)
```python
# Update issue state
mutation = """
mutation($id: String!, $stateId: String!) {
  issueUpdate(id: $id, input: { stateId: $stateId }) {
    success
  }
}
"""

# Update issue description (enrich from IMPL-MAP)
mutation = """
mutation($id: String!, $desc: String!) {
  issueUpdate(id: $id, input: { description: $desc }) {
    success
  }
}
"""
```

### Key IDs
| State | UUID |
|-------|------|
| Done | `4f15cb0a-a5a2-45e2-b441-05b468fedea1` |
| In Progress | `17db8a8b-46fd-4681-9703-ced64059738c` |
| Todo | `910fb97d-1954-4e7c-a6ed-8e43842eb372` |
| Backlog | `e4201e12-3448-459f-bdbc-e41a037c0bdb` |

---

## Sync Operations

### 1. `sync_status_to_linear` (repo → Linear)
**Trigger**: After IMPL-MAP status change or DYN-BACKLOG update
**Logic**:
1. Parse IMPL-MAP for entries with `linear_id` field
2. Compare IMPL `status` with Linear issue state
3. If IMPL `status: done` but Linear not Done → update Linear to Done
4. If IMPL `status: in_progress` but Linear not In Progress → update Linear
5. Log all changes to DYN-EXECUTION_STAGING.md

### 2. `sync_status_from_linear` (Linear → repo)
**Trigger**: claudecron scheduled job (07:00 daily)
**Logic**:
1. Query all non-Done SYN issues
2. Compare with DYN-BACKLOG.md project status
3. Flag discrepancies (Linear says Done but repo says active)
4. Write report to `agents/commander/inbox/TASK-linear-sync-report.md`
5. Do NOT auto-modify repo files — report only for Commander review

### 3. `reconcile_impl_map` (bidirectional)
**Trigger**: Manual command (`make linear-reconcile`)
**Logic**:
1. Query all SYN issues
2. Cross-reference with IMPL-MAP `linear_id` fields
3. Identify:
   - IMPL entries without Linear IDs (need creation)
   - Linear issues without IMPL entries (ad-hoc, need mapping)
   - Status mismatches
4. Generate reconciliation report
5. Optionally batch-create missing Linear issues

### 4. `enrich_linear_descriptions` (repo → Linear)
**Trigger**: Manual command (`make linear-enrich`)
**Logic**:
1. For each IMPL entry with `linear_id`
2. Build rich description from IMPL fields (intent, deliverable, dependencies, notes)
3. Push to Linear issue description
4. Skip if Linear description already richer (manual edits preserved)

---

## Conflict Resolution

| Scenario | Resolution |
|----------|-----------|
| Both changed status | Repo wins (Invariant #5) |
| Linear has richer description | Preserve Linear (human edits) |
| New issue in Linear without IMPL | Queue for manual IMPL creation |
| IMPL deleted, Linear exists | Leave Linear (mark stale) |
| Priority changed in Linear | Accept Linear priority (T1a authority) |

---

## Implementation Plan

### Phase 1: Read-Only Monitoring (Current)
- [x] Linear MCP LIVE (33 tools)
- [x] claudecron linear-check job (07:00)
- [x] Manual Python scripts for state updates
- [x] 19/176 IMPL→SYN bridge

### Phase 2: Automated Status Sync
- [ ] `linear_sync.py` script in `orchestration/scripts/`
- [ ] `make linear-sync` Makefile target
- [ ] claudecron integration (replace manual scripts)
- [ ] Reconciliation report format

### Phase 3: Full Bidirectional
- [ ] IMPL→Linear auto-creation for unmapped entries
- [ ] Linear→repo status feedback
- [ ] Description enrichment pipeline
- [ ] Cycle/sprint metrics extraction

### Phase 4: Real-Time (Aspirational)
- [ ] Webhook integration (Linear → n8n → repo)
- [ ] Auto-dispatch on state change
- [ ] Dashboard integration (SYN-40 JIT HighCommand)

---

## Sovereign Decision Points

1. **Unmapped IMPL entries (157)**: Batch-create Linear issues for all, or selective?
2. **Sync frequency**: Daily claudecron sufficient, or more frequent?
3. **Auto-commit**: Should sync script auto-commit backlog changes, or stage for review?
4. **Phase 2 priority**: Start immediately or after CLARESCE^3 v2?

---

## Makefile Targets

```makefile
linear-sync:     ## Sync IMPL-MAP status to Linear
	python3 orchestration/scripts/linear_sync.py --push

linear-pull:     ## Pull Linear status to report
	python3 orchestration/scripts/linear_sync.py --pull

linear-reconcile: ## Full reconciliation report
	python3 orchestration/scripts/linear_sync.py --reconcile

linear-enrich:   ## Enrich Linear issue descriptions from IMPL
	python3 orchestration/scripts/linear_sync.py --enrich
```

---

## Security

- API key sourced from `~/.syncrescendence/.env` (not in repo)
- Write operations require explicit `--push` flag (no accidental writes)
- All mutations logged to DYN-EXECUTION_STAGING.md
- Rate limiting: Linear API allows 1,500 requests/hour

---

*"The map is not the territory, but the bridge between maps must be maintained." — Sync Protocol axiom*
