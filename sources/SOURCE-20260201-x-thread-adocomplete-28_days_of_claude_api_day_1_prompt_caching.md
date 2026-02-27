---
url: https://x.com/adocomplete/status/2018041429361320443
author: "Ado (@adocomplete)"
captured_date: 2026-02-01
id: SOURCE-20260201-007
original_filename: "20260201-x_thread-28_days_of_claude_api_day_1_prompt_caching-@adocomplete.md"
status: triaged
platform: x
format: thread
creator: adocomplete
signal_tier: tactical
topics:
  - ai-engineering
  - claude-code
  - developer-tools
teleology: extract
notebooklm_category: ai-engineering
aliases:
  - "Ado - Claude API prompt caching day 1"
synopsis: "Day 1 of a 28-day Claude API tutorial series covering prompt caching: add cache_control with type 'ephemeral' to get up to 90% off cached reads and 85% faster responses. Notes minimum cacheable prompt length varies by model."
key_insights:
  - "Adding cache_control: {type: 'ephemeral'} to repeated prompts yields up to 90% cost reduction and 85% faster responses."
  - "Each Claude model has a minimum cacheable prompt length threshold that must be met for caching to activate."
  - "Prompt caching is the single highest-ROI optimization for applications that send similar prompts repeatedly."
---
# 28 Days of Claude API - Day 1 - Prompt Caching

Sending the same prompt over and over again?

Add `"cache_control": {"type": "ephemeral"}` and get up to **90% off cached reads** and **85% faster responses**.

Note: each model has a min cacheable prompt length.

One line. Massive savings.

(Description: IDE screenshot showing JavaScript/TypeScript code with Claude API integration. The code demonstrates cache control implementation with noCacheInputCost and cachedInputCost variables, showing price comparisons with and without caching. Key visible lines include cache_control configuration, cost calculations using PRICE.input and PRICE.cache_read values, and console logging comparing "No Cache:", "Cached:", and "Savings:" metrics. The example shows pricing per million tokens with cache_write: 3.75, cache_read: 0.30, output: 15.)

---

The minimum cacheable prompt length is:

- 4096 tokens for Opus 4.5 and Haiku 4.5
- 1024 tokens for Sonnet 4.5, Sonnet 4, Opus 4.1, Opus 4

Learn more: [Prompt caching - Claude API Docs](https://platform.claude.com)

---

Ha yeah. One line makes such a big difference. Especially if you have a beefy system prompt.