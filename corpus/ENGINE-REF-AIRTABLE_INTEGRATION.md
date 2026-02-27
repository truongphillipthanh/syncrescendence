# REF -- Airtable Ontology Surface Integration

## Visual Surface for the Syncrescendence Ontology (INT-MI19)

**Version**: 1.1.0
**Created**: 2026-02-10 | **Updated**: 2026-02-12
**Author**: airtable-onboarder agent (Opus 4.6)
**Linear Issue**: SYN-55
**Intention**: INT-MI19 (Palantir-like ontology) -- FINAL BOSS

---

## I. ACCOUNT STRUCTURE

| Property | Value |
|----------|-------|
| Account Email | truongphillipthanh@icloud.com |
| User ID | usrt0h6qVbteFamIB |
| API Endpoint | `https://api.airtable.com/v0/` |
| Auth Method | Bearer token (Personal Access Token) |
| Env Variable | `AIRTABLE_API_KEY` in `~/.syncrescendence/.env` |
| Token Prefix | `patU0h...` (82 chars) |
| Permission Level | `create` on all bases |

### Existing Bases

| Base ID | Name | Purpose |
|---------|------|---------|
| `appHyxiH0s9zOYH8I` | **Syncrescendence Ontology** (was "Airtable") | Ontology visual surface -- PRIMARY |
| `appdfOwqwnEkfHChk` | My Art Collection | Pre-existing (unrelated) |
| `appMbYkN1gzAcd6vg` | Indie Film Production | Pre-existing (unrelated) |
| `app6VLp2tjZzZBE2A` | PR & Media Lists | Pre-existing (unrelated) |

### API Limitations (Free Tier)

- 5 API requests per second per base
- 100 records per page (paginated with `offset`)
- 10 records per batch create/update
- No workspace ID API for non-enterprise (blocks base creation via API; must use existing bases or create in UI)
- Personal Access Token scopes control table read/write/create

---

## II. BASE SCHEMA -- Syncrescendence Ontology

**Base ID**: `appHyxiH0s9zOYH8I`

### Table: Platforms (`tbl2bifSCiHt8WtFX`)

Maps to: `ontology.db` -> `apps` table (126 records seeded)

| Field | Type | Description |
|-------|------|-------------|
| Name | singleLineText | Platform display name (primary) |
| Slug | singleLineText | URL-friendly identifier (vendor-product-surface) |
| Description | multilineText | Brief functional description |
| ASA Layer | singleSelect | L0-L6 ASA Model classification |
| Object Type | singleSelect | O.FN, O.SVC, O.WF, O.AGT, O.MOD, O.DP, O.SRF, O.INS, O.GRD, O.EVL, O.CPL |
| Lifecycle | singleSelect | experimental, active, primitive_repository, deprecated, archived |
| Stage | singleSelect | ACTIVE, EVALUATING, DORMANT, DEPRECATED |
| URL | url | Official platform URL |
| SQLite ID | number | FK to `apps.id` in ontology.db |

### Table: Models (`tbl7J4p9Qm410p4f4`)

Maps to: `ontology.db` -> `models` table (20 records seeded)

| Field | Type | Description |
|-------|------|-------------|
| Name | singleLineText | Model display name (primary) |
| API Name | singleLineText | API identifier (e.g. claude-opus-4-6) |
| Family | singleSelect | claude, gpt, o-series, gemini, llama, kimi, deepseek, grok |
| Research Lab | singleLineText | Anthropic, OpenAI, Google DeepMind, etc. |
| Context Window | number | Max tokens |
| Vision | checkbox | Supports image input |
| Extended Thinking | checkbox | Has CoT/extended thinking mode |
| SQLite ID | number | FK to `models.id` in ontology.db |

### Table: CANON Registry (`tblUV1j8L5it0kugg`)

Maps to: `ontology.db` -> `sources` table (100 of 184 records seeded)

| Field | Type | Description |
|-------|------|-------------|
| CANON ID | singleLineText | Source identifier (primary) |
| Title | singleLineText | Document title |
| Chain | singleSelect | INTELLIGENCE, CREATIVE, PROFESSIONAL, PERSONAL, FINANCIAL, INFRASTRUCTURE |
| Platform | singleLineText | Source platform (youtube, podcast, etc.) |
| Status | singleSelect | canonical, processed, raw, pending |
| Signal Tier | singleLineText | S1-S5 signal quality |

### Table: Intentions (`tbl2LQ50S7phz7oiW`)

Maps to: `ARCH-INTENTION_COMPASS.md` (manual population required)

| Field | Type | Description |
|-------|------|-------------|
| Intention ID | singleLineText | e.g. INT-1202, INT-MI19 (primary) |
| Text | multilineText | Full intention text |
| Category | singleSelect | strategic, operational, technical, personal |
| Priority | singleSelect | P0, P1, P2, P3 |
| SYN Link | singleLineText | Linked Linear issue (e.g. SYN-55) |
| Status | singleSelect | active, hibernating, achieved |

### Table: Projects (`tblH4NpzpwjaYW5Ms`)

Maps to: `ontology.db` -> `projects` table (30 records seeded)

| Field | Type | Description |
|-------|------|-------------|
| Project ID | singleLineText | e.g. PROJ-006 (primary) |
| Name | singleLineText | Project name |
| Status | singleSelect | not_started, active, in_progress, blocked, complete |
| Priority | singleSelect | P0, P1, P2, P3 |
| Owner | singleLineText | Responsible agent/person |
| Notes | multilineText | Project notes |

### Table: Commitments (`tblknyyoArt1OsHVR`)

Maps to: `ontology.db` -> `commitments` table (15 records seeded 2026-02-12)

| Field | Type | Description |
|-------|------|-------------|
| Code | singleLineText | CMT-001 through CMT-015 (primary) |
| Name | singleLineText | Commitment description |
| Stakeholder | singleSelect | Sovereign, System, Commander |
| Status | singleSelect | active, failed, achieved |
| Intention Link | singleLineText | e.g. INT-MI19 |
| Deadline | singleLineText | Target date or "this_week" |
| Notes | multilineText | Additional context |

### Table: Goals (`tblOnR3CW0MRkSRLm`)

Maps to: `ontology.db` -> `goals` table (12 records seeded 2026-02-12)

| Field | Type | Description |
|-------|------|-------------|
| Code | singleLineText | GOL-001 through GOL-012 (primary) |
| Name | singleLineText | Goal description |
| Status | singleSelect | active, blocked, partial, deferred, achieved |
| Intention Link | singleLineText | Linked intention |
| Notes | multilineText | Additional context |

### Table: Risks (`tblLSZby7G12lQ7qJ`)

Maps to: `ontology.db` -> `risks` table (15 records seeded 2026-02-12)

| Field | Type | Description |
|-------|------|-------------|
| Code | singleLineText | RSK-001 through RSK-015 (primary) |
| Name | singleLineText | Risk description |
| Category | singleSelect | economic, operational, strategic, dependency |
| Probability | singleSelect | very_low, low, medium, high, certain |
| Impact | singleSelect | low, medium, high, critical, catastrophic |
| Mitigation | multilineText | Mitigation strategy |
| Notes | multilineText | Additional context |

### Seeding Summary

| Table | Records Seeded | Source | Date |
|-------|---------------|--------|------|
| Platforms | 126 | ontology.db apps | 2026-02-10 |
| Models | 20 | ontology.db models | 2026-02-10 |
| CANON Registry | 179 | ontology.db sources | 2026-02-10 |
| Intentions | 84 | ARCH-INTENTION_COMPASS.md | 2026-02-10 |
| Projects | 30 | ontology.db projects | 2026-02-10 |
| **Commitments** | **15** | ontology.db commitments | 2026-02-12 |
| **Goals** | **12** | ontology.db goals | 2026-02-12 |
| **Risks** | **15** | ontology.db risks | 2026-02-12 |
| **Total** | **484** | | |

---

## III. SOURCE OF TRUTH ARCHITECTURE

### Ownership Model

```
SQLite (ontology.db)       Airtable                   Role
========================== ========================== ====================
apps, models, api_pricing  Platforms, Models           SQLite = source of truth
sources                    CANON Registry              SQLite = source of truth
projects, tasks            Projects                    SQLite = source of truth
(none)                     Intentions                  Airtable = source of truth
```

**Rule**: The SQLite ontology database (`~/.syncrescendence/ontology.db`) is the canonical source of truth for all structured data. Airtable is a **read-heavy visual surface** for browsing, filtering, and ad-hoc queries.

**Exception**: The Intentions table may serve as a write surface for new intentions, with periodic sync back to `ARCH-INTENTION_COMPASS.md`.

### Sync Direction

```
SQLite ontology.db  ---->  Airtable (primary direction)
                    <----  (Intentions only, optional)
```

### Conflict Resolution

If Airtable and SQLite diverge:
1. SQLite wins for Platforms, Models, CANON, Projects
2. Airtable wins for Intentions (if actively edited there)
3. The `SQLite ID` field in Airtable enables join-based reconciliation

---

## IV. MCP SERVER OPTIONS

### Recommended: `airtable-mcp-server` (domdomegg)

| Property | Value |
|----------|-------|
| Package | `airtable-mcp-server` |
| Version | 1.10.0 (Jan 2026) |
| License | MIT |
| Dependencies | 3 (@modelcontextprotocol/sdk, express, zod) |
| Binary | `airtable-mcp-server` |
| GitHub | github.com/domdomegg/airtable-mcp-server |

**Why this one**: Minimal, well-maintained, focused on read/write access. No bloat.

**Configuration for `~/.claude.json`**:

```json
{
  "mcpServers": {
    "airtable": {
      "command": "npx",
      "args": ["-y", "airtable-mcp-server"],
      "env": {
        "AIRTABLE_API_KEY": "<from ~/.syncrescendence/.env>"
      }
    }
  }
}
```

### Alternative: `@rashidazarang/airtable-mcp`

| Property | Value |
|----------|-------|
| Package | `@rashidazarang/airtable-mcp` |
| Version | 4.0.1 (Feb 2026) |
| License | MIT |
| Dependencies | 4 |

**More features** (analytics, predictive modeling) but heavier. Consider if advanced querying from Claude is needed.

### Installation

```bash
# Option A: npx (no install, recommended for MCP)
npx -y airtable-mcp-server

# Option B: Global install
npm install -g airtable-mcp-server
```

---

## V. SYNC STRATEGY

### Manual Sync (Current)

The seed script at `/tmp/airtable_seed_v2.py` performs one-way SQLite -> Airtable sync. Copy to permanent location for reuse:

```bash
cp /tmp/airtable_seed_v2.py ~/.syncrescendence/scripts/airtable_sync.py
```

**Limitation**: Creates new records; does not update existing ones. Each run will create duplicates unless records are cleared first.

### Recommended: Incremental Sync Script

Build a sync script that:
1. Reads all Airtable records (paginated)
2. Reads all SQLite records
3. Diffs by `SQLite ID` field
4. Creates new records for new SQLite rows
5. Updates existing records where data changed
6. Optionally deletes Airtable records with no SQLite match

**Rate limit consideration**: 5 req/sec with 10 records/batch means ~60 records/sec throughput. Full sync of 276 records takes ~5 seconds.

### Automation Options

| Method | Effort | Latency | Notes |
|--------|--------|---------|-------|
| Manual (run script) | Low | On-demand | Current state |
| claudecron task | Medium | Scheduled (daily) | Add to launchd via claudecron |
| Webhook (n8n/Make) | High | Real-time | Trigger on SQLite changes |
| MCP auto-sync | Medium | On-demand | Agent triggers sync via MCP tool |

**Recommendation**: Start with claudecron daily sync. Upgrade to webhook-triggered if edit frequency increases.

### claudecron Integration (Proposed)

```bash
# Add to claudecron: daily Airtable sync at 06:00
# Task: airtable-sync
# Schedule: Daily 06:00
# Command: python3 ~/.syncrescendence/scripts/airtable_sync.py
```

---

## VI. RELATIONSHIP TO INT-MI19 (PALANTIR ONTOLOGY)

Airtable serves as the **first visual surface** for the Palantir-like ontology vision:

```
Layer 1: SQLite (ontology.db)       -- Substrate (raw data, 2015 rows, 43 tables)
Layer 2: Airtable                    -- Visual Surface (484 records, 9 tables)
Layer 3: Dataview queries (Obsidian) -- In-vault querying (plugin needed)
Layer 4: Neo4j/Graphiti              -- Graph relationships (live)
Layer 5: Dashboard (CLI + surface)   -- ontology_query.py dashboard + SURFACE-ONTOLOGY_DASHBOARD.md
```

### What Airtable Unlocks

1. **Visual browsing**: Filter platforms by ASA layer, lifecycle, object type
2. **Quick editing**: Update records without SQL knowledge
3. **Sharing**: Share views with collaborators (future)
4. **Formula fields**: Computed columns (e.g., cost calculations for models)
5. **Linked records**: Cross-table relationships (Platforms <-> Models)
6. **Views**: Grid, Kanban, Gallery, Calendar views per table

### What Airtable Does NOT Replace

1. SQLite for complex joins and 89-function query interface
2. Graphiti/Neo4j for graph traversal and entity relationships
3. Obsidian Dataview for in-vault knowledge navigation
4. The repo as ground truth (Invariant 5: Repo Sovereignty)

---

## VII. API REFERENCE

### Authentication

```bash
export $(grep AIRTABLE_API_KEY ~/.syncrescendence/.env | xargs)
curl -H "Authorization: Bearer $AIRTABLE_API_KEY" "https://api.airtable.com/v0/..."
```

### Common Operations

```bash
# List all records in Platforms
curl -s -H "Authorization: Bearer $AIRTABLE_API_KEY" \
  "https://api.airtable.com/v0/appHyxiH0s9zOYH8I/tbl2bifSCiHt8WtFX"

# Filter active platforms
curl -s -H "Authorization: Bearer $AIRTABLE_API_KEY" \
  "https://api.airtable.com/v0/appHyxiH0s9zOYH8I/tbl2bifSCiHt8WtFX?filterByFormula={Stage}='ACTIVE'"

# Create record
curl -s -X POST "https://api.airtable.com/v0/appHyxiH0s9zOYH8I/tbl2bifSCiHt8WtFX" \
  -H "Authorization: Bearer $AIRTABLE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"records":[{"fields":{"Name":"New Platform","Stage":"EVALUATING"}}]}'

# Update record (PATCH)
curl -s -X PATCH "https://api.airtable.com/v0/appHyxiH0s9zOYH8I/tbl2bifSCiHt8WtFX" \
  -H "Authorization: Bearer $AIRTABLE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"records":[{"id":"recXXXXX","fields":{"Stage":"ACTIVE"}}]}'
```

### Table Quick-Reference

| Table | Table ID | Record Count |
|-------|----------|-------------|
| Platforms | `tbl2bifSCiHt8WtFX` | 126 |
| Models | `tbl7J4p9Qm410p4f4` | 20 |
| CANON Registry | `tblUV1j8L5it0kugg` | 179 |
| Intentions | `tbl2LQ50S7phz7oiW` | 84 |
| Projects | `tblH4NpzpwjaYW5Ms` | 30 |
| Commitments | `tblknyyoArt1OsHVR` | 15 |
| Goals | `tblOnR3CW0MRkSRLm` | 12 |
| Risks | `tblLSZby7G12lQ7qJ` | 15 |
| (default Table) | `tblFXRkMhQTZ8ZZrF` | 3 (can delete) |

---

## VIII. NEXT STEPS

### P0 (Immediate)

- [x] API verified and working
- [x] 5 tables created with ontology-aligned schema
- [x] 276 records seeded from SQLite (2026-02-10)
- [x] Integration document written
- [x] Intentions table seeded (84 records)
- [x] CANON Registry fully seeded (179 records)
- [x] Strategic tables created and seeded: Commitments (15), Goals (12), Risks (15) (2026-02-12)
- [x] Base total: 484 records across 9 tables
- [ ] Rename base from "Airtable" to "Syncrescendence Ontology" (requires UI -- API doesn't support base rename)

### P1 (This Week)

- [ ] Install `airtable-mcp-server` and add to `~/.claude.json`
- [ ] Copy sync script to `~/.syncrescendence/scripts/airtable_sync.py`
- [ ] Add incremental update logic (upsert by SQLite ID)
- [ ] Add claudecron daily sync task
- [ ] Delete default "Table" (`tblFXRkMhQTZ8ZZrF`)

### P2 (This Month)

- [ ] Add linked record fields (Platforms <-> Models)
- [ ] Add formula fields for computed metrics
- [ ] Create filtered views (Active platforms, by ASA layer, by family)
- [ ] Explore Airtable Automations for webhook-triggered sync
- [ ] Consider MCP server for Commander direct access

### P3 (Future)

- [ ] Bidirectional sync for Intentions
- [ ] Airtable Interface Designer for custom dashboards
- [ ] Airtable Apps (extensions) for visualization
- [ ] Integration with n8n for event-driven pipeline

---

## IX. CROSS-REFERENCES

- [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]] -- 4-layer ontology schema
- [[ARCH-INTENTION_COMPASS]] -- Source for Intentions table
- [[REF-SAAS_INTEGRATION_ARCHITECTURE]] -- Sovereignty strata mapping
- [[REF-STACK_TELEOLOGY]] -- Tool dispositional analysis
- `~/.syncrescendence/ontology.db` -- SQLite substrate (source of truth)
- `orchestration/00-ORCHESTRATION/scripts/ontology_query.py` -- CLI query interface
