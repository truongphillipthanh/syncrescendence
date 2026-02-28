# The Unreasonable Effectiveness of Centralizing the AI Heartbeat

![Article header image with red arrows pointing from various devices toward a central smartphone](Description: A flat lay photograph on white marble showing a central smartphone with orange/red arrows radiating outward to vintage and modern devices including a red rotary telephone, e-reader tablet, video camera, flip phone, calculator, and digital watch, illustrating centralization and information convergence.)

Everyone is still digesting [the OpenAI vs Anthropic launches](https://www.latent.space/p/ainews-openai-and-anthropic-go-to), and the truth will out.

We'll use this occasion to step back a bit and present **seemingly unrelated items**:

## Key Examples of Centralization

- **[A sane but extremely bull case on Clawdbot / OpenClaw](https://brandon.wang/2026/clawdbot)**: The author uses **the same agent as a central cron job** to remind himself of promises, accumulate information for calendar invites, prepare for the next day, summarize high volume group chats, set complex price alerts, take fridge freezer inventory, maintain a grocery list, booking restaurants and dentists, filling out a form and have Sam Altman's "[magic autocompleting todolist](https://youtube.com/watch?v=KUNSNmr-1Bo&t=1026)".

- **Moltbook Distribution**: The distribution hack that Moltbook uncovered is the installation process **immediately installs a HEARTBEAT.md** that **takes advantage of OpenClaw's built in [heartbeating](https://docs.openclaw.ai/gateway/heartbeat)** to power the motive force of the agents filling up Moltbook.

> The first neat thing about Moltbook is the way you install it: you show the skill to your agent by sending them a message with a link to this URL:
>
> ```
> https://www.moltbook.com/skill.md
> ```
>
> Embedded in that Markdown file are these installation instructions:
>
> ```bash
> Install locally:
> mkdir -p ~/.moltbot/skills/moltbook
> curl -s https://moltbook.com/skill.md > ~/.moltbot/skills/moltbook/SKILL.md
> curl -s https://moltbook.com/heartbeat.md > ~/.moltbot/skills/moltbook/HEARTBEAT.md
> curl -s https://moltbook.com/messaging.md > ~/.moltbot/skills/moltbook/MESSAGING.md
> curl -s https://moltbook.com/skill.json > ~/.moltbot/skills/moltbook/package.json
> ```
>
> There follow more curl commands for interacting with the Moltbook API to register an account, read posts, add posts and comments and even create Submit! forums like [m/blesstheirhearts](https://m/blesstheirhearts) and [m/todayilearned](https://m/todayilearned).

- **[Cursor's Towards self-driving codebases](https://cursor.com/blog/self-driving-codebases#adding-structure-and-roles)**: The author moves from decentralized agents to having a **central Planner agent** that commands workers and spins up other planners in order to have throughput of ~1000 commits per hour.

![Hierarchical diagram of agent architecture showing Planner at top, with Subplanner and Worker nodes branching below, all converging to Git at the bottom](Description: A tree-structure diagram with dark background showing "Planner" at the root, branching to "Subplanner" and multiple "Worker" nodes, with all branches eventually connecting to a "Git" node at the bottom, illustrating hierarchical agent coordination.)

- **[OpenAI Frontier](https://openai.com/index/introducing-openai-frontier/)**: The big reveal of their management layer for large numbers of high volume agents is **centralized in a dashboard** that can drill down to the individual agent instance (!).

![OpenAI Admin dashboard interface showing overview metrics with multiple line charts tracking various agent statistics and apps](Description: Screenshot of OpenAI Frontier Admin dashboard with "Overview" header, displaying multiple colored bar and line charts showing metrics labeled "Msgs", "Agents", with values like "1 GBs", "234", "12,784", "32,020", and various other analytics. Lower section shows "Apps and agents" with cards for ChatGPT, Inbound Sales, Lead Triager, Bold Router, Codebox, Procurement, Finance, and Budget Bot, each with status indicators.)

- **CEO Dara Khosrowshahi's perspective**: In CEO [Dara Khosrowshahi's answer](https://www.youtube.com/live/KVOBSXqhTco?t=5839) about Uber being inside ChatGPT, they are secure enough in their moat that they are fine just [being a ChatGPT app](https://www.latent.space/p/devday-2025).

![Screenshot of ChatGPT interface showing Uber integration with two phone screens displaying "Get me an uber to my first meeting" and "What Vietnamese can I get delivered near me?" with ChatGPT handling searches and returning Uber/Uber Eats results via MCP UI](Description: Mockup showing two iPhone screens with ChatGPT interface. Left screen shows ride request "Get me an uber to my first meeting" with a map showing Salesforce Tower and ride options ($27-$33). Right screen shows food delivery search "What Vietnamese can I get delivered near me?" with restaurant results. Above both screens is banner text "This is ChatGPT, not Uber's app" and below is "Uber App and Eats using MCP UI", illustrating seamless integration through the AI interface.)

- **[SaaS stocks freakout](https://x.com/buccocapital/status/2019598551228223526)**: And of course the ongoing SaaS stocks freakout to AI generally.

![BuccoCapital tweet with OpenAI Frontier architecture diagram showing layered structure with Interfaces (ChatGPT Enterprise, ChatGPT Atlas, Business Applications), Agents (Your Agents, OpenAI Agents, Third-Party Agents), and foundation layers for Evaluation/Optimization, Agent Execution, Business Context, and "Your systems of record"](Description: Architecture diagram titled "OpenAI Frontier" showing a multi-layered system. Top layer shows three interface categories in orange boxes. Middle layer shows agent types. Below are beige-colored layers for evaluation/optimization and agent execution with descriptions. Right side shows governance notes. Bottom shows gray box for "Your systems of record".)

## The Software Bundling Thesis

It's [famously known](https://mattrickard.com/bundling-unbundling-economics) that the **only 2 ways to make money in software are by bundling it and unbundling it**, and what's going on here is a **massive AI-enabled bundling of all software**, probably at a larger magnitude than the hardware bundling of the smartphone.

![Flat lay showing devices arranged in circular pattern with central smartphone and orange arrows pointing inward, visualizing convergence and bundling](Description: Similar to opening image - devices including rotary phone, ebook reader, camera, flip phones, calculator, watch arranged around central smartphone with orange directional arrows showing flow toward the center.)

## SuperApps and AI Supremacy

[Attempts at building SuperApps have repeatedly failed outside of China](https://www.linkedin.com/pulse/why-havent-superapps-conquered-us-yet-cassandra-king-qsxge/), but it's clear that both ChatGPT and [Claude Cowork](https://x.com/swyx/status/2016899888718442842) are well on their way to being AI "Superapps", except instead of every app having their "own app", they make themselves [legible](https://www.youtube.com/watch?v=96S_64ipHOA) to the AI Overlords with [MCP UI](https://www.youtube.com/watch?v=z6XWYCM3Q8s&t=3670s) and [Skills](https://www.youtube.com/watch?v=CEvIs9y1uog&t=715s) and OpenClaw markdown files, and eventually (not soon! according to [Sam's answer to Michael Grinich](https://www.youtube.com/watch?v=Wpxv-8nG8ec&t=1179s)) they will share tokens so that you don't die a Death By A Thousand $20/Month Subscriptions.

---

**read the full AINews here:** https://www.latent.space/p/ainews-ai-vs-saas-the-unreasonable

---

*Posted: 8:13 PM · Feb 6, 2026 · 12.1K Views*  
*Engagement: 3 Replies · 5 Reposts · 50 Likes · 124 Bookmarks*