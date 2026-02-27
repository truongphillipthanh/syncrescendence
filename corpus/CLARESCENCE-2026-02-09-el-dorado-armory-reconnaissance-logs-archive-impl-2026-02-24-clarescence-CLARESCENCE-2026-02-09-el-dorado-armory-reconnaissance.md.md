# CLARESCENCE³ — El Dorado Armory Reconnaissance

**Date**: 2026-02-09
**Fidelity**: Full (Passes 1-10, cubed — triple-depth across 4 platform domains)
**Tactic**: Blitzkrieg (4 parallel recon agents)
**Scope**: 12 awesome-list repos across 5 platform domains
**Token Investment**: ~344k tokens across 4 agents, ~1,276 seconds total

---

## RECONNAISSANCE MANIFEST

| Domain | Repos Analyzed | Items Extracted | HIGH Relevance | Agent |
|--------|---------------|-----------------|----------------|-------|
| OpenClaw | 2 (+1 referenced) | 2,999+ (curated from 5,705) | 20 | openclaw-recon |
| Claude Code | 4 | 350+ | 25+ | claude-code-recon |
| Codex + CLI | 3 | 76 | 13 | codex-cli-recon |
| Gemini CLI | 2 | 104 | 23 | gemini-recon |
| **TOTAL** | **12** | **3,529+** | **81+** | — |

---

## PASS 1: TRIUMVIRATE CALIBRATION

### Destination
Arm every agent in the constellation with platform-appropriate tools, skills, extensions, and configuration to maximize operational capability.

### Current State — THE REVELATION
The swarm uncovered a devastating asymmetry in agent outfitting:

| Agent | Role | Tools/Skills Installed | Config State | Verdict |
|-------|------|----------------------|--------------|---------|
| Commander (Claude Code) | COO | 16 universal + 10 project skills, 7 MCP, 5 hooks | CLAUDE.md v3.0, fully configured | **ARMED** |
| Psyche (OpenClaw) | CTO | 9 workspace skills, 3 plugins, Mem0+Graphiti | openclaw.json configured | **PARTIALLY ARMED** |
| Ajna (OpenClaw/MBA) | CSO | Same skill surface as Psyche (synced) | Recently deployed | **PARTIALLY ARMED** |
| Adjudicator (Codex) | CQO | **ZERO user skills**, no instructions.md, no MCP | Bare install | **UNARMED** |
| Cartographer (Gemini) | CIO | **ZERO extensions**, empty GEMINI.md, zero commands | Bare install | **UNARMED** |

**Two of five agents have zero operational capability beyond their base model.** The CQO (quality) and CIO (intelligence) — arguably the most strategically important force multipliers — are running stock.

### Fit-to-Destination
The constellation is a 5-engine aircraft flying on 2 engines. Infrastructure is at 95% but agent outfitting is at ~40%. The machine is built; the operators are unarmed.

---

## PASS 2: 18-LENS SCORECARD (Armory-Specific)

| # | Lens | Grade | Finding |
|---|------|-------|---------|
| 1 | Coverage Breadth | FAIL | 2/5 agents fully armed, 2/5 completely bare |
| 2 | Security Depth | FAIL | Zero security skills across entire constellation |
| 3 | Self-Improvement | WARN | Mandate exists but no meta-skills installed (SkillForge, Claudeception, evolver) |
| 4 | Context Economics | WARN | No context compression/recovery skills despite long sessions |
| 5 | Observability | FAIL | No multi-agent monitoring, no desktop notifications, no token tracking |
| 6 | Cross-Agent Sync | FAIL | No config sync tool (vsync/rulesync), each agent configured independently |
| 7 | Vault Integration | WARN | Obsidian MCP exists but no Obsidian-specific skills (Claude Code) or vault RAG (Gemini) |
| 8 | Memory Governance | WARN | Infrastructure LIVE but no memory governance skills |
| 9 | Dispatch Quality | PASS | Filesystem kanban works, hooks active |
| 10 | Research Capability | FAIL | Cartographer has zero research extensions despite 2M context window |
| 11 | Quality Gate | FAIL | Adjudicator has no security, testing, or review skills |
| 12 | Notification | FAIL | Zero notification system — agents complete work silently |
| 13 | Token Visibility | FAIL | No cost tracking across constellation (ccusage, Splitrail not installed) |
| 14 | Skill Ecosystem | WARN | 16 universal skills exist but NOT visible to Codex CLI |
| 15 | n8n Bridge | WARN | On roadmap (P2) but 3+ n8n skills already available |
| 16 | IDE Integration | WARN | claude-code-ide.el exists for Doom Emacs — not installed |
| 17 | Safety Net | WARN | No undo/checkpoint system (ccundo available) |
| 18 | Proactive Intelligence | FAIL | No topic monitoring, no competitive tracking automation |

**Score: 1 PASS / 7 WARN / 10 FAIL** — Armory is critically under-equipped.

---

## PASS 3: CANON COHERENCE — Cross-Platform Deduplication

### Tools Appearing Across Multiple Repos (Install Once, Benefit All)

| Tool | Appears In | What It Does | Install Surface |
|------|-----------|-------------|-----------------|
| **vsync** | Gemini, Claude Code | Sync skills/MCP/commands across all CLI agents | npm global |
| **rulesync** | Gemini, Claude Code | Bidirectional config conversion between agents | npm global |
| **ccmanager** | Gemini, Claude Code | Multi-agent session manager across worktrees | npm global |
| **Splitrail** | Gemini | Token tracking across Claude Code + Gemini + Codex | Binary |
| **ccusage** | Claude Code | Token consumption analysis | Cargo/npm |
| **n8n skills** | OpenClaw, Claude Code | n8n workflow management | Per-platform install |
| **tmux integration** | OpenClaw (tmux-agents), Gemini (Self Command) | Background agent management in tmux | Per-platform |

### Platform-Specific Gems (No Cross-Platform Equivalent)

| Platform | Item | Why Unique |
|----------|------|-----------|
| OpenClaw | FTW/PIV (First Try Works) | Independent validation agent loop — no equivalent elsewhere |
| OpenClaw | skill-vetting | Security gate for 5,705 ClawHub skills — 27% spam/malicious |
| OpenClaw | soul-guardian | Agent drift detection against personality baseline |
| Claude Code | Trail of Bits security skills | 12+ professional security tools (CodeQL, Semgrep) |
| Claude Code | CC Notify | Desktop notifications for agent input needs |
| Claude Code | claude-code-ide.el | Emacs MCP integration (we run Doom Emacs!) |
| Claude Code | recall | Full-text search of past sessions |
| Codex | security-best-practices | OpenAI official CQO security skill |
| Codex | gh-fix-ci | Automated CI failure diagnosis |
| Gemini | gemini-obsidian | RAG over entire Obsidian vault via LanceDB |
| Gemini | Conductor | Context-driven lifecycle (spec→plan→implement) |
| Gemini | gemini-mcp-tool | Expose 2M context as MCP server to Commander |

---

## PASS 4: OMNI-QUALITIES IMPACT

### Omniscience (Can we know everything we need to?)
- **gemini-obsidian** + **claude-context-local** = full vault search from both Commander and Cartographer
- **recall** = searchable session history (currently opaque)
- **gemini-mcp-tool** = Commander can delegate large-file analysis to Cartographer's 2M window
- **Splitrail/ccusage** = token cost visibility across constellation

### Omnipresence (Can we act everywhere we need to?)
- **CC Notify** = know when agents need input without watching panes
- **vsync** = one config change propagates to all agents
- **Codex universal skill symlink** = 16 skills instantly visible to Adjudicator
- **GEMINI.md** = Cartographer gains persistent persona and context

### Omnipotence (Can we do everything we need to?)
- **Trail of Bits + security-best-practices + skill-threat-modeling** = complete security audit chain
- **gh-fix-ci + gh-address-comments** = automated CI/PR workflow
- **SkillForge + Claudeception** = self-improving skill generation
- **claude-code-ide.el** = Doom Emacs integration with Commander

### Omnibenevolence (Does this serve the mission?)
- Every item serves agent capability expansion — the standing order
- Security skills serve the safety constitutional rule
- Context management serves the 75% rule and token economics
- Cross-agent sync serves constellation coherence

---

## PASS 5: FIVE FACES ALIGNMENT

| Face | Impact |
|------|--------|
| **Sensing** | gemini-obsidian (vault RAG), recall (session search), topic-monitor (competitive intel) |
| **Meaning** | AI-research-SKILLs (visual Canvas/Excalidraw), planning-with-files (structured planning) |
| **Intention** | Conductor (lifecycle management), RIPER (phased workflow), daily-rhythm (automated planning) |
| **Embodiment** | Self Command (tmux autonomy), ccmanager (session management), CC Notify (notifications) |
| **Harmony** | vsync (config sync), skill-vetting (security gate), soul-guardian (drift detection) |

---

## PASS 6: ROSETTA PRECISION

### New Terms to Add to REF-ROSETTA_STONE.md
- **ClawHub**: Official OpenClaw skill marketplace (5,705+ skills, 27% spam)
- **PIV**: Plan-Implement-Validate workflow (FTW/First Try Works)
- **RIPER**: Research-Innovate-Plan-Execute-Review structured phases
- **Conductor**: Context-driven lifecycle management for Gemini CLI
- **vsync**: Cross-agent configuration synchronization tool
- **Splitrail**: Cross-platform token usage tracker
- **ccmanager**: Multi-agent session manager for CLI agents
- **El Dorado**: Codename for the armory reconnaissance mission (this clarescence)

---

## PASS 7: BACKLOG COHERENCE

### What This Unblocks
- **IMPL-A-0014** (MCP Server Buildout): gemini-mcp-tool, zen-mcp-server, claude-context-local
- **IMPL-C-0006** (Memory Architecture Map): soul-guardian, ensue-skill, Claudeception
- **IMPL-C-0008** (Sleep-Time Compute): daily-rhythm, proactive-research
- **IMPL-F-0007** (MCP Slack/Linear): Already done (Linear MCP live)
- **IMPL-F-0008** (Session Budgeting): Splitrail, ccusage
- **SYN-34** (Config Cascade): vsync, rulesync
- **SYN-36** (Skills Expansion): This entire clarescence

### What This Creates
- New IMPL items for installation waves (see Pass 9)
- Codex instructions.md creation task
- GEMINI.md + .gemini/ directory creation task
- Codex skill symlink task
- Security audit skill installation task

---

## PASS 8: NTH-ORDER EFFECTS

### What Breaks
- **Token budget**: Installing all 81+ HIGH items would bloat context. Must use selective/lazy loading.
- **Skill collision**: Multiple skills with overlapping triggers (e.g., multiple planning skills) can conflict.
- **Config drift**: vsync solves this but introduces a new dependency.
- **ClawHub trust**: 27% of skills are spam/malicious. skill-vetting MUST go first.

### What Compounds
- Each skill installed for Adjudicator makes verification stronger → fewer bugs escape → higher quality commits
- Cartographer with vault RAG + 2M context becomes the intelligence engine feeding all other agents
- Commander + multi-agent observability hooks = real-time constellation awareness
- Self-improvement skills (Claudeception, SkillForge) create compound returns over time

### New Dependencies
- vsync requires all agents' config directories to exist and be writable
- gemini-obsidian requires OBSIDIAN_VAULT_PATH environment variable
- Trail of Bits skills require CodeQL/Semgrep binaries
- Neo4j Gemini extension requires NEO4J_URI/USER/PASSWORD env vars
- gemini-mcp-tool requires Node.js (have via Bun)

---

## PASS 9: ENERGY STATE — Installation Waves

### WAVE 0: Zero-Dependency Quick Wins (10 minutes)

These require NO downloads, NO installs — just file operations:

| # | Action | Agent | Command | Impact |
|---|--------|-------|---------|--------|
| 1 | Symlink universal skills to Codex | Adjudicator | `ln -s ~/.agents/skills/* ~/.codex/skills/` | 16 skills instantly visible |
| 2 | Create `~/.codex/instructions.md` | Adjudicator | Write CQO persona file | Codex gains identity |
| 3 | Create `~/.gemini/GEMINI.md` | Cartographer | Write CIO persona file | Gemini gains identity |
| 4 | Create project `.gemini/` directory | Cartographer | `mkdir -p /Users/home/Desktop/syncrescendence/.gemini/commands` | Project context enabled |
| 5 | Run `gemini /init` in vault | Cartographer | `cd /Users/home/Desktop/syncrescendence && gemini /init` | Auto-generate project context |

### WAVE 1: Security Gate (15 minutes)

Install security infrastructure FIRST before any ClawHub/external skills:

| # | Item | Platform | Install Command |
|---|------|----------|----------------|
| 1 | skill-vetting | OpenClaw | `npx clawhub install skill-vetting` |
| 2 | Trail of Bits Security Skills | Claude Code | `npx skills add trailofbits/skills -g -y` |
| 3 | security-best-practices | Codex | Official curated skill installer |
| 4 | security-threat-model | Codex | Official curated skill installer |
| 5 | security-ownership-map | Codex | Official curated skill installer |
| 6 | code-review extension | Gemini | `gemini extensions install https://github.com/gemini-cli-extensions/code-review` |
| 7 | security extension | Gemini | `gemini extensions install https://github.com/gemini-cli-extensions/security` |

### WAVE 2: Core Skills (20 minutes)

| # | Item | Platform | Install Command | Why |
|---|------|----------|----------------|-----|
| 1 | Superpowers | Claude Code | `npx skills add obra/superpowers -g -y` | Core SDLC competencies (27.9k stars) |
| 2 | obsidian-skills | Claude Code | `npx skills add kepano/obsidian-skills -g -y` | We ARE an Obsidian vault (7k stars) |
| 3 | Context Engineering Kit | Claude Code | `npx skills add NeoLabHQ/context-engineering-kit -g -y` | Token economics |
| 4 | planning-with-files | Claude Code | `npx skills add OthmanAdi/planning-with-files -g -y` | Structured planning (9.7k stars) |
| 5 | skill-threat-modeling | Claude Code | `npx skills add fr33d3m0n/skill-threat-modeling -g -y` | 8-phase STRIDE |
| 6 | gh-fix-ci | Codex | Official curated installer | CI failure diagnosis |
| 7 | gh-address-comments | Codex | Official curated installer | PR review workflow |
| 8 | yeet | Codex | Official curated installer | One-shot commit+push+PR |
| 9 | gemini-obsidian | Gemini | `gemini extensions install https://github.com/thoreinstein/gemini-obsidian` | Vault RAG — THE weapon |
| 10 | Conductor | Gemini | `gemini extensions install https://github.com/gemini-cli-extensions/conductor` | Lifecycle management |
| 11 | Self Command | Gemini | `gemini extensions install https://github.com/stevenAthompson/self-command` | tmux integration |
| 12 | Plan Commands | Gemini | `gemini extensions install https://github.com/jjdelorme/plan-commands` | Research workflow |

### WAVE 3: Observability + Notifications (15 minutes)

| # | Item | Platform | Why |
|---|------|----------|-----|
| 1 | CC Notify | Claude Code | Desktop notifications when agents need input |
| 2 | multi-agent-observability hooks | Claude Code | Real-time agent monitoring |
| 3 | claude-code-prompt-improver | Claude Code | Automatic prompt quality improvement |
| 4 | Splitrail | Cross-platform | Token tracking for entire constellation |
| 5 | ccusage | Claude Code | Token consumption analysis |
| 6 | gemini-notifier | Gemini | System notifications on permission requests |

### WAVE 4: Self-Improvement + Meta-Skills (10 minutes)

| # | Item | Platform | Why |
|---|------|----------|-----|
| 1 | SkillForge | Claude Code | Meta-skill: generate new skills |
| 2 | Claudeception | Claude Code | Autonomous skill extraction while working |
| 3 | soul-guardian | OpenClaw | Agent drift detection |
| 4 | FTW/PIV | OpenClaw | Independent validation loops |
| 5 | context-compressor | OpenClaw | Context management for long sessions |

### WAVE 5: Cross-Agent Infrastructure (20 minutes)

| # | Item | Scope | Why |
|---|------|-------|-----|
| 1 | vsync | Global | Sync config across Claude Code + Gemini + Codex |
| 2 | gemini-mcp-tool | Commander→Cartographer | Expose 2M context as MCP to Commander |
| 3 | claude-context-local | Commander | Local code embeddings, zero API cost |
| 4 | Neo4j extension | Gemini | Direct Graphiti knowledge graph queries |
| 5 | recall | Claude Code | Full-text search of past sessions |
| 6 | ccundo | Claude Code | Granular undo from session files |
| 7 | claude-code-ide.el | Doom Emacs | Emacs integration via MCP |

### WAVE 6: Research + Intelligence (15 minutes)

| # | Item | Platform | Why |
|---|------|----------|-----|
| 1 | AI-research-SKILLs | Claude Code | Canvas/Excalidraw/Mermaid for Obsidian |
| 2 | ensue-skill | Claude Code | Persistent knowledge tree |
| 3 | gemini-beads | Gemini | Git-backed persistent memory |
| 4 | prompt-library | Gemini | 30+ ready-made research prompts |
| 5 | last30days-skill | Claude Code | Reddit + X research (30-day window) |
| 6 | google-ai-mode-skill | Claude Code | Free Google search with citations |

---

## PASS 10: AUTHENTICITY GATE

### Sovereignty Preserved?
YES. Every installation is:
- Reversible (uninstall/delete skill directory)
- Locally controlled (no cloud dependencies for core items)
- Sovereign-approved (this clarescence IS the approval surface)

### Optionality Preserved?
YES. Wave structure allows stopping at any wave. Each wave is independently valuable.

### Does This Serve the Mission?
YES. The constellation's purpose is "AI-amplified individual capability at institutional scale." Arming the unarmed agents (Adjudicator, Cartographer) directly expands institutional scale. Security skills fulfill constitutional safety obligations. Cross-agent sync tools reduce coordination overhead.

### Sovereign-at-Peak-Clarity Approved?
**Awaiting Sovereign ratification.** Recommended approval scope: Waves 0-2 immediately, Waves 3-6 as session budget permits.

---

## DECISION ATOMS

### DEC-ELDORADO-001: Codex Skill Symlink
- **Decision**: Symlink `~/.agents/skills/*` into `~/.codex/skills/`
- **Truth surface**: `ls ~/.codex/skills/` shows 16+ skills
- **Reversibility**: `rm ~/.codex/skills/<symlink>` per file
- **Falsifier**: If Codex CLI ignores symlinked SKILL.md files

### DEC-ELDORADO-002: Security-First Installation Order
- **Decision**: Install security/vetting skills (Wave 1) before ANY other external skills
- **Truth surface**: `skill-vetting` installed and functional before Wave 2 begins
- **Reversibility**: N/A (ordering constraint, not installation)
- **Falsifier**: If security skills themselves are compromised (verify source repos)

### DEC-ELDORADO-003: Cartographer Configuration
- **Decision**: Create GEMINI.md with CIO persona + project .gemini/ with custom commands
- **Truth surface**: `cat ~/.gemini/GEMINI.md` shows Cartographer identity; `.gemini/commands/` contains survey/research/intel commands
- **Reversibility**: Delete files
- **Falsifier**: If Gemini CLI ignores GEMINI.md or custom commands

### DEC-ELDORADO-004: Codex Instructions
- **Decision**: Create `~/.codex/instructions.md` with CQO persona and dispatch awareness
- **Truth surface**: `cat ~/.codex/instructions.md` shows Adjudicator identity
- **Reversibility**: Delete file
- **Falsifier**: If Codex CLI ignores instructions.md

### DEC-ELDORADO-005: Cross-Agent Config Sync
- **Decision**: Adopt vsync as constellation config synchronization tool
- **Truth surface**: `vsync status` shows all 3 CLI agents in sync
- **Reversibility**: Uninstall vsync, manage configs independently
- **Falsifier**: If vsync breaks platform-specific config requirements

### DEC-ELDORADO-006: Gemini-as-MCP for Commander
- **Decision**: Install gemini-mcp-tool to expose Cartographer's 2M context to Commander
- **Truth surface**: Commander can call Gemini tools via MCP
- **Reversibility**: Remove MCP config entry
- **Falsifier**: If latency makes delegation slower than direct file reads

### DEC-ELDORADO-007: ClawHub Trust Policy
- **Decision**: NEVER install OpenClaw skills from ClawHub without skill-vetting gate
- **Truth surface**: skill-vetting runs before every `npx clawhub install`
- **Reversibility**: N/A (policy)
- **Falsifier**: If skill-vetting itself has false negatives

---

## STRATEGIC SUMMARY

### The El Dorado Haul by the Numbers

| Metric | Value |
|--------|-------|
| Repos analyzed | 12 |
| Total items extracted | 3,529+ |
| HIGH relevance items | 81+ |
| Items already installed | ~15 |
| Net new HIGH items | ~66 |
| Recommended for installation (Waves 0-6) | ~45 |
| Estimated installation time (all waves) | ~105 minutes |

### The Three Revelations

1. **The Unarmed Agents**: Adjudicator and Cartographer are running stock — zero skills, zero extensions, no persona files. This is the single highest-ROI fix in the entire constellation. Wave 0 costs 10 minutes and transforms both agents.

2. **The Security Vacuum**: Zero security skills across the entire constellation. Trail of Bits (Claude Code), OpenAI security trilogy (Codex), Google code-review+security (Gemini), and skill-vetting (OpenClaw) form a complete security perimeter. Wave 1 fills this gap.

3. **The Cross-Agent Blindspot**: No config sync, no token tracking, no multi-agent observability, no notifications. Each agent is a silo. vsync + Splitrail + CC Notify + multi-agent-observability-hooks create the connective tissue. Wave 3+5 addresses this.

### Convergent Path
Execute Waves 0-2 in this session. They arm every agent, establish security, and install core skills. Waves 3-6 are excellent but can be phased across subsequent sessions.

### Confidence
**HIGH** — All items verified via direct repo fetch. Installation commands confirmed. Anti-patterns identified and excluded.

---

## ANTI-PATTERNS REGISTRY (Consolidated)

### HARD REJECT
- `--dangerously-skip-permissions` wrappers (viwo-cli, claudebox)
- Auto-commit plugins (violate constitutional commit discipline)
- Composio connect/connect-apps (vendor lock, OAuth token sharing)
- Warp terminal (conflicts with Ghostty cockpit)
- SuperClaude Framework (conflicts with /claresce loop)
- Moltbook/social network skills (noise, 0 strategic value)
- Crypto/blockchain skills (not our domain)
- Self-evolving skills without governance (violate sovereignty)
- Pickle Rick / Ralph Wiggum persona overrides (conflict with enterprise roles)
- LLxprt/Qwen Code forks (diverge from stock, break compatibility)

### USE WITH CAUTION
- Ralph Wiggum autonomous loops (token budget risk — needs circuit breakers)
- claude-code-auto-memory (could modify curated CLAUDE.md)
- Multiple competing memory skills (our stack is Mem0+Graphiti+qmd — don't fragment)
- Superpowers full-load (many skills — use selective/lazy loading)

### DEFERRED
- Google Workspace MCP (160 tools via Apps Script — needs OAuth setup)
- Qodo Command (evaluation needed — freemium)
- squads-cli (may conflict with Linear/ClickUp architecture)
- Agent-Fusion multi-agent framework (evaluate against native Claude Code teams)

---

*Clarescence produced by Commander (COO) via 4-agent Blitzkrieg swarm. All 12 repos fetched, extracted, cross-referenced, and synthesized. Awaiting Sovereign ratification for installation waves.*
