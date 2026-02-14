# TASK-20260214-ecosystem_health

**From**: dispatch
**To**: Adjudicator (Codex CLI)
**Reply-To**: dispatch
**Issued**: 2026-02-14 08:00:03
**Fingerprint**: f25d4d9
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: adjudicator-M1-Mac-mini
**Claimed-At**: 2026-02-14T16:00:05Z
**Completed-At**: 2026-02-14T16:00:08Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: —
**Receipts-To**: -OUTBOX/adjudicator/RESULTS
**Escalation-Contact**: dispatch
**Escalation-Delay**: 10

---

## Objective

Perform a comprehensive health check of all Syncrescendence infrastructure: Docker containers (Neo4j 7474, Graphiti 8001, Qdrant 6333, Chroma 8765), launchd agents (15 expected via launchctl list | grep syncrescendence), MCP server connectivity (9 servers), CLI tools (recall, ccusage, ccundo, splitrail, vsync, gemini-mcp-tool), critical file paths (~/.syncrescendence/.env, dispatch.sh, CLAUDE.md, COCKPIT.md), and disk usage. Write a structured health report to -OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-YYYYMMDD-ecosystem_health.md with summary counts, failures, warnings, and recommendations. If any FAILURE is found, also escalate to -INBOX/commander/00-INBOX0/. Reference template: 00-ORCHESTRATION/state/impl/sensing/TEMPLATE-ecosystem-health.md

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-20260214-ecosystem_health.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: ecosystem_health complete" && git push`
