---
id: SOURCE-20260131-x-thread-exm7777-how_to_build_a_claude_skill
platform: x
format: thread
creator: exm7777
title: how to build a claude skill
status: triaged
original_filename: "20260131-x_thread-how_to_build_a_claude_skill-@EXM7777.md"
url: https://x.com/EXM7777/status/2017659658425758193
author: "Machina (@EXM7777)"
captured_date: 2026-01-31
signal_tier: tactical
topics:
  - claude-code
  - prompt-engineering
  - content-creation
teleology: implement
notebooklm_category: claude-code
aliases:
  - "Machina - Claude Skill for humanized writing"
synopsis: "Guide for building a Claude Skill that writes humanized AI content using a two-pass approach: pass one diagnoses banned phrases, repetitive sentence lengths, and audience intent; pass two rewrites accordingly. Teaches Claude to think in diagnostic then execution passes."
key_insights:
  - "The two-pass Skill approach (diagnose then rewrite) produces more human-sounding output than single-pass prompting."
  - "Banning specific AI-sounding phrases ('leverage,' 'robust,' 'delve') and flagging repetitive sentence lengths catches the most common tells."
  - "Protecting factual elements (numbers, names, dates) while rewriting style prevents hallucination during the humanization pass."
---
# How to Build a Claude Skill to Consistently Write Humanized AI Content

how to build a Claude Skill to consistently write humanized AI content:

**the core idea is simple: teach Claude to think in two passes**

**pass one is diagnosis**
> scan for banned phrases ("leverage," "robust," "delve")
> flag repetitive sentence lengths
> mark facts that must stay untouched (numbers, names, dates)
> identify your audience and intent

**pass two is reconstruction**
> rewrite with the diagnosis in mind
> preserve every fact you marked
> vary sentence rhythm naturally
> replace abstract verbs with concrete ones
> cut template structures

but here's what makes this different from a prompt:

you don't want to be giving Claude rules... you want to feed it with reference materials it can read

create a references folder with:
- rubric file (8 criteria for what "human enough" means)
- edit-library file (before/after examples of each transformation type)
- taboo-phrases file (categorized list of AI-isms to eliminate)
- fact-preservation file (rules for what never changes)

then build validation scripts:
- one checks if facts got preserved
- one scans for banned phrases
- one measures readability metrics
- one flags if you changed too much

the Skill file itself just routes traffic... it reads your input, picks which preset to use, runs the two passes, validates output

AI humanization fails a lot because it's vague... "write like a human" means nothing to an LLM

but "score above 4 on natural rhythm, eliminate these 17 phrase patterns, keep sentence variance between 8-25 words" is executable

your Skill becomes a system, now your goal is to update it as you detect what makes AI content sound AI

(Description: Code screenshot showing file structure for the humanize-ai-content Skill with directories including: humanize-ai-content/, skills.md, references/, rubric.md, edit-library.md, taboo-phrases.md, fact-preservation.md, and related validation scripts with annotations describing the purpose of each component)