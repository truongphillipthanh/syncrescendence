---
agent: adjudicator
priority: P1
category: sensing
frequency: daily
schedule: "08:00"
launchd_agent: com.syncrescendence.sensing-ecosystem-health
description: >
  Audit health of all infrastructure: MCP servers, launchd agents, Docker containers,
  CLI tools, and critical file paths. Report failures and drift.
---

# SENSING: Ecosystem Health Audit

**From**: Scheduler (launchd/claudecron)
**To**: Adjudicator (Codex CLI)
**Reply-To**: commander
**Kind**: SURVEY
**Priority**: P1
**Status**: PENDING
**Timeout**: 15
**CC**: commander

---

## Objective

Perform a comprehensive health check of all Syncrescendence infrastructure components and report any failures, degradation, or configuration drift.

### Audit Targets

#### 1. Docker Containers (4 expected)
```bash
docker ps --format '{{.Names}}\t{{.Status}}\t{{.Ports}}' | grep -E 'neo4j|graphiti|qdrant|chroma'
```
- Neo4j (port 7474)
- Graphiti API (port 8001)
- Qdrant (port 6333)
- Chroma (port 8765)

Report: running/stopped, uptime, port accessibility

#### 2. launchd Agents (15 expected)
```bash
launchctl list | grep syncrescendence
```
Verify all `com.syncrescendence.*` agents are loaded and not in error state (exit code 0 or running).

#### 3. MCP Server Connectivity (9 expected)
Test reachability of:
- Linear API (`curl -s https://api.linear.app/graphql`)
- ClickUp API (`curl -s https://api.clickup.com/api/v2/team`)
- Graphiti (localhost:8001)
- Qdrant (localhost:6333)
- Obsidian MCP, Filesystem MCP, Chrome DevTools, Playwright, Gemini-MCP

#### 4. CLI Tools (6 expected)
```bash
which recall ccusage ccundo splitrail vsync gemini-mcp-tool 2>/dev/null
```

#### 5. Critical Paths
Verify existence and non-emptiness of:
- `~/.syncrescendence/.env` (API keys present)
- `~/.syncrescendence/scripts/run_claude_task.sh`
- `/Users/home/Desktop/syncrescendence/CLAUDE.md`
- `/Users/home/Desktop/syncrescendence/COCKPIT.md`
- `/Users/home/Desktop/syncrescendence/orchestration/scripts/dispatch.sh`

#### 6. Disk & Resource
```bash
df -h / | tail -1
docker system df 2>/dev/null
```
Flag if disk usage > 85%.

## Expected Output

Write a structured health report:

```markdown
# Ecosystem Health Report — YYYY-MM-DD HH:MM

## Summary
- Docker: X/4 healthy
- launchd: X/15 loaded
- MCP: X/9 reachable
- CLI tools: X/6 available
- Critical paths: X/5 valid
- Disk: XX% used

## Failures
(List any component NOT in expected state)

## Warnings
(Components degraded but functional)

## Recommendations
(Actions to restore full health)
```

## Completion Protocol

1. Write results to `-OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-YYYYMMDD-ecosystem_health.md`
2. If any FAILURE found, also write to `-INBOX/commander/00-INBOX0/` as an escalation
3. Update **Status** above from PENDING to COMPLETE
