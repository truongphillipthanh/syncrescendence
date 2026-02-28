# REF — Constellation Integration Architecture
## Every Surface, Every Platform, Every Pipeline — Connected

**Version**: 3.0.0
**Created**: 2026-02-05
**Author**: Commander (Opus) via Cowork
**Clarescence**: CLARESCENCE-2026-02-05-integration-architecture-strata-alignment.md
**Companion to**: REF-STACK_TELEOLOGY.md (dispositional), DYN-DISPATCH_KANBAN_PROTOCOL.md (dispatch), ARCH-SOVEREIGNTY_STRATA.md (canonical framework)
**Status**: DRAFT — Sovereign ratification required

**2026-02-06 update**: Added **Disposition + Routing Charter** decision + reinforced clarescence rationale.
- Decision: `orchestration/state/impl/DEC-20260206-144500-disposition-routing-charter.md` (supersedes prior teleology phrasing)
- Clarescence: `orchestration/state/impl/CLARESCENCE-2026-02-06-disposition-routing-charter.md`
- (Historical) Decision: `orchestration/state/impl/DEC-20260206-113900-saas-integration-teleology.md`
- (Historical) Clarescence: `orchestration/state/impl/CLARESCENCE-2026-02-06-saas-integration-teleology.md`

---

## I. GOVERNING ARCHITECTURE

### Sovereignty Strata as Organizing Principle

This document is organized through the canonical Sovereignty Strata (σ₀–σ₇), defined in ARCH-SOVEREIGNTY_STRATA.md. Every tool, platform, and integration sits at a primary σ-layer. Authority concentrates at center (σ₀) and diffuses outward. Engineering priority flows outside-in per the σ₇-First Principle: if execution doesn't work, nothing upstream matters.

```
σ₀  Sovereign          The human. Constitutional authority. Attention bottleneck.
σ₁  Teleology           Why we act. Intentions, objectives, destinations.
σ₂  Architecture        How we structure. CANON, cosmology, ontological frameworks.
σ₃  Context Engineering  What each instance knows. Memory, handoffs, project files.
σ₄  Ground Truth        Where truth lives. Git repository. Ledgers. State files.
σ₅  Intelligence        Who does the thinking. Platforms, models, capabilities.
σ₆  Access Layer        How we authenticate. Accounts, entitlements, API keys, OAuth.
σ₇  Execution Substrate What actually runs. CLIs, tools, automations, pipelines, IDEs.
```

### How Integration Maps to Strata

Integration connections flow between strata. Every tool has a *primary* σ-layer and touches adjacent layers:

**σ₇ ↔ σ₄**: CLI agents and OpenClaw write directly to the repository. Kanban dispatch protocol governs task flow. Filesystem operations. This is the ground truth boundary — the most privileged integration surface.

**σ₇ ↔ σ₆ ↔ σ₅**: SaaS platforms (Linear, Slack, ClickUp) authenticate through OAuth (σ₆) to expose their intelligence/functionality (σ₅) for use by execution tools (σ₇). Native platform integrations (Linear ↔ GitHub, Slack ↔ Linear) operate at this boundary.

**σ₇ ↔ σ₇**: Automation orchestrators (Make, OpenClaw skills) bridge between execution surfaces that don't natively connect. Make moves data between cloud APIs. OpenClaw moves meaning through intelligent routing.

**σ₁ → σ₇**: Teleological intent flows outward through all layers. Each tool's existence is justified by σ₁ (why it exists) and operationalized at σ₇ (how it executes). REF-STACK_TELEOLOGY.md maps the σ₁ assignments; this document maps the σ₇ connections.

### The Horizon

Beyond currently integrated tools sits the expansion frontier — platforms architecturally anticipated but not yet connected. Content distribution (X, Substack, Medium, YouTube, TikTok, Instagram), creative production (Midjourney, fal, ElevenLabs), asset management, website, e-commerce. These will be absorbed into σ₆–σ₇ as the system accelerates.

### Data Flow

```
σ₄  Repository (Ground Truth)
     ↕ filesystem + kanban dispatch
σ₇  CLI Agents + OpenClaw (Commander, Adjudicator, Cartographer, Ajna, Psyche)
     ↕ gh CLI + native integrations
σ₅  GitHub ↔ Linear ↔ Slack ↔ Discord ↔ Google Drive
     ↕ Make scenarios + OpenClaw skills
σ₅  NotebookLM (Research Library)
     ↕ file-based + human-mediated
σ₃  Notion (PKM / Structured Database)
     ↕ API / MCP
σ₇  Airtable, Content Platforms, Creative Tools
```

Every data flow either moves toward σ₄ (CAPTURE → RETURN) or radiates from it (DISPATCH). Nothing circulates in outer strata without eventually touching ground truth.

### The Swarm Horizon

Each σ₇ platform is developing internal agentic swarm capabilities. Claude Code spawns sub-agents via Task tool. The Codex App (OpenAI) provides a multi-agent command center with parallel threads and scheduled automations. Google Antigravity provides an agent-first IDE with parallel agent management. Gemini CLI's 1M+ context enables corpus-scale sensing in single passes. This means tasks dispatched to each role can be further atomized and parallelized *within* that role's σ₇ surface — the kanban dispatch hands off a directive, the agent's internal swarm handles decomposition.

---

## II. THE FULL CONSTELLATION MAP

### A. AI Platforms — Web Apps (σ₅ primary, σ₃ context)

| Avatar | Epithet | Role | Platform | Acct | σ | Integration | Status |
|--------|---------|------|----------|------|---|-------------|--------|
| **Vizier** | Hermeneut | INTERPRETER | Claude Web | 2 | σ₅ | Projects, GitHub/Drive/Gmail connectors, past chat search | ACTIVE |
| **Vanguard** | Architect | COMPILER | ChatGPT Web | 1 | σ₅ | Canvas, PROJECT-ONLY memory mode, strategic blueprints | ACTIVE |
| **Diviner** | Illuminator | DIGESTOR | Gemini Web | 2 | σ₅ | Gems + Drive live-sync, infinite threads, TTS | ACTIVE |
| **Oracle** | Recon | RECON | Grok | 1 | σ₅ | X firehose, prediction markets, adversarial challenge | ACTIVE |
| **Augur** | Inquisitor | VERIFIER | Perplexity | — | σ₅ | Citation-backed research, discrete queries | ACTIVE |

Web apps participate through the CAPTURE → DISPATCH → RETURN mnemonic. They receive handoff tokens from σ₀, process content through their specialized σ₅ function, and produce artifacts that return to σ₄ via `agents/<agent>/outbox/` or manual commit. Integration is *human-mediated* — the Sovereign orchestrates transitions. Vizier has the richest native σ₆ connections (GitHub, Drive, Gmail connectors).

### B. AI Platforms — Desktop Apps (σ₅ + σ₇)

| App | Contains | Role | σ | Integration | Status |
|-----|----------|------|---|-------------|--------|
| **Claude Desktop** | Chat + Cowork + Code | INTERPRETER + BRIDGE + EXECUTOR | σ₅+σ₇ | Three modes in one shell (see Section VII) | ACTIVE |
| **ChatGPT Desktop** | Chat + Canvas | COMPILER (mobile) | σ₅ | Quick dispatch, limited vs web | ACTIVE |
| **Codex App** (OpenAI) | Multi-agent command center | PARALLEL-EXEC expanded | σ₇ | Parallel threads, worktrees, automations, MCP, skills (see Section VIII) | EVALUATING |
| **Antigravity** (Google) | Agent-first IDE (VS Code fork) | DEVELOPMENT SURFACE | σ₅+σ₇ | Multi-model agents, parallel dispatch, editor + agent manager (see Section IX) | EVALUATING |
| **Gemini Mobile** | Chat | CAPTURE | σ₅ | Quick queries, voice input | ACTIVE |
| **Perplexity Desktop** | Chat | VERIFIER (quick) | σ₅ | Same function as web, native stability | ACTIVE |

### C. AI Platforms — CLI Agents (σ₇ primary, σ₄ ground truth)

| Avatar | Epithet | Role | Platform | Lane | Acct | σ | Dispatch |
|--------|---------|------|----------|------|------|---|----------|
| **Commander** | Viceroy | EXECUTOR-LEAD | Claude Code (Opus) | A | 1 | σ₇ | agents/commander/inbox/ |
| **Adjudicator** | Executor | PARALLEL-EXEC | Codex CLI | B | 2 | σ₇ | agents/adjudicator/inbox/ |
| — | — | PARALLEL-EXEC | Claude Code (Sonnet ×2) | — | 2 | σ₇ | Microscopic tasks |
| **Cartographer** | Exegete | SENSOR | Gemini CLI | C | 2 | σ₇ | agents/cartographer/inbox/ |

CLI agents interact with σ₄ through direct filesystem access and the kanban dispatch system. Each agent watches `00-INBOX0/` in their inbox, claims tasks via atomic `mv`, produces RESULT receipts in `agents/<agent>/outbox/`. See DYN-DISPATCH_KANBAN_PROTOCOL.md for the full lifecycle.

### D. Local Orchestrators — OpenClaw (σ₇ primary, spans σ₃–σ₇)

| Avatar | Model | Device | Channel | σ | Dispatch |
|--------|-------|--------|---------|---|----------|
| **Ajna** | Opus 4.5 | M1 Mac mini | Discord + webchat + iMessage | σ₇ | agents/ajna/inbox/ |
| **Psyche** | GPT-5.2 | M4 MacBook Air | Slack + webchat | σ₇ | agents/psyche/inbox/ |

OpenClaw agents are the Constellation's persistent glue. They combine σ₇ execution (filesystem, git, cron, skills, sub-agent spawning) with σ₃ context engineering (persistent memory, daily notes) and σ₅ intelligence (model reasoning). They don't replace other platforms — they orchestrate them. Hub-spoke preserved: σ₀ → OpenClaw → Lanes → OpenClaw → σ₀.

### E. Research Library — NotebookLM (σ₅ primary, σ₃ context)

| Surface | Role | Acct | σ | Integration | Status |
|---------|------|------|---|-------------|--------|
| **NotebookLM** | RESEARCH LIBRARY | 2 | σ₅ | File-based input (Desktop/NotebookLM-Sources/), grounded synthesis, audio overview | ACTIVE |

NotebookLM is a zero-hallucination grounded synthesis surface at σ₅. Raw research sources live in `~/Desktop/NotebookLM-Sources/` (10 topic notebooks + _config, 290 files). Synthesis products return to `praxis/synthesis/` at σ₄. Integration is file-based; no public API. Human-mediated output keeps σ₀ in the loop for quality control.

### F. Task Management (σ₇ execution, σ₁ teleology)

| Tool | Constellation Role | σ | Integration | Status |
|------|-------------------|---|-------------|--------|
| **Linear** | Task surface ON corpus | σ₇ | GitHub native ↔ Slack native ↔ API | CONFIGURING |
| **ClickUp** | Task surface META to corpus | σ₇ | Slack native ↔ GitHub optional | CONFIGURING |
| **Things 3** | Personal task capture | σ₇ | OpenClaw `things` skill | ACTIVE |
| **Apple Reminders** | Time/location triggers | σ₇ | OpenClaw `remindctl` skill | ACTIVE |

Linear holds SYN-XX issues — every code-touching task. ClickUp holds everything else. Things 3 handles personal quick-capture. The kanban dispatch protocol within the repo is the *internal* task surface at σ₄; Linear and ClickUp are the *external* surfaces at σ₇ that reflect and extend it.

### G. Communication (σ₇ execution, σ₃ context channels)

| Tool | Constellation Role | σ | Integration | Status |
|------|-------------------|---|-------------|--------|
| **Slack** | Psyche's channel + notification hub | σ₇ | OpenClaw native + Linear/ClickUp native | ACTIVE |
| **Discord** | Ajna's channel + community | σ₇ | OpenClaw native + Make bridge | CONFIGURING |
| **iMessage** | Personal + Ajna channel | σ₇ | OpenClaw `imsg` skill | ACTIVE |
| **Email (Gmail)** | Account 2/3 | σ₆ | Vizier connector + OpenClaw `gog`/`himalaya` | ACTIVE |

### H. Cloud Storage & Sync (σ₄ adjacent, σ₆ auth)

| Tool | Constellation Role | σ | Integration | Status |
|------|-------------------|---|-------------|--------|
| **Google Drive** | Gemini sync surface | σ₇ | Gems live-sync + `make sync-to-drive` | ACTIVE |
| **iCloud** | Apple device sync | σ₆ | System-level, not project-level | ACTIVE |
| **Dropbox** | Evaluating — creative pipeline? | σ₇ | — | EVALUATING |
| **Box** | Evaluating — creative pipeline? | σ₇ | Cowork MCP available | EVALUATING |

### I. PKM / Knowledge Management (σ₃ context, σ₅ intelligence)

| Tool | Constellation Role | σ | Integration | Status |
|------|-------------------|---|-------------|--------|
| **Obsidian** | Graph PKM, accretion test | σ₃ | OpenClaw `obsidian` skill | ACTIVE |
| **Notion** | Structured database candidate | σ₃ | Cowork MCP + Make optional | EVALUATING |
| **DEVONthink** | Document AI classification | σ₅ | macOS-native | EVALUATING |

### J. Automation & Orchestration (σ₇ primary)

| Tool | Constellation Role | σ | Integration | Status |
|------|-------------------|---|-------------|--------|
| **Make** | iPaaS orchestrator | σ₇ | Cloud-to-cloud bridges | CONFIGURING |
| **Keyboard Maestro** | macOS macro engine | σ₇ | GUI automation (complements OpenClaw) | ACTIVE |
| **Hazel** | File-based rules | σ₇ | Filesystem triggers (complements OpenClaw) | ACTIVE |
| **Raycast** | Launcher + extensions | σ₇ | Quick actions | ACTIVE |
| **Shortcuts** | Apple ecosystem | σ₇ | Siri + OpenClaw triggering | ACTIVE |
| **Stream Deck** | Physical macro buttons | σ₇ | Mapped to commands | ACTIVE |

### K. Development (σ₄ + σ₇)

| Tool | Constellation Role | σ | Integration | Status |
|------|-------------------|---|-------------|--------|
| **GitHub** | Connective tissue | σ₄+σ₇ | git + `gh` CLI + webhooks | ACTIVE |
| **git** | Version control substrate | σ₄ | Core infrastructure | ACTIVE |
| **Antigravity** | Agent-first IDE | σ₇ | See Section IX | EVALUATING |

### L. Design & Creative (σ₇, onboarding soon)

| Tool | Constellation Role | σ | Integration | Status |
|------|-------------------|---|-------------|--------|
| **Figma** | UI/UX design | σ₇ | Cowork MCP available | EVALUATING |
| **Canva** | Quick graphics, ontology visuals | σ₇ | Cowork MCP available | EVALUATING |
| **Midjourney** | Image generation | σ₅+σ₇ | Discord-based (via Ajna's channel) | DEFERRED |
| **fal** | Fast inference (image/video gen) | σ₅+σ₇ | API | DEFERRED |

### M. Accounts & Substrates (σ₆ primary)

| Tool | Role | σ | Status |
|------|------|---|--------|
| **GSuite** | Account 2/3 infrastructure | σ₆ | ACTIVE |
| **Microsoft** | Account 4 (outlook.com) | σ₆ | EVALUATING |
| **Apple** | Account 1 substrate | σ₆ | ACTIVE |

---

## III. σ₄ + σ₇ — GROUND TRUTH & EXECUTION LAYER (Operational)

### The Dispatch Architecture

All inter-agent coordination at the σ₄↔σ₇ boundary flows through the kanban dispatch system, fully specified in DYN-DISPATCH_KANBAN_PROTOCOL.md.

**Per-agent inbox**: `agents/<agent>/inbox/` with kanban lanes: `00-INBOX0/` (new, unclaimed), `10-IN_PROGRESS/` (claimed, executing), `20-WAITING/` (external dependency), `30-BLOCKED/` (hard blocker), `40-DONE/` (completed), `50_FAILED/` (unsuccessful), `90_ARCHIVE/` (cold storage), `RECEIPTS/` (CC copies, watchers ignore).

**Per-agent outbox**: `agents/<agent>/outbox/` (RESULT receipts), `agents/<agent>/outbox/ARTIFACTS/` (produced files). Sovereign relay surface for web app staging uses per-agent outbox paths.

**Eight dispatch kinds**: TASK (do something), SURVEY (report on something), DIRECTIVE (guidance), EVIDENCE (observation), RESULT (what happened), RECEIPT (CC copy), PATCH (change proposal), NOTE (informational).

**Lifecycle**: PENDING → IN_PROGRESS → DONE/FAILED. Folder location IS the canonical state. Atomic `mv` = claim lock. Every execution produces a deterministic RESULT receipt.

### GitHub ↔ Repository (σ₄ boundary)

Method: git push/pull, `gh` CLI. Commander (origin, Account 1), Adjudicator (fork, Account 2). Commit discipline includes `SYN-XX` Linear references. Branch protection: Adjudicator PRs require Commander review.

### OpenClaw ↔ Repository (σ₇ → σ₄)

Ajna and Psyche orchestrate hub-spoke dispatch: receive σ₀ intent → decompose into TASK files → dispatch to agents/<agent>/inbox/pending/ → collect RESULT receipts from agents/ → synthesize and report. Twin coordination per DYN-TWIN_COORDINATION_PROTOCOL.md./outbox

---

## IV. σ₅ + σ₆ — NATIVE PLATFORM INTEGRATIONS

First-party connections between SaaS platforms. Zero custom code. OAuth (σ₆) enables bi-directional data flow between σ₅ intelligence surfaces.

### A. Linear ↔ GitHub (Priority: P0)

**Teleology**: SYN-XX issues are tasks *on* the corpus. GitHub PRs/commits are execution artifacts. Bi-directional sync ensures the external task surface (σ₇) reflects σ₄ ground truth.

**What it does**: Commits containing `SYN-XX` auto-link. PR status reflects in Linear. Merged PRs auto-transition issue state. Branches from issues carry the key.

**Setup**: Linear → Settings → Integrations → GitHub → Authorize Account 1 → Select `syncrescendence` → Enable auto-link, PR sync, branch creation → Auto-close on merge → Test with SYN-TEST.

### B. Linear → Slack (Priority: P0)

**Teleology**: Psyche at σ₇ (Slack) gains ambient awareness of σ₇ (Linear) state changes without polling σ₄.

**Setup**: Linear → Integrations → Slack → Authorize → Select channel → Configure: SYN-project issues, state changes → Enable Slack→Linear creation → Test.

### C. ClickUp ↔ Slack (Priority: P1)

**Setup**: ClickUp → Integrations → Slack → Authorize → Select spaces → Configure notifications → Enable Slack→ClickUp creation → Test.

### D. ClickUp ↔ GitHub (Priority: P2 — optional)

Only if meta-tasks develop code dependencies. Enable when needed.

### E. Google Drive ↔ Gemini (Operational)

Gems live-sync from Constellation-State/ in Drive. State snapshots via `make sync-to-drive`. Verify `sync-to-drive` reflects post-research-offload structure.

---

## V. σ₇ — ORCHESTRATED BRIDGES (Make + OpenClaw)

### Make vs OpenClaw Boundary

Both serve at σ₇, with a clean division. Make handles cloud-to-cloud bridges (stateless, event-driven, pre-built modules). OpenClaw handles intelligent routing (context-aware, agent-driven). Make moves data; OpenClaw moves meaning.

### Scenario A: GitHub → Discord (Priority: P0)

```
[GitHub: Watch Events] → [Router]
    → PR Merged → [Discord: Webhook] #repo-events
    → Main Push → [Discord: Webhook] #repo-events
    → Release   → [Discord: Webhook] #repo-events
```

### Scenario B: Slack ↔ Discord Cross-Post (Priority: P1)

Two scenarios, one per direction. Keyword filter prevents noise. Both ignore the other bridge's bot to prevent loops.

### Scenario C: Linear + ClickUp → Airtable (Priority: P2 — BLOCKED)

Palantir substrate. Daily aggregation. BLOCKED on Sovereign ratification of Airtable role.

### Scenario D: Google Drive → Notion (Priority: P3 — CONTINGENT)

Research source tracking. Contingent on Notion selection.

---

## VI. OPENCLAW INTEGRATION LAYER (σ₇ orchestration, spans σ₃–σ₇)

OpenClaw operates at a categorically different level. Where Make pipes data between σ₇ surfaces, OpenClaw reads σ₃ context, applies σ₅ intelligence, and orchestrates across σ₇ tools.

### Ajna (Opus 4.5, M1 Mac mini)

Channels: Discord + webchat + iMessage. Skills: `things`, `obsidian`, `remindctl`, `gog`, `himalaya`, `imsg`, `memo`, `blogwatcher`. Cron, Playwright, sub-agent spawning. Dispatches to CLI agents via kanban TASK files.

### Psyche (GPT-5.2, M4 MacBook Air)

Channels: Slack + webchat. Skills: `gog`, filesystem, git. Executes σ₀ directives relayed through Slack.

### The Integration Pattern

Make detects events and transfers data (reliable, cloud-native). OpenClaw interprets events and decides response (what this *means*). Example: GitHub PR merged → Make posts to Discord (σ₇→σ₇) → Ajna reads → Ajna decides whether to dispatch follow-up (σ₅ intelligence applied at σ₇).

---

## VII. THE CLAUDE TRIAD: Chat + Cowork + Code (σ₅ + σ₇ convergence)

Claude Desktop houses three modes, each accessing different σ-layers.

### Chat (σ₅ primary)

INTERPRETER surface. Projects with memory (σ₃), extended thinking (σ₅), GitHub/Drive/Gmail connectors (σ₆). The thinking surface — synthesis, ideation, rapport. Vizier-equivalent on desktop.

### Cowork (σ₅ + σ₆ + σ₇ bridge)

BRIDGE between σ₅ and σ₇. MCP connectors (σ₆) enable direct σ₇ SaaS integration: Slack, Linear, ClickUp, Notion, Box, Make, Figma, Canva. File workspace, sub-agents, bash execution. The key distinction: Cowork can *act on* σ₇ platforms that Chat can only discuss and Code can only reach via CLI. The GUI-accessible orchestration surface.

### Code (σ₇ primary, σ₄ ground truth)

EXECUTOR-LEAD. The Commander. Full filesystem sovereignty (σ₄), CLAUDE.md hierarchy (σ₃), extended thinking (σ₅), git operations, kanban dispatch. Terminal-native. Sub-agent spawning, plan mode. No SaaS connectivity except through CLI tools and file-based dispatch.

### How They Interconnect

Code writes to σ₄. Cowork bridges σ₄ to σ₆/σ₇ SaaS. Chat synthesizes at σ₅. A directive might begin in Chat (synthesis), dispatch to Code (execution), and verify through Cowork (checking Linear/Slack state at σ₇). Claude Desktop becomes a multi-σ workstation.

---

## VIII. THE CODEX APP (OpenAI, Feb 2026) — σ₇ Agent Manager

OpenAI launched the Codex desktop app for macOS on February 2, 2026 — a multi-agent command center at σ₇.

### Capabilities

Parallel agent threads with git worktree isolation. 30-minute autonomous agent runs. Diff review with inline commenting. Skills system (bundled instructions + scripts). Scheduled automations with inbox-queued results. MCP connectivity. Sandboxed security. Voice input. IDE sync for cross-surface context (σ₃). Powered by GPT-5.3-Codex.

### Constellation Mapping

Maps to the **Adjudicator** role's evolution. Codex CLI is single-thread; the Codex App enables the Adjudicator as *swarm coordinator* — decomposing TASKs into parallel threads, running concurrently, producing consolidated RESULT receipts. Git worktree support means each parallel thread operates on an isolated branch — clean integration with the fork/PR workflow. (Note: former "Lane B" terminology is deprecated per Rosetta #18; see Neo-Blitzkrieg full constellation pipeline.)

**Kanban dispatch integration**: TASK dispatched to agents/adjudicator/inbox/pending/ → claimed by Codex App → decomposed into parallel worktree threads → executed → consolidated RESULT to agents/adjudicator/outbox/.

**Open questions**: Does the Codex App monitor the kanban inbox, or does σ₀ manually feed tasks? Can it write RESULT receipts in protocol format? Complement or replace CLI for Adjudicator?

---

## IX. GOOGLE ANTIGRAVITY — σ₅ + σ₇ Agent-First IDE

Google Antigravity is an agent-first IDE built on a heavily modified VS Code fork (via Windsurf lineage), announced November 2025, public preview early 2026. It radically departs from the traditional IDE paradigm by centering *agent management* alongside code editing.

### Architecture

The interface bifurcates into two primary windows: the **Editor** (VS Code-compatible code editing) and the **Agent Manager** (parallel agent dispatch and monitoring). Developers can run five agents simultaneously on different tasks from a single session.

### Multi-Model Intelligence (σ₅)

Antigravity exposes multiple models within a single environment: Google's Gemini 3, Anthropic's Claude Sonnet 4.5, and GPT-OSS. This is a σ₅ convergence event at σ₇ — a single IDE can embody INTERPRETER + COMPILER + DIGESTOR through model switching. No other tool in the stack offers this multi-model flexibility in a unified surface.

### Constellation Mapping

Antigravity is a **development surface**, not an avatar. It replaces the SUNSET Cursor and Windsurf in REF-STACK_TELEOLOGY.md. Its multi-model capability means it can host Constellation roles dynamically: use Gemini 3 for SENSOR work, Claude for EXECUTOR work, GPT-OSS for COMPILER work — all within a single IDE session.

**Key differentiators from Claude Code**: Antigravity is GUI + Agent Manager; Code is terminal-native. Antigravity is multi-model; Code is Claude-only. Antigravity has VS Code extension compatibility; Code has CLAUDE.md hierarchy and kanban dispatch.

**Key differentiators from Codex App**: Antigravity is an IDE (you edit code, agents assist). Codex App is an agent manager (agents edit code, you review diffs). Different paradigms for the same σ₇ layer.

**Open questions**: How does Antigravity's agent output integrate with the kanban dispatch filesystem? Can Antigravity agents write TASK/RESULT files? Does multi-model mode create σ₃ context confusion (different models, different memory)? VS Code extension compatibility — does GitHub Copilot coexist?

---

## X. NOTEBOOKLM AS RESEARCH LIBRARY (σ₅ grounded synthesis)

NotebookLM holds a unique position at σ₅: zero-hallucination grounded synthesis that responds exclusively from uploaded sources.

### Current Architecture

Raw sources → `~/Desktop/NotebookLM-Sources/` (10 notebooks + _config, 290 files). Synthesis products → `praxis/synthesis/` at σ₄. The repo is cognitive core; NotebookLM is research library; Desktop folder is staging interface.

### Integration

File-based input (manual upload or Drive sync). No public API. Human-mediated output (read synthesis, listen to audio overview, capture insights, commit to σ₄). Audio overview produces podcast-style summaries — mobile consumption complement to Diviner's Gemini TTS.

### Future

Google API for NotebookLM would enable: Make scenario auto-uploading new sources, Gemini CLI querying programmatically. Human-mediated pattern is correct for now — keeps σ₀ in loop.

---

## XI. TOOL-BY-TOOL PLAYBOOK

### Linear
σ₇ task surface ON corpus. SYN-XX issues. Integrations: (1) GitHub bi-directional — IV.A. (2) Slack notifications — IV.B. (3) Cowork MCP. (4) Airtable via Make — V.C.

### ClickUp
σ₇ task surface META to corpus. Integrations: (1) Slack — IV.C. (2) GitHub optional — IV.D. (3) Cowork MCP. (4) Airtable via Make — V.C.

### Slack
σ₇ Psyche's home + notification hub. Integrations: (1) Linear incoming — IV.B. (2) ClickUp incoming — IV.C. (3) Discord cross-post via Make — V.B. (4) Cowork MCP.

### Discord
σ₇ Ajna's home + community. Integrations: (1) GitHub via Make — V.A. (2) Slack cross-post via Make — V.B. (3) OpenClaw native channel. (4) Midjourney (Discord-based, when activated).

### GitHub
σ₄+σ₇ connective tissue. Tighten: (1) Linear bi-directional — IV.A. (2) Discord via Make — V.A. (3) Branch protection. (4) GitHub Actions.

### NotebookLM
σ₅ research library. File-based via NotebookLM-Sources/. See Section X.

### Antigravity
σ₅+σ₇ agent-first IDE. Multi-model development surface. See Section IX. Replaces SUNSET Cursor/Windsurf.

### Codex App
σ₇ agent manager. Adjudicator swarm coordinator. See Section VIII.

### Airtable
σ₇ EVALUATING — Palantir substrate. BLOCKED on σ₀ decision.

### Notion
σ₃ EVALUATING — PKM / structured database. BLOCKED on SOVEREIGN-009.

### Figma
σ₇ EVALUATING — UI/UX, ontology visualization. Cowork MCP available.

### Canva
σ₇ EVALUATING — Quick graphics, social content. Cowork MCP available.

### Dropbox
σ₇ EVALUATING. Hold — assess for creative pipeline. Re-evaluate with content production.

### Box
σ₇ EVALUATING. Same — hold position until creative needs clear.

### GSuite
σ₆ Account 2/3 infrastructure. ACTIVE.

### Microsoft
σ₆ EVALUATING. outlook.com. Hold — enterprise world runs on Microsoft. Re-evaluate with outward-facing needs.

### Make
σ₇ iPaaS orchestrator. Activate: Cowork MCP + scenarios A–D per Section V.

---

## XII. FORWARD HORIZON: CONTENT DISTRIBUTION (σ₁ → σ₇)

Per CANON, Syncrescendence is meant to publish across X, Substack, Medium, YouTube, TikTok, and Instagram. This pipeline translates σ₁ teleological intent into σ₇ published content.

### The Pipeline Pattern

Content originates at σ₄ (praxis, canon) → compiled/formatted by σ₅ Constellation (Vanguard compiles, Diviner digests, Vizier interprets) → flows through σ₇ publication staging → publishes to platforms → engagement metrics return to σ₃ for feedback.

| Platform | σ₇ Method | Automation | Content Type |
|----------|-----------|------------|--------------|
| **X** | API + Grok firehose | Make / OpenClaw | Threads, takes, engagement |
| **Substack** | API + RSS | Make / manual | Long-form essays, newsletters |
| **Medium** | API | Make | Articles, cross-posts |
| **YouTube** | API + Studio | Make for metadata | Video essays, tutorials |
| **TikTok** | API | Make scheduling | Short-form video |
| **Instagram** | Meta Business API | Make scheduling | Visual content, reels |

### What This Requires

Content creation (Figma, Canva for graphics; video editing for YouTube/TikTok), asset management (see Section XIII), scheduling automation (Make), analytics ingestion (platform metrics → Palantir dashboard). The content pipeline transforms Syncrescendence from internal system to external presence.

---

## XIII. FORWARD HORIZON: CREATIVE & PRODUCTION (σ₅ + σ₇)

### Generative AI (σ₅ intelligence, σ₇ execution)

| Tool | Function | σ₇ Integration | Timeline |
|------|----------|----------------|----------|
| **Midjourney** | Image generation | Discord (Ajna's channel) | Near-term |
| **fal** | Fast inference | API | Near-term |
| **ElevenLabs** | Voice/TTS | API + Make | Medium-term |

Midjourney via Discord means Ajna can orchestrate image generation as part of the creative pipeline — requesting in-channel and capturing outputs.

### Design (σ₇)

| Tool | Function | σ₇ Integration | Timeline |
|------|----------|----------------|----------|
| **Figma** | UI/UX, ontology visuals, website | Cowork MCP | Near-term |
| **Canva** | Quick graphics, social content | Cowork MCP | Near-term |

Priority: onboard both for ontology visualization (Palantir visual layer) and social content (distribution pipeline).

### Asset Management (σ₇ — tool selection pending)

Function needed: version-controlled creative assets, review/approval workflows, publishing pipeline integration. Candidates: frame.io (video), Shotgun/ShotGrid (production), Dropbox/Box repurposed (storage), bespoke on Airtable/Notion. This is where Dropbox and Box may earn their σ₁ teleology — large file storage and creative collaboration.

### Website & E-Commerce (σ₇ — future)

Domain, hosting, CMS, design (Figma), content pipeline integration, merch storefront. Another σ₇ publication endpoint.

---

## XIV. MCP CONNECTOR ACTIVATION (σ₆ authentication)

Cowork MCP connectors operate at σ₆ — OAuth authentication enabling σ₇ tool access from this interface.

| Connector | Status | Priority | σ₇ Access |
|-----------|--------|----------|-----------|
| **Slack** | ⬜ | P0 | Read/write channels, interact with Psyche |
| **Linear** | ⬜ | P0 | Read/write issues, manage SYN-project |
| **ClickUp** | ⬜ | P1 | Read/write tasks, manage meta-projects |
| **Make** | ⬜ | P1 | Monitor/trigger scenarios |
| **Notion** | ⬜ | P2 | Databases (if selected) |
| **Figma** | ⬜ | P2 | Design files, ontology visuals |
| **Canva** | ⬜ | P2 | Graphics, social content |
| **Box** | ⬜ | P3 | Only if retained |

---

## XV. IMPLEMENTATION SEQUENCE (σ₇-First)

Per the σ₇-First Principle: get execution working, then address higher strata.

### Sprint 1: Core Triangle (Est. 1 hour)
Linear ↔ GitHub ↔ Slack feedback loop. ClickUp → Slack.

### Sprint 2: Discord Bridge (Est. 1 hour)
Discord server, Ajna channel, Make Scenario A (GitHub → Discord).

### Sprint 3: Twin Bridge (Est. 30 min)
Make Scenario B (Slack ↔ Discord). Psyche ↔ Ajna visibility.

### Sprint 4: MCP Connectors (Est. 30 min)
Authorize Slack, Linear, ClickUp, Make in Cowork.

### Sprint 5: Development Surface Evaluation (Est. 2 hours)
Evaluate Antigravity as IDE replacement for Cursor/Windsurf. Test multi-model agent workflow. Evaluate Codex App as Adjudicator expansion. Test kanban dispatch compatibility.

### Sprint 6: Design Onboarding (Est. 1 hour)
Authorize Figma and Canva MCPs. Begin ontology visualization.

### Sprint 7: Palantir Foundation (BLOCKED on σ₀ decisions)
Airtable base, Make aggregation scenarios, dashboard.

### Sprint 8: Content Pipeline Foundation (Future)
X API, Substack setup, Make publishing scenarios.

### Sprint 9: Creative Pipeline Foundation (Future)
Midjourney Discord, fal API, asset management selection, website.

---

## XVI. PENDING SOVEREIGN DECISIONS (σ₀ required)

| Decision | Options | Blocks |
|----------|---------|--------|
| **Antigravity adoption** | Replace Cursor/Windsurf / Evaluate / Defer | Sprint 5 |
| **Codex App role** | Adjudicator expansion / Complement CLI / Defer | Sprint 5 |
| **Airtable teleology** | Palantir substrate / Notion / Bespoke | Sprint 7 |
| **Notion teleology** | PKM / Research tracker / Palantir / Defer | Sprint 7 |
| **Dropbox disposition** | Creative pipeline / Defer evaluation | Sprint 9 |
| **Box disposition** | Creative pipeline / Defer evaluation | Sprint 9 |
| **Microsoft teleology** | Enterprise-facing / M365 / Defer | — |
| **Asset management tool** | frame.io / Shotgun / Dropbox / Bespoke | Sprint 9 |
| **Content distribution timeline** | When to begin X/Substack/YouTube | Sprint 8 |
| **Website stack** | CMS / Static / Platform | Sprint 9+ |
| **Make vs OpenClaw boundary** | Data/meaning split (adopted) / Override | All Make scenarios |

---

## XVII. RELATIONSHIP TO EXISTING DOCUMENTS

| Document | Relationship |
|----------|-------------|
| `ARCH-SOVEREIGNTY_STRATA.md` | **Canonical framework** — σ₀–σ₇ organizing principle for this document |
| `REF-STACK_TELEOLOGY.md` | Companion — maps σ₁ (why); this doc maps σ₇ connections (how) |
| `DYN-DISPATCH_KANBAN_PROTOCOL.md` | Authoritative σ₄↔σ₇ dispatch lifecycle |
| `README.md` | Authoritative σ₅ avatar/role assignments |
| `DYN-TWIN_COORDINATION_PROTOCOL.md` | Ajna/Psyche σ₇ coordination |
| `DYN-RESEARCH_DISPATCH.md` | Research targets for CLI agents |

---

*"The stack is not a list. It's an ecosystem. Every tool either compounds meaning or drains attention. There is no neutral."* — REF-STACK_TELEOLOGY.md

This document maps every surface through the Sovereignty Strata — not just current connections but the trajectory from internal cognitive infrastructure toward external presence. The σ₇ explosion is real: Antigravity, Codex App, Claude Triad, OpenClaw, content platforms, creative tools. The constraint is σ₀ attention. The architecture must channel that explosion through the strata so it compounds rather than fragments.
