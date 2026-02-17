---
url: https://x.com/nummanali/status/2021692332849131738
author: Numman Ali (@nummanali)
captured_date: 2026-02-13
---

# The Future of Engineering: Self Driving Software

How OpenAI, StrongDM, and I independently arrived at the same process for building software with coding agents.

OpenAI just published how their engineering team spent five months building a real product where every line of code was written by Codex. Earlier this month, StrongDM went public with their "Software Factory", a system where agents write and review all code without human intervention.

I've been doing the same thing at my company since November 2025.

Three teams. No coordination. Same conclusions.

Follow me through the details.

## What OpenAI built

(Description: Abstract 3D visualization on dark blue background featuring isometric geometric shapes in cyan and bronze/orange colors arranged in a scattered cluster pattern with subtle lighting effects suggesting depth and dimensionality.)

Their team started with an empty git repository in August 2025. Five months later:

- ~1 million lines of code
- ~1,500 pull requests merged
- 3 engineers at the start (now 7)
- Estimated 10x faster than writing by hand

Every line was written by Codex. Application logic, tests, CI configuration, documentation, internal tooling. The humans never contributed code directly. That became a core philosophy, not just a constraint.

The interesting part isn't the output volume. It's what happened to the engineers.

> "The primary job of our engineering team became enabling the agents to do useful work."

When something failed, the question was never "how do I write better prompts? - it was, "what capability or context is the agent missing, and how do I make it legible?"

They spent their time building feedback loops, structuring documentation, and designing environments. The code was a byproduct.

They report single Codex runs working on one task for six hours straight. Often while the team sleeps.

## What StrongDM built

(Description: Digital art showing a translucent glass screen or panel on dark blue background with various 3D geometric objects including spheres, cubes, and other crystalline shapes in shades of cyan, green, and blue, arranged as if floating behind the glass surface.)

A three-person team, working since July 2025. Justin McCarthy (StrongDM's CTO), Jay Taylor, and Navan Chauhan. They went public February 7th and hit Hacker News front page the same day. Simon Willison covered it immediately.

Their strongest idea: treat generated code like model weights. Opaque. Don't read it for correctness. Validate it through external behavior, the same way you'd evaluate a neural network through its outputs. What matters is whether the thing works.

To make that validation rigorous, they built Digital Twin Universes: behavioral clones of Okta, Jira, Slack, and Google Docs. Full API replicas that let agents run thousands of integration scenarios per hour. No rate limits, no API costs, no abuse detection triggers.

Test scenarios are stored outside the codebase as a holdout set. This is the key move. If tests live in the repo, agents can rewrite them to match broken code. External holdout sets can't be gamed.

Their coding agent, Attractor, is three markdown files. Natural language specs. Feed them to any modern coding agent and it builds itself.

## The patterns

(Description: Six wooden square tiles or blocks arranged in a horizontal line on dark blue background, each featuring different geometric patterns carved or embossed in gold/bronze tones - including grid patterns, circular spirals, leaf designs, and geometric arrangements.)

These teams didn't coordinate. They didn't read each other's work until after publishing. Here's what they all found.

### 1. Boring technology wins

Both teams chose composable, stable, well-documented tools. OpenAI says "boring" tech is easier for agents because it's well-represented in training data and has stable APIs. They went so far as to reimplement utility libraries rather than pull in packages with unpredictable behavior. StrongDM runs Go and Rust. Nobody picked anything exotic.

### 2. The repository is the only thing that exists

If knowledge lives in Slack threads, in someone's head, in a Google Doc, the agent can't see it. It doesn't exist. OpenAI's AGENTS.md is about 100 lines. Not an encyclopedia. A table of contents pointing to structured docs elsewhere. StrongDM uses natural language specs in markdown. Everything discoverable, everything versioned.

### 3. Full environments per branch

The agent needs to run what it built before anyone reviews it. OpenAI made their app bootable per git worktree so Codex could launch its own instance per change. They wired Chrome DevTools Protocol into the runtime so the agent can drive the UI, take screenshots, and validate its own work visually.

### 4. Mandatory automated verification

OpenAI's agents validate through DevTools Protocol and observability tooling. StrongDM validates through external holdout scenarios. Neither team trusts the agent's self-reported confidence.

### 5. Agents reviewing agents

OpenAI pushed almost all code review to agent-to-agent loops. Humans can step in but usually don't. StrongDM removed human review entirely.

### 6. Continuous cleanup

OpenAI's team used to spend every Friday fixing agent-generated drift. They called it "AI slop." That didn't scale. Now they run recurring agents that scan for pattern violations and open small refactoring PRs. Garbage collection, not spring cleaning.

## Why now

(Description: Dramatic landscape photograph featuring a bright golden-orange sun or light source on the horizon against a dark blue sky with warm golden rays or light streaks radiating upward in a natural sunrise or sunset scene.)

**GPT 5.2 Codex Extra High - the one that changed everything**

Before this generation of model, agents couldn't do complex work over long periods of time (context rot) to trust with large features end to end unsupervised. You could get through small pieces of work if there was a defined scope but not sustained, multi feature requirements that required architecture decisions and more to be done.

That's what has just been unlocked. The new Codex models are something else entirely and can obliterate work like we've never seen before.

Now a single agent can:

- Take a bug report
- Reproduce the failure
- Record a video demonstrating it
- Implement a fix
- Validate the fix by driving the application
- Open a pull request
- Respond to review feedback
- Handle CI failures
- Merge

One prompt. OpenAI reports this happening routinely. Single runs lasting six hours, producing working features while the team is asleep.

The model capability crossing that threshold is what made the rest of the process viable. Boring tech, structured repos, automated verification: none of it matters if the agent can't sustain coherent work.

## How I build software now

(Description: Abstract digital artwork on dark blue background showing a network visualization with multiple glowing spheres in warm gold and orange tones connected by thin lines in a geometric pattern, suggesting interconnected systems or nodes in a distributed network.)

I made this shift in early December 2025, when Opus 4.5 and GPT 5.2 dropped. The capabilities had improved enough that the economics flipped. I stopped writing code and started designing environments.

At RetailBook, I run a large TypeScript monorepo that has six applications, over twenty shared packages.

Here's how the work actually flows.

### Planning

Every feature starts with Claude Opus 4.6 writing the plan. Opus understands intent better than any model I've used. It captures the why behind a feature, the edge cases, the integration points. Then GPT 5.3 Codex augments the plan for thoroughness, filling in technical detail and catching gaps.

### Implementation

Then it flips. Codex takes over and does all the implementation work, end to end. Writing code, writing tests, updating configuration, handling dependencies. No human code in the loop.

### UI review

If the work touches frontend, Opus does a second pass. It reviews the generated Playwright screenshots and catches visual issues that Codex misses. Opus is significantly better at understanding whether a UI looks right. This two-model approach gets results that neither model achieves alone.

### Code review

The PR goes up. Multiple GitHub action supported agents review it, each running a different model. Different perspectives on the same code. Any findings get routed back to Codex for fixes. The loop continues until all agent reviewers pass.

High-stakes changes still get human eyes. I review the PR and check the preview deployment. Not every PR needs this. But some do, and knowing which is part of the judgment that hasn't been automated yet.

### Testing and environments:

- Every branch gets a full preview deployment across the entire monorepo. All six apps, all twenty-plus packages.
- Scenario-based seed data ensures everything is covered and reproducible. Not random fixtures. Deliberate scenarios that exercise real user journeys.
- E2E tests through Playwright are mandatory. No PR merges without them passing. The test suite is fast because I designed it that way from the start.

Everything is accessible to agents. Feature flags, managed by agents. Local development, staging, production, all logs. If the agent can't reach it, it can't reason about it. Same principle OpenAI and StrongDM found independently.

## The one-man team

(Description: Cinematic dark scene showing a solitary human figure standing in the center, backlit by bright golden-orange light, surrounded by a massive network of floating illuminated boxes, digital elements, and data points in cyan and warm tones arranged in a complex three-dimensional space suggesting advanced technology and connectivity.)

Here's what I've never said out loud. I'm a one-person engineering team.

I tried to hire three times. It was genuinely difficult. The role isn't "software engineer" anymore. It's engineer, product manager, and agent orchestrator in one.

You need someone who can design systems, translate product intent into specs, and build the scaffolding that makes agents productive. That combination is rare right now.

The job title I landed on: **Senior Agent Native Product Engineer**.

I finally found my first hire, they join next month! Everything is prepared for them: the monorepo, the CI, the preview environments, the agent workflows, the documentation. They're walking into a system designed to be orchestrated, not coded.

As I find new patterns that work, I'll share them. This is early. The process is still forming. But the direction is clear and the independent validation from OpenAI and StrongDM gives me confidence it's the right one.

## Where this goes

(Description: Serene landscape photograph showing a calm horizon line at dusk or dawn, with warm golden-orange tones in the upper atmosphere transitioning to cooler blue tones in the lower sky and reflecting on still water below, suggesting a peaceful sunset or sunrise over a body of water.)

Three teams arrived at the same answer because the problem has the same shape everywhere: make it possible for agents to do reliable, sustained work with minimal hand-holding.

The discipline hasn't gone away. It moved. From the code to the scaffolding. From writing software to designing the environments, feedback loops, and verification systems that let agents write software well.

This isn't a prediction. It's a description of where things already are.

---

ps. I hope you can tell I like using Nano Banana Pro