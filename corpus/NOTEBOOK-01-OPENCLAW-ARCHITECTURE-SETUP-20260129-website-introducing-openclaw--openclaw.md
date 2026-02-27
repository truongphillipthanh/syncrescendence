---
url: https://openclaw.ai/blog/introducing-openclaw
title: Introducing OpenClaw
domain: openclaw.ai
author: Peter Steinberger
published_date: January 29, 2026
captured_date: 2026-02-04
content_type: blog
---

# Introducing OpenClaw

(Image: OpenClaw logo featuring a red cartoon lobster with large claws, alongside the text "OPENCLAW" with the word "CLAW" in red. Alt text: Introducing OpenClaw. Caption: Project rebrand announcement visual.)

**By Peter Steinberger** ([@steipete](https://x.com/steipete))  
January 29, 2026 · 3 min read

---

Two months ago, I hacked together a weekend project. What started as "WhatsApp Relay" now has over 100,000 GitHub stars and drew 2 million visitors in a single week.

Today, I'm excited to announce our new name: **OpenClaw**.

## The Naming Journey

We've been through some names.

**Clawd** was born in November 2025—a playful pun on "Claude" with a claw. It felt perfect until Anthropic's legal team politely asked us to reconsider. Fair enough.

**Moltbot** came next, chosen in a chaotic 5am Discord brainstorm with the community. Molting represents growth—lobsters shed their shells to become something bigger. It was meaningful, but [it never quite rolled off the tongue](https://x.com/NetworkChuck/status/2016254397496414317).

**OpenClaw** is where we land. And this time, we did our homework: trademark searches came back clear, domains have been purchased, migration code has been written. The name captures what this project has become:

- **Open**: Open source, open to everyone, community-driven
- **Claw**: Our lobster heritage, a nod to where we came from

## What OpenClaw Is

OpenClaw is an open agent platform that runs on your machine and works from the chat apps you already use. WhatsApp, Telegram, Discord, Slack, Teams—wherever you are, your AI assistant follows.

**Your assistant. Your machine. Your rules.**

Unlike SaaS assistants where your data lives on someone else's servers, OpenClaw runs where you choose—laptop, homelab, or VPS. Your infrastructure. Your keys. Your data.

## What's New in This Release

Along with the rebrand, we're shipping:

- **New Channels**: Twitch and Google Chat plugins
- **Models**: Support for KIMI K2.5 & Xiaomi MiMo-V2-Flash
- **Web Chat**: Send images just like you can in messaging apps
- **Security**: 34 security-related commits to harden the codebase

I'd like to thank all security folks for their hard work in helping us harden the project. We've released [machine-checkable security models](https://github.com/vignesh07/clawdbot-formal-models) this week and are continuing to work on additional security improvements. Remember that prompt injection is still an industry-wide unsolved problem, so it's important to use strong models and to study our [security best practices](https://docs.openclaw.ai/gateway/security).

## The Road Ahead

What's next? Security remains our top priority. We're also focused on gateway reliability and adding polish plus support for more models and providers.

This project has grown far beyond what I could maintain alone. Over the last few days I've worked on adding maintainers and we're slowly setting up processes so we can deal with the insane influx of PRs and Issues. I'm also figuring out how to pay maintainers properly—full-time if possible. If you wanna help, consider [contributing](https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md) or [sponsoring the org](https://github.com/sponsors/openclaw).

## Thank You

To the Claw Crew—every clawtributor who's shipped code, filed issues, joined our Discord, or just tried the project: thank you. You are what makes OpenClaw special.

The lobster has molted into its final form. Welcome to OpenClaw.

---

**Get started:** [openclaw.ai](https://openclaw.ai)

**Join the Claw Crew:** [Discord](https://discord.gg/openclaw)

**Star on GitHub:** [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

— Peter

P.S. Yes, the mascot is still a lobster. Some things are sacred. 🦞

---

### Call to Action

Get started with a single command:
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

[Learn more →](/)