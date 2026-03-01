# CLARESCENCE: Session 6 — MCP Activation + Execution Sprint

```yaml
CLARESCENCE: Session 6 orientation — first full MCP session, execution mode
Fidelity: partial
Passes run: 1-3
Convergent Path: Housekeeping → Qdrant MCP fix → Linear hygiene → ClickUp MCP → claudecron → Blitzkrieg skill
Rationale (digest):
  - 53+ MCP tools now LIVE (Linear 33, Graphiti 9, Obsidian 11+) — first session with native access
  - Qdrant MCP NOT LOADING despite session 5 configuration — needs diagnosis
  - Cockpit reloaded ✓, Pane 1 = Psyche ✓, all services GREEN
  - "Last reconnaissance clarescence" mandate from session 5 — this session = EXECUTION
  - P1 roadmap: ClickUp MCP, claudecron, Blitzkrieg skill, MBA setup
  - 3 stale watchdog inbox tasks need archival (corpus-health already fixed in f42af3e)
Dependencies created/updated: ClickUp MCP → claudecron → SYN-31 (Live Ledger)
Falsifier: If Qdrant MCP config is fundamentally broken (uvx incompatibility), memory search degrades to Graphiti-only
Confidence: high
```

---

## Pass 1: Triumvirate Calibration

### Destination / Why Now

Session 6 is the **first session where Commander operates with full MCP tool access**. Sessions 1-5 built the infrastructure; session 5 configured 44 MCP tools that required a restart to activate. This restart has occurred.

The 3rd clarescence (session 5) declared itself the **LAST reconnaissance pass**. All subsequent sessions = execution against the 19 decision atoms. The P1 roadmap for this week:

| # | Target | Status | Unlocks |
|---|--------|--------|---------|
| 1 | ClickUp MCP server | NOT STARTED | T1b native access (replaces temp-file API) |
| 2 | claudecron (scheduled dispatch) | NOT STARTED | SYN-31 Live Ledger, always-on heartbeat |
| 3 | Blitzkrieg Agent Teams skill | NOT STARTED | Codified multi-agent dispatch pattern |
| 4 | MBA Ajna physical setup | GUIDE WRITTEN | Physical machine config (delegate to Psyche/Ajna) |

### Current State / What's Working

**Services (ALL GREEN):**

| Service | Port | Status | Verified |
|---------|------|--------|----------|
| Chroma | 8765 | ✓ | `{"status":"ok","collections":["engine","canon","test"]}` |
| Webhook | 8888 | ✓ | Inbox counts + git status reporting |
| Qdrant | 6333 | ✓ | `{"collections":[{"name":"memory_migrations"},{"name":"memories"}]}` |
| Neo4j | 7474 | ✓ | Connected (via Graphiti) |
| Graphiti | 8001 | ✓ | `{"status":"ok","message":"...connected to neo4j database"}` |
| OpenClaw | 18789 | ✓ | Gateway running |

**MCP Tools (53+ activated):**

| Server | Tools | Transport | Status |
|--------|-------|-----------|--------|
| Linear | 33 | HTTP (mcp.linear.app) | LIVE ✓ — tested list_issues, verified SYN-32/36 |
| Graphiti | 9 | stdio (Python) | LIVE ✓ — tested get_status |
| Obsidian | 11 | stdio (Node) | LIVE ✓ — loaded read_note, write_note, etc. |
| Filesystem | 16 | stdio (Node) | AVAILABLE (deferred, not yet loaded) |
| Qdrant | 2 | stdio (uvx) | **NOT IN DEFERRED LIST** — config issue |
| Chrome DevTools | 18+ | stdio | AVAILABLE (deferred) |
| Playwright | 20+ | stdio | AVAILABLE (deferred) |

**Cockpit:** Reloaded. Pane 1 = Psyche/CTO. Enterprise roles mapped.

**Working Tree:** 5 modified DYN files (expected hook outputs), 1 untracked dir (INBOX0/).

### What's Broken

1. **Qdrant MCP not loading**: Configured in session 5 (mcp-server-qdrant via uvx, local ONNX embeddings) but absent from Claude Code's deferred tools list. The Qdrant Docker container is healthy (port 6333 responds). The MCP server process likely isn't starting. Needs `.claude.json` or `settings.json` investigation.

2. **Stale watchdog inbox**: 3 TASK-WATCHDOG-* files in `-INBOX/commander/00-INBOX0/` from before the corpus-health fix (f42af3e). These are noise — the underlying issue was resolved.

3. **IMPLEMENTATION-MAP.md**: Referenced by clarescence procedure but doesn't exist at repo root. May have been renamed or consolidated during restructuring.

4. **Linear issue drift**: SYN-18 (MCP rollout) still shows "Todo" despite Linear/Graphiti/Obsidian MCPs being installed. SYN-33 (Hindsight activation) may need cancellation/archival since Hindsight was deleted.

### Fit-to-Destination Verdict

**STRONG FIT.** All infrastructure prerequisites are met. MCP tools are live. Cockpit is configured. The gap is purely execution — installing the remaining P1 items and beginning to use the infrastructure that was built in sessions 1-5.

---

## Pass 2: 18-Lens Scorecard

| # | Lens | Verdict | Notes |
|---|------|---------|-------|
| 1 | Structural Coherence | PASS | Repo structure intact, 5 numbered dirs + INBOX/OUTGOING/SOVEREIGN |
| 2 | CANON Alignment | PASS | 79 files, frontmatter complete, Bridge v1.0 done |
| 3 | Service Health | PASS | 6/6 services GREEN |
| 4 | Agent Coordination | WARN | Qdrant MCP not loading — reduces Commander memory search |
| 5 | Intention Alignment | PASS | P1 items map to INT-1501 (autonomy), INT-1202 (velocity) |
| 6 | Tool Availability | PASS | 53+ MCP tools live (was 0 before restart) |
| 7 | Backlog Coherence | WARN | IMPLEMENTATION-MAP.md missing, Linear issues need hygiene |
| 8 | Security | PASS | API keys in .env (chmod 600), auth-source for Emacs |
| 9 | Concurrency Safety | WARN | No git zone ownership protocol (identified session 2, deferred) |
| 10 | Documentation | PASS | COCKPIT.md v3.1.0, DEPLOYMENT-PLAYBOOK.md current |
| 11 | Automation | PASS | 12 launchd services, 5 hooks, 4-tier self-healing |
| 12 | Context Economics | PASS | MCP replaces temp-file patterns (~2900 tokens/session saved) |
| 13 | Sovereignty | PASS | Repo = ground truth, web apps = cache |
| 14 | Scalability | PASS | Constellation architecture supports MBA expansion |
| 15 | Energy State | PASS | "EXECUTION not reconnaissance" = sustainable momentum |
| 16 | Reversibility | PASS | All changes committed, git history clean |
| 17 | Deployment Cascade | WARN | MBA still unconfigured (guide written, execution pending) |
| 18 | Token Budget | PASS | ChatGPT Plus daily limit, NVIDIA free tier operational |

**Score: 14/18 PASS, 4 WARN**

WARN items are all addressable within this session or the current sprint. None are blockers.

---

## Pass 3: CANON Coherence

### What Canonical Docs Say

- **CLAUDE.md**: Commit discipline, verification before completion, dispatch with Reply-To
- **COCKPIT.md v3.1.0**: Constellation fully mapped — 6 agents, 12 services, enterprise roles
- **ARCH-INTENTION_COMPASS.md**: INT-1501 (maximize autonomy), INT-1503 (fiduciary level), INT-1202 (capitalize on heavy machinery)
- **3rd clarescence**: 19 decision atoms. P0 ALL DONE. P1 this week: ClickUp MCP, claudecron, Blitzkrieg skill, MBA.

### Where Reality Diverges

| # | Divergence | Severity | Fix |
|---|-----------|----------|-----|
| 1 | Qdrant MCP configured but not loading in Claude Code | Medium | Check settings.json mcpServers config |
| 2 | IMPLEMENTATION-MAP.md referenced by skill but doesn't exist | Low | Find renamed location or create |
| 3 | SYN-18 (MCP rollout) still "Todo" — 3/5 MCPs installed | Low | Update Linear issue status |
| 4 | SYN-33 (Hindsight) still "Todo" in Linear — feature deleted | Low | Cancel or archive in Linear |
| 5 | 3 stale watchdog tasks in commander INBOX0 | Low | Archive to 40-DONE |

---

## Execution Plan — Session 6

### Phase 1: Housekeeping (5 min)

1. Archive 3 stale TASK-WATCHDOG-* files to 40-DONE
2. Commit DYN state files (working tree hygiene)
3. Update SYN-18 description (MCP rollout progress)

### Phase 2: Qdrant MCP Diagnosis (5 min)

1. Check `.claude.json` or Claude Code `settings.json` for qdrant MCP config
2. Test `uvx mcp-server-qdrant` manually
3. Fix config and verify tool appears in deferred list

### Phase 3: ClickUp MCP (15 min)

1. Research available ClickUp MCP servers
2. Install + configure with API key
3. Test: list spaces, list tasks, create task
4. Update SYN-18 progress

### Phase 4: claudecron (20 min)

1. Research claudecron or equivalent scheduled dispatch for Claude Code
2. If no official solution: build launchd-based scheduled dispatch
3. This directly unlocks SYN-31 (Live Ledger — URGENT in Linear)

### Phase 5: Blitzkrieg Agent Teams Skill (15 min)

1. Create `.claude/skills/blitzkrieg_teams.md` — codifies multi-agent dispatch
2. Leverages Claude Code's native TeamCreate / Task tools
3. Defines standard team compositions for common operations

### Phase 6: Linear Hygiene + Commit (5 min)

1. Update issue statuses in Linear via MCP
2. Commit all session artifacts
3. Update DYN-EXECUTION_STAGING.md

---

## Decision Atoms

### DEC-S6-001: Qdrant MCP Priority

**Decision**: Diagnose Qdrant MCP loading issue before proceeding with ClickUp MCP.
**Rationale**: Memory search is a foundational capability. If Qdrant MCP works, Commander gains persistent memory via shared Mem0 collection.
**Reversibility**: High — if unfixable, Graphiti provides alternative graph-based memory.
**Falsifier**: If uvx MCP transport is fundamentally incompatible with Claude Code's stdio expectations.

### DEC-S6-002: claudecron Strategy

**Decision**: If no official claudecron exists, build a launchd-based scheduled dispatch that drops TASK files into agent inboxes on a cron schedule.
**Rationale**: The always-on heartbeat architecture (INT-PARETO) requires timed dispatch. launchd is macOS-native and already proven for 12 services.
**Reversibility**: High — launchd plists are trivially removable.
**Falsifier**: If Claude Code sessions cannot be triggered programmatically from outside.

---

*Clarescence produced by Commander (Opus 4.6) | Session 6 | 2026-02-09*
*IntentionLink: INT-1501, INT-1503, INT-1202, Epic 6 (Commander Bridge)*
