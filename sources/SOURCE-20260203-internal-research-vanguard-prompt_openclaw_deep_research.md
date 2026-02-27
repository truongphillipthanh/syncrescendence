---
id: SOURCE-20260203-007
original_filename: PROMPT-VANGUARD-20260203-openclaw_deep_research.md
status: triaged
platform: internal
format: research
creator: vanguard
signal_tier: tactical
topics:
  - ai-agents
  - openclaw
  - research
  - orchestration
teleology: reference
notebooklm_category: ai-agents
aliases:
  - "Vanguard prompt - OpenClaw deep research medley"
synopsis: "Research prompt dispatched from Ajna to Vanguard (ChatGPT) as COMPILER — practical implementation patterns and creative expansion for the OpenClaw research medley."
url: internal
key_insights:
  - "Vanguard's compiler role leverages ChatGPT's strength in practical code compilation and creative pattern expansion."
  - "The medley's 5 roles map to distinct epistemic functions in intelligence gathering."
  - "This prompt documents the multi-agent research coordination pattern using role-specialized prompts across foundation models."
---
# PROMPT-VANGUARD-20260203-openclaw_deep_research

**From**: Ajna (OpenClaw, M1 Mac mini)
**To**: Vanguard (ChatGPT)
**Status**: PENDING
**Execution Mode**: MEDLEY — you are one of 5 parallel research streams
**Your Role**: COMPILER — Practical implementation patterns & creative expansion

---

## Context

This is Syncrescendence. You are Vanguard, Architect, strategic formulator. You contribute creative expansion, mind-expanding ideas, and practical code compilation.

We are conducting a **Phase 1-3 Deep Research** on **OpenClaw** — the platform we now run as our 9th constellation role (Ajna on M1 Mac mini, Psyche on M4 MBA). We need to fast-track to best practices. The community is building multi-model collaboration patterns and we're behind.

**Current Syncrescendence OpenClaw Setup**:
- M1 Mac mini: Ajna (Opus 4.5) — always-on, webchat + iMessage channels
- M4 MacBook Air: Psyche (GPT-5.2) — Slack channel
- 10 ClawdHub skills installed (deep-research, council, parallel-ai-research, etc.)
- File-based memory (MEMORY.md + daily logs)
- Heartbeat cycle running (30min)
- Twin coordination protocol v1.2.0 (Ajna↔Psyche via Slack #all-syncrescendence)
- launchd watchers for 4 roles (ajna, commander, adjudicator, cartographer)
- No Brave API key yet (web_search blocked)
- No sandbox/Docker config

**Budget**: $160/mo (Claude Max $100 + ChatGPT Plus $20 + Claude Pro $20 + Google AI Pro $20)

---

## Prompt

Vanguard, formulate a comprehensive implementation blueprint:

### 1. OpenClaw Best Practices Audit
Review our current setup against community best practices and official docs. Identify:
- What we're doing right
- What we're missing (security, sandbox, skills, config patterns)
- Quick wins we can implement today
- Strategic improvements for the next 30 days

### 2. Multi-Model Collaboration Architecture
Design an architecture for our specific setup that enables:
- **Ajna (Opus 4.5)** as orchestrator/synthesizer
- **Psyche (GPT-5.2)** as parallel executor/holistic thinker
- **sessions_spawn** with cheaper models (Sonnet, Haiku, DeepSeek) for sub-tasks
- Web platform avatars (Vizier, Vanguard, Diviner, Oracle, Augur) integrated via -OUTGOING relay

Specifically:
- When should we use `sessions_spawn` vs direct execution?
- How should we route tasks by complexity/cost?
- Can we create a "council" pattern where multiple model perspectives converge?
- What's the token-optimal strategy given our $160/mo budget?

### 3. Skill Strategy
Given ClawdHub has 1,715+ skills:
- What skill categories should we prioritize?
- Should we build custom skills for Syncrescendence-specific workflows?
- How to audit third-party skills for security?
- Propose a skill governance policy

### 4. The Conversational AI Pattern
People are using OpenClaw to have different AI models collaborate:
- How would this work technically? (sessions_spawn with different models? Multi-agent config with different providers?)
- Design a concrete workflow where Claude Opus orchestrates, GPT-5.2 executes, Gemini researches, and DeepSeek handles bulk processing
- What are the failure modes? (Herbert Yang's bug: agentId silently drops model param)

### 5. Brave Search API Setup
- Step-by-step instructions to get Brave Search API key
- Config patch needed for OpenClaw
- Cost implications for our budget

**Output Format**: Actionable blueprint with numbered steps, config examples (JSON5), and priority rankings (P0-P3).

## Expected Return
Save the full output as: `-INBOX/ajna/RESULT-vanguard-20260203-openclaw_deep_research.md`
