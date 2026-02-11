---
id: REF-JIRA_INTEGRATION
kind: REF
scope: engine
target: constellation
status: active
created: 2026-02-10
updated: 2026-02-10
linear: SYN-51
---

# REF -- Jira Cloud Integration Design

## Scrum Methodology for Syncrescendence via Atlassian Jira Cloud

**Version**: 1.0.0
**Created**: 2026-02-10
**Author**: jira-onboarder agent (Opus 4.6)
**Linear Issue**: SYN-51
**Companion to**: PRAC-multi_methodology_framework.md, REF-SAAS_INTEGRATION_ARCHITECTURE.md

---

## I. ACCOUNT & API DETAILS

### Jira Cloud Instance

| Property | Value |
|----------|-------|
| **Site URL** | `https://syncrescendence.atlassian.net` |
| **Account Email** | `truongphillipthanh@icloud.com` |
| **Account ID** | `712020:6de8ce37-716e-4c5d-a6ac-729e324bc46c` |
| **Display Name** | Phillip Truong |
| **Time Zone** | America/Los_Angeles |
| **Deployment** | Jira Cloud |
| **API Version** | REST API v3 (`/rest/api/3/`) |
| **Agile API** | `/rest/agile/1.0/` |

### Authentication

**Method**: HTTP Basic Auth (NOT Bearer/OAuth2)

```
Authorization: Basic base64(email:api_token)
```

- API token sourced from `~/.syncrescendence/.env` as `ATLASSIAN_API_KEY`
- Token format: `ATATT3xFfG...` (Atlassian Personal API Token)
- The `/api.atlassian.com/me` endpoint does NOT work with API tokens (requires OAuth2); use direct site REST API instead

**curl example**:
```bash
source ~/.syncrescendence/.env
curl -s -u "truongphillipthanh@icloud.com:$ATLASSIAN_API_KEY" \
  https://syncrescendence.atlassian.net/rest/api/3/myself
```

**IMPORTANT**: The `/rest/api/3/search` endpoint has been deprecated. Use `/rest/api/3/search/jql` instead:
```bash
curl -s -u "$AUTH" \
  "https://syncrescendence.atlassian.net/rest/api/3/search/jql?jql=project=SCRUM&maxResults=50"
```

### Environment Variables for MCP/CLI

| Variable | Purpose | Source |
|----------|---------|--------|
| `JIRA_BASE_URL` | `https://syncrescendence.atlassian.net` | Static |
| `JIRA_USER_EMAIL` | `truongphillipthanh@icloud.com` | Static |
| `JIRA_API_TOKEN` | API token value | `$ATLASSIAN_API_KEY` from `~/.syncrescendence/.env` |
| `JIRA_TYPE` | `cloud` | Static |
| `JIRA_AUTH_TYPE` | `basic` | Static |

---

## II. CURRENT JIRA STATE

### Project

| Property | Value |
|----------|-------|
| **Project Name** | Syncrescendence |
| **Project Key** | `SCRUM` |
| **Project ID** | `10000` |
| **Type** | Software (next-gen/team-managed) |
| **Board** | SCRUM board (ID: 1, type: simple) |

### Issue Types Available

| ID | Name | Hierarchy | Scope |
|----|------|-----------|-------|
| 10001 | Epic | 1 (parent) | Project |
| 10003 | Task | 0 (standard) | Project |
| 10004 | Story | 0 (standard) | Project |
| 10005 | Feature | 0 (standard) | Project |
| 10006 | Request | 0 (standard) | Project |
| 10007 | Bug | 0 (standard) | Project |
| 10002 | Subtask | -1 (child) | Project |

### Workflow Statuses

| ID | Name | Category |
|----|------|----------|
| 10000 | To Do | New (blue-gray) |
| 10001 | In Progress | In Progress (yellow) |
| 10002 | In Review | In Progress (yellow) |
| 10003 | Done | Done (green) |

### Board Columns

```
To Do  -->  In Progress  -->  In Review  -->  Done
```

### Estimation

- **Field**: `customfield_10016` (Story point estimate)
- **Ranking**: `customfield_10019` (Rank)

### Sprints

| ID | Name | State | Start | End |
|----|------|-------|-------|-----|
| 2 | SCRUM Sprint 0 | **active** | 2026-02-10 | 2026-02-24 |
| 1 | SCRUM Sprint 1 | future | (not started) | -- |

### Existing Issues (Seed Data)

| Key | Type | Summary | Status | Sprint |
|-----|------|---------|--------|--------|
| SCRUM-1 | Task | Task 1 | To Do | Sprint 0 |
| SCRUM-2 | Story | Task 2 | In Progress | Sprint 0 |
| SCRUM-3 | Feature | Task 3 | In Progress | -- |
| SCRUM-4 | Subtask | Subtask 2.1 (child of SCRUM-2) | To Do | -- |

These appear to be sample/test issues created during initial site setup. They can be repurposed or archived.

### Custom Fields of Interest

| Field ID | Name | Use |
|----------|------|-----|
| `customfield_10016` | Story point estimate | Velocity tracking |
| `customfield_10020` | Sprint | Sprint assignment |
| `customfield_10015` | Start date | Sprint/issue timing |
| `customfield_10019` | Rank | Backlog ordering |
| `customfield_10021` | Flagged | Impediment marking |

---

## III. MAPPING DESIGN: JIRA <-> LINEAR

### Architectural Position

Jira SUPERSTRUCTURES Linear. Jira owns Scrum methodology (sprints, ceremonies, velocity). Linear owns granular engineering execution (issue tracking, cycles, triage). The relationship is hierarchical, not duplicative.

```
JIRA (Scrum Superstructure)
  |
  |-- Epics (= Linear Projects or cross-project themes)
  |-- Stories/Features (= Linear Issue clusters)
  |-- Sprints (= 2-week ceremony containers)
  |-- Velocity/Burndown (= Scrum metrics)
  |
  +-- LINEAR (Execution Engine)
       |-- Projects (13 mapped from PROJ-XXX)
       |-- Issues (SYN-5 to SYN-60)
       |-- Labels (P0-P3, chain:*, cli:*, domain:*)
       |-- Workflow (Backlog -> Todo -> In Progress -> Done)
```

### Entity Mapping

| Jira Entity | Linear Entity | Relationship |
|-------------|--------------|--------------|
| **Epic** | Project | 1 Jira Epic = 1 Linear Project (or a cross-project initiative) |
| **Story** | Issue (grouped) | 1 Jira Story = N Linear Issues (feature cluster) |
| **Task** | Issue (atomic) | 1 Jira Task = 1 Linear Issue |
| **Subtask** | Sub-issue | Direct mapping |
| **Sprint** | Cycle | Jira Sprint drives; Linear Cycle mirrors |
| **Story Points** | Estimate | Jira is source of truth for points |
| **Status** | State | Bidirectional sync (see Status Mapping) |
| **Labels** | Labels | Linear labels are more granular; Jira uses Components |

### Status Mapping

| Jira Status | Linear State | Notes |
|-------------|-------------|-------|
| To Do | Todo (`910fb97d`) | Direct |
| In Progress | In Progress (`17db8a8b`) | Direct |
| In Review | In Progress (`17db8a8b`) | Linear has no "Review" state; use label `review:pending` |
| Done | Done (`4f15cb0a`) | Direct |
| -- | Backlog (`e4201e12`) | Jira backlog items not yet in a sprint |

### Recommended Jira Project Structure

**Option A: Single Project (RECOMMENDED)**

Keep the existing `SCRUM` project as the single Scrum container. Use Jira Epics to mirror the 13 Linear projects:

| Jira Epic | Linear Project | PROJ Code |
|-----------|---------------|-----------|
| IIC Configuration | PROJ-002 | PROJ-002 |
| Ontology Content | PROJ-006a | PROJ-006a |
| Ontology Substrate | PROJ-006b | PROJ-006b |
| Linear Integration | PROJ-LINEAR | PROJ-LINEAR |
| Commander Bridge | PROJ-BRIDGE | PROJ-BRIDGE |
| Constellation Agents | PROJ-AGENTS | PROJ-AGENTS |
| Automation Master | PROJ-AUTO | PROJ-AUTO |
| Tool Onboarding | PROJ-TOOLS | PROJ-TOOLS |
| ... (remaining projects) | ... | ... |

**Rationale**: A single Jira project with one Scrum board keeps ceremonies unified. Splitting into multiple Jira projects would fragment sprint planning and velocity tracking across boards. The Sovereign is a solo operator -- one sprint backlog is optimal.

**Option B: Multi-Project** (NOT recommended for solo operator)

One Jira project per Linear project. Would fragment sprints and velocity. Only appropriate if multiple humans join.

---

## IV. DATA FLOW

### Directional Flow

```
                    SCRUM CEREMONIES
                         |
                    JIRA (Sprint)
                    /    |    \
              Epic  Story  Velocity
                |     |      |
           [superstructure bridge]
                |     |      |
           Project Issue  Metrics
                    |
               LINEAR (Execution)
                    |
              IMPL-MAP (Repo T2)
                    |
               CANON (Repo T1)
```

### Flow Rules

1. **Sprint Planning** (Jira -> Linear): Stories/tasks prioritized in Jira sprint planning. Corresponding Linear issues get state update to "Todo" or "In Progress".
2. **Daily Execution** (Linear -> Linear): Day-to-day work tracked in Linear. Agents work from Linear issues.
3. **Sprint Review** (Linear -> Jira): Completed Linear issues drive Jira story transitions to "Done". Story points credited.
4. **Retrospective** (Jira -> Repo): Retrospective notes flow to `05-SIGMA/practice/` or EXEMPLA docs.
5. **Velocity** (Jira): Burndown charts and velocity tracked in Jira. This is Jira's unique value.

### Sync Strategy

**Phase 1 (Manual / Semi-Automated)**: Commander creates Jira epics matching Linear projects. Sprint planning is manual. Status sync via MCP tools or scripts.

**Phase 2 (Automated via Make/n8n)**: Webhook-driven sync:
- Linear issue state change -> update Jira task status
- Jira sprint start/end -> update Linear cycle
- New Linear issue -> create Jira subtask under matching epic

**Phase 3 (Full Bridge)**: Bidirectional real-time sync. Jira is Scrum ceremony surface; Linear is execution surface; repo is ground truth.

---

## V. MCP SERVER INVESTIGATION

### Available Packages (npm registry, 2026-02-10)

| Package | Version | Last Updated | Maintainer | Assessment |
|---------|---------|-------------|------------|------------|
| **@rokealvo/jira-mcp** | 1.4.0 | 2026-01-19 | rokealvo | **RECOMMENDED** -- 15 tools, active, Jira-focused |
| **@ecubelabs/atlassian-mcp** | 1.12.0 | 2026-02-10 | selenehyun | Most active (32 versions), covers Jira + Confluence |
| **@answerai/jira-mcp** | 1.1.0 | 2025-09-30 | maxtechera | AI-focused branding, MIT, 5 versions |
| jira-mcp | 1.0.1 | 2025-02-27 | camdenclark | Smithery-listed, minimal (1 dep), oldest |
| @caobing122/jira-mcp-server | 1.1.5 | 2026-01-27 | caobing122 | Recent, 5 versions |
| @aot-tech/jira-mcp-server | 1.0.9 | 2025-09-08 | syama.sundara | 9 versions, multi-maintainer |
| @mcp-devtools/jira | 0.2.6 | 2025-03-11 | dxheroes_dev | DX Heroes, semver < 1.0 |
| @rafael-arreola/jira-rs | 0.3.10 | 2026-01-30 | rafael-arreola | Rust CLI wrapper |

**No official Anthropic Jira MCP** exists (`@anthropic-ai/mcp-server-jira` does not exist).

### Recommended: @rokealvo/jira-mcp v1.4.0

**Tools provided** (15 total):

| Tool | Description |
|------|-------------|
| `search_issues` | JQL search |
| `get_issue` | Issue details with comments |
| `create_issue` | Create new issue |
| `update_issue` | Update issue fields |
| `add_comment` | Add comment to issue |
| `get_transitions` | Available status transitions |
| `transition_issue` | Change issue status |
| `get_epic_children` | Issues under an epic |
| `add_attachment` | Attach file to issue |
| `get_create_meta` | Field schema for issue creation |
| `get_field_options` | Field value options |
| `get_projects` | List projects |
| `get_users` | Search users |
| `get_server_info` | Server information |
| `delete_issue` | Delete an issue |

**Configuration for `~/.claude.json`**:

```json
{
  "mcpServers": {
    "jira": {
      "command": "npx",
      "args": ["-y", "@rokealvo/jira-mcp"],
      "env": {
        "JIRA_BASE_URL": "https://syncrescendence.atlassian.net",
        "JIRA_USER_EMAIL": "truongphillipthanh@icloud.com",
        "JIRA_API_TOKEN": "${ATLASSIAN_API_KEY}",
        "JIRA_TYPE": "cloud",
        "JIRA_AUTH_TYPE": "basic"
      }
    }
  }
}
```

**Note**: The `${ATLASSIAN_API_KEY}` syntax may or may not be interpolated by Claude Code's MCP loader. If not, the raw token value must be placed directly (same pattern as other MCP servers in the existing config).

### Alternative: @ecubelabs/atlassian-mcp v1.12.0

Most actively maintained (32 versions, updated 2026-02-10). Covers both Jira and Confluence. Heavier dependencies (8 deps including axios, winston, zod). Good if Confluence integration is also desired in the future. Proprietary license (not MIT).

### Sprint-Specific API Endpoints (Direct curl)

The MCP servers may not expose sprint management directly. These endpoints are available via the Agile REST API:

```bash
# List sprints
GET /rest/agile/1.0/board/{boardId}/sprint

# Get sprint details
GET /rest/agile/1.0/sprint/{sprintId}

# Get issues in sprint
GET /rest/agile/1.0/sprint/{sprintId}/issue

# Create sprint
POST /rest/agile/1.0/sprint

# Start/close sprint
PUT /rest/agile/1.0/sprint/{sprintId}

# Move issues to sprint
POST /rest/agile/1.0/sprint/{sprintId}/issue
```

---

## VI. SCRUM CEREMONY MAPPING

### Sprint Cadence

| Ceremony | Frequency | Jira Surface | Repo Artifact |
|----------|-----------|-------------|---------------|
| Sprint Planning | Every 2 weeks (Monday) | Sprint board, backlog grooming | IMPL-MAP priority updates |
| Daily Standup | Daily (async) | Jira comments / Linear comments | `-INBOX/` dispatch notes |
| Sprint Review | End of sprint | Done column review | Commit log, execution log |
| Sprint Retrospective | End of sprint | Jira retrospective board | `05-SIGMA/practice/` entry |
| Backlog Grooming | Weekly (Wednesday) | Backlog ordering, story points | IMPL-MAP new entries |

### Velocity Tracking

- **Story Points**: Assigned in Jira via `customfield_10016` (Story point estimate)
- **Velocity Chart**: Native Jira feature on Scrum boards (requires converting board type from "simple" to "scrum")
- **Burndown**: Native Jira sprint report
- **Target**: Establish baseline velocity over first 3 sprints, then use for capacity planning

### Sprint Naming Convention

```
SCRUM Sprint {N} -- {YYYY-MM-DD} to {YYYY-MM-DD}
```

Sprint 0 is the current bootstrapping sprint (2026-02-10 to 2026-02-24).

---

## VII. INTEGRATION ROADMAP

### Phase 1: Foundation (Current -- SYN-51)

- [x] API authentication verified
- [x] Jira Cloud site discovered (`syncrescendence.atlassian.net`)
- [x] Project structure documented
- [x] MCP server options investigated
- [x] Integration design document created
- [ ] **SOVEREIGN ACTION**: Convert SCRUM board from "simple" to "Scrum" type (enables velocity charts, burndown, sprint planning view)
- [ ] **SOVEREIGN ACTION**: Review and approve MCP server addition to `~/.claude.json`
- [ ] Add `JIRA_USER_EMAIL` and `JIRA_BASE_URL` to `~/.syncrescendence/.env` for convenience

### Phase 2: Structure (Next)

- [ ] Create Jira Epics matching Linear projects (13 epics)
- [ ] Establish story point scale (Fibonacci: 1, 2, 3, 5, 8, 13)
- [ ] Archive seed issues (SCRUM-1 through SCRUM-4) or repurpose
- [ ] Plan first real sprint with Linear issues mapped to Jira stories
- [ ] Install and configure Jira MCP server

### Phase 3: Automation

- [ ] Webhook bridge (Jira <-> Linear status sync)
- [ ] Sprint lifecycle automation (auto-create Linear cycle on sprint start)
- [ ] Velocity dashboard integration
- [ ] Retrospective template automation

---

## VIII. SOVEREIGNTY STRATA POSITION

Per REF-SAAS_INTEGRATION_ARCHITECTURE.md:

| Stratum | Jira Role |
|---------|-----------|
| sigma-1 (Teleology) | Sprint goals express sigma-1 intentions |
| sigma-5 (Intelligence) | Scrum methodology intelligence, velocity analytics |
| sigma-6 (Access) | API token auth, Basic Auth over HTTPS |
| sigma-7 (Execution) | MCP server, REST API, board operations |

Jira sits at **sigma-5/sigma-7** boundary, same tier as Linear and ClickUp. Its unique contribution is Scrum ceremony infrastructure that neither Linear nor ClickUp provide with the same depth.

---

## IX. RISK & CONSTRAINTS

| Risk | Mitigation |
|------|------------|
| Jira Free tier limits (10 users, limited storage) | Solo operator -- well within limits |
| Board type is "simple" not "scrum" | Sovereign must convert via UI (Settings > Board > Type) |
| No native Jira-Linear integration | MCP + webhook bridge (Phase 3) |
| API token rotation | Track in credential rotation schedule (SYN-57 pattern) |
| MCP server stability | @rokealvo/jira-mcp is MIT, can fork if abandoned |
| Ceremony overhead for solo operator | Keep async: sprint planning = 30min, retro = 15min |

---

## X. QUICK REFERENCE

### API Cheat Sheet

```bash
# Source credentials
source ~/.syncrescendence/.env
JIRA="https://syncrescendence.atlassian.net"
AUTH="truongphillipthanh@icloud.com:$ATLASSIAN_API_KEY"

# Get current user
curl -s -u "$AUTH" "$JIRA/rest/api/3/myself"

# List projects
curl -s -u "$AUTH" "$JIRA/rest/api/3/project"

# Search issues (new endpoint)
curl -s -u "$AUTH" "$JIRA/rest/api/3/search/jql?jql=project=SCRUM+ORDER+BY+rank&maxResults=50"

# List sprints
curl -s -u "$AUTH" "$JIRA/rest/agile/1.0/board/1/sprint"

# Get sprint issues
curl -s -u "$AUTH" "$JIRA/rest/agile/1.0/sprint/2/issue"

# Create issue (via temp file)
cat > /tmp/jira-issue.json << 'EOF'
{
  "fields": {
    "project": {"key": "SCRUM"},
    "summary": "Issue title",
    "issuetype": {"name": "Story"},
    "customfield_10016": 3
  }
}
EOF
curl -s -u "$AUTH" -H "Content-Type: application/json" \
  -X POST "$JIRA/rest/api/3/issue" -d @/tmp/jira-issue.json
```

### Key IDs Reference

| Entity | ID | Name |
|--------|-----|------|
| Project | 10000 | SCRUM |
| Board | 1 | SCRUM board |
| Active Sprint | 2 | SCRUM Sprint 0 |
| Epic type | 10001 | Epic |
| Story type | 10004 | Story |
| Task type | 10003 | Task |
| Bug type | 10007 | Bug |
| Feature type | 10005 | Feature |
| Story Points field | customfield_10016 | Story point estimate |
| Sprint field | customfield_10020 | Sprint |

---

*This document is the authoritative reference for Jira integration within the syncrescendence toolchain. Updates should be made here as the integration matures through Phases 1-3.*
