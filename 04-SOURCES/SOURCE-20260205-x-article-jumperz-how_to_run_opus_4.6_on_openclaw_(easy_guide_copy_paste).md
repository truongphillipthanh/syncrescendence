---
url: https://x.com/jumperz/status/2019531293726503358
author: "JUMPERZ (@jumperz)"
captured_date: 2026-02-05
id: SOURCE-20260205-010
original_filename: "20260205-x_article-how_to_run_opus_4.6_on_openclaw_(easy_guide_copy_paste)-@jumperz.md"
status: triaged
platform: x
format: article
creator: jumperz
signal_tier: tactical
topics:
  - ai-agents
  - context-management
  - testing
  - anthropic
  - api
  - cost-optimization
  - token-management
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "How to Run Opus 46 on OpenClaw Easy Guide Copy Paste"
synopsis: "How to Run Opus 4.6 on OpenClaw (Easy Guide, Copy Paste) Overview Opus 4.6 dropped today. OpenClaw hasn't updated yet. We patched the model catalog and it's already running. Copy / Paste into your terminal. Step 1: Find Your OpenClaw Install ```bash npm root -g ``` That gives you the path. Everything below is relative to it."
key_insights:
  - "Important Notes - npm update will overwrite the patches."
  - "If your session exceeds that and falls back, it will break Confirmation That's it, you should be on Opus 4.6 =========== You should see this after you hit `/status` or ask it to check the model."
  - "How to Run Opus 4.6 on OpenClaw (Easy Guide, Copy Paste) Overview Opus 4.6 dropped today."
---
# How to Run Opus 4.6 on OpenClaw (Easy Guide, Copy Paste)

(Description: Digital artwork featuring two gray stone/marble sculptured faces in profile facing each other, with glowing red numbers "4.6" displayed prominently in the center, on a black background.)

## Overview

Opus 4.6 dropped today. OpenClaw hasn't updated yet. We patched the model catalog and it's already running.

Copy / Paste into your terminal.

## Step 1: Find Your OpenClaw Install
```bash
npm root -g
```

That gives you the path. Everything below is relative to it.

## Step 2: Add Opus 4.6 to the Model Catalog

Open: `<npm-root>/openclaw/node_modules/@mariozechner/pi-ai/dist/models.generated.js`

Search for `"claude-opus-4-5"` under the anthropic provider and add this block right before it:
```javascript
"claude-opus-4-6": {
  id: "claude-opus-4-6",
  name: "Claude Opus 4.6 (latest)",
  api: "anthropic-messages",
  provider: "anthropic",
  baseUrl: "https://api.anthropic.com",
  reasoning: true,
  input: ["text", "image"],
  cost: { input: 5, output: 25, cacheRead: 0.5, cacheWrite: 6.25 },
  contextWindow: 1000000,
  maxTokens: 128000,
},
```

## Step 3: Add the Alias

Search your openclaw dist folder for the function `normalizeAnthropicModelId`. The file will be something like `model-selection-XXXXXXXX.js` (the hash changes between versions).
```bash
grep -rl "normalizeAnthropicModelId" $(npm root -g)/openclaw/dist/
```

Open that file and add this line before the opus-4.5 alias:
```javascript
if (lower === "opus-4.6") return "claude-opus-4-6";
```

## Step 4: Update Your Config

In `~/.openclaw/openclaw.json`:
```json
"model": { "primary": "anthropic/claude-opus-4-6" },
"models": { "anthropic/claude-opus-4-6": {} }
```

## Step 5: Verify + Restart
```bash
openclaw models list | grep opus
```

Should show `anthropic/claude-opus-4-6` as default. Restart your bot.

## All Steps Verified

Every step matches the guide exactly:

| Step | Guide says | What's live |
|------|-----------|-----------|
| 2 | Add claude-opus-4-6 to models.generated.js | Line 1282, 1M context, 128K max |
| 3 | Add opus-4.6 alias | Line 2494, before opus-4.5 |
| 4 | Set as primary in config | Line 12, primary + models block |
| 5 | openclaw models list shows it | text+image 977k default, configured |

Verified. Ship it.

## Important Notes

- npm update will overwrite the patches. Save them or re-apply after updates
- Once openclaw ships the official release (probably 2026.2.4) you won't need any of this
- Fallback models (opus 4.5, sonnet) only support 200K context. If your session exceeds that and falls back, it will break

## Confirmation

That's it, you should be on Opus 4.6

===========

You should see this after you hit `/status` or ask it to check the model.

(Description: Chat interface screenshot showing a dark theme with a checkmark emoji and text reading: "We're on it ✅" followed by model information showing "Model: anthropic/claude-opus-4-6", "Context: 121k / 1.0M (12%) — the 1M context window is active", "Compactions: 0", and "Running on Opus 4.6 confirmed. The 1M context window is live too 🔥")

---

**Engagement Metrics:** 11 replies, 9 reposts, 111 likes, 172 bookmarks, 11,914 views | Posted 1:59 PM · Feb 5, 2026