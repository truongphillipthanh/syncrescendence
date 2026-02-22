---
url: https://x.com/DhravyaShah/status/2016308406701981731
author: "Dhravya Shah (@DhravyaShah)"
captured_date: 2026-01-27
id: SOURCE-20260128-002
original_filename: "20260128-x_article-clawd_molt_bot_memory_sucks_we_gave_it_supermemory-@dhravyashah.md"
status: triaged
platform: x
format: article
creator: dhravyashah
signal_tier: tactical
topics:
  - ai-agents
  - developer-tools
teleology: extract
notebooklm_category: ai-agents
aliases:
  - "Dhravya Shah - Supermemory for Clawdbot"
synopsis: "Supermemory founder Dhravya Shah diagnoses Clawdbot's memory problem: it relies on tool-calling for memory access but models aren't trained to consistently use tools. The fix integrates Supermemory for automatic recall at all times, cross-platform context sync (Telegram/WhatsApp/Slack), plus /remember and /recall commands."
key_insights:
  - "Clawdbot's memory architecture fails because LLMs aren't trained to proactively use memory tools — memory must be fed into context on every run, not gated behind tool calls."
  - "Cross-platform memory sync (Telegram, WhatsApp, Slack) via Supermemory integration enables seamless context continuity across messaging platforms."
  - "The fundamental insight from Anthropic: post-training with specific tools doesn't generalize — being good at file reading doesn't make the model good at using the filesystem for memory."
---
# Clawd / Molt bot's memory SUCKS. We gave it supermemory.

(Description: Brand collaboration graphic with Supermemory logo on left and red lobster illustration on right against gradient blue background)

I'm the founder of supermemory. Clawd/Molt bot is blowing up right now, with many, many use cases. I set it up, too, and have been using it through telegram.

## TLDR

Just go to https://supermemory.ai/docs/integrations/clawdbot to set up supermemory for your clawd bot.

## The Problem

However, me and some other friends of mine noticed that it's memory is really bad. It almost feels like... it _never_ wants to utilize it's memory to answer questions.

(Description: WhatsApp conversation screenshot. User message: "bro do you ever think to look at your memory for the token? 2:23 PM ✓". Bot response: "[Clawd] You're right. My bad — it was literally in my memory. 2:23 PM ✓")

Screenshot sent by a friend and enthusiast of clawd bot

For such a big and successful project, this sucks. but why? We instantly got to work...

@manthanguptaa did an awesome job breaking down their architecture - https://x.com/manthanguptaa/status/2015780646770323543 and from that, we know that it heavily relies on **tools** to reference memory.

### The problem with tools - The models aren't trained to use them all the time.

(Description: Multi-message explanation discussing tool usage training limitations. Content includes: "Yup. I honestly think people would pay real $$$ for Clawdbot memory that works. These are people who are buying $600 computers. I asked anthropic about this once, they do post training with only the tools at hand and the agent doesn't generalize well on tool calling. Eg. if it becomes good at reading a file doesn't necessarily mean it will also get better at using file system for memory. I had similar issue with formal tools, i had to abstract those tools behind something it already knows how to use (LSP) to trick it into using it more")

Memory needs to be something that the model can access any time, it should just be fed into the model on every run. However, the current architecture of Molt won't work at all because of this poor memory.

## The fix.

We integrated clawd bot with supermemory - with:

- Automatic recall at all time
- Tools to manually search, forget, get profile, etc.
- /remember and /recall commands

So now, you _always_ know that your clawd bot will have perfect memory.

Now, i can have extremely long conversations with Molt, switch from telegram to whatsapp to slack, and it has all the context about me, synced with supermemory.

This feels magical. You should try it.

## Learn More

If you want to learn more about supermemory, just read this - https://x.com/DhravyaShah/status/2015132693835714909

To install supermemory for your clawd bot, go here: https://supermemory.ai/docs/integrations/clawdbot

---

**Article Stats** (as of capture)  
Published: 4:32 PM · Jan 27, 2026  
Views: 434.3K  
Replies: 62  
Reposts: 96  
Likes: 1K  
Bookmarks: 2.2K