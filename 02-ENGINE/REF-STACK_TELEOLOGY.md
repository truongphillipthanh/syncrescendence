# STACK TELEOLOGY: Comprehensive Technology Disposition
## Every Tool, Every Surface, Every Platform — Teleologized

**Version**: 0.1.0 (DRAFT — Sovereign ratification required)
**Generated**: 2026-01-31
**Author**: Ajna (Opus 4.5, OpenClaw, M1 Mac mini)
**Purpose**: Line-by-line dispositional analysis of the entire technology stack
**Status**: LIVING DOCUMENT — update as decisions crystallize

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
- [ ] How does OpenClaw use Gemini CLI? (Oracle function)
- [ ] Twin coordination protocol (Opus ↔ GPT5.2)
- [ ] Security assessment (Cisco/Checkmarx reports)
- [ ] Lobster workflow shell — what does it enable?

---

## II. INCUMBENT SaaS — The "Sticky" Tools

Each tool below needs explicit disposition: keep, replace, integrate, or sunset.

### Project Management / Task Management

| Tool | Status | Teleology | OpenClaw Impact |
|------|--------|-----------|-----------------|
| **Linear** | EVALUATING | Engineering-grade PM. Kanban + sprint. API-first. | Could integrate via MCP or API. |
| **Things 3** | ACTIVE (Mac mini) | Personal task capture. Native macOS. Quick. | OpenClaw has `things` CLI skill. Direct integration possible. |
| **Todoist** | DEFERRED | Cross-platform but redundant with Things. | - |
| **Apple Reminders** | ACTIVE | Lightweight, Siri-accessible. Time/location triggers. | OpenClaw has `remindctl` skill. |
| **GoodTask** | EVALUATING | Reminders frontend with more power. | - |
| **NotePlan** | EVALUATING | Markdown-based daily planning. | Overlap with OpenClaw daily notes? |

**Decision needed**: Things vs Linear vs OpenClaw cron for task management. The Palantir endpoint suggests Linear (API-first, queryable). But daily personal tasks → Things/Reminders via OpenClaw.

### Knowledge Management / PKM

| Tool | Status | Teleology | OpenClaw Impact |
|------|--------|-----------|-----------------|
| **Obsidian** | ACTIVE | Graph-based PKM. Wikilinks = the accretion test surface. CANON lives here. | OpenClaw has `obsidian` skill. |
| **Notion** | EVALUATING | Databases + docs. Cowork MCP App candidate. | Could replace some manual tracking. |
| **Logseq** | SUNSET | Overlap with Obsidian. Block-based but less flexible. | - |
| **RemNote** | SUNSET | Spaced repetition + notes. Redundant. | - |
| **DEVONthink** | EVALUATING | Document management + AI classification. macOS-native. | Potential corpus management layer. |
| **Hookmark** | EVALUATING | Deep linking between any macOS objects. | Could be replaced by OpenClaw filesystem operations. |

**Decision needed**: Obsidian is the PKM winner (graph mode = accretion test). But DEVONthink's AI classification might serve the Palantir function. Notion's database model is powerful for the ontology.

### Cloud Storage

| Tool | Status | Teleology | OpenClaw Impact |
|------|--------|-----------|-----------------|
| **Google Drive** | ACTIVE | Gemini Gems live-sync. Account 3 primary. | `make sync-to-drive` pipeline. |
| **Dropbox** | EVALUATING | Legacy storage. Redundant with Drive? | - |
| **Box** | SUNSET | Cowork MCP App, but no other use. | - |
| **iCloud** | ACTIVE | Apple device sync. Account 1 substrate. | System-level, not project-level. |

**Decision needed**: Consolidate to Google Drive + iCloud. Sunset Dropbox/Box unless specific use case emerges.

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
| **Raycast** | ACTIVE | Launcher + extensions. Quick actions. | Raycast AI ↔ OpenClaw overlap. Choose one for AI queries. |
| **Shortcuts** | ACTIVE | Apple ecosystem automation. Siri integration. | OpenClaw can trigger Shortcuts via CLI. |
| **Stream Deck** | ACTIVE | Physical macro buttons. | Map buttons to OpenClaw commands? |
| **BetterTouchTool** | ACTIVE | Trackpad/touch gestures. | Peripheral input → OpenClaw commands. |
| **Make (Integromat)** | DEFERRED | Cloud automation. iPaaS. | OpenClaw + cron may replace this entirely. |
| **IFTTT** | SUNSET | Too simple. Make is superior if needed. | OpenClaw replaces this. |

**Key insight**: OpenClaw's cron + skills architecture may sunset Make/IFTTT entirely. Keyboard Maestro and Hazel remain valuable because they operate at the macOS GUI/filesystem level that OpenClaw doesn't directly touch.

---

## III. DEVELOPMENT TOOLS

| Tool | Status | Teleology | Notes |
|------|--------|-----------|-------|
| **GitHub** | ACTIVE | Connective tissue. Fork/sync architecture. Account 1 owns origin. | `gh` CLI available. |
| **git** | ACTIVE | Version control. Ground truth substrate. | Core infrastructure. |
| **VS Code** | EVALUATING | IDE. But Claude Code CLI may be sufficient. | - |
| **Cursor** | SUNSET | AI IDE. Redundant with Claude Code. | - |
| **Windsurf** | SUNSET | AI IDE. Same. | - |
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

## XI. OPEN DECISIONS — Requires Sovereign Input

1. **Things vs Linear vs OpenClaw cron** — Primary task management surface?
2. **Obsidian vs Notion vs DEVONthink** — Primary PKM beyond the corpus repo?
3. **Dropbox/Box** — Sunset both?
4. **Accounts 4-8** — Still needed?
5. **Make/IFTTT** — OpenClaw replaces?
6. **Atlas+Comet browser strategy** — Still needed with OpenClaw routing?
7. **Cursor/Windsurf** — Confirmed sunset?
8. **Setapp subscription** — Which apps justify continued payment?
9. **Raycast AI vs OpenClaw** — Which handles quick AI queries?
10. **Tailscale** — Enable for remote Mac mini access?

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
