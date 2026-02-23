# DISPATCH: OpenClaw Deep Research — MEDLEY

**Created**: 2026-02-03 @ 6:20 PM PT
**From**: Ajna
**Mode**: **MEDLEY** (specialized extraction per platform — NOT chorus)
**Topic**: OpenClaw best practices, multi-model collaboration, skill ecosystem

---

## Why MEDLEY (not Chorus)

**Chorus** = all platforms answer the same question → redundancy → synthesis required
**Medley** = each platform answers a different facet → complementary → integration required

This is MEDLEY because:
- Each platform has a unique data advantage (Perplexity has citations, Grok has X firehose, etc.)
- The research questions are faceted, not singular
- We want maximum information surface, not convergence

---

## Dispatch Order (Recommended)

Run these in parallel or in quick succession. Order doesn't matter (no dependencies between streams), but this sequence optimizes for Vizier receiving the others' output last for synthesis:

| # | Avatar | Platform | File | Time Est. |
|---|--------|----------|------|-----------|
| 1 | **Augur** | Perplexity | `-OUTGOING/augur/PROMPT-AUGUR-20260203-...` | 5-10 min |
| 2 | **Oracle** | Grok | `-OUTGOING/oracle/PROMPT-ORACLE-20260203-...` | 10-15 min |
| 3 | **Diviner** | Gemini Web | `-OUTGOING/diviner/PROMPT-DIVINER-20260203-...` | 10-15 min |
| 4 | **Vanguard** | ChatGPT | `-OUTGOING/vanguard/PROMPT-VANGUARD-20260203-...` | 10-15 min |
| 5 | **Vizier** | Claude Web | `-OUTGOING/vizier/PROMPT-VIZIER-20260203-...` | 15-20 min (synthesis) |

**Total estimated**: 30-45 min if parallelized, 50-75 min if sequential

---

## Instructions for Sovereign

### For Each Platform:
1. Open the web app (Perplexity / Grok / Gemini / ChatGPT / Claude)
2. Copy the **## Prompt** section from the corresponding PROMPT file
3. Paste into the platform
4. If the platform has the Avatar config loaded (project instructions/custom GPT/etc.), great — if not, also paste the **## Context** section
5. Capture the full output
6. Save to: `-INBOX/ajna/RESULT-{avatar}-20260203-openclaw_deep_research.md`
7. Mark the PROMPT file status as DISPATCHED → COMPLETE

### For Vizier (Last):
- **Wait until you have results from at least Augur + Oracle + Vanguard**
- Append a brief summary of their findings before/after the Vizier prompt
- This gives Vizier the raw material for synthesis
- Alternatively: just run Vizier independently and I'll do the final synthesis myself

### What Ajna Will Do While You Dispatch:
- Continue self-research using OpenClaw docs, web_fetch, bird search
- Test installed skills (council, deep-research, parallel-ai-research)
- Explore sessions_spawn patterns with different models
- Prepare SYNTHESIS document structure for when results come in

---

## Return Artifacts Expected

| File | From | Purpose |
|------|------|---------|
| `RESULT-augur-20260203-openclaw_deep_research.md` | Perplexity | Citations + ecosystem map |
| `RESULT-oracle-20260203-openclaw_deep_research.md` | Grok | X discourse intelligence |
| `RESULT-vanguard-20260203-openclaw_deep_research.md` | ChatGPT | Implementation blueprint |
| `RESULT-diviner-20260203-openclaw_deep_research.md` | Gemini | Technical reference |
| `RESULT-vizier-20260203-openclaw_deep_research.md` | Claude Web | Strategic synthesis |

All go to: `~/Desktop/syncrescendence/-INBOX/ajna/`

---

## After All Results Are In

Ajna will execute **Phase 3 (Synthesis)** → `sources/research/openclaw/SYNTHESIS-openclaw-v2.md`
Then **Phase 4 (Reconciliation)** → Rosetta Stone delta
Then **Phase 5 (Operationalization)** → Updated config, skills, workflows
