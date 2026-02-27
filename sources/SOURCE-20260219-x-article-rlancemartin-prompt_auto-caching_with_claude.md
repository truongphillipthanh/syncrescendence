---
url: https://x.com/RLanceMartin/status/2024573404888911886
author: "Lance Martin (@RLanceMartin)"
captured_date: 2026-02-21
id: SOURCE-20260219-013
original_filename: "20260219-x_article-prompt_auto-caching_with_claude-@rlancemartin.md"
status: triaged
platform: x
format: article
creator: rlancemartin
signal_tier: tactical
topics:
  - claude-code
  - prompting
  - context-management
  - api
  - product-development
  - cost-optimization
  - token-management
teleology: implement
notebooklm_category: claude-code
aliases:
  - "Prompt autocaching with Claude"
synopsis: "Prompt auto-caching with Claude TL;DR Prompt caching is a great way to save cost + latency when using Claude. Input tokens that use the prompt cache are 10% the cost of non-cached tokens. Auto-caching was just added to the API, which makes it easier to cache your prompt with a single `cache_control` parameter in the API request."
key_insights:
  - "[@peakji]( from Manus called out the cache hit rate as [the single most important metric]( for a production AI agent."
  - "[@trq212]( has noted that prompt caching is [critical for long running / token-heavy agents like Claude Code]( dated Dec 24, 2025, replying to @irl_danB."
  - "Inference libraries / frameworks like [vLLM]( and [SGLang]( use different approaches to achieve this central idea."
---
# Prompt auto-caching with Claude
## TL;DR
Prompt caching is a great way to save cost + latency when using Claude. Input tokens that use the prompt cache are 10% the cost of non-cached tokens. Auto-caching was just added to the API, which makes it easier to cache your prompt with a single `cache_control` parameter in the API request. Also, check out [@trq212's deep dive](https://x.com/trq212/status/2024574133011673516) on Claude Code's use of prompt caching and useful tips for cache-friendly prompt design.
### Example API Request
```json
{
  "cache_control": {"type": "ephemeral"},
  "messages": [
    {"role": "user", "content": "A"},
    {"role": "assistant", "content": "B"},
    {"role": "user", "content": "C"}
  ]
}
```
(Description: Diagram showing cache flow from initial request through cache lookup to Claude API response, with labeled boxes for "Old Context," "New" content blocks, cache storage, and the Claude endpoint.)
## The case for caching
Many AI applications ingest the same context across turns. For example, agents [perform actions in a loop](https://www.anthropic.com/engineering/building-effective-agents). Each action produces new context. [Claude's messages API](https://platform.claude.com/docs/en/api/overview#available-apis) is stateless, which means it doesn't remember past actions. The agent harness needs to package new context with past actions, tool descriptions, and general instructions at each turn.
This means most of the context is the same across turns. But, without caching, you pay for the entire context window every turn. Why not just re-use the shared context? That's what prompt caching does. You can see on [the pricing page](https://platform.claude.com/docs/en/about-claude/pricing) that cached tokens are 10% the cost of base input tokens. With caching, you only pay in full for each new context block once.
[@peakji](https://x.com/@peakji) from Manus called out the cache hit rate as [the single most important metric](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) for a production AI agent. [@trq212](https://x.com/@trq212) has noted that prompt caching is [critical for long running / token-heavy agents like Claude Code](https://x.com/trq212/status/2004026126889320668).
(Description: Tweet from Thariq (@trq212) dated Dec 24, 2025, replying to @irl_danB. Text reads: "Excited to see what you build but just FYI most context management and compaction techniques are limited by prompt caching. Coding agents would be cost prohibitive if they didn't maintain the prompt cache between turns. And it's very easy to break the cache when doing more...")
## How it works
There are some great resources (e.g., [here from @sankalp](https://sankalp.bearblog.dev/how-prompt-caching-works/) or [here from @kipply](https://kipp.ly/transformer-inference-arithmetic/#kv-cache:~:text=e12-,Flops%20vs%20Memory%20Boundedness,-Flops%20vs%20memory)) on the details of LLM inference and caching. In general, LLM inference pipelines typically use a prefill phase that processes the prompt and a decode phase that generates output tokens.
(Description: Diagram illustrating the caching mechanism with a "Breakpoint" marker showing how content flows through to "Find cache hits" and then to the "Cache" and "Claude" endpoints, with "Old Context" and "New" content boxes.)
The intuition behind caching is that the prefill computation can be performed once, saved (e.g., cached), and then re-used if (part of) a future prompt is identical. Inference libraries / frameworks like [vLLM](https://arxiv.org/pdf/2309.06180) and [SGLang](https://lmsys.org/blog/2024-01-17-sglang/) use different approaches to achieve this central idea.
## Usage with Claude
Caching with the Claude messages API uses a `cache_control` [breakpoint](https://platform.claude.com/cookbook/misc-prompt-caching), which can be [placed at any block in your prompt](https://platform.claude.com/docs/en/api/python/messages/create). This tells Claude two things.
First, it is a "write point" telling Claude to cache all blocks up to and including this one. This creates a cryptographic hash of all the content blocks up to that breakpoint. This is scoped to your [workspace](https://platform.claude.com/docs/en/build-with-claude/workspaces).
### Example: Cache Write Point
```json
{
  "messages": [
    {"role": "user", "content": "A"},
    {"role": "assistant", "content": "B"},
    {"role": "user", "content": "C", "cache_control": {"type": "ephemeral"}}
  ]
}
```
(Description: Diagram showing message progression with a "Breakpoint" marker indicating where the cache write point is positioned within the message sequence.)
Second, it tells Claude to search backward at most 20 blocks from the breakpoint to find any prior cache write matches ("hits"). The hash requires identical content. One character difference will produce a different hash and a cache miss. If there's a match, the cache is used in prefill.
Still, there are challenges with caching. For turn-based apps (e.g., agents), you have to move the breakpoint to the latest block as the conversation progresses. The API now addresses this with auto-caching. You can place a single `cache_control` parameter in your request to the Claude messages API.
### Example: Auto-Caching Parameter
```json
{
  "cache_control": {"type": "ephemeral"},
  "messages": [
    {"role": "user", "content": "A"},
    {"role": "assistant", "content": "B"},
    {"role": "user", "content": "C"}
  ]
}
```
With auto-caching, the cache breakpoint moves to the last cacheable block in your request. As your conversation grows, the breakpoint moves with it automatically. This still works with block-level caching if you want to set breakpoints (e.g., on your system prompt or other context blocks).
Another challenge is designing your prompt to maximize cache hits. For example, if you edit the history you risk breaking the cache.
This is a problem that we've tackled with Claude Code! [@trq212](https://x.com/@trq212) just [shared a number of useful insights](https://x.com/trq212/status/2024543492064882688) on prompt design with caching in mind.
(Description: Diagram showing system prompt layout and caching strategy with multiple rows labeled "System," "Action 1," "Observation 1," "Action 2," "Observation 2," etc., showing how content blocks are organized with cache boundaries marked in dashed green and red lines.)
(Description: Screenshot of a system prompt layout table showing cache states for different components: "Base System Instructions" (globally cached), "Tools (Read, Write, Bash, Grep, Clsh...)" (globally cached), "CLAUDE.md & Memory" (cached per project), "Session State (env, MCP, output style)" (cached per session), and "Messages (user messages, tool results...)" (green each turn).)
(Description: Embedded tweet from Thariq (@trq212) dated Feb 19, with article title "Lessons from Building Claude Code: Prompt Caching Is Everything." Article preview text reads: "It is often said in engineering that 'Cache Rules Everything Around Me', and the same rule holds for agents. Long running agentic products like Claude Code are made feasible by prompt caching which...")
---
**Article Statistics:**
- Posted: 11:54 AM · Feb 19, 2026
- Views: 547.8K
- Replies: 20
- Reposts: 107
- Likes: 1,010
- Bookmarks: 2.5K