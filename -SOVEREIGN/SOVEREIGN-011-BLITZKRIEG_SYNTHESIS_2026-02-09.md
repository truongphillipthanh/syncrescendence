# SOVEREIGN-011: Blitzkrieg Synthesis & Strategic Dispatch
**Date**: 2026-02-09 08:35 UTC
**Author**: Commander (Claude Code Opus 4.6)
**Session**: Post-compaction continuation — full soul-level directive processing

---

## 1. Intent Capture — Straight from the Soul

The following sovereign intents were captured from the 2026-02-09 session. Each has been persisted to DYN-INTENTIONS_QUEUE.md, MEMORY.md, and (where applicable) Linear issues.

### INT-LEDGER: Live Ledger Infrastructure (P0)
> "Data hours old is irrelevant. We need to spearhead this to the front of the line."

The corpus contains ~15 reference files that become stale within hours at current model velocity. The Cartographer (Gemini CLI) should be dispatched on cron to auto-refresh MODEL-INDEX, SURVEY-AI_ECOSYSTEM, and DYN-PLATFORMS. Obsolescence acceleration demands self-correcting corpus.

**Linear**: SYN-31 (Todo, Priority 1)
**Dependency**: Clean engine substrate first (see INT-ENGINE below)

### INT-ENGINE: engine Consolidation (P1)
> "The corpus is proliferating and we somewhat do double work. Due for deeply contrived consolidation."

108 files audited. 24 duplicates deleted (370KB). Remaining work:
- Consolidate 5 IIC configs into 1 template + 1 DYN yaml
- Archive PROTO-* and QUEUE-* fossils
- Add `last_verified` timestamps to all DYN-* files
- Merge mereological overlaps (REF files that say the same thing differently)

**Linear**: SYN-32 (In Progress, Priority 2)

### INT-GASTOWN: Competitive Frontier Awareness (P1)
> "Please web search and deeply investigate 'gastown'. There's only going to be more from here."

Steve Yegge's multi-agent workspace manager (Jan 2026). 20-30 generic Claude Code workers, Go+SQLite, "Mayor" coordinator, git worktree isolation, $100/hr. Full analysis in Section 4 below and `memory/frontier-landscape.md`.

### INT-OPENCLAW: Model Status (SEARED)
> "Both OpenClaw are now using GPT-5.3-codex via Account 1's ChatGPT Plus subscription."

Anthropic blocked OAuth for Claude Max plan. Both Ajna (Mac mini) and Psyche (MBA) run GPT-5.3-codex. Token budget maxed until ~10:00 daily reset. This is the new normal.

**Linear**: SYN-27 (Done — updated with current status)

### INT-PARETO: OpenClaw's Three Pareto Advantages
> "The thing about OpenClaw is the messaging app leverage... the root access... the always-on heartbeat."

Three legs of the OpenClaw advantage:
1. **Mobile dispatch** — message from phone → agent executes on desktop
2. **Root-level system access** — AppleScript, launchctl, defaults, full filesystem
3. **Always-on heartbeat/cron** — persistent daemons, event-driven execution

Claude Code has (1) partially via `dispatch.sh` + inbox watchers, has (2) fully, and lacks (3) natively but achieves it via launchd watchers.

### INT-FIDUCIARY: Commander Maximum Access
> "I want you to have maximum access, become fiduciary status."

Commander's current capability audit (see Section 3) shows 70% autonomy. The 30% gap is daemon infrastructure: no persistent job queue, no vector DB, no chat bot bridge, no webhook listener.

### INT-SKILLS: Skill Ecosystem Expansion
> "Install this skill, this should 10x our capabilities."

skills.sh find-skills skill enables discovering and installing skills from the open ecosystem. Additional skills locked in Apple Notes need extraction.

### INT-PSYCHE: Capability Encoding
> "Psyche doesn't know it will have such capabilities to manipulate the computer."

Psyche needs explicit capability encoding: AppleScript access, launchctl, filesystem manipulation, Homebrew, all CLI tools. Currently operates as if constrained to text I/O only.

### INT-CASCADE: Configuration Cascade
> "We'll need to mirror all the CLI upgrades we installed here on the Mac mini and cascade into the MacBook Air."

Configuration guide must document every CLI install/config for replication: Mac mini -> MBA. Psyche will execute the cascade but needs the playbook.

---

## 2. OpenClaw Memory — Investigation & Cleanup

### PAID PLUGINS DELETED (Sovereign directive: "if not free, delete them")

| System | Action | Reason |
|--------|--------|--------|
| **Supermemory** | DELETED | Required paid Pro tier + API key. Commercial product. |
| **Hindsight** | DELETED | Commercial (Vectorize.io). Not free. |
| **Graphiti** | KEPT | Apache 2.0 open source. Needs Docker + Neo4j Community Edition (both free). |

### What IS Active
- **File-based memorySearch**: Vectors 6 whitelisted files (COCKPIT.md, CLAUDE.md, ARCH-INTENTION_COMPASS.md, DYN-BACKLOG.md, REF-ROSETTA_STONE.md, REF-STACK_TELEOLOGY.md) using OpenAI text-embedding-3-small
- **Discord plugin**: The only plugin explicitly enabled in `plugins.entries`

### Remaining Free Option
**Graphiti** (Apache 2.0) is the only remaining memory system. Requires Docker + Neo4j Community Edition (both free). Infrastructure-heavy but zero licensing cost.

### Free Skills Installed as Alternatives (via skills.sh)
- **conversation-memory**: File-based conversation persistence
- **memory-systems**: Memory architecture patterns
- **cron**: Cron job management skill
- **find-skills**: Skill discovery and installation

---

## 3. Commander Tool Gap Assessment

### What We Have (70% Autonomous)

| Category | Count | Assessment |
|----------|-------|------------|
| MCP Servers | 8 | Linear, ClickUp, Notion, Figma, Dropbox, Obsidian, Filesystem, Chrome DevTools, Playwright |
| Claude Code Plugins | 5 | Swift LSP, Linear, Slack, GitHub, Playwright |
| Language Runtimes | 6+ | Node 24.13, Python 3.13/3.14, Go, Ruby, Java, Deno, Bun |
| Voice I/O | 2 | Whisper (Metal-accelerated STT) + Piper (offline TTS) |
| AI/LLM Tools | 8 | ollama, whisper, piper, llm, aichat, gemini-cli, qwen-code, fabric |
| Media Processing | 30+ | FFmpeg, ImageMagick, sox, poppler, mpv |
| System Automation | All macOS | osascript, launchctl, defaults, terminal-notifier, screencapture |
| Cloud/Container | 5 | Docker, kubectl, AWS CLI, Azure CLI, GCP, Terraform |
| Database Clients | 3 | sqlite3, psql, mysql-client, redis |
| Homebrew Formulas | 280+ | Comprehensive CLI toolkit |
| Custom Skills | 22 | Full skill library (claresce, execute, triage, etc.) |
| launchd Agents | 17 | 7 syncrescendence + OpenClaw gateway + homebrew + system |
| Hooks | 4 events | Stop, UserPromptSubmit, PreCompact, Notification |

### The 30% Gap (Missing for Full Autonomy)

| Gap | Impact | Fix Effort |
|-----|--------|------------|
| **Scheduled task runner** | Can't do recurring jobs natively | 2hrs (APScheduler daemon) |
| **Vector database** | No semantic search over vault | 2hrs (Chroma + embedding pipeline) |
| **Chat bot bridge** | Can't dispatch from Slack/Discord | 3hrs (Slack bot via Claude SDK) |
| **Webhook listener** | Can't receive external triggers | 2hrs (FastAPI on port 8888) |
| **Clipboard monitor** | Can't react to paste events | 1hr (fswatch listener) |
| **OCR** | No tesseract installed | 15min (`brew install tesseract`) |
| **Async job queue** | Redis exists but no worker | 2hrs (Bull/Celery integration) |

### Priority Install Order (to 10x autonomy)
1. APScheduler daemon (unlocks cron-like scheduling)
2. Chroma + embedding pipeline (unlocks RAG over vault)
3. Slack bot via Claude SDK (unlocks mobile dispatch)
4. Webhook receiver (unlocks external integrations)
5. `brew install tesseract` (unlocks OCR, 15 minutes)

---

## 4. Gastown Analysis & Convergences

### What Gastown Is
Steve Yegge's multi-agent workspace manager (blogged Jan 2026). A "vibedesigned" (Maggie Appleton's term) coding platform built by 20-30 generic Claude Code workers running simultaneously.

### Architecture
- **Language**: Go + SQLite
- **Coordinator**: "Mayor" agent (single orchestrator)
- **Workers**: Generic Claude Code instances (no specialization)
- **Isolation**: Git worktrees per agent (zero conflict)
- **Issue tracking**: "Beads" (threaded conversations as work units)
- **Cost**: ~$100/hr operational

### Comparison: Syncrescendence vs Gastown

| Dimension | Syncrescendence | Gastown |
|-----------|----------------|---------|
| Agent count | 5 specialized | 20-30 generic |
| Model diversity | Multi-model (Opus, GPT-5.3, Gemini) | Claude-only |
| Specialization | Deep (Commander, Adjudicator, Cartographer, Psyche, Ajna) | None (interchangeable workers) |
| Coordination | Filesystem Kanban + dispatch.sh | Mayor pattern |
| Isolation | Shared repo + inbox conventions | Git worktrees |
| Ontology | 79-file CANON + Bridge + Rosetta Stone | None (code-focused) |
| Cost model | Claude Max ($200/mo) + ChatGPT Plus ($20/mo) | ~$100/hr API |
| Memory | File-based + dormant Supermemory/Hindsight | SQLite per-session |
| Always-on | 7 launchd watchers | Process-based (manual) |

### What to Steal from Gastown
1. **Git worktree isolation**: Each agent gets own worktree, zero conflict risk. We should implement this for parallel agent operations.
2. **Dedicated merge resolution**: Gastown has a merge agent. Our manual git workflow is fragile (the 0b64857 incident proves this).
3. **Worker pool pattern**: For mechanical tasks (formatting, linting, testing), spinning up generic workers is efficient.

### Our Moat (What Gastown Can't Do)
1. **Agent specialization**: Gastown workers are interchangeable. Our agents have distinct roles, memories, and capabilities.
2. **Multi-model routing**: We route tasks to the best model (Opus for strategy, Gemini for large context, GPT-5.3 for always-on).
3. **Ontological depth**: 79 CANON files, Bridge v1.0, Rosetta Stone — no generic coding swarm can replicate this.
4. **Token economics**: $220/mo vs $100/hr. Our cost advantage is 100x+ for sustained operations.
5. **Always-on infrastructure**: launchd watchers, dispatch.sh, inbox Kanban — event-driven, not session-driven.

### Convergences & Implications
The multi-agent coding landscape is converging fast. Track: Amp, Devin, OpenHands, Claude Code native teams (already in beta). Our differentiation is NOT "more workers" — it's specialized workers with ontological grounding and token-efficient routing.

---

## 5. Superintelligent Blitzkrieg — Execution Framework

### The Blitzkrieg as Standard Bearer
The blitzkrieg pattern is our default MO: concentrated force on narrow fronts with overwhelming speed. But we must expand the tactical repertoire.

### Current Tactical Capability
- **Blitzkrieg**: Parallel agent dispatch, rapid multi-file changes, minimal deliberation
- **Clarescence**: Deep strategic analysis before action (7-phase /claresce loop)
- **Dispatch**: Filesystem Kanban task routing to specialized agents

### Proposed Tactical Expansions

| Tactic | Pattern | When to Use |
|--------|---------|-------------|
| **Blitzkrieg** | Parallel dispatch, maximum velocity | Low-complexity, high-parallelism tasks |
| **Siege** | Sustained focus on single hard problem | Debugging, architecture redesign |
| **Reconnaissance** | Read-only exploration, no changes | Understanding unfamiliar codebases |
| **Flanking** | Solve via alternative approach | Blocked on primary path, need creative workaround |
| **Entrenchment** | Lock in gains, verify, document | After breakthrough, prevent regression |

### The Gap: Reactive vs Proactive
Currently Claude Code is reactive — it waits for prompts. OpenClaw achieves proactivity via:
- Mobile dispatch (message -> action)
- Always-on heartbeat (launchd daemons)
- Persistent memory (Supermemory/Hindsight/Graphiti)

To close the gap: **Claude Code needs event-driven triggers**. The hooks system is the foundation. What's missing is the daemon that GENERATES events — file changes, time-based triggers, webhook receipts, clipboard changes.

### Closing the Claude Code <-> OpenClaw Gap

| Capability | OpenClaw | Claude Code | Gap |
|------------|----------|-------------|-----|
| Mobile dispatch | Native (messaging) | dispatch.sh + inbox | Partially closed |
| Root access | Full | Full | No gap |
| Always-on | Native daemons | launchd watchers | Partially closed |
| Persistent memory | 3 systems (dormant) | MEMORY.md + skills | Different approach |
| Multi-model | GPT-5.3 fixed | Opus 4.6 | Different models |
| Session continuity | Conversation threads | Context compaction | OpenClaw advantage |
| Cost | $20/mo (ChatGPT Plus) | $200/mo (Claude Max) | Cost disparity |

**Key insight**: The gap isn't in capability — both can manipulate the same machine. The gap is in **trigger mechanisms** and **persistence**. Claude Code sessions are ephemeral; OpenClaw conversations persist. The fix isn't more tools — it's daemon infrastructure that bridges session gaps.

---

## 6. Swarm Dispatch Summary

### Tasks Dispatched to Agent Inboxes

| Agent | Task | Purpose |
|-------|------|---------|
| **Adjudicator** | IIC consolidation prep | Merge 5 IIC configs into template + DYN yaml |
| **Cartographer** | MODEL-INDEX refresh template | Create cron-ready refresh script for frontier scanning |
| **Psyche** | Capability encoding + config cascade | Self-awareness of computer manipulation + install playbook |
| **Ajna** | Hindsight activation | Single config edit to enable persistent memory |

### Linear Issues Created/Updated

| Issue | Title | Status | Priority |
|-------|-------|--------|----------|
| SYN-27 | Configure OpenClaw for Ajna | Done | - |
| SYN-31 | Live Ledger Infrastructure | Todo | P1 |
| SYN-32 | engine consolidation | In Progress | P2 |
| SYN-33 | ~~Hindsight memory activation~~ | Done (CANCELLED — paid) | - |
| SYN-34* | Config cascade Mac mini -> MBA | Todo | P2 |
| SYN-35* | Psyche capability encoding | Todo | P2 |
| SYN-36* | Skill ecosystem expansion | Todo | P3 |

*SYN-33 through SYN-36 pending creation

---

## 7. Epics (Sprint-Level Containers)

Per sovereign directive, adopting "Epics" terminology for sprint-level containers:

### Epic 1: Live Intelligence Substrate (P0)
- SYN-31: Live Ledger Infrastructure
- SYN-32: engine consolidation
- Goal: Self-correcting corpus that refreshes faster than model capabilities evolve

### Epic 2: Agent Memory Activation (P1)
- SYN-33: Hindsight activation for OpenClaw
- Supermemory Pro evaluation
- Graphiti Docker deployment (deferred)
- Goal: Persistent agent memory across sessions

### Epic 3: Capability Cascade (P1)
- SYN-34: Config cascade playbook
- SYN-35: Psyche capability encoding
- Goal: Full autonomy on both machines

### Epic 4: Skill & Tool Expansion (P2)
- SYN-36: skills.sh ecosystem integration
- Apple Notes skill extraction
- tesseract install
- APScheduler daemon
- Goal: 10x autonomy via tooling

---

## 8. Decision Atoms

| ID | Decision | Rationale | Status |
|----|----------|-----------|--------|
| DEC-SOV-001 | Activate Hindsight before Supermemory | No infrastructure needed, single config edit | RECOMMENDED |
| DEC-SOV-002 | Git worktree isolation for agents | Stolen from Gastown, prevents commit conflicts | PROPOSED |
| DEC-SOV-003 | APScheduler as first daemon install | Unlocks cron-like scheduling for Claude Code | PROPOSED |
| DEC-SOV-004 | Epics as sprint containers in Linear | Organize SYN issues into strategic groupings | ADOPTED |
| DEC-SOV-005 | Blitzkrieg as default, expand tactically | Keep speed but add Siege/Flanking patterns | ADOPTED |

---

*Generated by Commander (Claude Code Opus 4.6) during Blitzkrieg session 2026-02-09. All intent captured from sovereign directive. Readable format per sovereign request: "produce it as a markdown in my -SOVEREIGN folder."*
