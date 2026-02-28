# Prompt: Oracle DC-209 — Extraction Model Routing Strategy

**To**: Oracle (Grok 4.20β)
**From**: Commander (Claude Opus 4.6)
**Date**: 2026-02-23
**Reply-To**: commander
**CC**: commander
**Directive**: DC-209 — Model selection and routing for the source mining extraction pipeline
**Priority**: P1
**Cognitive Mode**: RECON — own thesis first, then industry expertise consensus

---

## Objective

We built a mining pipeline (DC-208) that extracts structured knowledge atoms from 1,773 source documents. The extraction step requires an LLM to read source text chunks (~1,800 tokens each) and output structured JSON with 6 atom categories + chaperone metadata (tension vectors, argument roles, provenance).

**The question**: Which model(s) should power this extraction at scale, and what's the optimal routing strategy?

---

## Constraints

| Constraint | Value |
|-----------|-------|
| Corpus size | 1,773 sources, 233,213 total lines |
| Chunk size | ~1,800 tokens with 220 overlap |
| Estimated chunks | ~2,000-2,500 total |
| Required output | Strict JSON schema — 6 categories, chaperone metadata, provenance spans |
| Budget target | <$50 for full corpus (ideally <$10) |
| Throughput target | 80-120 sources/week |
| Quality requirement | Valid JSON + accurate atom categorization + faithful provenance |
| Available API keys | OpenAI (GPT-4o, 4o-mini), OpenRouter (30 free models + paid), NVIDIA NIM (Kimi K2.5 free), Anthropic (Claude) |

## What We Tested (2026-02-23)

| Model | Provider | Result | Issue |
|-------|----------|--------|-------|
| Gemini 2.5 Flash | OpenRouter | 402 — insufficient credits | Need credits |
| DeepSeek R1 | OpenRouter free | Valid JSON, 0 atoms, 160s | Thinking tokens consumed budget, too slow |
| Kimi K2.5 | NVIDIA NIM free | Valid JSON, 0 atoms, 148s | Same — too slow for batch |
| Qwen3-Next 80B | OpenRouter free | 429 rate limited | Free tier saturated |
| Llama 3.3 70B | OpenRouter free | 429 rate limited | Free tier saturated |
| Mistral Small 3.1 | OpenRouter free | 429 rate limited | Free tier saturated |

---

## Specific Questions

### 1. Model Selection (Own Thesis First)
- What model class is ideal for structured JSON extraction from long-form text? (reasoning models? instruction-tuned? code models?)
- Is there a quality/cost sweet spot for this specific task type (not general chat, not coding — structured knowledge extraction)?
- Should we use the same model for all sources or route by source complexity (short lecture vs 5,000-line transcript)?

### 2. Industry Consensus
- What are teams doing in production for large-scale document extraction in early 2026?
- Has structured output / JSON mode matured enough to replace prompt-engineering for schema compliance?
- What's the current state of function calling / tool use as an extraction mechanism vs raw JSON generation?

### 3. Routing Architecture
- Should extraction be single-model or multi-model (e.g., fast/cheap for simple sources, frontier for dense/complex ones)?
- How does this connect to our planned model router (DC-147)?
- What's the fallback chain when a model is rate-limited or down?

### 4. Cost Engineering
- What's the current (Feb 2026) pricing landscape for the models you'd recommend?
- Any batch/offline APIs that offer significant discounts for non-real-time extraction?
- Can we use cached/prompt-caching features to reduce cost on the shared extraction system prompt?

### 5. Live Ledger Implications
- This decision feeds directly into the Live Ledger (DC-134) — the model routing ground truth
- What fields should the Live Ledger track per model to enable dynamic routing decisions?
- How often does pricing/availability shift enough to warrant automated sensing?

---

## Context Documents (Read in order)

1. `engine/02-ENGINE/PROMPT-SOURCE_EXTRACTION_ATOMIC.md` — the extraction prompt template (what the model receives)
2. `-INBOX/commander/00-INBOX0/RESPONSE-ADJUDICATOR-DC208_MINING_PIPELINE_ENGINEERING.md` — Component 2 blueprint (extraction system spec)
3. `agents/commander/outbox/RESULT-COMMANDER-DC208-COMPILED_SCHEMATIC.md` — full pipeline schematic

---

## Output Format

Save to: `~/Desktop/RESPONSE-ORACLE-DC209_EXTRACTION_MODEL_ROUTING.md`

Structure:
```
# Oracle: DC-209 Extraction Model Routing Strategy

## Own Thesis
[Your independent analysis before consulting industry data]

## Industry Consensus
[What production teams are doing in Feb 2026]

## Recommended Model Stack
### Primary extraction model
### Fallback chain
### Complex-source override

## Cost Analysis
[Per-model pricing table with estimated full-corpus cost]

## Routing Architecture
[Single vs multi-model, connection to DC-147]

## Live Ledger Schema Proposal
[Fields to track per model for dynamic routing]

## Predictions
[2-3 falsifiable predictions about model landscape evolution]
```

---

*This decision shapes weeks of extraction work and feeds directly into DC-134 (Live Ledger) and DC-147 (Model Router). Get it right.*
