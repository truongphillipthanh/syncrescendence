# COCKPIT.md
## Syncrescendence System Overview

**Version**: 3.1.0
**Updated**: 2026-02-09
**Purpose**: 30,000ft orientation for any platform entering the constellation

---

## What Is Syncrescendence?

Syncrescendence is a distributed cognition system designed to demonstrate that individual capability can achieve institutional-scale intelligence through orchestrated AI platforms. It serves as proof-of-concept for navigating civilizational phase transitions where no single intelligence possesses the complete capability matrix for polymathic synthesis.

**We are no longer coding, but conducting logistics. Our materiel is tokens, and our personnel are agents.**

---

## The Constellation

### Three Accounts
| Account | Email | Auth | Tier | Monthly | Purpose |
|---------|-------|------|------|---------|---------|
| 1 | truongphillipthanh@icloud.com | Apple | Claude Max + ChatGPT Plus | $120 | Sovereign substrate, primary execution |
| 2 | icloud.truongphillipthanh@gmail.com | Google | Claude Pro + Google AI Pro | $40 | Parallel execution + corpus sensing |
| 3 | truongphillipthanh@gmail.com | Google | Unpaid | $0 | Free tier access |

### The Constellation (Pantheon v3)

The constellation has three tiers: **CLI agents** (always-on, cockpit-resident, autonomous), **local agents** (OpenClaw, always-on), and **web avatars** (interactive, browser-based, Sovereign-operated).

#### CLI Agents (Enterprise Roles — Primary Operational Tier)

| Avatar | Epithet | Role | Platform | Acct | Machine | Cockpit | Summon |
|--------|---------|------|----------|------|---------|---------|--------|
| **Commander** | Viceroy | COO | Claude Code (Opus 4.6) | 1 | Mac mini | Pane 2 | "Commander, pivot to..." |
| **Adjudicator** | Executor | CQO | Codex CLI (Sonnet) | 2 | Mac mini | Pane 3 | "Adjudicator, execute..." |
| **Cartographer** | Exegete | CIO | Gemini CLI (2.5 Pro) | 2 | Mac mini | Pane 4 | "Cartographer, survey..." |

#### Local Agents (AjnaPsyche Archon — Fused Executive Brain)

| Avatar | Epithet | Role | Platform | Acct | Machine | Cockpit | Summon |
|--------|---------|------|----------|------|---------|---------|--------|
| **Psyche** | Synaptarch | CTO | OpenClaw GPT-5.3-codex | 1 | Mac mini | Pane 1 | "Psyche, holistically calibrate..." |
| **Ajna** | Strategos | CSO | OpenClaw Kimi K2.5 | — | MBA (remote) | — | "Ajna, illuminate..." |

Ajna (steering wheel) + Psyche (rudder) = AjnaPsyche Archon. StarCraft High Templar fusion metaphor.

#### Web Avatars (Pantheon v2 Legacy — Sovereign-Operated)

| Avatar | Epithet | Role | Platform | Acct | Summon |
|--------|---------|------|----------|------|--------|
| **Augur** | Inquisitor | VERIFIER | Perplexity | — | "Augur, ascertain..." |
| **Oracle** | Recon | RECON | Grok | 1 | "Oracle, understand..." |
| **Vizier** | Hermeneut | INTERPRETER | Claude Web | 2 | "Vizier, elucidate..." |
| **Vanguard** | Architect | COMPILER | ChatGPT Web | 1 | "Vanguard, formulate..." |
| **Diviner** | Illuminator | DIGESTOR | Gemini Web | 2 | "Diviner, elaborate..." |

Web avatars are interactive and require Sovereign presence. They are NOT autonomous agents.

#### Operational Notes
- **Stable mapping**: Platforms characterized into roles mirroring their capabilities
- **Future**: Live model capabilities/benchmark ledger for efficacious routing

---

## The State Machine

Content flows through defined states:

```
CAPTURED > INTERPRETED > COMPILED > STAGED > COMMITTED
                      \ DIGESTED /
                      \ SENSED   /
                      \ VERIFIED /
```

- **CAPTURED**: Raw ideation in Sovereign's mind
- **INTERPRETED**: Structured understanding (Claude Web artifact)
- **COMPILED**: Formatted artifact (ChatGPT Canvas)
- **DIGESTED**: Clarified summary (Gemini Docs)
- **SENSED**: Evidence pack (Gemini CLI output)
- **VERIFIED**: Externally validated (Perplexity/Grok)
- **STAGED**: In -OUTGOING/, ready for commit
- **COMMITTED**: In repository (ground truth)

### The Three-Word Mnemonic: CAPTURE > DISPATCH > RETURN

1. **CAPTURE** — Seize the idea before it evaporates. Raw form is fine. Rivers are ephemeral.
2. **DISPATCH** — Route to the right platform for processing.
3. **RETURN** — Commit the processed artifact to the repository. Work doesn't exist until it's in the repo.

---

## Ground Truth

The **repository** is ground truth. All platforms verify against it via:
- **Fingerprint**: 8-character git commit hash
- **Handoff Token**: State marker transferred between platforms

```
Repository (Account 1 Origin)
├── 00-ORCHESTRATION/  # Strategic coordination (state/, scripts/, archive/)
├── 01-CANON/          # Verified canonical knowledge (PROTECTED)
├── 02-ENGINE/         # Functions, prompts, avatars, model profiles, queue items
├── 04-SOURCES/        # Source documents (raw/, processed/, research/)
├── 05-SIGMA/          # Operational knowledge + memory + exempla
│   ├── mechanics/     # Deep-dive mechanisms
│   ├── practice/      # Implementation patterns
│   └── journal/       # Org-mode daily journal (dormant)
├── -INBOX/            # Agent watch folders (per-agent task dispatch)
│   ├── commander/     # Claude Code (Opus) incoming
│   ├── adjudicator/   # Codex CLI incoming
│   ├── cartographer/  # Gemini CLI incoming
│   ├── ajna/          # OpenClaw Kimi K2.5 incoming (MBA remote)
│   └── psyche/        # OpenClaw GPT-5.3-codex incoming (Mac mini)
├── -OUTGOING/         # CLI > WebApp prompt staging
└── -SOVEREIGN/        # Async decision queue
```

---

## Handoff Protocol

| Transition | Target |
|------------|--------|
| Claude > ChatGPT | 30 sec |
| ChatGPT > Gemini | 20 sec |
| Gemini > Claude | 15 sec |
| Any > CLI | 10 sec |
| CLI > Repository | 5 sec |

---

## Sovereign Cockpit (Operational Infrastructure)

### 8-Layer Stack
```
1. Ghostty          Terminal emulator (macos-titlebar-style=hidden)
2. Zsh + P10k       Shell + prompt
3. tmux + sesh      Terminal multiplexer (session: constellation)
4. Bun              JavaScript runtime
5. Neovim/LazyVim   Code editor (in cockpit bottom panes)
6. Whisper/Piper    Offline STT/TTS
7. Doom Emacs       Observation Layer (standalone, NOT in cockpit)
8. Cursor           AI IDE (standalone)
```

### Display Geometry
- **Display**: 5120x1440 ultrawide
- **Grid**: 6 lanes horizontal, center 4 = cockpit
- **Window bounds**: {853, 0, 4267, 1440} via osascript
- **Font**: Liga SFMono Nerd Font, size 13 = 93 chars/lane
- **NO AEROSPACE** — disabled, conflicts with osascript bounds

### Cockpit Layout (Window 1: cockpit)

```
┌──────────┬──────────┬──────────┬──────────┐
│ PSYCHE   │ COMMANDER│ADJUDICATOR│CARTOGR. │  48 rows (SEARED)
│ OpenClaw │Claude Code│ Codex CLI│Gemini CLI│  (agent CLIs)
│ pane 1   │ pane 3   │ pane 5   │ pane 7   │  (odd = agents)
├──────────┼──────────┼──────────┼──────────┤
│  nvim    │  nvim    │  nvim    │  nvim    │  15 rows (SEARED)
│ pane 2   │ pane 4   │ pane 6   │ pane 8   │  (even = editors)
└──────────┴──────────┴──────────┴──────────┘
```

### SEARED Dimensions (Sovereign-Verified 2026-02-08)
```
Window height:    65 rows
Status bar:        1 row
Top pane (agent): 48 rows  (FORCED by resize-pane -y 48 via tmux hooks)
Border:            1 row
Bottom pane (nvim):15 rows  (auto: 65 - 1 - 48 - 1 = 15)
Total content:    63 rows   (48 + 15)
```

**Why absolute heights, not percentages**: `-l 25%` fails because Ghostty resize races with tmux split calculations. `exec tmux attach` triggers proportional redistribution that undoes pre-attach resize commands. Solution: tmux hooks (`client-attached` + `window-resized`) enforce `resize-pane -y 48` after every attach and terminal resize.

**Why nvim is launched directly**: `split-window "$NVIM_BIN"` passes `/opt/homebrew/bin/nvim` as the pane command. No shell intermediary. No PATH resolution. No aliases. No race condition. The old `send-keys` approach failed 3/4 times because shells weren't ready, nvim commands were silently dropped, and panes fell back to zsh with hostname as title.

### Keybindings (tmux.conf)
| Keybind | Target | Physical Pane |
|---------|--------|---------------|
| prefix+1 | Psyche (agent) | .1 |
| prefix+2 | Commander (agent) | .3 |
| prefix+3 | Adjudicator (agent) | .5 |
| prefix+4 | Cartographer (agent) | .7 |
| prefix+5 | nvim-Psyche | .2 |
| prefix+6 | nvim-Commander | .4 |
| prefix+7 | nvim-Adjudicator | .6 |
| prefix+8 | nvim-Cartographer | .8 |

### Watchers Window (Window 2: watchers)
```
┌────────────────┬────────────────┐
│ INBOX Triage   │ Git Status     │
│ (ls + triage)  │ (status + log) │
├────────────────┼────────────────┤
│ Agent Logs     │ System Monitor │
│ (tail -F)      │ (btop)         │
└────────────────┴────────────────┘
```

### Launch Commands
```bash
cockpit              # Create/attach (shells with banners)
cockpit --launch     # Create AND launch agent CLIs
cockpit --resize     # Reposition window + fix heights
cockpit --kill       # Kill constellation session
```

**CRITICAL**: After ANY cockpit.sh change: `cockpit --kill && cockpit`. Never reattach to stale sessions.

---

## Agent Assignments

| Pane | Agent | CLI | Platform | Role |
|------|-------|-----|----------|------|
| 1 | **Psyche** | `openclaw tui --session main` | OpenClaw (GPT-5.3-codex) | CTO, system cohesion, Mac mini resident |
| 2 | **Commander** | `claude --dangerously-skip-permissions` | Claude Code (Opus 4.6) | COO, primary executor, BLITZKRIEG lead |
| 3 | **Adjudicator** | `codex --full-auto` | Codex CLI (Sonnet) | CQO, standards, parallel execution |
| 4 | **Cartographer** | `gemini --yolo` | Gemini CLI (2.5 Pro) | CIO, corpus sensing, 1M context surveys |

### Agent Loop Architecture
Each agent runs a 7-phase always-on loop. Full specification: `00-ORCHESTRATION/state/ARCH-CONSTELLATION_AGENT_LOOPS.md`

```
1. ORIENT     → /claresce (situational awareness)
2. SITUATE    → /claresce (repo state)
3. CALIBRATE  → /claresce (CANON alignment)
4. TRIAGE     → /claresce (inbox) → /PLAN → /EXECUTE → DISPATCH
5. PROACTIVE  → /claresce (seek work) → /PLAN → /EXECUTE
6. SOVEREIGN  → /claresce (direct interaction) → update all systems
7. REPEAT
```

### Ajna (NOT in cockpit — remote on MacBook Air)
- **Platform**: OpenClaw (Kimi K2.5 via NVIDIA NIM API)
- **Machine**: MacBook Air (Apple Silicon)
- **Enterprise Role**: CSO (Chief Strategy Officer) — strategic direction, orchestration, dispatch
- **Communication**: Git sync via `-INBOX/ajna/`, Tailscale network
- **Archon**: Forms AjnaPsyche Archon with Psyche (CSO steering wheel + CTO rudder)
- **Status**: MBA configured — OpenClaw + NVIDIA provider active

---

## Always-On Services (12 total)

| Service | Label | Watches | Status |
|---------|-------|---------|--------|
| Commander Watcher | `com.syncrescendence.watch-commander` | `-INBOX/commander/00-INBOX0/` | ACTIVE |
| Adjudicator Watcher | `com.syncrescendence.watch-adjudicator` | `-INBOX/adjudicator/00-INBOX0/` | ACTIVE |
| Cartographer Watcher | `com.syncrescendence.watch-cartographer` | `-INBOX/cartographer/00-INBOX0/` | ACTIVE |
| Ajna Watcher | `com.syncrescendence.watch-ajna` | `-INBOX/ajna/00-INBOX0/` | ACTIVE |
| Psyche Watcher | `com.syncrescendence.watch-psyche` | `-INBOX/psyche/00-INBOX0/` | ACTIVE |
| Canon Watcher | `com.syncrescendence.watch-canon` | Registry-driven state files | ACTIVE |
| Emacs Server | `com.syncrescendence.emacs-server` | N/A (daemon) | ACTIVE |
| OpenClaw Gateway | `ai.openclaw.gateway` | Port 18789 (RPC) | ACTIVE |
| Chroma Server | `com.syncrescendence.chroma-server` | Port 8765 (semantic search) | ACTIVE |
| Webhook Receiver | `com.syncrescendence.webhook-receiver` | Port 8888 (events) | ACTIVE |
| Corpus Health | `com.syncrescendence.corpus-health` | 6h schedule (git + structure) | ACTIVE |
| QMD Update | `com.syncrescendence.qmd-update` | 1h schedule (BM25 index) | ACTIVE |
| Watchdog | `com.syncrescendence.watchdog` | 5min schedule (service health) | ACTIVE |

### Filesystem Kanban (watch_dispatch.sh)
```
00-INBOX0/ (PENDING)
  → mv to 10-IN_PROGRESS/ (claim + tag agent-hostname)
  → exit 0:   40-DONE/     + CONFIRM + RESULT + EXECLOG
  → exit 124: 30-BLOCKED/  + timeout notification
  → exit !=0: 50_FAILED/   + error report
```

**Bidirectional feedback mandatory**: Every execution produces CONFIRM + RESULT + EXECLOG piped back to dispatching agent via Reply-To header.

---

## Emacs Observation Layer (Layer 7)

Doom Emacs serves as a **read-only state monitor and dashboard** — NOT a code editor.

**Status**: CONFIGURED but DORMANT (2026-02-08)

### Operational
- Linear API: `SPC L f` fetches SYN team issues
- ClickUp API: `SPC U f` fetches tasks by list
- Dashboard: `SPC d s` (cockpit), `SPC d i` (intentions), `SPC d e` (exec log), `SPC d a` (agenda)
- Read-only enforcement on `00-ORCHESTRATION/state/` files
- Org-super-agenda with P0-P3, BLOCKED, IN-PROGRESS, agent-tag grouping

### Configured but Unused
- org-roam: Database empty (no .org files in repo)
- org-journal: Directory empty (no 2026 entries)
- org-capture: 8 templates defined, target .org files don't exist
- **Critical mismatch**: Repo uses .md, org expects .org — bridge needed

Launch: `doom-dash` (alias for `emacsclient -nw -c`)

---

## Hooks & Skills Inventory

### Active Hooks (5 scripts, executable but NOT registered in .claude/settings.json)
| Hook | Event | Script | Output |
|------|-------|--------|--------|
| Session Log | Stop | `session_log.sh` | DYN-SESSION_LOG.md |
| Ajna Pedigree | Stop | `ajna_pedigree.sh` | DYN-PEDIGREE_LOG.md |
| Execution Log | Stop | `create_execution_log.sh` | DYN-EXECUTION_STAGING.md |
| Intent Compass | UserPromptSubmit | `intent_compass.sh` | DYN-INTENTIONS_QUEUE.md |
| Pre-Compaction | PreCompact | `pre_compaction.sh` | Blocks if uncommitted |

### Active Skills (15+, all callable via /skillname)
| Category | Skills |
|----------|--------|
| Transformation | readize, listenize, audize, integrate, transcribe_youtube, transcribe_interview |
| Orchestration | execute, dispatch, triage, plan |
| Decision | claresce, pedigree, method_kaizen, reviewtrospective |
| Auxiliary | update_agent_memory, update_universal_ledger, intentions |

### Modus Operandi
- **Medley mode** (default): Each agent receives specialized prompts per its role. This is how the Constellation normally operates — NOT Chorus mode.
- **Chorus mode** (reserved): Same prompt to all platforms, integrate outputs afterward. Use only for deliberate parallel-identical experiments.
- **BLITZKRIEG**: Standard-bearer tactic — parallel lane execution across agents
- **Expanding**: Additional multi-agent tactics under development (Siege, Reconnaissance, Flanking, Entrenchment)
- **Each agent**: Can deploy their own swarm (subagents)

---

## Platform Configuration Summary

### Vizier — Claude Web (INTERPRETER)
- Project: "Syncrescendence IIC"
- Memory: Project-specific enabled
- Connectors: GitHub, Drive, Gmail
- Strength: Rapport, synthesis, past chat search

### Vanguard — ChatGPT Web (COMPILER)
- Project: "Syncrescendence Compiler"
- Memory: PROJECT-ONLY MODE (critical)
- Strength: Canvas, strategic blueprints, deterministic output

### Diviner — Gemini Web (DIGESTOR)
- Gem: "Constellation Digestor"
- Drive Link: Constellation-State/ (live sync)
- Strength: Multimodal clarification, infinite threads, TTS

---

## Semantic Notation (SN)

~80% token compression via hybrid symbol/operator/block notation.

**Symbols**: Psi = Syncrescendence, K = CANON, O = ENGINE, Sigma = SOURCE, Delta = DIRECTIVE, Lambda = LOG
**Operators**: `::` expands, `|` constrains, `>>` transforms, `:=` binds, `=>` implies, `<->` bidirectional
**Tools**: `sn_encode.py`, `sn_decode.py`, `SN_BLOCK_TEMPLATES.md`, `sn_symbols.yaml`

---

## Quick Reference

| Command | Effect |
|---------|--------|
| `cockpit` | Create/attach tmux cockpit |
| `cockpit --launch` | Create + launch agent CLIs |
| `cockpit --kill` | Kill constellation session |
| `doom-dash` | Launch Emacs Observation Layer |
| `/blitz` | Parallel directive mode |
| `/claresce` | Value-guided progressive refinement |
| `/triage` | Scan + categorize inbox |

---

## When In Doubt

1. Check the repository (ground truth)
2. Verify the fingerprint matches
3. Ask the Sovereign for clarification
4. Never assume context not explicitly provided

---

## Key References

| Reference | Path |
|-----------|------|
| Agent loop architecture | `00-ORCHESTRATION/state/ARCH-CONSTELLATION_AGENT_LOOPS.md` |
| Blitzkrieg buildout | `00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md` |
| Cockpit script | `00-ORCHESTRATION/scripts/cockpit.sh` |
| Dispatch watcher | `00-ORCHESTRATION/scripts/watch_dispatch.sh` |
| Fleet handbook | `02-ENGINE/REF-FLEET_COMMANDERS_HANDBOOK.md` |
| Terminology | `02-ENGINE/REF-ROSETTA_STONE.md` |
| Stack teleology | `02-ENGINE/REF-STACK_TELEOLOGY.md` |
| Clarescence runbook | `02-ENGINE/REF-CLARESCENCE_RUNBOOK.md` |

*This document provides orientation. For detailed implementation, see the referenced files.*
