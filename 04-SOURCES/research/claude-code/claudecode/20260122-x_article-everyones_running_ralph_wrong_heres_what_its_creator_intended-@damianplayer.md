---
url: "https://x.com/damianplayer/status/2014327653264744566"
author: "Damian Player (@damianplayer)"
captured_date: "2026-01-24"
---

# EVERYONE'S running ralph wrong. here's what its creator intended..

(Description: Hero image featuring a cartoon character with wide eyes, labeled "NO MORE RALPH" in bold yellow text against dark background. The character appears to be Ralph from The Simpsons, rendered in monochromatic line-art style.)

## Overview

4 days ago I wrote about ralph, the AI coding loop that builds software while you sleep. Zero lines written manually. That post blew up. But here's the thing: after watching dozens of people try to implement it, I realized most are doing it wrong. Even Anthropic's official plugin misses the point. The creator, Jeff Huntley, has called this out publicly.

So what's the actual canonical way? And why does getting it wrong turn a $30 build into a $300 mess that still doesn't work?

Let me break it down.

## The One Insight That Makes Ralph Work

Ralph isn't about running AI in a loop. Any script can do that.

Ralph works because it keeps the AI operating in its smartest mode.

Here's what most people don't understand about large language models: they get worse as context grows.

Think of the context window like a whiteboard. At the start, it's clean. The AI reads your instructions clearly. Executes precisely. Makes smart decisions.

But as the conversation continues, that whiteboard fills up. Old code. Previous attempts. Failed approaches. Random tangents.

By the time you're mostly full, the AI is wading through noise to find signal. It forgets things. Contradicts itself. Makes obvious mistakes.

Ralph solves this by wiping the whiteboard after every single task.

Fresh start. Full brainpower. Every time.

## Why Anthropic's Plugin Gets It Wrong

The official Ralph Wiggum plugin from Anthropic does something the creator never intended.

Instead of wiping context completely, it compacts.

Compaction means the AI looks at everything that happened and picks out what it thinks is important to carry forward.

Sounds reasonable. But there's a fatal flaw.

The AI doesn't know what's actually important. It guesses. And when it guesses wrong, critical information disappears. Bugs compound. Features break in ways that don't make sense.

The whole point of ralph vanishes.

The plugin also adds max iterations and completion conditions. But sometimes you want ralph to keep running indefinitely. It finds bugs you didn't know existed. Adds improvements you didn't think of. Surfaces edge cases that would have broken production.

When you cap iterations, you cut off that discovery.

## The Growing File Problem

Another common mistake: letting the AI modify its own instructions on each loop.

One popular approach has the agent update an `agents.md` file every iteration. Learning from what it did. Adding notes for next time.

Sounds smart. Breaks everything.

Models are verbose by default. Each loop adds tokens. Ten iterations in, you've stuffed the context window before the actual task even starts.

You've pushed the AI into the zone where it starts making mistakes while trying to make it smarter.

The canonical ralph keeps the prompt static. The only thing that changes is a simple flag marking tasks complete. Nothing else grows.

## What Jeff Huntley Actually Intended

The original implementation is brutally simple.

One bash while loop.

It reads a prompt file. Runs Claude. Waits for it to finish. Loops again.

That's it.

No compaction. No growing memory files. No clever additions.

The prompt tells the AI: read the plan, pick the most important incomplete task, implement it, test it, commit it, mark it done. Exit when everything passes.

The key is that the loop lives outside the model's control. The AI can't decide when to stop. It can't modify the loop itself. It just executes tasks until the external script sees everything marked complete.

This keeps the AI focused on one thing at a time with maximum context available for that one thing.

## The Task Structure That Works

Your plan file needs specific structure. Vague tasks produce vague results.

Each task should have:

- A clear category (frontend, backend, database, etc.)
- A specific description of what done looks like
- Concrete validation steps the AI can check
- A passes flag (true or false)

The AI reads the plan, finds tasks where passes is false, picks the highest priority one, implements it, runs the validation steps, and only marks passes true if everything checks out.

Your exit condition: the loop only stops when every single task shows passes true.

If you're lazy with task definitions, ralph is lazy with implementation. Garbage in, garbage out.

## Variations That Don't Break the Core

Some people have built on ralph correctly.

One approach runs multiple ralphs in parallel. Different tasks, different instances, all feeding into the same codebase. Dramatically faster for large projects.

Another uses browser automation for validation. Instead of just running tests, the AI actually opens the app, clicks through flows, verifies things work like a real user would.

A third treats tasks as GitHub issues. Ralph picks the most important open issue, implements it, closes the issue when done. Clean integration with existing workflows.

These all work because they add capabilities without breaking the fundamental principle: fresh context every loop.

The moment you start accumulating state inside the context window, you're back to the original problem.

## When Ralph Makes Sense

Ralph is a proof of concept machine.

You have an idea. You want to see if the architecture works. You want to validate your tech stack choices before committing to a full build.

Ralph can build the entire thing overnight. Multiple versions if you want. You wake up, review what it created, and know whether your approach is sound.

This is incredibly valuable. The exploratory phase that used to take weeks now takes hours.

But ralph is not production engineering.

The code needs review. Edge cases need human judgment. Architectural decisions need context ralph doesn't have.

Use ralph to validate. Use your actual engineering process to ship.

## The Setup in 10 Minutes

Ralph is free and open source: https://github.com/snarktank/ralph

You need four files.

**`prompt.md`**: Static instructions that never change. Tells the AI how to read the plan, pick tasks, implement, validate, and mark complete.

**`prd.md`**: Your task list. Every feature broken into specific, validatable chunks with passes flags.

**`activity.md`**: A log file. Each loop appends what happened. This gives you visibility without bloating context (the AI reads it fresh each time).

**`settings.json`**: Sandbox configuration. Limits what commands the AI can run. You're giving it permissions to act autonomously, so constrain the damage radius.

Create the prd by describing your project to Claude. Have it generate the task breakdown. Review and adjust. Then run the loop.

Most projects need 15-25 iterations. Budget accordingly.

## The Cost Math

Typical ralph run: 10-20 iterations at roughly $2-3 each. Call it $30-50 for a complete proof of concept.

One builder shipped an entire app that would have cost $50,000 to hire out. Spent under $300.

The economics only work if you're getting clean iterations. If your implementation is wrong and the AI is spinning in circles, you burn tokens accomplishing nothing.

**Correct setup**: $30 and a working proof of concept.

**Wrong setup**: $300 and a broken mess you have to rebuild manually.

The difference is fresh context every loop.

## The Bottom Line

Ralph works because it respects how AI actually functions. Limited context, maximum focus, clean resets.

The moment you add compaction, growing files, or accumulated state, you're fighting against the architecture instead of working with it.

One bash loop. Static prompt. Clean task list. Fresh start every iteration.

That's it. That's the whole thing.

Part one showed you what ralph can build. This showed you how to actually build it right.

---

## Call to Action

I put together a one-pager with my exact Claude code setup. The interview prompt. The progress file template. The feature testing checklist. Everything I covered here in a copy-paste format.

RT + comment "RALPH" and I'll send it over.

If you want more breakdowns like this:

- **YouTube** (launching soon): https://www.youtube.com/@damianplayer (deep dives and tutorials)
- **LinkedIn**: https://www.linkedin.com/in/damianplayer (daily posts on AI and business)

---

**Post Analytics**: 184 replies, 183 reposts, 1048 likes, 2459 bookmarks, 158,604 views | Posted: Jan 22, 2026 at 5:21 AM