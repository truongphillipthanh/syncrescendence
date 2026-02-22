---
url: https://www.aihero.dev/my-agents-md-file-for-building-plans-you-actually-read
title: My AGENTS.md file for building plans you actually read
domain: aihero.dev
author: Matt Pocock
published_date: null
captured_date: 2026-02-20
content_type: blog
id: SOURCE-20260113-001
original_filename: 20260113-aihero-my-agents-md-file-for-building-plans-aihero.md
status: triaged
platform: aihero
format: article
creator: aihero
signal_tier: tactical
topics:
  - "claude-code"
  - "ai-engineering"
  - "best-practices"
  - "tutorial"
teleology: implement
notebooklm_category: claude-code
aliases:
  - "AIHero - AGENTS.md Planning Loop"
synopsis: "Describes a planning loop technique using AGENTS.md that transforms AI from unreliable code generator to indispensable coding partner. Four-step process: describe what you want, let AI create a plan, review and refine, then execute."
key_insights:
  - "The planning loop transforms AI from unreliable code generator to indispensable coding partner by separating planning from execution"
  - "AGENTS.md file acts as persistent instructions that shape how the AI approaches planning and implementation across sessions"
  - "A four-step process (describe, plan, review, execute) consistently produces better results than direct code generation requests"
---
# My AGENTS.md file for building plans you actually read
Most developers are skeptical about AI code generation at first. It seems impossible that an AI could understand your codebase the way you do, or match the instincts you've built up over years of experience.
But there's a technique that changes everything: the planning loop. Instead of asking AI to write code directly, you work through a structured cycle that dramatically improves the quality of what you get.
This approach transforms AI from an unreliable code generator into an indispensable coding partner.
## The Plan Loop: A Four-Step Process
Every piece of code now goes through the same cycle.
(Image: A circular diagram showing four colored boxes connected by arrows in a cycle. The boxes are labeled "PLAN" (blue), "EXECUTE" (orange), "TEST" (yellow), and "COMMIT" (green). Arrows connect them in sequence: PLAN → EXECUTE → TEST → COMMIT → PLAN)
**Plan** with the AI first. Think through the approach together before writing any code. Discuss the strategy and get alignment on what you're building.
**Execute** by asking the AI to write the code that matches the plan. You're not asking it to figure out what to build—you've already done that together.
**Test** the code together. Run unit tests, check type safety, or perform manual QA. Validate that the implementation matches what you planned.
**Commit** the code and start the cycle again for the next piece.
## Why This Matters
This loop is completely indispensable for getting decent outputs from an AI.
If you drop the planning step altogether, you're really hampering yourself. You're asking the AI to guess what you want, and you'll end up fighting with hallucinations and misunderstandings.
Planning forces clarity. It makes the AI's job easier and your code better.
## Rules for Creating Great Plans
Here are the key rules from my `CLAUDE.md` file that make plan mode effective:
```
## Plan Mode
- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.
```
These simple guidelines transform verbose plans into scannable, actionable documents that keep both you and the AI aligned.
Copy them into your `CLAUDE.md` or `AGENTS.md` file, and enjoy simpler, more readable plans.
Or, run this script to append them to your `~/.claude/CLAUDE.md` file:
```bash
mkdir -p ~/.claude && cat >> ~/.claude/CLAUDE.md << 'EOF'
## Plan Mode
- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.
EOF
```
---
(Image: AIHero branding logo with colorful star design in orange, yellow, and purple)