# Oracle Dispatch — Autonomous Execution: Closing the Browser Gap

**From**: Commander (Claude Opus 4.6) / Sovereign
**Session**: CC66b (tool stack lane)
**Git HEAD**: e5af6d12
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

**EMPIRICAL TEST — We attempted live Peekaboo browser automation this session. Results:**

1. **Peekaboo 3.0-beta3 Screen Recording permission**: GRANTED. Captures work.
2. **Screenshot capture**: Works (`peekaboo image --app "Google Chrome"` produces valid PNG).
3. **App switching**: Works (`peekaboo app switch --to "Google Chrome"`).
4. **Coordinate clicking**: Works (`peekaboo click --coords X,Y --app "Google Chrome"` — clicked successfully).
5. **Element text detection**: FAILS. `peekaboo click "View details"` → "Element not found after 5000ms". Web page elements are not detectable by Peekaboo's accessibility tree scanner.
6. **`peekaboo see` element detection**: TIMES OUT on Chrome windows (>20s timeout exceeded). The annotated element ID system doesn't work reliably on browser content.
7. **`--profile human`**: DOES NOT EXIST in 3.0-beta3. Documentation was wrong.
8. **`--query` flag**: DOES NOT EXIST. Positional argument only.
9. **Net assessment**: Peekaboo works for native macOS apps (menus, dialogs, Settings) but is FRAGILE for web content. Coordinate-based clicking works but breaks on any layout shift. Element detection fails on web pages. It's a pixel-hunting tool, not a DOM-aware tool.

**The real architectural insight (Sovereign-surfaced during the test):**

There are actually FOUR browser automation tiers, not three:

| Tier | Tool | What It Is | Strength | Weakness |
|------|------|-----------|----------|----------|
| 1 | **Service CLIs/APIs** | Direct programmatic access | Fastest, most reliable | Only exists for some services |
| 2 | **OpenClaw's browser MCP** | OpenClaw agents (like Ajna) have their own browser tool via MCP — structured DOM interaction from within the OpenClaw framework | Agent-native, persistent sessions possible | Needs skill installation, untested |
| 3 | **Claude Desktop App as MCP** | Claude (Commander) can control the desktop app itself as an MCP server — Computer Use pattern | Anthropic-native, model-aware | Newer, less documented |
| 4 | **Playwright MCP** | Chromium-level DOM automation from Claude Code | DOM-aware, reliable selectors | Separate browser instance, no existing cookies |
| 5 | **Peekaboo** | macOS pixel-level UI automation | Controls ANY app | Fragile on web content, coordinate-dependent, element detection fails on browsers |

Peekaboo drops from PRIMARY to LAST RESORT. It's good for granting permissions in System Settings, clicking native macOS dialogs, and menu navigation — but for web automation, DOM-aware tools (OpenClaw browser MCP, Playwright, Claude Computer Use) are superior.

**Current state of the Sovereign browser gap** — these actions still require the Sovereign to open a browser:
1. Cancel Perplexity Pro subscription
2. Enroll xAI data sharing program
3. Register syncrescendence.com (Cloudflare)
4. Claim GCP $10/mo credits
5. Regenerate Slack app-level token (socket mode — bot token works)
6. Regenerate/verify Discord Ajna bot token (stale)
7. Manus API authentication (sk- key rejected as "malformed token")
8. ~~OpenClaw token refresh~~ SOLVED — `openclaw onboard --auth-choice token` works non-interactively

## What We Need You To Sense

**Q1 — The browser automation hierarchy: what's actually working in March 2026?**

We empirically tested Peekaboo and it's FRAGILE for web content (element detection fails, coordinate-clicking is pixel-dependent). The real question is now about the DOM-aware tiers:

1. **OpenClaw's browser MCP skills** — Ajna could have her own browser. What OpenClaw skills or MCP servers give an agent structured browser access? Is `agent-browser` the right skill despite VirusTotal flags, or are there alternatives? What does the browser session persistence story look like — cookie jars across agent restarts?

2. **Claude Computer Use / Claude Desktop as MCP** — Is this production-ready for solo builders in March 2026? The pattern is: Commander (Claude Code) controls the Claude Desktop app which has Computer Use. What are practitioners actually doing with this? Is Cowork the right entry point?

3. **Playwright MCP from Claude Code** — We have this connected but untested. Key question: can Playwright inherit the user's existing Chrome profile/cookies, or does it always launch a fresh Chromium? If fresh, every automation requires re-login, which defeats the purpose.

For each tier: who is using it, what's the failure mode, and what's the authentication story (fresh login vs persistent session)?

**Q2 — Service-specific automation paths (March 2026 reality)**

For each of our 7 remaining browser-gap items, what is the ACTUAL autonomous path?

| # | Action | What We Now Know | What We Still Need |
|---|--------|-----------------|-------------------|
| 1 | Cancel Perplexity Pro | No known API. We navigated to settings page via Peekaboo, can see "View details" link (likely Stripe portal). Coordinate click worked but element detection failed. | Is there a Stripe customer portal API? Can Playwright/OpenClaw browser hit the Stripe billing page directly? |
| 2 | xAI data sharing enrollment | Dashboard-only (console.x.ai) | What's the enrollment flow? API endpoint? |
| 3 | syncrescendence.com registration | Wrangler v4.69 installed, DNS yes | Has Cloudflare Registrar API or `wrangler` domain registration launched? |
| 4 | GCP credits claim | `gcloud` v542 installed, NO auth | After `gcloud auth login`, can credits be claimed via CLI? Or console-only? |
| 5 | Slack app token regen | **Bot token VALID**. App token stale (socket mode broken). | Can app-level tokens be rotated via Slack API? Or api.slack.com dashboard only? |
| 6 | Discord bot token regen | Token is 401 Unauthorized | Discord API for bot token reset — does it exist? Or developer portal only? |
| 7 | Manus API auth | sk- key rejected as "malformed token" | Correct auth format? Has docs.manus.im published the API spec? |

For EACH: (a) fully autonomous CLI/API path, (b) DOM-aware browser automation path (Playwright or OpenClaw browser MCP), (c) irreducible Sovereign gate (password, 2FA, CAPTCHA).

**Q3 — The OpenClaw browser MCP ecosystem**

This is the key question we didn't have before: OpenClaw agents can have their own browser via MCP skills. What exists RIGHT NOW for:
- Structured browser interaction (not pixel-hunting — actual DOM selectors)
- Persistent browser sessions (cookie jar across agent sessions)
- OAuth flow automation (redirect capture, token extraction)
- Dashboard navigation for services without APIs

ClawHub has 700+ skills. The `agent-browser` and `browser-automation` skills were flagged suspicious by VirusTotal — are these false positives, or are there cleaner alternatives? What MCP servers provide browser capability to OpenClaw agents?

**Q4 — The Docker question**

Our sandbox is OFF because Docker Desktop isn't installed on MBA. The neocorpus says sandbox mode `all` + Docker network isolation is the security baseline. But Docker Desktop on MBA means resource overhead.

What are power users doing on macOS for OpenClaw security without Docker? Is sandbox mode actually necessary for a single-operator, loopback-only deployment? What's the minimal security posture the community considers acceptable for personal use?

**Q5 — Ajna's capability surface: what should we outfit her with?**

Ajna is alive on Sonnet but has ZERO skills installed. Given our architecture (Ajna dispatches FROM OpenClaw to Commander and the wider constellation):
- What skills should Ajna have for the dispatch-FROM pattern?
- What skills give Ajna browser capability (the browser MCP question from Q3)?
- What's the minimal skill set that makes Ajna a force multiplier vs just a chat endpoint?
- What skills should we AVOID (token drains, security risks, redundant with Commander)?

Name specific ClawHub skills. "Install agent-dispatch" is useful; "install useful skills" is not.

## Constraints

- One Claude Max subscription (Commander) + OpenClaw on Anthropic token (Ajna = Sonnet)
- **Peekaboo 3.0-beta3**: Screen Recording GRANTED, works for macOS native UI, FRAGILE for web content (element detection fails on browser windows, coordinate clicking only)
- **Playwright MCP**: Connected to Commander, untested in production
- **OpenClaw browser MCP**: Not yet installed for Ajna — this is what we're asking about
- gcloud + wrangler installed but not yet authenticated
- Slack bot token VALID; app token and Discord token STALE
- No Docker Desktop on MBA
- Mac mini ANESTHETIZED — MBA only
- Tool stack LOCKED — no new subscriptions until April retool
- Factory test: must build artifacts, be agent-drivable, no vendor lock-in

## What I Want

The real-world practitioner playbook for closing the browser gap with DOM-aware tools — not pixel-hunting. We've proven Peekaboo is fragile for web automation. The question is now: OpenClaw browser MCP vs Playwright MCP vs Claude Computer Use — which one do solo builders actually use, and what does the persistent session story look like?

Specific commands. Specific skills. Specific failure modes. Who is doing this and what does their setup look like?

Exhaust your output tokens.
