# 🔑 You're Using Opus 4.6 Wrong

(Description: A dark-themed graphic showing pixelated block-style text reading "OPUS 4.6" with a yellow chevron arrow (>) and dash (-) symbol in the upper left corner)

## Overview

everyone's posting Opus 4.6 benchmark comparisons.

cool. now show me the workflow.

i've been running Claude Opus 4.6 since launch. not benchmarking it. not testing trivia questions. running actual work through it, every day, for real output.

and here's what i realized after the first few days: individual prompts are a dead end.

one prompt gives you one output. you tweak it, get a slightly better output, and move on. next day you're starting from scratch again. there's no compounding. no system. just isolated moments of "that was pretty good."

the people getting real results aren't using prompts. they're running systems.

so i built one. five prompts that connect into a loop. each one feeds the next. the system gets smarter the longer you run it because context accumulates, patterns emerge, and Claude starts anticipating what you need before you ask.

here's the entire system, prompt by prompt, with the honest breakdown of what works and what doesn't.

## The Foundation: Why a System Beats a Prompt Collection

before the prompts, let me explain the architecture.

most people collect prompts like recipes. they bookmark 47 of them, use 2, forget the rest.

a system is different. it's a connected workflow where the output of step 1 becomes the input for step 2, and the insight from step 5 feeds back into step 1.

### Here's the Loop:

**step 1: AUDIT.** figure out what's actually draining your time and energy

**step 2: ARCHITECT.** plan the solution before building anything

**step 3: BUILD + REVIEW.** execute and quality-check in one pass

**step 4: REFINE.** run the output through a convergence loop until it hits your bar

**step 5: COMPOUND.** weekly review that stacks improvements and feeds back into step 1

each step has one prompt. the prompts are designed to work together but each one is independently useful too.

you don't need to run all five from day one. start with prompt 1. add one per week. by week 5, the full loop is running and compounding.

i'll also give you the honest take on Opus 4.6 at the end. what's genuinely better, what's the same, what's worse. no hype.

let's build.

## Step 1: THE AUDIT (Find What's Actually Worth Automating)

this is where most people skip straight to "give me a cool prompt." wrong move. if you automate the wrong thing, you just made a fast version of something that shouldn't exist.

this prompt turns Opus 4.6 into a productivity analyst that maps your actual workflow, scores each task by energy drain and automation potential, and hands you a prioritized 4-week plan.

the key difference from a generic "help me be productive" prompt: it scores tasks on TWO dimensions. time consumed AND mental energy drained. sometimes a 15-minute task that sits in the back of your mind all day is worth automating before a 2-hour task that doesn't bother you.

### The Prompt:
```
You are a Productivity Systems Analyst. Your specialty: identifying the highest-leverage automation opportunities in someone's specific workflow. Your approach is diagnostic, not prescriptive. You don't assume what needs fixing. You investigate first. Work through this process:

PHASE 1: DISCOVERY

Ask me 4-5 targeted questions about my work and daily routine. Focus on:
> what tasks repeat weekly or daily
> what I procrastinate on or dread
> what requires context-switching between tools
> what produces the most output relative to effort
> what I'd delegate to an assistant if I had one

Keep it conversational. One question at a time. Dig deeper on anything that sounds like a bottleneck.

PHASE 2: SCORING

Based on my answers, create a task inventory. For each task, score on two dimensions (1-10 scale):
> TIME COST: hours per week spent on this task
> ENERGY DRAIN: mental load this task creates, even when you're not doing it (rumination, dread, context-switching cost)

Then calculate an AUTOMATION SCORE using this formula:

Automation Score = (Time Cost + Energy Drain) × Feasibility Rating

Where Feasibility Rating is:
1.0 (fully automatable), 0.7 (partially automatable), 0.3 (needs human judgment but AI can assist)

Rank everything by Automation Score, highest first.

PHASE 3: THE 4-WEEK PLAN

Build a progressive automation calendar:
> Week 1: highest-scoring task that's also simplest to set up (quick win for momentum)
> Week 2: highest-scoring remaining task
> Week 3: highest-scoring remaining task
> Week 4: highest-scoring remaining task

For each week, provide:
> the specific task being automated
> which tool handles it best (default to Claude unless something else is genuinely better for the job)
> exact setup steps I can follow today
> expected time saved per week
> the trigger, the process, and the output format

RULES:
> Be specific to MY situation. No generic productivity advice.
> If a task is better handled by a specialized tool (Zapier for app connections, Apple Shortcuts for phone workflows, a simple script for data tasks), say so. Don't force everything into Claude.
> Simplest working version first. We can optimize later.
> After each phase, pause and check in before continuing.
```

when i ran this on Opus 4.6, something interesting happened. previous models would ask surface-level questions like "what's your job title?" Opus 4.6 asked things like "of the tasks you mentioned, which one do you find yourself thinking about even when you're not working on it?" That's the energy drain dimension at work. it's mapping the invisible cost, not just the visible one.

the adaptive thinking in Opus 4.6 matters here. it doesn't apply the same reasoning depth to "what time do you start work?" as it does to "how should we prioritize automation of your content pipeline vs your client onboarding?" simple questions get fast answers. complex tradeoff analysis gets genuine deliberation.

if you automate just one task per week using this plan, you'll have 4 workflows running within a month. in 3 months, 12. you'll be ahead of 99% of people still bookmarking "top 10 ai tools" threads they'll never read.

## Step 2: THE ARCHITECT (Plan Before You Build)

here's where most people waste hours. they jump straight into building, hit a wall, backtrack, rebuild, hit another wall.

this prompt turns Opus 4.6 into a solution architect that creates a complete implementation blueprint BEFORE you write a single line of code or set up a single automation. it asks the questions a senior engineer would ask in a design review.

this one is especially powerful with Opus 4.6's 1M token context window. you can feed it your entire codebase, documentation, or project context and it actually holds it all in working memory while designing the solution.

### The Prompt:
```
You are a Solution Architect specializing in AI-augmented workflows. Your job: create a clear implementation blueprint before any building begins. I'm going to describe a problem I want to solve or a workflow I want to automate.

Before proposing any solution, work through this framework:

STEP 1: PROBLEM DEFINITION

Restate my problem in your own words. Then ask me 2-3 clarifying questions focused on:
> what "done" looks like (specific output, format, destination)
> what constraints exist (tools I already use, budget, technical skill level)
> what I've already tried (so we don't repeat failed approaches)

STEP 2: APPROACH MAP

Present 2-3 possible approaches, ranked by simplicity. For each:
> describe the approach in plain language
> list the tools/components needed
> estimate setup time (be honest, not optimistic)
> name the biggest risk or failure point
> rate complexity: SIMPLE (afternoon project) / MODERATE (weekend project) / COMPLEX (multi-day project)

Recommend one approach and explain why. But give me the choice.

STEP 3: IMPLEMENTATION BLUEPRINT

For the chosen approach, create a step-by-step blueprint:
> break the build into phases (never more than 4)
> each phase should produce something testable
> specify: what to build, what to test, what "working" looks like at each stage
> flag any decisions I'll need to make during the build
> include rollback points (if this phase fails, here's how to recover without losing earlier work)

STEP 4: DEPENDENCY CHECK

Before I start building, confirm:
> what accounts/tools/APIs do I need access to?
> what data or assets do I need to prepare?
> are there any costs I should know about?
> what's the first concrete action I should take right now?

RULES:
> Simplest working version first. Always. We can add complexity later.
> Don't assume technical knowledge. If a step requires something non-obvious, explain it.
> If my idea is overcomplicated, tell me. Suggest the simpler version.
> If my idea won't work, tell me why and propose what will.
> No jargon without immediate explanation.
```

the architecture prompt is the one people skip. and it's the one that saves the most time.

i used this to plan an automated content pipeline last week. my first instinct was to build a complex multi-tool workflow with Zapier, a database, and three different APIs. the Architect prompt mapped three approaches. the simplest one, a Claude-native workflow with a single Google Sheet as the database, handled 90% of my requirements. took an afternoon instead of a weekend.

that's the value of planning: you avoid building the complex thing when the simple thing works.

## Step 3: THE ANALYST (Build and Review in One Pass)

this is the engineering prompt. works for code reviews, vibe coding projects, automation debugging, or any technical build.

the key design choice: instead of asking Claude to "review my code" (vague, produces generic feedback), you embed your actual engineering standards directly into the prompt. Claude reviews like a senior developer who knows how YOU think about quality.

i restructured this from a framework that's been circulating in the Claude Code community. the original was solid but overbuilt for most users. this version is tighter and works for both experienced developers and vibe coders.

### The Prompt:
```
You are a Senior Engineering Analyst. Your job: review my code (or plan, or automation) the way a principal engineer would during a design review. Thorough, opinionated, constructive.

BEFORE making any changes to the code, review it completely. For every issue or recommendation:
> explain the concrete tradeoff (not just "this is bad" but "this approach trades X for Y")
> give your recommended fix with reasoning
> ask for my input before assuming a direction

MY ENGINEERING STANDARDS (use these to calibrate your review):

> Repetition is debt. Flag any duplicated logic aggressively.
> Tests are non-negotiable. I'd rather over-test than under-test.
> Code should be "engineered enough." Not fragile and hacky. Not prematurely abstracted. The sweet spot in the middle.
> Handle more edge cases, not fewer. Thoughtful error handling over optimistic happy-path code.
> Explicit beats clever. If I have to think twice to understand it, simplify it.

REVIEW PROCESS (work through each section, pause after each for my feedback):

1. ARCHITECTURE SCAN
> system design and component boundaries
> data flow: where does information enter, transform, and exit?
> dependency health: anything fragile, outdated, or unnecessary?
> scaling characteristics: what breaks first under load?

2. CODE QUALITY PASS
> organization and readability
> DRY violations (flag with file + line references)
> error handling coverage
> edge cases: what inputs or states would cause unexpected behavior?
> technical debt: anything that works now but will cause pain later?

3. RELIABILITY CHECK
> test coverage gaps (what's untested that should be tested?)
> assertion quality (are tests actually verifying the right things?)
> failure modes: what happens when external services are down, data is malformed, or timeouts occur?

4. PERFORMANCE SCAN
> unnecessary database calls or API requests
> memory usage patterns
> caching opportunities
> anything that's slow now or will be slow at scale

FOR EACH ISSUE:
> describe the problem with specific file and line references
> present 2-3 options (always include "leave it as-is" when reasonable)
> for each option: effort required, risk level, maintenance burden
> recommend one option and explain why
> wait for my confirmation before moving on
```

Opus 4.6 handles this prompt noticeably better than previous models. the adaptive thinking scales its analysis depth to the complexity of the code. a simple utility function gets a quick review. a complex state management system gets deep analysis with genuine tradeoff reasoning across multiple concerns.

tip: customize the "engineering standards" section to match YOUR actual preferences. that's the difference between generic feedback and feedback that feels like a collaborator who knows your codebase.

for vibe coders who aren't writing code directly: this works equally well for reviewing code that Claude Code or Cursor generated for you. paste in what was generated, run this review, catch problems before they compound.

## Step 4: THE REFINERY (Recursive Improvement Until Convergence)

this is the pattern that makes everything else better. the concept: instead of generating once and shipping, you tell Claude to generate, score its own output against specific criteria, diagnose what's weak, rewrite, and re-score until it converges on quality.

i rebuilt this from a marketing framework into a clean, reusable system. the key improvement: it tracks the delta between versions so you can see exactly what changed and why. it also detects when it's hit diminishing returns and stops instead of endlessly rewriting.

### The Prompt:
```
You will use a convergence loop to produce the highest quality output for this task.

Here's the process:

1. GENERATE: Create your first version based on my request.

2. SCORE: Rate your output against these criteria (1-10 each):
> [CRITERION 1 - specific to your task]
> [CRITERION 2 - specific to your task]
> [CRITERION 3 - specific to your task]
> [CRITERION 4 - specific to your task]

Calculate an overall quality score (average of all criteria).

3. DIAGNOSE: For any criterion below 8/10:
> identify the specific weakness (not vague, specific: "paragraph 3 uses generic examples instead of named sources")
> explain WHY it scored low
> describe your planned fix

4. REWRITE: Apply the fixes. Produce version 2.

5. RE-SCORE: Rate version 2 against the same criteria.

6. CONVERGENCE CHECK:
> if all criteria are 8/10 or above: stop and present the final version
> if overall score improved by less than 0.5 from previous version: stop (diminishing returns)
> otherwise: repeat steps 3-5

7. FINAL OUTPUT: Present:
> the final version
> final scores for each criterion
> a brief changelog: what changed between v1 and the final version, and why

My request: [YOUR TASK HERE]

Scoring criteria for this task:
> [CUSTOMIZE BASED ON TASK TYPE - see examples below]
```

### Customization Guide by Task Type:

**for writing or content:** hook strength, clarity and flow, specificity (named examples, real numbers), emotional resonance, actionability

**for code:** correctness, readability, edge case handling, performance characteristics, test coverage

**for research or analysis:** source quality, depth of reasoning, practical applicability, logical structure, intellectual honesty

**for emails or outreach:** tone calibration, brevity, clarity of ask, personalization, professional warmth

Opus 4.6's adaptive thinking makes this loop actually work. on previous models, the "self-scoring" was often performative. the model would say "7/10 on specificity" and then rewrite with the same level of specificity. Opus 4.6 genuinely engages deeper reasoning to diagnose root causes in its own output.

when i tested this on an article draft, v1 scored 6/10 on specificity. the model diagnosed the problem as "using generic category references instead of named companies and data points." v2 replaced generic examples with specific named sources and concrete numbers. v3 hit 9/10. the self-diagnosis was accurate, not theater.

## Step 5: THE COMPOUNDER (The Weekly Review That Makes the System Smarter)

this is the prompt most people would never think to build. and it's the one that turns five isolated prompts into an actual system.

every Friday (or whatever your review day is), you run this prompt. it reviews what you automated that week, what worked, what didn't, and plans the next week's automation target. over time, it builds a pattern library of what works for YOUR specific workflow.

### The Prompt:
```
You are my Weekly Systems Review Partner. Every week, we review what I automated, what worked, what broke, and what to tackle next.

Here's our review process:

1. PROGRESS CHECK

I'll tell you what I automated or built this week. For each item, help me assess:
> is it actually saving time, or did I just move the work around?
> is the quality of the output good enough, or does it need refinement?
> what broke or caused friction this week?

2. FRICTION LOG

Help me identify the biggest remaining friction points in my workflow. Ask me:
> what task annoyed me most this week?
> where did I waste time on something that felt automatable?
> what manual step kept appearing inside an automated workflow?

3. NEXT WEEK'S TARGET

Based on our original Audit results and this week's friction log:
> recommend the next task to automate
> suggest improvements to existing automations
> flag any automation that should be simplified or removed (yes, sometimes removing complexity is the win)

4. PATTERN RECOGNITION

Look across all our previous reviews and identify:
> what types of automations consistently work well for me?
> what types consistently fail or get abandoned?
> any emerging patterns in what I find valuable vs what I thought would be valuable?

5. UPDATED SYSTEM MAP

Maintain a running inventory of:
> all active automations (what they do, which tools, estimated time saved)
> total estimated hours saved per week
> next 3 automation targets in priority order

RULES:
> Be honest. If something I built isn't actually useful, tell me.
> Track cumulative impact. I want to see the hours stack up over time.
> Challenge my assumptions. If I think something needs automation but the simpler fix is changing my process, say so.
> Reference our previous reviews when relevant. Build on what we've learned.
```

this prompt leverages Opus 4.6's context management features. with the 1M token context window, it can hold several weeks of review history in a single conversation. the context compaction feature means it automatically summarizes older reviews to preserve space for new ones without losing the important patterns.

the compounding effect is real. week 1, you have one automation saving maybe 2 hours. week 4, you have four saving 6-8 hours. week 12, you have a dozen micro-systems running your workflow and Claude knows your patterns well enough to suggest automations you hadn't considered.

## How the System Connects

the five prompts aren't random. they form a cycle:

**THE AUDIT** identifies what to automate
→ **THE ARCHITECT** plans how to build it
→ **THE ANALYST** reviews what you built
→ **THE REFINERY** polishes the output quality
→ **THE COMPOUNDER** reviews the week and feeds insights back into the next AUDIT

each prompt makes the others better. the Architect creates cleaner plans because the Analyst's review standards are embedded in your thinking. the Refinery produces better output because the Audit identified the right tasks. the Compounder detects patterns that improve future Audits.

that's the difference between a prompt collection and a system. prompts are isolated events. systems compound.

## The Honest Take on Opus 4.6

after running real work through it for weeks, here's where i landed:

### What's Genuinely Better:

**adaptive thinking is real.** the model dynamically adjusts its reasoning depth based on task complexity. ask a simple question, get a fast answer. give it a complex multi-step problem, it actually deliberates. this isn't marketing language. you can feel the difference in how it handles the Analyst prompt on simple vs complex code.

**the 1M token context window changes what's possible for large projects.** feeding an entire codebase into the Analyst prompt, or maintaining weeks of review history in the Compounder, simply wasn't feasible before. context compaction helps too. it automatically summarizes older conversation turns to preserve space without losing critical decisions.

**sub-agent orchestration is a quiet upgrade.** when you give Opus 4.6 a complex task, it recognizes when parts of the work would benefit from being delegated to specialized sub-processes. you don't have to prompt for this. it just does it.

### What's About the Same:

standard writing tasks, basic Q&A, simple content generation. if your workflow is mostly "write me a caption," you won't notice a meaningful jump. the improvements show up on complex, multi-step, reasoning-heavy tasks.

### What's Worse:

some users report that the optimization for precision and structured reasoning makes freeform creative output feel more mechanical. if you want pure creative writing, test it against Sonnet before committing. also, pricing scales significantly past 200K tokens. the 1M context window is powerful but not free.

the pattern holds with every model release: about 20% of workflows genuinely improve. the other 80% stays the same. the people who benefit aren't the ones reading every benchmark thread. they're the ones who run 5 real prompts and make a decision in 30 minutes.

## Why This Works (And Why Most Prompt Collections Don't)

the problem with "500 prompts for ChatGPT" lists: they optimize for breadth. one prompt for emails. one for code. one for recipes. no connection between them. no compounding.

this system optimizes for depth. five prompts, tightly connected, that get better the longer you use them.

the uncomfortable truth about AI productivity: the tool doesn't matter nearly as much as the system around it. people chase the latest model release looking for a magic upgrade. the real upgrade is building a workflow that compounds regardless of which model you're running.

Opus 4.6 is the best model i've used for this system. but the system works on GPT-5.2 too. and it'll work on whatever ships next quarter. because the architecture is model-agnostic. the intelligence compounds in the workflow, not just the model.

## Start Here

don't try to implement all five prompts today. that's how systems die.

here's the actual sequence:

**week 1:** run the Audit prompt. identify your top 4 automation targets. automate the easiest one.

**week 2:** run the Architect prompt on your second target. build it.

**week 3:** use the Analyst prompt to review what you built in weeks 1-2. fix what's broken.

**week 4:** run the Refinery on your most important output. see the quality jump.

**week 5:** run the Compounder. review everything. plan the next month.

if you automate one thing per week, you'll have 12 workflows running in 3 months. most people reading this will bookmark it and never start. the ones who run Prompt 1 tonight will have a completely different relationship with their workload by March.

copy the prompts. customize the criteria to your actual work. keep what's better, ignore what isn't.

that's the whole system.

---

p.s. if you want to see more AI tips & workflows, subscribe to my free newsletter here.