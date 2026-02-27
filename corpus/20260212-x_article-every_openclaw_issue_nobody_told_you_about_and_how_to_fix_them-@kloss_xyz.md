---
url: https://x.com/kloss_xyz/status/2022101005064974600
author: klöss (@kloss_xyz)
captured_date: 2026-02-12
---

# Every OpenClaw Issue Nobody Told You About (And How to Fix Them)

(Description: A stylized monochromatic illustration of a robotic sphere surrounded by mechanical gears, springs, and bolts in a radial pattern, with "OpenClaw" text centered below the sphere)

I've been running multi agent orchestration with my OpenClaw for over a week. It's getting much, much closer to where I want it to be. The issue is though that everyone's telling you theirs is perfect, and they did it in a day. They're lying. I've been building mine for a week plus.

Every single thing that could break when I built mine, literally broke.

What follows is every annoying ass problem I hit, every issue power users have reported, and every config that actually made this thing work reliably. Whether you're running one agent or ten with subagents, whether you're technical or just getting started, this is the reference guide I wish existed when I began. This isn't a setup guide. It's an optimization one.

This isn't something you skim and forget. Please bookmark it and save it. Come back to it every time something goes sideways with OpenClaw.

Let's get into it.

## 1. Upgrading Your OpenClaw

If you're coming from an old OpenClaw setup, the good news is that installer actually handles the migration pretty well. It moves your `.clawdbot` directory to `.openclaw` and creates a symlink back so nothing breaks, and your config, soul files, memory, and workspace all carry over. The clawdbot package also stays as a compatibility shim.

The real problem is what it doesn't actually clean up. The old `clawdbot-gateway.service` can keep running alongside the new `openclaw-gateway.service` in some cases, and when both try to grab port 18789 you'll get a restart loop where the new gateway fails over and over with "another gateway instance is already listening." It looks like OpenClaw is broken but it's actually just fighting itself with its own predecessor for the port.

Before you install OpenClaw, stop and disable the old service completely:
```bash
systemctl --user stop clawdbot-gateway.service
systemctl --user disable clawdbot-gateway.service
rm -f ~/.config/systemd/user/clawdbot-gateway.service
systemctl --user daemon-reload
```

Then uninstall the old npm package (`npm uninstall -g clawdbot`) and check for leftover files in `/usr/local/bin/clawdbot` or `/usr/local/lib/node_modules/clawdbot` since residual packages can silently interfere with the new install. After that, install OpenClaw fresh and your existing workspace files will be picked up automatically.

## 2. Agent Stability (Hangs, Crashes, and Silent Deaths)

Your agent will hang, it will crash, and it will go completely silent for minutes with no explanation. This is normal when you're running agents 24/7, and the fix is building around it.

Write a simple watchdog script that pings the gateway health endpoint every 15 minutes. If it doesn't respond, auto-restart the whole thing. You shouldn't be babysitting this manually.

OpenClaw has a built-in diagnostic command called `openclaw doctor` that checks your config, gateway, channels, workspace, and permissions in one shot. Run it with the `--fix` flag (`openclaw doctor --fix`) and your actual issue and it will auto-repair common issues like permission problems, missing directories, legacy config keys, and outdated service paths. It backs up your config before making changes and won't touch your API keys or credentials, so it's safe to run whenever something feels off or after an upgrade. You can also use it without the `--fix` flag and some users have found better results that way.

## 3. Security (Lock This Down Immediately)

If your server is internet-facing, assume someone is already trying to brute force their way in. This isn't paranoia, it's what happens to every exposed server within hours of going live.

At minimum:
```bash
apt install fail2ban -y
ufw allow 22
ufw enable
```

But honestly, the better move is to not expose it at all. Use Cloudflare Tunnel or Tailscale to access your server without opening ports to the internet. In your OpenClaw config, set `gateway.bind: "loopback"` so the gateway only listens locally. No exposed ports means no attack surface for nefarious actors.

## 4. Plugins Breaking Your Gateway

Plugins are powerful but they can take your entire gateway down. If something dies right after you install a plugin, that plugin is almost certainly the cause.

The fix is simple:

- Check `gateway.err.log` for the actual error
- Uninstall the plugin: `openclaw plugins disable <name>`
- Restart

The habit to build here is verifying your gateway restarts cleanly after every single plugin install. Don't install three plugins at once and then wonder which one broke everything, just go one at a time, verify, and move on.

## 5. The Autonomy Problem

This is the issue I see more than any other, where the agent doesn't listen, leaves tasks unfinished, or says "done" when the work is clearly broken.

Here's the thing: the agent is exactly as autonomous as your instructions make it. If your instructions are vague, the agent's behavior will be vague. If you don't define what "done" means, the agent will decide for itself, and its definition will be generous.

Put explicit rules in your `AGENTS (.md)` file:

> Every time the agent claims "done," it must include the repo name, branch, and commit hash. It must verify its work with actual commands, not just say "I checked." Design heartbeat loops that catch incomplete tasks before they sit there rotting for hours.

The agent isn't being lazy. It's following the looseness in your instructions. Tighten those up and the behavior changes immediately.

## 6. Model Configuration

Too many models in your fallback list creates unpredictable behavior. The agent switches between different reasoning styles mid-task and the output quality becomes inconsistent.

Keep your model list to 2 or 3 maximum and stay within the same family, either all Anthropic or all OpenAI. Don't mix providers in the same fallback chain.

Configure your models in the actual config file, not through the TUI or GUI. Those interfaces sometimes don't persist settings correctly, and you'll wonder why your changes disappeared after a restart.

If you're using free models, put them last in the fallback chain and never as the primary model for anything critical since they're a safety net, not the foundation.

Here's how a solid failover config looks:
```json
"model": {
  "primary": "anthropic/claude-opus-4-6",
  "fallbacks": ["anthropic/claude-sonnet-4-20250514", "anthropic/claude-haiku-4-5"]
}
```

Auto-switches on failures so your agent never goes dark.

## 7. TUI Shows "(no output)"

This one drove me crazy before I figured it out. The TUI shows "(no output)" for every reply and nothing seems to work.

If you configured Telegram delivery with the `--deliver` flag but you've never actually sent a direct message to your bot on Telegram, the delivery failure kills the entire output pipeline, not just Telegram delivery but everything.

The fix is absurdly simple: open Telegram, send one message to your bot, and the pipeline unblocks and everything starts flowing.

## 8. Messages Getting Dropped

When your agent is busy processing a request and new messages come in, they can get silently dropped. You'll never know they existed and the sender thinks they were heard, but they weren't.

Enable queue mode:
```json
"messages": {
  "queue": {
    "mode": "collect"
  }
}
```

Every message gets queued and processed in order with nothing lost, even if 5 messages pile up while the agent is in the middle of a long tool call.

## 9. Local Memory with QMD

If you want to avoid paying for embedding APIs, OpenClaw's QMD backend does BM25 keyword search, vector search, and reranking entirely on your local machine. It requires the qmd binary (install via `bun install -g github.com/tobi/qmd`) and runs local GGUF models for embeddings and reranking.
```json
"memory": {
  "backend": "qmd"
}
```

The default builtin backend already does hybrid BM25 + vector search, but QMD adds a local reranker on top and can index multiple external folders beyond your workspace. The tradeoff is more moving parts and heavier CPU/disk usage, so if your memory set is small and mostly workspace Markdown, the builtin hybrid search is already solid without QMD. First search will be slow since QMD downloads local models (~300MB+) on the first query.

## 10. Making Responses Feel Human

Instant replies on Telegram and Discord feel robotic. Real people don't respond in 200 milliseconds. It immediately signals "this is a bot" to anyone paying attention.
```json
"humanDelay": {
  "mode": "custom",
  "minMs": 800,
  "maxMs": 2500
}
```

Responses now arrive with natural timing, somewhere between 0.8 and 2.5 seconds of delay. It feels like a person typing instead of a machine firing back instantly, and that small detail makes a big difference in how people interact with your agent.

## 11. Controlling Who Can Spawn What

First, understand the difference between agents and subagents because most people conflate them.

**Agents** are your team, where each one is a distinct personality with its own workspace, its own `SOUL (.md)`, its own model, and its own role. Think of them as employees: your CEO agent handles strategy and external communication, your CTO agent handles technical decisions, and your CMO handles content and marketing. They're all top-level, persistent, and always available.

**Subagents** are temporary background workers that any agent on your team can spawn to handle a task without blocking its main conversation. The subagent runs in an isolated session, does its work, and reports back when finished before getting archived. They're one-off workers, not permanent team members.

The important distinction: by default, subagents cannot spawn other subagents. This is intentional. It prevents runaway delegation chains that burn tokens exponentially. There's a feature request to make this configurable, but for now, the nesting stops at one level per spawn.

To control which agents your team members can delegate to, set up allowlists:
```json
{
  "id": "ceo",
  "subagents": {
    "allowAgents": ["cto", "cmo", "cro"]
  }
}
```

Your CEO can spawn subagents under the CTO, CMO, or CRO agent identities. Your CMO can't spawn work under the CTO's identity unless you explicitly allow it. This gives you a clean organizational hierarchy without runaway cross-delegation.

## 12. Different Models for Different Agents

Not every agent on your team needs the most expensive model. Your CEO needs strong reasoning for orchestration and decision-making. Your CTO agents need code-optimized models. Your COO running operational tasks can use something lighter and cheaper.

The pattern:

- Your CEO runs on Opus for complex reasoning and strategic decisions
- Your CTO runs on Codex for code generation and technical work
- Your COO runs on Haiku for quick operational tasks and routine coordination

Set global defaults in your config and then override per agent. This is how you control costs without sacrificing quality where it matters. A subagent doing a quick research task doesn't need Opus. Set a cheaper model as the subagent default via `agents.defaults.subagents.model` and keep your top-level agents on the higher-quality models.

## 13. Concurrency Settings

OpenClaw defaults are conservative on purpose. Two settings control parallel processing:

- `maxConcurrent: 4` controls how many top-level sessions can run at the same time
- `subagents.maxConcurrent: 8` controls how many subagent sessions can run in parallel

If your hardware can handle it, crank these up. More concurrency means your multi-agent system processes work faster instead of queuing everything behind a bottleneck.

## 14. Nesting and Delegation Depth

By default, subagents cannot spawn other subagents. OpenClaw hardcodes this restriction to prevent runaway fan-out where delegation chains spiral and burn tokens exponentially.

The architecture that works is having your top-level agents (CEO, CTO, CMO) each spawn subagents for background work, and those subagents complete their tasks in a single shot and report back. No deeper nesting and no subagent-spawning-subagent chains.

There's a configurable override being discussed (via `allowNesting: true` or adding `sessions_spawn` to subagent tool allowlists), but the default behavior exists for a good reason. Keep your delegation flat where the top-level agent breaks work into atomic units that a subagent completes and returns.

## 15. Routing External Communications

Each agent on your team gets its own workspace, personality, and model. But route all external communications through one agent, your CEO or primary.
```
Telegram → CEO agent
Discord → CEO agent
CTO, CMO, COO → internal only
```

Your specialized agents stay internal while one agent handles all human-facing channels, which prevents conflicting responses, maintains a consistent voice, and keeps your specialized team members focused on their actual jobs instead of managing conversations. They do work and the CEO reports externally.

## 16. Sharing State Between Agents

Don't copy files between agent workspaces. You'll end up with diverging versions and nobody knows which one is current.

Symlink them instead:
```bash
ln -s ~/workspace/state ~/workspace-cto/state
```

One source of truth where the main agent writes and everyone else reads. The filesystem is your coordination protocol, simple, reliable, and no fancy tooling required.

## 17. Agent Personalities and SOUL (.md)

This is where most people either skip entirely or get wrong by dumping everything into one file.

OpenClaw separates identity into distinct files, each serving a specific purpose. `SOUL (.md)` defines who your agent is, not what it can do or how it's configured, but who it is at its core: its philosophy, its voice, its boundaries, and its personality. `AGENTS (.md)` defines operational rules and behavioral instructions, while `IDENTITY (.md)` defines presentation details like display name and avatar.

The `SOUL (.md)` file is what makes each agent on your team feel like a different person rather than the same model wearing different hats. OpenClaw's default `SOUL (.md)` template opens with: "You're not a chatbot. You're becoming someone." That's the mindset. You're writing a character sheet, not a config file.

For a CTO agent, your `SOUL (.md)` might define a personality that's precise, skeptical, and evidence-first, someone who's allergic to vague requirements, prefers technical specificity, and pushes back on ambiguous asks. For a CMO agent, the `SOUL (.md)` defines someone creative, strategic, and brand-aware who's focused on narrative and positioning. Same underlying model but completely different thinking patterns.

The key principles for writing good SOUL files: specificity over generality, real opinions over safe positions, and clear boundaries over open-ended flexibility. If someone reading your agent's `SOUL (.md)` can't predict how that agent would respond to a new situation, the file is too vague.

Each agent reads its `SOUL (.md)` at the start of every session. It's injected into the system prompt as the foundation of the agent's identity. If the agent modifies its own `SOUL (.md)` (which it can), it tells you, because that file is its identity and you should know when it evolves.
```json
"agentDir": "~/.openclaw/agents/cto/agent"
```

Point each agent to its own directory. `SOUL (.md)` goes in the workspace alongside `AGENTS (.md)` and `USER (.md)`. The personality files shape how each agent approaches problems, formats outputs, communicates with other agents, and decides what's worth pushing back on.

## 18. Subagent Crashes

Here's a specific failure mode that took me a while to diagnose: a subagent running `rm -rf .next` on a repository that has a running dev server, which causes the dev server to silently die with no error, no crash log, and just stops serving.

The rule that fixed this is that subagents verify their work with `tsc --noEmit` (type checking without building) and only the top-level agent that owns the workspace touches dev servers. Subagents never interact with running processes directly, they just do their isolated task and report back.

## 19. Announcement Floods

When 5 subagents finish their tasks at roughly the same time, each one announces its results back to the parent agent. The announce queue backs up. The gateway can time out.

Two fixes:

- Set `cleanup: "delete"` on non-critical subagent spawns so they archive immediately after announcing instead of lingering
- Stagger your launches so subagents aren't all finishing simultaneously. Remember that announce is best-effort. If the gateway restarts while announcements are pending, those results are lost.

## 20. Cron Job Aliases

Model aliases in cron configs don't always resolve correctly. Your cron job says "haiku" and the system doesn't know which haiku you mean.

Always use the full model string: `anthropic/claude-haiku-4-5`, not `haiku`. Saves you from debugging phantom failures where the cron runs but uses the wrong model or no model at all.

## 21. Context Window Management

Over long sessions, the context fills up with stale tool outputs. Old API responses, outdated file contents, completed task results. The agent starts getting confused because it's referencing information that's no longer relevant.
```json
"agents": {
  "defaults": {
    "contextPruning": {
      "mode": "cache-ttl",
      "ttl": "30m",
      "keepLastAssistants": 3
    }
  }
}
```

When the last Anthropic API call for the session is older than the TTL, pruning kicks in and trims oversized tool results from the in-memory context. It doesn't rewrite your session history on disk, it just slims down what gets sent to the model on the next call. The last 3 assistant responses stay untouched. Massive token savings and the agent stays focused on what's current.

## 22. Compaction Safeguard

Before OpenClaw compresses your context window, you want the agent to save its memories to disk first. Otherwise context compression can erase information the agent hasn't persisted anywhere.
```json
"compaction": {
  "mode": "safeguard",
  "memoryFlush": {
    "enabled": true
  }
}
```

The agent gets a silent turn to write durable notes to `memory/YYYY-MM-DD (.md)` before compression runs. Context it hasn't saved yet never gets silently dropped.

## 23. Memory File Limits

`MEMORY (.md)` and other workspace files get injected into your agent's context on every message, and OpenClaw has a bootstrap budget that caps how much total workspace content gets loaded. When a file exceeds this budget, it gets truncated using a 70/20/10 split where 70% comes from the head, 20% from the tail, and the middle gets cut. There's no error and no warning in chat, so the agent just loses whatever was in the middle of a bloated file.

Keep `MEMORY (.md)` lean and move detailed information into sub-files under `memory/` that the agent reads on demand. Think of `MEMORY (.md)` as an index rather than a database, where you point to things instead of storing everything inline.

## 24. Heartbeat Targeting

The default heartbeat target is "last," meaning whatever channel the agent used most recently. This causes problems when you're active across multiple channels because the heartbeat hops around unpredictably.
```json
"heartbeat": {
  "target": "telegram"
}
```

Be explicit about where heartbeat messages go and lock it in instead of letting it float.

## 25. Discord Permission Issues

Your bot has Administrator permission but can't read certain channels. This happens because OpenClaw's permission checker doesn't properly account for the way Administrator override interacts with `@everyone` channel denies.

The fix: add explicit bot role allows on each channel you need the bot to access. Don't rely on the Administrator permission to cascade through everything. It should work that way, but OpenClaw doesn't interpret it correctly yet.

## 26. BOOT (.md)

This file runs every time your gateway restarts. Think of it as your startup checklist that executes automatically.

Mine checks server health, verifies branch state, and runs security checks so that every restart, before the agent does anything else, `Boot (.md)` ensures the environment is solid.
```bash
openclaw hooks enable boot-md
```

This catches the kind of subtle breakage that accumulates over time like server drifts, branch mismatches, and permission changes, surfacing all of it before it becomes a real problem.

## 27. The Golden Rule of Debugging

When something breaks, check `gateway.err.log` first. Not your config, not your code, not the plugin settings, just the error log.

Every single time I tried to guess what went wrong instead of just reading the log, I made the problem worse. The log tells you exactly what happened so start there, always.

## 28. Memory Architecture: Please Stop Dumping Everything in MEMORY (.md)

This connects directly to the truncation issue in section 23, but it deserves its own section because most people get the entire memory architecture wrong.

OpenClaw's memory system has two official layers. `MEMORY (.md)` is your curated long-term memory for decisions, preferences, and durable facts, and it only loads in private (DM) sessions, never in group contexts, to protect sensitive information. The `memory/YYYY-MM-DD.md` files are daily logs that are append-only and raw, capturing everything that happened that day, with the agent reading today's file plus yesterday's at session start for continuity.

That two-layer system is the default. But if you're running anything complex, you should split further:

Keep a `memory/active-tasks (.md)` file as your live task tracker for what's in progress, what's waiting, and what's blocked, basically your save strategy for crash recovery (more on that in section 30 below). Use `memory/projects (.md)` for project-specific context that doesn't change daily, and use `memory/lessons (.md)` to capture patterns and corrections the agent has learned over time so it doesn't repeat mistakes.

The principle is that your agent wakes up fresh every session and these files are its brain. If you dump everything into `MEMORY (.md)` you hit the 20K character limit and the agent loads context it doesn't need for the current task, but if you split intelligently it loads only what's relevant. `MEMORY (.md)` becomes an index that points to detail files and the agent drills into specific files on demand instead of carrying the entire history in every session.

The memory search system (powered by memory-core or QMD) indexes everything under `memory/` with semantic and keyword search. So even if the agent doesn't load a file at session start, it can find it when the conversation requires it.

## 29. Cron Jobs vs Heartbeats

People use these interchangeably and then wonder why their automation is either wasteful or unreliable. They serve completely different purposes.

Heartbeats run in your main session at a regular interval (default every 30 minutes) where the agent wakes up, reads `HEARTBEAT (.md)`, runs through a checklist, and decides if anything needs your attention. If nothing does, it sends a silent HEARTBEAT_OK and goes back to sleep with no notification spam. Heartbeats are great for batching multiple periodic checks into one turn like scanning your inbox, checking the calendar, and reviewing pending tasks, all in a single agent turn with full conversational context.

Cron jobs run on precise schedules in isolated sessions where each job gets its own context, its own model if you want, and its own delivery target. No token waste from loading the full conversation history since they fire at exact times regardless of what the main session is doing.

The rule: if you need something checked periodically and it benefits from conversational context, use heartbeat. If you need something done at a specific time with isolation, use cron.
```bash
openclaw cron add \\
  --name "Morning briefing" \\
  --cron "0 7 * * *" \\
  --session isolated \\
  --message "Generate today's briefing: weather, calendar, top emails." \\
  --model opus \\
  --announce \\
  --channel telegram
```

Daily content ideas at 6am, overnight research scout at 2am, tech monitoring at 8am, each running in isolation with its own context. Clean, predictable, and no bleed between tasks.

One gotcha from the community: if `HEARTBEAT (.md)` is empty (or only has comments), cron jobs using `wakeMode: "now"` can get incorrectly skipped. There's a known bug and fix for this. If your cron jobs show "idle" and never fire, check that `HEARTBEAT (.md)` has at least one non-comment line, or use the isolated session target to bypass the heartbeat runner entirely.

## 30. The Crash Recovery Pattern

Your agent will crash and your gateway will restart, and this is inevitable when running 24/7 so you need a system that handles it gracefully instead of starting from zero every time.

The pattern is simple: maintain an `active-tasks (.md)` file in your memory directory.

When you start a task, write it to the file. When you spawn a subagent, note the session key. When a task completes, update the status, and when it fails, log what went wrong.

In your `Boot (.md)` [section 26], add a step that reads `active-tasks (.md)` on every gateway restart. The agent comes back online, reads the file, sees what was in progress, and resumes autonomously. No "what were we doing?" conversation. It figures it out from the file and picks up where it left off.

This pairs with the compaction safeguard from section 22. Before any context compression, the agent flushes important state to disk. Between `Boot (.md)` on startup and compaction safeguard during long sessions, you have crash recovery at both ends.

## 31. Model Selection for Security

If your agent reads any external content like emails, web pages, tweets, or articles, this matters more than you think.

Use your strongest model (Opus) for any task that processes external content because weaker models are way more vulnerable to prompt injection from hostile websites and manipulated text. A well-crafted injection in a webpage or email can redirect a weaker model's behavior while stronger models are much harder to steer off course.

For internal tasks like file reading, reminders, and local workspace operations, Sonnet or Haiku is fine since the content is trusted because you control it. But the moment your agent fetches something from the internet or processes an incoming email from an unknown sender, route that through your strongest model.

This is also a good reason to use the per-agent model overrides from section 12 and cron model flags from section 29, where your internal operations agent can run cheap while your external-facing agent that processes inbound content should run expensive.

## 32. Keep Your HEARTBEAT (.md) Small!

Every time `HEARTBEAT (.md)` runs, it loads into the agent's context and burns tokens. With a default interval of 30 minutes, a bloated heartbeat file compounds into serious cost over the course of a day.

Keep it under 20 lines with just a simple checklist covering things like active task freshness, session health (archiving bloated sessions), self-review every few hours, and flagging anything urgent.

That's the extent of it. Heavy work goes in cron jobs with isolated sessions, not in the heartbeat. The heartbeat's job is to notice things, not to do things, and if it notices something that needs attention it alerts you or kicks off a cron job. It shouldn't be writing reports, generating content, or running complex analysis every 30 minutes.

The OpenClaw docs say it directly: "Keep HEARTBEAT (.md) small to minimize token overhead." Take that literally and seriously.

## 33. Skills Need Routing Logic

If you have multiple skills installed, the agent decides which skill to use based on the name and description in each skill's YAML frontmatter. The skill body only loads after the agent has already decided to trigger it. This means your routing logic lives entirely in the description field.

Without clear "use when" and "don't use when" triggers in each skill description, the agent misfires and picks the wrong skill for the job. You'll see it grab a research skill when you wanted a coding skill, or fire a deployment skill when you just wanted a status check.

Think of it as writing if/else logic for your agent's decision-making. Each skill description should be explicit about its trigger conditions: what context activates it, what context should not activate it, and what it does vs what it doesn't do. The OpenClaw skills docs emphasize this: the description is the primary triggering mechanism, and all "when to use" information must live there, not in the skill body.

## The Architecture That Works

After a week of running this 24/7 and debugging everything above, here's the pattern that actually holds up for me (never assume someone's setup will perfectly work for you either, audit it first, even ask OpenClaw):

You build a team of specialized agents, each with their own `SOUL (.md)` personality, workspace, and model. One agent (your CEO) handles all external communication via Telegram, Discord, or whatever channels you're running. The rest of your team (CTO, CMO, COO, whatever roles you need) stay internal and focus on their specialties. Any agent on the team can spawn subagents for background work that would otherwise block their main session, and those subagents complete atomic tasks and report back. Shared state lives in symlinked files so everyone reads from one source of truth, context gets pruned automatically, memory stays lean, `Boot.md` catches drift on every restart, and the error log is the first place you look when anything goes wrong.

30% of this work is building. 70% is debugging infrastructure you didn't know freaking know existed. That ratio doesn't change, but the debugging gets faster when you know where to look.

If you made it this far, you're already ahead of 99% of people who will bookmark this and never come back.

I'm not claiming to have all the answers. I'm building with this stuff daily, experimenting and breaking things constantly, and writing down what actually works so nobody else has to guess. No one has all the answers or the best setup for everyone, and if they claim so, they're lying. If something in this guide is wrong, missing, or outdated, tell me. I'd rather fix it than let someone build on bad information.

---

Follow me for more on all things AI: [@kloss_xyz](https://x.com/kloss_xyz)