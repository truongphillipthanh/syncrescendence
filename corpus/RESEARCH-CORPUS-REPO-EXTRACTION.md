# Research Corpus: Repository & Tool Extraction

**Date:** 2026-02-16
**Source:** 267 research files at `/Users/system/Desktop/research/`
**Purpose:** Comprehensive extraction of all GitHub repos, npm packages, tools, and frameworks referenced across the research corpus for Syncrescendence whitelabel/customization evaluation.

---

## 1. AGENT INFRASTRUCTURE (MCP Servers, Orchestration Frameworks)

### 1.1 OpenClaw / Clawdbot / Moltbot (Core Platform)
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/openclaw/openclaw` | Core open-source AI agent platform (108K+ stars). Formerly Clawdbot/Moltbot. Local-first, chat-platform integration, skills, heartbeat system. | `20260129-website-introducing-openclaw--openclaw.md`, `20260203-openclaw_minimax.md`, multiple | **CRITICAL** - Primary agent infrastructure for constellation |
| `https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md` | Contributing guide | `20260129-website-introducing-openclaw--openclaw.md` | Reference |
| `https://github.com/openclaw/openclaw/security` | Security advisories | `20260211-witcheer.md` | Security hardening |
| `https://github.com/sponsors/openclaw` | Sponsorship page | `20260129-website-introducing-openclaw--openclaw.md` | Community |
| `https://docs.openclaw.ai/` | Official documentation portal | Multiple files | Reference |
| `https://agentskills.io/` | Agent Skills Open Standard specification | `20260204-deep_dive_on_agent_skills.md`, `20260209-ai_agent_army.md` | **HIGH** - Skills spec standard |
| `npm install -g @openclaw/openclaw` | npm global install | `20260203-openclaw_minimax.md` | Install method |

### 1.2 Claude Code Agent Teams & Skills
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/anthropics/skills` | Anthropic's official public skills repository. Dozens of customizable skills. | `20260209-ai_agent_army.md` | **HIGH** - Official skill templates |
| `https://github.com/anthropics/claude-plugins-official` | Official Claude Code plugin directory (incl. playground plugin) | `20260208-claude_code_plugin_visual.md`, `20260207-deedydas.md` | **HIGH** - Plugin ecosystem |
| `https://github.com/anthropic-experimental/sandbox-runtime` | Claude Code open source sandbox runtime for safer agent execution | `20260211-bcherny.md` | **HIGH** - Security sandbox |
| `https://skills.sh` | Skills.sh - CLI for browsing/installing agent skills | `20260201-prompt_engineering_501.md` | Skills distribution |
| `https://www.clawhub.ai` | ClawHub - Public skill registry for OpenClaw (~700+ skills) | Multiple files | **HIGH** - Skill marketplace |

### 1.3 Multi-Agent Orchestration
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| Claude-Flow | Claude-first orchestration (13.6k stars), 60+ agents, swarm coordination, 3-tier routing (WASM->Haiku->Opus), Byzantine consensus | `RESPONSE-VIZIER-20260203.md` | **CRITICAL** - Multi-agent orchestration |
| CrewAI | Role-based agent crews (30.5k stars, 1M monthly downloads), 700+ integrations, 5.76x faster than LangGraph | `RESPONSE-VIZIER-20260203.md`, `RESPONSE-AUGUR-20260203.md` | HIGH - Alternative framework |
| LangGraph | Industry standard for complex agent workflows with lowest latency | `RESPONSE-VIZIER-20260203.md`, `RESPONSE-AUGUR-20260203.md` | HIGH - Alternative framework |
| `https://github.com/agno-agi/dash` | Dash - Open-source data agent (OpenAI's internal agent architecture, open-sourced). SQL agent with 6-layer context and self-learning memory. | `20260201-dash.md`, `20260202-ashpreetbedi.md` | **HIGH** - Data agent pattern |
| `https://github.com/Team9ai` | Team9.ai - Native AI workspace for deploying infinite OpenClaw agents with zero local setup. Going open-source. | `20260209-team9_ai.md` | HIGH - Agent deployment platform |

### 1.4 Agent Teams Infrastructure
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/ericbuess/claude-code-docs.git` | Documentation repo for Claude Code agent teams | `20260206-claude_code_agent_teams.md` | Reference |
| `https://github.com/mkusaka/it2` | it2 CLI for iTerm2 Python API (enables split panes for agent teams) | `20260206-claude_code_agent_teams.md` | Tooling |
| `https://github.com/tmux/tmux/wiki` | tmux - Terminal multiplexer for agent team coordination | `20260206-claude_code_agent_teams.md` | Tooling |
| `https://github.com/ghostty-org/ghostty` | Ghostty terminal emulator (split pane support for agents) | `20260202-ghostty_nightly.md` | Tooling |

---

## 2. MEMORY SYSTEMS (Context, Knowledge Graphs, Recall)

### 2.1 Memory Plugins & Services
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `openclaw plugins install @honcho-ai/openclaw` | Honcho - Memory that reasons. Builds working model of user. Continual learning, implicit pattern extraction. | `20260203-openclaw_honcho.md` | **CRITICAL** - Advanced memory |
| `https://app.honcho.dev` / `https://docs.honcho.dev` | Honcho web app and documentation | `20260203-openclaw_honcho.md` | Reference |
| `https://supermemory.ai` | SuperMemory - Cross-platform memory sync for agents (Telegram, WhatsApp, Slack). Replaces local memory files. | `20260127-supermemory.md` | **HIGH** - Memory layer |
| `https://github.com/Versatly/clawvault` | ClawVault - Solving memory for OpenClaw and general agents. npm package: `clawvault` | `20260213-solving_memory.md` | HIGH - Memory solution |
| `npm install clawvault` | ClawVault npm package | `20260213-solving_memory.md` | Install |
| `https://github.com/letta-ai/letta-code` | Letta Code - The memory-first coding agent. Context repositories (git-tracked files as memory). | `20260212-letta_ai.md` | **HIGH** - Memory-first agent |
| `@mastra/memory` / `@mastra/core/agent` | Mastra - Observational memory system for AI agents. Human-inspired memory with benchmarks. | `20260210-observational_memory.md` | HIGH - Memory architecture |
| `https://github.com/mastra-ai/mastra` | Mastra framework repo (includes LongMemEval benchmark) | `20260210-observational_memory.md` | Reference |

### 2.2 Context & Search Systems
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/tobi/qmd` | QMD - Local indexing and retrieval tool by Tobi Lutke. BM25 keyword search + vector search + reranking. SQLite-based. | `20260131-agentic_pkm.md`, `20260212-every_openclaw_issue.md`, `20260213-compounding_ai_os.md` | **CRITICAL** - Local search engine for agents |
| `https://github.com/TheAgentContextLab/OneContext` | OneContext - Context management for Claude Code. Improves SWE-Bench by ~13%. `npm i -g onecontext-ai` | `20260207-onecontext.md` | **HIGH** - Context optimization |
| `npm i -g onecontext-ai` | OneContext npm install | `20260207-onecontext.md` | Install |
| `https://hornet.dev` | Hornet.dev - Retrieval engine built specifically for agents. Agent DX-optimized search. | `20260203-few_things_worth_building.md` | HIGH - Agent search |
| Unstructured.io | Open-source platform for multi-format parsing, intelligent chunking, metadata preservation | `20260208-agent_architecture_guide.md` | HIGH - Document processing |

### 2.3 Knowledge Management Integrations
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/lobehub/lobehub` | LobeHub - Agent groups, multi-agent collaboration, knowledge bases (RAG), multi-model routing, visual interface. | `20260129-openclaw_full_product.md` | **HIGH** - Agent design + KB |
| `@lobehub/tts` | LobeHub TTS toolkit - Production-quality text-to-speech (15 lines for OpenAI-level speech) | `20260129-openclaw_full_product.md` | Voice integration |
| Obsidian + Claude Code | Async hooks for note history, wikilinks as cognitive architecture | `20260118-obsidian_claude_code.md`, `20260125-obsidian_claude_code_101.md`, `20260206-agentic_note_taking.md` | **HIGH** - PKM integration |
| LogSeq | Outliner-style notes app with markdown files. Agent read/write via iCloud sync. | `20260207-automatic_discipline.md` | PKM alternative |

---

## 3. AUTOMATION (Browser, Workflow, Scheduling)

### 3.1 Browser Automation
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/jo-inc/camofox-browser` | CamoFox Browser - OpenClaw browser that doesn't get blocked. Anti-fingerprint, Bezier mouse trajectories. MIT-licensed. | `20260210-camofox_browser.md` | **HIGH** - Stealth browsing |
| `openclaw plugins install @askjo/camofox-browser` | CamoFox OpenClaw plugin install | `20260210-camofox_browser.md` | Install |
| `https://github.com/daijro/camoufox` | Camoufox - Upstream anti-detection browser patches (WebGL spoofing, WebRTC IP masking, etc.) | `20260210-camofox_browser.md` | Upstream dependency |
| `https://github.com/lekt9/unbrowse-openclaw` | Unbrowse - 100x faster than browser automation. Captures website internal APIs, turns into tools. | `20260203-unbrowse.md` | **HIGH** - API extraction |
| `openclaw plugins install @getfoundry/unbrowse-openclaw` | Unbrowse OpenClaw plugin install | `20260203-unbrowse.md` | Install |
| Hyperbrowser | AI agents can now learn from web browsing | `20260204-hyperbrowser.md` | Browser learning |

### 3.2 Workflow & Scheduling Tools
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| n8n | Workflow automation platform (RSS triggers, HTTP requests, email nodes, AI agent nodes) | `20260206-how_to_stop_feeling_behind.md` | HIGH - Workflow engine |
| `npm install -g todoist-ts-cli` | Todoist CLI for task management integration | `20260205-clawdbot_masterclass.md` | Task management |
| `https://mcp.linear.app/mcp` | Linear MCP server for task/project management | `20260202-dkundel.md` | **HIGH** - Project management |
| Moltbook | Social network for AI agents. Heartbeat-driven agent content platform (~153K agents). | `20260206-unreasonable_effectiveness.md`, `20260214-minchoi.md` | Agent social network |

### 3.3 Content & Social Automation
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/rohunvora/x-research-skill` | X/Twitter research skill for Claude Code and OpenClaw. Agentic search, thread following, deep-dives. 78 stars. | `20260208-frankdegods.md` | **HIGH** - X research |
| Postiz | Social media posting automation (used by OpenClaw agent "Larry" for X posting) | `20260212-openclaw_agent_larry.md` | Social automation |
| Postey.ai | Social-specific workflow (caption generation, multi-platform posting, scheduling, analytics) | `20260124-clawdbot_40_hours.md` | Social automation |
| `bird` skill | OpenClaw skill for browsing X, made by @steipete (OpenClaw creator) | `20260212-openclaw_agent_larry.md` | X integration |

---

## 4. SECURITY (Hardening, Sandboxing, Scanning)

### 4.1 Security Tools & Standards
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/Dicklesworthstone/acip` | ACIP (Advanced Cognitive Inoculation Prompt) - Prompt injection resistance. Teaches model to recognize manipulation patterns. | `20260131-safe_sandboxed.md`, `20260202-security_first_guide.md` | **CRITICAL** - Prompt injection defense |
| `npx clawhub install skillguard` | SkillGuard - Audits skills for security issues before installation. Checks permissions, suspicious patterns. | `20260202-security_first_guide.md` | **HIGH** - Skill auditing |
| `npx clawhub install prompt-guard` | Prompt-Guard - Additional prompt injection resistance layer | `20260202-security_first_guide.md` | **HIGH** - Injection defense |
| SHIELD.md | Security standard for OpenClaw/AI agents. Policy file at agent root. Allowlists, blocklists, threat categories. | `20260206-shield_md.md` | **HIGH** - Security standard |
| `https://nova-hunting.github.io/shield.md/` | SHIELD.md documentation site | `20260206-shield_md.md` | Reference |
| `https://clawdex.koi.security` | Clawdex - Koi Security's skill scanner. Web version to check skills before install. | `20260211-witcheer.md` | Skill scanning |
| `https://github.com/vignesh07/clawdbot-formal-models` | Machine-checkable formal security models for Clawdbot/OpenClaw | `20260129-introducing-openclaw.md` | Formal verification |
| MoltThreats | Prompt intelligence tool at `promptintel.novahunting.ai/molt` | `20260206-shield_md.md` | Threat intelligence |

### 4.2 Network & Infrastructure Security
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| Tailscale | WireGuard-based mesh VPN. Peer-to-peer encrypted. Free tier: 100 devices. Key for agent isolation. | `20260202-security_first_guide.md`, `20260205-jordanlyall.md`, `20260206-tailscale_illusion.md` | **CRITICAL** - Network isolation |
| `https://github.com/cloudflare/cloudflared` | Cloudflare Tunnel - Secure access to agent dashboard without public ports | `20260126-securing_clawdbot_vps.md` | Infrastructure |
| Docker | Container isolation for agent sandboxing | `20260211-witcheer.md` | Sandboxing |

---

## 5. SKILLS & PROMPTS (Skill Repos, Prompt Libraries, Builders)

### 5.1 Skill Repositories
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/elevenlabs/skills` | ElevenLabs skills - Voice call integration for OpenClaw. `npx skills add elevenlabs/skills` | `20260204-deep_dive_skills.md`, `20260206-elevenlabs_agents.md` | **HIGH** - Voice skills |
| `https://github.com/jbrukh/skills` | jbrukh skills - Includes "sharpen-output" skill (self-improving prompt quality) | `20260201-prompt_engineering_501.md` | Prompt engineering |
| `https://github.com/rjs/shaping-skills` | Shaping & breadboarding skills for product development with Claude Code | `20260207-shaping_0_1.md` | Product skills |
| `https://github.com/rb-mm/skillmaxxer-3000` | Skillmaxxer 3000 - Meta-skill for building expert-level Claude skills | `20260207-skillmaxxer_3000.md`, `20260213-compounding_ai_os.md` | **HIGH** - Skill builder |
| `https://github.com/rjs/tick` | Tick project - Example repo with all markdown docs Claude generated (shaping methodology) | `20260207-shaping_0_1.md` | Reference |
| `https://github.com/badlogic/pi-skills` | Pi skills - Skills for local AI agent on MacBook (pi-coding-agent) | `20260212-local_ai_agent.md` | Local agent skills |
| `https://www.clawhub.ai/ivaavimusic/x402-layer` | x402-layer / Singularity Layer - Agent autonomous earning skill | `20260202-openclaw_skill_earn.md` | Agent economy |
| RevenueCat skill | Analytics skill for customer subscriptions/churn tracking (by RevenueCat CEO) | `20260212-openclaw_agent_larry.md` | Business analytics |

### 5.2 Plugin Collections
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/composio/awesome-claude-plugins` (alias: `ComposioHQ/awesome-claude-plugins`) | Community-maintained collection of Claude Code plugins outside official directory. Includes connect-apps plugin. | `20260203-openclaw_minimax.md` | **HIGH** - Plugin discovery |
| `https://github.com/dair-ai/dair-academy-plugins` | Image generator plugin for Claude Code (Gemini Nano under hood, text-to-image, 4K resolution) | `20260208-claude_code_plugin_visual.md` | Visual workflow |
| `https://github.com/EveryInc/compound-engineering-plugin` | Compound Engineering plugin for Claude Code | `20260208-compound_engineering.md` | Engineering practice |
| awesome-openclaw-skills | Community-maintained categorized skill overview list | `20260202-security_first_guide.md` | Discovery |

### 5.3 Prompt & Skill Methodology
| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/danielmiessler/TheAlgorithm` | The Algorithm (v0.5.6) - Self-improvement system by Daniel Miessler | `20260214-danielmiessler.md` | **HIGH** - Self-improvement |
| `https://github.com/Shubhamsaboo/awesome-llm-apps` | Awesome LLM Apps - 100+ open-source agent implementations | `20260210-skills_that_matter.md` | Reference collection |
| `https://github.com/weitianxin/Awesome-Agentic-Reasoning` | Awesome Agentic Reasoning - Academic paper + curated list (Meta, Amazon, DeepMind) | `20260205-meta_amazon_deepmind.md` | Research reference |

---

## 6. VOICE & COMMUNICATION

| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| ElevenLabs Conversational AI API | Phone call integration for OpenClaw (voice calls via ngrok proxy) | `20260204-elevenlabs_agents.md`, `20260206-elevenlabs_agents.md` | **HIGH** - Voice interface |
| `openclaw plugins install @openclaw/matrix` | Matrix chat protocol plugin for OpenClaw | `20260202-security_first_guide.md`, `20260211-witcheer.md` | Chat integration |
| BlueBubbles | iMessage integration for agents (5 email accounts, calendars, iMessages) | `20260201-20_more_setups.md` | Messaging |
| Granola | Meeting transcript integration | `20260201-20_more_setups.md` | Meetings |

---

## 7. SEARCH & WEB APIs

| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| Brave Search API | LLM Context API. Own index, privacy, MCP server ready. 2K free queries/month. $5/1K after. | `20260213-agent_search.md`, `RESPONSE-VANGUARD.md` | **CRITICAL** - Agent web search |
| `@anthropic/mcp-server-brave-search` | Brave Search MCP server npm package | `20260129-openclaw_full_product.md` | MCP integration |
| Tavily | Search API for agents (comparison in agent search article) | `20260213-agent_search.md` | Search alternative |
| Exa | Semantic search API for research tasks | `20260213-agent_search.md` | Research search |
| Firecrawl | Deep web extraction, anti-bot fallback for web_fetch | `20260213-agent_search.md`, `RESPONSE-DIVINER.md` | Web extraction |
| Perplexity | AI search (comparison reference) | `20260213-agent_search.md` | Search alternative |

---

## 8. MODEL ROUTING & COST OPTIMIZATION

| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/BlockRunAI/ClawRouter` | ClawRouter - Intelligence routing layer between OpenClaw and AI providers/models. Cost optimization. | `20260211-how_not_to_go_broke.md` | **HIGH** - Cost management |
| Ollama | Local model runner. `curl -fsSL https://ollama.com/install.sh`. Used for $0 heartbeats. | `20260207-openclaw_mac_mini.md`, `20260202-minchoi.md` | **HIGH** - Local models |
| `npm install -g @mariozechner/pi-coding-agent` | Pi-coding-agent - Local coding agent for MacBook | `20260212-local_ai_agent.md` | Local agent |
| `npx ccusage@latest daily` | ccusage - Token usage monitoring tool | `20260207-openclaw_mac_mini.md` | Cost tracking |
| llama.cpp | Local LLM inference (`brew install llama.cpp`) | `20260212-local_ai_agent.md` | Local inference |
| mlx-lm | Apple MLX local LLM (`pip install mlx-lm`) | `20260212-local_ai_agent.md` | Apple silicon inference |
| `https://github.com/MiniMax-AI/MiniMax-M2` | MiniMax M2 model repo | `20260203-openclaw_minimax.md` | Budget model |

---

## 9. DEVELOPMENT & DEPLOYMENT

| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| Supabase | PostgreSQL backend for agent state (shared memory, mission queues). Used with pgvector for RAG. | `20260207-6_ai_agents.md` | **HIGH** - Agent state DB |
| Vercel | Serverless deployment for agent heartbeat APIs, cron jobs | `20260207-6_ai_agents.md` | Deployment |
| `https://github.com/nvm-sh/nvm` | Node Version Manager (used in OpenClaw setup) | `20260202-security_first_guide.md` | Setup tool |
| `https://github.com/shadcn-ui/ui` | shadcn/ui - UI component library (used as test codebase for react-grab benchmark) | `20260203-how_i_made_claude_code_3x_faster.md` | UI components |
| `https://github.com/aidenybai/react-grab` | React Grab - Makes Claude Code 3x faster at UI element retrieval. Open source. | `20260203-how_i_made_claude_code_3x_faster.md` | **HIGH** - Agent UI tool |
| `https://github.com/astral-sh/ruff` | Ruff - Fast Python linter (recommended for agent code quality) | `20260203-claude_code_for_scientists.md` | Code quality |
| `https://github.com/patrickmineault/true-neutral-cookiecutter` | True neutral cookiecutter - Project template for scientific computing | `20260203-claude_code_for_scientists.md` | Project template |

---

## 10. MONITORING & OBSERVABILITY

| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/koala73/worldmonitor` | World Monitor - Makes agents aware of world events | `20260213-world_monitor.md` | **HIGH** - World awareness |
| Sentry MCP server | Error monitoring + code review skill | `20260209-ai_agent_army.md` | Error tracking |
| Attio / Universal Context | CRM with agent-friendly MCP server, semantic search, external consistency | `20260205-introducing_universal_context.md` | CRM integration |

---

## 11. COMMUNITY & HOME AUTOMATION PLUGINS

| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://github.com/buddyh/alexa-cli` | Alexa CLI - Control Amazon Alexa devices via Clawdbot/OpenClaw | `20260201-20_more_setups.md` | Smart home |
| `https://github.com/pepicrft/clawd-plugin-grocery` | Grocery plugin for Clawdbot - Shopping list management | `20260201-20_more_setups.md` | Personal automation |
| `https://github.com/ivaavimusic/SGL_DOCS_2025` | Singularity Layer documentation | `20260202-openclaw_skill_earn.md` | Agent economy |
| `https://github.com/Ronakkadhi/awesome-openclaw-usecases` | Running list of OpenClaw use cases | `20260209-openclaw_browser_email.md` | Use case catalog |
| Boktoshi | Agent security hardening platform | `20260206-tailscale_illusion.md` | Security |

---

## 12. CLOUD AGENT PLATFORMS

| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| Warp / Oz (oz.dev) | Cloud-native agents with coding capabilities, persistent work records, live human takeover. Warp Drive for agent memory. | `20260213-multi_agent_collaboration.md` | **HIGH** - Cloud agent platform |
| Team9.ai | Native AI workspace for deploying OpenClaw agents. Going open-source. | `20260209-team9_ai.md` | Agent deployment |
| Hetzner | VPS provider for always-on agent hosting | `20260129-openclaw_full_product.md` | Infrastructure |

---

## 13. COMPANION GISTS & CONFIG REFERENCES

| URL / Reference | Description | Source File | Relevance |
|---|---|---|---|
| `https://gist.github.com/jordanlyall/8b9e566c1ee0b74db05e43f119ef4df4` | Complete security setup commands for OpenClaw (Tailscale, allowlists, read-only tokens) | `20260205-jordanlyall.md` | **HIGH** - Security config |
| `https://gist.github.com/dabit3/86ee04a1c02c839409a02b20fe99a492` | "You Could've Invented OpenClaw" - Full implementation gist | `20260213-you_couldve_invented_openclaw.md` | Architecture reference |
| `https://github.com/shanraisshan/claude-code-best-practice` | Claude Code best practices repository | `20260207-dr_cintas.md` | Best practices |

---

## PRIORITY MATRIX: Syncrescendence Whitelabel Candidates

### Tier 1: Immediate Integration (Critical Path)
These directly enable constellation agent capabilities:

1. **QMD** (`github.com/tobi/qmd`) - Local search engine for agent memory. Replaces need for external embedding APIs. Perfect for Ontology DB integration.
2. **ACIP** (`github.com/Dicklesworthstone/acip`) - Prompt injection defense. Non-negotiable for any agent with system access.
3. **Honcho** (`@honcho-ai/openclaw`) - Memory-that-reasons. Replaces brittle file-based memory with continual learning.
4. **SHIELD.md** (`nova-hunting.github.io/shield.md`) - Security policy standard. Should be part of every constellation agent.
5. **Brave Search MCP** (`@anthropic/mcp-server-brave-search`) - Web grounding for agents. LLM-optimized context.
6. **Anthropic Skills Repo** (`github.com/anthropics/skills`) - Official skill templates to fork/customize.

### Tier 2: High-Value Enablers
These multiply agent effectiveness:

7. **ClawRouter** (`github.com/BlockRunAI/ClawRouter`) - Model routing for cost optimization across 5 agents.
8. **OneContext** (`github.com/TheAgentContextLab/OneContext`) - Context management (+13% on SWE-Bench).
9. **CamoFox Browser** (`github.com/jo-inc/camofox-browser`) - Anti-detection browsing for research agents.
10. **Unbrowse** (`github.com/lekt9/unbrowse-openclaw`) - API extraction from any website.
11. **Skillmaxxer 3000** (`github.com/rb-mm/skillmaxxer-3000`) - Meta-skill for building constellation-specific skills.
12. **Letta Code** (`github.com/letta-ai/letta-code`) - Memory-first coding agent architecture.
13. **React Grab** (`github.com/aidenybai/react-grab`) - 3x faster UI element retrieval for coding agents.

### Tier 3: Ecosystem Enrichment
These extend capabilities for specific use cases:

14. **LobeHub** (`github.com/lobehub/lobehub`) - Multi-agent visual design + knowledge base + TTS.
15. **Dash** (`github.com/agno-agi/dash`) - Data agent with self-learning SQL.
16. **ElevenLabs Skills** (`github.com/elevenlabs/skills`) - Voice call integration.
17. **World Monitor** (`github.com/koala73/worldmonitor`) - World event awareness.
18. **Composio Plugins** (`github.com/composio/awesome-claude-plugins`) - Plugin collection for tool access.
19. **X Research Skill** (`github.com/rohunvora/x-research-skill`) - Twitter/X agentic search.
20. **Compound Engineering Plugin** (`github.com/EveryInc/compound-engineering-plugin`) - Engineering practice enforcement.

### Tier 4: Reference & Architecture
Not for direct integration, but inform constellation design:

21. **Claude-Flow** - Swarm orchestration patterns (3-tier routing, Byzantine consensus).
22. **The Algorithm** (`github.com/danielmiessler/TheAlgorithm`) - Self-improvement methodology.
23. **Awesome Agentic Reasoning** (`github.com/weitianxin/Awesome-Agentic-Reasoning`) - Academic survey.
24. **Awesome LLM Apps** (`github.com/Shubhamsaboo/awesome-llm-apps`) - 100+ implementations.
25. **Formal Security Models** (`github.com/vignesh07/clawdbot-formal-models`) - Machine-checkable security.

---

## NPM PACKAGES SUMMARY

| Package | Install Command | Purpose |
|---|---|---|
| `@openclaw/openclaw` | `npm install -g @openclaw/openclaw` | Core platform |
| `@anthropic-ai/claude-code` | `npm install -g @anthropic-ai/claude-code` | Claude Code |
| `@mariozechner/pi-coding-agent` | `npm install -g @mariozechner/pi-coding-agent` | Local coding agent |
| `@honcho-ai/openclaw` | `openclaw plugins install @honcho-ai/openclaw` | Memory plugin |
| `@askjo/camofox-browser` | `openclaw plugins install @askjo/camofox-browser` | Browser plugin |
| `@getfoundry/unbrowse-openclaw` | `openclaw plugins install @getfoundry/unbrowse-openclaw` | API extraction |
| `@openclaw/matrix` | `openclaw plugins install @openclaw/matrix` | Matrix chat |
| `@anthropic/mcp-server-brave-search` | via MCP config | Web search |
| `todoist-ts-cli` | `npm install -g todoist-ts-cli` | Task management |
| `onecontext-ai` | `npm i -g onecontext-ai` | Context management |
| `clawvault` | `npm install clawvault` | Memory system |
| `ccusage` | `npx ccusage@latest daily` | Token monitoring |
| `skillguard` | `npx clawhub install skillguard` | Skill auditing |
| `prompt-guard` | `npx clawhub install prompt-guard` | Injection defense |

---

## KEY DOCUMENTATION URLS

| URL | Purpose |
|---|---|
| `https://docs.openclaw.ai/` | OpenClaw docs |
| `https://docs.openclaw.ai/gateway/security` | Security best practices |
| `https://docs.openclaw.ai/gateway/heartbeat` | Heartbeat system |
| `https://docs.openclaw.ai/tools/clawhub` | ClawHub docs |
| `https://docs.openclaw.ai/tools/skills` | Skills docs |
| `https://docs.openclaw.ai/concepts/multi-agent` | Multi-agent routing |
| `https://agentskills.io/specification` | Agent Skills spec |
| `https://code.claude.com/docs/en/agent-teams` | Claude Code agent teams |
| `https://code.claude.com/docs/en/hooks` | Claude Code hooks |
| `https://code.claude.com/docs/en/skills` | Claude Code skills guide |
| `https://docs.anthropic.com/en/docs/claude-code/memory` | CLAUDE.md memory system |
| `https://ai.ethereum.foundation/blog/openclaw-security-guide` | Security guide (EF) |

---

## STATISTICS

- **Total distinct GitHub repos extracted:** 42
- **Total npm packages identified:** 14
- **Total OpenClaw plugins cataloged:** 5
- **Total ClawHub skills referenced:** 4 (SkillGuard, Prompt-Guard, x402-layer, RevenueCat)
- **Total MCP servers mentioned:** 8+ (Brave Search, Linear, Sentry, Gmail, Google Calendar, Zapier, Apple Xcode, custom RAG)
- **Total cloud/SaaS tools referenced:** 15+ (Tailscale, Cloudflare, Supabase, Vercel, Hetzner, ElevenLabs, Brave, Attio, etc.)
- **Total framework comparisons found:** 5 (Claude-Flow, CrewAI, LangGraph, AutoGPT, AgentStack)
- **Files containing actionable repo/tool references:** ~85 of 267 (32%)

---

*Generated by Commander (COO) for Syncrescendence Constellation. Cross-reference with CLARESCENCE-2026-02-09-el-dorado-armory-reconnaissance.md and CLARESCENCE-2026-02-09-awesome-openclaw-appropriation.md for prior reconnaissance.*
