---
url: https://x.com/milesdeutscher/status/2016016997507862648
author: Miles Deutscher (@milesdeutscher)
captured_date: 2026-02-04
---

# I Turned Clawdbot Into My Personal AI Assistant (Full Thoughts)

(Description: Dark-themed header image showing dystopian mechanical figure with "CLAWDBOT" text and "My Full Thoughts" tagline in white serif font)

For the past 48 hours, I've been extensively testing Clawdbot. My old Mac Studio was collecting dust - now it's a 24/7 AI agent helping me run three businesses.

I open Telegram, send a prompt, forget about it, and come back to fully functional workflows.

That's the power of this tool.

And the best part is, it's completely open-source, and costs just a few dollars to get running.

But while this all sounds great, there are some nuances people aren't telling you about this tool. In this guide, I'll break down **everything** you need to know before installing this software on your device.

The pros, the cons, how to set it up, and a few real workflows I've been testing.

At the end, I've included an "Average Joe" section that rates every aspect of this workflow on a 1-10 scale - **accessibility, value, privacy, and impact.**

Stick around until the end to see my official ratings.

---

## What even is Clawdbot?

In one line: Clawdbot is an AI tool that lets AI models connect directly to your desktop.

Once set up, it integrates with various messaging apps (iMessage, Discord, WhatsApp, Telegram).

i.e., you send a message to the bot on Telegram:

"Build me an app for [x]"

"Shop around and buy [X] on Amazon for me..."

"Check my desktop emails and respond."

Any desktop task a human can do, Clawdbot can automate.

### Do you need a Mac Mini?

You've probably seen people rushing out to buy Mac Minis to run Clawdbot, and you're wondering if you should do the same.

Simply put, **no**, you don't need a Mac Mini.

Clawdbot can run on pretty much any laptop/computer.

However, there is a case to be made for running Clawdbot on a Mac device.

Think of it this way: Clawdbot is the brain, but it still needs a good environment to run, and Mac software provides that.

You'd want to give a real employee a powerful machine - the same applies here.

I'm personally running Clawdbot on an old Mac Studio I wasn't using. I'm doing it on a separate device, and not on my main Studio, because of the security risks I'll now expand on.

(Description: Photo of a modern home office setup with white walls, natural light from large windows, dark vertical curtain panels, a desk with a dark monitor, wireless keyboard with RGB lighting, ergonomic mesh chair, additional desk setup in background, wooden flooring with geometric patterned rug, clean minimalist aesthetic)

---

## Downfalls/Caveats

Before we dive into the fun stuff, I have to talk about the potential risks with an AI tool like this.

I'm personally wary of giving away access to my personal data, so here are my thoughts on running Clawdbot while still protecting your information.

### Security risks

You are literally opening your entire desktop to another "person," and Clawdbot can access all your personal data if you allow it.

Prompt injections are also a very real thing and could destroy your device.

My recommendation would be **not to** run this software on your main computer (especially if you're deep in crypto/markets/finance).

Instead, I recommend investing in a Mac mini/dedicated Clawdbot device and downloading only the tools/files/data you feel comfortable with Clawdbot accessing.

The caveat is that without access to all your data, it can't be a true personal assistant. As you'll see later in the article, there are definitely some amazing workflows you can still execute in a sandboxed environment - but until the security issues are fixed, the tradeoffs are just too big to give it full access to your life.

### Cost

Nobody is talking about this right now.

Clawdbot can be VERY expensive - especially if you're using API calls.

My advice is to get on a paid plan and avoid racking up endless API model calls. If you run out of usage, oh well, just resume after the cooldown.

Without limits, this type of tool could easily rack up your expenses. Use paid plans as a "limit" to usage.

Tbh, this entire exercise isn't something I'd recommend if you're resource restricted.

But if you do want to go ahead, or if you at least want to test it out with some light prompts, here's the full guide on how to get set up.

---

## (How to) Set Up

### 1. Open your computer terminal

On Mac, you can open Spotlight with: Command + Space bar and search "Terminal."

### 2. Visit: https://clawd.bot/

(Description: Screenshot of Clawdbot official website featuring red robot mascot icon, large "Clawdbot" text in red and gray gradient, tagline "THE AI THAT ACTUALLY DOES THINGS." in orange text, and descriptive text: "Clears your inbox, sends emails, manages your calendar, checks you in for flights. All from WhatsApp, Telegram, or any chat app you already use.")

### 3. Run the download command in your terminal
```
curl -fsSL https://clawd.bot/install.sh | bash
```

(Description: Terminal window screenshot showing "Quick Start" header in orange text, with terminal commands including "curl -fsSL https://clawd.bot/install.sh | bash", green status indicators, and gray text: "Works on macOS, Windows & Linux. The one-time install NodeJS and everything else for you.")

### 4. Accept Permissions

Once installed, you'll be prompted with a safety guardrails screen.

Please make sure to read the Clawdbot safety docs.

(Description: Terminal screenshot of Clawdbot safety warning in red and white text, featuring Clawdbot ASCII art logo, warnings about setup, safety notice about "Clawdbot agents can run commands, read/write files, and act through any tools you enable," with detailed security information and text: "I understand this is powerful and inherently risky. Continue?" with Yes/No options)

Click 'yes' and continue.

### 5. AI Model Selection Process

Before continuing with the steps below, make sure you have downloaded and logged in to the Claude Code CLI in your Terminal if you plan to use your Anthropic account.

After you have successfully logged in to Claude Code in your Terminal, you'll want to pick Anthropic as your AI provider.

(Description: Terminal interface showing "QuickStart" section with configuration details including "Gateway port: 18789", "Gateway bind: Loopback (127.0.0.1)", "Model/auth provider" section listing multiple AI options with radio buttons: OpenAI, Anthropic (with green dot and "Claude Code CLI + API key" note), MiniMax, Qwen, Synthetic, Venice AI, Google, Copilot, OpenRouter, Vercel AI Gateway, Moonshot AI, Z.AI (OLM 4.7), OpenCode Zen, and Skip for now option)

Continue forward, and you'll be prompted to choose one of the available Anthropic login options.

Select "paste token setup" to use your existing Anthropic account.

In a new terminal window, paste: "claude setup-token"

The Terminal will then connect to Claude Code and output a private key.

Copy that private key and paste it back into your Clawdbot setup terminal.

Keep this private key safe.

You're now connected to your Claude account.

Lastly, select the Claude model you want to use.

I personally opted for Opus 4.5.

(Description: Terminal interface showing model selection menu with heading "Default model" in orange, option "Keep current (default: anthropic/claude-opus-4-5)" with green indicator selected, followed by "Enter model manually" option and extensive list of available Claude models including claude-3-haiku variants, claude-opus variants, claude-sonnet variants with dates and version numbers)

Note: If you want to use a different AI provider (e.g., OpenAI), select it instead of Anthropic and follow the similar on-screen steps.

### 6. Channel Selection

Next, you'll choose where you want to interact with Clawdbot.

You can set up Telegram, WhatsApp, Discord, Slack, iMessage, and more.

(Description: Terminal interface showing "Select channel (QuickStart)" header in orange with multiple channel options listed with radio buttons: Telegram (Bot API) in green with "(not configured)" note, WhatsApp (QR link), Discord (Bot API), Google Chat (Chat API), Slack (Socket Mode), Signal (signal-cli), iMessage (imsg), Nostr (NIP-04 DMs), Microsoft Teams (Bot Framework), Mattermost (plugin), Nextcloud Talk (self-hosted), Matrix (plugin), BlueBubbles (macOS app), LINE (Messaging API), Zalo (Bot API), Zalo (Personal Account), Tiion (Urbit), Skip for now)

I personally went with Telegram here (I use it often for crypto research, so less friction).

You'll be given instructions - follow them (super simple):

(Description: Terminal code snippet showing Telegram bot token setup instructions numbered 1-3, including steps to "Open Telegram and chat with @BotFather", "Run /newbot (or /mybots)", "Copy the token (looks like 123456:ABC...)" with additional notes about setting TELEGRAM_BOT_TOKEN in environment variables, links to Clawdbot Telegram documentation and website)

### 7. Final Setup

You'll then continue with a few final setup steps in your Terminal.

Custom skills, hooks, and a few other optional miscellaneous options.

Once you complete those steps (or skip them), your new AI assistant will be ready, and Terminal will launch you into a gateway website.

(Description: Screenshot of Clawdbot gateway interface showing dark theme with "at" text, gateway chat session interface, message saying "Wake up, my friend!" in pink text with timestamp, and conversation snippet: "Hey! 🚀 I just woke up. Fresh slate, no memories yet — just these starter files and a whole lot of potential. So... who am I? Who are you? — Maybe I'm your kind of AI assistant. Lightning-quick and endlessly creative. Just describe what you need, and let's figure this out together.")

---

## My Experiments

Real workflows I've been testing over the past few days:

### 1. Crypto Research Assistant

One of the coolest ways I've been using Clawdbot is for automated market research.

Example: I recently set up the bot to send me daily market research reports on Telegram at 9 am.

I told the bot to scrape X, CoinGecko, and more sites to ensure high-quality reports.

The convenience of simply opening TG and getting market analysis has been very beneficial (you can even tell it to scroll your X lists).

(Description: Embedded video demonstration showing Telegram conversation with Clawdbot sending a "Daily Crypto Market Recap" for January 26, 2026, with 12:00 PM Dubai timestamp, displaying market overview table with metrics for Total Market Cap, BTC Dominance, ETH Dominance and their 24h changes, followed by additional market data tables showing crypto price and percentage change information)

### 2. Vibe Coding Crypto Apps

There's no real need to manually prompt Vibe Coding tools anymore.

You can just text your bot to execute the entire Planning → Building process.

Tip: I find that vibe coding directly on the gateway website is better than using Telegram.

Example: I prompted it build a real-time, stablecoin-yield-tracking app using live market data from reliable sources like DeFiLlama.

(Description: Embedded video demonstration showing a crypto trading application interface with real-time stablecoin yield tracking, displaying data visualization with graphs, market indicators, and yield percentage displays for various stablecoin positions)

### 3. Trading Journal + Tracker

Lastly, I spent some time building this market trading journal.

The cool thing about Clawdbot is that it can pull data from external sources, like Notion, where I naturally store all my market trades.

Without giving away my exact trading journal log, here's the concept.

(Description: Embedded video demonstration showing a trading journal interface with a personal trading dashboard, displaying trade entries, market data, performance metrics, and portfolio tracking information in a clean, organized layout)

It's pretty crazy that Clawdbot can take these coding builds from 0 → 100 with zero manual intervention.

All I did was prompt it with what I envisioned, it sent a plan, I approved, and I came back to fully functional workflows.

---

## Final Thoughts

As you can see, this tool is very powerful, and the direct messaging integrations are definitely convenient and worth using.

I was in bed, prompting my bot to complete tasks for me - it's pretty crazy.

As I mentioned before, I recommend giving this bot a dedicated setup with restrictions rather than letting it run free on your main computer.

Huge credit to @steipete for building this tool.

---

## Average Joe Ratings

**Accessibility** - **4/10** | Requires CLI, Node ≥22, channel config. Hours/days to get running and possibly a dedicated device/servers.

**Value** - **5/10** | Open source, but hidden costs add up: API calls, hardware, time investment.

**Privacy/Security** - **2/10** | 1,000+ exposed instances on Shodan. Full access to OAuth tokens, API keys, filesystem. One misconfiguration = complete compromise.

**Impact** - **9/10** | If it works safely, genuinely transformative. 24/7 AI assistant across your entire desktop.

**Overall: 5.0/10**

---

## Outro

If you enjoy content like this, be sure to follow me @milesdeutscher.

For deeper AI insights, follow me on @aiedge_.

Im curious, how are you guys implementing Clawdbot? - I'm always looking to test new AI workflows.

If you found value from this article, consider a Like/Repost 💙