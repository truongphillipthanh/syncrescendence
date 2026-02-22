---
id: SOURCE-20251202-944
platform: youtube
format: lecture
cadence: evergreen
value_modality: audio_primary
signal_tier: strategic
status: raw
chain: null
topics:
  - "vibes"
  - "allowed"
  - "solving"
  - "hard"
  - "problems"
creator: "AI Engineer"
guest: null
title: "No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer"
url: "https://www.youtube.com/watch?v=rmvDxxNubIg"
date_published: 2025-12-02
date_processed: 2026-02-22
date_integrated: null
processing_function: transcribe_youtube
integrated_into: []
duration: "20m 31s"
has_transcript: no
synopsis: "No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer by AI Engineer. A lecture covering vibes, allowed, solving."
key_insights: []
visual_notes: null
teleology: strategize
notebooklm_category: ai-engineering
aliases:
  - "No Vibes Allowed: Solving"
  - "No Vibes Allowed: Solving Hard Problems"
---

# No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer

**Channel**: AI Engineer
**Published**: 2025-12-02
**Duration**: 20m 31s
**URL**: https://www.youtube.com/watch?v=rmvDxxNubIg

## Description (no transcript available)

It seems pretty well-accepted that AI coding tools struggle with real production codebases. At AI Engineer 2025 in June, The Stanford study on AI's impact on developer productivity found:

A lot of the ""extra code"" shipped by AI tools ends up just reworking the slop that was shipped last week.

Coding agents are great for new projects or small changes, but in large established codebases, they can often make developers less productive.

The common response is somewhere between the pessimist ""this will never work"" and the more measured ""maybe someday when there are smarter models.""

After several months of tinkering, we've found that you can get really far with today's models if you embrace core context engineering principles.

This isn't another ""10x your productivity"" pitch. I tend to be pretty measured when it comes to interfacing with the ai hype machine. But we've stumbled into workflows that leave me with considerable optimism for what's possible. We've gotten claude code to handle 300k LOC Rust codebases, ship a week's worth of work in a day, and maintain code quality that passes expert review. We use a family of techniques I call ""frequent intentional compaction"" - deliberately structuring how you feed context to the AI throughout the development process.
 
In this talk, I'll share what we've learned since first sharing these techniques back in August, and some educated predictions on what's coming in the next 6-12 months for software engineers.

Speaker: twitter.com/dexhorthy

Timestamps:
00:00 intro: complex code
01:40 context engineering
02:53 advanced context
04:38 context obsession
05:55 dumb zone concept
07:26 context management
09:37 complex problem solved
10:45 semantic diffusion
12:14 onboarding agents ‍
13:57 internal docs lies
15:03 mental alignment key
16:12 code snippet plans
17:38 don't outsource think
18:45 rpi: smart zone
19:46 cultural change hard ‍‍

Hey - I'm Dex, and I'm hacking on getting AI coding agents to solve hard problems in complex codebases at HumanLayer. Before this I was working on APIs for agent orchestration and Human-in-the-Loop, and wrote the April 2025 essay "12 factor agents" that first coined the term Context Engineering. I've been coding since high school, when I built tools for NASA researchers to navigate the south pole of the moon. Enjoyer of tacos and burpees (not necessarily in that order).
