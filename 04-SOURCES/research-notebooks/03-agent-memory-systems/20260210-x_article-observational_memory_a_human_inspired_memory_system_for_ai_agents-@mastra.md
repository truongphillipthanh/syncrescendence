---
url: https://x.com/mastra/status/2021280193273336131
author: Mastra (@mastra)
captured_date: 2026-02-10T21:48:00Z
---

# Observational Memory: A Human-Inspired Memory System for AI Agents

(Description: A dark-themed promotional graphic with the Mastra logo and a stylized head profile containing neural/memory visualization. The title "Observational Memory" is displayed prominently in white text. A small profile avatar labeled "Tyler Barnes" appears in the corner.)

At Mastra, we just shipped a new type of memory for agentic systems: observational memory.

Observational memory is text-based (no vector/graph DB needed), SoTA on benchmarks like LongMemEval, and compatible with Anthropic/OpenAI/etc prompt caching.

Even better: our implementation is open-source.

## Compressing context to observations

If you step outside on a busy street, your brain processes millions of pixels, but distills down to one or two observations. That blue SUV just ran a red light. Your neighbor's pit bull is off their leash.

## How it works

Observational memory is designed to work the same way. In the context of a coding agent, it might compress a user session down to something like this:
```plaintext
Date: 2026-01-15
🔴 12:10 User is building a Next.js app with Supabase auth, due in 1 week (meaning January 22nd 2026)
🔴 12:10 App uses server components with client-side hydration
🟡 12:12 User asked about middleware configuration for protected routes
🔴 12:15 User stated the app name is "Acme Dashboard"
```

## Observations are log-based messages

The core message format resembles logs:

- **Formatted text, not structured objects.** Down with knowledge graphs. Roon was right. Text is the universal interface. It's easier to use, optimized for LLMs, and far easier to debug.

- **A three-date model** which we've seen perform better at temporal reasoning. This includes the observation date, referenced date, and relative date. Events are grouped by date with timestamps displayed inline.

- **Emoji-based prioritization.** We're essentially using emojis to reimplement log levels. 🔴 means important. 🟡 means maybe important. 🟢 means info only.

## Managing context: observations and raw messages

In observational memory, the context window is broken into two blocks.

The first block is the list of observations (like above). The second block is raw messages that haven't yet been compressed.

When new messages come in, they are appended to the end of the second block.

When it hits 30k tokens (the default threshold, though it's configurable), a separate "observer agent" compresses messages into new observations that are appended to the first block.

When observations hit 40k tokens (the default threshold, again configurable), a separate "reflector agent" garbage collects observations that don't matter.

Our token limit defaults are relatively conservative, providing SoTA results on benchmarks while staying well within context window limits.

This structure enables consistent prompt caching. Messages keep getting appended until the threshold is hit—full cache hits on every turn. When observation runs, messages are replaced with new observations appended to the existing observation block. The observation prefix stays consistent, so you still get a partial cache hit. Only during reflection (infrequent) is the entire cache invalidated.

## Results

Mastra's new memory system, Observational Memory, achieves 94.87% on LongMemEval with gpt-5-mini — over 3 points higher than any previously recorded score. With gpt-4o (the standard benchmark model), it scores 84.23%, beating the gpt-4o oracle (a configuration given only the conversations containing the answer) by 2 points, and the previous gpt-4o SOTA from Supermemory by 2.6 points.

These scores were achieved with a completely stable context window. The context is predictable, reproducible, and fully prompt-cacheable. See the full research breakdown.

(Description: A benchmark comparison table with three columns—System, Model, and LongMemEval score. The table shows multiple memory systems and their performance across different models. Key entries include: Mastra OM with gpt-5-mini at 94.87%, Mastra OM with gemini-3-pro-preview at 93.27%, Hindsight with gemini-3-pro-preview at 91.40%, Mastra OM with gemini-3-flash-preview at 89.20%, Hindsight with GPT-OSS 120B at 89.00%, EmergenceMem Internal with gpt-4o at 86.00%, Supermemory with gemini-3-pro-preview at 85.20%, and Mastra OM with gpt-4o at 84.23%. All entries in the table are visible.)

* EmergenceMem's 86.00% is reported for an "Internal" configuration and is not publicly reproducible. Both EmergenceMem and Hindsight use multi-stage retrieval and neural reranking; OM uses a single pass with a stable context window.

Full per-category breakdowns and methodology are in the research page.

## Mastra's New Memory System

I've been working on memory at Mastra for the last year. We shipped working memory and semantic recall in March and April before "context engineering" was a thing.

Working memory provided moderate lifts to benchmarks and was cacheable, while semantic recall provided larger lifts but was not.

Then context engineering became a thing. We noticed that a lot of our users were getting their whole context windows blown up by tool call results. Other users brought up wanting to aggressively cache using Anthropic, OpenAI, and other providers to reduce token costs.

This problem was compounded with newer types of parallelizable agents that generate huge amounts of context very quickly. Browser agents using Playwright and screenshotting pages. Coding agents scanning files and executing commands. Deep research agents browsing multiple URLs in parallel.

In some ways observational memory is the child of working memory and semantic recall. We're considering this the new primary Mastra memory system and encouraging users to migrate over.

## Current limitations

Observation currently runs synchronously — when the token threshold is hit, the conversation blocks while the Observer processes messages. We've solved this with an async background buffering mode that runs observation outside the conversation loop and we're shipping it this week.

## Get started now
```typescript
import { Memory } from "@mastra/memory";
import { Agent } from "@mastra/core/agent";

export const agent = new Agent({
  name: "om-agent",
  instructions: "You are a helpful assistant.",
  model: "openai/gpt-5-mini",
  memory: new Memory({
    options: {
      observationalMemory: true,
    },
  }),
});
```

- [Read the docs](https://mastra.ai/docs/memory/observational-memory)
- [Read the research](https://mastra.ai/research/observational-memory)
- [View the benchmark](https://github.com/mastra-ai/mastra/tree/main/explorations/longmemeval)

---

**Engagement Metrics:**
- 18 replies
- 51 reposts
- 429 likes
- 824 bookmarks
- 108,403 views
- Posted: 9:48 AM · Feb 10, 2026