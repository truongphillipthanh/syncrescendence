# 🔑 OpenClaw + MiniMax = The $14/Month AI Agent

(Description: Comic illustration featuring two anthropomorphic red lobsters. The left lobster displays a cheerful expression with raised claws. The right lobster wears a headband with a star and holds a sword. Blue radial starburst pattern fills the background. Bold white text reads "OpenClaw MiniMax")

## The Problem

You're paying $200/month for AI APIs.

Your agent runs for 3 hours before you shut it off because the token costs are bleeding you dry.

Meanwhile, developers on X are running OpenClaw bots 24/7 for about the cost of two coffees. Same capabilities. Same intelligence. 90% cheaper.

### The Math Breaks Down Like This:

- Hetzner VPS: ~$4/month (CX23 or CAX11)
- MiniMax Coding Plan Starter: $10/month
- **Total: ~$14/month**

MiniMax has a subscription model for developers. Not per-token. Flat monthly fee. The Starter plan gives you 100 "prompts" per 5-hour rolling window (one prompt equals roughly 15 API requests). For a personal assistant handling occasional messages throughout the day, that's plenty. Heavy use? Upgrade to Plus ($20) or Max ($50).

This week, 100,000 developers discovered this combination. Here's the exact setup.

---

## > The Lobster Everyone's Talking About

On January 30, 2026, the open-source project formerly known as Clawdbot completed its third rebrand. First Clawd (Anthropic's lawyers weren't fans). Then Moltbot. Now OpenClaw.

The name finally stuck. The momentum hit escape velocity.

**108,000+ GitHub stars in days. 2 million visitors in a week. Developers buying Mac Minis specifically to host it.**

OpenClaw runs AI agents locally. Your hardware. Your data. Your rules.

The practical version: you message your assistant on WhatsApp, Telegram, Discord, Slack, or iMessage. It messages back. But unlike ChatGPT or Claude's web interface, OpenClaw doesn't just respond.

It reads your emails and surfaces what matters. Updates your calendar when you forward a flight confirmation. Runs terminal commands when you ask it to deploy. Browses the web. Fills out forms. Sends messages on your behalf.

The catch? Running an agent 24/7 means paying for AI 24/7. That's where most setups fall apart.

---

## > Why MiniMax Changes the Math

Claude Opus costs $15 per million input tokens. GPT-4 is in the same range. Run an always-on assistant with those models and you're looking at hundreds per month in API costs. Maybe more if your agent is actually useful and does real work.

**MiniMax M2.1 flips the economics.**

The model hit 72.5% on SWE-Multilingual, outperforming Claude Sonnet 4.5 (68.0%) on multilingual coding tasks. It scores 88.6% on VIBE-Bench, MiniMax's executable code benchmark that tests whether generated apps actually run. It approaches Claude Opus 4.5 in coding benchmarks while costing a fraction per token.

But the real unlock is the Coding Plan.

MiniMax offers three subscription tiers specifically for developers building agents and coding tools:

- **Starter**: $10/month (100 prompts per 5 hours, ~1,500 requests)
- **Plus**: $20/month (more capacity)
- **Max**: $50/month (heavy usage)

One "prompt" equals roughly 15 API requests. The quota rolls every 5 hours. For a personal assistant that handles messages throughout the day, Starter is usually enough. Hit the limit? You switch to pay-as-you-go temporarily or upgrade.

Why does this pricing exist? MiniMax uses a Mixture-of-Experts architecture. 230 billion total parameters, but only 10 billion activate per token. The sparsity means lower compute costs per request. They're passing that efficiency to developers who commit to the platform.

**The result: developers running OpenClaw with moderate daily usage report their MiniMax costs staying flat at $10-20/month. Combined with a $4 VPS, you get a functional AI agent for under $15/month total.**

---

## > Now Your Bot Can Talk Back

MiniMax dropped Speech 2.8 this week.

**300+ voices. 40+ languages. Studio-quality text-to-speech that doesn't sound like a robot reading a teleprompter.**

The official MiniMax account put it simply: ask your AI to create a skill for the Speech 2.8 model and start receiving voice messages from your OpenClaw bot.

**Before:** You check your phone. A wall of text from your assistant. You skim it while walking and miss half the details.

**After:** Your assistant narrates your morning emails while you make coffee. Reads research papers during your commute. Voice-announces calendar changes.

The voices rank number one on major TTS quality benchmarks. Artificial Analysis Arena. Hugging Face TTS Arena. Users consistently prefer them over ElevenLabs and OpenAI's offerings in blind tests.

You can add interjections like (laughs), (sighs), (clears throat) and the model delivers them naturally. Control emotion, speed, pitch. Clone your own voice with 10 seconds of audio.

Speech 2.8 comes in two variants: HD for final production quality, Turbo for real-time responses. Pick based on whether you need polish or speed.

---

## > The Setup (30 Minutes If You Can't Code)

Here's the thing: you don't need to be a developer.

Corey Ganim (@GanimCorey) put it bluntly: "I'm not a software engineer. I can't code. I literally failed computer science 1 in college. But I still set up 3 custom OpenClaw agents in under 30 minutes."

### His Mental Model for Understanding Agents:

- **Agent Harness** = The structure holding everything together
- **LLM** = The brain (MiniMax, Claude, etc.)
- **Skills** = Your automated SOPs
- **Sessions** = How it learns over time
- **Tools** = Specialized capabilities you plug in
- **Data** = Your personalized knowledge base

Learn it once, apply it anywhere.

### Step 1: Pick Where to Host

Head to the OpenClaw quick start guide. Your options:

- Mac (many started on Mac Minis)
- Windows with WSL
- Ubuntu VPS (cheapest long-term)

Pick one. Move on.
```bash
npm install -g @openclaw/openclaw
openclaw configure
```

The setup wizard walks you through everything. No command-line wizardry.

For server hosting: Hetzner's CX23 costs €3.49/month (~$4). Their ARM option (CAX11) is €3.79/month. Both include 20TB traffic.

### Step 2: Choose Your Brain

This is where you pick which AI powers your agent.

Corey's setup (and what most people are running):

- **Daily driver:** MiniMax M2.1 (fast, cheap, handles 90% of tasks)
- **Heavy lifting:** Anthropic Opus 4.5 (for complex analysis and deep work)

Think Toyota Camry vs Ferrari. Camrys are cheap and reliable. Ferraris are powerful but expensive.

Get a Coding Plan API key from `platform.minimax.io/subscribe/coding-plan`. Pick your tier (Starter at $10/month is fine for most personal use). After subscribing, go to Account/Coding Plan to generate your API key.

**Important:** The Coding Plan API key is separate from the regular pay-as-you-go key. Don't mix them up.

### Step 3: Set Up Communication Channels

Configure where you'll talk to your bot. Discord, WhatsApp, Telegram, Slack, Teams.

Discord is popular for the collaborative environment. You message the bot, your team messages the bot, all in one place.

### Step 4: Add Skills (This Is Where It Gets Good)

Skills are automated SOPs. Instead of doing the same task 50 times manually, teach your agent once. It handles it the same way every time.

**Pre-installed skills worth enabling:**

- Summarize (drop any URL, get key points)
- gog (manages Google Workspace: emails, calendars, docs)

The community has built hundreds more on clawdhub. Install what you need.

**Custom skills people have built:**

- Podcast research (find shows to guest on)
- Email drafts (write templated emails in your voice)
- Brand voice (understand how you write, create content that sounds like you)

### Step 5: Configure Memory (The Secret Sauce)

When you first install OpenClaw, it's the dumbest it will ever be.

It has long-term memory, daily memories, and ad-hoc memories. After a few sessions, it starts forgetting things. Don't panic. AI has finite context windows.

**The fix: semantic search.**

Think Ctrl+F for your conversation history, but instead of searching exact keywords, it understands meaning. Search for an idea, find related concepts even with different words.

Ask: "When does Corey prefer meetings?"

It doesn't just search for "Corey" and "meetings." It understands you're asking about preferences and scheduling patterns.

Over time, this makes your agent powerful. It builds a personalized knowledge base that grows smarter with every conversation.

### Step 6: Add Voice (Optional)

Create a skill that calls MiniMax Speech 2.8. The community has shared templates on the Skills hub.

Your bot receives text, converts to audio, sends back through your chat app. Voice memos instead of text walls.

---

## > What People Built This Week

The OpenClaw + MiniMax combination is enabling use cases that felt theoretical months ago.

**Research assistant that actually researches.** One developer pointed their bot at MCP documentation. Asked it to turn the docs into study materials. Got back a visual explainer PDF, organized notes per concept, and a diagram showing how everything connects. No manual reading. No scattered notes.

**24/7 code review.** MiniMax M2.1 reads code across Rust, Java, Golang, TypeScript, Kotlin, C++. Developers are routing merge requests through OpenClaw agents that review, suggest changes, and create follow-up tickets automatically. The agent doesn't sleep.

**iPod-style music client.** Someone built a YouTube Music desktop app using MiniMax in one night. Pure Rust. Retro iPod aesthetic. The agent handled all the code generation.

**Automated deal hunting.** Agents comparing prices across dealers, sending follow-up emails, handling insurance claims. Memory persists. Tell your bot you only drink oat milk lattes once. It remembers forever.

**Voice journaling.** Speech 2.8 reads back your notes in a natural voice. Daily summaries. Meeting recaps. Calendar overviews as audio instead of text.

---

## > MiniMax Agent Desktop (Skip the Terminal)

Not everyone wants to manage infrastructure. Some people just want the AI to work.

MiniMax Agent Desktop is their answer. They're calling it an "AI-native Workspace" with a bold tagline: **Everyone is an Agent Designer.**

Cross-platform app for macOS and Windows. Available to all users (not locked behind Pro tiers like Claude Cowork). For OpenClaw users: throw in your Coding Plan key and channel tokens, Agent Desktop powers through the config automatically. MiniMax tweeted this directly. Skip the terminal, skip straight to the fun part.

### What It Actually Does:

**Zero-code full-stack development.** Describe what you want in plain text. The agent builds complete webs and apps with backend logic, data workflows, and self-testing. One-shot delivery.

**MCP auto-tooling.** The agent automatically creates and reuses MCPs as tasks get complex. No manual setup. No deployment headaches. It adapts and scales with you.

**Selector editing.** Click any element on a web page. Tell the agent how to improve it. Fine-tuning UI becomes point-and-describe.

**Create your own Experts.** New feature. Describe what you need, Agent Desktop generates a custom Expert for you. Configure via simple form. Test instantly.

**Desktop Cowork.** This is the big one. MiniMax Agent runs directly on your desktop, bringing AI beyond chatbots and onto real computer screens. Built for AI-native teams and real-world workflows.

### The Privacy Angle (This Matters for Enterprise):

**Deep local integration.** Privacy-first by design. Connect authorized local files, email, calendars, GitLab, logs. All data stays on your device. No cloud processing of sensitive files.

This unlocks use cases that security teams would never approve with cloud-only tools.

**Agentic batch workflows:** Code edits, merge requests, alerts, repetitive dev tasks. All in batch. Spend less time on maintenance, more time on creative work. One user described routing all their MRs through Agent Desktop. The agent reviews, suggests, creates follow-up tickets.

**Full browser control:** Describe your goal once. The agent navigates the web, clicks, fills forms, executes. From research to real execution, hands-free.

**The Experts Community:** An agent marketplace. Build and share domain-specific expert agents for finance, law, writing, hiring, research. Use what others have built or create your own. Think of it as an app store for AI workflows.

### Agent Desktop vs Claude Cowork

(Description: Dark-themed comparison table with three columns. Header row shows "Feature", "MiniMax Agent Desktop", and "Claude Cowork". Rows compare: Platforms (macOS + Windows vs macOS only), Access (All users vs Max/Pro only), Browser control (Full vs Limited), Custom Experts (Yes vs No), Free tier (1,000 credits vs No), MCP auto-creation (Yes vs No))

**Platforms:** macOS + Windows | macOS only  
**Access:** All users | Max/Pro o