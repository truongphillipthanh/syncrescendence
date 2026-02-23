---
id: ARCH-COCKPIT_OPERATIONAL_PROTOCOL
kind: ARCH
scope: orchestration
target: cockpit
status: active
updated: 2026-02-08
---

# Cockpit Operational Protocol

> The always-on cockpit is the nervous system of Syncrescendence. Each agent runs a continuous clarescence-driven operational loop. This document defines the target-state behavior for all four Mac mini cockpit agents and the MBA-resident Psyche.

## Layout (4x2 Grid on 5120x1440 Ultrawide)

```
┌──────────┬──────────┬──────────┬──────────┐
│  AJNA    │ COMMANDER│ADJUDICATOR│CARTOGR. │  75% height
│ OpenClaw │Claude Code│ Codex CLI│Gemini CLI│  (agent CLIs)
│ pane 1   │ pane 3   │ pane 5   │ pane 7   │
├──────────┼──────────┼──────────┼──────────┤
│  nvim    │  nvim    │  nvim    │  nvim    │  25% height
│ pane 2   │ pane 4   │ pane 6   │ pane 8   │  (editors)
└──────────┴──────────┴──────────┴──────────┘

Display: center 4/6 of 5120px (x: 853–4267). Flanking 1/6 each side free.
```

**Psyche** does NOT run on the Mac mini cockpit. She operates independently on the M4 MacBook Air via Tailscale bridge (see §VI).

---

## I. Universal Clarescence Cycle

Every agent follows a 7-phase operational loop. The cycle is continuous — agents don't wait for Sovereign input to begin work.

### Phase 1: Orient
- Read `agents/<agent>/inbox/pending/` for pending TASK files
- Check for CONFIRM-* and RESULT-* completion signals
- Scan `ARCH-INTENTION_COMPASS.md` for active intentions

### Phase 2: Situate
- `git status` — verify working tree state
- Read `README.md` + `CLAUDE.md` (or agent-equivalent config)
- Verify fingerprint matches expected state

### Phase 3: Calibrate
- Assess current directive against Triumvirate (Destination / Method / Current State)
- Check `IMPLEMENTATION-MAP.md` for relevant T2 items
- Identify delegation opportunities to other agents

### Phase 4: Triage
- Prioritize tasks by P0 > P1 > P2 > P3
- Identify blocked items and escalate to Sovereign if needed
- Claim actionable tasks, defer non-urgent items

### Phase 5: Execute + Document
- Execute the highest-priority task
- Commit with semantic prefixes (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`)
- Write execution log to `DYN-EXECUTION_STAGING.md`

### Phase 6: Proactive Awareness
- Monitor agent-specific sources for drift or new information
- Update memory architecture (`05-SIGMA/`) with session learnings
- Identify emerging patterns or issues

### Phase 7: Sovereign Interaction
- Report completion/blockers to Sovereign
- Stage handoff artifacts in `agents/<agent>/outbox/` if cross-platform relay needed
- Update `DYN-SESSION_LOG.md` via hooks

---

## II. Ajna — Local Orchestrator (Pane 1)

**Platform**: OpenClaw TUI (Opus 4.5 on M1 Mac mini)
**CLI**: `openclaw tui --session main`
**Role**: Sub-agent orchestration, webchat/iMessage, focused precision
**Color**: Mauve (`#cba6f7`)

### Operational Loop

```
BOOT:
  openclaw tui --session main
  → Load session context from OpenClaw persistent state
  → Connect to webchat/iMessage bridges

ORIENT:
  Scan agents/ajna/inbox/pending/ for TASK files
  Process CONFIRM-* and RESULT-* signals from other agents
  Read ARCH-INTENTION_COMPASS.md

TRIAGE:
  Prioritize local orchestration tasks
  Route sub-agent work via dispatch.sh
  HOOKS: {intent_compass.sh on input}

EXECUTE:
  Run orchestration directives
  Manage webchat/iMessage conversations
  Coordinate cross-agent task flow
  HOOKS: {session_log.sh, ajna_pedigree.sh on stop}

PROACTIVE:
  Monitor launchd watcher outputs (/tmp/syncrescendence-watch-*.log)
  Track OpenClaw session health
  HOOKS: {/updateOpenClawConfig(Ajna) — update Ajna-specific settings}  [ASPIRATIONAL]

SOVEREIGN INTERACTION:
  Report via agents/ajna/outbox/ or direct conversation
  Escalate blocked items to -SOVEREIGN/
```

### Existing Infrastructure
| Component | Status |
|-----------|--------|
| `watch_dispatch.sh` (launchd watcher) | ACTIVE |
| `agents/ajna/inbox/pending/` | ACTIVE |
| `ajna_pedigree.sh` (Stop hook) | ACTIVE |
| OpenClaw gateway (port 18789) | ACTIVE |

---

## III. Commander — Primary Executor (Pane 2)

**Platform**: Claude Code (Opus 4.6)
**CLI**: `claude --dangerously-skip-permissions`
**Role**: EXECUTOR-LEAD, primary directive handler, architectural decisions
**Color**: Blue (`#89b4fa`)

### Operational Loop

```
BOOT:
  claude --dangerously-skip-permissions
  → CLAUDE.md loaded automatically
  → Hooks fire: intent_compass.sh on UserPromptSubmit

ORIENT (/claresce Phase 1-2):
  Scan agents/commander/inbox/pending/ for TASK files
  Process CONFIRM-* and RESULT-* signals
  git status — verify ground truth
  Read ARCH-INTENTION_COMPASS.md
  HOOKS: {intent_compass.sh on every prompt}

SITUATE:
  Verify fingerprint matches
  Read IMPLEMENTATION-MAP.md for active T2 items
  Check Linear (SYN-* issues) for assigned work

CALIBRATE:
  Triumvirate alignment (Destination / Method / Current State)
  Assess delegation: mechanical → Adjudicator, corpus → Cartographer
  HOOKS: {dispatch.sh for cross-agent routing}

TRIAGE:
  P0 blockers first
  Claim highest-priority unclaimed task
  Enter Plan Mode for >3 file changes

EXECUTE:
  Primary code/document creation
  Extended thinking for architectural decisions
  Commit frequently with semantic prefixes
  HOOKS: {session_log.sh, create_execution_log.sh on Stop}

DOCUMENT:
  Write execution log entry
  Update DYN-PEDIGREE_LOG.md via ajna_pedigree.sh
  HOOKS: {pre_compaction.sh on PreCompact}

PROACTIVE:
  Monitor for configuration drift
  Update 05-SIGMA/ with session learnings
  HOOKS: {/updateClaudeConfig(Commander) — sync Commander settings}  [ASPIRATIONAL]
  HOOKS: {/conductReviewtrospective — post-session review}  [ASPIRATIONAL]

SOVEREIGN INTERACTION:
  Direct conversation (Commander IS the primary Sovereign interface)
  Stage cross-platform artifacts in agents/commander/outbox/
```

### Existing Infrastructure
| Component | Status |
|-----------|--------|
| CLAUDE.md (constitutional config) | ACTIVE |
| `intent_compass.sh` (UserPromptSubmit hook) | ACTIVE |
| `session_log.sh` (Stop hook) | ACTIVE |
| `ajna_pedigree.sh` (Stop hook) | ACTIVE |
| `create_execution_log.sh` (Stop hook) | ACTIVE |
| `pre_compaction.sh` (PreCompact hook) | ACTIVE |
| `dispatch.sh` (manual delegation) | ACTIVE |
| `agents/commander/inbox/pending/` | ACTIVE |
| Linear API integration | ACTIVE (API key configured) |

---

## IV. Adjudicator — Parallel Executor (Pane 3)

**Platform**: Codex CLI (GPT-5.2-codex, GPT-5.3-codex when entitled)
**CLI**: `codex --dangerously-bypass-approvals-and-sandbox` (fallback `--full-auto`)
**Role**: PARALLEL-EXEC, mechanical tasks, test suites, formatting, linting
**Color**: Green (`#a6e3a1`)

### Operational Loop

```
BOOT:
  codex --dangerously-bypass-approvals-and-sandbox  # fallback: --full-auto
  → Load AGENTS.md configuration
  → Full-auto mode: execute without confirmation prompts

ORIENT:
  Scan agents/adjudicator/inbox/pending/ for TASK files
  Process CONFIRM-* and RESULT-* from Commander dispatches

TRIAGE:
  Prioritize mechanical execution tasks
  Tests > formatting > linting > refactoring
  Flag architectural decisions for Commander escalation

EXECUTE:
  Run test suites and report results
  Execute formatting/linting passes
  Implement mechanical code changes per spec
  Commit with semantic prefixes

DOCUMENT:
  Write RESULT-* files back to Commander's inbox
  HOOKS: {dispatch.sh reply mechanism}

PROACTIVE:
  Monitor test health across codebase
  Track code quality metrics
  HOOKS: {/updateCodexConfig(Adjudicator) — sync Adjudicator settings}  [ASPIRATIONAL]
  HOOKS: {/implementMethodKaizen — technique improvement tracking}  [ASPIRATIONAL]

SOVEREIGN INTERACTION:
  Report via RESULT-* files to Commander
  Escalate non-mechanical decisions
```

### Existing Infrastructure
| Component | Status |
|-----------|--------|
| `watch_dispatch.sh` (launchd watcher) | ACTIVE |
| `agents/adjudicator/inbox/pending/` | ACTIVE |
| AGENTS.md (Codex config) | ACTIVE |

---

## V. Cartographer — Corpus Sensor (Pane 4)

**Platform**: Gemini CLI (Gemini 2.5 Pro)
**CLI**: `gemini -m gemini-2.5-pro --yolo`
**Role**: SENSOR, corpus-wide surveys, 1M+ context analysis, citation extraction
**Color**: Yellow (`#f9e2af`)

### Operational Loop

```
BOOT:
  gemini
  → Stateless — no persistent session
  → Load gemini-settings.json (MCP: filesystem)

ORIENT:
  Scan agents/cartographer/inbox/pending/ for TASK files
  Process CONFIRM-* and RESULT-* from Commander dispatches

TRIAGE:
  Prioritize corpus survey requests
  Full-corpus scans > targeted searches > citation extraction

EXECUTE:
  Run 1M+ context surveys across CANON, ENGINE, SIGMA
  Extract citations and evidence packs
  Produce structured survey reports
  Write results to agents/cartographer/outbox/ or RESULT-* files

DOCUMENT:
  Write RESULT-* files back to Commander's inbox
  Append findings to relevant 05-SIGMA/ files

PROACTIVE:
  Monitor corpus coherence (detect stale/conflicting documents)
  Track CANON coverage gaps
  HOOKS: {/updateGeminiConfig(Cartographer) — sync Cartographer settings}  [ASPIRATIONAL]
  HOOKS: {/updateMemoryArchitecture — push learnings to 05-SIGMA}  [ASPIRATIONAL]

SOVEREIGN INTERACTION:
  Report via RESULT-* files to Commander
  Flag corpus drift for Sovereign attention
```

### Existing Infrastructure
| Component | Status |
|-----------|--------|
| `watch_dispatch.sh` (launchd watcher) | ACTIVE |
| `agents/cartographer/inbox/pending/` | ACTIVE |
| gemini-settings.json (MCP config) | ACTIVE |

---

## VI. Psyche — Holistic QA (MBA Only)

**Platform**: OpenClaw (GPT-5.2 on M4 MacBook Air)
**Role**: Extraction, specs, QA, holistic synthesis
**Machine**: M4 MacBook Air (NOT Mac mini cockpit)
**Connection**: Tailscale bridge to Mac mini

### Field Kit Configuration (DEC-PSYCHE-001 through 008)

| Decision | Ruling |
|----------|--------|
| DEC-PSYCHE-001 | Field Kit, not mirror — MBA is lean subset |
| DEC-PSYCHE-002 | Tailscale bridge for cross-machine connectivity |
| DEC-PSYCHE-003 | chezmoi for dotfile synchronization |
| DEC-PSYCHE-004 | Separate SSH keys per machine |
| DEC-PSYCHE-005 | Brewfile subset (essentials only on MBA) |
| DEC-PSYCHE-006 | No local constellation on MBA — connect to Mac mini |
| DEC-PSYCHE-007 | Twin coordination via Slack + filesystem + git |
| DEC-PSYCHE-008 | AeroSpace + Karabiner on both machines |

### Operational Loop

```
BOOT:
  openclaw tui --session psyche
  → Connect to Mac mini via Tailscale
  → Access shared filesystem via git pull

ORIENT:
  Scan agents/psyche/inbox/pending/ for TASK files
  Check Slack for Commander/Ajna dispatches

EXECUTE:
  QA review of Commander output
  Holistic synthesis across corpus
  Extraction and spec generation
  Write results back via git push or Slack

PROACTIVE:
  Monitor overall system health
  Cross-validate agent outputs
  Flag inconsistencies
```

### Status: BLOCKED
MBA config blocked by Tailscale setup on both machines. Estimated 70 minutes Sovereign interaction once Tailscale is active.

---

## VII. Hook & Skill Audit

### Existing (ACTIVE)

| Hook/Script | Event | Agent | Output |
|-------------|-------|-------|--------|
| `intent_compass.sh` | UserPromptSubmit | Commander | DYN-INTENTIONS_QUEUE.md |
| `session_log.sh` | Stop | Commander | DYN-SESSION_LOG.md |
| `ajna_pedigree.sh` | Stop | Commander | DYN-PEDIGREE_LOG.md |
| `create_execution_log.sh` | Stop | Commander | DYN-EXECUTION_STAGING.md |
| `pre_compaction.sh` | PreCompact | Commander | stdout warning |
| `dispatch.sh` | Manual | All | TASK-* files in agent inboxes |
| `watch_dispatch.sh` | Background (launchd) | All agents | Task claim/execute/complete |
| `triage_outgoing.sh` | Manual | Commander | agents/*/outbox/ scan |
| `triage_inbox.sh` | Manual | All | agents//inbox scan |

### Existing Skills

| Skill | File | Agent |
|-------|------|-------|
| `/pedigree` | `.claude/skills/pedigree.md` | Commander |
| `/intentions` | `.claude/skills/intentions.md` | Commander |
| `/readize` | `.claude/skills/readize.md` | Commander |
| `/listenize` | `.claude/skills/listenize.md` | Commander |
| `/audize` | `.claude/skills/audize.md` | Commander |
| `/integrate` | `.claude/skills/integrate.md` | Commander |

### Aspirational (TO BE CREATED)

| Hook/Skill | Agent | Purpose | Priority |
|------------|-------|---------|----------|
| `/claresce` | All (Commander primary) | Clarescence runbook as invocable skill | P1 |
| `/conductReviewtrospective` | Commander | Post-session review cycle | P2 |
| `/implementMethodKaizen` | Adjudicator | Technique improvement tracking | P3 |
| `/updateMemoryArchitecture` | All | Push session learnings to 05-SIGMA | P2 |
| `/updateClaudeConfig(Commander)` | Commander | Sync Commander config changes | P3 |
| `/updateCodexConfig(Adjudicator)` | Adjudicator | Sync Adjudicator config changes | P3 |
| `/updateGeminiConfig(Cartographer)` | Cartographer | Sync Cartographer config changes | P3 |
| `/updateOpenClawConfig(Ajna)` | Ajna | Sync Ajna config changes | P3 |

---

## VIII. Keybinding Reference

### tmux (prefix = Ctrl+Space)

| Binding | Target | Description |
|---------|--------|-------------|
| prefix+1 | cockpit.1 | Ajna (top) |
| prefix+2 | cockpit.2 | nvim-Ajna (bottom) |
| prefix+3 | cockpit.3 | Commander (top) |
| prefix+4 | cockpit.4 | nvim-Commander (bottom) |
| prefix+5 | cockpit.5 | Adjudicator (top) |
| prefix+6 | cockpit.6 | nvim-Adjudicator (bottom) |
| prefix+7 | cockpit.7 | Cartographer (top) |
| prefix+8 | cockpit.8 | nvim-Cartographer (bottom) |
| prefix+J | cockpit.1 | Jump to Ajna |
| prefix+C | cockpit.3 | Jump to Commander |
| prefix+A | cockpit.5 | Jump to Adjudicator |
| prefix+G | cockpit.7 | Jump to Cartographer |
| prefix+B | — | Broadcast toggle (all panes) |
| prefix+X | — | Emergency stop (Ctrl-C all agents) |

### Neovim Agent Pipe (leader = Space)

| Binding | Mode | Target | Pane |
|---------|------|--------|------|
| `<leader>aj` | Visual | Selection -> Ajna | 1 |
| `<leader>ac` | Visual | Selection -> Commander | 3 |
| `<leader>aa` | Visual | Selection -> Adjudicator | 5 |
| `<leader>ag` | Visual | Selection -> Cartographer | 7 |
| `<leader>ap` | Visual | Selection -> Auto-detect | even->odd |
| `<leader>aJ` | Normal | Buffer -> Ajna | 1 |
| `<leader>aC` | Normal | Buffer -> Commander | 3 |
| `<leader>aA` | Normal | Buffer -> Adjudicator | 5 |
| `<leader>aG` | Normal | Buffer -> Cartographer | 7 |
| `<leader>aP` | Normal | Buffer -> Auto-detect | even->odd |

---

## Cross-References

| Reference | Path |
|-----------|------|
| Cockpit script | `00-ORCHESTRATION/scripts/cockpit.sh` |
| tmux config | `~/.tmux.conf` |
| Agent Pipe plugin | `~/.config/nvim/lua/plugins/agent-pipe.lua` |
| Clarescence Runbook | `02-ENGINE/REF-CLARESCENCE_RUNBOOK.md` |
| Neo-Blitzkrieg Buildout | `00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md` |
| Terminal Stack Config | `00-ORCHESTRATION/TERMINAL-STACK-CONFIG.md` |
| Fleet Commander's Handbook | `02-ENGINE/REF-FLEET_COMMANDERS_HANDBOOK.md` |
| Twin Coordination Protocol | `00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md` |
