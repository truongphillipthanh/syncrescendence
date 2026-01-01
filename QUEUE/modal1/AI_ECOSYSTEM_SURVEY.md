# AI ECOSYSTEM SURVEY (OPERATIONAL)

**Document Type**: OPERATIONAL (Living Document)
**Last Updated**: 2025-12-21
**Refresh Cycle**: 30 days
**Next Review**: 2026-01-20
**Status**: Current (needs refresh for post-December developments)
**Graduation Candidate**: No (perishable content, ongoing updates expected)

---

## REFRESH NOTES

**Current State**: Document reflects December 2025 frontier AI landscape. Comprehensive survey of CLI tools, product releases, browser integrations, system prompt configurability, recent market shifts, and practitioner toolkit.

**Sections Needing Update** (as of 2025-12-29):
- CLI tools pricing/features (Claude Code, Codex CLI, Gemini CLI evolving rapidly)
- Model releases (frontier labs release cadence: monthly-quarterly)
- Browser landscape (ChatGPT Atlas, Comet, Opera Neon early-stage, expect feature additions)
- MCP adoption metrics (97M+ downloads as of December, tracking growth)
- Pricing shifts (noted volatility: Notion AI, GitHub Copilot, Writesonic)

**Sections Likely Stable**:
- Architectural implications (MCP as integration layer, OpenAI compatibility as API lingua franca)
- Tool selection hierarchy (general patterns persist despite specific tool evolution)
- 4D Framework for AI literacy (foundational competencies)

---

# The complete frontier AI ecosystem for cognitive architects

The frontier AI landscape in December 2025 has crystallized into a sophisticated multi-vendor ecosystem where **every major lab now offers CLI-based agentic tools**, MCP has become the universal standard for AI-to-tool communication, and the line between chatbot and autonomous agent has permanently blurred. For practitioners building multi-platform cognitive architectures, the critical insight is that **no single vendor dominates across all use cases**—the winning strategy involves strategic orchestration of specialized tools rather than platform lock-in.

This survey maps the complete landscape across CLI tools, product offerings, browser integrations, system prompt configurability, recent market shifts, and the essential practitioner toolkit—providing the architectural foundation for a multi-account cognitive operating system.

---

## Research Block 1: CLI tools and development ecosystems

The three major Western labs have converged on remarkably similar agentic CLI paradigms, while Chinese labs and smaller players have released compelling alternatives with aggressive pricing.

### Anthropic's Claude Code leads the agentic CLI revolution

**Claude Code** emerged in February 2025 as the definitive terminal-based agentic coding tool. Installation is simple: `npm install -g @anthropic-ai/claude-code`. The tool reads, edits, and writes code files, executes terminal commands, manages Git workflows, and creates PRs directly. IDE extensions exist for VS Code, Cursor, Windsurf, and JetBrains.

Pricing tiers reflect heavy usage patterns: **Pro** ($20/month) provides 40-80 hours of Sonnet 4 weekly; **Max 5x** ($100/month) extends to ~140 hours; **Max 20x** ($200/month) reaches ~480 hours. Usage limits reset every 5 hours and are shared across Claude web/desktop/mobile/terminal. Free tier does **not** include Claude Code access.

**MCP (Model Context Protocol)** has become the industry standard. Anthropic donated MCP to the **Agentic AI Foundation** under Linux Foundation in December 2025, co-founded by Anthropic, Block, and OpenAI with support from Google, Microsoft, AWS, and Cloudflare. Official SDKs exist in Python, TypeScript, C#, and Java with **97M+ monthly downloads**. Over 75+ official connectors exist (Google Drive, Slack, GitHub, Jira, Postgres), with thousands of community-built servers.

### OpenAI's Codex CLI brings open-source competition

**Codex CLI** is an open-source (Rust) terminal agent installed via `npm i -g @openai/codex` or Homebrew. It supports multimodal inputs (screenshots, diagrams) and offers three approval modes: Suggest (read-only), Auto-edit (workspace access with approval), and Full-auto (unrestricted).

The tool runs on **GPT-5.2-Codex** (December 2025 release) with improved long-context handling and Windows support. Codex is included in ChatGPT Plus, Pro, Business, and Enterprise plans—no separate subscription required.

**Codex Cloud Agent** (web-based) handles tasks in isolated sandboxes, taking 1-30 minutes per task. Slack integration launched October 2025; GitHub Actions support enables CI/CD integration.

**Operator** (January 2025) evolved into **ChatGPT Agent** (July 2025), providing browser automation via the Computer-Using Agent (CUA) model. It processes raw pixels to control virtual mouse/keyboard. Pro users get 400 agent messages/month; Plus/Team receive 40 messages/month.

### Google's Gemini CLI offers the largest free tier

**Gemini CLI** (June 2025) is open-source (Apache 2.0) with a **1M token context window**—the largest free offering. Installation: run `gemini` after npm install. Built-in tools include Google Search grounding, file operations, shell commands, and web fetching.

The free tier provides **60 requests/minute and 1,000 requests/day** with a personal Google account—dramatically more generous than competitors. December 2025 added extensions for Figma, Postman, Shopify, and Stripe integration.

**Jules** is Google's asynchronous coding agent that clones codebases to secure Cloud VMs, executes tasks in parallel, and creates PRs with test results. Free tier: 15 tasks/day, 3 concurrent; **AI Pro** ($19.99/month): 100 tasks/day; **AI Ultra** ($124.99/month): 300 tasks/day with Gemini 3 Pro access.

### Other labs fill specialized niches

| Lab | CLI Tool | Key Differentiator | Free Tier |
|-----|----------|-------------------|-----------|
| **xAI** | No official CLI | OpenAI-compatible API; $0.20/$0.50 per 1M tokens (Grok 4 Fast) | Limited via X |
| **Meta** | `llama-model`, `llama stack` | Full open-source framework; unified API layer | Fully open |
| **Mistral** | `mistral-vibe` | Project-aware context; Devstral 2 currently **free** | Yes |
| **DeepSeek** | Community `deepseek-cli` | ~$0.03/M input tokens; MIT licensed | 5M tokens/30 days |
| **Qwen** | `qwen-code` | OpenAI-compatible; 256K-1M context | Open models |
| **Kimi** | `kimi-cli` (uv tool install) | Dual agent/shell mode; 256K context | API credits |

**Critical finding for architects**: All major APIs are now **OpenAI-compatible**, enabling easy provider switching. Simply change `base_url` and API key to route Claude Code, Codex, or any OpenAI SDK client to DeepSeek, Qwen, Kimi, or others.

---

## Research Block 2: Complete frontier lab product releases

### Anthropic's model lineup centers on Sonnet 4.5

**Claude Opus 4.5** (November 2025) is Anthropic's flagship—first model exceeding **80% on SWE-bench Verified**, with 1M token context and 64K output tokens. Pricing: $5/$25 per million tokens (input/output). ASL-3 safety classification.

**Claude Sonnet 4.5** (September 2025) claims "best coding model in the world" at **77.2% SWE-bench** (82% high-compute). Hybrid model supporting instant responses or extended thinking. $3/$15 per million tokens—the default in Claude Code.

**Claude Haiku 4.5** (October 2025) delivers near-frontier quality at **73.3% SWE-bench** for $1/$5 per million tokens—ideal for high-volume tasks and sub-agents.

**Key Claude.ai features** (December 2025):
- **Memory**: Project-scoped, with conversation search and recent chats tools
- **Skills** (December 18): Folders with instructions/scripts Claude loads contextually; portable across apps/API
- **Artifacts**: Dedicated window for code/documents with real-time preview
- **Claude for Chrome** (Beta December 18): Browser navigation, scheduled tasks, workflow recording
- **Claude for Excel** (Beta): Sidebar add-in with financial service connectors (S&P, Morningstar, PitchBook)

### OpenAI's product sprawl continues accelerating

**Model lineup** spans GPT-5.2 (latest flagship), GPT-4.1 series (1M context, SWE-bench leader), GPT-4o (multimodal default), and the o-series reasoning models. **o3** (April 2025) is the most powerful reasoning model; **o3-pro** (June 2025) provides extended thinking; **o4-mini** offers cost-efficient reasoning.

**ChatGPT features** include Memory (persistent preferences), Custom GPTs (no-code chatbot creation), Advanced Voice Mode (natural intonation), Vision, Canvas (collaborative editing), and Projects.

**ChatGPT Atlas** (October 2025) is OpenAI's Chromium-based AI browser with built-in sidebar, browser memories (30-day retention), and Agent Mode for Plus/Pro users. Currently macOS only; Windows/iOS/Android coming.

**Sora 2** (September 2025) generates video with synchronized audio up to 1080p/20 seconds. Disney partnership (December 2025) licensed 200+ characters. Free tier available; Pro subscribers get Sora 2 Pro.

### Google's Gemini 3 represents their strongest generation

**Gemini 3 Pro** (November 2025) outperformed GPT-5 Pro on Humanity's Last Exam (41% vs 31.64%). 1M token context; $2/$12 per million tokens. **Gemini 3 Flash** (December 2025) achieved **78% SWE-bench Verified** at 3x faster speeds.

**Gemini 3 Deep Think** (AI Ultra only) uses parallel reasoning achieving **45.1% on ARC-AGI-2**—gold-medal performance at International Mathematical Olympiad.

**Subscription tiers**:
- **Google AI Pro** ($19.99/month): Gemini 3 Pro, Deep Research, Jules, NotebookLM Plus, 2TB storage
- **Google AI Ultra** ($249.99/month): Deep Think, Veo 3, Project Mariner (10 simultaneous browser tasks), 20x Jules limits, 30TB storage, YouTube Premium included

**NotebookLM** evolved significantly with Audio Overviews (podcast-style AI discussions), Video Overviews, interactive "join the conversation" mode, infographics, and Mind Maps. NotebookLM Plus provides 5x quotas across all features.

**Media generation**: Imagen 4 with 2K resolution and excellent text rendering; Veo 3 with native audio and best-in-class realism; Lyria 2 for music with commercial licensing path.

### Chinese labs offer compelling price-performance

**DeepSeek-V3.2** delivers GPT-4o-comparable performance at **$0.028/M input tokens**—roughly 6x cheaper than Western alternatives. R1 reasoning model matches o1 on AIME/MATH benchmarks. MIT licensed, fully open-source.

**Qwen3** (April 2025) includes dense models up to 32B and MoE models reaching 235B (22B active). Supports **1M token context** and 119 languages. **Qwen3-Max** (September 2025) outperforms DeepSeek V3.1 and Claude 4 Opus.

**Kimi K2** (July 2025) is a 1T total parameter model (32B active) achieving **71.6% on SWE-bench** with native tool calling. K2 Thinking variant handles 200-300 sequential tool calls autonomously—~5x cheaper than Claude/Gemini.

### Other notable players

**Grok 4** (July 2025) features native multi-agent architecture with 256K context. Access via X Premium+ ($40/month) or SuperGrok ($30/month). Aurora generates photorealistic images with fewer restrictions than competitors.

**Meta** released Llama 4 (April 2025) with native multimodality and MoE architecture (Scout: 17B/16 experts; Maverick: 17B/128 experts). The Ray-Ban Meta Display ($799) launched September 2025 as first AI glasses with integrated display.

**Mistral Large 3** (December 2025) is a 675B parameter MoE model with 256K context. Le Chat offers Flash Answers (~1000 words/second), Deep Research preview, and Voice Mode powered by Voxtral. Free tier provides full access to core features.

**Perplexity** reached **780M queries/month** by mid-2025. Features include Spaces (custom workspaces), Focus Modes (Web, Academic, Social, Finance), Deep Research (2-4 minute comprehensive reports), and the Comet browser. Pro: $20/month; Max: $200/month with unlimited advanced models.

---

## Research Block 3: The AI browser landscape

### AI-native browsers have arrived with distinct philosophies

**ChatGPT Atlas** (OpenAI, October 2025) is Chromium-based with a built-in sidebar for any webpage. Browser Memories (opt-in, 30-day retention) remember visited site context. Agent Mode lets AI take cursor control for multi-step tasks—but cannot download files, run code, or access passwords. Currently macOS only; Plus/Pro/Business required for Agent Mode.

**Perplexity Comet** (July 2025, free October 2025) positions as "personal assistant that can take actions." Features include Comet Assistant sidebar, per-page AI history persistence, and Background Assistants for asynchronous tasks. Available on Mac/Windows/Android; iOS rolling out.

**Dia** (The Browser Company) replaced Arc after development ceased in May 2025. AI URL bar executes tasks; self-driving cursor automates shopping/booking; 7-day browsing history provides context. **Acquired by Atlassian for $610M** (October 2025). macOS only; Pro $20/month.

**Opera Neon** (September 2025) is the first fully agentic browser from a major vendor. Three agent types: Chat (questions), Do (navigation/form-filling), Make (reports/apps in cloud VM). $19.90/month subscription. Privacy-focused: all browsing actions execute locally.

**BrowserOS** is the open-source alternative (AGPL-3.0) with local AI agent execution. Supports OpenAI, Claude, Gemini via API keys or fully local via Ollama/LMStudio. Pre-installed MCP servers for Gmail, Calendar, Notion. Free and privacy-first.

### Traditional browsers gained AI capabilities rapidly

**Chrome** (September 2025) integrated Gemini for spoken conversations (Gemini Live), multi-tab analysis, natural language history search, and YouTube summaries. Agentic browsing (multi-step tasks) announced but not yet released.

**Edge Copilot Mode** (July 2025) replaced the classic new tab page with unified chat/search. Multi-tab reasoning, natural language history search, and Agent Mode (private preview) automates workflows on IT-approved sites. Requires Microsoft 365 Copilot license for advanced features.

**Brave Leo** maintains the strongest privacy model—no conversation storage, anonymous submissions via reverse proxy, NEAR.AI TEE integration (November 2025) for cryptographically verifiable privacy. AI Browsing (agentic) testing in Nightly builds. Leo Premium: $14.99/month.

**Firefox** announced AI Window (November 2025) as an opt-in interface with user-chosen providers. New CEO confirmed Firefox will evolve into "modern AI browser" with a complete **AI Kill Switch** coming Q1 2026.

**Safari** relies on Apple Intelligence with on-device Ajax LLM for Reader View summaries and Highlights. Apple is "actively looking at" adding AI search engines (OpenAI, Perplexity, Anthropic) as options. Safari searches declined for first time in April 2025.

**Arc** is effectively abandoned—maintenance mode only, will not be open-sourced.

| Browser | Agentic | Memory | Privacy | Price | Platforms |
|---------|---------|--------|---------|-------|-----------|
| ChatGPT Atlas | Yes (Preview) | 30-day cloud | Opt-in training | Free/Plus+ | macOS |
| Perplexity Comet | Yes | Page-specific | Some concerns | Free/Max | Mac/Win/Android/iOS |
| Dia | Yes | 7-day history | User-controlled | Free/Pro $20 | macOS |
| Opera Neon | Full | Task-isolated | Local-first | $19.90/mo | Mac/Win |
| BrowserOS | Yes | Local only | Best (OSS) | Free | Mac/Win/Linux |
| Chrome | Coming | User-controlled | Google | Free | All |
| Edge | Enterprise | MS Graph | Enterprise | Free/M365 | All |
| Brave | Testing | Local | Best | Free/Premium $15 | All |

---

## Research Block 4: System prompt configurability audit

Custom instruction capabilities vary dramatically across platforms, with significant implications for cognitive architecture design.

### Claude offers the most robust project-based customization

**Projects** (Pro/Team/Enterprise only) provide 200K token context windows per project with document/code uploads forming knowledge bases. Custom instructions control behavior per project. No cross-project memory sharing. The API supports full `system` role that cannot be overridden by users. 1M token beta available for Sonnet 4/4.5.

### ChatGPT provides the widest free-tier configurability

**Custom Instructions** accessible to all tiers including free. Two text fields ("What would you like ChatGPT to know?" and "How would you like ChatGPT to respond?") with **1,500 characters per field** (3,000 total). Memory and Custom Instructions work together but separately. GPT Builder (Plus+) enables full system prompt control per custom GPT.

### Gemini restricts Gems to paid tiers

**Gems** custom AI experts available only to Gemini Advanced/Business/Enterprise. No explicit character limit; instruction length is flexible. Can upload files for additional context. Google AI Studio provides full `systemInstruction` parameter in API.

### Other platforms show mixed support

| Platform | UI Custom Instructions | API System Prompt | Key Limitations |
|----------|----------------------|-------------------|-----------------|
| **Grok** | Limited (prompt engineering) | Full support | Public system prompts on GitHub |
| **Perplexity** | Spaces with instructions | Full support | Search component **ignores** system prompt |
| **DeepSeek** | None | Full support | API-only customization |
| **Qwen** | Limited | Full support (DashScope) | Enhanced system prompt training |
| **Kimi** | Session preferences | Full support | OpenAI/Anthropic compatible |
| **Mistral Le Chat** | None | Full support (newer models) | Older models need workarounds |
| **Meta AI** | Memory feature | Via Llama API | No opt-out for personalization |

**Critical finding**: Perplexity's search component operates independently—system prompts control style/tone but not search queries. This matters for research-focused workflows.

---

## Research Block 5: AI tools cartography (November-December 2025)

### Major acquisitions reshaped the landscape

**Windsurf** experienced dramatic turmoil: OpenAI's **$3B acquisition collapsed** in July 2025 when Microsoft blocked due to IP concerns. Google DeepMind secured a $2.4B licensing deal plus hired CEO and co-founder. **Cognition** (Devin AI) then acquired the remaining product, brand, and team. Windsurf had reached ~$100M ARR.

**Dia (The Browser Company)** was acquired by Atlassian for **$610M** after Arc development ceased.

**Runway rejected Meta's acquisition bid** and released Gen-4.5, now #1 on Video Arena benchmark.

### Pricing shifts favor bundled AI

**Notion AI** now requires Business tier ($20/user/month)—free/Plus users lost AI access. **GitHub Copilot Pro+** launched at $39/month with model choice (Claude, Gemini, GPT). **Microsoft 365 Copilot Business** introduced at $21/user/month (down from $30 Enterprise).

**Writesonic** increased from $16 to $39/month. **ElevenLabs** secured Meta partnership for Instagram/WhatsApp integration.

### MCP adoption accelerated dramatically

**Google launched managed MCP servers** (December 10) for Maps, BigQuery, Compute Engine, and Kubernetes. **Zapier MCP** connects AI tools to 8,000 apps and 30,000+ actions. Security startup **Runlayer** raised $11M with 8 unicorn customers (Gusto, dbt Labs, Instacart).

MCP security concerns emerged: GitHub prompt injection and Asana data exposure vulnerabilities (fixed June 2025). Cloudflare, Docker, and Wiz releasing MCP security products.

### Coding tools reached plateau maturity

**Cursor 2.0** (October 2025) added parallel agents (up to 8) and native browser testing. **GitHub Copilot** shifted default model to GPT-4.1; coding agent became GA in September.

~85% of developers now use at least one AI coding tool. **Claude Code** gaining traction for complex refactoring workflows.

### Video generation competition intensified

**Runway Gen-4.5** (December 2025) now leads Video Arena benchmark. **Chinese labs** released open-source alternatives: ByteDance Vidi2 (12B parameters) and Tencent HunyuanVideo-1.5 (8.3B, optimized for 14GB VRAM).

**ElevenLabs** launched Eleven Music (August 2025)—first AI music generator cleared for commercial use via Merlin Network and Kobalt partnerships. Series C: $180M at $3.3B valuation.

---

## Research Block 6: The modern practitioner's essential arsenal

### The essential platform hierarchy has crystallized

**Tier S (Must Master)**:
- **ChatGPT**: Most versatile, 69% adoption rate, 400M weekly active users
- **Claude**: Best for long-form writing and coding, largest context windows
- **Perplexity**: Dominant for research with citations, 780M queries/month

**Tier A (Role-Dependent)**:
- GitHub Copilot (developers)
- Midjourney/DALL-E (visual creation)
- Notion AI (knowledge organization)
- Google Gemini (Google ecosystem users)

### Minimum viable stacks for different budgets

**$0 Stack** (covers ~80-85% of needs):
- ChatGPT free + Claude free + Perplexity free

**$20/month Sophisticated User**:
- ChatGPT Plus OR (Claude Pro + Perplexity Pro together for $40)

**$60/month Power User**:
- ChatGPT Plus ($20) + Claude Pro ($20) + Perplexity Pro ($20)

**Developer Addition**:
- GitHub Copilot ($10-19/month) for "40% productivity boost"

### Baseline AI fluency now means four competencies

The **4D Framework** (Anthropic) defines modern AI literacy:
1. **Delegation** — Knowing what tasks to assign to AI
2. **Description** — Communicating effectively (prompting)
3. **Discernment** — Evaluating outputs critically
4. **Diligence** — Maintaining ethics and continuous improvement

Per 2025 ETS Human Progress Report: **82% of HR leaders now prioritize AI literacy**. LinkedIn data shows 34% surge in job listings requiring explicit AI tool experience—"AI literacy is now rated alongside foundational skills such as Excel or PowerPoint."

### Tool selection follows a clear hierarchy

| Task | Best Tool | Why |
|------|-----------|-----|
| General writing | ChatGPT | Most versatile for short-medium |
| Long-form analysis | Claude | Largest context, natural prose |
| Research with sources | Perplexity | Real-time web, auto-citations |
| Coding | Claude or Copilot | Claude for explanation, Copilot inline |
| Image generation | Midjourney or DALL-E | DALL-E simplicity, Midjourney artistry |

**Expert consensus**: "There is no absolute winner in the AI battle of 2025. The best strategy is a hybrid approach where you use each tool for its strengths."

---

## Architectural implications for multi-platform cognitive systems

For practitioners building cognitive architectures, this survey reveals several structural truths:

**MCP is the integration layer**. With Anthropic, OpenAI, Google, and Block all backing MCP under Linux Foundation governance, building MCP-compatible tools ensures future interoperability. The 97M+ monthly SDK downloads indicate critical mass.

**OpenAI compatibility is the API lingua franca**. DeepSeek, Qwen, Kimi, Mistral, and xAI all support OpenAI-compatible endpoints. A cognitive architecture can route requests to any provider by changing `base_url`—enabling cost optimization, capability matching, and redundancy.

**System prompts require per-platform adaptation**. Perplexity ignores system prompts for search; Mistral older models need workarounds; Meta AI has no opt-out for personalization. Architecture must accommodate these constraints.

**Browser agents remain early-stage**. ChatGPT Atlas, Comet, Dia, and Opera Neon represent first-generation browser agents. Reliability varies significantly; human-in-the-loop design remains necessary for production workflows.

**Chinese labs offer the best price-performance**. DeepSeek at $0.03/M input and Kimi at 5x lower cost than Western alternatives make them compelling for high-volume batch processing—provided data sovereignty permits.

**The cognitive OS stack for late 2025**: Claude for deep work and coding, ChatGPT for versatility and agents, Perplexity for research, a CLI tool (Claude Code or Gemini CLI) for terminal workflows, and an AI browser (Comet or BrowserOS) for web automation—all connected via MCP servers to personal knowledge bases.

---

**END AI ECOSYSTEM SURVEY**
