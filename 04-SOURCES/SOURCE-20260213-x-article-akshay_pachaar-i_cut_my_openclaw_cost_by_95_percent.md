---
url: https://x.com/akshay_pachaar/status/2022309334483677654
author: "Akshay (@akshay_pachaar)"
captured_date: 2026-02-13
id: SOURCE-20260213-001
original_filename: "20260213-x_article-i_cut_my_openclaw_cost_by_95_percent-@akshay_pachaar.md"
status: triaged
platform: x
format: article
creator: akshay_pachaar
signal_tier: tactical
topics:
  - ai-agents
  - agentic-development
  - ai-workflow
  - context-management
  - memory-management
  - api
  - open-source
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "I Cut My OpenClaw Cost by 95"
synopsis: "I Cut My OpenClaw Cost by 95% and Minimax M2.5 logo on dark background with white and red text styling) Overview An open source model just released that is: - Better than Opus 4.6 for coding - Faster than Sonnet - State of the art for tool calling Minimax just dropped M2.5. It scores on par with Opus 4.6 on coding benchmarks. It's built from the ground up for agentic workflows."
key_insights:
  - "At roughly $1 per hour with 100 tokens per second, you can now scale long-running agents in a way that was never economically feasible before."
  - "Always grab the latest command from the official site: openclaw.ai Step 2: Pick Your Model During setup, OpenClaw will prompt you to choose a model."
  - "It scores on par with Opus 4.6 on coding benchmarks."
---
# I Cut My OpenClaw Cost by 95%

(Description: Hero image featuring OpenClaw mascot (red crab character) and Minimax M2.5 logo on dark background with white and red text styling)

## Overview

An open source model just released that is:

- Better than Opus 4.6 for coding
- Faster than Sonnet
- State of the art for tool calling

Minimax just dropped M2.5. It scores on par with Opus 4.6 on coding benchmarks. It's built from the ground up for agentic workflows. And it costs a fraction of what you'd pay for frontier models.

We're talking about a 95% reduction in cost.

I've already switched my entire OpenClaw setup to run on it. Let me show you exactly why, and how you can do the same.

## Why Minimax M2.5 Changes the Game

Here's the problem with running AI agents today.

Frontier models like Opus 4.6 are incredibly capable, but they're also incredibly expensive. If you want an agent that runs autonomously for hours, handling complex multi-step tasks, your API bill adds up fast.

@MiniMax_AI M2.5 solves this problem entirely.

It hits 80.2% on SWE-Bench Verified, which puts it right alongside Opus 4.6 in coding performance. It scores 76.3% on BrowseComp for search tasks and 76.8% on BFCL for agentic tool-calling.

(Description: Benchmark comparison chart showing six different evaluation metrics (SWE-Bench Verified, SWE-Bench Pro, Multi-SWE-Bench, VIBE Pro (AVG), BrowseComp (aclta), BFCL multi-turn, REWC, and GDPalMM) with red/coral bars for Minimax M2.5 and M2.1, gray bars for Claude Opus and other models)

What really stands out is that **it's designed for long-horizon agentic tasks.**

This means your OpenClaw agent can independently keep running, planning, and finishing complex tasks without falling apart midway. The model doesn't lose context. It doesn't get confused 15 steps into a workflow.

At roughly $1 per hour with 100 tokens per second, you can now scale long-running agents in a way that was never economically feasible before.

And here's what most people miss. M2.5 only activates 10 billion parameters. That makes it the smallest among all Tier-1 models. So if you're self-hosting, you get an unparalleled advantage in terms of compute and memory requirements.

I'm not saying it's better than Opus 4.6 at everything. But for agentic coding and automation workflows? It's the better choice at a fraction of the cost.

## How to Set Up OpenClaw with Minimax M2.5

The setup is straightforward, and here's the step-by-step walkthrough.

### Step 1: Install OpenClaw
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

Follow the on-screen instructions. The installer handles everything.

**Note:** Installation commands may vary by OS. Always grab the latest command from the official site: openclaw.ai

### Step 2: Pick Your Model

During setup, OpenClaw will prompt you to choose a model.

Select **Minimax M2.5**. It's the recommended choice.

(Description: Terminal screenshot showing Model/auth provider selection menu with options including OpenAI, Anthropic, MiniMax (M2.5 recommended), Moonshot AI, Google, xAI, OpenRouter, Qwen, Z.AI, Qianfan, Copilot, Vercel AI Gateway, OpenCode Zen, Xiaomi, Synthetic, Together AI, Venice AI, LiteLLM, Cloudflare AI Gateway)

### Step 3: Setup OAuth or get your API key

1. Subscribe to a coding plan here: https://platform.minimax.io/subscribe/coding-plan
2. Minimax offers a starter Coding Plan at $8.8/month, which gives you production-grade agentic coding accessible to individual developers.

### Step 4: Register Your Telegram Bot

To create your bot:

1. Open Telegram
2. Search for Botfather
3. Start a chat and choose **Create New Bot**
4. Assign a name and a unique username

BotFather will create the bot instantly.

### Step 5: Copy the Bot Token

After creating the bot, BotFather will provide a **Bot Token**.

Copy this token, you'll paste it into your terminal when ClawdBot asks for it during channel setup.

After the setup, you can access it Telegram, see how I am able chat with my new agent name Gilfoyle (yes the one from Silicon valley..xD) 👇

(Description: Telegram chat window showing conversation with Gilfoyle bot, displaying setup messages including "OpenClaw: access not configured," "Your Telegram user id:" and "Pairing code:" fields)

And that's all. You can take it from here.

## What I'm Actually Building With This

I don't just run one agent. I run three.

Think of them as AI employees that work for me around the clock. Each one has a specific role, and I interact with all of them through Telegram.

### Neo: My AI Engineer

Neo is a highly capable software developer that works 24/7.

Whether it's building a feature, fixing a bug, or automating some tedious workflow, I just message Neo and it gets done.

Because M2.5 excels at long-horizon tasks, Neo can take a complex coding assignment and work through it independently. It plans, writes code, tests, and iterates without me having to babysit every step.

(Description: Telegram chat interface showing Neo bot conversation with capabilities listed including "Read PDFs, analyze documents on Your Mac," "Run commands, install packages," "Manage files, processes, services," "Access installed tools (ffmpeg, brew, etc.)," "Communication," "Transcribe audio (Whisper)," "Send messages across channels," "Set reminders, manage schedules." Shows conversation about creating a Manim animation with gradient descent and a technical diagram on the right)

### Pulse: My Deep Researcher

Every morning at 8:30 AM, I get a curated research briefing from Pulse.

It scans the sources that matter most:

- Hugging Face blog and trending models
- Trending GitHub repos
- Official blogs from major AI labs
- Relevant subreddits

Then it distills everything into a clean, actionable summary. No noise, no scrolling through 47 tabs, just the signal that actually matters.

This alone has saved me hours every week. I stay on top of what's happening in AI and ML without the information overload.

(Description: Telegram chat showing Pulse bot interface with research briefing including topics like "VibeTransfer: an open source deep learning runtime built for coding agents under high-level human guidance," "2. 1.5 Million AI Agents 'At Risk of Going Rogue'" with source citations and survey information about AI agent deployment security)

### Pixel: My Graphic Designer

Pixel understands the Daily Dose of Data Science brand.

It creates educational visuals that have our signature hand-thrown feel. It breaks down complex concepts into simple illustrations. And it keeps everything on-brand and consistent across all our content.

When I need a visual for a newsletter or social post, I message Pixel with the concept. It delivers something that looks like it came from our design team.

(Description: Telegram chat showing Pixel bot conversation with detailed design instructions. Chat shows message "Create a nice diagram showing the end to end MLOps cycle" and visual diagram delivered showing "Data Collection," "Data Validation & Prep," "Continuous Learning," "Model Training," "Model Evaluation," "Deployment & Serving," and "Production Monitoring" in a cyclical workflow with hand-drawn style illustrations)

All three agents run on Minimax M2.5, available to me through Telegram, at a fraction of what I'd pay with frontier models.

If you want to see the full setup in action, I published a 30-minute YouTube masterclass on OpenClaw where you learn how to create your first agent and then scale from 1 to 10 so they can all collaborate and work 24/7 for you.

I started with Minimax M2.1, switched to Opus 4.6 for better results, and now I've been getting consistently strong results with M2.5.

Will continue testing and sharing what we find.

Check this out: https://youtu.be/aFQJYaornJ4

(Description: YouTube video thumbnail showing Akshay's headshot on right side, red background with white OpenClaw logo and text "OpenClaw master in 30 min" with engagement metrics: 1,850 comments, 7,856 reposts, 4,652 likes, 1.7M views)

Stay tuned, I'll be covering more on deploying OpenClaw securely and how you can also optimize the token usage.

And if you found it insightful, reshare with your network.

Find me → @akshay_pachaar ✔️

For more insights and tutorials on LLMs, AI Agents, and Machine Learning!

---

**Post Details**
- Published: 5:58 AM · Feb 13, 2026
- Views: 92.9K
- Engagement: 43 Replies, 89 Reposts, 935 Likes, 2.1K Bookmarks