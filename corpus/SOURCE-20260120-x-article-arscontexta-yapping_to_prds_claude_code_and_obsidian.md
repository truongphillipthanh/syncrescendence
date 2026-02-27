# Yapping to PRDs: Claude Code & Obsidian

(Description: Engraved illustration in classical style showing a bearded man in period clothing with pointed hat, gesturing expressively while sitting at a desk with a laptop. Drafting tools, scrolls, hourglasses, and architectural elements surround him, rendered in black ink with detailed cross-hatching.)

## Overview

Meetings used to be overhead, now yapping is work.

When my coworker and I yap about a project we record it. An hour later the transcript gets processed and suddenly there's:

- Documentation
- Feature ideas in the backlog
- Decisions captured with their reasoning
- The project status updated
- Notes about our working philosophy extracted

Everything is connected with wikilinks to all the notes we had before.

(Ralph is also happy because he gets his polished PRDs right after the meeting.)

(Description: Engraved illustration showing an elderly bearded man in historical robes leaning over a young child who is sitting at a laptop, both rendered in classical cross-hatched ink style with period architectural details and scholarly instruments in the background.)

## Project Structure Example

This is what a processed project structure could look like:
```
team-vault/
├── 01_Inbox/
│   └── README.md
├── 02_Projects/
│   ├── README.md
│   ├── Habit-Tracker-App/
│   │   ├── Habit-Tracker-App.md
│   │   ├── Ideas/
│   │   │   ├── Streak Notifications.md
│   │   │   └── Social Accountability.md
│   │   └── Meetings/
│   │       ├── 2026-01-08 Kickoff.md
│   │       └── 2026-01-15 MVP Scope.md
│   ├── Recipe-Manager/
│   │   ├── Recipe-Manager.md
│   │   ├── Docs/
│   │   │   └── Database Schema.md
│   │   ├── Ideas/
│   │   │   └── AI Meal Planning.md
│   │   └── Meetings/
│   │       └── 2026-01-12 Feature Prioritization.md
│   └── Workout-Logger/
│       ├── Workout-Logger.md
│       └── Meetings/
│           └── 2026-01-10 Technical Planning.md
├── 03_Areas/
│   ├── README.md
│   ├── Design-System/
│   │   └── Component Library.md
│   ├── Infrastructure/
│   │   ├── Deployment Pipeline.md
│   │   └── Monitoring Setup.md
│   └── User-Research/
│       └── Interview Insights.md
├── 04_Knowledge/
│   ├── README.md
│   ├── Frameworks/
│   │   └── React Native Patterns.md
│   └── Tools/
│       └── Supabase.md
├── 05_Archive/
│   ├── README.md
│   └── Transcripts/
│       ├── 2026-01-08 Kickoff Transcript.md
│       ├── 2026-01-10 Technical Planning Transcript.md
│       ├── 2026-01-12 Feature Prioritization Transcript.md
│       └── 2026-01-15 MVP Scope Transcript.md
└── CLAUDE.md
```

These are not random meeting summaries. This is a structured system where every piece of knowledge lives in a specific place and wikilinks connect ideas across the whole network.

(The folder system is basically the PARA system from Tiago Forte, which is usually thought for personal knowledge management but works great for team projects too.)

### What's the most efficient way to build this?

**Transcript mining.**

I'll break down the command I use for this at the end.

## Documentation Is For Agents Now

This only works if you learn to manage context and structure knowledge for retrieval so Claude can actually find what it needs.

When Claude needs to understand your deployment setup it loads `03_Areas/Infrastructure/Deployment Pipeline`, when it needs the database schema it loads `02_Projects/Recipe-Manager/Docs/Database Schema`, when it needs to understand a past decision it loads the meeting where you discussed it.

Everything is defined in `claude.md` which tells Claude the vault philosophy, folder structure, how to navigate and how to take notes.

Each folder has a README that goes deeper into that specific folder philosophy (more on this setup in another post).

Without structure you just have a pile of meeting notes.

With structure you have a knowledge system that Claude can build on.

And most importantly that you can build on together with Claude.

Feature brainstorming becomes way better when Claude has all the context, all the ideas you've had before, all the decisions you've made, all the competitor research and all the user feedback.

Product steering becomes a real conversation when the context window is decorated with everything relevant.

That's what I mean by **ars contexta**.

## Why Yapping?

When people say LLMs aren't there yet, it's usually a context problem. The knowledge exists somewhere but the model can't access it.

Some of that is locked in slide decks and PDFs, but that's basically solved with vision models now.

The harder problem is **tacit knowledge** — the stuff that's hard to articulate because it lives in your head as intuition.

I noticed this when building automated note-taking systems. My philosophy of how I write notes, connect them and structure knowledge was way more complex than I thought, and a lot of it happened subconsciously. I couldn't write it down because I didn't know I was doing it.

Transcripts help to externalize that.

When you talk through something you naturally include your reasoning path, your uncertainties, the alternatives you considered. You explain things in depth because you're responding to another person. All of that becomes capturable context.

## The Command

This is what a command like this could look like, but to work efficiently it needs a LOT of your note-taking philosophy in the `claude.md` as well.

The core idea is simple: **this is mining not summarizing**.

A rich 1-hour meeting can yield 10+ ideas, multiple frameworks, a dozen decisions and state changes across multiple projects. If you're producing a short summary with 3–4 bullet points you're not going deep enough.

### Define a Role

First I like to define a role:
```
<role>
you are the knowledge architect for this vault. you process meeting transcripts with exhaustive depth, mining every valuable insight, idea, philosophy, decision and status update. meetings are the primary sync mechanism between reality and vault state. missing content is unacceptable.
</role>
```

### Tell It What to Look For

Then tell it what to look for:
```
as you read, actively hunt for:

- feature ideas ("wouldnt it be cool if...", "we could also...")
- project sparks (new tool concepts, standalone initiatives)
- frameworks (mental models, principles, ways of thinking)
- philosophies (team beliefs, working principles)
- decisions (explicit choices made, direction set)
- status updates ("X is now live", "Y is on hold")
- action items (tasks assigned, next steps)
- blockers (what is preventing progress)

look for implicit content too:

- ideas embedded in problem discussions ("the issue is we dont have X" → X is an idea)
- philosophies expressed as asides ("we always say..." → philosophy)
- decisions made by NOT deciding ("lets not wait for..." → decision)
```

### Plan All Extractions

Before writing anything make it plan all extractions:
```
before writing anything, plan all extractions:

example todo list for a complex meeting:

1. archive raw transcript
2. create meeting summary
3. update project A status (now live)
4. update project B status (blocked on X)
5. create idea: feature X for project A
6. create idea: feature Y for project A
7. create idea: new tool concept Z
8. add philosophy to team hub
9. update project hubs with new decisions
```

### Vault State Synchronization

The key insight is **vault state synchronization**:
```
meetings reveal new reality. update the vault to match.

for each project mentioned:

1. read the current hub to understand existing state
2. identify discrepancies between hub and meeting discussion
3. update status if changed (active → paused, prototype → live)
4. add decisions to key decisions section
5. add meeting link to recent meetings
6. link new ideas in ideas section
```

### Set Quality Standards

And set quality standards so it doesn't just skim:
```
before marking processing complete, verify:

- read entire transcript (no skimming)
- all explicit decisions captured
- all implicit decisions captured
- all feature ideas extracted (even casual mentions)
- all frameworks/philosophies captured
- all status changes reflected in project hubs
- state sync complete (vault reflects post-meeting reality)

red flags (processing incomplete):

- meeting summary is shorter than 1 page for hour+ meeting
- only 1-2 ideas extracted from brainstorming discussion
- no state changes identified in status-heavy meeting
```

## What Does Good Output Look Like?

For a 1h 20m weekly coordination meeting:

- 1 archived transcript
- 1 comprehensive meeting summary
- 7 feature idea notes across multiple projects
- 2 framework notes
- 4 philosophy additions to team hub
- 3 project hub status updates
- 9 hub updates across projects and areas
- 20+ files created or modified

---

**Yapping IS work.**

—heinrich