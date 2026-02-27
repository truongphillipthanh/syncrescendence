---
url: https://x.com/Shpigford/status/2019743885942002144
author: "Josh Pigford (@Shpigford)"
captured_date: 2026-02-13
id: SOURCE-20260206-019
original_filename: "20260206-x_article-token_efficiency_in_openclaw_let_scripts_do_the_heavy_lifting-@shpigford.md"
status: triaged
platform: x
format: article
creator: shpigford
signal_tier: strategic
topics: [ai-agents, automation, best-practices, ai-engineering, tutorial]
teleology: implement
notebooklm_category: ai-agents
aliases: ["Shpigford - OpenClaw Token Efficiency"]
synopsis: "Demonstrates how to cut AI agent operational costs by replacing 'smart polling' with 'dumb scripts + smart triggers.' Shows real savings: 260+ empty Opus queue checks ($10-20 wasted) eliminated by moving deterministic logic to cron/bash scripts and reserving model invocations for genuine ambiguity. Introduces a three-tier model strategy (Opus for conversation, Sonnet for research, Haiku for browser automation at 5x cheaper)."
key_insights: ["Models are expensive thinkers, scripts are free doers — if a task can be expressed as deterministic logic (if X then Y), it belongs in a script not a model invocation", "Three-tier model strategy: Opus ($0.089/turn) for conversation, Sonnet for research, Haiku ($0.017/turn) for browser automation yields 5x cost reduction on identical work", "Scripts should output nothing on success — the model only wakes when there is something worth reporting, eliminating hundreds of empty 'HEARTBEAT_OK' invocations"]
---
# Token Efficiency in OpenClaw: Let Scripts Do the Heavy Lifting

(Description: Hero image showing a scorpion silhouette surrounded by orange and red flames against a dark rocky background, with dramatic fire effects)

Here's how I cut token costs by moving from "smart polling" to "dumb scripts + smart triggers".

## The Problem

When you first set up an AI assistant (OpenClaw, in my case), it's tempting to make it do everything. Check your email every hour. Monitor your print farm. Sync your bookmarks. Watch for errors.

But here's the math problem: if your agent wakes up every few minutes to "check on things," and each check burns tokens just to read context and decide "nothing happening" — you're spending real money on nothing.

I learned this the hard way, with the problem being magnified while I was building a "swarm" coding system. Looking back at my session logs:

- **260+ Swarm Dispatcher sessions** where Opus checked if there was work to do
- **315+ "Queue empty" responses** — each one burning $0.01-0.07 in tokens
- **8 consecutive HEARTBEAT_OK responses in 16 minutes** — all on the most expensive model

The Swarm dispatcher alone burned **$10-20 just checking empty queues**. Every two minutes, Opus woke up, loaded context, checked an endpoint, found nothing, and responded. Repeat 260+ times.

And that was just one feature I was building...not even accounting for all the other things I was having OpenClaw do.

## How Heartbeats Work

OpenClaw has a "heartbeat" system — a periodic poll (default every 30 minutes) that wakes your agent and asks "anything need attention?" The agent reads a HEARTBEAT.md file in your workspace, which lists tasks to check: emails, calendar, printer status, whatever you've configured.

The idea is good: your agent stays aware of the world without you manually asking. But every heartbeat is a full model invocation — context loading, reasoning, tool calls, response. Even if the answer is "nothing happening," you've paid for the model to figure that out.

## The Philosophy

**Models are expensive thinkers. Scripts are free doers.**

If a task can be expressed as deterministic logic ("if X, then Y"), it belongs in a script. Models should only engage when there's actual ambiguity — formatting for humans, deciding whether something is worth reporting, or handling edge cases that would be painful to code.

## The Three-Tier Model Strategy

Not all model work is equal. OpenClaw can/will use browsers a lot to find data or perform actions. But "browsing" itself doesn't need a fancy model. Here's what I measured when running the same browser task on different models:

- **Opus:** $0.089 per turn, ~$0.15+ per task
- **Haiku:** $0.017 per turn, ~$0.03 per task

**5x cheaper for identical work.**

This led to a tiered approach:

- **Premium (Opus)** — Main conversation, complex decisions
- **Workhorse (Sonnet 4.5)** — Research, writing, analysis
- **Cheap (Haiku 4.5)** — Browser automation, mechanical tasks

The key insight: **your main session should orchestrate, not execute**. When I need browser work done, I spawn a Haiku sub-agent. Research tasks get Sonnet. Opus stays focused on conversation.

One gotcha: model names matter. OpenClaw initially used `claude-3-5-haiku` instead of `claude-haiku-4-5`, which caused silent fallback to Opus. Always verify the model actually applied.

## The Cron + Script Pattern

**Before (Token-Heavy)**

Heartbeat → Model wakes → Reads HEARTBEAT.md → Figures out what to check → Runs commands → Interprets output → Decides action → Maybe reports

Every step burns tokens. The model is *thinking* about things that don't require thought.

**After (Token-Light)**

Cron fires → Script runs (zero tokens) → Script handles all logic → Only calls model if there's something to report → Model formats & sends

## Real Examples

### Swarm Dispatcher

- **Old way:** Opus cron job every 2 minutes checking dispatch queue, $0.01-0.07 per tick
- **New way:** Native code in hankOS checks the queue, only invokes model when work exists
- **Savings:** 260+ empty invocations eliminated = **$10-20 saved**

### Print Farm Monitoring

- **Old way:** Model checks printer status every 5 minutes, compares to last state, decides if alert needed
- **New way:** Bash script does the diff, only outputs if something changed
- **Savings:** ~50 model invocations/day → ~3

### Auth Watchdogs

- **Old way:** Model checks if API tokens are valid during every heartbeat
- **New way:** Script returns exit code 0 (valid) or 1 (invalid). Model only wakes on failure.
- **Savings:** Moved from every-heartbeat to 6-hour cron = **12x reduction in invocations**

### Browser Automation

- **Old way:** Opus doing the clicking, burning $0.089 per turn
- **New way:** Haiku sub-agent, $0.017 per turn
- **Savings:** **5x cost reduction**, plus 168k tokens isolated from main session context

## Implementation Tips

### 1. Write Scripts That Output Nothing on Success
```bash
#!/bin/bash
result=$(check_something)
if [ "$result" != "ok" ]; then
  echo "$result"
fi
```

Then your cron job prompt becomes: "Run the script. If there's output, send it to me. If not, stay silent."

### 2. Use delivery: "none" by default

Most cron jobs shouldn't announce themselves. Set delivery mode to none and have the agent explicitly send messages only when warranted.

### 3. Pre-Format in Scripts

Don't make the model format tables or summaries. Do it in the script:
```bash
echo "🏦 *Banking Summary*"
echo "• Checking: \\$$(get_balance checking)"
echo "• Savings: \\$$(get_balance savings)"
```

The model's job becomes "send this" — not "understand this data and present it nicely."

### 4. Isolated Sessions for Everything Scheduled

Every cron job should run in `sessionTarget: "isolated"`. This keeps your main session context clean and prevents scheduled tasks from polluting your conversation history.

### 5. Match Model to Task

In your cron job payloads, explicitly set the model:
```bash
{
  "payload": {
    "kind": "agentTurn",
    "message": "...",
    "model": "anthropic/claude-haiku-4-5"
  }
}
```

My X bookmark syncing process didn't need Opus.

## The Heartbeat's New Role

After optimizing, I realized my heartbeat could be nearly empty. Tasks I initially kept there — backup sync, dispatch queue checks — were still following the old pattern. They didn't need model judgment. So I moved them to cron:

- **Backup sync** — Every 30m, Haiku, silent unless failure
- **Mission Control Dispatcher** — Every 5m, Sonnet, spawns sub-agents if work exists

My HEARTBEAT.md is now just a fallback:
```markdown
# HEARTBEAT.md
Routine tasks have moved to cron jobs. Heartbeat is now reserved for:
- Edge cases requiring main session context
- Batched checks that benefit from correlation

If nothing needs attention, reply `HEARTBEAT_OK`.
```

Heartbeats still have a use case: **batched checks that benefit from shared context**. If you want your agent to check email, calendar, and weather in one turn and correlate them ("you have an outdoor meeting in an hour and rain is coming"), that's a heartbeat task.

But if your checks are independent? Cron jobs. Every time.

## Results

After migrating to this pattern:

- **Swarm empty-queue checks:** 260+ sessions costing $10-20 → 0 (native code)
- **Browser task cost:** $0.15+ per task → $0.03 per task
- **Auth check frequency:** Every heartbeat → Every 6 hours (12x reduction)
- **Heartbeat response:** Run checks then report → Instant HEARTBEAT_OK

The main session stays lean. Scheduled work runs isolated on cheaper models. Scripts handle the deterministic stuff for free.

## TL;DR

- **Scripts for logic, models for judgment** — if it can be an if statement, don't burn tokens on it
- **Tier your models** — Haiku for labor ($0.017/turn), Sonnet for craft, Opus for conversation ($0.089/turn)
- **Silent by default** — only invoke models when there's something to say
- **Isolated sessions** — scheduled work shouldn't pollute your main context
- **Verify model names** — a typo can silently fall back to expensive defaults

**Your AI assistant is a thinker, not a cron daemon.**

---

*Note: You should be able to just point OpenClaw to this article and say "Implement this" to make sure your own system is optimized.*

**Engagement:** 16 replies, 42 reposts, 433 likes, 1.2K bookmarks, 58.8K views  
**Posted:** 4:04 AM · Feb 6, 2026