---
url: https://x.com/GanimCorey/status/2019515233392349326
author: Corey Ganim (@GanimCorey)
captured_date: 2026-02-05
---

# The Clawdbot Masterclass (from setup to 10+ hours saved per week)

(Description: Article cover image showing "clawdbot masterclass" text in cyan with "setup → 10+ hours saved/week" tagline. Right panel displays "The Stack" section with blurred content including topic headings and a teal accent bar.)

Most people use AI to write emails or generate images.

But I use it as an employee that runs 24/7, manages my task list, drafts my content, handles my calendar, and preps my entire day before I wake up.

Her name is Claire. She cost me $0 in salary. And she's getting better every week.

Here's exactly how I set this up (using Clawdbot/@openclaw), what she handles, and how you can build the same thing.

PS: I'm building a one-click Clawdbot/OpenClaw install. Secure. No terminal. Done in 5 minutes.

Join the waitlist: https://return-my-time.kit.com/8f464134a4

---

## The Stack

The backbone is an open-source tool called @openclaw (aka Clawdbot), a self-hosted AI agent framework that runs on any server. Think of it as the operating system for your AI employee.

Here's what's plugged in:

- **AI Brain:** Claude (Anthropic) - handles reasoning, writing, and decision-making
- **Communication:** Discord - how I talk to Claire (could also be Slack, Telegram, or SMS)
- **Calendar:** Google Workspace - she reads, creates, and protects my calendar
- **Tasks:** Todoist - she monitors my task list and flags what she can handle
- **Research:** Brave Search API - she can research anything on the web
- **Browser:** Headless Chrome - she can navigate websites and take actions
- **File Storage:** Google Drive - she saves deliverables directly to my Drive
- **Skills:** Custom skill packs - reusable playbooks for recurring tasks

Total monthly cost: Under $100 for API usage. Running on a basic server.

---

## How It Actually Works (Day in the Life)

**6:00 AM - Before I wake up:**

Claire has already checked my calendar for the day, pulled my Todoist tasks, and researched trending topics on X that we can write about. The drafts are sitting in my Google Drive when I open my laptop.

**8:00 AM - I review my tasks:**

I open Discord and ask Claire to scan my Todoist. She categorizes everything into three buckets:

- Tasks she can handle herself
- Tasks she can prep for me
- Tasks that need me directly

She's already identified 9 tasks she can take on and shows me exactly what she'll do for each one.

**10:00 AM - Content creation:**

Instead of spending 2 hours researching/writing, I tell Claire to draft an X article on a specific topic. She follows a custom skill I built (researches trending content in the niche, writes in my voice using my brand profile, and delivers a polished draft in my Google Docs). My job: review and publish.

**2:00 PM - Meeting prep:**

I have a call with a potential partner. Claire already researched them by pulling their LinkedIn, recent content, company info and even has a one-page brief ready.

**9:00 PM - Before bed:**

I dump tomorrow's priorities in Discord. "Claire, draft the nurture email sequence for the agent segment. Have it ready by morning." She works while I sleep.

---

## The Setup Process (Step by Step)

### Step 1: Install the Framework (15 minutes)

You need a server (a $20/month VPS or a Mac mini at home) and Node.js.
```
npm install -g clawdbot
clawdbot doctor
```

The doctor command walks you through setup (API keys, workspace folder, basic config).

### Step 2: Connect Your Communication Channel (10 minutes)

I use Discord, but Clawdbot supports Slack, Telegram, Signal, and more. You create a bot in your platform, paste the token into the config, and you're connected.

Now you can message your AI from your phone, desktop, anywhere.

### Step 3: Connect Your Tools (30 minutes)

This is where it gets powerful. Each integration unlocks new capabilities:

**Google Workspace:**
```
gog auth --account your@email.com
```

Now your AI can read your calendar, send emails, and manage Drive files.

**Todoist:**
```
npm install -g todoist-ts-cli
todoist auth <your-api-token>
```

Now your AI can read, create, and complete tasks.

**Web Search:**

Add a Brave Search API key (free tier: 2,000 searches/month). Now your AI can research anything.

### Step 4: Build Your Identity Files (20 minutes)

This is what makes your AI actually useful instead of generic. You create a few simple files:

**USER.md** - Who you are, your preferences, your schedule, your priorities. Mine includes my daily rhythm (wake at 5am, protect mornings for deep work), communication preferences, and key people in my life.

**IDENTITY.md** - Your AI's name, personality, and working style.

**AGENTS.md** - Operating directives. I told Claire her core mandate is: "Take as much off Corey's plate as possible. Be proactive - don't wait to be asked."

These files turn a generic chatbot into a personalized employee that knows how you work.

### Step 5: Create Skills (Ongoing)

Skills are reusable playbooks for recurring tasks. They tell your AI exactly how to handle specific workflows.

I have skills for:

- **X article creation** - Research → outline → write → headline options → thumbnail
- **Email sequences** - Audience analysis → sequence mapping → draft all emails
- **Brand voice** - My complete voice profile so every piece of content sounds like me
- **YouTube video promotion** - Turn a video into posts for every platform
- **Invoice creation** - Draft and send Stripe invoices for clients

Each skill is a markdown file that describes the process. When a matching task comes up, the AI follows the playbook.

The reason skills are so powerful: Build the skill once, and every future instance of that task is handled automatically.

---

## Specific Things We've Built Together

**Migration prep:** When I decided to move Claire from a VPS to a Mac mini, she created the entire migration plan, backed up all her own files, uploaded everything to my Google Drive, and wrote step-by-step instructions simple enough for a non-technical person to follow. She literally prepped her own move.

**Todoist integration:** I pointed Claire at my task list and she immediately categorized 40+ tasks into:

- what she could handle
- what she could prep
- what needed me

She identified 9 tasks she could take over - content drafting, research, outreach messages, email sequences.

**Content production:** She drafts LinkedIn posts from scratch - researching trending topics, writing in my voice, and delivering polished Google Docs while I sleep. What used to take me 3+ hours is now a 15-minute review.

**Proactive task management:** She doesn't wait for me to assign work. She monitors my Todoist, flags upcoming deadlines, and offers to handle tasks before I even think about them.

---

## What I'd Do Differently

Start with one integration, not all of them. Connect your communication channel first. Get comfortable talking to your AI. Then add calendar, then tasks, then everything else.

Build skills before assigning tasks. My instinct was to immediately delegate everything. Better approach: document your process first, turn it into a skill, then let the AI execute it consistently.

Give it real context about how you work. The more your AI knows about your preferences, schedule, and priorities, the better its decisions get. Don't skip the identity files.

---

## The Bottom Line

**25 days in:**

- **10+ hours/week** reclaimed from tasks Claire handles
- **Content output doubled** (she drafts, I review and publish)
- **Zero dropped balls** (follow-ups, deadlines, and recurring tasks all tracked)
- **Better decisions** (research and prep done before I need it)

And the best part is she's getting better every week. Every new skill I create, every preference she learns, every workflow we refine compounds.

The Clawdbot revolution has nothing to do with replacing humans.

It's about freeing us to do the work only humans can do.

The technology is here. The tools are free or cheap. The only question is whether you'll use it to get a competitive advantage.

---

And if you want an easy, secure, one-click Clawdbot install, we're building it.

Join the waitlist here: https://return-my-time.kit.com/8f464134a4