# INTENTION ARCHAEOLOGY COMPASS
<!-- Pruned CC28 2026-02-24: 97 → 35 active. 38 DONE, 14 STALE, 10 MERGED archived below. -->
## Council Pedigree Extraction Instrument
Version: 4.0.0
Updated: 2026-02-24
**Last Updated**: 2026-02-24
**Version**: 4.0.0
**Lineage**: Oracle 0–17 (historical) → Council 18+ (current)
**Status**: Rolling snapshot
**Authority**: Council 22 / Commander

> **Terminology**: "Oracle" was sunsetted as a session term (now exclusively Grok's epithet).
> Sessions 18+ are **Councils** — the National Security Council model:
> Sovereign (President) + Commander (National Security Advisor) convene to assess, decide, direct.
> Historical Oracle numbering (0–17) preserved as lineage markers.

---

## PURPOSE

The Intention Archaeology Compass is a unified instrument that extracts, categorizes, and tracks Sovereign intentions across Council sessions. It serves as both:
- **Cache**: Quick reference for active intentions
- **Rolling Snapshot**: Historical record of intention evolution

From Council 12 (Sovereign's words):
> "The intention archaeology compass should be unified. All intentions are compounding vectors that are interdependent... In essence, it's a cache, but it's also a rolling snapshot."

---

## SCHEMA

Each intention entry contains:

```yaml
- id: INT-XXXX
  council: [origin Council number (Oracle 0-17 for historical)]
  timestamp: [ISO datetime or Council reference]
  category: [urgent|sprint|backlog|pattern|capture]
  priority: [P0|P1|P2|P3]
  status: [active|resolved|superseded|deferred]
  text: "[Sovereign's actual words]"
  interpretation: "[Commander's understanding]"
  blocked_by: [null|dependency]
  integrated_into: [null|CANON/task/decision]
  notes: "[additional context]"
```

### Category Definitions

| Category | Description | Action Horizon |
|----------|-------------|----------------|
| **urgent** | Address NOW | Same session |
| **sprint** | Integrate at checkpoint | Current Oracle |
| **backlog** | Future work | Future Oracles |
| **pattern** | Meta-observations | Ongoing |
| **capture** | Undifferentiated inbox | Pending triage |

---

## ACTIVE INTENTIONS

### URGENT (Address NOW — Council 22 Reset)

> **2026-02-23 SOVEREIGN DIRECTIVE**: "We fucked up. Revert. Triage and align."
> INT-2210 (scaffold triage) reverted. 6 commits rolled back. Architecture restored to INT-2209.
> All urgencies realigned to execution critical path: Infrastructure → Memory → Scaffold → Automations.

| ID | Oracle | Text | Status | Notes |
|----|--------|------|--------|-------|
| INT-1202 | 12 | "capitalize on these heavy machinery to construct as much of Syncrescendence" | active | Maximum velocity during capability window |
| INT-1612 | 16 | "Begin ALL automations" | active | Blocked by DC-130 (cockpit activation). Requires agents alive + memory working first. |

### SPRINT (Current Cycle)

| ID | Oracle | Text | Status | Integrated Into |
|----|--------|------|--------|-----------------|
| INT-1203 | 12 | "design/architect for 3 Claude + 1 Gemini + 1 ChatGPT paid" | active | [[CANON-25200-CONSTELLATION_ARCH-lattice]] |
| INT-1206 | 11 | "Complete Efficacy, Mastery, Transcendence IIC configs" | active | PROJ-002 |

### SESSION 15+ (2026-02-09): Autonomy Expansion + Narrative DNA

| ID | Oracle | Text | Status | Integrated Into |
|----|--------|------|--------|-----------------|
| INT-1501 | 15 | "Maximize Claude Code autonomy, close that final 30%" | active | SOVEREIGN-012, SYN-34 |
| INT-1503 | 15 | "Close 30% gap to fiduciary level — Commander must self-improve, embrace or die" | active | SOVEREIGN-TRAJECTORY.md §7 |
| INT-1504 | 15 | "Cascade deployment from Mac mini HQ to MBA field ops" | active | DEPLOYMENT-PLAYBOOK.md Cascade Differential |
| INT-1505 | 15 | "Deep syncretization of sci-fi/gaming/literature narratives" | active | TASK-NARRATIVE-EXEGESIS.md (Cartographer) |
| INT-1506 | 15 | "We are a Neo-organization — individual + AI constellation as institutional equivalent" | active | SOVEREIGN-012 §3 |

### SESSION 16 (2026-02-09): Sovereign Expansion Directive

| ID | Oracle | Text | Status | Integrated Into |
|----|--------|------|--------|-----------------|
| INT-1601 | 16 | "Syncrescript synchronized to corpus, adopt Rails sensibilities" | active | SYN-37 |
| INT-1602 | 16 | "IIC ingestion pipeline on Google ecosystem + feedcraft sources" | active | SYN-49 |
| INT-1603 | 16 | "JIT-software — HighCommand as variable tmux dashboard, Mac mini stable/dashboard, MBA kinetic cockpit" | active | SYN-40 |
| INT-1604 | 16 | "Web app memory architecture audit + Project custom instructions + RAG strategy" | active | SYN-38 |
| INT-1605 | 16 | "NotebookLM research architecture + operational thesis" | active | SYN-39 |
| INT-1606 | 16 | "Discord + Slack — give OpenClaw all tools to self-service" | active | SYN-50 |
| INT-1607 | 16 | "Setapp app audit — clone to terminal-first, reconceptualize interaction dynamic, evaluate Hammerspoon" | active | SYN-47 |
| INT-1608 | 16 | "Extract Apple Notes — ingest/digest/excrete" | active | SYN-46 |
| INT-1609 | 16 | "YouTube Watch Later + X favorites — meta-digests via OpenClaw" | active | SYN-46 |
| INT-1610 | 16 | "Terminal cascade sync — AI CLI tools across iTerm/Ghostty continuum, synchronized between machines" | active | SYN-43 |
| INT-1611 | 16 | "Mac mini + MacBook Air handbooks once settled" | active | SYN-44 |
| INT-1613 | 16 | "Cockpit border white instead of blue" | active | SYN-42 |
| INT-1617 | 16 | "Add Marvel/ComicbookUniverses/Star Wars/Star Trek/Accelerando to narrative imaginal layers" | active | SYN-41, narrative-dna.md |

### SESSION 17 (2026-02-16): Research Corpus Intelligence Extraction

*Source: 267-file research corpus analysis (59 articles deep-read, 4 parallel agents). Insights extracted from RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md and RESEARCH-INSIGHTS-HIGH-SIGNAL.md.*

| ID | Oracle | Text | Status | Integrated Into |
|----|--------|------|--------|-----------------|
| INT-1701 | 17 | "Progressive Disclosure is the correct context loading pattern — 4-layer graduated system for vault traversal" | active | RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md §1.1 |
| INT-1702 | 17 | "Judgment Engineering as Service — exocortex encodes accumulated judgment that agents execute against" | active | → IMPL-Q-0005 (Three-Layer Memory); RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md §3.1 |
| INT-1703 | 17 | "Attention as the Post-Labor Currency — cognitive sovereignty becomes a governance question" | active | → CONVERGENCE-INTENT-TAXONOMY.md domain 7; strategic framing, no direct IMPL (academic); RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md §3.5 |
| INT-1704 | 17 | "Anti-Tool-Shaped-Object Discipline — institutionalize 'what is the number before making it go up?'" | active | → IMPL-Q-0027 (Anti-Tool-Shaped-Object Gate), IMPL-Q-0028 (Tool-Shaped System Audit); RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md §3.6 |
| INT-1705 | 17 | "Instruction → Skill → Hook maturity ladder — new patterns start as instructions, graduate to hooks" | active | RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md §Cross-Cutting #3 |
| INT-1706 | 17 | "Data Layer Sovereignty — ontology, convergence taxonomy, Rosetta Stone ARE proprietary data assets" | active | → REF-ROSETTA_STONE.md v2.7.0 + ontology.db (1484 rows); RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md §INT-004 |
| INT-1707 | 17 | "Three-Layer Memory Architecture — Knowledge Graph + Daily Notes + Tacit Knowledge (consensus converging)" | active | RESEARCH-INSIGHTS-VERY-HIGH-SIGNAL.md §2.1 |
| INT-1708 | 17 | "Research → NotebookLM pipeline automation — classify, partition, upload, question, extract, inject" | active | → IMPL-P-0001 through IMPL-P-0014 (full pipeline); MVP: P-0003→P-0001→P-0002→P-0004→P-0005→P-0007→P-0012→P-0013→P-0009; RESEARCH-PIPELINE-AUTOMATION-SPEC.md |
| INT-1709 | 17 | "Security is existential — 200+ exposed instances, supply chain attacks via skill marketplaces" | active | RESEARCH-INSIGHTS-HIGH-SIGNAL.md §18 |

### BACKLOG (Future Work)

| ID | Oracle | Text | Status | Priority | Notes |
|----|--------|------|--------|----------|-------|
| INT-1614 | 16 | "Student (Chaffey college) + apprentice (IEETC) — FDE modules into Syncrescendence" | active | P1 | Education/professional integration; health+fitness, homeowner property mgmt |
| INT-1615 | 16 | "Health+fitness and homeowner property management modules" | active | P2 | Personal domain integration into Syncrescendence |
| INT-1616 | 16 | "LifeOS/Zettelkasten/PKM/PARA/GTD architectural convergence" | active | P1 | Serious discussion needed: note-taking, linking your thinking, personal context lakehouse, pillars, pipelines, vaults |
| INT-2202 | 20 | "MBA-primary consolidation — single control plane. SSH into Mac mini, control constellation from MBA. The larger goal: one cockpit, not two half-cockpits." | active | P1 | Promoted from deferred. DC-208 source mining (6,850+ atoms in progress) will surface memory/dispatch architecture patterns from research corpus. Current dual-machine paradigm (INT-P015) re-evaluated: MBA is de facto primary, Mac mini is compute/daemon host. Next: let DC-208 research + DC-206 triangulation inform the consolidated cockpit design. Blocked by Phase 2C/2D completion. |
| INT-2204 | 20 | "Platform-native accommodation — work WITH model architectures instead of forcing uphill battles. Gemini 3.1 Pro (weak tools, strong 1M context), Grok Build (proto-CLI, no real harness yet), OpenClaw (root-level arch at ~/.openclaw/). Each agent's dispatch mode should play to its platform's strengths, not impose a uniform interface." | active | P1 | **Promoted from P2.** Three sub-problems: (a) OpenClaw arch harmonization — OpenClaw's SOUL.md/HEARTBEAT.md/USER.md/MEMORY.md at ~/.openclaw/ is a parallel personality layer that must compose with syncrescendence, not compete; (b) weak-tool agents (Gemini CLI, Grok Build) need file-first dispatch patterns, not tool-use assumptions; (c) memory architecture ideology proliferation (Three-Layer, Graphiti, Obsidian vault, ClawVault) — DC-208 research must arbitrate before we commit. |

### SESSION 24 (2026-02-24): Loose End Capture — Constellation Accommodation

*Source: Sovereign scratch pad review. Confirmed existing intentions resolved (INT-2201 agent offices, INT-2203 collab/) and promoted unresolved themes.*

| ID | Oracle | Intention Text | Status | Notes |
|----|--------|---------------|--------|-------|
| INT-2401 | 24 | "OpenClaw architecture harmonization — syncrescendence repo structure must compose with OpenClaw's root-level personality layer (~/.openclaw/SOUL.md, HEARTBEAT.md, USER.md, MEMORY.md). Work WITH the models' native architecture, not against it. The larger goal: any agent, regardless of CLI harness, should be able to orient itself from a single init file that bridges to the constellation." | active | New intention. OpenClaw agents (Psyche, Ajna) currently straddle two identity systems. Harmonization means: (1) agent INIT.md references OpenClaw personality files, (2) memory sync between OpenClaw MEMORY.md and syncrescendence memory/, (3) dispatch patterns respect each platform's native idioms. Blocked by DC-208 research (memory architecture patterns from corpus). |
| INT-2402 | 24 | "CLI agent heterogeneity strategy — the constellation spans 5+ CLI harnesses with radically different capabilities. Claude Code (rich tools, hooks, skills), Codex CLI (strong execution, limited customization), Gemini CLI (huge context, weak tools), OpenClaw/Kimi (generous limits, async), Grok Build (proto-CLI, no harness). Design dispatch and coordination patterns that degrade gracefully across this spectrum." | active | Subsumes INT-2204(b). The file-first dispatch pattern (auto_ingest_loop.sh) already accommodates heterogeneity — formalize this as the canonical pattern. Research from DC-208 corpus (memory architectures, agent coordination patterns) should inform which patterns to adopt vs. build. |

| INT-2403 | 24 | "Ultimate power-user harness for every CLI agent — outfit Claude Code, Codex CLI, OpenClaw with overpowered, bleeding-edge skill arsenals. The larger goal: each agent becomes a maximally capable operator within its platform's idioms. OpenClaw is especially sensitive to model intelligence, so its harness must compensate with superior tooling (skills, memory, context engineering). Skills should be shareable across agents where possible — a skill proven in Claude Code should be portable to Codex/OpenClaw with minimal adaptation." | active | New intention. The harness is the force multiplier that makes mid-tier models punch above their weight. Cross-platform skill sharing is the key leverage — reduces per-agent maintenance, compounds improvements. Depends on INT-2108 (three-track eval framework) for onboard/white-label/verticalize decisions. |
| INT-2405 | 24 | "Vendor-Native Epistemology — teleologize the interaction grammar for every platform in the serendipitous encounters pipeline. YouTube: what criteria to Like, what to Save, how to craft playlists, Watch Later as inbox-zero queue (drain → transcribe → excrete). X/Twitter: what to Favorite, unfavorite-after-transcribe as inbox-zero pattern. NotebookLM: how to create notebooks (topic scoping, source selection, question strategy). Each platform's native affordances (like, save, favorite, playlist, notebook) become epistemic primitives — not arbitrary social gestures but intentional routing signals in the intelligence pipeline. The goal: every platform interaction is a triage decision that feeds the dual-stream architecture (INT-2101). Ultra-synaptical — not Zettelkasten/PARA/GTD cargo-culted, but our own framework honed to how WE think." | active | Recurring unresolved theme. Multiple CANONs touch this (CANON-31115, CANON-31143, feedcraft research) but no operational epistemology has been codified. Keeps surfacing because the pipeline can't be fully automated without decision rules for what enters it. Blocked by INT-2104 (feedcrafting algorithm). Synergy with INT-1616 (LifeOS/PKM convergence). |
| INT-2404 | 24 | "Skills audit + bleeding-edge shopping — use Oracle (Grok) for real-time reconnaissance on the skills/extensions/MCP ecosystem across all CLI platforms. Coalesce and amalgamate overlapping skills, compartmentalize or mereologize (part-whole decompose) them into composable units. Evaluate against three-track framework (INT-2108): ONBOARD (adopt third-party), WHITE-LABEL (adopt + rebrand/customize), VERTICALIZE (build from scratch). The engine/ analysis (DC-202, 147 files already inspected) informs what we already have — skills shopping fills the gaps." | active | New intention. Oracle gives us bleeding-edge visibility into ecosystem evolution. The engine/ directory already contains 147 files of prompts, functions, templates — the skills audit maps new ecosystem offerings against existing capabilities to identify: (1) gaps to fill, (2) redundancies to collapse, (3) novel capabilities to onboard. Synergy with DC-206 (triangulated improvement on surviving content). |

| ID | Oracle | Pattern | Status | Notes |
|----|--------|---------|--------|-------|
| INT-2406 | 24 | "Manus for automation plumbing — evaluate Manus as a paid service to build out automation infrastructure (pipelines, integrations, browser automation, API plumbing) that would otherwise consume constellation cycles. Apply INT-2108 three-track eval: is Manus ONBOARD (pay them to build), WHITE-LABEL (use their output as scaffold we customize), or does it make more sense to VERTICALIZE (build ourselves)? The key question: does Manus's browser automation + multi-step execution capability let us bootstrap the dual-stream pipeline (INT-2101) and NotebookLM automation (INT-2106) faster than building from scratch?" | active | New intention. Manus = potential force multiplier for plumbing that blocks higher-value architectural work. Cost-benefit: Manus subscription vs. constellation cycles spent on Playwright/GCP/pipeline glue. |
| INT-2407 | 24 | "macOS Actuator Suite — procure and configure the durable automation layer that survives the headless/agentic trajectory. Thesis (from macapps.md analysis): keep tools that sit in hard macOS seams (filesystem, dialog augmentation, capture pipelines, selection HUDs, text surgery); treat everything else as provisional. Current owned: Keyboard Maestro, BetterTouchTool. Evaluating: Hazel (filesystem reactor), Default Folder X (open/save seam), CleanShot X (capture pipeline → agentic sensory input), PopClip (selection HUD), BBEdit (text scalpel). Discount strategy: Student App Centre first, then vendor edu pages, then BundleHunt for bench utilities. Architecture principle: prioritize tools exposing stable automation surfaces (CLI, scripting hooks, predictable file outputs), deprioritize tools whose value is intricate GUI." | active | Connects to INT-MI17 (on-device automation) and INT-MI18 (web↔CLI bridge). The actuator suite IS the constellation's limbs — sensors and effectors that persist even when the brain goes conversational. Zsh/Ghostty/tmux/Neovim/Emacs are the terminal layer (already partially deployed). Hazel+KM+BTT are the macOS automation layer. |

| INT-2408 | 24 | "Exocortex integration — synergistically slot incumbent SaaS tools (GitHub, Obsidian, Linear, Todoist, ClickUp, Notion, Slack, Discord, Telegram, etc.) into the constellation architecture. Maximize free-tier leverage. Each tool evaluated not as standalone but as a node in the exocortex: what epistemic primitive does it provide that the constellation can't? How does it compose with our dispatch, memory, and feedcraft layers? Deep research corpus exists (19 files, ~700k words) at ~/Desktop/exocortex/ covering: Obsidian, Linear, ClickUp, Todoist, Notion, Slack, Discord, Telegram, Jira, Confluence, Airtable, Coda, Basecamp, Smartsheet, TickTick, OpenClaw, + PM epistemology meta-analysis. Phase sequencing: scaffold (DONE) → exocortex (THIS) → feedcraft." | active | Major phase transition. The scaffold is built (Phases 0-2C). Exocortex integration is the next strategic layer — how our constellation's internal architecture (agents, memory, dispatch) composes with external SaaS primitives. The deep research files are the raw material; DC-208 source mining pipeline can process them. Connects to INT-1616 (LifeOS/PKM convergence), INT-MI19 (Palantir-like ontology), INT-1606 (Discord+Slack for OpenClaw). |

| INT-2409 | 24 | "CLI ↔ webapp bridge architecture — Grok can simply read GitHub. Web apps (ChatGPT, Gemini, Claude web) see conversations but can't touch the repo. CLI agents (Claude Code, Codex, Gemini CLI) touch the repo but can't see web state. The bridge question: how do we effectively close this gap? Grok reading GitHub is the closest current approximation — it can see repo state from the web side. Connectors (MCP servers, webhooks, API integrations) are the plumbing. The larger goal: any agent, web or CLI, can orient itself from the repo regardless of its interface modality. This is what makes tools become agents become headless." | active | Connects to INT-2402 (CLI heterogeneity), INT-2408 (exocortex integration). The bridge is what makes the constellation truly multi-modal — not just multi-agent. |
| INT-2411 | 24 | "Psyche/Ajna recharacterization — given what we now understand about OpenClaw's architecture and each model's cognitive profile, how best to manifest the TRUE essences of Psyche (CTO, Synaptarch, GPT-5.3-codex) and Ajna (CSO, Strategos, Kimi K2.5)? Psyche's autism-coded systematization should be leveraged for system cohesion, automation policy, pipeline fusion. Ajna's untested philosophical depth needs a scaffolding fortress (rails, training wheels, explicit guardrails) before strategic trust. OpenClaw's personality layer (SOUL.md, HEARTBEAT.md) is the tuning surface. The recharacterization lands when each agent's INIT.md + OpenClaw personality files express a coherent cognitive identity that WORKS, not just sounds good." | active | Depends on INT-2401 (OpenClaw harmonization) and INT-2410 (avatarization thesis). This is where architectural understanding meets operational tuning. |
| INT-2412 | 24 | "Recanonize after research — once DC-208 extraction completes, DC-206 triangulated improvement runs, and exocortex research (INT-2408) is synthesized, conduct a formal recanonization pass. New knowledge from the 1,152-source corpus + 19 exocortex deep researches should update, enrich, or supersede existing CANON files. This is the metabolism cycle: sources → extraction → synthesis → canon update. Not a rename or restructure — a content-level enrichment of verified knowledge." | active | Phase gate: only after Phase 2C+2D complete. Connects to INT-P020 (verbatim trap test — synthesis must produce what sources didn't contain). The recanonization is where extracted atoms become institutional knowledge. |

### PATTERNS (Meta-Observations)

| ID | Oracle | Pattern | Status | Notes |
|----|--------|---------|--------|-------|
| INT-P004 | 7 | "Globe before trees" | active | Holistic framing first |
| INT-P017 | 17 | "File-First, Always — plain markdown outperforms specialized memory infrastructure" | active | ClawVault benchmark: markdown+grep 74.0% vs specialized tools 68.5%. LLMs trained on text files. Own data as files. |
| INT-P028 | 22 | "Architecture without execution is decoration. 14% delivery rate IS the problem." | active | 22 Council sessions produced pristine architecture. Near-zero execution. Memory is the root cause — sessions are amnesiac. |
| INT-P034 | 25 | "Feedback loops > memory engineering — the real bottleneck is quality signals, not storage" | active | Corpus×Intention synthesis finding. |
| INT-P035 | 25 | "Security is Phase 0 of every phase — not Phase 5. 230+ malicious skills Jan-Feb 2026" | active | Corpus×Intention synthesis finding. Security escalation. |

### SESSION 18 (2026-02-16): Token Economics + Antifragile Constellation

**Sovereign Directive**: "Opus 4.6 is second-to-none in interpretability. 5.3-Codex is very meticulous but sub-optimal in rapport. Gemini CLI has large token limits but worst at tool use. Kimi K2.5 has generous but fickle limits. Most intelligent models strategize and plan. Open models conduct housekeeping. Onboard Cline and OpenCode."

| ID | Oracle | Intention Text | Status | Notes |
|----|--------|---------------|--------|-------|
| INT-1801 | 18 | "Token Economics Dispatch — budget-aware routing across shared API plans" | active | ChatGPT Plus fuels BOTH Psyche (5.3-codex) AND Adjudicator (5.2-codex). Shared rate limit pool. Dispatch must account for cumulative consumption. |
| INT-1802 | 18 | "Model Role Specialization — assign by cognitive strength, not availability" | active | Opus 4.6 = interpreter/orchestrator (rapport, interpretability). GPT-5.3-codex = meticulous executor (systematic, thorough). Gemini 2.5 Pro = capacity/fidelity passes (1M context, multi-pass). Kimi K2.5 = strategic auxiliary (generous limits, philosophical depth). |
| INT-1803 | 18 | "Open Model Onboarding — Cline + OpenCode for housekeeping at scale" | active | **Ground truth (2026-02-16)**: Cline v2.2.2 installed (`/opt/homebrew/bin/cline`), TUI-based, supports OpenRouter (free tier = DeepSeek, Qwen, Llama). Needs auth setup via "Use your own API key" → OpenRouter. OpenCode not yet installed (empty `~/.config/opencode/`, no binary in PATH). Both need tmux-dispatchable configuration for Commander orchestration. → IMPL-Q-0031, IMPL-Q-0033, IMPL-Q-0034 |
| INT-1804 | 18 | "Antifragile Agent Infrastructure — self-healing constellation" | active | Five capabilities: (1) auto-ingest loop polls INBOX0, (2) health watchdog monitors panes every 60s, (3) rate limit circuit breaker with failover dispatch, (4) worktree isolation via git worktree or read-only mode, (5) local-first sync via SCP when git push blocked. |

### SESSION 21 (2026-02-22): Dual-Stream Architecture + Account Feed Restructure

*Source: Source Anneal session — audit of CANON-31115 dual-stream documentation + Sovereign account feed directive.*

| ID | Oracle | Intention Text | Status | Notes |
|----|--------|---------------|--------|-------|
| INT-2101 | 21 | "Dual-stream architecture plan — automated intelligence stream (curated regular-cadence sources → 3-tier digest: read/listen/consumption-worthy) + serendipitous encounters stream (feeds into next day's digest). GCP/Gemini multimodal transcription pipeline for Dwarkesh-fidelity." | active | **Authoritative reference**: `canon/CANON-31115-IIC_IMPL-lunar-ACUMEN-planetary-INFORMATION.md` (dual-stream nature is defined here). Operational implementation: ~15%. YouTube serendipitous pipeline partially built (batch_transcribe.py, enrichment). Automated intelligence stream: 0% built. Current DC-208 source mining (1,152 sources, 6,850+ atoms) is operationalizing the serendipitous encounters side only — automated intelligence stream architecture is entirely unbuilt. |
| INT-2102 | 21 | "3-tier consumption model: read (distilled digest/telegram-esque), listen (more in-depth digest + synthesis), consumption-worthy (experience primary source). Replaces CANON-31143's 4-tier model (Immediate/Curated/Archive/Prune)." | active | New taxonomy — NOT in any current document. Must reconcile with CANON-31143 and canonize. |
| INT-2103 | 21 | "Account feed restructure — unify paid accounts. Account 1 (iCloud/Apple): liberal arts, philosophy, history, culture. Account 2 (Google): AI, CS, IT, Cognitive Science — all paid apps here. Account 3: AI design+creation (visual/audio/simulation/multimodality). Overhaul algorithms accordingly." | active | Previously: A1=liberal arts+design, A2=Google infra, A3=AI engineering. Shift: A3 loses AI/CS to A2, gains multimodal creation from A1. A1 loses art/design, focuses philosophy/history/culture. A2 becomes AI+CS hub with all paid subscriptions. |
| INT-2104 | 21 | "Feedcrafting algorithm development for both streams — serendipitous encounters AND automated intelligence. Current work only operationalizes serendipitous encounters (YouTube Watch Later drain)." | active | Blocked by INT-2101 (architecture plan) and INT-2103 (account restructure). |
| INT-2105 | 21 | "Serendipitous encounters feed into the following day's digest — bridge pipeline from evening browsing to morning intelligence brief." | active | Architecturally described in CANON-31115 Part I.C. Zero operational implementation. |

| INT-2106 | 21 | "NotebookLM automation pipeline — Playwright browser automation to create notebooks, upload sources, extract synthesis. No public API (Enterprise alpha only). Drive API for source upload, Playwright for notebook creation. Potent questions → high-signal answers → digest into corpus (integrate or excrete)." | active | Blocked by Account 2 Google setup. Connects to INT-1708 + INT-MI16. Fallbacks: notebooklm-py, notebooklm-mcp-2026. |
| INT-2107 | 21 | "CLI Agent Setup Architecture docs — definitive setup/config guides per platform: Claude Code, OpenClaw, Codex CLI, Gemini CLI. Skills proliferation is the critical vector — systematize before ecosystem sprawl." | active | Claude Code setup existed historically. OpenClaw, Codex, Gemini CLI need equivalent. |
| INT-2108 | 21 | "Three-track evaluation framework: (1) ONBOARD = shelfware/third-party, least favorable; (2) WHITE-LABEL = adopt + syncrescendence branding, medium; (3) VERTICALIZE = build from scratch, most favorable. Apply to all incoming skills, MCP servers, extensions, CLI tools." | active | Decision framework for skills proliferation. Research → evaluate → classify → act. |

### SESSION 22 (2026-02-23): The Revert — Execution Over Architecture

*Source: Sovereign directive after INT-2210 revert. Commander botched scaffold triage (6 commits: renamed dirs, dissolved structures, deleted 3966 lines of architectural docs). Sovereign ordered hard reset to INT-2209. Full triage of unexecuted Council session specs.*

| ID | Oracle | Intention Text | Status | Notes |
|----|--------|---------------|--------|-------|
| INT-2305 | 22 | "Phase gate rule: no phase begins until prior phase P0 items are DONE" | active | New constitutional rule. Prevents INT-2210 pattern (running rename before validate exists, triage before memory works). |

| ID | Oracle | Pattern | Status | Notes |
|----|--------|---------|--------|-------|
| INT-P028 | 22 | "Architecture without execution is decoration. 14% delivery rate IS the problem." | active | 22 Council sessions produced pristine architecture. Near-zero execution. Memory is the root cause — sessions are amnesiac. |

### CAPTURE (Pending Triage)

| ID | Oracle | Raw Capture | Status |
|----|--------|-------------|--------|
| INT-C001 | 12 | "audit and anneal the corpus again for alignment/congruence" | resolved |
| INT-C002 | 12 | "attached reports ought to be canonized" | pending |
| INT-C003 | 13 | "Revenue target reset — new deadline TBD by Sovereign" | pending |
| INT-C004 | 13 | "Corpus hygiene sprint: triage inbox, refresh stale state, compress" | resolved |
| INT-C006 | 14 | "HighCommand (Agendizer) = GUI substrate for INT-MI19 Ontology — document the connection, track as PROJ dependency" | pending |
| INT-C007 | 14 | "Session discipline: chunk work into parallel sessions, stop sequential single-terminal habits" | pending |
| INT-C011 | 18 | "Cline + OpenCode installed — integrate for Commander manipulation via tmux, use most intelligent free models (OpenRouter free tier). Backlog now, operationalize as constellation stabilizes." | pending |
| INT-C012 | 19 | "Grok Build (xAI's CLI coding agent, analogue to Claude Code) — not yet released publicly (npm package absent, waitlist only at grokai.build as of 2026-02-19). When released: avatarize into constellation as 6th agent." | pending |

### PRE-ORACLE INTENTIONS (Extracted from `my inputs.md`, 2026-02-01)

*Source: Sovereign raw inputs to ChatGPT Vizier sessions, pre-dating formal Oracle numbering. 50 entries compressed into 20 intention vectors.*

**Resolved by Restructuring (Oracle 13 work):**

| ID | Text (compressed) | Status | Resolved By |
|----|-------------------|--------|-------------|
| INT-MI01 | "Don't nerf ChatGPT/Grok/Gemini—general intelligence has value beyond narrow roles" | resolved | Avatar Pantheon v3 (README.md) — roles expanded, not lobotomized |
| INT-MI02 | "Capitalize on ALL memory features across ALL platforms" | resolved | CANON-25000 (Memory Architecture + Teleology) — comprehensive coverage |
| INT-MI03 | "Algebraize/symbolize the corpus—reduce tokens, maximize semantics" | resolved | PROJ-SN-VARS — SN system (79% compression) + DEF variables |
| INT-MI04 | "Code-ify the corpus so things update everywhere—variables, not literals" | resolved | sn_expand.py + 9 DEF blocks in DEF-CONSTELLATION_VARIABLES.md |
| INT-MI05 | "Obsidian-friendly wikilinks and graph backlinks" | resolved | Cross-references maintained throughout restructuring ([[CANON-XXXXX]] format) |
| INT-MI06 | "Rename directories—developer happiness, not legacy numbering" | resolved | PROJ-RESTRUCTURE — 00/01/02/04/05 + agents/-SOVEREIGN |
| INT-MI07 | "GEMINI.MD and AGENTS.MD in root for CLI agents" | resolved | AGENTS.md created, gemini-settings.json in engine |
| INT-MI08 | "02-OPERATIONAL is a shitshow—why does it look like that?" | resolved | PROJ-RESTRUCTURE — orchestration/state/scripts/archive/ |
| INT-MI09 | "Consolidate directives and execution logs holistically" | resolved | archive/ with compendiums, compact_wisdom.sh automation |
| INT-MI10 | "Forensic audit of Canon—conceptual coherence, not metadata" | resolved | CANON lean-out (82→79), cross-reference sweep, CANON-00007+00008 merge |
| INT-MI11 | "Live capability and features matrix—not ossified in stone" | resolved | MODEL-INDEX.md + ARCH-LIVE_CANON_TICKER.md design |
| INT-MI12 | "05 is short-term memory; 06 is cautionary tales/aphorisms" | resolved | praxis merger — MEMORY-*, EXEMPLA-*, synthesis/mechanics/practice/ |
| INT-MI13 | "03→06 are interim containers" | resolved | 03 absorbed into engine, 05+06+07 merged into praxis |
| INT-MI14 | "Semantic annealment—collapse bloated logs, condense with acumen" | resolved | PROJ-RESTRUCTURE (1267→636 files), compact_wisdom.sh |

**Active (Not Yet Resolved):**

| ID | Text (compressed) | Status | Priority | Blocked By |
|----|-------------------|--------|----------|------------|
| INT-MI15 | "Offload transcripts to Google ecosystem—sources externalized into Drive" | active | P2 | Google AI Pro setup (Account 2) |
| INT-MI16 | "Build pipeline in Google ecosystem—Drive sync, Personal Intelligence, Gmail integration" | active | P2 | PROJ-014 (Multi-Account Sync) |
| INT-MI17 | "On-device automation—Hazel, Keyboard Maestro, BTT, AppleScript, Shortcuts" | active | P3 | — |
| INT-MI18 | "Web↔CLI bridge via Hazel + macros—automate between web and CLI" | active | P3 | INT-MI17 |
| INT-MI19 | "Palantir-like ontology—the FINAL BOSS" | active | P1 | PROJ-006, PROJ-003. **UPDATE 2026-02-07**: HighCommand (Agendizer) now implements OntologyClass enum, force-directed graph, convergence detection, echo patterns, bidirectional edges. Reflect primitives (daily notes, backlinks, entity types) are the GUI interaction grammar for this ontology. HighCommand = the native substrate. |
| INT-MI20 | "Category/type theory applied to corpus taxonomization down to token level" | active | P2 | SN system provides foundation; deeper application pending |

*Patterns INT-P009 through INT-P013 archived as institutionalized in CC28 pruning.*

---

## HISTORICAL EXTRACTIONS

### Oracle 0: Vision

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0001 | "civilizational sensing infrastructure" | resolved | Core framing established |
| INT-0002 | "skate to where the puck is going" | active | Ongoing design principle |
| INT-0003 | "leverage The Bitter Lesson" | active | Lens 2 institutionalized |

### Oracle 1: Research

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0101 | "consumer/prosumer focus" | resolved | Ecosystem cartography scope |
| INT-0102 | "multi-platform strategy" | active | 5-platform constellation |

### Oracle 2: Infrastructure

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0201 | "flat + symlink architecture" | resolved | Decision 2.1 |
| INT-0202 | "designing the librarian, not compressing the library" | active | Context engineering thesis |
| INT-0203 | "human navigation: comprehensible in 5 minutes" | active | Design constraint |

### Oracle 3: Orchestration Peak

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0301 | "orchestration infrastructure pattern" | resolved | THE MODEL established |
| INT-0302 | "Reception Calibration vs Archetype Engineering (DEPRECATED, Rosetta #79)" | resolved | Three-layer architecture; Reception Calibration won |
| INT-0303 | "visibility bridge via execution logs" | active | Visibility flow |

### Oracle 4: Metabolic Defrag

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0401 | "canonize or delete, no middle ground" | superseded | Too aggressive |
| INT-0402 | "79% file reduction" | resolved | Defrag completed |
| INT-0403 | "nine evaluative lenses" | resolved | Extended to 18 in Oracle 6 |

### Oracle 5: Recovery + Genesis

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0501 | "orchestration is protected infrastructure" | resolved | Constitutional rule |
| INT-0502 | "Genesis layer creation" | resolved | CANON-0000x series |
| INT-0503 | "most extreme dynamic progressive route" | active | Decision principle |

### Oracle 6: Semantic Annealment

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0601 | "extended nine lenses to 18" | resolved | STANDARDS.md |
| INT-0602 | "bifurcation: filesystem vs Obsidian" | resolved | Decision 6.2 |
| INT-0603 | "aliases for Finder, not Obsidian" | active | Design principle |

### Oracle 7: Ground Truth

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0701 | "REVIEW EVERY CONVERSATION" | resolved | Forensic audit completed |
| INT-0702 | "maximum resolution documentation" | active | ORACLE_DECISIONS.md created |
| INT-0703 | "repository is Foyer" | active | All context accessible |

### Oracle 8-9: [Recovery Phase]

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0801 | "complete PROJ-001 transcript ingestion" | resolved | 43 sources processed |
| INT-0901 | "directory restructuring to 00-06" | resolved | Numbered scheme deployed |

### Oracle 10: Infrastructure Completion

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-1001 | "PROJ-011 automation infrastructure" | resolved | CLAUDE.md + Makefile + commands |
| INT-1002 | "multi-Claude coordination" | resolved | coordination.yaml |
| INT-1003 | "worktree-based isolation" | active | Zone ownership pattern |

### Oracle 11: Blitzkrieg

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-1101 | "parallel stream execution" | resolved | 4 streams completed |
| INT-1102 | "IIC configuration reconnaissance" | resolved | 14500+ lines reviewed |
| INT-1103 | "Gemini CLI validation" | resolved | APPROVED |

### Oracle 12: Constellation Architecture

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-1201 | "self-sustaining by month end" | active | Revenue target |
| INT-1202 | "5-platform constellation" | active | [[CANON-25200-CONSTELLATION_ARCH-lattice]] |
| INT-1203 | "ChatGPT Plus integration" | active | coordination.yaml update |
| INT-1204 | "Oracle Pedigree protocol" | resolved | [[CANON-25100-CONTEXT_TRANS-lattice]] update |
| INT-1205 | "unified intention compass" | resolved | This document |

---

## Archived Intentions (CC28 Pruning — 2026-02-24)

### DONE (38 items)

| INT-ID | Title | Status | Evidence |
|--------|-------|--------|----------|
| INT-2301 | Fix Docker on Mac mini | ✅ DONE | DC-100 DONE. Neo4j 5.26.0 + Graphiti 0.22.0 healthy. |
| INT-2302 | Agent fleet audit | ✅ DONE | DC-101 DONE. Fleet audited, SSH bridge verified. |
| INT-2303 | Memory Phase 1 — memsync + JSONL | ✅ DONE | DC-110–113 all DONE. E2E write path verified. |
| INT-2304 | Antifragile scaffold scripts | ✅ DONE | DC-120+121 DONE. scaffold_validate.sh + scaffold_heal.sh installed. |
| INT-1204 | Update CANON-25100 with Oracle Pedigree | ✅ DONE | CANON-25100 v2.1.0. |
| INT-1205 | Unified intention compass | ✅ DONE | This document IS the deliverable. |
| INT-1101 | Multi-CLI integration validation | ✅ DONE | DIRECTIVE-042B. |
| INT-1210 | Canonize Model Manual/Prompting | ✅ DONE | DIRECTIVE-044B audit. |
| INT-1211 | Canonize Platform Features | ✅ DONE | 77 CANON files. |
| INT-1212 | Canonize Model Qualities | ✅ DONE | 73 CANON files. |
| INT-1213 | Blitzkrieg model specification | ✅ DONE | CLAUDE.md v2.1.0. |
| INT-1502 | Inscribe narrative DNA | ✅ DONE | memory/narrative-dna.md. |
| INT-1507 | Appropriate martial/legal terminology | ✅ DONE | REF-ROSETTA_STONE.md v2.3.0. |
| INT-1508 | Track Yegge Gas Town + Anthropic Hivemind | ✅ DONE | memory/narrative-dna.md. |
| INT-1509 | launchd over cron | ✅ DONE | DEC-SOV-006, plists deployed. |
| INT-2201 | Complete repo rearchitecture | ✅ DONE | Agent offices deployed, collab/ created. |
| INT-2203 | Collaboration directory design | ✅ DONE | collab/ with anti-proliferation policy. |
| INT-1209 | Temporal intelligence refresh | ✅ DONE | DC-134 DONE (ledger_refresh.sh). Broader vision tracked as DCs. |
| INT-0001 | Civilizational sensing infrastructure | ✅ DONE | Core framing established. |
| INT-0101 | Consumer/prosumer focus | ✅ DONE | Ecosystem cartography scoped. |
| INT-0201 | Flat + symlink architecture | ✅ DONE | Decision 2.1. |
| INT-0301 | Orchestration infrastructure pattern | ✅ DONE | THE MODEL established. |
| INT-0302 | Reception Calibration vs Archetype Engineering | ✅ DONE | Three-layer architecture decided. |
| INT-0401 | Canonize or delete | ✅ DONE | Superseded — nuanced approach adopted. |
| INT-0402 | 79% file reduction | ✅ DONE | Defrag completed. |
| INT-0403 | Nine evaluative lenses | ✅ DONE | Extended to 18. |
| INT-0501 | Orchestration is protected infrastructure | ✅ DONE | Constitutional rule. |
| INT-0502 | Genesis layer creation | ✅ DONE | CANON-0000x series. |
| INT-0601 | Extended nine lenses to 18 | ✅ DONE | STANDARDS.md. |
| INT-0602 | Bifurcation: filesystem vs Obsidian | ✅ DONE | Decision 6.2. |
| INT-0701 | Review every conversation | ✅ DONE | Forensic audit completed. |
| INT-0801 | Complete PROJ-001 transcript ingestion | ✅ DONE | 43 sources processed. |
| INT-0901 | Directory restructuring to 00-06 | ✅ DONE | Numbered scheme deployed. |
| INT-1001 | PROJ-011 automation infrastructure | ✅ DONE | CLAUDE.md + Makefile. |
| INT-1002 | Multi-Claude coordination | ✅ DONE | coordination.yaml. |
| INT-1101 (O11) | Parallel stream execution | ✅ DONE | 4 streams completed. |
| INT-1102 (O11) | IIC configuration reconnaissance | ✅ DONE | 14,500+ lines reviewed. |
| INT-1103 | Gemini CLI validation | ✅ DONE | APPROVED. |

### STALE (14 items)

| INT-ID | Title | Status | Evidence |
|--------|-------|--------|----------|
| INT-1201 | Accounts self-sustaining by month end | ⏸️ STALE | Jan 31 deadline missed. No reset target. |
| INT-1207 | Manus before Perplexity | ⏸️ STALE | P3 deferred since Oracle 12. No activity. |
| INT-1208 | Promos for Perplexity + Gemini account | ⏸️ STALE | P3 deferred since Oracle 12. |
| INT-0802 | Modal 2 visual capabilities | ⏸️ STALE | P3 deferred. PROJ-009. No activity since Oracle 8. |
| INT-1102 (skills) | Skills conversion for top 5 functions | ⏸️ STALE | Superseded by INT-2404 skills audit. |
| INT-0701 (backlog) | Browser automation for account cloning | ⏸️ STALE | P3 deferred since Oracle 7. |
| INT-1214 | Deep Research: Claude Code + Anthropic | ⏸️ STALE | Prompt prepared but never executed. |
| INT-1215 | Deep Research: OpenAI Codex | ⏸️ STALE | Never started. |
| INT-1216 | Deep Research: Google Jules + Gemini CLI | ⏸️ STALE | Never started. |
| INT-1217 | Plan Mode as Oracle replacement | ⏸️ STALE | Obsolete — triangulation playbook supersedes. |
| INT-1218 | Permission fatigue mitigation | ⏸️ STALE | skipDangerousModePermissionPrompt already set. |
| INT-1618 | Celestial alignment synchronization | ⏸️ STALE | Poetic/cathartic. No operational dependency. |
| INT-0801 (backlog) | Tech Lunar 306K specs to CANON | ⏸️ STALE | P2 deferred since Oracle 8. |
| INT-1901 | Avatarize Grok Build | ⏸️ STALE | Blocked by Grok Build not publicly released. |

### MERGED (10 items)

| INT-ID | Title | Status | Evidence |
|--------|-------|--------|----------|
| INT-2306 | Rename praxis sigma container | 🔀 MERGED into DC-122 | Same scope. |
| INT-2307 | Numbered→semantic dir rename is Phase 4 | 🔀 MERGED into DC-146 | Sanctify numbered layers per DC-204T. |
| INT-1710 | Constellation pattern validated | 🔀 MERGED into INT-P022 | Same pattern observation. |
| INT-1711 | Agent Vault = Human-Agent Shared Knowledge Graph | 🔀 MERGED into INT-1707 | INT-1707 is broader. |
| INT-1712 | Security perimeter is capability not network | 🔀 MERGED into INT-1709 + INT-P019 | Combined scope. |
| INT-2410 | Constellation avatarization thesis | 🔀 MERGED into INT-2411 | Theory merged with execution. |
| INT-C009 | Celestial alignment (capture) | 🔀 MERGED into INT-1618 | Duplicate. |
| INT-C008 | Notion/Airtable LifeOS discussion | 🔀 MERGED into INT-1616 + INT-2408 | Subsumed. |
| INT-C010 | Notion/Airtable/PKM (capture) | 🔀 MERGED into INT-1616 + INT-2408 | Duplicate of C008. |
| INT-C005 | Learn tmux | 🔀 MERGED | tmux operational. |

### Archived Patterns (institutionalized — no longer tracked individually)

| INT-ID | Pattern | Status |
|--------|---------|--------|
| INT-P001 | Orchestration is OPERATIONAL, not CANON | Institutionalized in CLAUDE.md |
| INT-P002 | Metabolism applies to CONTENT, not infrastructure | Institutionalized in CLAUDE.md |
| INT-P003 | Verify before declare | Institutionalized in CLAUDE.md |
| INT-P005 | Automation infrastructure must precede content work | PROJ-011 complete |
| INT-P006 | Multi-agent 90.2% outperforms single-agent | Constellation justification — embedded |
| INT-P007 | Pedigree supersedes handoff | Embedded in CC lineage protocol |
| INT-P008 | Temporal vs evergreen distinction | CANON = evergreen only — embedded |
| INT-P009 | ChatGPT proposes creative postulations Claude wouldn't | Embedded in model behavioral profiles |
| INT-P010 | Claude amenable but lacks mind-expansion | Embedded in model behavioral profiles |
| INT-P011 | Everything is just trade-offs | Institutionalized |
| INT-P012 | ChatGPT SD → Codex DD → Claude CD pipeline | Architecture metaphor — embedded |
| INT-P013 | Chorus/collaboration, not unidirectional | Embedded in triangulation playbook |
| INT-P014 | Tokens are the new minerals and vespene gas | Embedded in token economics dispatch |
| INT-P015 | Mac mini = stable dashboard, MBA = kinetic cockpit | Embedded in dual-machine paradigm |
| INT-P016 | Web app system prompts general | Thesis validated — embedded |
| INT-P018 | Supersede, Never Delete | Institutionalized |
| INT-P019 | Security as Binding Constraint | Subsumed by INT-P035 |
| INT-P020 | The Verbatim Trap Test | Institutionalized |
| INT-P021 | Knowledge-Code Isomorphism | Institutionalized |
| INT-P022 | Constellation pattern is emergent consensus | Embedded |
| INT-P023 | Shared Rate Limit Awareness | Embedded in dispatch protocol |
| INT-P024 | Intelligence Tiering | Embedded in model registry |
| INT-P025 | Agent Auto-Recovery | Embedded in auto-ingest system |
| INT-P026 | Google moving towards world models | Embedded in account thesis |
| INT-P027 | New paradigms ship by the hour | Embedded in evaluation framework |
| INT-P029 | Never triage without validation infrastructure | Embedded in phase gate rule |
| INT-P030 | Phase gates are constitutional | = INT-2305, redundant |
| INT-P031 | Triangulated specs are execution-ready | Institutionalized |
| INT-P032 | Work with the grain, not against it | = INT-2204, redundant |
| INT-P033 | Research before architecture | = phase gate rule, redundant |
| INT-P036 | Feedcrafting = computational RAS | Embedded in INT-2104 |
| INT-P037 | Syncrescendence IS the exocortex | Embedded in INT-2408 |

---

## INTEGRATION PROTOCOL

### 1. Extraction (During Oracle Session)

When Sovereign speaks:
1. Capture exact words in quotes
2. Assign temporary INT-XXXX ID
3. Note Oracle number
4. Add to CAPTURE category if unclear

### 2. Categorization (Session Checkpoint)

Move from CAPTURE to appropriate category:
- **urgent**: Requires immediate action
- **sprint**: Part of current cycle
- **backlog**: Future work
- **pattern**: Meta-observation

### 3. Resolution Tracking

When intention is addressed:
1. Update status to `resolved`
2. Add `integrated_into` reference
3. Document outcome

### 4. Supersession

When intention is replaced:
1. Update status to `superseded`
2. Reference replacing intention
3. Document rationale

---

## DEPENDENCY MAP

### Critical Path (Council 22 — EXECUTION ORDER)

```
PHASE 0: INFRASTRUCTURE ALIVE
INT-2301 (Docker/Graphiti) ──────────────► DC-100, DC-102
     │
     └── INT-2302 (agent fleet audit) ───► DC-101
              │
              ▼
PHASE 1: MEMORY (gates ALL subsequent work)
INT-2303 (memsync + JSONL) ──────────────► DC-110→111→112→113
     │
     ▼
PHASE 2: ANTIFRAGILE SCAFFOLD
INT-2304 (validate + heal) ──────────────► DC-120→121
     │
     ├── INT-2306 (sigma→praxis rename) ─► DC-122 (sigma ONLY)
     │
     └── INT-2307 (numbered→semantic) ───► DC-146 (Phase 4 — NOT before)
              │
              ▼
PHASE 3: AUTOMATIONS + SENSING
INT-1612 (begin automations) ────────────► DC-130 (cockpit)
     │
     ├── INT-1209 (temporal sensing) ────► DC-134 (Live Ledger Phases 2-4)
     │
     └── INT-2303.2 (memory Phase 2) ───► DC-131→132→133 (/triples, backfill, query tools)
              │
              ▼
PHASE 4: HARDENING + SCALE
DC-140 (security audit) ────────────────► MUST precede any external shipping
DC-142 (memory compaction) ─────────────► Weekly agent memory management
DC-144 (Sixth Agent) ──────────────────► Diviner's topological observer
DC-146 (full directory rename) ─────────► ONLY after all above phases pass
```

### Legacy Dependency Map (Preserved)

```
INT-1201 (sustainability) ──────────────────► Revenue generation
     │
     ├── INT-1202 (heavy machinery) ──────► Maximum velocity
     │        │
     │        └── INT-1203 (5 platforms) ─► [[CANON-25200-CONSTELLATION_ARCH-lattice]]
     │
     └── INT-1206 (IIC configs) ──────────► PROJ-002 completion
              │
              └── INT-1101 (multi-CLI) ───► Gemini validated

INT-1612 (begin automations) ────────────► Everything below
     │
     ├── INT-1603 (JIT HighCommand) ─────► Mac mini dashboard + MBA cockpit
     ├── INT-1608 (Apple Notes) ──────────► Information extraction
     ├── INT-1602 (IIC Google) ───────────► Ingestion pipeline
     └── INT-1604 (web app memory) ───────► Platform leverage audit

INT-P014 (tokens = minerals) ────────────► Resource economics lens
INT-P015 (dual-machine paradigm) ─────────► INT-1603, INT-1611
```

---

## PATTERN ANALYSIS

### Recurring Themes

1. **Velocity**: "capitalize", "heavy machinery", "accelerating pace", "begin all automations"
2. **Architecture**: "constellation", "5-platform", "specialization", "JIT-software"
3. **Sustainability**: "self-sustaining", "month end"
4. **Holism**: "unified", "integrated", "globe before trees", "LifeOS convergence"
5. **Trade-off Pragmatism**: "everything is trade-offs", "don't disqualify for spottiness"
6. **Compression**: "algebraize", "symbolize", "reduce tokens maximize semantics", "Rails conventions"
7. **Automation**: "Hazel", "macros", "bridge web and CLI", "sensing", "begin ALL automations"
8. **Resource Economics**: "tokens are the new minerals and vespene gas", API credits as strategic resource
9. **Dual-Machine Paradigm**: Mac mini = stable dashboard (macro), MBA = kinetic cockpit (micro)
10. **Information Stream Extraction**: Apple Notes, YouTube, X favorites — ingest/digest/excrete cycle
11. **Narrative Depth**: Marvel, Star Wars, Star Trek, Accelerando join StarCraft/Dune/Halo/anime/gaming

### Anti-Patterns Identified

1. **Oracle 4 Category Error**: Applied metabolism to infrastructure
2. **Oracle 6 Verification Failure**: Evaluated reports, not reality
3. **Fragmented Intention Tracking**: Pre-compass scattered approach

### Success Patterns

1. **Oracle 3 Model**: Orchestration infrastructure pattern
2. **Oracle 10-11 Blitzkrieg**: Parallel stream execution
3. **Oracle 12 Constellation**: Purpose-specialized platforms

---

## MAINTENANCE SCHEDULE

| Action | Frequency | Responsible |
|--------|-----------|-------------|
| Extract intentions | Every Council session | Commander |
| Categorize captures | Session checkpoint | Commander |
| Resolve completed | Immediately on completion | Executing agent |
| Pattern analysis | Monthly | Any Council |
| Archive old resolved | Quarterly | Any Council |

---

## VERSION HISTORY

**v4.0.0** (2026-02-24): CC28 Intention Pruning — 97 → 35 Active
- 38 DONE intentions archived (Phases 0-2 infrastructure, historical resolved)
- 14 STALE intentions archived (missed deadlines, no activity 5+ sessions)
- 10 MERGED intentions archived (subsumed by broader intentions)
- 27 patterns archived as "institutionalized" (embedded in constitutional rules, AGENTS.md, operational practice)
- 5 patterns retained as operationally active: P004, P017, P028, P034, P035
- 35 active intentions cluster: Pipeline/Feedcraft, Infrastructure, Architecture, Content, Security
- Authority: Sovereign + Commander / CC28

**v3.5.0** (2026-02-24): Loose End Capture — Constellation Accommodation + Skills Arsenal (Session 24)
- INT-2201 (repo rearchitecture) → RESOLVED: agent offices + collab/ deployed
- INT-2203 (collaboration directory) → RESOLVED: collab/ with anti-proliferation policy
- INT-2202 (MBA consolidation) → PROMOTED from deferred to active P1, blocked by DC-208 research
- INT-2204 (platform accommodation) → PROMOTED from P2 to P1, 3 sub-problems identified
- INT-2401: NEW — OpenClaw architecture harmonization (compose, don't compete)
- INT-2402: NEW — CLI agent heterogeneity strategy (formalize file-first dispatch)
- INT-2403: NEW — Ultimate power-user harness for every CLI agent (cross-platform skill portability)
- INT-2404: NEW — Skills audit + bleeding-edge shopping via Oracle recon (onboard/white-label/verticalize)
- INT-2405: NEW — Vendor-Native Epistemology (platform interaction grammars as epistemic routing)
- INT-2406: NEW — Manus evaluation for automation plumbing
- INT-2407: NEW — macOS actuator suite procurement (durable seam tools)
- INT-2408: NEW — Exocortex integration (19 deep researches, SaaS slotting, free-tier leverage)
- INT-2409: NEW — CLI ↔ webapp bridge architecture (Grok-reads-GitHub pattern)
- INT-2410: NEW — Constellation avatarization thesis (cognitive archetypes as dispatch intelligence)
- INT-2411: NEW — Psyche/Ajna recharacterization via OpenClaw personality tuning
- INT-2412: NEW — Recanonize after research (content enrichment of CANON from corpus extraction)
- INT-P032: NEW pattern — work with the grain, not against it
- INT-P033: NEW pattern — research before architecture (DC-208 informs design)
- Authority: Commander / Sovereign Session 24

**v3.5.0** (2026-02-23): Corpus×Intention Synthesis — Phase 2 Capstone (Council 25)
- 14,311 atoms from 1,152 sources cross-referenced against 80+ active intentions
- 5 parallel mining agents: memory, dispatch, feedcraft, security, exocortex
- INT-2413: NEW — Ingest execution logs as action nodes into Graphiti (context graphs pattern)
- INT-2414: NEW — Mine execution logs for emergent operational patterns (process pattern mining)
- INT-2415: NEW — Enable agent self-maintenance of memory (promote/demote/reorganize, Letta model)
- INT-2416: NEW — Implement scored context loading with TTL decay (7d/30d/90d)
- INT-P034: NEW pattern — Feedback loops > memory engineering (the real bottleneck is quality signals, not storage)
- INT-P035: NEW pattern — Security is Phase 0 of every phase (not Phase 5 — 230+ malicious skills Jan-Feb 2026)
- INT-P036: NEW pattern — Feedcrafting = computational RAS (filter by declared intentions, not engagement)
- INT-P037: NEW pattern — Syncrescendence IS the exocortex (connect, don't build from scratch)
- REFRAME: DC-140 security audit reclassified from Phase 5 → continuous concern
- REFRAME: DC-P20 exocortex = "connect existing exocortex to external sources via MCP"
- REFRAME: DC-P19 macOS actuators = "adopt OpenClaw CLI ecosystem, not buy GUI tools"
- REFRAME: INT-2104 feedcrafting = "computational RAS with intention-weighted scoring"
- Phase 2 assessed as SUBSTANTIALLY COMPLETE (all P0 items done, quality gate + cluster engine are P1)
- Deliverable: `agents/commander/outbox/DECISION_ATOMS-PHASE2-CORPUS_INTENTION_SYNTHESIS-2026-02-23.md`
- Authority: Commander / Sovereign Council 25

**v3.4.0** (2026-02-23): The Revert — Execution Over Architecture (Council 22)
- INT-2210 (scaffold triage) REVERTED: 6 commits rolled back to d33aaf13 (INT-2209)
- INT-2301–2307: Infrastructure→Memory→Scaffold→Automations critical path established
- INT-P028–P031: Execution discipline patterns seared (14% delivery rate, phase gates, no-triage-without-validation)
- DYN-DEFERRED_COMMITMENTS.md overwritten with phased execution plan (DC-100 through DC-146 + 10 parked)
- Phase gate rule: no phase begins until prior phase P0 items DONE
- Triangulated Oracle/Vanguard/Diviner specs (memory architecture, antifragile scaffold, scaffold consensus) aligned to execution order
- Backup branch: `backup-pre-revert-2026-02-22` preserves reverted work
- Authority: Sovereign + Commander / Council 22

**v3.3.0** (2026-02-22): Dual-Stream Architecture + Account Feed Restructure (Session 21)
- INT-2101: Dual-stream architecture plan — automated intelligence + serendipitous encounters, GCP/Gemini pipeline
- INT-2102: 3-tier consumption model (read/listen/consumption-worthy) — replaces CANON-31143 4-tier
- INT-2103: Account feed restructure — A1=liberal arts/philosophy/history, A2=AI/CS/IT/CogSci (all paid), A3=multimodal creation
- INT-2104: Feedcrafting algorithm for both streams
- INT-2105: Serendipitous→digest bridge pipeline
- INT-2107: CLI Agent Setup Architecture docs — per-platform setup parity
- INT-2108: Three-track evaluation framework (onboard/white-label/verticalize)
- INT-P026: Google world-models pivot rebalances account thesis
- INT-P027: Paradigm shipping velocity demands systematic evaluation
- Authority: Commander / Sovereign Session 21

**v3.2.0** (2026-02-22): Repo Rearchitecture Directive (Session 20)
- INT-2201: Complete repo rearchitecture — agent-centric offices, per-platform init files, rename COCKPIT — P1 backlog, blocked by sources research
- INT-2202: MBA-primary consolidation — Mac mini underutilized, SSH control plane — P1 backlog
- INT-2203: Collaboration directory design — shared multi-agent workspace with anti-proliferation policy — P1 backlog
- INT-2204: Platform-native accommodation — Gemini 3.1 Pro, Grok Build, OpenClaw arch alignment — P2 backlog
- Authority: Commander / Sovereign Session 20

**v3.1.0** (2026-02-19): Grok Build Backlog Entry (Session 19)
- INT-1901: Grok Build avatarization — P2 backlog, blocked by public release. Pre-position slot in constellation.
- INT-C012: Capture entry for Grok Build monitoring
- Authority: Commander / Sovereign Session 19

**v3.0.0** (2026-02-09): Sovereign Expansion Directive (Session 16)
- 18 new intentions (INT-1601 through INT-1618) from massive Sovereign brain dump
- 3 new patterns (INT-P014 through INT-P016): token economics, dual-machine paradigm, web app thesis confirmation
- 3 new captures (INT-C008 through INT-C010): Notion/Airtable/LifeOS discussion, celestial alignment
- 14 Linear issues created (SYN-37 through SYN-50)
- 8 ClickUp tasks created across Professional/Personal/Financial spaces
- Narrative DNA expanded: Marvel, Star Wars, Star Trek, Accelerando
- Dependency map expanded with new intention chains
- Authority: Commander / Sovereign Session 16

**v2.0.0** (2026-02-01): Pre-Oracle Extraction + Resolution Sweep
- Metabolized `my inputs.md` (16K, 50 entries) → 20 INT-MI entries
- 14 resolved (by PROJ-RESTRUCTURE, PROJ-SN-VARS, PROJ-CANON-LEAN, PROJ-AVATARS)
- 6 active (Google pipeline, on-device automation, Palantir ontology)
- 5 new patterns (P009-P013: platform cognitive strengths, trade-off philosophy)
- Resolved INT-C001 (corpus audit) and INT-C004 (corpus hygiene sprint)
- Authority: Oracle 13+ / Commander session

**v1.0.0** (2026-01-11): Genesis establishment
- Complete extraction from Oracle 0-12
- Schema defined with 5 categories
- Integration protocol documented
- Pattern analysis included
- Authority: Oracle 12 / DIRECTIVE-043A

---

**END ARCH-INTENTION_COMPASS.md**
