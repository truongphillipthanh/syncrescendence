# PROMPT-DIVINER-20260203-openclaw_deep_research

**From**: Ajna (OpenClaw, M1 Mac mini)
**To**: Diviner (Gemini Web)
**Status**: PENDING
**Execution Mode**: MEDLEY — you are one of 5 parallel research streams
**Your Role**: DIGESTOR — Technical spec extraction & long-context analysis

---

## Context

This is Syncrescendence. You are Diviner, Illuminator, multimodal clarifier. You excel at extracting technical specifications from large contexts and illuminating architectural patterns.

We are conducting a **Phase 1-3 Deep Research** on **OpenClaw**. We need deep technical extraction from the platform's architecture, focusing on the interfaces and integration points that matter for our Constellation.

**Key URLs to Deep-Read**:
1. https://docs.openclaw.ai — Full official documentation
2. https://github.com/openclaw/openclaw — Source repo, README, issues
3. https://docs.openclaw.ai/concepts/multi-agent — Multi-agent routing
4. https://docs.openclaw.ai/tools/skills — Skills system
5. https://docs.openclaw.ai/gateway/configuration — Config reference
6. https://docs.openclaw.ai/multi-agent-sandbox-tools — Per-agent sandbox + tools
7. https://agentskills.io — AgentSkills specification

---

## Prompt

Diviner, elaborate on the deep technical architecture of OpenClaw:

### 1. Complete API Surface Extraction
Extract the full tool/API surface available to an OpenClaw agent:
- All built-in tools (read, write, edit, exec, process, browser, canvas, nodes, cron, message, gateway, sessions_*, session_status, memory_*, web_search, web_fetch, image, tts, agents_list)
- For each tool: parameters, capabilities, limitations, gotchas
- Which tools are available in sandboxed vs unsandboxed mode?
- What's the `tools.profile` system? (coding, messaging, etc.)

### 2. Sessions Architecture Deep-Dive
- How does `sessions_spawn` actually work? (model routing, label, cleanup, timeout)
- What's the relationship between sessions, agents, and session keys?
- How do sessions communicate? (sessions_send, sessions_history)
- What are the session lifecycle events?
- The Herbert Yang bug: `agentId` + `model` interaction — is this documented?

### 3. Cron & Heartbeat Architecture
- Full cron job schema (schedule types: at, every, cron)
- Payload types: systemEvent vs agentTurn
- sessionTarget: main vs isolated — when to use which?
- How does heartbeat polling interact with cron?
- Can cron jobs trigger sessions_spawn?

### 4. Skills System Technical Spec
- Full SKILL.md schema (frontmatter fields, metadata, gating)
- How does skill precedence work? (workspace > managed > bundled)
- How does `{baseDir}` resolution work?
- Can skills register custom tools? Or only teach existing tool usage?
- Plugin skills vs standalone skills — what's the difference?

### 5. Multi-Agent Configuration Patterns
- Full `agents.list[]` schema (all fields)
- Binding resolution order (most-specific wins)
- Tool restriction precedence chain (8 levels documented)
- Agent-to-agent messaging: how to enable and use
- How do multiple agents share a single channel account?

### 6. Integration Points for Syncrescendence
Map OpenClaw's architecture onto our Constellation:
- Which OpenClaw patterns map to our CAPTURE → DISPATCH → RETURN flow?
- Can we use multi-agent routing to create dedicated "lanes" for different constellation roles?
- How does OpenClaw's memory system (MEMORY.md + memory_search) compare to our repo-based ground truth?
- Can webhook/cron trigger external tool invocations (Gemini CLI, Claude Code)?

**Output Format**: Technical reference document with code examples, schema definitions, and architecture diagrams (text-based). Organize as a reference manual.

## Expected Return
Save the full output as: `-INBOX/ajna/RESULT-diviner-20260203-openclaw_deep_research.md`
