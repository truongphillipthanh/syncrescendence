# How to Reduce OpenClaw Model Costs by up to 90% (Full Guide)
(Description: A beige-colored illustration showing a humanoid character in front of a computer monitor, with a toilet overflowing with papers and plants, and a money bag spilling coins. Text bubble reads "Task inefficiently. Costs add up medially here.")
## TLDR
This is the guide that's going to save you a lot of money if you're using OpenClaw (fka Clawdbot). In this article I will highlight:
- The problem: why OpenClaw by default burns money
- Model pricing comparisons and how to optimize
- Advanced strategies and setups to save even more
## The Problem: Why OpenClaw by Default Burns Money
(Description: Cartoon illustration with "Don't be this guy!" caption, showing wasteful token usage patterns with visual representations of money being wasted.)
Running OpenClaw with a single frontier model for all tasks is the number one cost mistake users make. This post above highlights the issue - you can easily run up a monthly Anthropic API bill in the $1000s even if you're just doing some basic stuff. Why? Because OpenClaw sends *everything* to your primary model by default. That means all heartbeats, sub-agent tasks, simple calendar lookups, web searches, etc. all go to your primary model by default. So if your primary is Opus 4.6, you're paying $5/$25 per million tokens for a heartbeat check that a $0.30 model could easily handle.
Additionally, OpenClaw's architecture compounds costs through several mechanisms:
- **Context accumulation:** Session history grows with every message. A mature session can reach 200K+ tokens, meaning even a simple follow-up question carries enormous context overhead
- **System prompt re-injection:** The SOUL.md, AGENTS.md, MEMORY.md, and skill descriptions (3,000–14,000 tokens) are re-sent with every API call
- **Tool output storage:** File listings, browser snapshots, and command outputs all get logged into session history and re-transmitted
- **Heartbeat overhead:** A heartbeat running every 30 minutes on Opus triggers 48 full-context API calls per day
- **Cron jobs:** Each cron trigger creates a fresh conversation with full context injection so 96 triggers/day at 15-minute intervals can cost $10–20/day on Opus alone
The good news: a well-configured multi-model setup can reduce monthly API costs by up to 90% while maintaining (or improving) output quality where it matters.
## Can I use My Claude Max Plan With OpenClaw?
This has become quite controversial. The short answer is no, it's against Anthropic's terms of service and there are reports of people getting banned for this so it appears they are enforcing it.
There are some people claiming workarounds but I've not tried them - personally I don't want to get banned as I love Anthropic products. If you want to get cute with it and try, just do so at your own risk. But if you want to optimize your setup without violating any service terms, this is your guide.
## Model Pricing - Let's Compare
You should have a good understanding of the different models and pricing. I'll make it easy for you and just list out it (note: data as of Feb 15, 2026)
(Description: A dark-themed pricing comparison table for Anthropic Claude Family models showing Claude Opus 4.6, Claude Opus 4.5, and other variants with input/output costs per million tokens and context windows.)
Even within just Anthropic, you can greatly optimize across models with different pricing tiers
(Description: A pricing comparison table showing OpenAI models including GPT-4o, GPT-4o Mini, and other variants with their respective costs and capabilities.)
OpenAI models offer a variety of options as well
(Description: A pricing comparison table for Google Gemini Family models including Gemini 2.0 Pro, Gemini 2.5 Flash, and Gemini Flash-Lite with their input/output token costs.)
Gemini models, especially 2.5 Flash, offer great value without sacrificing quality for certain workflows
(Description: A pricing comparison table for Open-Weight Challengers showing models like Kimi K2.5, MiniMax M2.5, DeepSeek V3.2, and others with their providers and token costs.)
The biggest bang for your buck comes from the latest versions of the open models such as Kimi K2.5 and the recently-released MiniMax M2.5
Now that we know the pricing, let's figure out how to optimize across them.
## Optimizing Your Setup With Intelligent Routing
The core principle for optimizing your model routing: match model capability to task complexity. OpenClaw supports per-function model assignment, so let's use it.
Below is a simple framework of common tasks and recommended models to use to drastically low your costs.
(Description: A white-background table with four tiers of task complexity. Tier 1: Heartbeat/Status - Background checks, keep-alive - Recommended Model: Gemini Flash-Lite, Haiku 4.5, or DeepSeek V3.2 - Cost Profile: $0.075-$1.00/MTok input. Tier 2: Simple Queries - Calendar, weather, file lookups - Recommended Model: Haiku 4.5, Craft 4.1 Fast, Kimi K2.5 - Cost Profile: $0.20-$1.00/MTok input. Tier 3: Standard Work - Coding, analysis, writing - Recommended Model: Sonnet 4.5, MiniMax M2.5, Kimi K2.5 - Cost Profile: $0.30-$3.00/MTok input. Tier 4: Complex Reasoning - Multi-step planning, critical decisions - Recommended Model: Opus 4.6 or Opus 4.5 - Cost Profile: $5.00/MTok input.)
Use lightweight rules like keywords, regex, intent classification, or even a cheap pre-router model to detect the task type, then forward the prompt to the chosen LLM via OpenClaw's configurable endpoints. This leverages OpenClaw's modular architecture, where skills and sessions can override the default model on-the-fly.
For example, if the task has the words "email triage" (which could be user prompted or part of a regular cron job), you can simply tell OpenClaw to use Haiku for this task. Getting started is straightforward - OpenClaw's config.yaml and skills system support this natively, with options for manual rules or automated routers. Start by classifying 2-3 task types, monitor via logs (see below), then expand to more.
```
openclaw logs --tail
```
## Building a Custom Routing Skill
If you want to go one step further, you can build a private skill for routing your common tasks to various LLM providers. See below for a sample Python "router.py" skill.
```python
import re
from openclaw import Skill, Context
class RouterSkill(Skill):
    def __init__(self):
        self.rules = {
            r'code|debug|script': 'openai/gpt-5.2-turbo',  # Coding
            r'email|schedule|remind': 'anthropic/claude-3-haiku-20240307',  # Routine
            r'plan|strategy|brainstorm': 'anthropic/claude-3-opus-20240229',  # Complex
            'default': 'google/gemini-flash-1.5'
        }
    async def execute(self, context: Context):
        prompt = context.message.content.lower()
        for pattern, model in self.rules.items():
            if isinstance(pattern, str) and re.search(pattern, prompt):
                context.llm_model = model  # Override for this session
                break
        # Proceed to default skill chain
        return await self.next(context)
```
Then once you've configured this, run:
```
openclaw skills enable router --path skills/router.py
```
You can get as complex as you want with this and don't let the code scare you off - just let Claude (or your model of choice) walk you through it. The main point here is to give it some rules so it doesn't treat all tokens as equal.
## Auto-Routing via OpenRouter (300+ Models, 1 API)
Another option is to use OpenRouter's built-in router which uses prompt analysis for hands-off decisions (albeit with a bit of latency).
This option is great if you don't want to mess with multiple model providers or setup complex routing skills. Just create a free account, fund it with some credits, update your OpenClaw config, then let OpenRouter handle the rest.
```yaml
llm:
  provider: openrouter
  routing:
    enabled: true
    rules:
      - task: "routine"  # Auto-detected via OpenRouter's classifier
        model: "deepseek/deepseek-chat"
        max_cost: 0.50  # $/M tokens
      - task: "coding"
        model: "openai/gpt-5.2-turbo"
      - fallback: "anthropic/claude-3-haiku-20240307"
```
## Routing with ClawRouter (OpenClaw Native Skill)
The hottest new tool in the OpenClaw ecosystem right now is ClawRouter with its 2.4k GitHub stars in 11 days.
ClawRouter is an alternative to OpenRouter and acts as a smart intermediary layer that sits between your application/agent and the LLM providers. Its main goal is to dramatically reduce inference costs while still delivering appropriate quality for each request.
How it works: ClawRouter analyzes each incoming query locally using a fast, lightweight classifier based on weighted scoring dimensions (things like query length, presence of code, reasoning markers, multi-step intent, tool usage signals, etc.). It classifies requests into tiers:
- **Simple** → cheap/fast models (e.g. DeepSeek, Gemini Flash, ~$0.27–0.60/M tokens)
- **Medium** → mid-tier (e.g. GPT-4o-mini)
- **Complex** → strong models (e.g. Claude Sonnet)
- **Heavy reasoning/agentic/multi-step** → frontier models (e.g. Opus 4.6, Kimi K2.5)
It then routes to the cheapest capable model for that complexity level.
It also supports multiple profiles: Auto (balanced), Eco (max savings, up to 95–100% on simple queries), Premium (best quality), Free (zero-cost models).
If you want a routing tool designed specifically for OpenClaw, this is the one.
## Optimizing via Prompt Caching
Prompt caching is one of the most underused optimizations for OpenClaw.
When you send a request to Claude or GPT, the model processes every token from scratch each time. Prompt caching lets the provider remember the static parts of your prompt, so you only pay full price once (or once every so often).
How it works: Anthropic and OpenAI cache parts of your prompt that don't change between requests. For OpenClaw, that means your SOUL.md, AGENTS.md, MEMORY.md, and system instructions get cached and reused across calls instead of being re-processed every time.
So with those 3,000-14,000 token system prompts being sent with every API call, with caching you only pay full price once. Then it's 90% cheaper for every subsequent hit within the cache TTL (5 minutes standard, up to 60+ minutes with extended retention).
Here's how you would set that up in your config:
```json
{
  "models": {
    "anthropic/claude-opus-4.6": {
      "cacheRetention": "long",
      "cacheSystemPrompts": true,
      "cacheThresholdTokens": 2048
    }
  }
}
```
Here's one example of prompt caching in action. Anthropic's extended cache stays warm for 55+ minutes. If you set your heartbeat interval to 55 minutes (instead of the default 30), every heartbeat hits warm cache and you get 90% off on all that system context.
Combined with routing heartbeats to Haiku, you're paying $0.30/MTok for the base model and then only $0.03M/Tok for cached system context - your heartbeats now cost ~$0.50/month instead of $100+
## Local Models via Ollama: Zero Marginal Cost
If you're running OpenClaw 24/7 with heavy automation, local models start to become economically compelling. Once you've paid for the hardware, every inference is free.
### When local models make sense:
- You have consistent, predictable load (not bursty)
- You need privacy (sensitive data that shouldn't hit external APIs)
- You're running high-volume, low-complexity tasks (data processing, classification, routine checks)
- You have spare compute (existing server, gaming PC that's idle during work hours)
### When local models don't make sense:
- You need frontier capabilities (extended reasoning, complex creative work, advanced coding)
- Your workload is bursty (you'd be paying for idle hardware)
- You don't want to manage infrastructure
Unless you're willing to shell out $14k for a decked out Mac Studio, you won't be able to run any of the latest models in the Opus 4.5 category, but with fairly inexpensive hardware you can run models that compare well with Sonnet 3.5.
(Description: A technical comparison chart showing local model performance metrics and hardware requirements, with visual indicators for recommended configurations.)
Qwen 3 32B seems to be the current choice for local OpenClaw deployments. It's competitive with Sonnet 3.5 on many tasks and runs at 40+ tokens/sec on a single 4090.
## Bottom Line
OpenClaw is an incredible tool, but the default config treats all tokens equally which can cost you a lot of money if you're not optimizing your setup.
90% of what your agent does is likely routine work that doesn't need a $5/MTok model. Route intelligently, cache aggressively, and use local models if it makes sense. You'll cut costs by 80–90% while getting better output quality on the stuff that actually matters.
The tools exist. The models exist. The only question is whether you're going to keep burning money or spend 30 minutes optimizing your setup.
Your wallet will thank you.
---
**Metadata:** Posted 3:42 AM · Feb 16, 2026 · 640.7K Views · 76 Replies · 225 Reposts · 2.2K Likes · 8.1K Bookmarks