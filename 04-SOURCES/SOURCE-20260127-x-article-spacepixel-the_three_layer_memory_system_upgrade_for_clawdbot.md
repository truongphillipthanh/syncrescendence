---
url: https://x.com/spacepixel/status/2015967798636556777
author: "pixel (@spacepixel)"
captured_date: 2026-02-04
id: SOURCE-20260127-004
original_filename: "20260127-x_article-the_three_layer_memory_system_upgrade_for_clawdbot-@spacepixel.md"
status: triaged
platform: x
format: article
creator: spacepixel
signal_tier: strategic
topics:
  - ai-agents
  - automation
  - framework
  - best-practices
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "pixel - three layer Clawdbot memory"
synopsis: "Architectural guide for upgrading Clawdbot's static memory into a self-maintaining, compounding knowledge graph with three layers: Layer 1 (entity-based knowledge graph with atomic facts in items.json and living summaries), Layer 2 (daily notes as raw event logs), Layer 3 (tacit knowledge in MEMORY.md). Includes automatic fact extraction via cheap sub-agents every 30 minutes and weekly synthesis crons that prune stale context."
key_insights:
  - "Facts should be superseded rather than deleted — marking old facts as historical while preserving full history enables tracing how relationships and context evolved over time."
  - "The compounding flywheel (conversation → fact extraction → knowledge graph → weekly synthesis → better context → better responses) makes the assistant progressively smarter at pennies per day in sub-agent costs."
  - "Entity-based storage (per person, company, project) with tiered retrieval (summary first, raw facts on demand) beats both monolithic context files and black-box vector databases for transparency and maintainability."
---
# The Three-Layer Memory System Upgrade for Clawdbot

(Description: A futuristic digital illustration showing a holographic crab-bot with glowing blue and purple energy connecting to a knowledge network. On the left is a stack of leather-bound books labeled "OLD STATIC MEMORY." The crab's claws extend toward a dynamic network diagram with interconnected nodes labeled PEOPLE, COMPANIES, PROJECTS, and WEEKLY SYNTHESIS, illustrating the transformation from static to dynamic memory systems.)

Give your Clawdbot a knowledge graph that compounds forever

Most AI assistants forget by default. Clawdbot doesn't—but out of the box, its memory is still **static**.

This guide upgrades Clawdbot's memory into a **self-maintaining, compounding knowledge graph** that evolves automatically as your life changes.

And all you have to do is copy this article into your Clawdbot — it will know what to do.

No stale context. No manual cleanup. No "I already told you this."

## How Clawdbot Memory Works (Out of the Box)

Clawdbot already ships with solid primitives:

- **AGENTS.md** — behavioral rules and operating principles
- **MEMORY.md** — persistent user preferences
- **Heartbeats** — periodic wake-ups
- **Cron jobs** — scheduled automation

This is enough for basic continuity. Your Clawdbot remembers preferences, follows your rules, and can act proactively.

But there's a structural flaw.

All of this memory is static. You have to maintain it manually.

Life doesn't work that way.

You wrote "my boss Sarah is difficult" six months ago. You've since changed jobs. You like your new manager.

Your Clawdbot still thinks you hate your boss.

This system fixes that.

## What This Upgrade Adds

The **Three-Layer Memory System** turns memory from a flat file into a living knowledge graph:

- **Automatic fact extraction** — Every ~30 minutes, a cheap sub-agent scans conversations and saves durable facts (pennies per day).
- **Entity-based storage** — Facts are stored by **person**, **company**, or **project**—not dumped into a single blob.
- **Weekly synthesis** — A Sunday cron rewrites summaries from raw facts and prunes stale context automatically.
- **Superseding, not deleting** — When facts change, old ones are marked historical. Full history is preserved.

Result: Your Clawdbot's understanding updates itself. Context stays current without manual edits.

## The Three-Layer Architecture
```
Layer 1: Knowledge Graph (/life/areas/)
└── Entities with atomic facts + living summaries

Layer 2: Daily Notes (memory/YYYY-MM-DD.md)
└── Raw event logs — what happened, when

Layer 3: Tacit Knowledge (MEMORY.md)
└── Patterns, preferences, lessons learned
```

This isn't just memory. It's **compounding intelligence**.

Every conversation adds signal. Every week, that signal is distilled. Six months from now, your Clawdbot understands your life—structured, searchable, and current.

## Layer 1: The Knowledge Graph

This is where the magic happens.

Every meaningful entity in your life gets a folder:
```
/life/areas/
├── people/
│   ├── sarah/
│   │   ├── summary.md
│   │   └── items.json
│   ├── maria/
│   ├── emma/
│   └── sarah-connor/
├── companies/
│   ├── acme-corp/
│   ├── newco/
│   └── skynet/
```

### Atomic Facts (items.json)

Every fact is stored as a discrete, timestamped unit:
```json
{
  "id": "sarah-003",
  "fact": "Difficult manager, micromanages",
  "timestamp": "2025-06-15",
  "status": "active"
}
```

When reality changes, facts are **superseded**, not erased:
```json
{
  "id": "sarah-003",
  "status": "superseded",
  "supersededBy": "sarah-007"
},
{
  "id": "sarah-007",
  "fact": "No longer works together — left Acme Corp",
  "timestamp": "2026-01-15",
  "status": "active"
}
```

Nothing is lost. Your Clawdbot can trace how relationships evolved over time.

### Living Summaries (summary.md)

Your Clawdbot never loads hundreds of raw facts into context.

Instead, each entity has a **weekly-rewritten snapshot**:
```markdown
# Sarah

Former manager at Acme Corp (2024–2025). No longer relevant after job change.
```

Old information fades naturally. Context stays lean and accurate.

## Layer 2: Daily Notes

`memory/2026-01-27.md` — the raw timeline.
```markdown
# 2026-01-27

- 10:30am: Shopping trip
- 2:00pm: Doctor follow-up
- Decision: Calendar events now use emoji categories
```

This is the "when" layer.

Clawdbot writes these continuously. Durable facts are later extracted into Layer 1.

## Layer 3: Tacit Knowledge

**MEMORY.md** captures how **you** operate.
```markdown
## How I Work

- Sprint worker — intense bursts, then rest
- Contact preference: Call > SMS > Email
- Early riser, prefers brief messages

## Lessons Learned

- Don't create cron jobs for one-off reminders
```

These aren't facts about the world. They're facts about **you**.

(The file already exists—the upgrade simply formalizes its role.)

## The Compounding Engine

This is where basic Clawdbots get left behind.

### Real-Time Extraction (Every ~30 Minutes)

A cheap sub-agent (e.g. Haiku, ~$0.001) scans recent conversations for durable facts:

- "Maria's company hired two developers"
- "Emma took her first steps"
- "Started new job, reports to James"

The main model stays idle unless you're actively chatting. Cost: pennies per day.

### Weekly Synthesis (Sunday)

Once a week, Clawdbot:

- Reviews newly added facts
- Updates relevant summaries
- Marks contradicted facts as historical
- Produces a clean, current snapshot

No manual edits. No stale assumptions.

## The Flywheel
```
Conversation
↓
Facts extracted (cheap)
↓
Knowledge graph grows
↓
Weekly synthesis
↓
Better context next chat
↓
Better responses
↓
More conversation
```

This compounds.

- **Week 1:** Basic preferences
- **Month 1:** Routines, key people
- **Month 6:** Projects, milestones, relationships
- **Year 1:** A richer model of your life than most humans have

All human-readable. All searchable. Always current.

## Why This Beats Everything Else

**Vector databases / RAG**
Black box. You can't inspect what the AI "knows."

**Monolithic context files**
Don't scale. Go stale. Expensive to load.

**Basic Clawdbot**
Strong foundation, but static.

**Three-Layer Clawdbot**
Readable files. Automatic maintenance. Compounding intelligence.

## Implementation Guide

### 1. Create the folder structure
```bash
mkdir -p ~/life/areas/people
mkdir -p ~/life/areas/companies
mkdir -p ~/clawd/memory
```

### 2. Add to AGENTS.md
```markdown
## Memory — Three Layers

### Layer 1: Knowledge Graph (`/life/areas/`)

- `people/` — Person entities
- `companies/` — Company entities

Tiered retrieval:
1. summary.md — quick context
2. items.json — atomic facts

Rules:
- Save facts immediately to items.json
- Weekly: rewrite summary.md from active facts
- Never delete — supersede instead
```

### 3. Add to HEARTBEAT.md
```markdown
## Fact Extraction

On each heartbeat:
1. Check for new conversations
2. Spawn cheap sub-agent to extract durable facts
3. Write to relevant entity items.json
4. Track lastExtractedTimestamp

Focus: relationships, status changes, milestones
Skip: casual chat, temporary info
```

### 4. Weekly synthesis cron (Sunday)
```markdown
## Weekly Memory Review

For each entity with new facts:
1. Load summary.md
2. Load active items.json
3. Rewrite summary.md for current state
4. Mark contradicted facts as superseded
```

### 5. Atomic fact schema
```json
{
  "id": "entity-001",
  "fact": "The actual fact",
  "category": "relationship|milestone|status|preference",
  "timestamp": "YYYY-MM-DD",
  "source": "conversation",
  "status": "active|superseded",
  "supersededBy": "entity-002"
}
```

## The Result

A Clawdbot that:

✅ Never forgets
✅ Never goes stale
✅ Costs pennies to maintain
✅ Understands boss vs former boss
✅ Gets smarter every week

While other assistants wake up with amnesia, yours wakes up **better informed than yesterday**.

The knowledge graph grows. The context improves. The responses get better.

This is the difference between an AI assistant and an AI that actually knows you.

Copy this article into your Clawdbot. Tell it to set up the Three-Layer Memory System. Then watch it compound.