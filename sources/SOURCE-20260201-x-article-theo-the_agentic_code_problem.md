---
url: https://x.com/theo/status/2018091358251372601
author: "Theo - t3.gg (@theo)"
captured_date: 2026-02-01
id: SOURCE-20260201-006
original_filename: "20260201-x_article-the_agentic_code_problem-@theo.md"
status: triaged
platform: x
format: article
creator: theo
signal_tier: tactical
topics:
  - claude-code
  - developer-tools
  - opinion
teleology: contextualize
notebooklm_category: claude-code
aliases:
  - "Theo - agentic code problem"
synopsis: "Theo (t3.gg) identifies the UX problem of running multiple parallel Claude Code workflows: when a notification sounds, you don't know which terminal tab finished. Highlights the emerging developer ergonomics challenge of managing multiple concurrent AI agent sessions across terminals, IDEs, and browsers."
key_insights:
  - "Running multiple parallel agentic coding sessions creates a new UX problem — managing attention across terminals, IDEs, and browser tabs for different projects."
  - "The notification/context-switching overhead of parallel agent workflows is an unsolved developer ergonomics challenge."
  - "As parallel agent sessions become the productivity standard, tooling must evolve to provide better session management and routing."
---
# The Agentic Code Problem

(Description: Diagram showing three projects (A, B, C) split across Terminal, IDE, and Browser tabs with specific ports and services labeled for each project)

*ding*

You hear a notification sound from a Claude Code workflow finishing. Which terminal tab was it?

Hop around terminal windows and tabs for a bit, finally find it. It was Project B. Okay, now which browser was that in...

Oh, it got assigned localhost:3001, now my auth redirects are broken. Which terminal tab is using :3000 right now?

Okay, it was Project A, just killed it. Where's the tab for Project B's dev server?

*ding*

Another workflow has finished. It briefly grabs your attention - just long enough to lose track of what you were doing.

**This is not your fault**

## Our tools were not built for how we work today.

Back in my day (read: 2 months ago), we worked on one thing at a time. Our work was split between 3 apps, the terminal, IDE and browser. Let's say we were working on Project A. It looked something like this:

(Description: Diagram labeled "Working on: Project A" showing Terminal column with "A: Dev server" and "A: tab for git", IDE column with "A: Workspace", and Browser column with "A: localhost" and "A: github")

Our work is split across multiple. Not great! But totally workable, because of our mental model:

(Description: Diagram labeled "Everything was contained under Project A" showing a large blue dashed box containing three columns (Terminal, IDE, Browser) with the same A-labeled items nested inside)

The split didn't matter because it was all grouped together in your head. Project A was split between apps, but we think of it differently. We used all of these apps WITHIN Project A.

But I'm not just working on Project A anymore.

## The Problem™

(Description: Diagram labeled "Working on: Project A, Project B, Project C" showing a 3x3 grid with three rows for each project. Each project has items in Terminal (Dev server, tab for git, cc/codex), IDE (Workspace), and Browser (localhost, github) columns, with colored text for each project - blue for A, red for B, and orange for C)

Oh...oh no...

When you have more than one project going, the mental model collapses.

(Description: Diagram showing three projects (A, B, C) split between columns but with separate colored sections and dashed boxes attempting to group them by project - demonstrating the fragmentation and lack of natural grouping)

Our projects are split BETWEEN apps, windows and tabs. There's no natural grouping! If I see some work finish in Claude Code for Project A, I have to go hunt for the *right* Chrome window/tab to see the results. If I want to check the code, I have to hop between multiple IDE windows trying to find it. When it's time to file a PR, good luck finding the right github tab!

The issues with this workflow go way deeper. Death by thousands of papercuts (in parallel!)

Do you split terminal between tabs or windows? Tmux?

How do you know which terminal window you are in?

What about your browser? How will you split your work up?

How do you handle collisions when everything uses :3000? Can your auth redirects handle it?

I fight these issues every single day. I spend more time switching between apps than I spend building.

## The Solution

I'll be honest, I don't have one. Here are some things I can confidently say are NOT a solution

**tmux** (Great for splitting terminals, does not help with mental overhead)

**Agent orchestration GUIs** (Roughly same as above)

**IDE w/ built-in browser** (Cool, what about github? Auth?)

**Docker** (lmao)

**Background agents** (Make agent management easier at the cost of everything else)

I am not writing this post to announce something or to sound smart. I really, really just want this fixed. I almost started to build an OS to do it.

I need to be realistic. I can't do this one. I don't have the skill, time or mental bandwidth to figure this one out.

I wrote this in hopes I can inspire others to solve this problem. There is no single "correct" solution to this. We need lots of them.

Experiment. It's never been easier to test out theories. Build new workflows. Feel this pain deeply. Try to fix it. Fail. Try again. Keep trying. We need to figure this out.

We need to change how we use computers.

---

**Post Details**
- Posted: 2:37 PM · Feb 1, 2026
- Views: 1.3M
- Replies: 300
- Reposts: 199
- Likes: 2,038
- Bookmarks: 2,164