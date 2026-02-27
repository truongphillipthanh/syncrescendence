---
url: https://x.com/pradeep24/status/2021319785947316490
author: "pradeep (@pradeep24)"
captured_date: 2026-02-10
id: SOURCE-20260210-005
original_filename: "20260210-x_article-camofox_browser_a_openclaw_browser_that_doesnt_get_blocked-@pradeep24.md"
status: triaged
platform: x
format: article
creator: pradeep24
signal_tier: tactical
topics:
  - ai-agents
  - ai-workflow
  - context-management
  - automation
  - api
  - product-development
  - cli-tools
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "camofoxbrowser  A openclaw browser that doesnt get blocked"
synopsis: "camofox-browser - A openclaw browser that doesn't get blocked **camofox-browser** is an OpenClaw plugin that lets your agents browse sites that normally block automation — X, Product Hunt, Amazon, and more. It was extracted from Jo, where it powers our server-side web browsing."
key_insights:
  - "WHAT GETS INTERCEPTED The patches follow a simple pattern: check config, return spoofed value if set, otherwise fall through to normal implementation."
  - "It was extracted from Jo, where it powers our server-side web browsing."
  - "It's a headless browser server built on Camoufox, a Firefox fork that spoofs browser fingerprints at the C++ level rather than in JavaScript."
---
# camofox-browser - A openclaw browser that doesn't get blocked

(Description: A red fox character with golden eyes, facing forward, with white chest markings. Text reads "camofox-browser / An OpenClaw browser that doesn't get blocked" with tagline "C++ anti-detection · element refs · search macros")

**camofox-browser** is an OpenClaw plugin that lets your agents browse sites that normally block automation — X, Product Hunt, Amazon, and more. It was extracted from Jo, where it powers our server-side web browsing.

It's a headless browser server built on Camoufox, a Firefox fork that spoofs browser fingerprints at the C++ level rather than in JavaScript. This gives it a higher probability of passing detection systems than standard headless browsers.

If your OpenClaw is on a Mac Mini, the built-in browser tool drives a real browser window that sites treat normally. On a VPS or remote server, you're stuck with headless Chrome or raw HTTP requests — both commonly blocked. Camofox solves that for remote servers, and is also faster than desktop browsing for agent workflows.

This post covers why that matters and how it works.

## OPENCLAW PLUGIN
```bash
openclaw plugins install @askjo/camofox-browser
```

Exposes tools: `camofox_create_tab`, `camofox_snapshot`, `camofox_click`, `camofox_type`, `camofox_navigate`, `camofox_scroll`, `camofox_screenshot`.

## THE PROBLEM WITH JAVASCRIPT-LEVEL EVASION

Playwright and Puppeteer work fine on cooperative sites. Point them at Google, Amazon, or anything behind Cloudflare, and the requests aren't rate-limited — they're rejected outright.

Detection systems fingerprint browsers across hundreds of dimensions: WebGL renderer strings, AudioContext sample rates, `navigator.hardwareConcurrency`, screen geometry, WebRTC IP leaks, battery API quirks, speech synthesis voices.

The standard fix is stealth plugins: patch `navigator.webdriver`, override a few properties. This works until the patch itself becomes a fingerprint signal — and against a serious detection stack, it will.

**The fundamental problem:** any property you override in JavaScript can be inspected in JavaScript. Property descriptors, prototype chains, and `function toString()` all leak the override.

## WHY C++ IS THE RIGHT LAYER

When JavaScript calls `navigator.hardwareConcurrency`, it's backed by a C++ implementation in Firefox. Override it in JS, and pages can detect the discrepancy — property descriptors look wrong, prototypes don't match, functions aren't native. Change the C++ return path, and JavaScript sees the spoofed value as if it's real.

From the Camoufox README:

> In Camoufox, data is intercepted at the C++ implementation level, making the changes undetectable through JavaScript inspection.

`camofox-browser` wraps this engine in a REST API designed for programmatic use.

## WHAT GETS INTERCEPTED

The patches follow a simple pattern: check config, return spoofed value if set, otherwise fall through to normal implementation. From `fingerprint-injection.patch`:
```c
double nsGlobalWindowInner::GetInnerWidth(ErrorResult& aError) {
  if (auto value = MaskConfig::GetDouble("window.innerWidth"))
    return value.value();
  FORWARD_TO_OUTER_OR_THROW(GetInnerWidthOuter, (aError), aError, 0);
}
```

This pattern covers window geometry, navigator fields, screen details, WebGL parameters (GPU fingerprints via [`webgl-spoofing.patch`](https://github.com/daijro/camoufox/blob/main/patches/webgl-spoofing.patch)), WebRTC IP masking ([`webrtc-ip-spoofing.patch`](https://github.com/daijro/camoufox/blob/main/patches/webrtc-ip-spoofing.patch)), audio fingerprints, geolocation with auto-approval, battery API, and speech synthesis voices.

Camoufox also includes Bézier curve-based mouse trajectories in [`MouseTrajectories.hpp`](https://github.com/daijro/camoufox/blob/main/additions/camoucfg/MouseTrajectories.hpp) — because detection systems increasingly grade *how* you interact, not just what you send.

All of this is intercepted in C++ before JavaScript ever sees it.

## WHY WE WRAPPED IT AS A SERVER

A Google results page is ~500KB of HTML. The accessibility tree for the same page is ~5KB. When the consumer is an LLM with a context window, that's a 100x reduction that matters.

So `camofox-browser` provides:

- **Accessibility snapshots** instead of HTML
- **Element refs** (e1, e2, e3) instead of brittle selectors
- **Macros** for common sites (@google_search, @youtube_search, @amazon_search)
```bash
# Create tab, get snapshot, click by ref
curl -X POST http://localhost:9377/tabs \\
  -d '{"userId": "agent1", "sessionKey": "task1", "url": "https://google.com"}'

curl "http://localhost:9377/tabs/TAB_ID/snapshot?userId=agent1"

curl -X POST http://localhost:9377/tabs/TAB_ID/click \\
  -d '{"userId": "agent1", "ref": "e3"}'
```

## PROXIES STILL MATTER

This remains the gnarliest piece of the puzzle. Most anti-bot systems check whether your IP is residential or datacenter, and datacenter ranges are well-catalogued. You can work around this with ISP or residential proxies, but it's janky infrastructure work. Camofox isn't always successful here, but your odds are better than raw Playwright.

We got around this in Jo by building a local Safari-powered stack through the macOS app — your real browser, your real IP, your real cookies. It works great, but the tradeoff is WebView-specific blocking. No silver bullet.

C++ spoofing handles browser identity, not IP identity. Most anti-bot systems correlate both: same fingerprint from 100 IPs looks weird; 100 fingerprints from one IP also looks weird. Rotate fingerprints with IPs, keep them stable within a session. Camoufox configures fingerprints per-session via environment variables, which maps well to isolated agent sessions.

## GETTING STARTED
```bash
npm install @askjo/camofox-browser

# or from source
git clone https://github.com/jo-inc/camofox-browser
cd camofox-browser && npm install && npm start

curl http://localhost:9377/health

# Create tab, get snapshot, click by ref
curl -X POST http://localhost:9377/tabs \\
  -d '{"userId": "agent1", "sessionKey": "task1", "url": "https://google.com"}'

curl "http://localhost:9377/tabs/TAB_ID/snapshot?userId=agent1"

curl -X POST http://localhost:9377/tabs/TAB_ID/click \\
  -d '{"userId": "agent1", "ref": "e3"}'
```

The repo is MIT-licensed and still early — there will be bugs. Contributions are welcome, and if you run into anything, [file an issue](https://github.com/jo-inc/camofox-browser/issues). We hope the OpenClaw community finds it useful.