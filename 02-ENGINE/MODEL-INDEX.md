# MODEL INDEX
## Frontier AI Model Registry

**Document Type**: OPERATIONAL (Living Document)
**Last Updated**: 2026-02-01
**Refresh Cycle**: As models release
**Purpose**: Track frontier model capabilities for IIC constellation routing

---

## FIDS — Fleet Status Board

| Platform | Status | Flagship | Latest Release | Delta |
|----------|--------|----------|----------------|-------|
| Anthropic | NOMINAL | Claude 4.5 Opus | 2025-11-01 | — |
| OpenAI | NOMINAL | GPT-5.2 | 2025-09-15 | — |
| Google | NOMINAL | Gemini 3 Pro | 2025-10-01 | — |
| xAI | NOMINAL | Grok 4 | 2025-12-01 | — |
| DeepSeek | WATCH | V3.2 | 2025-11-15 | V4 rumored |

Status: `NOMINAL` (stable) · `WATCH` (change expected) · `UPDATING` (active transition) · `DEGRADED` (regression) · `NEW` (just released)

**Last verified**: 2026-02-02 · **Ticker**: `DYN-TICKER_FEED.md`

---

## CONSTELLATION ECONOMICS

| Account | Platform | Tier | Monthly | Avatars |
|---------|----------|------|---------|---------|
| A1 | Claude | Max 5x | $100 | Commander |
| A1 | ChatGPT | Plus | $20 | Vanguard |
| A2 | Claude | Pro | $20 | Vizier, Adjudicator |
| A2 | Google AI | Pro | $20 | Cartographer, Diviner |
| — | — | **Total** | **$160** | — |

**Last verified**: 2026-02-02 · **DEF**: `PlatformBudget` in `DEF-CONSTELLATION_VARIABLES.md`

---

## ACTIVE PRODUCTION MODELS (2026-01)

### Anthropic (Claude)

| Model | API String | Context | Strengths | IIC Assignment |
|-------|------------|---------|-----------|----------------|
| **Claude 4.5 Opus** | `claude-opus-4-5-20251101` | 200K | Deep synthesis, architectural thinking, extended thinking | Oracle sessions, strategic synthesis |
| **Claude 4.5 Sonnet** | `claude-sonnet-4-5-20251101` | 200K | Fast, balanced, excellent coding | Daily operations, code generation |
| **Claude 4.5 Haiku** | `claude-haiku-4-5-20251101` | 200K | Speed, efficiency, sub-tasks | Batch processing, triage |

**Notes**:
- Extended thinking available on Opus/Sonnet for complex analysis
- Sonnet is default for Claude Code CLI
- All support 1M token beta context

### OpenAI (ChatGPT)

| Model | API String | Context | Strengths | IIC Assignment |
|-------|------------|---------|-----------|----------------|
| **GPT-5.2** | `gpt-5-turbo` | 128K | Versatile, broad knowledge | General synthesis, creative |
| **GPT-4.1** | `gpt-4-turbo` | 1M | Long context, SWE-bench leader | Code analysis, large documents |
| **o3** | `o3` | 128K | Deep reasoning, chain-of-thought | Complex problem solving |
| **o3-pro** | `o3-pro` | 128K | Extended reasoning | Mathematical proofs, research |

**Notes**:
- Memory feature for conversation continuity
- Projects feature for context isolation
- Atlas browser for real-time web access

### Google (Gemini)

| Model | API String | Context | Strengths | IIC Assignment |
|-------|------------|---------|-----------|----------------|
| **Gemini 3 Pro** | `gemini-3-pro` | 1M | Multimodal, research synthesis | Deep Research, comprehensive analysis |
| **Gemini 3 Flash** | `gemini-3-flash` | 1M | Speed, efficiency | Rapid triage, summarization |
| **Gemini 3 Deep Think** | `gemini-3-deep-think` | 1M | Advanced reasoning | Mathematical, scientific analysis |

**Notes**:
- 1M context window largest free offering
- NotebookLM integration for Audio/Video Overviews
- Deep Think requires AI Ultra subscription

### xAI (Grok)

| Model | API String | Context | Strengths | IIC Assignment |
|-------|------------|---------|-----------|----------------|
| **Grok 4** | `grok-4` | 256K | Real-time X/Twitter data, cultural fluency | Current discourse, trend analysis |
| **Grok 4 Fast** | `grok-4-fast` | 256K | Speed, efficiency | Rapid queries |

**Notes**:
- Native multi-agent architecture
- Aurora image generation with fewer restrictions
- X Premium+ required for full access

### Chinese Labs (Reference)

| Model | Lab | Context | Strengths | Use Case |
|-------|-----|---------|-----------|----------|
| **DeepSeek-V3.2** | DeepSeek | 128K | Cost-efficient ($0.03/M) | Batch processing |
| **Qwen3-Max** | Alibaba | 1M | Multilingual, long context | Translation, analysis |
| **Kimi K2** | Moonshot | 256K | Sequential tool calling | Agentic workflows |

---

## MODEL SELECTION MATRIX

### By Task Type

| Task | Primary | Fallback | Rationale |
|------|---------|----------|-----------|
| **Strategic Synthesis** | Claude 4.5 Opus | GPT-5.2 | Deep architectural thinking |
| **Daily Operations** | Claude 4.5 Sonnet | Gemini 3 Flash | Balance of speed/quality |
| **Code Generation** | Claude 4.5 Sonnet | GPT-4.1 | SWE-bench performance |
| **Long Document Analysis** | Gemini 3 Pro | GPT-4.1 | 1M context |
| **Real-time Discourse** | Grok 4 | ChatGPT + Atlas | X/Twitter integration |
| **Mathematical Reasoning** | o3-pro | Gemini Deep Think | Formal verification |
| **Batch Processing** | DeepSeek-V3.2 | Claude Haiku | Cost optimization |
| **Research Synthesis** | Gemini 3 Pro + Deep Research | Claude Opus | Comprehensive coverage |

### By IIC Chain

| Chain | Primary Model | Rationale |
|-------|---------------|-----------|
| **Acumen** (Sensing) | Grok 4 | Real-time awareness |
| **Coherence** (Synthesis) | Claude 4.5 Opus | Deep integration |
| **Efficacy** (Execution) | Claude 4.5 Sonnet | Code + speed |
| **Mastery** (Teaching) | GPT-5.2 | Explanation clarity |
| **Transcendence** (Wisdom) | Claude 4.5 Opus | Philosophical depth |

---

## CAPABILITY TRACKING

### Context Windows (Effective)

| Model | Stated | Effective | Notes |
|-------|--------|-----------|-------|
| Claude 4.5 (all) | 200K | 200K | 1M beta available |
| GPT-4.1 | 1M | ~500K | Quality degrades beyond |
| Gemini 3 Pro | 1M | 1M | Full utilization |
| Grok 4 | 256K | 256K | Consistent |

### Tool Use

| Model | Native Tools | MCP Support | Agentic |
|-------|--------------|-------------|---------|
| Claude 4.5 | Yes | Yes (native) | Yes |
| GPT-5.2 | Yes | Via plugin | Yes |
| Gemini 3 | Yes | Yes | Yes |
| Grok 4 | Yes | Via API | Yes |

### Vision

| Model | Image Input | Video Input | Generation |
|-------|-------------|-------------|------------|
| Claude 4.5 | Yes | No | No |
| GPT-5.2 | Yes | Yes | DALL-E integration |
| Gemini 3 | Yes | Yes | Imagen/Veo |
| Grok 4 | Yes | No | Aurora |

---

## PRICING REFERENCE (2026-01)

### Subscription Tiers

| Platform | Tier | Monthly | Key Features |
|----------|------|---------|--------------|
| **Claude** | Pro | $20 | Sonnet unlimited, Opus access |
| **Claude** | Max 5x | $100 | Extended limits |
| **ChatGPT** | Plus | $20 | GPT-5, o3 access |
| **ChatGPT** | Pro | $200 | Unlimited o3-pro |
| **Gemini** | AI Pro | $20 | Gemini 3 Pro, Deep Research |
| **Gemini** | AI Ultra | $250 | Deep Think, Veo 3 |
| **Grok** | SuperGrok | $30 | Full Grok 4 |
| **Grok** | Premium+ | $40 | Via X subscription |

### API Pricing (per 1M tokens)

| Model | Input | Output |
|-------|-------|--------|
| Claude 4.5 Opus | $5 | $25 |
| Claude 4.5 Sonnet | $3 | $15 |
| Claude 4.5 Haiku | $1 | $5 |
| GPT-5.2 | $5 | $15 |
| GPT-4.1 | $2 | $8 |
| Gemini 3 Pro | $2 | $12 |
| DeepSeek-V3.2 | $0.03 | $0.15 |

---

## PROFILE STUBS

Profile YAML stubs deleted (2026-02-01 audit). Model registry tables above serve operational needs. Detailed profiles deferred until PROJ-003 (Tooling Stack) finalizes platform selection — regenerate from this index when needed.

---

## REFRESH NOTES

**2026-02-02**: Live CANON Ticker MVP — FIDS board, economics table, DYN-TICKER_FEED.md linked
**2026-02-01**: Refresh — profile stubs deferred, timestamp updated
**2026-01-02**: Initial index created from DIRECTIVE-036 Phase F

---

*Index maintained as living document | Refresh on model releases*
