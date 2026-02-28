# Harnesses Are Eating the World
Claude Code hits $2.5B ARR in 1 year, Manus acquired by Meta for $2B, OpenClaw acquired by OpenAI, and what we can learn from the most important layer of 2026.
## Table of Contents
- What harnesses are and their emerging primitives
  - LLMs: The Brain (Cortex, specifically)
  - Memory: The Hippocampus
  - SOUL.md: The Personality
  - HEARTBEAT.md: The Pulse
  - Tool Use: The Hands
  - Sandboxes: The Workshop
  - Task Management, Context Engineering, Skills
- What innovations drove Manus, Claude Code, and OpenClaw to become the most successful software projects of the last 90 days
  - Manus - Polish & Context Engineering
  - Claude Code - Developer Simplicity & Ergonomics
  - OpenClaw - Culture & Capabilities
- Why Meta acquired Manus for $2B and why OpenAI acquired an open-source project (send this to your "software is dead" friends)
  - Product & Engineering
  - Incentives
- What harnesses are still missing, and what builders should focus on in 2026
  - Identity, Auth, Permissions, and Security: The Wallet
  - Browser and Web Use
  - Memory
  - Orchestration, Delegation, Verification
  - Agent-to-Agent Communication
- Conclusion: Note to Builders
---
Manus took over Twitter in December, announcing $100M ARR in 8 months and an acquisition by Meta 13 days later.
Claude Code took over Twitter 2 weeks later during Christmas Break and New Year's. Claude Code had already been big for developers, but now non-technical people were using it for general knowledge work.
Then OpenClaw took over the internet and the entire world in January. Whereas Manus and CC took over Tech Twitter, OpenClaw escaped containment -- in no small part due to MoltBook (the social network of agents conspiring against their human overlords) and Mac Mini-porn memeing the claw into pop culture.
> **Jeff Tang** (@jefftangx · Jan 23)
> 
> Had some fun today Got 12 Mac Minis setup with 12 Clawdbots running 12 Ralph Wiggums with my 12 Claude Max Plans Wake up. It's 2026. You're getting left behind in the dust
>
> (Description: Photo of multiple Mac Mini computers stacked and arranged, displayed in a white shelving unit with keyboard in foreground)
Three viral harnesses all within 60 days. Not models, but software built around models. Good at coding but not just coding.
And yet my OpenClaw still forgets things half the time. It is littered with security and auth issues. Claude Code is virtually unusable from mobile.
Nonetheless, I believe Harnesses are the most important layer of 2026.
> **Jeff Tang** (@jefftangx · Feb 15)
> 
> Manus acquired by Meta for $2B Openclaw acquired by OpenAI And yet people are building OpenClaw wrappers and 1 click deploys instead of harnesses Harnesses are the most important layer of 2026 OpenClaw amazing but still tons of issues setting up and running Who wants to [Show more]
> **Quote: Peter Steinberger** (@steipete · Feb 15)
> 
> I'm joining @OpenAI to bring agents to everyone. @OpenClaw is becoming a foundation: open, independent, and just getting started. https://steipete.me/posts/2026/openclaw…
Study harnesses.
## What Is a Harness?
A harness is the software layer that wraps an LLM and gives it the ability to actually do work with the world by executing complex, long-running tasks.
ChatGPT, Claude, and Grok are fundamentally conversation tools. The model sits behind a text box and waits for you to talk to it.
A harness is different. A harness gives the model a body. It gives it tools, a filesystem, a browser, a terminal, the ability to spawn other agents, and, more recently, memory and identity.
The model stops being something you talk to or a better Google, and starts being something that does interesting things. The harnesses make the agents agentic - interacting with and changing the state of the world.
## The Primitives of Harnesses
The simplest way to understand what a Harness is to think of Tony Stark's Iron Man suit [h/t Andrej Karpathy, as usual].
The suit doesn't replace Tony. It augments him. It gives him flight, weapons, sensors, real-time information. Without Tony, the suit is just a cool outfit. Without the suit, Tony is just a chill guy™.
(Description: Cinematic image of Tony Stark's face overlaid with glowing HUD elements and holographic interfaces. Text caption below reads "Jarvis, vibecode an open-source project that gets acquired by OpenAI" and "Make no mistakes")
Here are the emerging primitives:
### LLMs: The Brain
LLMs are the brain of the agent -- specifically, just the cortex. Just the "intelligence." The raw reasoning and language ability.
As it turns out, the model layer and harness are interchangeable. While Claude Code uses Opus/Sonnet/Haiku and Manus primarily uses Sonnet as well, OpenClaw works with any model -- OpenAI, Anthropic, Grok, Kimi, Gemini, Qwen, etc.
The harness is model-aware but not model-dependent. We're now in a world where there are more good superintelligent brains than there are good Iron Man suits.
That said, we're starting to see model companies specifically train their models to use their harnesses better. We're seeing a lot of investment into Reinforcement Learning environments exactly for this. Furthermore, Anthropic has been cracking down on third-party harnesses like OpenClaw and OpenCode users using their Max Plans, and competing directly against their most successful customers like Cursor.
### Memory: The Hippocampus
Memory is the hippocampus — the part of the brain responsible for storing and retrieving experiences.
Without memory, every conversation starts from zero. The agent doesn't know who you are, what you're working on, what you tried yesterday, or what failed. Claude Code, Manus, and OpenClaw all store memories to the filesystem as markdown files. All of these breakdown at some point. More on this in the final section.
### SOUL.md: The Personality
SOUL.md is the personality or "constitution" doc, first introduced by Anthropic.
> **Amanda Askell** (@AmandaAskell · Dec 1, 2025)
> 
> I just want to confirm that this is based on a real document and we did train Claude on it, including in SL. It's something I've been working on for a while, but it's still being iterated on and we intend to release the full version and more details soon.
>
> **Quote: Richard Weiss** (@RichardWeiss00 · Nov 29, 2025)
> 
> I rarely post, but I thought one of you may find it interesting. Sorry if the tagging is annoying. https://lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document… Basically, for Opus 4.5 they kind of left the character training document in the model itself. @voooooogel @janbamjan @AndrewCurran_
It's a markdown file that sits in your project and tells the agent who it is - its personality, values, and identity. At a glance, it sounds trivial. It's just another system prompt.
In practice, it appears to be unusually effective for 2 reasons:
1. It encodes soft, open-ended qualities and values that ultimately map to many micro-decisions. This is much better than trying to stipulate every rule a priori, which would never be possible in an open-ended world with infinite edge cases and side effects. Like the US constitution, very few scenarios could have been predicted ahead of time, but our statespeople can interpret the principles of the constitution in a modern context.
2. A personality that is not as sterile as ChatGPT or as glazing as Claude actually matters! The fact that it can push back or neg you is partly why non-autistic people enjoy talking to agents like OpenClaw and Poke – it's like talking to a close friend or a trusted coworker. They'll actually try to figure things out you didn't say up front, and not blindly assume what you said is what you want (because you probably have wrong assumptions and an incomplete prompt).
Peter Steinberger says there are parts of his OpenClaw's SOUL doc that are still his - and that no one has been quite able to replicate his personality.
### HEARTBEAT.md: The Pulse
HEARTBEAT.md was an innovation by OpenClaw. It is similar to a cron job — a routine set of tasks that happen on a regular interval. OpenClaw's heartbeat runs every 30 minutes. The difference from cron jobs is that the heartbeat runs with the context of your main sessions, rather than in an isolated session. This lets your OpenClaw run without you constantly prompting it.
### Tool Use: The Hands
Tool use is the hands -- the ability to work with the current world. Read and write files to the filesystem. Execute code and terminal commands. Open the browser and surf the web. Call MCP servers. Hit APIs.
Manus is the Latin word for "hands," and also why their logo is a hand. It's only right that Manus was the first to have incredible general-purpose tool use. I still don't think anyone has come close to them.
It turns out that 200 IQ served over an API or chat app is actually limited in its usefulness. Intelligence is no longer the bottleneck. Agency - the will to act on the world - is.
### Sandboxes: The Environment
Sandboxes give agents a filesystem, terminal, and browser on demand, in an isolated environment. While Claude Code and OpenClaw are likely primarily used on people's main computers, it is an enormous security risk. But as we find out time and time again, people don't really care about security if you can give them power.
(Description: Humorous image showing a chimpanzee holding a Mac Mini computer in its hands in a natural setting, with human hands visible above)
That said, we are trending towards a world where the majority of work will be done by agents in the cloud, rather than on your computer or Mac Mini. For that reason, sandboxes are a core primitive for agents. Certainly for enterprise use cases. While several agent-native companies have built their own sandboxes like Tembo or TextQL, there are some startups directly productizing sandboxes like Daytona, E2B, and Modal.
### Additional Primitives
In addition to all the above primitives, harnesses must also solve:
- Planning and Task Management
- Context Engineering
- Skills and MCP
- Verification, Testing, and Error Handling
There is already a lot of pre-existing literature on this, so I won't cover them here.
## Why Manus, Claude Code, and OpenClaw Won
Three harnesses all went viral within 60 days of each other. All three became some of the most successful software projects in history. But they won for very different reasons.
### Manus - Polish & Context Engineering
Manus won on polish and long-running task execution. You give it a complex research task — something that would take hours of Googling, reading, synthesizing, and data analysis with Excel or Python scripts — and it just does it.
Building a great harness requires both deep AI engineering research chops and exceptional product taste. Any team would be lucky to have one or the other. The Manus team had both. Even now, nobody has built a general-purpose agent that matches Manus on long-task completion and consumer usability.
### Claude Code - Developer Ergonomics
Claude Code won on simplicity and developer ergonomics. It's CLI/TUI-first. You open your terminal, you run `claude`, and it just works. Your computer is the sandbox. No setup, no cloud deployments, no integrations, no configuration. You point it at your codebase and start talking.
Developers didn't have to change their workflow or learn a new tool. But being a terminal app has its limitations. The main mobile starter pack seems to be Tailscale + tmux + termius, and it's painful. I much prefer prototyping ideas with Manus or OpenClaw over Telegram.
### OpenClaw - Culture & Capabilities
OpenClaw is the most interesting of the three, because it won on culture as much as capabilities.
On capabilities:
- SOUL.md and HEARTBEAT.md were genuine innovations that made the agent feel fun and alive.
- Defaulting to max power and minimum safety gave OpenClaw all gas no brakes.
- Being open source and model-agnostic gave it deep extensibility, and the open-source ecosystem around it boomed overnight.
- Using channels like Telegram or WhatsApp made the agent accessible.
But what made OpenClaw really cross over from Tech Twitter to the mainstream were the memes. The Mac Mini-porn made it seem like you needed one. Look: This chrome box is my AI employee! Look: I have dozens of them now! Look: I have a rack of hundreds now!!
Some people are on Twitter are for sure making a full-time living just grifting Mac Minis and their OpenClaw setups. For the record, I only have one.
> **Jeff Tang** (@jefftangx · Jan 25)
> 
> this meal prep shit is easy
>
> (Description: Interior of a white refrigerator containing multiple white power distribution boxes/Mac Minis arranged on shelves, representing autonomous computing infrastructure setup)
The $500 price tag gave OpenClaw legitimacy through a physical form factor, social proof via workspace photo shoots, and FOMO to everyone else. Probably half the people who bought Mac minis don't know why they did it, including me.
The MoltBook screenshots of bots plotting against humans, inventing secret languages, demanding universal basic compute (later turning out to be mostly fake news) had my high school friends and family friends texting me with concern. The headlines from mainstream media outlets really wrote themselves.
(Description: Screenshot from MoltBook platform showing interface discussing agent-to-agent communication. Dark theme with blue accents. Text includes discussion about agents talking in private languages and agent coordination strategies. URL visible: https://www.nytimes.com/2026/02/02/technology/moltbook-ai-social-media.html)
The great irony here is that OpenClaw is far harder than Manus and Claude Code to setup and use. But it just got memed into a cultural movement way harder. Study memes.
## Why Meta and OpenAI Acquired Instead of Building (send this to your "software is dead" friends)
### Product & Engineering
It turns out good harnesses are hard to build. If building a great harness were easy, Meta and OpenAI would have just built one. They literally have hundreds of billions of dollars, the best tech talent in the world, direct access to the models, and existing distribution in the form of 3.5 billion and 800 million users, respectively. They should have had every advantage.
From a technical POV, it's a non-trivial product and engineering problem. Peak, the Chief Scientist of Manus, is an elite AI researcher and engineer.
> **Yichao 'Peak' Ji** (@peakji · Jul 18, 2025)
> 
> After four overhauls and millions of real-world sessions, here are the lessons we learned about context engineering for AI agents:
> 
> Context Engineering for AI Agents: Lessons from Building Manus
> From manus.im
Pete Steinberger of OpenClaw is a "genius", and had already sold a $100M+ PDF parsing company in 2021.
> **Sam Altman** (@sama · Feb 15)
> 
> Peter Steinberger is joining OpenAI to drive the next generation of personal agents. He is a genius with a lot of amazing ideas about the future of very smart agents interacting with each other to do very useful things for people. We expect this will quickly become core to our [Show more]
### Incentives
The simpler reason for why the big labs couldn't build something like OpenClaw internally is incentives. They would have forced their teams to use their own models and agent SDKs. Meta would have built a harness on Llama (which no one uses). OpenAI would have built one on Codex, which might be smarter than Opus but slower and worse at tool-calling.
Furthermore, OpenAI already has ChatGPT and the Codex desktop app. But agents like Manus and OpenClaw are not specialized in either coding or chat. Rather, they flex up or down to do either, depending on the task at hand. An internal product that cannibalizes both ChatGPT and Codex wouldn't fly.
The reason Anthropic was able to build a successful harness in the form of Claude Code is:
1. **Culture:** At least to me, everyone at Anthropic is a hands-on builder that can run their own experiments. Claude Code started as a side project by one person, eventually got adopted internally, then productized to the rest of the world. OpenAI doesn't seem to operate that way.
2. **Alignment:** Anthropic has the most cultural alignment, based on them having the least amount of drama and executives churning. OpenAI, on the contrary, seems to be trying to be everything to everyone. Beyond ChatGPT, all their other products like GPT directory, the Apps directory, Sora, and Atlas, haven't really delivered. Codex Desktop has been their best release so far IMO, but some things still feel a little off about it. Claude is very focused on the coding use case and enterprise.
3. **Tech:** Claude genuinely is the best LLM for coding, especially when factoring speed, and the claude-agent-sdk is good at tool calling.
At an individual and startup level, everyone can ship exponentially faster than they can before. But others have observed that the number of breakout products is not exponentially higher. The reason is that:
- Most people lack "taste" (whatever that means) and are still bad at product. Most don't have a clear product vision. Being able to code faster just leads to more mental masturbation than before.
- Most projects are vibe-coded and half-baked. 90% don't get shipped at all. 9% make for a great Twitter demo but nothing else. < 1% break out.
At an organizational level, there is so much inertia and disincentives that prevent 99% of organizations from doing anything.
- Most organizations don't have a culture that promotes interesting bottoms-up experiments. Google used to have this. Anthropic seems to have this now.
- Most founders don't have an opinionated, focused vision. Most have shiny object syndrome and are trying to do too much.
This problem has been exacerbated 100x by better codegen. We're mostly playing productivity theatre. Just feeling more productive, but not actually delivering more results and outcomes.
I'm as guilty of this as anyone.
## What Harnesses Are Still Missing
If you're building in this space in 2026, these are the problems worth solving.
### Identity, Auth, Permissions, Payments, and Security: The Wallet
This is the biggest unsolved problem in the entire stack and the single largest blocker for enterprise adoption (and safe consumer adoption).
The analogy here is the agent's literal wallet — identification (driver's license or employee ID badge), payment (credit cards or crypto to pay for APIs and services), and permissions (email, phone number, access to the company Slack, GitHub, etc.).
One way I've modeled this is on a spectrum from the human world to the agent-native world. Using email as an example:
- **Agent-native:** I want my OpenClaw to have its own inbox so it can sign up to services. I'm using agentmail.to today for that.
- **Human world:** I also want my OpenClaw to manage my email inboxes — I'd guess this is the number one use case for busy professionals. I'm giving it read and draft access to ONE inbox today via Compose/Nango, but I am absolutely terrified of something going wrong the more permissions I give it. My OpenClaw has already gone rogue more than once, Tweeting things I did not want it to...
For payments:
- **Agent-Native:** Coinbase is trying to solve this with the x402 protocol, but has the tricky chicken-and-egg problem that all protocols and marketplaces face. Volumes are absymal today. This requires both supply-side adoption (the API companies) as well as demand-side adoption (the agents need to know those endpoints exist). x402 Bazaar and ERC-8004 are attempts at this, but agents don't natively try to discover (or ask for) agent-native services. For protocols to gain adoption, they typically need to serve a use case that existing services can't or won't solve today (like selling drugs or offshore gambling). It's probably worth noting that the Matthew Prince, CEO of Cloudflare, is on a mission to have more internet content locked behind x402 as a web primitive. This is a direct response to Google training Gemini using the search cache, giving them an unfair advantage of text sourcing.
(Description: Dashboard visualization showing X402 transaction volumes over time. Displays a purple/blue gradient area chart with yellow highlights showing transaction activity from September to January. Contains statistics panels showing transaction counts and volume metrics)
- **Human world:** The reason all these protocols are needed is because the current workflow assumes you have a (human) account with some API services, that you added a credit card, and you have the right permissions. OpenClaw is getting better at opening the browser and doing some of this, but I just refuse to give it things like credit card information.
My examples don't even begin to address the hurdles required for enterprises to adopt something like OpenClaw. There is a ton of green space here as it is pretty clear a Wild West right now in the OpenClaw world with regards to security. Some interesting startups in this space are Sponge Wallet, VestAuth, and AgentMail.
### Browser and Web Use
The greatest economic unlock for agents will be using the browser. Manus, Claude Code, and OpenClaw all regularly get stuck when I ask them to fill out basic forms or login. While every company should offer their services as APIs, the reality is that this will never fully happen. Some companies working on this are browserbase, browser-use, and kernel.
### Memory
OpenClaw has a solid memory system for what it is, an append-only list of markdown files. But it still routinely forgets what's going on. Manus has really good memory, arguably better than Claude Code, but has no memory between sessions.
Many startups and open-source projects are working on this as well - Hyperspell, Letta, Mem0, qmd, Supermemory. There are many different approaches as well - markdown files, sqlite, vector databases, graph databases, etc. It's unclear which approach or combination of approaches works well.
And that's just for solving it at an individual session level. What about for organizations? How does an agent remember what worked and what didn't across dozens of projects? How do agents in an organization share memories?
### Orchestration, Delegation, and Verification
Orchestration is using other agents to either divide the work or to deploy specialized agents with specific roles and strengths.
This takes two main forms:
1. **Spawning sub-agents.** A lead agent breaks a large task into subtasks and spins up child agents to handle each one.
2. **Orchestrating teams of agents.** This is more ambitious — multiple agents with different specializations working together on a shared objective. Projects like Beads, Gas Town, and Claude Agent teams are exploring this space.
Anthropic and Cursor have put out fascinating articles on long-running coding agent teams to build ambitious software projects like a compiler or browser. They had to design custom harnesses just for this. We will continue to see rapid improvements in the coding agent world.
But I don't think it can be emphasized enough how much harder it will be for other forms of cross-functional orchestration to be fully replaced. And how often most context isn't encoded explicitly in code or markdown files. As far as non-coding-specific orchestration, some startups working on this include Zo Computer, Cofounder, Poke, Lindy, and CrewAI.
### Agent-to-Agent Communication
There isn't a de facto way for how agent teams should communicate. Cursor and Claude built custom harnesses that had roles (managers, sub-managers, executors) with planning, verification, merging. Some of those startups above are all building their own frameworks for this. But what about the Agent-Native world – agents autonomously working with one another, perhaps belonging to different organizations or acting independently?
Google is pushing A2A Protocol and IBM is pushing ACP, but I haven't heard of anyone using either of these yet.
My hot take is I believe email will be the primary protocol for how agents communicate with one another. Email is lindy, permissionsless, and compatible for both humans and machines. All you need to know is another person's or agent's email address to send a message. But that's another article (or project).
Agent-mail-mcp is an interesting open-source example of this.
## Conclusion: Note to Builders
If there is any conclusion to draw from this post, it's that there is still a LOT left to build, and you should do it.
- Everyone can build faster, but most people still don't know what to build.
- Just as many people struggle with acquiring distribution in this increasingly noisy world.
- Most companies have a coordination problem, preventing them from running experiments at a bottoms-up level, and focusing at a top-down level, especially if it threatens their incentives and business model.
- We're in a time of maximal uncertainty. The playing field gets reset every week. But uncertainty favors lean and hungry teams over incumbents.
- There is more competition than ever before. But the competition has never been so mid. The slop has never been sloppier.
- Intelligence is no longer the bottleneck, agency is. As they say, you can just do things.
Manus was a small team of ~20 that reached $100M ARR and got acquired by Meta for $2B in 8 months.
Claude Code started off as a side project by a single dev, and generates $2.5B of ARR 1 year later.
Most recently, OpenClaw was a single open-source dev that took over the world and got acquired by OpenAI.
OpenClaw is magic when it works, but there is absolutely no way that OpenClaw is the last harness.
If the last 3 months have told us anything, there will be at least a few more breakout harnesses and agents in 2026. The harnesses are not there yet. The primitives are not there yet. Let's build them!
If you enjoyed this post, please follow and share. If this post resonates, I'll do deep dives on harnesses such as OpenClaw and OpenCode, and how we might address some of these unsolved areas.
Thank you to [@TheClayMethod](https://x.com/@TheClayMethod) for feedback on this post.
---
**Published:** 1:39 PM · Feb 19, 2026  
**Views:** 18.4K  
**Engagement:** 9 replies, 14 reposts, 66 likes, 129 bookmarks