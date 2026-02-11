---
id: REF-TODOIST_INTEGRATION
kind: REF
scope: engine
target: constellation
status: active
updated: 2026-02-11
---

# REF -- Todoist GTD Integration
## Rapid Capture, Context-Based Execution, Weekly Review

**Version**: 1.0.0
**Created**: 2026-02-10
**Author**: todoist-onboarder agent (Opus 4.6)
**Linear Issue**: SYN-53
**Companion to**: REF-SAAS_INTEGRATION_ARCHITECTURE.md, REF-STACK_TELEOLOGY.md

---

## I. ROLE IN THE FIVE-TIER ARCHITECTURE

Todoist operates as a **substructure to ClickUp (T1b)**, providing GTD methodology for rapid personal task capture that is too granular for ClickUp. It handles the "bottom of the funnel" -- quick thoughts, errands, phone calls, micro-tasks under 30 minutes.

```
T0  Intention Compass       Strategic vision vectors
T1a Linear                  Work done TO the repo (SYN issues)
T1b ClickUp                 Work NOT ON repo (Professional/Personal/Financial)
    |-- Todoist (GTD)       Rapid capture + context execution (substructure)
T2  Implementation Map      Sprint-level tasks
T3  Claude Code Tasks       Session-level atomic ops
```

**Governing Principle**: Todoist is the inbox for your brain. ClickUp is the kanban for your life. They do not compete -- they feed each other.

---

## II. ACCOUNT & API DETAILS

| Field | Value |
|-------|-------|
| Account | User ID `52681159` |
| Tier | Free (8 projects max, 5 active tasks per project in some modes) |
| API Version | **v1** (REST) -- `https://api.todoist.com/api/v1/` |
| API Fallback | REST v2 (`/rest/v2/`) still works with Bearer auth. v1 requires different header format. |
| Auth | Bearer token: `$TODOIST_API_KEY` (in `~/.syncrescendence/.env`) |
| Auth Note | `source ~/.syncrescendence/.env` does NOT export vars. Use `KEY=$(grep TODOIST_API_KEY ~/.syncrescendence/.env \| cut -d= -f2)` or use key directly. |
| Deprecated | Sync API v9 (`/sync/v9/`) returns 410 Gone. |
| Connection | **VERIFIED 2026-02-11** -- REST v2 returns 200, all 8 projects visible, CRUD operations confirmed |
| Web UI | `https://app.todoist.com/` |

### API Endpoints Used

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/v1/projects` | GET | List all projects |
| `/api/v1/projects` | POST | Create project |
| `/api/v1/tasks` | GET/POST | List/create tasks |
| `/api/v1/tasks/{id}/move` | POST | Move task between projects |
| `/api/v1/tasks/{id}/close` | POST | Complete a task |
| `/api/v1/labels` | GET/POST | List/create labels |
| `/api/v1/sections` | GET/POST | List/create sections |

### Authentication Pattern

```bash
export $(grep TODOIST_API_KEY ~/.syncrescendence/.env | xargs)
curl -s -H "Authorization: Bearer $TODOIST_API_KEY" \
  "https://api.todoist.com/api/v1/projects" | python3 -m json.tool
```

Note: The `.env` file uses `KEY=value` format without `export`. Use `export $(grep ... | xargs)` pattern or a temp-file approach for shell scripts.

---

## III. GTD STRUCTURE (IMPLEMENTED)

### Projects (8/8 slots used -- free tier limit)

| # | Project | ID | Color | GTD Role |
|---|---------|---|----|----------|
| 0 | **Inbox** | `6XF8J65C6M3hFjc2` | charcoal | GTD Inbox -- capture everything here |
| 1 | **@Computer** | `6fxg9w4j8Vqr8VRv` | blue | Context: tasks requiring a computer (FROZEN*) |
| 2 | **@Phone** | `6fxg9wQrJXqWpqhQ` | blue | Context: tasks requiring phone calls (FROZEN*) |
| 3 | **@Errands** | `6fxg9whPWw2MxPj7` | blue | Context: tasks requiring going somewhere |
| 4 | **@Home** | `6fxg9wm3RhJvj8rR` | blue | Context: tasks done at home |
| 5 | **@Office** | `6fxg9wqwqr9c8x5X` | blue | Context: tasks done at office/desk |
| 6 | **@Waiting** | `6fxg9wxRPrjvGvrp` | orange | Context: delegated/blocked, awaiting response |
| 7 | **Professional** | `6fxg9x4h6FPPvqX9` | red | Area: career and professional tasks |

*FROZEN: Free tier freezes projects beyond threshold. @Computer and @Phone show `is_frozen: true`. **Sovereign decision (2026-02-11): Option C accepted** -- API still works for CRUD operations; UI is read-only for frozen projects. Tasks can be created, completed, and moved via API. No upgrade needed at this time.

### Sections

**Inbox** (`6XF8J65C6M3hFjc2`):
| Section | ID | Purpose |
|---------|----|---------|
| Capture | `6fxgC53pPRWpCP3R` | Raw brain-dump zone (default landing) |
| Clarify & Organize | `6fxgC57fjpVvQjj2` | Items being processed into GTD buckets |

**Professional** (`6fxg9x4h6FPPvqX9`):
| Section | ID | Purpose |
|---------|----|---------|
| Next Actions | `6fxgC5Hfxf8qgrf9` | Actionable items ready to execute |
| Active Projects | `6fxgC5RM5VRC9rPh` | Multi-step efforts in progress |
| Someday/Maybe | `6fxgC5gXMQ3RH85h` | Low-priority parking lot |

### Labels (13 created)

**Energy Level:**
| Label | ID | Color | Use |
|-------|----|-------|-----|
| `energy_high` | `2183015625` | red | Tasks requiring focus/creativity |
| `energy_low` | `2183015626` | green | Tasks doable when tired |

**Time Estimates:**
| Label | ID | Color | Use |
|-------|----|-------|-----|
| `5min` | `2183015627` | mint_green | Quick wins |
| `15min` | `2183015629` | lime_green | Short tasks |
| `30min` | `2183015631` | yellow | Medium tasks |
| `1hr_plus` | `2183015634` | orange | Long tasks -- consider ClickUp escalation |

**GTD Workflow:**
| Label | ID | Color | Use |
|-------|----|-------|-----|
| `next_action` | `2183015635` | red | The very next physical action on any project |
| `someday_maybe` | `2183015637` | grey | Deferred, review weekly |
| `reference` | `2183015639` | charcoal | Non-actionable info to keep |
| `weekly_review` | `2183015645` | blue | Items flagged for weekly review attention |

**Integration:**
| Label | ID | Color | Use |
|-------|----|-------|-----|
| `escalate_clickup` | `2183015641` | violet | Task has grown beyond Todoist scope |
| `personal` | `2183015642` | green | Area tag (mirrors ClickUp Personal space) |
| `financial` | `2183015644` | yellow | Area tag (mirrors ClickUp Financial space) |

---

## IV. GTD WORKFLOW

### 1. Capture (Inbox)
- Dump everything into the Inbox. No filtering, no judgment.
- Use natural language dates: "call dentist tomorrow", "buy groceries friday"
- Apply labels later during Clarify phase.

### 2. Clarify & Organize
Move items from "Capture" section to "Clarify & Organize", then:

```
Is it actionable?
  NO  -> Label: reference (keep) or delete (trash)
  YES -> Can it be done in < 2 minutes?
    YES -> Do it now, complete the task
    NO  -> Is it a single action?
      YES -> Move to appropriate @Context project + label time estimate
      NO  -> Is it multi-step (> 30 min total)?
        YES -> Label: escalate_clickup -> create in ClickUp -> complete Todoist task
        NO  -> Move to Professional > Active Projects section
```

### 3. Execute by Context
When you are:
- At your computer -> open `@Computer` project, pick by energy/time
- Running errands -> open `@Errands` project
- On the phone -> open `@Phone` project
- At home -> open `@Home` project
- Waiting for someone -> check `@Waiting` for follow-ups

### 4. Weekly Review (Sunday)
1. Process all Inbox items to zero
2. Review `@Waiting` -- follow up or escalate
3. Review `someday_maybe` labeled items -- promote or delete
4. Review `Professional > Active Projects` -- ensure each has a `next_action`
5. Review `escalate_clickup` items -- ensure all were migrated
6. Quick scan of ClickUp spaces for anything that decomposed into Todoist-level micro-tasks

---

## V. CLICKUP ESCALATION RULES

### When does a Todoist task escalate to ClickUp?

A task escalates when ANY of these are true:

| Criterion | Threshold | Reasoning |
|-----------|-----------|-----------|
| **Time estimate** | > 30 minutes | Beyond "quick action" scope |
| **Multi-step** | > 3 sub-steps | Needs project tracking |
| **Involves others** | Delegation needed | ClickUp has assignment |
| **Deadline-critical** | Hard external deadline | ClickUp has Gantt/calendar |
| **Recurring complex** | Repeated with variations | ClickUp templates |
| **Financial** | Any dollar amount attached | Financial space tracking |

### Escalation Mapping

| Todoist Area/Label | ClickUp Space | ClickUp Space ID |
|---|---|---|
| Professional project | Professional | `901313150565` |
| `personal` label | Personal | `901313150566` |
| `financial` label | Financial | `901313150567` |

### Escalation Process

1. In Todoist, add label `escalate_clickup` to the task
2. Create the task in the appropriate ClickUp space/list
3. In the Todoist task description, add `CU: <clickup-task-id>`
4. Complete the Todoist task (it has been promoted)

---

## VI. MCP SERVER OPTIONS

### Recommended: `todoist-mcp` v1.2.4

```
Package:     todoist-mcp
Version:     1.2.4
Published:   2025-07-13
Author:      stanislavlysenko
License:     MIT
Deps:        @modelcontextprotocol/sdk, uuid, zod
Binary:      todoist-mcp
```

**Installation** (when ready to integrate into Commander's MCP config):

```json
{
  "mcpServers": {
    "todoist": {
      "command": "npx",
      "args": ["-y", "todoist-mcp@1.2.4"],
      "env": {
        "TODOIST_API_KEY": "<key>"
      }
    }
  }
}
```

### Alternatives Evaluated

| Package | Version | Notes |
|---------|---------|-------|
| `todoist-mcp` | 1.2.4 | Best: maintained, minimal deps, MCP SDK 1.1.1 |
| `@chrusic/todoist-mcp-server-extended` | 0.2.5 | Larger (150KB), older MCP SDK 0.5.0, label-focused |
| `todoist-mcp-app` | 1.0.0 | Interactive UI -- not suitable for CLI agents |
| `@abhiz123/todoist-mcp-server` | 0.1.0 | Minimal, outdated |

### MCP Integration Status: NOT YET INSTALLED

Todoist MCP should be installed in `~/.claude.json` only after Sovereign ratification. The free tier's project/task limits may make MCP less valuable than direct API calls for now.

---

## VII. SYNC STRATEGY

### Data Flow

```
Brain -> Todoist (capture)
         |
         v
     GTD Processing (clarify, organize, context-assign)
         |
         +-- Quick tasks (<30 min) -> Execute from Todoist -> Complete
         |
         +-- Complex tasks (>30 min) -> ClickUp (tracking) -> Execute -> Complete both
         |
         +-- Repo work -> ClickUp may note it, but IMPL-MAP is truth -> SYN issue
```

### Sync Directions

| From | To | Trigger | Method |
|------|-----|---------|--------|
| Todoist | ClickUp | `escalate_clickup` label | Manual (Phase 1), automated (Phase 2 via Make/n8n) |
| ClickUp | Todoist | Task decomposition | Manual: break ClickUp task into micro-actions in Todoist |
| Todoist | IMPL-MAP | Never directly | Todoist is pre-repo; repo work goes through Linear (T1a) |

### Phase 1: Manual (NOW)
- Use Todoist for capture and GTD workflow
- Manually escalate to ClickUp when thresholds are hit
- Weekly review catches anything that fell through

### Phase 2: Semi-Automated (Future -- requires paid tier or Make/n8n)
- Make/n8n webhook: when `escalate_clickup` label is applied, auto-create ClickUp task
- ClickUp webhook: when a task is decomposed, push sub-tasks to Todoist
- Requires Todoist Pro for webhooks/API limits, or use polling

### Phase 3: Full MCP Integration (Future)
- Install `todoist-mcp` into Commander's MCP config
- Commander can create/complete/move Todoist tasks natively
- GTD review becomes part of `/claresce` loop

---

## VIII. FREE TIER CONSTRAINTS

| Limit | Free Value | Impact |
|-------|-----------|--------|
| Projects | 8 max | ALL SLOTS USED. Cannot add Personal/Financial/Someday/Reference as projects. Use labels instead. |
| Active tasks | 5 per project (UI limit varies) | May need frequent completion/archival |
| Filters | 3 max | Limited custom views |
| Reminders | Not available | Use due dates + priority instead |
| Labels | Unlimited | Primary organizational tool on free tier |
| Sections | Unlimited | Use sections heavily within projects |
| Collaborators | Limited | Solo use only (matches our need) |

### Free Tier Adaptation

Because we hit the 8-project limit, the GTD structure adapts:
- **Contexts**: 6 projects (@Computer, @Phone, @Errands, @Home, @Office, @Waiting)
- **Areas**: Professional as project; Personal and Financial as labels on tasks in other projects
- **Someday/Maybe**: Label (`someday_maybe`) + section in Professional
- **Reference**: Label (`reference`) on tasks anywhere

If upgraded to Pro ($5/mo), we could:
- Create dedicated Personal, Financial, Someday/Maybe, Reference projects
- Use filters for advanced views (Today + energy_high, Next Actions across all)
- Enable reminders
- Access activity log for review

---

## IX. QUICK REFERENCE

### Key Extraction (shell)

```bash
# Correct pattern — source does NOT export from .env
TODOIST_KEY=$(grep TODOIST_API_KEY ~/.syncrescendence/.env | cut -d= -f2)
```

### Create a task via API (REST v2 -- VERIFIED WORKING)

```bash
TODOIST_KEY=$(grep TODOIST_API_KEY ~/.syncrescendence/.env | cut -d= -f2)
curl -s -X POST "https://api.todoist.com/rest/v2/tasks" \
  -H "Authorization: Bearer $TODOIST_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Buy milk",
    "project_id": "2367047925",
    "labels": ["5min", "energy_low"],
    "priority": 2,
    "due_string": "tomorrow"
  }' | python3 -m json.tool
```

### Complete a task via API

```bash
curl -s -X POST "https://api.todoist.com/rest/v2/tasks/{task_id}/close" \
  -H "Authorization: Bearer $TODOIST_KEY"
```

### List all tasks

```bash
curl -s "https://api.todoist.com/rest/v2/tasks" \
  -H "Authorization: Bearer $TODOIST_KEY" | python3 -m json.tool
```

### Project ID Quick Reference (REST v2 IDs)

| Project | REST v2 ID | API v1 ID |
|---------|-----------|-----------|
| Inbox | `2348487086` | `6XF8J65C6M3hFjc2` |
| @Computer | `2367047921` | `6fxg9w4j8Vqr8VRv` |
| @Phone | `2367047923` | `6fxg9wQrJXqWpqhQ` |
| @Errands | `2367047925` | `6fxg9whPWw2MxPj7` |
| @Home | `2367047926` | `6fxg9wm3RhJvj8rR` |
| @Office | `2367047927` | `6fxg9wqwqr9c8x5X` |
| @Waiting | `2367047928` | `6fxg9wxRPrjvGvrp` |
| Professional | `2367047929` | `6fxg9x4h6FPPvqX9` |

### Section ID Quick Reference

| Section | REST v2 ID | API v1 ID | Parent Project |
|---------|-----------|-----------|----------------|
| Capture | `215043395` | `6fxgC53pPRWpCP3R` | Inbox |
| Clarify & Organize | `215043397` | `6fxgC57fjpVvQjj2` | Inbox |
| Next Actions | `215043400` | `6fxgC5Hfxf8qgrf9` | Professional |
| Active Projects | `215043401` | `6fxgC5RM5VRC9rPh` | Professional |
| Someday/Maybe | `215043402` | `6fxgC5gXMQ3RH85h` | Professional |

### Rate Limit Note

REST v2 has aggressive rate limiting. When creating multiple tasks, add `sleep 2` between calls. Batch creation via temp JSON files (`-d @/tmp/task.json`) avoids shell escaping issues.

---

## X. OPEN ITEMS / SOVEREIGN DECISIONS NEEDED

1. ~~**Frozen projects**~~: **RESOLVED** -- Option C accepted (2026-02-11). API works, UI limited. Revisit if workflow friction emerges.
2. **MCP installation**: `todoist-mcp` is ready to install but adds another MCP server. Sovereign approval needed. Todoist task created to track.
3. **Automation phase**: Make/n8n escalation webhook requires Todoist Pro tier.
4. **Weekly review cadence**: Recurring task created (every Sunday at 10:00). Add to claudecron as P2 enhancement.

---

## XI. IMPLEMENTATION STATUS (2026-02-11)

### Connection Verified
- REST v2 API: **200 OK** with Bearer auth
- API v1: Returns 403 with Bearer auth (requires different header format -- use v2 for now)
- All CRUD operations confirmed: create, list, close tasks

### Structure Confirmed Live
- **8/8 projects** operational (2 frozen: @Computer, @Phone -- API still works)
- **5 sections** across Inbox and Professional
- **13 labels** covering energy, time estimates, GTD workflow, and integration
- **Frozen project workaround**: Option C -- API bypass accepted

### GTD Task Inventory (16 active tasks)

#### @Computer (project `2367047921` / v2 `6fxg9w4j8Vqr8VRv`) -- 12 tasks
| Task | SYN | Priority | Due | Labels |
|------|-----|----------|-----|--------|
| Complete Mastery IIC account email setup | SYN-24 | P1 (urgent) | 2026-02-10 | next_action, 15min, energy_low |
| Review Linear-to-IMPL-MAP sync gap | SYN-16 | P2 (high) | 2026-02-11 | next_action, 30min, energy_high |
| Test Jira API connectivity | SYN-51 | P3 (medium) | 2026-02-13 | next_action, 15min, energy_low |
| Draft tmux dashboard layout spec | SYN-40 | P3 (medium) | 2026-02-13 | next_action, 30min, energy_high |
| List dotfiles for machine sync | SYN-43 | P3 (medium) | 2026-02-13 | next_action, 15min, energy_low |
| Audit Psyche OpenClaw config | SYN-35 | P3 (medium) | 2026-02-16 | next_action, 30min, energy_high |
| Research OpenClaw Discord setup | SYN-50 | P4 (normal) | 2026-02-16 | 15min, energy_low |
| Identify Google APIs for IIC pipeline | SYN-49 | P4 (normal) | 2026-02-23 | 15min, energy_high |
| Map PKM tools overlap | SYN-48 | P4 (normal) | 2026-02-23 | 30min, energy_high |
| Create Trello board | SYN-52 | P4 (normal) | 2026-02-23 | 15min, energy_low |
| Set up Notion LifeOS workspace | SYN-59 | P4 (normal) | 2026-02-23 | 30min, energy_high |
| Upload docs to NotebookLM | SYN-39 | P4 (normal) | 2026-02-23 | 15min, energy_low |

#### Professional > Next Actions (project `2367047929` / section `215043400`) -- 2 tasks
| Task | SYN | Priority | Due | Labels |
|------|-----|----------|-----|--------|
| Install todoist-mcp in ~/.claude.json | SYN-53 | P3 (medium) | 2026-02-13 | next_action, 5min, energy_low |
| Weekly GTD Review | -- | P2 (high) | Recurring Sun 10:00 | weekly_review, 1hr_plus, energy_high |

#### @Waiting (project `2367047928` / v2 `6fxg9wxRPrjvGvrp`) -- 2 tasks
| Task | SYN | Priority | Due | Labels |
|------|-----|----------|-----|--------|
| MBA Ajna agent setup | -- | P2 (high) | No due (blocked) | 1hr_plus, energy_high |
| Sovereign: Todoist Pro upgrade decision | -- | P3 (medium) | No due | 5min, energy_low |

### SYN Issues NOT in Todoist (by design)

These issues are project-level work tracked in Linear, not GTD-level "next physical actions":

| Issue | Title | Reason Not in Todoist |
|-------|-------|----------------------|
| SYN-28 | Metabolize Coherence/ (193 files) | Backlog, multi-session repo work |
| SYN-17 | Triangulate FDIS requirements | Backlog, P3 research task |
| SYN-19 | Token/cost burn management | Backlog, P3 engineering task |
| SYN-37 | Syncrescript Rails refactor | Backlog, HIBERNATE verdict |
| SYN-44 | Machine Handbooks | Todo, documentation project (>1hr) |
| SYN-46 | Info Stream Extraction Pipeline | Todo, engineering project |
| SYN-54 | TeamGantt onboarding | Todo, blocked by Trello first |
| SYN-60 | Raycast clone design | Backlog, long-term |

### ClickUp Escalation Mapping (verified)

| Todoist Area | ClickUp Space | ClickUp ID | Status |
|--------------|---------------|------------|--------|
| Professional project | Professional | `901313150565` | MAPPED |
| `personal` label | Personal | `901313150566` | MAPPED |
| `financial` label | Financial | `901313150567` | MAPPED |
