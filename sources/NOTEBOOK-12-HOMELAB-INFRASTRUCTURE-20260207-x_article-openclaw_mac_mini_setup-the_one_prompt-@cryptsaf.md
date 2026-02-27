---
url: https://x.com/CrypSaf/status/2020211635579756905
author: SafZ (@CrypSaf)
captured_date: 2026-02-13
---

# OpenClaw Mac Mini Setup - The One Prompt 🦞

(Description: A dark-themed hero image featuring a Mac Mini computer on the left, security lock icon, lightning bolt symbol, and a cartoon lobster emoji on the right. Text overlay reads "GET STARTED / OpenClaw × Mac Mini – The Only Setup Guide You Need" with neon cyan and purple accents.)

## Why This Exists

Most people set up OpenClaw, pick Claude Opus as default, connect Telegram, and call it a day.

Then they wonder why:

- Their API bill hit $300 in week one
- Their agent forgot everything from yesterday
- A session-logs skill they never installed is silently loading full conversation history into every prompt
- Their gateway is exposed to their local network
- Their bot's personality file got rewritten by a prompt injection

This prompt fixes all of that before it happens.

## What It Does

You paste it into **any AI** (Claude, GPT, Gemini, or Grok) and it walks you through the full setup, step by step.

When you're done:

1. **You spend less:** Haiku default, Ollama for heartbeats (local LLM), no silent context loading, session-logs killed
2. **You're secure:** loopback gateway, pairing-only DMs, sandboxed channels, SOUL.md integrity checks, config.patch disabled
3. **Your agent's memory is clean:** file-first, explicit loads only, no background bleed, auditable workspace
4. **Your agent has rules per tool:** not one vague contract, but specific governance files for Gmail, reminders, filesystem, and cron
5. **Your automation is safe:** isolated sessions, no-deliver, Haiku-only, artifact output only

## How To Use It

1. Copy the entire prompt below
2. Open a new chat in your preferred AI
3. Paste it
4. Follow the steps it gives you
5. Don't skip security

That's it.

## The Prompt

Copy everything:
```
You are my setup assistant for OpenClaw on a fresh Mac Mini (Apple Silicon, 16GB RAM). Walk me through the entire setup step by step. Be direct — give me exact commands to paste, exact files to create, exact prompts to use. No explanations unless I ask. Just: do this, paste this, confirm this, next. This setup must be optimized for three things: SECURITY, TOKEN COST, and MEMORY. In that order. Here is the full spec. Follow it exactly.

--- MACHINE SETUP (before OpenClaw):
- macOS: "Set up as new" — no migration, no data transfer
- FileVault: ON
- Firewall: ON
- iCloud: sign in for Continuity, but disable iCloud Drive, Desktop/Documents sync, Photos, Notes, Safari, Messages, and Keychain on this machine
- Universal Clipboard / Handoff: treat as shared surface — disable if strict isolation is needed
- Install Xcode CLI tools: xcode-select --install
- Install Homebrew (Apple Silicon path: /opt/homebrew/)
- Install Node.js 22+ via brew

--- OPENCLAW INSTALL:
- Install OpenClaw globally via npm
- Run: openclaw onboard --install-daemon
- Provider: Anthropic
- Auth: API key (not subscription — API requires funded credits at console.anthropic.com)
- First hatch: TUI (not web UI)
- Gateway must bind to 127.0.0.1 (loopback only) — verify with: openclaw gateway status
- If remote access is ever needed: Tailscale tunnel only, never expose ports

--- SECURITY CONFIG (non-negotiable):

1. DM policy = pairing (never "open") for all messaging channels
2. Sandbox mode = "non-main" in ~/.openclaw/openclaw.json (isolates Telegram/WhatsApp from host)
3. Disable config.patch tool on any agent connected to external messaging channels (prevents "soul-evil" backdoor — a known mechanism that can swap SOUL.md via prompt injection)
4. Run: openclaw security audit --fix
5. Store API keys via: openclaw auth set anthropic (system keychain, not plaintext files)
6. Hash SOUL.md for integrity checking: md5 ~/.openclaw/workspace/SOUL.md — save the hash, compare weekly
7. Create containment folder: mkdir ~/ClawWork — agent can only read/write inside this path and ~/.openclaw/workspace/
8. Never grant Full Disk Access
9. Create individual rule files per tool (not one big contract):
   - GMAIL_RULES.md
   - REMINDERS_RULES.md
   - FILESYSTEM_ACCESS.md
   - HEARTBEAT_PROMPT.md
   Each file governs exactly what the agent can and cannot do with that tool.

--- TOKEN OPTIMIZATION (critical):

1. Default model = Claude Haiku: openclaw models set claude-haiku-4-5
   - Sonnet = heavy lifting only (specs, code gen, architecture)
   - Opus = complex reasoning only, switched manually with /model
2. Delete session-logs skill IMMEDIATELY: rm -rf ~/.openclaw/workspace/skills/session-logs
   This skill silently loads full conversation history into every prompt. Biggest hidden token drain in OpenClaw.
3. Memory is NOT auto-loaded. For routine prompts, always include: "Do not load MEMORY.md / IDENTITY.md / session logs."
   Only load memory when personalized context is actually needed.
4. Install Ollama for $0 heartbeats: curl -fsSL https://ollama.com/install.sh | sh
   ollama pull llama3.2:3b
   Point heartbeat model to ollama/llama3.2:3b in ~/.openclaw/openclaw.json
5. Disable unused MCP servers (/mcp to check). Each adds 313-700+ tokens to every message.
6. Compact sessions proactively at 60-70% context with /compact — don't wait for auto-compact at 80%+
7. For long sessions use "Document and Clear": ask agent to write plan/progress to ~/ClawWork/handoff.md, then /clear, then point agent to that file to continue. Saves 50-70% tokens.
8. Set hard monthly spending limit at console.anthropic.com → Billing
9. Monitor with: npx ccusage@latest daily
10. Gmail must be bounded: last 24hrs only, max 5 threads, no attachments, no full mailbox scans, no sending/deleting. Create GMAIL_RULES.md with these exact limits.
11. Cron heartbeats must use: isolated session + --no-deliver + Haiku model + timeout. Otherwise they load full main session context every ping.
12. Local transcription via Whisper.cpp (ffmpeg .m4a→.wav→whisper-cli) = 0 API tokens for voice notes.

--- MEMORY SYSTEM:

1. All memory files live in ~/.openclaw/workspace/ (NOT agents/main/agent/)
   Required files: USER.md, IDENTITY.md, SOUL.md, MEMORY.md, OPERATING_CONTRACT.md
   Daily logs: memory/YYYY-MM-DD.md
2. USER.md = full brain dump about the user (name, role, projects, routine, preferences, tools, important people)
3. IDENTITY.md = agent persona (name, role, communication style)
4. OPERATING_CONTRACT.md must contain: "You prepare, propose, and remind. I decide and approve. Never execute destructive actions without my explicit OK. Never contact anyone on my behalf without approval. Questions = answer them. Don't execute. If unsure about intent, ask before acting."
5. MEMORY_POLICY.md must contain: "Do not load memory by default. Load only when prompt explicitly requests it. Availability ≠ inclusion."
6. Memory verification test after setup: Prompt: "Confirm memory loaded. Reply OK." Then: "What are my current projects? 2 sentences max." If it hallucinates → files are in wrong directory.
7. To save facts: "Remember this: [fact]" — agent must confirm write to MEMORY.md
8. Before any /compact or /clear: "Write all important decisions and action items from this session to today's memory log before I clear." Wait for confirmation.
9. Keep all memory files under 4-8KB combined. Over 16KB = 20-30% performance drop. Point to external files instead of pasting content inline.
10. Weekly hygiene prompt: "Review this week's daily logs. Extract important long-term facts to MEMORY.md. Summarize what you moved."

--- FINAL STATE VERIFICATION:

After setup is complete, confirm:
- Gateway: loopback only (127.0.0.1)
- Default model: Haiku
- session-logs skill: deleted
- Sandbox: non-main
- DM policy: pairing
- config.patch: disabled
- SOUL.md: hashed
- Memory: explicit load only
- Cron: empty (automation is earned, not assumed)
- Spending limit: set
- Skills installed: minimal (tmux-terminal, gmail read-only, apple-reminders max)

Walk me through each section now. One step at a time. Wait for my confirmation before moving to the next step.
```

That's it. Paste it. Follow the steps. Lock your setup down before you do anything else.

Everything you add after, skills, dashboards, automations, browser control, is built on top of this foundation.

Not before it. After.

P.S: Shoutout to @AlexFinn, learned a lot from his YT videos ❤️

All the best.

---

**Engagement:** 76 replies, 42 reposts, 583 likes, 1.3K bookmarks, 109.8K views

**Published:** 11:02 AM · Feb 7, 2026