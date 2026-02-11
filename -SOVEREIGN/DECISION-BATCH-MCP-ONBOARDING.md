# Sovereign Decision Batch: MCP Server Onboarding
**Date**: 2026-02-10
**From**: Commander
**Priority**: P1
**Status**: PENDING

## Context

Three integration design docs are complete with API keys installed. MCP server installation requires Sovereign approval per policy.

---

## Decision 1: Install Jira MCP Server

**Package**: `@rokealvo/jira-mcp` v1.4.0 (MIT license, 15 tools)
**Config** (add to `~/.claude.json` under mcpServers):
```json
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
```

**Prerequisite**: Convert Jira board from "simple" to "Scrum" type (requires Sovereign UI action in Jira settings -> Board -> Board type)

**Impact**: Enables Commander + Adjudicator to create/manage Jira sprints, epics, stories directly
**Risk**: Low -- read/write to Sovereign's own Jira workspace

[ ] APPROVED  [ ] DENIED  [ ] DEFERRED

---

## Decision 2: Install Todoist MCP Server

**Package**: `todoist-mcp` v1.2.4 (MIT license, minimal deps)
**Config**:
```json
"todoist": {
  "command": "npx",
  "args": ["-y", "todoist-mcp"],
  "env": {
    "TODOIST_API_KEY": "${TODOIST_API_KEY}"
  }
}
```

**Sub-decision**: Frozen projects on free tier
- Option A: Upgrade to Todoist Pro ($5/mo) -- unfreezes projects, enables reminders/labels
- Option B: Delete frozen projects, use labels for contexts
- Option C: Accept limitation (API still works, UI shows frozen badge)

**Impact**: Enables GTD workflow management via Commander
**Risk**: Low

[ ] APPROVED  [ ] DENIED  [ ] DEFERRED
Frozen projects: [ ] A (upgrade)  [ ] B (delete)  [ ] C (accept)

---

## Decision 3: Install Airtable MCP Server

**Package**: `airtable-mcp-server` (standard Airtable MCP)
**Config**:
```json
"airtable": {
  "command": "npx",
  "args": ["-y", "airtable-mcp-server"],
  "env": {
    "AIRTABLE_API_KEY": "${AIRTABLE_API_KEY}"
  }
}
```

**Impact**: Enables ontology surface browsing/editing via Commander
**Risk**: Low

[ ] APPROVED  [ ] DENIED  [ ] DEFERRED

---

## Decision 4: Todoist Weekly Review Cadence

Should Commander run a weekly GTD review automatically?
- Option A: Claudecron Sunday 09:00 -- automated review + report
- Option B: Manual only -- Sovereign triggers when ready
- Option C: Hybrid -- automated report, Sovereign reviews

[ ] A (auto)  [ ] B (manual)  [ ] C (hybrid)

---

## Batch Approval

To approve all 3 MCP installations:
Write "APPROVED ALL" and sign.

Sovereign: _______________
Date: _______________
