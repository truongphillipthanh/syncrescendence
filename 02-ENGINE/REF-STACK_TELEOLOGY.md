---
id: ref-stack_teleology
kind: reference
scope: engine
target: engine
---

# STACK TELEOLOGY: Comprehensive Technology Disposition
## Every Tool, Every Surface, Every Platform — Teleologized

**Version**: 1.0.0 (SOVEREIGN RATIFIED — 2026-02-10)
**Generated**: 2026-01-31
**Ratified**: 2026-02-10 (SOVEREIGN-009 decisions applied)
**Author**: Ajna (original draft), Commander (ratification edits)
**Purpose**: Line-by-line dispositional analysis of the entire technology stack
**Status**: RATIFIED — decisions crystallized, onboarding in progress

---

## Governing Principles

1. **Every tool must have an explicit teleology** — "why this and not that?"
2. **Selection criteria**: Does it compound meaning? Does it preserve sovereignty? Does it reduce Principal attention cost?
3. **Categories of disposition**: ACTIVE (in use), SELECTED (chosen but not configured), EVALUATING (under investigation), DEFERRED (not now), SUNSET (replacing), ELIMINATED (rejected with rationale)
4. **The Palantir test**: Can this tool eventually feed into the live ontological dashboard?
5. **OpenClaw changes everything**: Persistent local agent = new integration paradigm

---

## I. AI PLATFORMS — The Constellation

### A. Claude (Anthropic)

| Surface | Role | Account | Status | Teleology |
|---------|------|---------|--------|-----------|
| **Claude Web** | INTERPRETER | 3 | ACTIVE | Synthesis, ideation, rapport. Best project isolation, past chat search, extended thinking. The thinking surface. |
| **Claude Desktop** | EXECUTOR-LEAD | 3 (MBA) | ACTIVE | Opus-tier execution with Cowork integration. Bridge between Web and CLI. |
| **Claude Desktop** | PARALLEL-EXEC | 2 (Mac mini) | ACTIVE | Dual Sonnet executors for mechanical parallel tasks. |
| **Claude Code CLI** | EXECUTOR | 1 (origin) | ACTIVE | Filesystem sovereignty. CLAUDE.md hierarchy. The implementation surface. |
| **Claude Chrome Ext** | CAPTURE | 3 | ACTIVE | Tab-level tasks, screenshots, quick transcription. See configuration_layers/chrome/. |
| **Claude Cowork** | BRIDGE | 3 | EVALUATING | MCP Apps (Slack, Asana, Figma, Box, Canva). Potential "work in folder" = Cowork as Claude Code with GUI. Coming: direct CLI integration. |

**Open questions:**
- [ ] Can Cowork use Claude Code AND Web simultaneously? (heading that direction)
- [ ] How do MCP Apps change the "sticky incumbent" problem?
- [ ] What's the Cowork ↔ OpenClaw relationship?

### B. ChatGPT (OpenAI)

| Surface | Role | Account | Status | Teleology |
|---------|------|---------|--------|-----------|
| **ChatGPT Web** | COMPILER | 1 | ACTIVE | Mechanical formatting, Canvas for iterative docs. Project-Only Memory mode prevents leakage. |
| **ChatGPT Desktop** | COMPILER (mobile) | 1 | ACTIVE | Quick dispatch when away from browser. Limited vs Web. |
| **Atlas Browser** | - | 1 | ACTIVE | Dedicated browser for Account 1 ChatGPT access on both Macs. |
| **Codex CLI** | ARCHITECT | 1 | EVALUATING | GitHub-native, spec mode. Needs equivalent deep research per Ajna9 directive. |

**Open questions:**
- [ ] GPT-5.2 memory regression in Projects — still an issue?
- [ ] Codex CLI platform idiosyncrasies vs Claude Code — research needed
- [ ] Does Atlas/Comet browser model survive OpenClaw era?

### C. Gemini (Google)

| Surface | Role | Account | Status | Teleology |
|---------|------|---------|--------|-----------|
| **Gemini Web** | DIGESTOR | 3 | ACTIVE | Clarity production, TTS-optimized summaries. Gems + Drive link = fastest state sync. |
| **Gemini CLI** | ORACLE | 3 | ACTIVE | 1M/2M token context. Corpus sensing, evidence packs. Stateless = reproducible. |
| **Gemini Mobile** | CAPTURE | 3 | ACTIVE | Quick queries, voice input while mobile. |
| **NotebookLM** | VERIFIER-ALT | 3 | EVALUATING | Zero-hallucination grounded synthesis from uploaded sources. Audio overview feature. |

**Open questions:**
- [ ] Gemini CLI idiosyncrasies — research needed per Ajna9 Stream D
- [ ] NotebookLM's role vs Perplexity for verification
- [ ] Does Gemini's Personal Intelligence (beta) change the DIGESTOR role?

### D. Grok (xAI)

| Surface | Role | Account | Status | Teleology |
|---------|------|---------|--------|-----------|
| **Grok Web** | RED TEAM | 1 | ACTIVE | Adversarial challenge, X firehose for social sensing. Prediction markets, EQ, recon. |

**Teleological note**: No persistent config = correct for adversarial role. Fresh perspective every time.

### E. Perplexity

| Surface | Role | Account | Status | Teleology |
|---------|------|---------|--------|-----------|
| **Perplexity Web** | VERIFIER | - | ACTIVE | Citation-backed research, fact-checking. Discrete queries, not extended collaboration. |
| **Perplexity Desktop** | VERIFIER (quick) | - | ACTIVE | Same function, native stability. |

### F. OpenClaw — THE NEW 9TH ROLE

| Surface | Role | Account | Status | Teleology |
|---------|------|---------|--------|-----------|
| **OpenClaw (Mac mini)** | LOCAL ORCHESTRATOR | - | ACTIVE | Ajna Opus 4.5. Persistent memory, filesystem access, webchat + iMessage. Always-on. |
| **OpenClaw (MBA)** | LOCAL ORCHESTRATOR | - | ACTIVE | Ajna GPT5.2. Slack channel. Directive execution. |

**Teleology**: OpenClaw is the missing layer the Constellation always needed — a persistent, local, multi-channel agent with filesystem sovereignty. It doesn't replace the other platforms; it **orchestrates** them. It's the glue.

**Capabilities unique to OpenClaw:**
- Persistent memory across sessions (MEMORY.md, daily notes)
- Cron scheduling (reminders, periodic checks)
- Multi-channel messaging (webchat, Slack, iMessage, Discord, Telegram...)
- Sub-agent spawning (parallel execution)
- Browser automation (Playwright)
- Skills architecture (extensible)
- Canvas (live visual workspace)
- Voice wake + talk mode

**Open questions:**
- [ ] How does OpenClaw use Claude Code? (Can it spawn Claude Code sessions?)
- [ ] How does OpenClaw use Gemini CLI? (SENSOR function — corpus sensing)
- [ ] Twin coordination protocol (Opus ↔ GPT5.2)
- [ ] Security assessment (Cisco/Checkmarx reports)
- [ ] Lobster workflow shell — what does it enable?

---

## II. INCUMBENT SaaS — The "Sticky" Tools

Each tool below needs explicit disposition: keep, replace, integrate, or sunset.

### Project Management / Task Management — RATIFIED

**Sovereign Decision (2026-02-10)**: Multi-methodology stack with native integrations. ClickUp as hub. Goal: eventually replace with internal tools.

#### Tier 1: Core PM (ACTIVE)

| Tool | Status | Methodology | Role | Integrations |
|------|--------|-------------|------|-------------|
| **Linear** | ACTIVE | Agile/Scrum | T1a — engineering-grade PM, API-first | MCP server LIVE, Jira bridge |
| **ClickUp** | ACTIVE | Multi-method hub | T1b — operational PM, native integrations | MCP server LIVE, bridges to all below |
| **Things 3** | ACTIVE | GTD (light) | Personal quick capture, native macOS | OpenClaw `things` skill |
| **Apple Reminders** | ACTIVE | GTD (triggers) | Time/location-based triggers | OpenClaw `remindctl` skill |

#### Tier 2: Methodology Expansion (ONBOARDING)

| Tool | Status | Methodology | Role | Relationship to Hub |
|------|--------|-------------|------|-------------------|
| **Jira** | SELECTED | Scrum | Superstructures Linear, bridges ClickUp | Sprint planning, backlog grooming |
| **Trello** | SELECTED | Kanban | Phases, stages, tiers, strata, levels | Visual flow management |
| **Todoist** | SELECTED | GTD | Substructures ClickUp | Quick capture → ClickUp dispatch |
| **TeamGantt** | SELECTED | Waterfall | Superstructures ClickUp | Timeline/dependency visualization |

#### Tier 3: Evaluation Pipeline (CONSIDER)

| Tool | Status | Methodology | Notes |
|------|--------|-------------|-------|
| **Airtable** | SELECTED | Relational/custom | Spreadsheet-database hybrid. For sure onboarding. |
| **Asana** | EVALUATING | Agile/Waterfall hybrid | Freemium, good integrations |
| **Basecamp** | EVALUATING | Shape Up | Freemium, opinionated |
| **Smartsheet** | CLONE TARGET | Waterfall/Gantt | Clone the primitives, don't subscribe |

#### Methodology Framework (ONBOARDING)

| Methodology | Tool Surface | Status | Notes |
|-------------|-------------|--------|-------|
| **Scrum** | Jira + Linear | SELECTED | Sprint ceremonies, backlog, velocity |
| **Kanban** | Trello + ClickUp views | SELECTED | Flow visualization, WIP limits |
| **GTD** | Todoist → ClickUp | SELECTED | Capture → Process → Organize → Review → Do |
| **Waterfall** | TeamGantt + ClickUp Gantt | SELECTED | Dependency tracking, critical path |
| **Prince2** | Documentation layer | PLANNED | Controlled environments, business case justification |
| **Critical Chain** | Buffer management | PLANNED | Constraint-based scheduling, buffer tracking |
| **Critical Path** | TeamGantt + custom | PLANNED | Longest-path analysis, float calculation |
| **OPM3** | Maturity assessment | PLANNED | Organizational PM maturity model |
| **CMMI** | Process improvement | PLANNED | Capability maturity integration |
| **XP (Extreme Programming)** | Development practices | PLANNED | TDD, pair programming, continuous integration |

**Architecture**: ClickUp sits at the center with maximum native integrations. Jira superstructures Linear (engineering escalation). Todoist substructures ClickUp (quick capture flows up). TeamGantt superstructures ClickUp (timeline views down). Long-term: build internal replacements.

| GoodTask | DEFERRED | Reminders frontend — may not need with Todoist |
| NotePlan | DEFERRED | Overlap with OpenClaw daily notes |

### Knowledge Management / PKM — RATIFIED

**Sovereign Decision (2026-02-10)**: Obsidian = corpus/extended cognition. Notion = personal context manager/LifeOS. These tools may be too complex to clone correctly; if exact PKM function needed, find copycat in interim.

| Tool | Status | Teleology | OpenClaw Impact |
|------|--------|-----------|-----------------|
| **Obsidian** | ACTIVE (PRIMARY) | Corpus ownership. Extended cognition. Graph-based PKM. CANON lives here. Git-tracked. | OpenClaw `obsidian` skill + MCP server. |
| **Notion** | ACTIVE (LifeOS) | Personal context manager. Relational databases. Structured dashboards. IIC views. | MCP server available. Cowork MCP App. |
| **Logseq** | SUNSET | Overlap with Obsidian. | - |
| **RemNote** | SUNSET | Redundant. | - |
| **DEVONthink** | DEFERRED | May revisit if Palantir needs document AI classification. | - |
| **Hookmark** | DEFERRED | OpenClaw filesystem operations may replace. | - |

### Cloud Storage — RATIFIED

**Sovereign Decision (2026-02-10)**: All four services retained with differentiated roles. No sunsetting.

| Tool | Status | Role | Teleology |
|------|--------|------|-----------|
| **Google Drive** | ACTIVE (PRIMARY) | Main storage | Gemini Gems live-sync. Account 3 primary. `make sync-to-drive` pipeline. |
| **Dropbox** | ACTIVE | Client sharing | Share deliverables with external clients/collaborators. |
| **Box** | ACTIVE | Staging | Stage deliverables before distribution. Cowork MCP App. |
| **iCloud** | ACTIVE | Cross-format sync | Apple device sync. Cross-format file access. Account 1 substrate. |

### Communication

| Tool | Status | Teleology | OpenClaw Impact |
|------|--------|-----------|-----------------|
| **Slack** | ACTIVE | Twin's channel. Team collaboration surface. Cowork MCP App. | OpenClaw primary channel for MBA twin. |
| **Discord** | EVALUATING | Community engagement (OpenClaw Discord). | OpenClaw has Discord channel support. |
| **iMessage** | ACTIVE | Personal communication. OpenClaw listening. | OpenClaw `imsg` skill. |
| **Email (Gmail)** | ACTIVE | Account 3 primary. Connectors for Claude/Gemini. | OpenClaw has `gog` (Google) and `himalaya` (IMAP) skills. |

### Design / Creative

| Tool | Status | Teleology | OpenClaw Impact |
|------|--------|-----------|-----------------|
| **Figma** | ACTIVE | UI/UX design. Cowork MCP App. | Integration via MCP. |
| **Canva** | EVALUATING | Quick graphics. Cowork MCP App. | - |
| **Final Cut Pro** | ACTIVE | Video editing. Launch prep (auteur theory). | - |
| **DaVinci Resolve** | EVALUATING | Color grading + editing. Free tier powerful. | - |
| **Midjourney** | DEFERRED | Image generation. Not yet integrated. | - |

### Automation / Orchestration

| Tool | Status | Teleology | OpenClaw Impact |
|------|--------|-----------|-----------------|
| **Keyboard Maestro** | ACTIVE | macOS macro engine. RTS interaction dynamics. | Complements OpenClaw (KM = GUI automation, OC = agent automation). |
| **Hazel** | ACTIVE | File-based rules. Auto-organize downloads/inbox. | Complements OpenClaw (Hazel = filesystem triggers, OC = intelligent routing). |
| **Raycast** | ACTIVE (FREE) | Launcher only (free tier). Clone candidate for internal app. | AI queries → OpenClaw. Raycast = launcher surface only. |
| **Shortcuts** | ACTIVE | Apple ecosystem automation. Siri integration. | OpenClaw can trigger Shortcuts via CLI. |
| **Stream Deck** | ACTIVE | Physical macro buttons. | Map buttons to OpenClaw commands? |
| **BetterTouchTool** | ACTIVE | Trackpad/touch gestures. | Peripheral input → OpenClaw commands. |
| **Make (Integromat)** | SUNSET | OpenClaw + cron replaces all use cases. | - |
| **IFTTT** | SUNSET | OpenClaw replaces this. | - |
| **Setapp** | CANCELLING | Extract primitives, then cancel subscription. Clone useful functionality. | Audit in progress. |

**Key insight**: OpenClaw's cron + skills architecture sunsets Make/IFTTT entirely. Keyboard Maestro and Hazel remain valuable at the macOS GUI/filesystem level. Raycast is a strong clone candidate for internal app development.

---

## III. DEVELOPMENT TOOLS

| Tool | Status | Teleology | Notes |
|------|--------|-----------|-------|
| **GitHub** | ACTIVE | Connective tissue. Fork/sync architecture. Account 1 owns origin. | `gh` CLI available. |
| **git** | ACTIVE | Version control. Ground truth substrate. | Core infrastructure. |
| **VS Code** | ELIMINATED | CLI-first cockpit paradigm makes GUI IDE redundant. Not installed. | - |
| **Cursor** | ACTIVE | Reclassified as **Simulator** (DEC-COCKPIT-005). Async delegation, not primary IDE. | DEC-HQ-002 |
| **Windsurf** | SUNSET | AI IDE. Redundant with Cockpit. | - |
| **iTerm / Ghostty** | ACTIVE | Terminal. Shell is primary interaction surface. | - |
| **Docker** | EVALUATING | Containerization. Not needed yet. | Future: deploy services. |
| **Tailscale** | EVALUATING | Mesh VPN. OpenClaw supports Tailscale mode. | Could enable remote access to Mac mini agent. |

---

## IV. macOS NATIVE — First Party

| Tool | Status | Teleology |
|------|--------|-----------|
| **Finder** | ACTIVE | File navigation. Enhanced by Hazel rules. |
| **Automator** | SUNSET | Replaced by Shortcuts. |
| **Shortcuts** | ACTIVE | Apple ecosystem automation. |
| **AppleScript** | ACTIVE | Deep macOS scripting. OpenClaw uses osascript. |
| **Spotlight / Siri** | ACTIVE | Quick queries. Siri = voice trigger surface. |
| **Notes** | ACTIVE (light) | Quick capture when away from repo. OpenClaw `memo` skill. |
| **Calendar** | ACTIVE | Schedule management. OpenClaw `gog` skill. |
| **Reminders** | ACTIVE | Time/location triggers. OpenClaw `remindctl` skill. |
| **Mail** | DEFERRED | Using Gmail web instead. |
| **Preview** | ACTIVE | Quick PDF/image viewing. |
| **Terminal** | ACTIVE | Shell access. Primary execution surface. |

---

## V. HARDWARE

| Device | Account | Role | Teleology |
|--------|---------|------|-----------|
| **M1 Mac mini** | 2 (primary), 1 (bridge) | Stationary Workhorse | Repo host, always-on, external displays, Ajna Opus (OpenClaw). Parallel execution. |
| **M4 MacBook Air** | 3 (primary), 1 (bridge) | Mobile Primary | Thinking surface. Claude Web, Ajna GPT5.2 (OpenClaw). Follows the thinker. |
| **iPhone 15** | 3 | Primary Mobile | Extension of Account 3 cognitive surface. Capture + review. |
| **iPhone mini** | 1 | Backup Mobile | Stable substrate access. Account 1 emergency dispatch. |

**Convergence question**: As OpenClaw matures, do we need all the browser-per-account gymnastics? OpenClaw can route to any platform from any device. The Atlas+Comet browser strategy may simplify.

---

## VI. BROWSERS — Surface Mapping

| Browser | Account | Device(s) | Teleology | OpenClaw Impact |
|---------|---------|-----------|-----------|-----------------|
| **Chrome** | 3 | MBA, Mac mini | Primary interface. Claude Web, Gemini, Google ecosystem. | OpenClaw's built-in browser. |
| **Atlas+Comet** | 1 | MBA, Mac mini | Account 1 bridge. ChatGPT COMPILER access. | May become redundant if OpenClaw handles routing. |
| **Orion** | 2 | Mac mini | Account 2 parallel execution monitoring. | - |
| **Safari** | - | All | Apple ecosystem integration. Extensions. | - |
| **Brave** | - | - | Privacy-focused. Not actively used. | - |

---

## VII. ACCOUNTS — The Eight Emails

| # | Email | Auth | Role | Status |
|---|-------|------|------|--------|
| 1 | truongphillipthanh@icloud.com | Apple | Sovereign substrate, origin | ACTIVE |
| 2 | icloud.truongphillipthanh@gmail.com | Google | Parallel execution | ACTIVE |
| 3 | truongphillipthanh@gmail.com | Google | Primary interface | ACTIVE |
| 4 | acumen.truongphillipthanh@gmail.com | Google | IIC: Acumen chain | DEFERRED |
| 5 | coherence.truongphillipthanh@gmail.com | Google | IIC: Coherence chain | DEFERRED |
| 6 | efficacy.truongphillipthanh@gmail.com | Google | IIC: Efficacy chain | DEFERRED |
| 7 | mastery.truongphillipthanh@gmail.com | Google | IIC: Mastery chain | DEFERRED |
| 8 | transcendence.truongphillipthanh@gmail.com | Google | IIC: Transcendence chain | DEFERRED |

**Decision needed**: Accounts 4-8 were designed for IIC chain segregation. With OpenClaw + simplified Constellation, do we still need 8 accounts? Or can 3 suffice?

---

## VIII. THE FEEDCRAFT PIPELINE (Todo #1 + #8)

| Source | Volume | Status | Teleology |
|--------|--------|--------|-----------|
| **X Bookmarks** | Unknown | PENDING | Extract: Education/Learning, Strays, Clawdbot categories. |
| **YouTube Watch Later** | 942 videos | PENDING | 80/20 selection for Syncrescendence-relevant content. |
| **x_articles (Desktop)** | 17 articles | PENDING | Dan Koe, focus, learning, strategy, AI articles to read + metabolize. |
| **RSS/Blogs** | Not configured | DEFERRED | OpenClaw has `blogwatcher` skill. Could automate. |

---

## IX. SCRIPTS / SHORTCUTS / AUTOMATIONS (Todo #6)

| Automation | Platform | Status | Teleology |
|------------|----------|--------|-----------|
| **Audize** | Gemini TTS → custom pipeline | NEEDS IMPROVEMENT | Economical TTS. Configuration in Desktop/configuration_layers/gem/. |
| **Chrome Transcription Scripts** | Claude Chrome Ext | ACTIVE | Transcribe: medium articles, websites, X articles, X threads. |
| **Makefile** | CLI | ACTIVE | `make sync-to-drive`, `make state-snapshot`, etc. |
| **Hazel Rules** | macOS | UNKNOWN | Need audit of current rules. |
| **KM Macros** | Keyboard Maestro | UNKNOWN | Need audit. |
| **Stream Deck Profiles** | Elgato | UNKNOWN | Need audit. |

---

## X. DEVELOPMENT BACKLOG (Todo #7)

### Bespoke Apps Desired
These represent gaps in the macOS app ecosystem that Phillip wants filled:

| Need | Existing Approximations | Bespoke Vision |
|------|------------------------|----------------|
| Per-format text editor | TextEdit, PlainPad, Antinote, CotEditor | One app, format-aware (.txt, .md, .yaml, .xml) |
| Daily log + planning | Everlog, Agenda, NotePlan | Unified journal + planner |
| Task management | Things, Todoist, TaskPaper | Sovereignty-native task system |
| Outliner + database | Bike, Notion | Structured thinking tool |
| Quick notes | Drafts, Pronto | Lightweight capture → dispatch |
| Text expansion | - | Pattern-based expansion of repeated phrases |
| LUI (Language UI) | - | vim-like but conversation-driven |
| KM replacement | Keyboard Maestro | Possibly OpenClaw-native? |

**Assessment**: Many of these are now partially addressed by OpenClaw itself (quick capture → dispatch, text expansion via skills, task management via cron + skills). The "LUI" concept is essentially what OpenClaw provides — a language-driven interface to everything.

---

## XI. DECISIONS LOG — Sovereign Ratified (2026-02-10)

| # | Decision | Sovereign Ruling | Status |
|---|----------|-----------------|--------|
| 1 | Task management surface | Multi-methodology: Linear + ClickUp + Jira + Trello + Todoist + TeamGantt | RATIFIED |
| 2 | Primary PKM | Obsidian (corpus) + Notion (LifeOS/PCM) | RATIFIED |
| 3 | Dropbox/Box | KEEP BOTH — Box=staging, Dropbox=client sharing, Drive=main, iCloud=sync | RATIFIED |
| 4 | Accounts 4-8 | Defer activation — 3 accounts suffice for now | RATIFIED (original rec) |
| 5 | Make/IFTTT | SUNSET both — OpenClaw replaces | RATIFIED |
| 6 | Atlas+Comet browser | Keep for now (Account 1 ChatGPT access) | RATIFIED (original rec) |
| 7 | Cursor/Windsurf | SUNSET confirmed | RATIFIED |
| 8 | Setapp | CANCEL — extract primitives and clone | RATIFIED |
| 9 | Raycast AI vs OpenClaw | Raycast FREE tier only (launcher). Clone candidate. OpenClaw for AI. | RATIFIED |
| 10 | Tailscale | Enable for remote Mac mini access | RATIFIED (original rec) |

### Additional Onboarding (2026-02-10)
- **Airtable**: SELECTED — spreadsheet-database hybrid, for sure onboarding
- **Asana, Basecamp**: EVALUATING — freemium, good integrations
- **Smartsheet**: CLONE TARGET — extract primitives, build internal

### Methodology Expansion (2026-02-10)
Prince2, Critical Chain, Critical Path, OPM3, CMMI, XP — all PLANNED for integration into multi-methodology framework.

---

## XII. TOWARD THE PALANTIR ONTOLOGY

The stack teleology is the foundation for the Palantir-like live ontological dashboard. Each tool above should eventually be:
- **Queryable**: "What tools do I use for task management?"
- **Relational**: "How does Things connect to OpenClaw?"
- **Temporal**: "When did I last use Logseq?" (→ sunset signal)
- **Measurable**: "How many tasks completed via Things vs Linear?"
- **Live**: Status indicators for each tool (active/degraded/offline)

**Next steps toward Palantir:**
1. Convert this document into a structured database (CSV → Airtable/Notion/custom)
2. Add relationship mapping (tool A feeds tool B)
3. Add temporal tracking (last used, frequency)
4. Build dashboard view (FIDS-style)

This document is the seed. It will grow.

---

*"The stack is not a list. It's an ecosystem. Every tool either compounds meaning or drains attention. There is no neutral."*
