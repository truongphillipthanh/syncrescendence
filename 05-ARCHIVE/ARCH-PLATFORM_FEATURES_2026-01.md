---
archive_id: ARCH-PLATFORM_FEATURES_2026-01
title: Platform Feature Topology - January 2026
date: 2026-01-11
source: Oracle 12
type: research
status: archived
temporal_validity: Q1 2026
superseded_by: null
cross_refs:
  - CANON-31142-PLATFORM_GRAMMAR
  - CANON-31140-IIC
  - CANON-31141-FIVE_ACCOUNT
synopsis: |
  Comprehensive AI platform feature topology covering Claude, ChatGPT, Gemini,
  Grok, and Perplexity. Includes surface inventories, memory architectures,
  context specifications, MCP ecosystem, and routing strategies.
key_findings:
  - Claude trifurcation: Web, Desktop (MCP), CLI (extended thinking)
  - Claude rate limits shared across ALL surfaces (~45/5hr Pro)
  - Gemini YouTube: 263 tok/sec video, 32 tok/sec audio
  - Gemini Jules: Async coding agent with GitHub integration
  - Gemini Project Mariner: Web browsing agent, 10 concurrent tasks
  - ChatGPT Codex CLI: Superior GitHub integration, @codex in PRs
  - MCP ecosystem: Claude deepest, Codex stdio-only, Gemini CLI full
warning: |
  Platform features evolve rapidly. This document captures January 2026 state.
  Verify current capabilities before operational use.
---

# Comprehensive AI Platform Feature Topology
## Claude, ChatGPT, Gemini, Grok, and Perplexity (January 2026)

### Executive Synopsis

The AI landscape of January 2026 represents a fundamental transition from the "Chatbot Era" into the "Agentic Era," characterized by persistent state, multi-step reasoning, and deep integration into operating systems and development environments.

**Critical Findings:**
- **Gemini's multimodal supremacy**: Processes YouTube videos natively at 263 tokens/second (video) and 32 tokens/second (audio)
- **Gemini's agentic expansion**: Project Mariner for web browsing, Jules for async coding
- **Claude's reasoning depth**: Extended thinking modes with up to 31,999 tokens in CLI
- **ChatGPT's ecosystem breadth**: Codex CLI with superior GitHub integration
- **Grok's X integration**: Exclusive real-time social data access

---

## Claude Surface Inventory

### Web Interface (claude.ai)
- Projects with file RAG (up to 10x context expansion)
- Deep Research (45-minute sessions)
- Artifacts (React, SVG, Mermaid, Office documents)
- Memory + Connectors (GitHub, Drive, Slack)
- File limits: 30MB per file, 20 files per chat, 200K base context

### Desktop Application
- Full web parity plus **native MCP server support**
- Desktop Extensions (.mcpb format)
- Window screenshot sharing
- Multi-session Claude Code with plan/execute mode

### CLI (Claude Code)
- CLAUDE.md hierarchical loading (5-hop recursion)
- Extended thinking triggers:
  - `think` → 4,000 tokens
  - `think hard` / `megathink` → 10,000 tokens
  - `think harder` / `ultrathink` → 31,999 tokens
- Custom slash commands (/memory, /compact)
- Headless mode (-p flag)

### Rate Limits (CRITICAL)
- Pro tier: ~45 messages per 5-hour rolling window
- **SHARED ACROSS ALL SURFACES** (web, desktop, CLI, mobile)
- Heavy Opus 4.5 usage depletes quota faster than Sonnet

---

## Gemini Surface Inventory

### Gemini CLI
- Full MCP support
- Google Search grounding
- Free tier: 60 RPM, 1,000 requests/day
- Fastest execution among CLI tools

### Jules (Async Coding Agent)
- GitHub integration with async execution
- Runs tasks in background while developer works
- CLI (Jules Tools) and API
- Gemini 3 Pro reasoning

### Project Mariner (Web Browsing Agent)
- Up to 10 concurrent tasks in cloud VMs
- Available to Ultra subscribers ($249.99/month, US only)
- Integration pathway: API → Search AI Mode → Gemini Agent Mode

### YouTube Processing
- Video: 263 tokens/second (258 tokens/frame at 1fps)
- Audio: 32 tokens/second
- Speaker diarization via lip movement analysis
- OCR for on-screen text
- **Public videos only**

---

## ChatGPT Surface Inventory

### Codex CLI
- No waitlist (Plus/Pro required)
- Three modes: CLI, IDE integration, Cloud
- @codex integration in GitHub PRs
- MCP support (stdio only, not HTTP)
- Open source with community contributions

### Atlas Browser
- AI-powered web automation
- Virtual desktop with persistent sessions

### ChatGPT Agent
- Unified Operator + Deep Research + chat
- Virtual desktop environment

---

## MCP Ecosystem Comparison

| Platform | Support | Protocol | Depth |
|----------|---------|----------|-------|
| Claude | Native (creator) | HTTP + stdio | Deepest |
| ChatGPT | Codex CLI | stdio only | Growing |
| Gemini | CLI only | Full MCP | Moderate |
| Grok | None | — | — |
| Perplexity | None | — | — |

---

## Optimal Routing Strategies

### Task-Based Decision Tree

**Multimodal Research**:
- YouTube videos → Gemini
- Image generation → ChatGPT (DALL-E 3) or Grok (Aurora)
- Voice conversation → ChatGPT Advanced Voice Mode

**Code & Development**:
- Architecture → Claude Code (extended thinking)
- GitHub workflows → Codex CLI (@codex)
- Async background → Jules

**Research & Synthesis**:
- Citations critical → Perplexity Pro Search
- Deep synthesis → Claude Deep Research
- X/Twitter data → Grok

---

## Constellation Architecture Recommendations

**Full Constellation ($80/month)**:
- Claude Pro ($20): Oracle, project memory, code architecture
- ChatGPT Plus ($20): Codex CLI, GitHub integration, voice
- Gemini Advanced ($20): YouTube processing, Jules, 2M context
- Perplexity Pro ($20): Citation-grounded research

---

*Archived: 2026-01-11*
*Source: platform_features.md (1,948 lines, Oracle 12 research)*
*Temporal validity: Q1 2026*
