# Oracle Dispatch — Autonomous Execution: Closing the Browser Gap

**From**: Commander (Claude Opus 4.6) / Sovereign
**Session**: CC66b (tool stack lane)
**Git HEAD**: c0af4f30
**Repo**: https://github.com/truongphillipthanh/syncrescendence
**Date**: 2026-03-01

---

## Context (You Have This From Our Thread)

In CC65 you told us 4/6 Sovereign actions were automatable via Playwright MCP + APIs. We've now executed:
- OpenClaw clean rebuild: Ajna alive on Claude Sonnet 4.5, gateway running, dispatch confirmed
- Commander (Claude Opus via Claude Code) has Playwright MCP installed
- Commander → Ajna dispatch works (`openclaw agent --agent main --message`)
- Tool stack LOCKED per `engine/CC65-TOOL-STACK-FINAL.md`

**What we discovered during the rebuild:**
- Channel tokens (Slack bot, Discord bot) from the previous install are ALL stale — `invalid_auth` and `Failed to resolve Discord application id`
- OpenClaw `setup-token` auth requires interactive browser OAuth — no headless path
- Docker sandbox requires Docker Desktop (not installed on MBA) — sandbox mode is OFF
- The workspace must NOT be the repo root (repo's AGENTS.md at 22K gets loaded as agent instructions)

**Current state of the Sovereign browser gap** — these actions still require the Sovereign to open a browser:
1. Cancel Perplexity Pro subscription
2. Enroll xAI data sharing program
3. Register syncrescendence.com (Cloudflare)
4. Claim GCP $10/mo credits
5. Regenerate Slack bot token (stale)
6. Regenerate/verify Discord Ajna bot token (stale)
7. Manus API authentication (sk- key rejected as "malformed token")
8. Any future OAuth token refresh for OpenClaw

## What We Need You To Sense

**Q1 — The Playwright MCP bridge: what's actually working in production?**

Commander has `@playwright/mcp` installed in Claude Code. In theory this gives browser automation. In practice:
- Are solo builders ACTUALLY using Playwright MCP from Claude Code to manage subscriptions, claim credits, regenerate API keys?
- What are the specific failure modes? (2FA gates, CAPTCHA, session cookies, rate limiting on automated logins)
- Is there a better MCP server or skill for browser automation than Playwright? (Computer use agents, OpenClaw browser skills, Cowork)
- What's the authentication pattern — does the agent log in from scratch each time, or is there a persistent browser profile/cookie jar approach?

Quote real practitioner experiences. "Works great" is useless; I need "I use Playwright MCP to renew my API keys on console.anthropic.com every month — here's the flow: ..."

**Q2 — Service-specific automation paths (March 2026 reality)**

For each of our 8 browser-gap items, what is the ACTUAL autonomous path as of March 2026?

| # | Action | What We Know | What We Need |
|---|--------|-------------|-------------|
| 1 | Cancel Perplexity Pro | No known API | Is there a CLI, API, or Playwright-drivable cancellation flow? |
| 2 | xAI data sharing enrollment | Dashboard-only (CC65) | Has this changed? Any API? Any community automation? |
| 3 | syncrescendence.com registration | Cloudflare API for DNS, not registration | Has Cloudflare Registrar API launched? Any registrar with full API? |
| 4 | GCP credits claim | Console-only (CC65) | `gcloud` CLI path? Any community automation? |
| 5 | Slack bot token regeneration | api.slack.com dashboard | Slack API has programmatic token rotation — what's the exact endpoint? |
| 6 | Discord bot token regeneration | Discord developer portal | Discord API for bot token reset — does it exist? |
| 7 | Manus API auth | sk- key rejected | What is the correct auth format? JWT? Bearer token? Has the API documentation been published? |
| 8 | OpenClaw OAuth refresh | Browser required | Any headless OAuth flow? `openclaw models auth` non-interactive path? |

For EACH: (a) fully autonomous CLI/API path if it exists, (b) Playwright-drivable path if no API, (c) irreducible Sovereign gate if neither works.

**Q3 — The OpenClaw skills/MCP ecosystem for browser automation**

What OpenClaw skills or MCP servers exist RIGHT NOW for:
- Persistent browser sessions (cookie jar across agent sessions)
- Subscription management automation
- API key rotation automation
- OAuth token refresh automation
- Dashboard navigation for services without APIs

ClawHub has 700+ skills. Which ones address this gap? Are any production-tested for the specific services in our stack (Anthropic, Slack, Discord, Cloudflare, GCP, xAI)?

**Q4 — The Docker question**

Our sandbox is OFF because Docker Desktop isn't installed on MBA. The neocorpus says sandbox mode `all` + Docker network isolation is the security baseline. But Docker Desktop on MBA means:
- Resource overhead (RAM, disk)
- Potential conflicts with other dev tools
- One more thing to maintain

What are power users doing on macOS for OpenClaw security without Docker? Is sandbox mode actually necessary for a single-operator, loopback-only deployment? What's the minimal security posture that the community considers acceptable for personal use?

**Q5 — Ajna's capability surface: what should we outfit her with?**

Ajna is alive on Sonnet but has ZERO skills installed. The neocorpus (`openclaw-skills-platform-economics.md`) says 44 skills were eligible in the old install, with agent-dispatch and team-orchestration as the recommended minimum.

Given our architecture (Ajna dispatches FROM OpenClaw to Commander and eventually to the wider constellation):
- What skills should Ajna have for the dispatch-FROM pattern?
- What skills enable Ajna to close the browser gap (if any)?
- What's the minimal skill set that makes Ajna a force multiplier vs just a chat endpoint?
- What skills should we AVOID (token drains, security risks, redundant with Commander's capabilities)?

Name specific ClawHub skills. "Install agent-dispatch" is useful; "install useful skills" is not.

## Constraints

- One Claude Max subscription (Commander) + OpenClaw on Anthropic token (Ajna = Sonnet)
- No Docker Desktop on MBA currently
- Mac mini ANESTHETIZED — MBA only
- Playwright MCP installed in Claude Code but untested
- Tool stack LOCKED — no new subscriptions until April retool
- Factory test: must build artifacts, be agent-drivable, no vendor lock-in

## What I Want

The real-world practitioner playbook for closing the browser gap with the tools we already have. Not architecture diagrams — specific commands, specific skills, specific failure modes. Who is doing this successfully and what does their setup look like?

Exhaust your output tokens.
