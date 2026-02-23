---
id: SOURCE-20251230-661
platform: youtube
format: interview
cadence: evergreen
value_modality: dialogue_primary
signal_tier: paradigm
status: raw
chain: null
topics:
  - "state"
  - "reasoning"
  - "imo"
  - "ioi"
  - "gold"
creator: "Latent Space"
guest: null
title: "[State of RL/Reasoning] IMO/IOI Gold, OpenAI o3/GPT-5, and Cursor Composer — Ashvin Nair, Cursor"
url: "https://www.youtube.com/watch?v=4JHXU1Cpcsc"
date_published: 2025-12-30
date_processed: 2026-02-22
date_integrated: null
processing_function: transcribe_youtube
integrated_into: []
duration: "45m 13s"
has_transcript: no
synopsis: "[State of RL/Reasoning] IMO/IOI Gold, OpenAI o3/GPT-5, and Cursor Composer — Ashvin Nair, Cursor by Latent Space. A interview covering state, reasoning, imo."
key_insights: []
visual_notes: null
teleology: implement
notebooklm_category: coding-tools
aliases:
  - "[State of RL/Reasoning] IMO/IOI"
  - "[State of RL/Reasoning] IMO/IOI Gold, OpenAI"
---

# [State of RL/Reasoning] IMO/IOI Gold, OpenAI o3/GPT-5, and Cursor Composer — Ashvin Nair, Cursor

**Channel**: Latent Space
**Published**: 2025-12-30
**Duration**: 45m 13s
**URL**: https://www.youtube.com/watch?v=4JHXU1Cpcsc

## Description (no transcript available)

From Berkeley robotics and OpenAI's 2017 Dota-era internship to shipping RL breakthroughs on GPT-4o, o1, and o3, and now leading model development at *Cursor,* *Ashvin Nair* has done it all. We caught up with Ashvin at *NeurIPS 2025* to dig into the inside story of OpenAI's reasoning team (spoiler: it went from a dozen people to 300+), why *IOI Gold felt reachable in 2022 but somehow didn't change the world* when o1 actually achieved it, how RL doesn't generalize beyond the training distribution (and why that means you need to bring economically useful tasks _into_ distribution by co-designing products and models), the deeper lessons from the RL research era (2017–2022) and why most of it didn't pan out because the community overfitted to benchmarks, how *Cursor is uniquely positioned to do continual learning at scale* with policy updates every two hours and product-model co-design that keeps engineers in the loop instead of context-switching into ADHD hell, and his bet that the next paradigm shift is *continual learning with infinite memory*—where models experience something once (a bug, a mistake, a user pattern) and never forget it, storing millions of deployment tokens in weights without overloading capacity.
We discuss:

* Ashvin's path: *Berkeley robotics PhD → OpenAI 2017 intern (Dota era) → o1/o3 reasoning team → Cursor ML lead* in three months
* Why *robotics people are the most grounded at NeurIPS* (they work with the real world) and simulation people are the most unhinged (Lex Fridman's take)
* The *IOI Gold paradox:* "If you told me we'd achieve IOI Gold in 2022, I'd assume we could all go on vacation—AI solved, no point working anymore. But life is still the same."
* The *RL research era (2017–2022) and why most of it didn't pan out:* overfitting to benchmarks, too many implicit knobs to tune, and the community rewarding complex ideas over simple ones that generalize
* Inside the *o1 origin story:* a dozen people, conviction from Ilya and Jakob Pachocki that RL would work, small-scale prototypes producing "surprisingly accurate reasoning traces" on math, and first-principles belief that scaled
* The *reasoning team grew from ~12 to 300+ people* as o1 became a product and safety, tooling, and deployment scaled up
* Why *Cursor is uniquely positioned for continual learning:* policy updates every two hours (online RL on tab), product and ML sitting next to each other, and the entire software engineering workflow (code, logs, debugging, DataDog) living in the product
* *Composer* as the start of product-model co-design: smart enough to use, fast enough to stay in the loop, and built by a 20–25 person ML team with high-taste co-founders who code daily
* The *next paradigm shift: continual learning with infinite memory*—models that experience something once (a bug, a user mistake) and store it in weights forever, learning from millions of deployment tokens without overloading capacity (trillions of pretraining tokens = plenty of room)
* Why *off-policy RL is unstable* (Ashvin's favorite interview question) and why Cursor does two-day work trials instead of whiteboard interviews
* The vision: automate software engineering as a process (not just answering prompts), co-design products so the entire workflow (write code, check logs, debug, iterate) is in-distribution for RL, and make models that *never make the same mistake twice*

—
Ashvin Nair

* Cursor: \
* X: \

00:00:00 Introduction: From Robotics to Cursor via OpenAI
00:01:58 The Robotics to LLM Agent Transition: Why Code Won
00:09:11 RL Research Winter and Academic Overfitting
00:11:45 The Scaling Era and Moving Goalposts: IOI Gold Doesn't Mean AGI
00:21:30 OpenAI's Reasoning Journey: From Codex to O1
00:20:03 The Blip: Thanksgiving 2023 and OpenAI Governance
00:22:39 RL for Reasoning: The O-Series Conviction and Scaling
00:25:47 O1 to O3: Smooth Internal Progress vs External Hype Cycles
00:33:07 Why Cursor: Co-Designing Products and Models for Real Work
00:34:14 Composer and the Future: Online Learning Every Two Hours
00:35:15 Continual Learning: The Missing Paradigm Shift
00:44:00 Hiring at Cursor and Why Off-Policy RL is Unstable
