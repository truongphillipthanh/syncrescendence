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

**What we discovered SINCE the rebuild (new intelligence):**
- **Peekaboo 3.0** is installed — full macOS UI automation (click, type, scroll, capture, menus, dialogs, ANY app). This is potentially MORE powerful than Playwright for our use case because it controls the actual macOS desktop, not just a browser tab. Has `--profile human` for anti-bot organic mouse motion. Needs Screen Recording + Accessibility permissions (one-time).
- **Slack bot token is ACTUALLY VALID** (`auth.test` returns ok=true, team=Syncrescendence, user=ajna). The socket mode app token is stale but bot API access works.
- Discord bot token is genuinely stale (401 Unauthorized from `/users/@me`).
- `gcloud` CLI is installed (v542) but has NO auth — needs one-time browser OAuth
- `wrangler` CLI installed (v4.69) — needs one-time auth
- `gh` CLI fully authenticated and operational
- `clawhub` CLI installed globally
- OpenClaw has 36/51 bundled skills ready including `peekaboo`, `slack`, `discord`, `github`, `coding-agent`, `tmux`, `gog` (Google Workspace), `gemini`
- ClawHub browser skills (`agent-browser`, `browser-automation`) flagged suspicious by VirusTotal — not safe to install
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

**Q1 — Peekaboo vs Playwright vs Computer Use: what's the production winner?**

We now have THREE browser automation options:
1. **Peekaboo 3.0** (macOS UI automation) — controls the actual desktop, any app, menus, dialogs. Has `--profile human` anti-bot. OpenClaw bundled skill + CLI.
2. **Playwright MCP** (browser automation) — Chromium-level DOM interaction from Claude Code.
3. **Claude Computer Use / Cowork** — Anthropic's native approach.

Which are solo builders ACTUALLY using for: managing subscriptions, regenerating API keys, claiming credits, navigating dashboards? Is Peekaboo the winner for macOS-native deployments? What are the failure modes of each? (2FA gates, CAPTCHA, session cookies, rate limiting)

What's the authentication pattern — does the agent log in from scratch each time, or is there a persistent browser profile/cookie jar approach? Peekaboo works at the OS level so it inherits the user's existing browser sessions — is this the practical advantage?

Quote real practitioner experiences. "Works great" is useless; I need "I use Peekaboo to regenerate my Slack tokens monthly — here's the flow: ..."

**Q2 — Service-specific automation paths (March 2026 reality)**

For each of our 8 browser-gap items, what is the ACTUAL autonomous path as of March 2026?

| # | Action | What We Now Know | What We Still Need |
|---|--------|-----------------|-------------------|
| 1 | Cancel Perplexity Pro | No known API | Peekaboo-drivable flow? What's the click path? |
| 2 | xAI data sharing enrollment | Dashboard-only | Peekaboo-drivable? What's the click path on console.x.ai? |
| 3 | syncrescendence.com registration | Cloudflare Wrangler v4.69 installed — DNS yes, registration unclear | Has Cloudflare Registrar API launched in 2026? `wrangler` domain registration? |
| 4 | GCP credits claim | `gcloud` v542 installed, NO auth | After `gcloud auth login`, can credits be claimed via CLI? Or Peekaboo on console? |
| 5 | Slack app token regen | **Bot token VALID** (ajna@Syncrescendence). App token stale (socket mode). | Slack `apps.connections.open` needs fresh app-level token — can this be rotated via Slack API? Or dashboard-only? |
| 6 | Discord bot token regen | Token is 401 Unauthorized | Discord API for bot token reset — does it exist? Or developer portal only (Peekaboo)? |
| 7 | Manus API auth | sk- key rejected as "malformed token" | Correct auth format? JWT? Has docs.manus.im published the API spec? |
| 8 | OpenClaw token refresh | `openclaw onboard --auth-choice token --token KEY --token-provider anthropic` WORKS non-interactively | SOLVED — no browser needed if Sovereign provides the setup-token string |

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
- Peekaboo 3.0 installed but NEEDS Screen Recording + Accessibility permissions
- Playwright MCP connected but untested in production
- gcloud + wrangler installed but not yet authenticated
- Slack bot token VALID; app token and Discord token STALE
- No Docker Desktop on MBA
- Mac mini ANESTHETIZED — MBA only
- Tool stack LOCKED — no new subscriptions until April retool
- Factory test: must build artifacts, be agent-drivable, no vendor lock-in

## What I Want

The real-world practitioner playbook for closing the browser gap with the tools we already have. Not architecture diagrams — specific commands, specific skills, specific failure modes. Who is doing this successfully and what does their setup look like?

Exhaust your output tokens.
