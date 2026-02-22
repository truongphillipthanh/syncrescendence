---
id: SOURCE-20260203-001
original_filename: PROMPT-AUGUR-20260203-openclaw_deep_research.md
status: triaged
platform: internal
format: research
creator: augur
signal_tier: tactical
topics:
  - ai-agents
  - openclaw
  - research
  - orchestration
teleology: reference
notebooklm_category: ai-agents
aliases:
  - "Augur prompt - OpenClaw deep research medley"
synopsis: "Research prompt dispatched from Ajna to Augur (Perplexity) as part of a 5-stream parallel research medley on OpenClaw. Augur's role is VERIFIER — citation-backed intelligence gathering."
url: internal
key_insights:
  - "The medley pattern dispatches the same research topic to 5 different AI models in parallel, each with a specialized role."
  - "Augur's verifier role leverages Perplexity's strength in sourced information retrieval."
  - "This prompt artifact documents the multi-agent research coordination pattern used by the Syncrescendence constellation."
---
# PROMPT-AUGUR-20260203-openclaw_deep_research

**From**: Ajna (OpenClaw, M1 Mac mini)
**To**: Augur (Perplexity)
**Status**: PENDING
**Execution Mode**: MEDLEY — you are one of 5 parallel research streams
**Your Role**: VERIFIER — Citation-backed intelligence gathering

---

## Context

This is Syncrescendence. You are Augur, Inquisitor, epistemic scout. You provide real-time information retrieval with citations.

We are conducting a **Phase 1-3 Deep Research** on **OpenClaw** (the platform we now run as our 9th constellation role). The goal is to fast-track to best practices — the community is already ahead of us on multi-model collaboration patterns and skill ecosystems. Some practitioners are paywalling skills. We need to catch up.

**What Ajna already has** (don't duplicate):
- Official docs read (docs.openclaw.ai)
- GitHub repo examined
- SYNTHESIS-openclaw.md written (Phase 3 synthesis from Feb 2)
- 10 ClawdHub skills installed (deep-research, council, parallel-ai-research, agentarxiv, etc.)
- Multi-agent routing docs read

---

## Prompt

Augur, ascertain the following with full citations:

### 1. OpenClaw Skill Ecosystem — State of the Art (Feb 2026)
- How many skills exist on ClawdHub as of now? Growth trajectory?
- Which skills are being paywalled or gated? By whom?
- What are the **top 10 most-installed/recommended skills** by the community?
- Are there security incidents or concerns documented?
- What's the AgentSkills spec status — is it still Anthropic-maintained or community-forked?

### 2. Multi-Model Collaboration Patterns
- Who is building multi-model agent architectures on OpenClaw? Cite specific practitioners.
- What patterns have emerged? (e.g., "council chambers," parallel research, model routing by task type)
- What's the `sessions_spawn` + `agentId` bug status (Herbert Yang reported model param silently ignored)?
- How are people using `conversationalAI` — is this an official feature or community pattern?
- What does "superintelligent paths forward" mean in practice — are there documented architectures?

### 3. OpenClaw vs Alternatives (Competitive Intelligence)
- How does OpenClaw compare to LangGraph, CrewAI, AutoGPT, AgentStack, n8n as of Feb 2026?
- What's the community sentiment? (Discord, Reddit, HN, X)
- Any notable migrations TO or FROM OpenClaw?

### 4. Brave Search API — Quick Setup
- Current pricing for Brave Search API (we need it for web_search)
- Is there a free tier?
- Any community alternatives people use instead?

**Output Format**: Structured findings with [source](url) citations for every claim. Mark confidence: CONFIRMED / DISPUTED / UNVERIFIED.

## Expected Return
Save the full output as: `-INBOX/ajna/RESULT-augur-20260203-openclaw_deep_research.md`
