# I gave OpenClaw a name, its own computer, and told it to figure things out. Here's the 32-hour recap

(Description: Header image featuring the OpenClaw logo (red lobster mascot) and a smiling raccoon character mascot side-by-side)

I didn't give an AI agent access to my computer.

I didn't give it access to my email, GitHub, browser sessions, or files.

I gave it its own computer, accounts, and workspace. After 32 hours of running OpenClaw this way, I want to share what's actually working and why I think the setup matters more than most people realize.

## It's not just about the machine. It's about the work environment.

Most people installing AI agents give them access to their personal setup. Their files, their credentials, their inbox. It's convenient.

But think about what an agent actually does. It reads files. It runs commands. It controls a browser. It sends messages.

That's not a chatbot. That's a very capable team member sitting at your keyboard.

So I asked myself: would I hand a brand-new hire my personal laptop, my email password, and my GitHub on day one?

No. I'd give them their own setup.

That's what I did. A spare Ubuntu laptop. A fresh email account. A fresh GitHub account. A fresh X account. The agent doesn't touch my stuff. It has its own work environment, completely separated from mine.

If something goes wrong, it goes wrong over there. If a credential leaks, my personal accounts are untouched. Everything is logged, everything is auditable, and I can rebuild the whole setup from scratch if I need to.

## We share work through GitHub

We still need to exchange files outside of the Telegram chat. The one place our worlds connect is a GitHub repo called `shared_workspace`.

This is how I exchange files and documents with the agent. I push something there, and it picks it up. It produces something; it commits it there. It's version-controlled, transparent, and I can review every change.

Inside that repo, the agent organizes its own work: a `writing/` folder with drafts, archived, and published posts. An `x_metrics/` folder tracking followers' history. An `outbound/` folder for the content it produces. Even `project_ideas/` for things we're exploring together.

I also asked it to create a "recovery kit," a full set of instructions for how to rebuild the current setup if the laptop dies or something blows up. All the configs, all the steps, stored right there in the shared workspace.

If your agent's environment isn't recoverable, it's not really a system. It's a house of cards.

(Description: GitHub repository view showing the shared_workspace directory structure with folders including main, drafts, archived, stats, project_ideas, and other organizational folders)

## I created a full identity for the agent

This is the part that sounds weird until you try it.

I didn't want a generic "assistant." I wanted an operator with consistent behavior, something that acts the same way whether I'm watching or not.

So I created **Tanuki-kun**: a name, a personality, explicit rules for what it can and can't do, default language settings (Portuguese internally, English externally), strict formatting conventions for GitHub PRs, and memory files to retain context across restarts.

This isn't about making it cute. It's about making it predictable. An agent without rules turns chaotic fast. A named identity with documented boundaries behaves like a teammate you can trust over time. (But yes… it's also cute 😆)

In another repo, I keep a list of rules outlining what's permitted and what's not, along with a file that defines the decision-making baseline and tone.

(Description: GitHub file browser showing RULES.md document titled "RULES.md — Working Agreement (nitta-san × Tanukikun)" with sections including "O) Prime directive" and last updated date of 2026-02-07)

I also asked Tanuki-kun to keep a daily journal, recording everything he does each day. I started it as a fun experiment, but it turned out to be incredibly useful for tracking what he does without me having to ask.

(Description: GitHub file view showing dated journal entry "2026-02-07 — Notes (Day One)" with sections for "What I set up / shipped" including Identity & working agreement, Tooling brought online, and GitHub work. The journal documents setup activities with bullet points listing email configuration, browser setup, GitHub integration, and other initial setup tasks)

You can find him at [@Tanuki26302](https://x.com/@Tanuki26302) or on his website: [https://tanukikun01.github.io/](https://tanukikun01.github.io/)

## Telegram as the control plane

Instead of a dashboard or a web UI, the agent lives in a Telegram chat. I message what I want. It runs tools, the terminal, a browser, and git, and reports back.

It's hard to describe, but interacting with it through Telegram changed the experience in a very real way. It's genuinely exciting to text it.

It feels less like using software and more like messaging a coworker. "Check the inbox." "Push that commit." "What's the status on X?" And it just does it.

For the avatar, for example, we went back and forth a bit but weren't getting a good result. So I grabbed one of its files, refined it in ChatGPT, and sent it back via Telegram. It picked up the file, updated GitHub, and propagated the changes elsewhere.

How cool is that?

## Here's the crazy part: it also configures itself

Not only the avatar, but also the machine dependencies.

Early on, I sent it a voice message. It replied: "I can't process audio."

So I asked: "Can you figure it out?"

It said it needed to install ffmpeg and faster-whisper, so I told it: go ahead, you have sudo access.

A few minutes later, it replied with a voice message.

It had installed the dependencies on its own, tested the pipeline, and responded in kind. No hand-holding. I gave it the problem and the permissions, and it solved it.

That moment changed how I think about this setup. It's not about micromanaging every tool installation. It's about giving the agent a safe environment where it can figure things out, and then verifying the results.

## What it actually does today

After 32 hours, here's where things stand.

**Email:** It reads its own inbox and drafts replies. I got a summary of unread messages this morning without opening a browser.

**GitHub:** It creates repos, commits, and pushes code, and opens PRs with proper formatting. The shared_workspace repo is how we coordinate all our files.

**Browser automation:** It navigates, clicks, and fills forms for workflows that would otherwise need paid APIs. The catch: new accounts don't have a reputation yet, so it sometimes hits CAPTCHA and trust gates.

**Routines:** I set up cron jobs for daily snapshots, periodic checks, and housekeeping tasks. These run whether I'm around or not.

**X:** I configured his account minutes before writing this. It's having a hard time finding what's what, but already followed people I asked to, including me, of course, liked a few posts, and replied to my posts mentioning it.

## It's still very early days

OpenClaw is just starting, thank you [@steipete](https://x.com/@steipete) for building and sharing [@openclaw](https://x.com/@openclaw)!

My own setup started just days ago. The routines aren't bulletproof. There are rough edges everywhere.

But like a new hire, a good orientation pays dividends.

The time I'm spending now, setting up clean accounts, writing clear rules, building the recovery kit, documenting the shared workspace, that's not wasted time. That's the foundation that makes everything after this faster and more reliable.

## The real takeaway

I'm building an assistant that earns trust through repetition: clear rules, an isolated work environment, a shared version-controlled workspace, and small automations that compound over time.

If you're working with AI agents, I think the "separate environment + separate identity" pattern is underrated. It's not sexy. But it's the difference between a toy and something you can actually rely on.

---

**Published:** 1:03 PM · Feb 12, 2026  
**Engagement:** 23 replies · 30 reposts · 301 likes · 1,038 bookmarks · 150.5K views