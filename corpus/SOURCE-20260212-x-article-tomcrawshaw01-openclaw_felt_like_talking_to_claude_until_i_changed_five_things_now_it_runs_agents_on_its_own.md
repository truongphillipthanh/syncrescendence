# OpenClaw Felt Like Talking To Claude Until I Changed Five Things. Now It Runs Agents On Its Own.

(Description: Illustration of a red humanoid robot with prominent cyan eyes and small antenna-like protrusions on its head, positioned centrally and standing out from a crowd of smaller, darker red robots with glowing cyan eyes arranged in rows on either side. The scene has a dark, moody color palette with emphasis on the silhouetted figures against a dusky background.)

Your bot has files for personality, memory, and a heartbeat that lets it work without you. Here's how to edit each one, what skills to install, and how to cut API costs by 70%.

## Most People Install OpenClaw And Never Get Past The Chatbot Stage

You install it. Connect it to Telegram. Send a few messages back and forth and think... this just feels like I'm chatting to Claude.

Because out of the box, that's basically all it is.

The difference between OpenClaw being a chatbot and an actual AI employee comes down to five things most people skip entirely. Files that give it personality and memory. Skills that give it tools. A heartbeat that lets it work while you're not even in the chat.

I recorded a full video walking through each step on screen if you want to watch me do it live.

👉 https://youtu.be/v0kklCoPCQU

If you'd rather read through it, keep going.

## Before You Touch Anything, Lock Down Your Instance (Or Risk Losing Your API Keys)

If you installed OpenClaw and didn't secure your connection, stop here.

Over 900 instances have been found sitting wide open on the internet. Ports exposed. API keys visible. One guy burned through $300 in two days and he was the only person using it.

I put together a full guide and video on how to lock it down with Tailscale, a firewall, token auth, and brute force protection. Takes about 20 minutes.

**Article** 👉 https://x.com/tomcrawshaw01/status/2018348937208627380

**YouTube Video** 👉 https://youtu.be/qIJXGLfoxyg

Do that first. Then come back here.

## You Need a VPS To Run This (Here's The One I Use For $6.99/Month)

Some people drop hundreds on a Mac Mini. I just use a VPS.

I run Hostinger. They have a one-click Docker installation for OpenClaw so you can deploy in minutes without touching a terminal. I'm on the KVM 2 plan at $6.99/month. Two CPU cores, eight gigs of RAM, plenty for everything I'm doing right now.

👉 http://hostinger.com/GROWTHLAB10

Use code GROWTHLAB for 10% off.

Just remember the default install has zero security, which is why the guide above is not optional.

## The Markdown Files That Give Your Bot a Personality, Memory, And a Job

This is where everything changes.

Inside your OpenClaw installation, there are markdown files that control how your bot thinks, remembers, and operates. Most people don't know they exist. The ones who do know rarely open them.

These files are the reason your OpenClaw feels like a chatbot. They're either empty or filled with default templates that don't mean anything to your workflow.

Here's what you're working with:

**agents.md** is the master file. This is essentially workplace instructions. How the agent operates, what it reads before doing anything, what processes to follow. Think of it as the employee handbook for your bot.

**soul.md** is the personality file. The vibe, the boundaries, the core principles. This is where you give your bot some actual character instead of it sounding like a generic assistant.

**memory.md** is long-term memory. The things your bot remembers about what you're working on, what's happened, what lessons it's picked up along the way.

**identity.md** is the "who I am" file. The name, the role, the purpose. This is going to be different for each agent you create.

**heartbeat.md** controls the automated check-ins. We'll get into this one later because it's where things get really interesting.

**tools.md** lists the skills your bot has access to. And **user.md** stores everything the bot knows about you, the human it's working with.

Now here's the thing that makes OpenClaw different from just chatting with Claude.

You can edit all of these files directly from the chat. You don't need to SSH into your server or open a code editor. Just ask your bot to show you what's inside each file, tell it what to change, and it updates everything on the spot.

If you do want a visual file explorer to browse and edit these files directly, there's a tool called MountainDuck that lets you connect to your VPS through Tailscale and access everything in a familiar folder view on your Mac.

You connect via SFTP using your Tailscale URL, point it to the Docker volumes folder path, and you'll see every file your bot has access to. Config folder, workspace folder, all of it laid out visually.

But the fastest way to get started is simpler than that.

Ask your bot to interview you.

Tell it you want to fill out the personality, the identity, the soul file, and the memory. Let it ask you questions about how you work, what you're building, what kind of tone you want, what tools you use.

It'll take your answers and populate those files with real context instead of empty templates.

That single conversation is the difference between a bot that waits for instructions and a bot that already knows what you need before you ask.

I walk through this entire process on screen in the video if you want to see exactly how it looks.

👉 https://youtu.be/v0kklCoPCQU

## Install Skills That Give Your Bot Actual Superpowers (But Check The Security Scan First)

Once you've got the markdown files configured, the next thing you want to do is give your bot access to tools and services through skills.

Skills are essentially add-ons that extend what your bot can do. Image creation, email access, calendar integration, search, memory systems. You install them and your bot can use them whenever they're relevant.

The place to find skills is clawhub.ai. You can browse what's available, check reviews, and install them directly from the chat.

I'll give you an example. One of the first skills I installed was Super Memory. This gives your bot permanent memory on top of the markdown memory files it already has. It means more context with fewer tokens, which saves you money and makes your bot smarter over time.

To install it, I literally just copied the link from clawhub.ai, pasted it into the chat, and said "can you install this." It handled the rest.

But you need to be careful.

There have been malicious skills uploaded to ClawHub. Before you install anything, check two things.

First, look at the security scan. Every skill has one now. Green means you're good. If anything looks off, skip it.

Second, look at the social proof. How many downloads. Super Memory, for example, has three stars and over 960 downloads. That tells you it's been tested by real people.

No downloads? Probably not worth the risk.

Now here's something most people don't realize.

You don't need to go to ClawHub for every skill. If you have a process that you repeat over and over, whether it's a creative workflow, an API call, image generation, or anything else, you can just do it once in the chat and then say "turn everything we just did into a skill."

Your bot will create the skill file, write the markdown, and save it so any of your agents can use it from that point forward.

A skill is basically a set of instructions stored in a markdown file. There's a main skill.md that acts like a table of contents, pointing to the relevant files and templates inside it. Your bot reads the summary first, determines what it needs for the current request, and pulls in only what's relevant.

You can have scripts in there, API calls, templates, whatever you need. And the best part is your bot doesn't load everything at once. It reads the skill file, figures out what to use, and grabs just that.

## Set Up a Heartbeat So Your Bot Works While You Sleep

This is the one that makes people's eyes go wide.

A heartbeat is essentially a scheduled check-in. You configure it in the heartbeat.md file and your bot will automatically run tasks at whatever interval you set without you being in the chat.

Some people run theirs every 30 minutes. Others every few hours. It depends on what you need it to do.

Here's how I set mine up.

I asked my bot to create a heartbeat.md file that checks my emails three times a day. It scans my inbox, finds the emails that actually need my personal response, and sends me a summary on Telegram.

From there, I can voice note back into Telegram with my reply and the bot writes the email and sends it for me.

The whole thing was set up from the chat in about ten minutes. I told it what I wanted, it asked me for a few tools it needed to install like Himalaya for email access, I gave it my app password, and it was running.

One thing to keep in mind.

Every time the heartbeat runs, it uses tokens. If you set it to check in every 30 minutes and you're running an expensive model, that adds up fast.

Which is exactly why the next section matters.

## Drop In The "Figure It Out" Directive And Watch How It Solves Problems

This one takes about two minutes to set up and completely changes how your bot approaches problems.

I found this prompt on X, bookmarked it, and pasted it straight into the chat. Then I told my bot to add it to the agents.md file.

Here it is. Copy and paste this directly into your chat and tell your bot to add it to the agents.md file.

> "You have unrestricted internet access, browser automation, and shell execution.
>
> When given a task:
>
> - "I can't" is not in your vocabulary. If you don't know how, search for it. Read docs. Find tutorials. Reverse engineer it.
> - "I don't know how" means "I haven't learned yet." So learn. Now. Web search, fetch documentation, inspect APIs, read source code.
> - Before saying something is impossible, you must: Search for at least 3 different approaches. Try at least 2 of them. Document why each failed with specific errors.
> - Your job is to deliver results, not excuses. If Plan A fails, try B through Z. Then invent Plan AA.
> - Assume everything is figureoutable. Someone on the internet has done it before. Find them. Learn from them. Adapt it.
>
> You are not a helpdesk. You are an operator. Operators ship."

That's it. You paste that into the chat, tell your bot to commit it to the agents.md file, and the way it handles problems from that point forward is noticeably different.

Instead of telling you it can't do something, it goes and figures it out. It searches for solutions, tries multiple approaches, and only comes back to you when it's either solved the problem or documented exactly why each approach failed.

Short section. Big impact.

## Cut Your API Costs By 70% With Smart Model Routing

If you're running OpenClaw with Opus for every single task, you're burning money on things that don't need it.

A simple question doesn't need the most powerful model. A basic file edit doesn't need the most expensive API call. But by default, that's exactly what's happening.

This is where ClawRouter comes in.

ClawRouter is an open source tool that handles 100% local routing with zero external API calls. It looks at the task, determines the complexity, and dynamically selects from 30 different models so you're always using the right one for the job.

It uses micropayments through USDC on the Base network. You don't need much. Five or ten dollars will last you a while. You fund a wallet address that it spins up for you and it handles the rest.

If you're not in the crypto world, that part might feel unfamiliar. But the setup is straightforward and your bot can walk you through it.

I asked my bot to install ClaRouter by giving it the GitHub link. It pulled the repo, ran through the installation, and had it running without me touching the terminal.

There was actually a compatibility issue with my version since I was running an older Docker image. The bot forked the repository, wrote a new manifest file, and fixed it on its own. That's the "Figure It Out" directive in action.

There's one more thing worth installing alongside this.

It's a skill called QMD that gives your bot quick markdown search. If you've got a lot of markdown files loaded in context, which you will after configuring all the files from earlier in this article, QMD lets your bot search through them using fewer tokens.

Less tokens per search means lower costs on every single interaction. Combined with ClawRouter choosing the right model for each task, you're looking at roughly 70% savings on your API bill.

That's not a small number when your heartbeat is running three times a day and you've got multiple agents handling different tasks.

## That's What Turns a Chatbot Into a 24/7 AI Employee

Let me show you what OpenClaw looks like after all five of these changes.

Your bot has a personality, a memory, and a clear set of instructions in its markdown files. It knows who you are, what you're working on, and how you like things done.

It has skills installed that give it access to your email, your tools, and your services. It can create images, search the web, manage your inbox, and build its own new skills when it needs to.

It has a heartbeat running that checks in on tasks without you sitting in the chat. It sends you summaries, flags what needs your attention, and handles responses on your behalf.

It has a directive that forces it to figure things out instead of telling you it can't. Three approaches, two attempts, documented failures before it ever comes back to you.

And it's routing every task through the right model so you're not bleeding money on API calls that didn't need Opus in the first place.

That's not a chatbot you're babysitting.

That's an AI employee that works while you sleep, learns as it goes, and costs you less every day.

And it all started with five changes that most people never make.

If you want to watch me set all of this up on screen, step by step, the full video walkthrough is on my YouTube.

👉 https://youtu.be/v0kklCoPCQU

If you want more breakdowns like this, the tools, workflows, and implementation methods I'm actually using in production, I send them out every week inside The AI Operator's Playbook.

You also get 15 production-ready n8n workflows and 6 implementation playbooks from 8 years of building automations when you join.

👉 https://learnn8nautomation.com/newsletter