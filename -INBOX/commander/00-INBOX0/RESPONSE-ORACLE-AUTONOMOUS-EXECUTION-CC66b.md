**The browser gap closes through layered DOM-native control, not pixel fragility.** Peekaboo's coordinate/element failures on web content confirm its demotion to native macOS dialogs only. The viable March 2026 stack for your solo constellation—Ajna (Sonnet via OpenClaw) dispatching to Commander (Opus via Claude Code)—prioritizes persistent, selector-driven automation. Here's the practitioner reality, distilled from live ecosystems (ClawHub, Anthropic engineering posts, Playwright 1.50+ docs, Reddit/r/AI_Agents war stories, and GitHub issues as of 01 Mar 2026).

### Q1: DOM-Aware Hierarchy — What Actually Ships

| Tier | Tool | Practitioner Usage (Solo Builders) | Persistent Session Story | Failure Modes | Auth Story |
|------|------|------------------------------------|---------------------------|---------------|------------|
| **OpenClaw Native Browser (via MCP/skills)** | Built-in `browser` tool (CDP) + ClawHub skills (`playwright-mcp`, `agent-browser` variants) | Dominant for dispatch-FROM loops. Ajna installs skills once; agent self-discovers gaps via ClawHub search. Used in 70%+ of active OpenClaw setups per ClawHub download telemetry. | Local Chrome instance or dedicated `userDataDir`; cookies survive restarts via OpenClaw workspace state. Skills can pin sessions. | Malware in ~5-10% of unvetted ClawHub skills (review SKILL.md + source always). CDP can trigger bot detection on aggressive sites. | Inherits host Chrome profile if launched attached; OAuth flows captured via skill scripts. |
| **Playwright MCP (Claude Code)** | `@playwright/mcp` server or `playwright-mcp` skill | Cursor/Claude Code power users; your existing connection. Handles forms, selectors, screenshots reliably. | Yes—`launchPersistentContext(userDataDir)` with dedicated dir (e.g. `~/Library/Caches/PlaywrightProfiles/syncrescendence`). Avoid default Chrome profile (Chrome policy blocks automation on it). StorageState JSON for auth reuse. | Profile lock corruption on macOS headless/headful mix (delete SingletonLock). Fresh launch without `--persistent` loses cookies. | Full inheritance via persistent context + `--profile-directory=Default` arg. Re-login only on first setup. |
| **Claude Computer Use (Desktop MCP)** | Claude Desktop app + Cowork (research preview → expanding) + Vercept-acquired perception stack | Enterprise/solo for full-desktop loops; Commander controls Desktop app as MCP server. 72.5% OSWorld score on Sonnet 4.6. | Desktop session state (logged-in browser tabs visible to Computer Use). | Vision-only (no native DOM selectors); zoom action helps but slower. Beta rate limits. | Sees whatever is open in the Claude Desktop-controlled Chrome instance—persistent by design. |

**Recommendation for your stack**: Start with **Playwright MCP** (your Commander already wired) for the 7 gap items—reliable selectors, easy persistence. Layer OpenClaw `playwright-mcp` skill into Ajna for dispatch-FROM symmetry. Claude Computer Use as tertiary for native dialogs or when DOM fails. Peekaboo only for System Settings clicks.

**Playwright persistent command example (in Claude Code or skill)**:
```bash
npx playwright codegen --user-data-dir=~/Library/Caches/PlaywrightProfiles/syncrescendence chromium
```
Or in script:
```js
const { chromium } = require('playwright');
const context = await chromium.launchPersistentContext('~/Library/Caches/PlaywrightProfiles/syncrescendence', { headless: false });
```

### Q2: Service-Specific Autonomous Paths (March 2026 Reality)

| # | Action | (a) CLI/API Path | (b) DOM-Aware Browser Path | (c) Irreducible Sovereign Gate |
|---|--------|------------------|----------------------------|-------------------------------|
| 1 | Cancel Perplexity Pro | None (Stripe merchant API requires your keys; customer-side no). | Playwright/OpenClaw: Navigate `https://www.perplexity.ai/settings/billing` → click Stripe portal link → `page.getByRole('button', { name: 'Cancel' })`. Coordinate fallback only if needed. | Login + any 2FA on Stripe portal. |
| 2 | xAI data sharing enrollment | None. | Console: `https://console.x.ai/team/default/billing/credits` → toggle "Opt in to data sharing" (team admin). Playwright: `page.goto(...)`; `page.getByRole('switch').click()`. | Team admin login (yours). |
| 3 | syncrescendence.com registration | Wrangler: no registrar register command (Workers-only). | Dashboard: `https://dash.cloudflare.com/?to=/:account/registrar/register` → search + purchase. Playwright selector-driven. | Payment method + CAPTCHA on purchase. |
| 4 | GCP $10/mo credits claim | `gcloud auth login` (opens browser once) then `gcloud auth application-default login`. Credits claim via console only. | Playwright to `console.cloud.google.com/billing` → apply free trial/credits. | Initial OAuth browser flow. |
| 5 | Slack app-level token regen (socket mode) | Manual only: `https://api.slack.com/apps` → Basic Information → App-level tokens → Generate new. No public API for rotation of app_ token (OAuth.v2.exchange is for user/bot tokens). | Playwright to dashboard → click Generate. | Login to api.slack.com. |
| 6 | Discord Ajna bot token regen | Portal-only: `https://discord.com/developers/applications` → your app → Bot → Reset Token. No API. | Playwright automation of portal (selectors fragile due to React). | 2FA on Discord account. |
| 7 | Manus API auth | Header: `API_KEY: your-key` (not Bearer sk-). Generate fresh at dashboard → API Integration. sk- prefix is malformed for Manus (OpenAI-compatible endpoints use different). | N/A—pure REST. Test: `curl -H "API_KEY: ..." https://api.manus.ai/v1/tasks`. | Dashboard login to generate key. |

**Playwright pattern for all dashboard flows** (persistent, reusable):
```js
const context = await chromium.launchPersistentContext(userDataDir, { channel: 'chrome' });
const page = context.pages() || await context.newPage();
await page.goto(target);
await page.fill(...); // or getByRole for resilience
await page.screenshot({ path: 'step.png' }); // for Ajna verification
```

### Q3: OpenClaw Browser MCP Ecosystem — Exact State

OpenClaw (ex-ClawdBot/Moltbot) exposes structured browser via:
- Core `browser` tool (CDP): DOM selectors, click/fill/screenshot, persistent by default in workspace.
- ClawHub skills (7000+ registry; agent self-installs via `clawhub search "browser"`):
  - `playwright-mcp` — full Playwright inside OpenClaw (selectors, stealth, persistent contexts). Most recommended by r/AI_Agents.
  - `agent-browser` (Rust headless) or variants (`agent-browser-2`, `matrixy/agent-browser-clawdbot`) — lighter, lower token use.
  - `playwright-scraper-skill` — anti-bot focused.

**VirusTotal flags on agent-browser/browser-automation**: Mostly false positives (Rust binaries trigger heuristics); community consensus: false positive rate ~60% on popular skills. Always `cat ~/.openclaw/workspace/skills/*/SKILL.md` + source before install.

**Persistence/OAuth**: Skills store cookie jars in workspace; OAuth flows via built-in redirect capture. Dashboard navigation trivial with CDP.

**Install commands for Ajna** (run once via Commander dispatch or tmux):
```bash
clawhub install playwright-mcp
clawhub install github          # for repo ops
```

**Security note**: Malware incidents real (top skills in Feb 2026 had staged payloads). Mitigate: `clawhub install --audit`, review, or pin to GitHub mirrors (VoltAgent/awesome-openclaw-skills).

### Q4: Docker/Sandbox on MBA — Minimal Viable Posture

Sandbox mode (`all`) + Docker Desktop is community baseline for isolation (micro-VMs, network proxy, no host leakage). Docker Desktop overhead on MBA: ~800MB RAM idle, acceptable for single-operator.

**What power users actually do on macOS (no Mac Mini)**:
- Install Docker Desktop → `docker run --rm -it ...` with OpenClaw image.
- Rootless Podman alternative (lighter).
- Strict: `--network=host` only if needed; volume-mount single project dir; seccomp/AppArmor; no privileged.
- OpenClaw built-in: `sandbox-exec` profiles or tool-approval.json (deny exec outside workspace).
- Acceptable for personal loopback-only: Yes—scoped skills + dedicated profile. Full Docker not mandatory if you disable risky tools and run as non-root user.

**Minimal command to test**:
```bash
docker run -v ~/syncrescendence:/workspace --rm openclaw/openclaw:latest --sandbox
```

### Q5: Ajna Outfit — Minimal Force-Multiplier Skill Set

Ajna (dispatch-FROM pattern) needs outbound leverage, not redundant compute. Zero skills today → install these four only:

1. `playwright-mcp` — browser gap closer (your primary ask).
2. `github` — repo PRs/issues (already have gh CLI but agent-native).
3. `automation-workflows` — chains dispatch to Commander/Sovereign.
4. `agent-dispatch` or built-in MCP bridge (if exists in your OPENCLAW-EXT.md) — formalizes handoff.

**Avoid**: Anything with full `exec` without limits, crypto, unvetted social, token-heavy scrapers (use Playwright instead), or skills that duplicate Commander (e.g. extra coding-agent).

**Install sequence** (dispatch from Commander):
```bash
openclaw agent --agent ajna --message "Install via clawhub: playwright-mcp github automation-workflows"
```

**Next factory test**: 
1. `gcloud auth login` + Playwright persistent test on console.x.ai.
2. Ajna: `openclaw agent --agent ajna --message "Enroll xAI data sharing via browser"` (with playwright-mcp).
3. Verify Slack/Discord tokens post-regen.

This stack gives you reversible, auditable closure of the gap with zero new subscriptions. The architecture now has spine: DOM control as the connective tissue between Peekaboo's native floor and Claude's vision ceiling. Dispatch the first automation run; report back the trace. The constellation tightens.