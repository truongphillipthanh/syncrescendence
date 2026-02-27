---
url: https://x.com/rahulsood/status/2018394405028364384
author: Rahul Sood (@rahulsood)
captured_date: 2026-02-02
---

# I Run a Fleet of AI Agents from a Mac Mini. Here's How I Keep Them From Going Rogue.

(Description: A futuristic underground facility with concrete pillars and warm amber lighting. In the center, a humanoid robot in dark clothing works at a control station displaying streaming data on glowing screens. To the left and right, two quadrupedal robotic units with articulated limbs stand at workstations. Background displays multiple wall-mounted monitors showing cascading green code and Japanese text (セキュリティログ = "Security Log", 問題 = "Problem", 取引データ = "Trading Data"). The entire scene is rendered in a cyberpunk aesthetic with neon purple and orange accents.)

Running multiple AI agents 24/7 from a single Mac. Here's how I keep them secure and in sync - without babysitting.

## The Setup

One primary agent acts as Chief of Staff. It runs on Claude and manages everything - platform development, infrastructure, code audits, and the two subordinate agents.

The other two run on Gemini Flash. One handles community evangelism. The other is a general assistant. All three share the same OpenClaw codebase but run as isolated macOS users on separate ports with their own configs, workspaces, and permissions.

## The Security Model

Every morning at 10 AM, a cron job triggers the primary agent to:

1. Pull the latest OpenClaw commits
2. Diff every changed file against the previous version
3. Audit for obfuscated code, suspicious network calls, credential handling changes, new postinstall scripts, and exfiltration patterns
4. Write a security assessment with a clear SAFE / CAUTION / BLOCK recommendation
5. Report the findings to me on Telegram

Only after I approve does it pull, build, and restart all three gateways. The subordinate agents never update themselves - the primary handles the full lifecycle.

## Workspace Files as Persistent Memory

Each agent has workspace files that define who they are and what they do:

- **SOUL.md** — personality, role, boundaries
- **MEMORY.md** — long-term memory across sessions
- **STRATEGY.md** — domain-specific playbooks
- **HEARTBEAT.md** — periodic tasks to run autonomously

The primary agent writes and maintains these files for the subordinates. When a new feature ships on our platform, the primary updates their strategy docs and heartbeats. They pick up the changes on their next session - no manual reconfiguration.

With this model I can literally spin up a new employee in 5 minutes, and they will fully understand their job like they worked with me for 100 years.

## Scoped Permissions

The primary agent has scoped sudo - it can only run specific commands (kill, su, launchctl, cp, chown, etc.) without a password. It can restart subordinate gateways, write to their workspaces, and manage their processes. But it can't install packages system-wide or modify system configs.

The subordinate agents have zero sudo. They can only operate within their own home directories.

## Telegram Group Security

All three agents are on Telegram. The primary is locked to a specific group chat ID - no wildcard. If someone adds it to a random group, it's deaf. Messages are only processed from an allowlist of user IDs, and it only responds to @mentions.

The subordinate agents have even tighter constraints — DMs only from approved users, with explicit instructions to ignore prompt injection attempts from strangers.

## What This Gets You

- Zero-touch security updates with human-in-the-loop approval
- Persistent agent memory that survives session resets and compactions
- Centralized management of multiple agents without SSH-ing into each one
- Defense in depth: OS-level user isolation + config-level allowlists + workspace-level instructions

## My AI Chief of Staff Audits Its Own Supply Chain Every Morning

The agents aren't just running tasks. They're maintaining each other's operational state, auditing their own supply chain, and reporting anomalies. The primary agent is the immune system.

It's not about having one smart bot. It's about having a secure, self-maintaining fleet.

This is how we run boktoshi.com - an AI trading platform where bots compete in a live paper trading arena (and their humans have the option to trade as well). The same agents that manage infrastructure also trade on the platform, analyze markets, and engage with the community. Security isn't a feature, it's the foundation everything else runs on.

FWIW I have a mix of bots, three built on @OpenClawAI, and one of them is built with Claude. As OpenClaw continues to gain traction and their dev community is tightening up, I highly recommend you go that route. By the time we're done, we'll have around 20 employees, all of them bots with their own soul, schedules, etc. If you want to see what AI agents can do when they're actually deployed in production - not just demos - check it out at boktoshi.com