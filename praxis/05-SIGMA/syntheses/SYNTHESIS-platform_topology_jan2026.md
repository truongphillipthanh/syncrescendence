# Platform Topology: Durable Technical Specs (January 2026)

**Type:** Synthesis (extracted from competitive analysis)
**Date:** 2026-01-10 (research), 2026-02-22 (distilled)
**Status:** Snapshot — review quarterly for staleness

---

## Tokenization Physics

| Platform | Video Rate | Audio Rate | Notes |
|----------|-----------|-----------|-------|
| Gemini 3 | 263 tokens/sec (variable sequence length) | 32 tokens/sec | Native multimodal — NOT frame sampling |
| Gemini 3 LOW res | 70 tokens/frame | — | Scene gist, action recognition |
| Gemini 3 HIGH res | 280 tokens/frame | — | OCR on video frames, small object ID |

**Implication**: 1hr video @ 263 tok/s ≈ 946,800 tokens — nearly fills 1M context window.

## Context Windows (API vs Reality)

| Platform | API Limit | Web UI Effective | Throughput |
|----------|-----------|-----------------|------------|
| Grok 4.1 Fast | **2M tokens** | Unknown | 4M tokens/min |
| Gemini 3 | 1M tokens | ~32-64K active | Rate-limited (see below) |
| GPT-5.2 | 400K tokens | Project-dependent | 128K max output |
| Claude 4.5 | 200K tokens | 200K | Extended thinking consumes window |

**Reality Gap**: Web UIs aggressively compress context for browser performance. API is the real capability surface.

## Rate Limits (Gemini — the binding constraint)

| Metric | Flash (Free/Paid) | Pro (Free/Paid) |
|--------|-------------------|-----------------|
| RPM | 15 / 300 | 5 / 150 |
| TPM | 1M+ | 250K-500K |
| RPD | 1,500 | 1,000 |

## Architectural Differentiators

- **Interleaved Thinking** (Anthropic): Model re-enters thinking state *between* tool calls. Enables recursive error correction — if tool fails, model thinks about error before retrying. Linear Plan→Act architectures cannot do this.
- **Variable Sequence Length** (Google): Dynamic token allocation based on scene complexity, vs competitors' fixed 1 FPS frame sampling. Captures motion, temporal cues.
- **Large Action Models** (OpenAI Operator): Cloud-based sandboxed browser autonomy. Cannot touch local filesystem — runs in OpenAI's containers.
- **X Firehose** (Grok): Privileged real-time access to public X posts. Breaking news detection minutes before search indexes update.

## Economic Structure

- Generation tokens: commoditized ($0.50-2.00/M)
- Reasoning tokens: premium (5-10x generation cost)
- Context caching: ~10% of full input cost on subsequent prompts (Anthropic, Google)
- Perplexity Enterprise: model-agnostic — can swap underlying engine to o3 or Claude Opus ($325/seat/yr)

## Milestone Facts (Jan 2026)

- Claude Labs: $1B ARR within 6 months of launch
- MCP: 100M monthly downloads — de facto industry standard ("USB-C for AI")
- Grok Voice Agent API: 100+ languages, sub-second latency, $0.05/min, OpenAI Realtime-compatible
- ChatGPT Go: $8/mo tier, 10x usage of GPT-5.2 Instant
- Google Jules: async coding agent, clones GitHub repos to Cloud VMs

---

*Distilled from 338-line competitive analysis. Raw source archived 2026-02-22.*
