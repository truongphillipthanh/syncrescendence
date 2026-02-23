---
url: https://x.com/gregisenberg/status/2024838731757224095
author: "GREG ISENBERG (@gregisenberg)"
captured_date: 2026-02-20
id: SOURCE-20260220-012
original_filename: "20260220-x_thread-things_i_wish_someone_told_me-@gregisenberg.md"
status: triaged
platform: x
format: thread
creator: gregisenberg
signal_tier: tactical
topics:
  - ai-agents
  - context-management
  - extended-thinking
  - gemini
  - cost-optimization
  - token-management
  - rules-files
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "Things I wish someone told me before I almost gave up on Ope"
synopsis: "Things I wish someone told me before I almost gave up on OpenClaw I've been in the same boat as a lot of people here spending the first two weeks babysitting, burning tokens, and watching my agent loop on the same answer eight times in a row. After a lot of trial and error I've got it running reliably and actually doing useful work. Here's what made the difference for me."
key_insights:
  - "Don't run everything through your best mode This is the single biggest mistake."
  - "Anti-looping rules, compaction summaries, task checking before asking your questions."
  - "YOU MUST RESEARCH YOURSELF and not assume the agent knows everything."
---
# Things I wish someone told me before I almost gave up on OpenClaw
(Description: Screenshot image from r/openclaw showing post titled "Things I wish someone told me before I almost gave up on OpenClaw" with a Tutorial/Guide tag)
I've been in the same boat as a lot of people here spending the first two weeks babysitting, burning tokens, and watching my agent loop on the same answer eight times in a row.
After a lot of trial and error I've got it running reliably and actually doing useful work. Here's what made the difference for me. This is all available in more detail with all the actual config examples, terminal commands, a model comparison table, and a common issues FAQ here if anyone wants the full version
## 1. Don't run everything through your best mode
This is the single biggest mistake. Heartbeats, cron checks, and routine tasks don't need Opus or Sonnet. Set up a tiered model config. Use a cheap model (Haiku, Gemini Flash, or even a local model via Ollama) as your primary for general tasks, and keep a stronger model as a fallback. Some people get a 40k token costs from 20-40k tokens down to like 1.5k just by routing smarter. You can switch models mid-session with /model too.
## 2. Your agent needs rules. A lot of them.
Out of the box OpenClaw is dumb. It will loop, repeat itself, forget context, and make weird decisions. You need to add guardrails to keep it in check. Create skills (SKILL.md files in your workspace/skills/ folder) that explicitly tell it how to behave. Anti-looping rules, compaction summaries, task checking before asking your questions. The agents that work well are the ones with heavily customised instruction sets. YOU MUST RESEARCH YOURSELF and not assume the agent knows everything. You are a conductor, so conduct.
## 3. "Work on this overnight" doesn't work the way you think
If you ask your agent to work on something and then close the chat, it forgets. Sessions are stateful only while open. For background work you need cron jobs with isolated session targets. This spins up independent agent sessions that run on a schedule and message you results. One-off deferred tasks need a queue (Notion, SQLite text file) paired with a cron that checks the queue.
## 4. Start with one thing working end-to-end
Don't try to set up email + calendar + Telegram + web scraping + cron jobs all at once. Every integration is a separate failure mode. Get one single workflow working perfectly like a morning briefing cron then add the next. Run openclaw doctor --fix if things are broken.
## 5. Save what works
Compaction loses context over time. Use state files, fill in your workspace docs (USER.md, AGENTS.md, HEARTBEAT.md), and store important decisions somewhere persistent. The less your agent has to re-learn, the better it performs.
## 6. The model matters more than anything
Most frustration comes from models that can't handle tool calls reliably. Chat quality ≠ agent quality. Claude Sonnet/Opus, GPT-5.2, and Kimi K2 via API handle tool calls well. Avoid DeepSeek Reasoner specifically (great reasoning, malformed tool calls). GPT-5.1 Mini is very cheap but multiple people here have called it "pretty useless" for agent work.
## 7. You're not bad at this. It's genuinely hard right now
OpenClaw is not a finished product. The people posting "my agent built a full app overnight" have spent weeks tuning. The gap between the demo and daily use is real. It's closing fast, but it's still there.
---
**Reply from GREG ISENBERG (Feb 20):**
i always tell em
---
**Reply from GREG ISENBERG (Feb 20):**
Yep - it's a struggle for sure