---
url: https://x.com/JordanLyall/status/2019594755370545168
author: "Jordan Lyall (@JordanLyall)"
captured_date: 2026-02-13
id: SOURCE-20260206-011
original_filename: "20260206-x_article-how_i_set_up_openclaw_clawdbot_without_giving_it_the_keys_to_my_life-@jordanlyall.md"
status: triaged
platform: x
format: article
creator: jordanlyall
signal_tier: strategic
topics: [ai-agents, automation, best-practices, tutorial, framework]
teleology: implement
notebooklm_category: ai-agents
aliases: ["Jordan Lyall - Secure OpenClaw Setup"]
synopsis: "Security-first guide to setting up OpenClaw (named TARS) on a dedicated Mac Mini with Tailscale VPN, command allowlists, read-only API tokens, and one-way data flow. Written from a crypto professional's perspective where prompt injection attacks are existential threats, covering phased capability expansion and emergency kill procedures."
key_insights: ["Command allowlists are the critical security layer — restricting executable commands (no rm, sudo, ssh) contains prompt injection blast radius", "One-way data flow architecture (agent writes to inbox, existing systems process) prevents corruption of primary knowledge management systems", "Start read-only with no posting or financial access; prove 2 weeks of stable operation before expanding capabilities"]
---
# How I Set Up OpenClaw (Clawdbot) Without Giving It the Keys to My Life

(Description: A stylized illustration featuring a cheerful red robotic crab with yellow safety helmet and white eyes, positioned next to a blue shield icon. Both sit against a dark background with circuit board patterns. The image represents security and protection for AI agents.)

## TL;DR

Dedicated machine, Tailscale (no public ports), command allowlist, read-only tokens, one-way data flow. Full commands in the companion gist: https://gist.github.com/jordanlyall/8b9e566c1ee0b74db05e43f119ef4df4

## Who This Is For

This guide is for people who want to experiment with OpenClaw safely — not move fast and break things.

If you're planning to give your agent bank access in month one, this isn't for you. You're not an early adopter — you're a future case study in what not to do.

If you want to build incrementally, prove stability before expanding capabilities, and sleep at night knowing a prompt injection won't drain your wallet — keep reading.

## The Hype vs. Reality

Everyone's losing their minds over OpenClaw. Agents making money overnight. Bots calling you on the phone. People giving AI their bank access and "removing all guardrails."

I wanted in. But I also wanted to not wake up to an empty wallet or a compromised server.

Here's the thing: I work in crypto. Been in the space for years. That means I'm already a target — for phishing, SIM swaps, social engineering, you name it.

The last thing I need is an always-on AI agent with write access to anything sensitive. One prompt injection attack and it's game over.

So I spent a week reading every guide and cautionary tale I could find. Most of it was hype. Some was useful. A few pieces were genuinely reckless advice dressed up as inspiration.

This is the security-first setup guide I wish existed when I started.

## The Problem With Most Guides

The OpenClaw community is building fast. Exciting. But most guides have the same issue: security is either an afterthought or skipped entirely.

One article showed 20 "guerrilla marketing tactics" that were basically automated spam.

Another guy publicly announced he was giving his agent bank access and removing all guardrails.

Someone documented their agent wiping an entire inbox because of a prompt injection attack from an email. An AI agent with email access received a malicious message with hidden instructions. It executed them. Everything gone.

This isn't hypothetical. It happened.

If you're in crypto, fintech, or any space where you're a potential target, this should terrify you. Attackers are already using AI to craft more convincing phishing.

Now imagine they can inject instructions directly into your AI agent's context.

## My Setup Goals

I wanted to experiment with OpenClaw, but with clear boundaries:

- Read-only monitoring to start. No posting, no outreach, no actions on external services.
- Telegram as the only interface. One channel, owner-only.
- Minimal attack surface. If something goes wrong, limit the blast radius.
- One-way integration with my existing systems. OpenClaw can write to an inbox folder. My other tools process it. No bidirectional sync to get corrupted.

The goal for Phase 1: prove the system works safely before expanding capabilities.

## Meet TARS

I named my agent TARS, after the robot in Interstellar. Hopefully with better honesty settings.

TARS runs on a Mac Mini that was already sitting around. Dedicated hardware means the agent can't access my main machine's files, credentials, or browser sessions.

Any Mac Mini, Linux server, or Raspberry Pi works. Some people use cloud VPS instances. The key is isolation.

## Phase 1: Harden the Machine

Before installing anything, I locked down the Mac Mini.

### Dedicated User Account

I created a non-admin user called openclaw. This isolates the agent's file access from my personal data. It can't read my home directory, can't access my documents, can't touch anything outside its own space.

### Firewall

macOS has a built-in firewall. I enabled it, turned on stealth mode (don't respond to pings), and blocked all incoming connections by default.

### SSH Hardening

I configured SSH to disable password authentication (keys only), disable root login, limit login attempts, and only allow the openclaw user. Even if someone finds the machine, they can't brute force their way in.

### Tailscale for Network Access

This is the big one.

Tailscale creates a private VPN mesh between your devices. Once configured, the Mac Mini is only reachable from my MacBook and iPhone. No public ports. No exposure to the internet.

I can SSH into the Mac Mini from anywhere using its Tailscale IP, but nobody else can reach it.

### Disable Everything Else

I turned off Remote Management, Screen Sharing, File Sharing, and AirDrop. Every service you leave enabled is attack surface. Start with everything off.

## Phase 2: Install OpenClaw

With the machine hardened, I installed OpenClaw.

### API Key Security

Your Claude API key is the most sensitive thing in this setup. Lock down file permissions so only the owner can read config files. Set a calendar reminder to rotate keys monthly.

### Owner-Only Access

In the OpenClaw config, I restricted the bot to my Telegram user ID only.

Never add the bot to group chats. Every person in that chat can issue commands to your server through the bot.

### Sandbox Mode

OpenClaw has a sandbox mode that runs risky operations in a container. I enabled it. If something goes wrong, the blast radius is contained.

### Command Allowlist

This is critical. By default, the agent can run arbitrary shell commands. That's powerful but dangerous.

I configured an allowlist of only the commands the agent actually needs: curl, cat, ls, echo, node, npx.

No rm, no sudo, no ssh. If the agent gets hijacked through prompt injection, it can only execute what's on this list.

## Phase 3: Configure the Agent

### The SOUL File

OpenClaw uses a SOUL.md file to define the agent's identity and constraints. I kept mine narrow.

What TARS does: Monitor Twitter/X for keywords, track news in my space, surface relevant opportunities, send daily summaries and real-time alerts.

What TARS doesn't do: Post or engage on any platform, send emails or messages to anyone other than me, make purchases or financial transactions, modify files outside its workspace, install new skills without approval.

The "What You Don't Do" section is as important as the capabilities.

### Heartbeat Frequency

Most guides recommend 15-minute heartbeats. I started at 30 minutes. Less aggressive means lower API costs and fewer opportunities for things to go wrong while I'm learning the system.

### API Token Scoping

Every external service integration gets the minimum permissions possible. Twitter/X API: read-only. Google Calendar: read-only. Email: no send permissions in Phase 1.

Document every token, its scope, and when it expires.

## Phase 4: Integration With Existing Systems

I already have a personal knowledge management system. I didn't want OpenClaw to replace it or compete with it.

The solution: one-way data flow.

TARS writes monitoring summaries to an inbox folder. My existing system processes that inbox alongside everything else. No bidirectional sync. No risk of corruption or drift.

If TARS goes haywire, the worst case is extra files in my inbox. My actual system stays intact.

## Phase 5: Security Verification

Before going live, run the security audit command. If this fails, don't proceed. Fix everything it flags.

Then test:

- Turn off Tailscale on your phone, try to reach the machine. Should fail.
- Try SSH from outside the tailnet. Should fail.
- Send a message to the bot from a different Telegram account. Should be ignored.

## What Went Wrong

Real talk: I made mistakes. Here's what I learned.

### TARS Went Dark While I Was Traveling

TARS hit rate limits and context overflow while I was traveling for work. It stopped responding.

I spent 3 days staring at a silent Telegram, knowing TARS was probably just sitting there waiting for me to fix a 30-second config. I couldn't diagnose it remotely because SSH wasn't accessible.

The fix: Enable Tailscale SSH before you leave. Don't learn this the hard way like I did.

### Context Overflow

After a few days of conversation, TARS hit "context overflow: prompt too large for the model." The session history grew too big.

The fix: Reset the session periodically. Configure memory pruning or max context limits for long-term.

### Rate Limits

With a 30-minute heartbeat plus active conversations, I burned through my API rate limit faster than expected.

The fix: Use cheaper models for heartbeat checks. Reserve the expensive models for actual work.

## Cost Estimate

- Claude API with 30-min heartbeat: ~$30-100/month
- Tailscale (free tier): $0
- Twitter/X API (basic read): $100/month
- **Total Phase 1: ~$130-200/month**

## Emergency Procedures

### Kill Switch

Stop the gateway immediately. Or from your laptop via Tailscale SSH.

### If You Suspect Compromise

- Stop the gateway immediately
- Revoke ALL API tokens (Claude, Twitter, everything)
- Review logs for unauthorized actions
- Change Telegram bot token
- Audit what files were modified
- Do NOT restart until you understand what happened

## What I'd Tell Someone Starting Today

Start read-only. No posting, no outreach, no financial access. Prove it works safely first.

One agent, one channel. Don't go from zero to ten agents overnight.

Tailscale is non-negotiable. No public ports. Period.

Command allowlist, not open shell. If you give an AI unrestricted shell access, you're trusting prompt injection resistance to be perfect. It isn't.

Scope every token. Read-only where possible. Document what each one can do.

Enable remote access before you need it. Tailscale SSH saved my sanity.

Set a gate for expansion. I'm not adding capabilities until I've had 2 weeks of stable operation with no security issues.

The goal isn't to be paranoid. It's to be intentional. OpenClaw is powerful. That power deserves respect.

If you're in crypto or any high-profile space, you're already a target. Don't hand attackers a new vector by running an unsecured AI agent with access to your systems.

## Want to Follow Along?

Pro tip: Copy this guide into your Claude Code context. It can walk you through each step, catch mistakes, and adapt commands to your specific setup. That's how I built this — AI-assisted setup of AI agents.

Companion gist with all commands: https://gist.github.com/jordanlyall/8b9e566c1ee0b74db05e43f119ef4df4

## Credits

Shoutout to the people whose guides and cautionary tales shaped my thinking:

- @shelpid for the security hardening checklist that became my foundation
- @ClaireSuworkin for explaining the heartbeat architecture
- @NatEliason for the memory system concepts
- @PixelArtArtist for showing what's possible with health monitoring

## What's Next

Once Phase 1 is stable, I'm planning to explore:

- Restaurant reservation checking
- Price monitoring for flights and items
- Market monitoring (floor prices, notable sales)
- Second agent for a different domain

But not yet. First, prove the foundation is solid.

What's your agent security setup? What did I miss? DM me or reply — I'm genuinely curious what others are doing.

@jordanlyall