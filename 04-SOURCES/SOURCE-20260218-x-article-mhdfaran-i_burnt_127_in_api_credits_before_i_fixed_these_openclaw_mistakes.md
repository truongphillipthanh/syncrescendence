---
url: https://x.com/mhdfaran/status/2024107207252713752
author: "Farhan (@mhdfaran)"
captured_date: 2026-02-18
id: SOURCE-20260218-013
original_filename: "20260218-x_article-i_burnt_127_in_api_credits_before_i_fixed_these_openclaw_mistakes-@mhdfaran.md"
status: triaged
platform: x
format: article
creator: mhdfaran
signal_tier: tactical
topics:
  - ai-agents
  - debugging
  - extended-thinking
  - api
  - startup
  - token-management
  - rules-files
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "I Burnt 127 in API Credits Before I Fixed These OpenClaw Mistakes"
synopsis: "I Burnt $127 in API Credits Before I Fixed These OpenClaw Mistakes Everyone on Twitter said OpenClaw would build my startup while I slept. Instead, I spent two weeks watching it burn through my API credits while it asked the same question eight times in a row. It wasn't thinking hard. It was stuck in a loop, and I was the idiot paying $0.03 per token to watch it spin."
key_insights:
  - "I Burnt $127 in API Credits Before I Fixed These OpenClaw Mistakes Everyone on Twitter said OpenClaw would build my startup while I slept."
  - "If you're currently babysitting your agent, watching it loop on simple tasks, or wondering if you should just go back to coding manually, I was there."
  - "It was fixing these specific, stupid mistakes."
---
# I Burnt $127 in API Credits Before I Fixed These OpenClaw Mistakes
(Description: A white background image featuring the article title in serif black text on the left side, with an illustration of a red cartoon ant character on the right side, rendered in a minimalist style.)
Everyone on Twitter said OpenClaw would build my startup while I slept. Instead, I spent two weeks watching it burn through my API credits while it asked the same question eight times in a row. It wasn't thinking hard. It was stuck in a loop, and I was the idiot paying $0.03 per token to watch it spin.
If you're currently babysitting your agent, watching it loop on simple tasks, or wondering if you should just go back to coding manually, I was there.
I almost gave up.
Now I have OpenClaw running my morning briefings and handling database chores without me touching it. The difference wasn't buying a better API tier. It was fixing these specific, stupid mistakes.
## Stop using your expensive model for everything
I had Claude Opus set as the default for every single task. Heartbeat checks, file scans, cron jobs—all of it. I was asking a Formula 1 car to deliver groceries.
OpenClaw lets you set up tiered model configs. I switched to using Haiku for routine stuff: file reads, syntax checks, "does this file exist" queries. Basically anything that needs speed, not reasoning. I kept Sonnet for actual coding and reserved Opus for when things broke twice or I needed complex debugging.
My daily token spend dropped from 40,000 to around 1,500. You can switch models mid-session with `/model` if you need to escalate, but most of the time, you don't.
## Your agent needs rules written in stone
Out of the box, OpenClaw will loop forever, forget what it was doing, and rewrite your database schema because it misread a comment. You have to parent this thing with explicit, paranoid instructions.
I keep a `workspace/skills/` folder full of `SKILL.md` files. These aren't suggestions. They're laws. One file is literally called `anti-loop.md` and says: "If you see the same error twice, stop and ask me. Do not try a third variation." Another forces the agent to check `USER.md` before asking questions.
Every assumption the agent makes is a potential landmine. OpenClaw doesn't know your database schema. It doesn't remember that you told it yesterday to never touch the auth module. Write it down. The agents that actually work are the ones with heavy custom instruction sets.
## Closing the chat kills the session
I told OpenClaw to optimize some queries and message me when done. Closed my laptop. Came back the next morning to find it had done nothing.
Sessions die when you close the chat. They're stateful only while the window is open. When you reopen, you might get a summary, but the context, the stack, the "where was I"—gone.
If you want actual background work, use OpenClaw's cron jobs with isolated session targets. These spin up fresh agent instances on a schedule, do one task, message you results, and die. For one-off tasks, I use a simple SQLite queue paired with a cron that checks it hourly.
Don't try to maintain long-running thinking sessions. They break, they cost money, and they hallucinate when context gets long.
## One working workflow beats five broken ones
I tried setting up email, calendar, Telegram, web scraping, and reporting all at once. Everything broke, and I couldn't tell which integration was failing.
Start with one thing that hurts slightly every day. I started with a morning briefing cron that reads my calendar and summarizes Slack mentions. I got that working end-to-end—running without me touching it, messaging me reliably, failing loudly instead of silently—before I added anything else.
Every new integration is a new failure mode. If things feel broken, run `openclaw doctor --fix`. Half the "my agent is stupid" complaints are actually "my config is borked" problems.
## Compaction eats your memories
OpenClaw has a context window. When it fills up, the system compacts older messages—which means it forgets stuff. I spent twenty minutes explaining my database schema once, then the agent compacted and hallucinated a new one. Almost dropped a production table.
Now I persist everything important:
- **State files** (JSON/YAML) for long-running task status
- **Workspace docs** (`USER.md` for context, `AGENTS.md` for behavior rules)
- **Decision logs** where I write down architectural choices so the agent reads them first next session
The less OpenClaw has to re-learn, the less it hallucinates.
## Chat quality and agent quality are different animals
I was using a model that gave beautiful, articulate chat responses. Great reasoning. But it couldn't call tools to save its life. It generated malformed JSON and hallucinated function names.
### Models that actually work for agentic coding:
- Claude Sonnet/Opus
- GPT-5.2
- Kimi K2 via API
### Models to avoid:
- **DeepSeek Reasoner.** Amazing at thinking, terrible at doing. It reasons beautifully about why your code is broken while generating completely broken tool calls.
- **GPT-5.1 Mini.** Cheap, but it skips steps and ignores tool results. Multiple people have called it useless for agent work.
Test your model with three sequential tool calls. If it can't handle that without hand-holding, don't use it for autonomous work.
## You're not bad at this. It's just early.
The gap between Twitter demos and daily use is real. When someone posts "my agent built a SaaS overnight," you're seeing the highlight reel. You're not seeing the three weeks they spent tuning prompts and debugging why OpenClaw kept trying to pay AWS with Monopoly money.
This stuff is genuinely hard right now. Not "you need a CS degree" hard. Just "the tools are immature" hard. The people making it work are treating these agents like orchestras, not autopilots.
Start with one cron job. Write one guardrail file. Use the cheap model. Save your state.
It gets easier. Don't give up before the compound interest kicks in.