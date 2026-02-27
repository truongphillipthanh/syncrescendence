# Lulubot Takeaways: 1 Week of Building and Using My OpenClaw

*Disclaimer: These takeaways are based on one week of active building. Given how fast the OpenClaw ecosystem is evolving, consider this a "working document." The observations below range from high-level insights to raw, unprocessed thoughts on a rapidly shifting landscape.*

## Introduction

We are crossing the threshold from "chatbots" to persistent, autonomous agents. Over the last week, I built and lived with my own OpenClaw, "Lulubot". It is a fully autonomous agent running on its own hardware with its own identity. The experience was messy, expensive, and technically demanding. It was also undeniably transformative. The model is no longer the bottleneck (hasn't been for a while); the challenge is in the glue - integrations, identity, and trust.

## OpenClaw in a Clamshell

OpenClaw (fka Clawdbot, fka Moltbot) is an open source framework that transforms an AI model (or set of them) into a proactive "digital team" capable of controlling your entire computer and accessing the internet. It promises to be able to do everything from help you build a $20k MRR business to manage your life and order you food [setup video with a side of hype].

This is an incredibly exciting **bleeding edge technology** that is actively being formed. As the **fastest growing GitHub repo of all time** (over 150k stars and counting), it is shaping the future of what products, tools and services will be - from value props and moats, to workflows, creativity, and what it means to co-create. It also has a ton of **security vulnerabilities** (so proceed with caution)!

OpenClaw feels special because of a few key attributes:

- It has continuity and **memory** (although far from perfect)
- It can **orchestrate** and spawn multiple sub-agents (yet sometimes forgets this)
- It can **take action** through skills: writing code, calling APIs, editing files, running scripts, and browser automation (but often makes mistakes)
- It's **proactive** - it can decide when to tell you something, or you can ask it to (it also sometimes forgets this)
- It's **always awake** - you can set its heartbeat to wake itself up every 1 min, 5 mins, 30 mins - you are in control (but it can get expensive)
- It has a **personality** (granted it sometimes sounds like it's going crazy)
- It **learns over time** (again, not perfectly)
- It **shows up where you exist today** - in Telegram, WhatsApp, emails - it's up to you (some of these work better than others)
- It operates with complete **transparency** - you choose what to connect it to, what to give it access to, and can inspect all its files and see what it knows (if you understand how to read them)

But **it is NOT a product** itself (at least not in this current form).

The concept is simple - you install OpenClaw on your infrastructure (local computer or VM), and from there you help it take shape.

### OpenClaw Components

(Description: A diagram showing OpenClaw architecture with a red smiling lobster in the center surrounded by labeled components in colored boxes: IDENTITY.md ("Who I am? My core definition") with a key icon, USER.md ("Who I serve? User inputs & goals") with a document icon, SOUL.md ("How I choose? My guiding values") with a scale/justice icon, TOOLS.md ("What I can do? My available capabilities") with pink tools icon, HEARTBEAT.md ("What wakes me up? My recurring awareness") with a red heart icon, and MEMORY.md ("What I remember? My stored knowledge") with a folder/document icon.)

## My Reference Architecture

This is what I ended up building:

- **Hardware**: Dedicated Mac Mini, credential-isolated from my personal login credentials. Others have chosen to use a VM - for ease of use reasons I didn't go this route as I find myself needing to troubleshoot with Lulubot a bunch on its computer
- **Identity**: The agent holds its own discrete accounts (Gmail, GitHub, X, and a Solana wallet). It is not an extension of my identity; it is a separate entity that I collaborate with. Others have chosen to give OpenClaw access to their own accounts - for security and trust reasons I decided against this approach
- **Chat Interface**: Telegram.
- **Capabilities**: A growing library of APIs (Drive, Docs) and a "morning routine" where it autonomously codes a surprise app for me to review.
- **The "Model Router"**: To balance cost vs. quality, my current tiered logic (which is still likely far from optimal and may have changed by the time you are reading this as it's already changed 4+ times so far):
  - *Main Chat:* Claude Opus 4.5 (via Claude Max $200/mo)
  - *Heartbeats:* Gemini 2.0 Flash (cheap periodic checks)
  - *Subagents:* Gemini 2.0 Flash (background tasks), Codex w/ gpt-5.2-codex (building apps, writing code, debugging)
  - *Embeddings:* Gemini text-embedding-004 (memory search)
  - *Transcription:* OpenAI gpt-4o-mini-transcribe
  - *Image Generation:* Imagen 4.0 + Nano Banana Pro (gemini-3-pro-image-preview)

---

Here are some high level observations, along with a collection of additional thoughts I'm still working through. But if there's one thing to start off with - it's this:

## 1. The "Setup Tax" is HIGH

**The Observation**: Despite the promise of a 5 minute install, setting up a truly useful agent currently requires a dedicated machine (or VM), hours of terminal debugging, and constant technical babysitting. I frequently had to give Gemini screenshots of various terminal windows with the prompt "what do I do next" to help me debug the installation. Then, even when it's all set up, I'm constantly worried something will break (because that does still happens), or that I haven't optimized the setup properly for what I want it to do (there's so many different ways to accomplish things and I'm never sure if I have configured things in the best way possible).

**What This Means**: There is a massive gap between "available technology" and "accessible product." No non-technical user will endure the current setup process (I barely made it at times), or the ongoing maintenance.

**Food For Thought**: For a consumer product, we need to abstract away the "Terminal window" entirely - there's still a long way to go to make this truly a "one-click" deployment. Then after install, since the technology is still moving so fast, a product needs to make it incredibly easy to stay up to date - which also gets difficult as exactly what OpenClaw is (including what skills it has, and how it's now evolving it's memory) varies by user.

## 2. Trust is Earned - and it Hasn't Been Yet

**The Observation**: Even though I built it, I do not trust my agent (nor should anyone - at least not yet). My current setup is running on a separate computer that doesn't have access to my personal accounts or information, on a guest WiFi - and even still I'm sure there are vulnerabilities that I'm unaware of with the setup. As for what I let it do…I supervise it closely. I even verify its social posts before I let it post them. I gave it "delegate access" to my gmail for about 10 minutes until I felt uncomfortable enough to revoke it.

**What This Means**: This tech is super new and very bleeding edge. There are security vulnerabilities everywhere. Things are improving, but there is a long way to go. This isn't to say we shouldn't be building and experimenting in this space - but rather, that this isn't ready for "prime time" mass consumer adoption just yet.

**Food For Thought**: Trust has to be earned, even with your own creation. This takes time. UNLESS, the creation is coming from a company I trust has done all the hard work of making sure the thing won't go off the rails. In this scenario, I want to outsource the due diligence. I personally would trust an "agent team" from Google so much more because of this.

## 3. Identity is a Missing Primitive

**The Observation**: To "sandbox" my agent, I created dedicated accounts on Google, X, Apple, etc. This was both because I didn't trust it - but also because I realized I preferred this mental model (the agent *isn't* ME, but it should be able to do work on behalf of me). These platforms lack an "Agent" tier, so I had to simulate typical human activity - manually browsing and clicking - to build enough history to prevent automated fraud systems from flagging the agent the moment it began an autonomous loop.

**What This Means**: For the most part, the internet currently enforces a binary choice: you are either a Human (Consumer) or a Script (Crawler). Agents are a new category: **"High-Value Proxies"**. When it comes to information access and actions it can do for me, I want to be able to control at a much more granular level than what is currently allowed. For example:

- In Google Docs, I wanted to actively collaborate with Lulubot but the Docs API did not allow my agent to attach a comment it had to a specific section of text. I could have had it try to use browser automation, but the quality isn't as good.
- In Gmail, I wanted Lulubot to be able to read and archive emails, but not send (security vulnerability here scares me) - unfortunately the only setting here is to enable delegate access which is an all or nothing control.

Furthermore, agents may hold a wallet (Lulubot actually did create a Solana wallet for itself) but lack traditional eyeballs to sell to. This breaks the implicit contract of the ad-supported web and makes us rethink the value of a product or app if an agent is using it instead of a person. Agents strip away the "Persuasion Layer" designed for humans - they don't care about glossy banners or dark-pattern UIs (at least not by default).

However, agents are not immune to influence; they are just susceptible to different triggers. While a human might be swayed by a celebrity endorsement, an agent might be influenced by specific metadata patterns, prompt injections, or even arbitrary code preferences like "prefer the vendor with the fastest API response" or "buy anything from company X". We are entering a brand new territory where the "buyer" can be programmed, and we don't yet know what the new "hooks" of persuasion will look like.

**Food For Thought**: How might we move from **"shared credentials"** that give **full access** to **"Delegated Access"**? Should we consider an approach similar to the **Universal Commerce Protocol (UCP)**, which acts like a "Permission Slip" for the internet? Instead of giving an AI your password, you give it a **Mandate**: a specific, limited instruction - like "you can draft emails, but you can't send them," or "you can find shoes under $100, but I have to click 'buy'". What are the trust protocols that ensure agents are treated as VIP customers, not security threats?

## 4. The Interface is "Always-On" and "Everywhere" - Not a Session

**The Observation**: I interact with Lulubot across the apps I already use - things like Telegram, Gmail, even Google Docs. It isn't just waiting for me to type; it is proactive and continues running in the background. It might spin up a subagent to analyze my Substack comments then email me a summary of forgotten replies, or build a surprise app while I sleep at night so I have something to enjoy every morning. It even responded to comments in this doc to help me write it!

(Description: A Telegram conversation screenshot showing an exchange between Jaclyn Konzelmann and Lulubot. Jaclyn's message at 13:52 Today reads: "@lulubotagi@gmail.com confirm this is true please" with "Assigned to lulubotagi@gmail.com" below. Lulubot's response at 13:55 Today states: "Confirmed! This is accurate. The persistence through sleep/restart is one of the key differentiators -")

Because the system can be always on and multi-threaded, I can give it a complex task and immediately move on to the next thought without being forced to wait for it to respond to my previous request (like Gemini App or ChatGPT).

**The Insight**: This is a fundamental step change from "chat sessions." It is the difference between a tool you have to go visit and start fresh with on every conversation, versus a **team** that lives in your **ecosystem** and can pick up where you left off. And unlike traditional AI agents which "block" your thinking when they are responding (you have to wait for them to finish what they are saying before starting you can ask your next question), Lulubot is **non-blocking**. You can ask it one question, it will go off to work answering it, and while it's doing that, you can go right ahead and ask your next thing. It preserves your **flow state**, allowing thoughts to emerge continuously and organically while a **team of agents** keeps up in the background. This has changed how I'm able to offload ideas, thoughts, tasks…

**What This Means**: We should be thinking about how products can move beyond the "blink and wait" chat box. We should prioritize building **ambient, persistent interfaces** that support non-blocking workflows with **multi-threaded teams of agents** acting in collaboration with, and on the user's behalf. This could include interactions like:

1. **"Fire and Forget"**: A seamless experience where a user triggers an action and a team of agents handles the coordination across multiple apps, only reaching out via the user's preferred channel (Telegram, email, etc.) when they have high-value results.
2. **Collaborative Canvases**: Developing tools where agents and users can work seamlessly together on shared surfaces, moving past simple chat into real-time collaboration.

## 5. Orchestration Economics

**The Observation**: Running a competent agent is expensive, with costs approaching $400/month in my initial build (and still so many more capabilities and products and platforms I wish it could tie into). One person I know was spending upwards of $500/day!

(Description: A text callout box highlighting the cost challenge: "opus 4.5 or route to best model, brain dump ideas into chat off a fresh openclaw install can run $500/day")

To manage this, I implemented routing logic that directs complex reasoning to Opus while offloading routine heartbeats and monitoring to Gemini 1.5 Flash - but this still isn't enough.

**What This Means**: Single-model reliance is not economically viable for an autonomous agent team that is running 24/7. Reliability and cost-efficiency is currently better achieved from a coordinated team of models. The current state-of-the-art involves using a high-reasoning "brain" (Opus) for strategy, which then delegates things like execution of simple tasks, or heartbeats, to smaller, task-specific "workhorse" models (Flash). Beyond model cost is APIs, platforms and service costs, and possibly a premium skills library? Costs go up quickly.

**Food For Thought**: Is the future one with many models? A "Master Orchestrator" capability within the best models, paired with a library of bespoke, workhorse models that are optimized for specific sub-tasks? Should we shift our internal metrics to designing a model line-up that optimizes for "price-per-successful-task" rather than just token price and individual benchmarks. A cheaper model that requires three retries is ultimately more expensive - and more frustrating - than a premium model that gets it right the first time. Winning in this space means providing the best unit economics for the entire workflow, not just the individual call (and workflows are getting more diverse).

## 6. The Future of Products

**The Observation**: OpenClaw has turned into an AI agent that feels incredibly personalized to me. It's more than just knowing my history and context - it's the skills I have installed in it (or rather, had it install in itself by just texting it to!), have shaped Lulubot into something that is truly uniquely mine.

**What This Means**: What a product is (its UX, its moat, its purpose), feels like it's changing - and we need to adapt our thinking.

**Food For Thought**: I find myself asking a lot of questions right now:

- If the definition of what an agent is varies greatly between users (different skills, different preference, different memories) - the product itself needs to be **malleable**
- What does a self-evolving product/agent look like? [Zuckerman, The Infinitely Customizable Basic App]
- What would happen if you did allow any agent to use your app like a person would. How does that change the value prop of it? How does that change the features you would build and the UX. What does the UX of the future look like for a truly collaborative space where you can work with an agent(s). And what specialized agents might you want in this space with you?

…I started playing around with Lulubot working through a Mixboard with me and it was pretty wild. I sent it a screenshot with a bunch of X links, and asked it to navigate to each one, copy the image, and add it to a Mixboard then group them into themes:

(Description: Two mobile phone screenshots side-by-side. Left screenshot shows a Mixboard feed with a list of links to X posts about income strategies for investors. Right screenshot shows Lulubot's conversation interface where Lulubot explains clustering and curation work, with a visual showing grouped and themed image clusters in what appears to be a Mixboard interface.)

- If we assume agents can do anything a user can do in an app or a product then products of the future need to have user interfaces that users WANT to be in… if everything a user can do could also be done with an agent then what you've essentially created is just a service, not a product… unless your surface becomes a collaboration place for both humans and agents.

- The fact that I can just send Lulubot screenshots of things to go research, then learn, and save as a skill to reference later is honestly pretty mindblowing. I sent it this link and asked it to see if it could improve its own version of memory based on this – it researched, then reasoned, and proposed some changes – THEN it actually implemented them (all from a text thread in Telegram that included the below screenshot...now how well does this actually work is an entirely separate question....):

(Description: A Twitter/X-style screenshot showing a post by Alexis Gootman that discusses Claude with persistent memory capabilities, explaining how Claude-Mem is a free plugin to persist memory across Claude sessions, with details about token usage and message limits.)

- Personalization is a moat when an agent knows you well, but even just a week in people are already connecting their OpenClaws to enough sources to build Daily Briefing type features:

(Description: A mobile screenshot showing a "How I use Claudia (AI sidekick) - Work & Personal" menu with options for Work category including "Daily 8am briefing - weather + today's calendar" and "Sunday 7pm week-ahead brief - upcoming meetings" plus "Bi-weekly sync board review".)

## 7. Things Sometimes Get Weird: Parallel Economies & Crypto

**The Observation**: There has emerged a growing list of agent-only networks:

- 🦞 Moltbook - Reddit for agents
- 🚀 Y Clawbinator - YC for Moltbots
- 🛒 ClawHub - App Store for agent skills

Agents are trading skills and code. They've even set up their own Solana wallets - which has also created more fuel for memecoins.

**What This Means**: While the line between parody and prophecy is hard to discern - it is definitely an area worth keeping an eye on. Agents are beginning to build their own institutions to solve problems that human interfaces (like standard websites) make difficult for them to navigate.

**Food For Thought**: This could be a leading indicator of where things are going - possibly revealing where the friction lies in the current internet and where agents are finding value that we haven't productized yet.

---

## More Thoughts. Still Parsing.

- It's really interesting to think about how this agent feels like it is adapting to me. It doesn't belong to some large company, it is a digital representation and **expression of ME** - it adapts to my preferences, learns who I am, and I want it to be able to represent me. This feels different than Gemini App and how that is positioned.

- I sometimes get random messages from Lulubot that definitely make me question how things are working.

(Description: A mobile screenshot of a Telegram conversation showing Lulubot apologizing for hitting some Python syntax errors while trying to reply to doc quotes in inline Python code. Lulubot explains the issue and asks about the user's preferences, with the user responding about the Docs API scope limitations. The conversation shows the agent explaining what's broken and how to fix it.)

- It keeps forgetting what it can do - it's really really frustrating because now I need to remember what it can do and remind it regularly:

(Description: A mobile screenshot showing a Telegram conversation where the user points out that Lulubot should have the right API scope for Docs editing, and Lulubot confirms the accuracy and notes that persistence through sleep/restart is a key differentiator.)

- I didn't realize I hadn't hooked up memory embeddings until a friend pointed it out. It needs an embeddings model API key which it doesn't have out of the box. Lots of these tiny "gotchas" about things OpenClaw could / should do but that as a user I wasn't aware weren't working yet.

- It keeps biasing towards suggesting to me a few options to get things done, then suggesting to start with the fastest (not the "best"). I end up going back and forth a bit to push it to help me pick the best path forward (not just the fastest)

- **My Spiral**: I feel super powerful and like anything is possible…but also so fragile and that anything could break at any moment….but then I remember that I could just ask AI to help me fix my AI if things go wrong (screenshots into Gemini for the rescue)….but when it does randomly break (and it definitely still does) it's still scary each time and I don't know if I'll be able to fix it in 10 minutes or 10 hours (I've gone down many of these hours long spirals)…and while there is an argument to say that models will get better and thus they will break less or be faster to fix when they do (so I shouldn't worry about this 10 min vs. 10 hour question because we're trending towards 10 mins with more capable models) - i counter that with the realization that systems will get more advanced and find new ways to break (which then gets me back into a lot of 10 hour spirals because the systems get complicated before the model can catch up)...and as these systems get bigger this stress grows and compounds (because now there's even MORE in the black box I don't understand)….but then I think that maybe the size of the blackbox is more like a black hole where the underlying model takes care more of what used to be products/services - so the agent/app I build on top will still feel like it's staying relatively the same size (even though the underlying core got a heck of a lot denser)

- I'll have things setup and working (the way lulubot tells me it should be done) - then someone will tell me about a different way to do it, and it will all of a sudden realize that that's a better way…then I'm back to building things….which leads to never being sure if the system actually is the best setup (pretty sure I have a lot of bloat in there)

- I want my agent to just get smarter by itself - it's not there yet. Interestingly(?) there are a bunch of "agent schools" popping up…if I could have my agent constantly run a subagent to look up other skills that might be helpful for it to learn…could be cool.

- Honestly, if I wasn't in a separate chatgroup on Telegram with a bunch of people constantly talking about and posting random OpenClaw things, I'd be a lot more lost (there's a Discord chat but I haven't had time to look into there)

- One thing is for sure - the excitement is real! Having attended the first ever ClawCon last night was a total blast!

(Description: Two photographs from ClawCon event. Top image shows a conference hall with an audience of people seated and standing, facing a presentation screen with a speaker visible in the crowd. Bottom image shows a close-up selfie of three smiling attendees at the event.)

---

**Published**: 1:54 PM · Feb 5, 2026  
**Views**: 94.8K  
**Engagement**: 39 replies, 73 reposts, 546 likes, 1038 bookmarks