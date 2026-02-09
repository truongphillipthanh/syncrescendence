# MODEL INDEX
## Frontier AI Model Registry

**Document Type**: OPERATIONAL (Living Document)
**Last Updated**: 2026-02-09
**Last Verified**: 2026-02-09
**Refresh Cycle**: As models release
**Purpose**: Track frontier model capabilities for IIC constellation routing

---

## FIDS — Fleet Status Board

| Platform | Status | Flagship | Latest Release | Delta |
|----------|--------|----------|----------------|-------|
| Anthropic | UPDATING | Claude Opus 4.6 | 2026-02-05 | Opus 4.6 just launched |
| OpenAI | NOMINAL | GPT-5.2 | 2025-12-11 | GPT-5.2 Pro variant active |
| Google | NOMINAL | Gemini 3 Pro (Preview) | 2025-11-18 | GA pending |
| xAI | WATCH | Grok 4.1 | 2025-11-17 | Grok 5 training (Q1 2026) |
| Meta | NOMINAL | Llama 4 Maverick | 2025-04-05 | Behemoth still training |
| Mistral | NOMINAL | Mistral Large 3 | 2025-12-04 | Devstral 2 for coding |
| DeepSeek | WATCH | V3.2 | 2025-09-29 | V4 imminent (~Feb 17) |
| Alibaba | NOMINAL | Qwen3-Max | 2025-09-23 | Qwen3-Next released |

Status: `NOMINAL` (stable) · `WATCH` (change expected) · `UPDATING` (active transition) · `DEGRADED` (regression) · `NEW` (just released)

**Last verified**: 2026-02-09 · **Ticker**: `DYN-TICKER_FEED.md`

---

## CONSTELLATION ECONOMICS

| Account | Platform | Tier | Monthly | Avatars |
|---------|----------|------|---------|---------|
| A1 | Claude | Max 5x | $100 | Commander |
| A1 | ChatGPT | Plus | $20 | Vanguard |
| A2 | Claude | Pro | $20 | Vizier, Adjudicator |
| A2 | Google AI | Pro | $20 | Cartographer, Diviner |
| — | — | **Total** | **$160** | — |

**Last verified**: 2026-02-09 · **DEF**: `PlatformBudget` in `DEF-CONSTELLATION_VARIABLES.md`

---

## ACTIVE PRODUCTION MODELS (2026-02)

### Anthropic (Claude)

| Model | API String | Context | Max Output | Release | Strengths | IIC Assignment |
|-------|------------|---------|------------|---------|-----------|----------------|
| **Claude Opus 4.6** | `claude-opus-4-6-20260205` | 200K (1M beta) | 128K | 2026-02-05 | Adaptive thinking, agent teams, highest agentic coding scores, 1M context beta | Oracle sessions, strategic synthesis, agent orchestration |
| **Claude Opus 4.5** | `claude-opus-4-5-20251101` | 200K (1M beta) | 128K | 2025-11-01 | Deep synthesis, architectural thinking, extended thinking | Deep analysis, complex reasoning |
| **Claude Sonnet 4.5** | `claude-sonnet-4-5-20241022` | 200K (1M beta) | 128K | 2024-10-22 | Fast, balanced, excellent coding | Daily operations, code generation |
| **Claude Haiku 4.5** | `claude-haiku-4-5-20241022` | 200K | 128K | 2024-10-22 | Speed, efficiency, sub-tasks | Batch processing, triage |

**Notes**:
- Opus 4.6 is the NEW flagship — released 2026-02-05 with agent teams and adaptive thinking
- Extended thinking available on Opus 4.6/4.5 and Sonnet 4.5 for complex analysis
- 1M token context window beta available on Opus 4.6, Sonnet 4.5, and Sonnet 4 (usage tier 4+)
- Sonnet 4.5 is default for Claude Code CLI; Opus 4.6 available via model override
- Fast mode on Opus 4.6 (research preview): 6x pricing for significantly faster output

### OpenAI (ChatGPT)

| Model | API String | Context | Max Output | Release | Strengths | IIC Assignment |
|-------|------------|---------|------------|---------|-----------|----------------|
| **GPT-5.2** | `gpt-5.2` | 400K | 128K | 2025-12-11 | Agentic coding, long context, vision, tool-calling | General synthesis, creative, agentic workflows |
| **GPT-5.2 Pro** | `gpt-5.2-pro` | 400K | 128K | 2025-12-11 | Extended reasoning, highest capability | Complex research, enterprise analysis |
| **GPT-4.1** | `gpt-4.1` | 1M | 128K | 2025-04-14 | Long context, SWE-bench leader, cost-efficient | Code analysis, large documents |
| **GPT-4.1 Mini** | `gpt-4.1-mini` | 1M | 128K | 2025-04-14 | Budget-friendly, good quality | Batch tasks, light workloads |
| **o3** | `o3` | 200K | — | 2025-04-16 | Deep reasoning, chain-of-thought, agentic tools | Complex problem solving |
| **o3-pro** | `o3-pro` | 200K | — | 2025-06-10 | Most reliable extended reasoning | Mathematical proofs, research |
| **o4-mini** | `o4-mini` | 200K | — | 2025-04-16 | Cost-efficient reasoning, math/coding/visual | Budget reasoning tasks |

**Notes**:
- GPT-5.2 released Dec 2025 with 3 modes: Instant, Thinking, Pro
- o-series reasoning tokens billed as output tokens (invisible via API, inflate actual cost)
- Memory feature for conversation continuity
- Projects feature for context isolation

### Google (Gemini)

| Model | API String | Context | Max Output | Release | Strengths | IIC Assignment |
|-------|------------|---------|------------|---------|-----------|----------------|
| **Gemini 3 Pro** (Preview) | `gemini-3-pro-preview` | 1M | 64K | 2025-11-18 | Multimodal, research synthesis, 80%+ better reasoning | Deep Research, comprehensive analysis |
| **Gemini 3 Flash** (Preview) | `gemini-3-flash-preview` | 1M | 64K | 2025-11-18 | Speed, efficiency, multimodal | Rapid triage, summarization |
| **Gemini 2.5 Pro** | `gemini-2.5-pro` | 1M | 64K | 2025-03-25 | Strong reasoning, excellent value | Stable production workloads |
| **Gemini 2.5 Flash** | `gemini-2.5-flash` | 1M | 64K | 2025-05-20 | Fast thinking, lightweight | Cost-efficient reasoning |

**Notes**:
- Gemini 3 models still in "Preview" — GA pending
- 1M context window across all current models — largest free offering
- NotebookLM integration for Audio/Video Overviews
- Deep Think requires AI Ultra subscription ($125/3mo)
- Gemini 2.5 Pro remains excellent value at $1.25/$10 per MTok

### xAI (Grok)

| Model | API String | Context | Max Output | Release | Strengths | IIC Assignment |
|-------|------------|---------|------------|---------|-----------|----------------|
| **Grok 4** | `grok-4` | 256K | — | 2025-07-09 | Deep reasoning, X/Twitter data | Strategic reasoning, trend analysis |
| **Grok 4.1** | `grok-4.1` | 2M | — | 2025-11-17 | 2M context, 3x lower hallucination, tool-calling | Long-context analysis, agentic tasks |
| **Grok 4.1 Fast** | `grok-4.1-fast` | 2M | — | 2025-11-17 | Speed, best tool-calling, ultra-cheap | Rapid queries, agentic workflows |

**Notes**:
- Grok 4.1 has 2M token context window — largest among commercial APIs
- Grok 5 in training with 6T parameters — expected Q1 2026
- Native multi-agent architecture, Aurora image generation
- X Premium+ ($40/mo) or SuperGrok ($30/mo) required for full consumer access

### Meta (Llama) — Open Source

| Model | Parameters | Context | Release | Strengths | Use Case |
|-------|------------|---------|---------|-----------|----------|
| **Llama 4 Scout** | 17B active / 109B total (16 experts) | 10M | 2025-04-05 | Industry-leading 10M context, multimodal | Massive context tasks, self-hosted |
| **Llama 4 Maverick** | 17B active / 400B total (128 experts) | 1M | 2025-04-05 | Best multimodal in class, beats GPT-4o | Production inference, self-hosted |
| **Llama 4 Behemoth** | 288B active / 2T total (16 experts) | TBD | Training | Outperforms GPT-4.5/Sonnet 3.7 on STEM | Research (unreleased) |

**Notes**:
- Apache 2.0 license — free for commercial use
- Natively multimodal (text + image input, text output), 12 languages
- No API pricing — self-hosted or via cloud providers (AWS, Azure, GCP, Together, etc.)
- Behemoth still training as of Feb 2026

### Mistral

| Model | API String | Parameters | Context | Release | Strengths | Use Case |
|-------|------------|------------|---------|---------|-----------|----------|
| **Mistral Large 3** | `mistral-large-latest` | 41B active / 675B total (MoE) | 256K | 2025-12-04 | Most capable Mistral, strong reasoning | Production reasoning |
| **Mistral Medium 3** | `mistral-medium-latest` | Dense | 131K | 2025-05-08 | Balanced performance/cost | General workloads |
| **Devstral 2** | `devstral-2` | 123B (dense) | 256K | 2026-01-29 | Coding-focused, 256K context | Code generation, review |

**Notes**:
- Open-weight models (Apache 2.0) available alongside API
- Devstral 2 currently free via Mistral API
- Mistral Small 3 available in 3B/8B/14B dense variants
- Strong European AI ecosystem play

### Chinese Labs (Reference)

| Model | Lab | Parameters | Context | Release | Strengths | Use Case |
|-------|-----|------------|---------|---------|-----------|----------|
| **DeepSeek-V3.2** | DeepSeek | MoE | 128K | 2025-09-29 | Ultra cost-efficient, reasoning + chat | Batch processing, cost optimization |
| **DeepSeek-V4** | DeepSeek | Hybrid MoE | 1M+ | ~2026-02-17 (EXPECTED) | Engram memory, 1M+ context, hybrid reasoning/chat | STALE — not yet released |
| **Qwen3-Max** | Alibaba | MoE (235B/22B active) | 128K | 2025-09-23 | Multilingual (119 langs), hybrid thinking | Translation, analysis |
| **Qwen3-Next** | Alibaba | MoE | 128K | 2025-09-10 | Improved reasoning, multi-token prediction | Research, fast inference |
| **Kimi K2** | Moonshot | — | 256K | 2025-07-01 | Sequential tool calling | Agentic workflows |

**Notes**:
- DeepSeek V4 targets mid-Feb 2026 release — will unify V3.x and R1 into single hybrid model
- DeepSeek V3.2 pricing is the cheapest frontier model: $0.28 input / $0.42 output per MTok (cache hits: $0.028)
- Qwen3 models available open-source (Apache 2.0) on HuggingFace
- Qwen3 has both dense (0.6B-32B) and sparse (30B/235B MoE) variants

---

## MODEL SELECTION MATRIX

### By Task Type

| Task | Primary | Fallback | Rationale |
|------|---------|----------|-----------|
| **Strategic Synthesis** | Claude Opus 4.6 | GPT-5.2 Pro | Adaptive thinking, agent teams |
| **Daily Operations** | Claude Sonnet 4.5 | Gemini 3 Flash | Balance of speed/quality |
| **Code Generation** | Claude Opus 4.6 | GPT-4.1 | Highest agentic coding scores |
| **Long Document Analysis** | Gemini 3 Pro | Grok 4.1 (2M) | 1M-2M context |
| **Real-time Discourse** | Grok 4.1 | ChatGPT + browsing | X/Twitter integration |
| **Mathematical Reasoning** | o3-pro | Gemini 2.5 Pro | Formal verification |
| **Batch Processing** | DeepSeek-V3.2 | Claude Haiku 4.5 | Cost optimization |
| **Research Synthesis** | Gemini 3 Pro + Deep Research | Claude Opus 4.6 | Comprehensive coverage |
| **Massive Context** | Llama 4 Scout (10M) | Grok 4.1 (2M) | Self-hosted vs API |

### By IIC Chain

| Chain | Primary Model | Rationale |
|-------|---------------|-----------|
| **Acumen** (Sensing) | Grok 4.1 | Real-time awareness, 2M context |
| **Coherence** (Synthesis) | Claude Opus 4.6 | Adaptive thinking, agent teams |
| **Efficacy** (Execution) | Claude Sonnet 4.5 | Code + speed |
| **Mastery** (Teaching) | GPT-5.2 | Explanation clarity |
| **Transcendence** (Wisdom) | Claude Opus 4.6 | Philosophical depth, deep reasoning |

---

## CAPABILITY TRACKING

### Context Windows (Effective)

| Model | Stated | Effective | Notes |
|-------|--------|-----------|-------|
| Llama 4 Scout | 10M | 10M | Open-source, self-hosted |
| Grok 4.1 / 4.1 Fast | 2M | 2M | Largest commercial API context |
| Gemini 3 Pro | 1M | 1M | Full utilization |
| Gemini 2.5 Pro | 1M | 1M | Full utilization |
| GPT-4.1 | 1M | ~500K | Quality degrades beyond |
| Llama 4 Maverick | 1M | 1M | Open-source, self-hosted |
| Claude Opus 4.6 | 200K (1M beta) | 200K (1M beta) | 1M beta tier-4+ only |
| GPT-5.2 | 400K | 400K | 128K max output |
| Grok 4 | 256K | 256K | Consistent |
| Mistral Large 3 | 256K | 256K | Consistent |
| o3 / o4-mini | 200K | 200K | Reasoning tokens consume context |

### Tool Use

| Model | Native Tools | MCP Support | Agentic |
|-------|--------------|-------------|---------|
| Claude Opus 4.6 | Yes | Yes (native) | Yes (agent teams) |
| Claude Sonnet 4.5 | Yes | Yes (native) | Yes |
| GPT-5.2 | Yes | Via plugin | Yes |
| o3 / o4-mini | Yes | Via plugin | Yes (first o-series with tools) |
| Gemini 3 | Yes | Yes | Yes |
| Grok 4.1 | Yes | Via API | Yes (best tool-calling) |

### Vision

| Model | Image Input | Video Input | Generation |
|-------|-------------|-------------|------------|
| Claude Opus 4.6 | Yes | No | No |
| GPT-5.2 | Yes | Yes | DALL-E integration |
| Gemini 3 | Yes | Yes | Imagen/Veo |
| Grok 4.1 | Yes | No | Aurora |
| Llama 4 | Yes | No | No |

---

## PRICING REFERENCE (2026-02)

### Subscription Tiers

| Platform | Tier | Monthly | Key Features |
|----------|------|---------|--------------|
| **Claude** | Pro | $20 | Sonnet unlimited, Opus access |
| **Claude** | Max 5x | $100 | Extended limits, Opus 4.6 |
| **ChatGPT** | Plus | $20 | GPT-5.2, o3 access |
| **ChatGPT** | Pro | $200 | Unlimited o3-pro, GPT-5.2 Pro |
| **Gemini** | AI Pro | $20 | Gemini 3 Pro, Deep Research |
| **Gemini** | AI Ultra | $125/3mo | Deep Think, Veo 3.1, Gemini Ultra-tier |
| **Grok** | SuperGrok | $30 | Full Grok 4/4.1, 128K memory |
| **Grok** | Premium+ (X) | $40 | Via X subscription, Grok 4/4.1 |

### API Pricing (per 1M tokens)

| Model | Input | Output | Notes |
|-------|-------|--------|-------|
| **Claude Opus 4.6** | $5 | $25 | Long ctx (>200K): $10/$37.50. Fast mode: $30/$150 |
| **Claude Opus 4.5** | $5 | $25 | Long ctx (>200K): $10/$37.50 |
| **Claude Sonnet 4.5** | $3 | $15 | Long ctx (>200K): $6/$22.50 |
| **Claude Haiku 4.5** | $1 | $5 | — |
| **GPT-5.2** | $1.75 | $14 | — |
| **GPT-5.2 Pro** | $21 | $168 | Premium reasoning |
| **GPT-4.1** | $2 | $8 | Best value long-context |
| **GPT-4.1 Mini** | $0.40 | $1.60 | Budget option |
| **o3** | $2 | $8 | + reasoning tokens as output |
| **o3-pro** | $20 | $80 | + reasoning tokens as output |
| **o4-mini** | $1.10 | $4.40 | + reasoning tokens as output |
| **Gemini 3 Pro** (Preview) | $2 | $12 | Long ctx (>200K): $4/$18 |
| **Gemini 3 Flash** (Preview) | $0.50 | $3 | Audio input: $1/MTok |
| **Gemini 2.5 Pro** | $1.25 | $10 | Long ctx (>200K): $2.50/$15 |
| **Gemini 2.5 Flash** | $0.30 | $2.50 | Audio input: $1/MTok |
| **Grok 4** | $3 | $15 | Cached: $0.75 input |
| **Grok 4.1 Fast** | $0.20 | $0.50 | Cached: $0.05 input |
| **Mistral Large 3** | $0.50 | $1.50 | Open-weight MoE |
| **Mistral Medium 3** | $0.40 | $2 | — |
| **Devstral 2** | Free | Free | Coding-focused, currently free |
| **DeepSeek-V3.2** | $0.28 | $0.42 | Cache hits: $0.028 input |
| **Qwen3-Max** | $1.20 | $6 | — |

---

## PROFILE STUBS

Profile YAML stubs deleted (2026-02-01 audit). Model registry tables above serve operational needs. Detailed profiles deferred until PROJ-003 (Tooling Stack) finalizes platform selection — regenerate from this index when needed.

---

## REFRESH NOTES

**2026-02-09**: Major refresh — Claude Opus 4.6 (released 2026-02-05), verified all pricing from official sources. Added Llama 4, Mistral, expanded xAI (Grok 4.1 with 2M context). Updated OpenAI pricing from official API docs. DeepSeek V4 flagged as imminent. Gemini 3 still in Preview.
**2026-02-02**: Live CANON Ticker MVP — FIDS board, economics table, DYN-TICKER_FEED.md linked
**2026-02-01**: Refresh — profile stubs deferred, timestamp updated
**2026-01-02**: Initial index created from DIRECTIVE-036 Phase F

---

*Index maintained as living document | Refresh on model releases*
