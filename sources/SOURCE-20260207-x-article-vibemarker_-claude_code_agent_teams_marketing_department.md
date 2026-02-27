---
url: https://x.com/VibeMarketer_/status/2020142441769156678
author: "J.B. (@VibeMarketer_)"
captured_date: 2026-02-13
id: SOURCE-20260207-015
original_filename: "20260207-x_article-claude_code_agent_teams_marketing_department-@vibemarker_.md"
status: triaged
platform: x
format: article
creator: vibemarker_
signal_tier: tactical
topics: [claude-code, ai-agents, content-creation, tutorial]
teleology: implement
notebooklm_category: claude-code
aliases: ["VibeMarketer - Agent Teams Marketing Department"]
synopsis: "Guide to building a marketing department inside Claude Code's Agent Teams feature, with specialized agents for different marketing functions. Reports 'kind of ridiculous' results using agent swarms for marketing workflows across major projects."
key_insights: ["Agent Teams can be structured as functional departments (marketing) with specialized agents for different marketing functions", "The marketing use case benefits from parallelism: research, copywriting, and campaign planning can run simultaneously", "Non-technical marketers can leverage Agent Teams by describing desired marketing workflows in plain language"]
---
# Claude Code Just Shipped Agent Teams. Here's How to Build Your Own Marketing Department Inside It.

(Description: Hero image showing a glowing plus/cross symbol on a blue circuit board background with golden light rays, and a person visible from the side in amber lighting. Text overlay reads "claud agent swarm (for marketers)")

## Overview

I've been using it on every major project and the results have been kind of ridiculous. Here's how it works:

Now, first of all - this isn't another prompt trick. It's a new way to run multiple Claude instances that actually work together.

One lead coordinating, multiple teammates executing in parallel, all communicating with each other in real time.

It's experimental right now, and you have to enable it manually. But if you're running any kind of marketing operation, this changes the game.

## How It Actually Works Under the Hood

You tell Claude to create a team and define the roles. It spawns separate instances - each with their own context window, and they get to work. The lead coordinates. Teammates claim tasks from a shared list. And unlike subagents (which just report back), teammates can message each other directly.

That last part is the unlock. They don't just work in parallel, they collaborate, challenge each other, and build on each other's findings.

## Real Marketing Use Cases

### Campaign Research Sprint

"Create an agent team to research the launch strategy for [product]. Spawn three teammates: one on competitor ad analysis, one on customer voice mining from reviews and reddit, one stress-testing our current positioning against what they find. Have them share findings and challenge each other."

They work simultaneously. When the competitor researcher finds a gap, the positioning teammate pressure-tests whether we can actually own it. The voice-of-customer teammate validates whether real buyers even care. The lead synthesizes into a strategy doc.

### Landing Page Builds

"Create an agent team to build the landing page for [offer]. One teammate on copy and messaging, one on conversion structure and CRO, one running adversarial review as a skeptical buyer. Require plan approval before any implementation."

The plan approval piece is key - each teammate has to outline their approach before executing. The lead reviews and either approves or sends back with feedback. Catches bad directions before they waste cycles.

### Ad Creative Exploration

"Spawn 4 teammates to explore different hook angles for [product]. Have them each develop one direction, then debate which is strongest. Update findings doc with consensus."

The debate structure is the secret sauce. One agent exploring alone tends to anchor on the first decent idea. Four agents actively trying to disprove each other? The angle that survives is actually battle-tested.

### Content Production

"Create a team for this week's content. One teammate on search intent and competitive gaps, one drafting based on findings, one running the recursive quality loop on every piece before it ships."

Parallel processing instead of sequential bottleneck. Research and production happen at the same time, with built-in QA.

You get the idea. These are just a couple of examples but imagination is the limit in terms of how far you want to take this.

## How to Set Up Agent Swarms in Claude Code

### Enable Agent Teams

Add this to your `settings.json`:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Key Commands & Techniques

1. **Tell Claude to create a team in natural language.** Be specific about roles. "One teammate on X, one on Y, one playing devil's advocate" works. "Make a team to help with marketing" doesn't.

2. **Use delegate mode** if you want the lead to only coordinate. Press Shift+Tab after starting the team. This prevents the lead from doing the work itself - it only spawns, assigns, and synthesizes.

3. **Require plan approval for high-stakes work.** Add "require plan approval before they make any changes" to your prompt. Each teammate outlines their approach, the lead reviews, and only approved plans get executed.

4. **Talk to teammates directly when needed.** Shift+Up/Down to select a teammate, then type. You can redirect anyone without going through the lead.

5. **Use the shared task list.** The lead creates tasks, teammates claim them. You can check status anytime with Ctrl+T. If something's stuck, nudge the teammate or reassign.

6. **Let them argue.** When you tell teammates to "challenge each other" or "debate," they actually do. Don't flatten this - the friction is where the insight lives.

## Mistakes to Avoid

- **Don't use agent teams for simple tasks.** Single deliverables, quick copy tweaks, sequential work - just use one session. The coordination overhead isn't worth it.

- **Don't let teammates edit the same files.** Two agents writing to the same doc = overwrites. Break work so each owns different pieces.

- **Don't spawn too many teammates.** 3-5 is usually right. More than that and coordination overhead kills you.

- **Don't let them run unattended too long.** Check in, redirect, synthesize as they go. The longer they run without input, the higher the risk of wasted work.

- **Don't forget context.** Teammates don't inherit the lead's conversation history. Include relevant context in your spawn prompts.

- **Don't skip plan approval on complex work.** It feels slower but catches bad directions before they burn cycles.

## Things to Keep in Mind

- **Teammates each have their own context window.** They load project context (CLAUDE.md, skills, MCP servers) but not the lead's conversation history.

- **Token usage scales with team size.** Each teammate is a separate Claude instance. Worth it for complex work, overkill for simple tasks.

- **Task dependencies work automatically.** When a teammate completes a task that others depend on, blocked tasks unblock.

- **You can specify models.** "Use Sonnet for each teammate" if you want to manage costs.

- **Shutdown can be slow.** Teammates finish their current work before stopping.

- **Clean up through the lead.** When you're done, tell the lead to clean up. Don't have teammates do it - can leave things in a broken state.

## Final Thoughts

Again, this isn't for everything. Quick copy tweaks, single deliverables, sequential work - just use one session and keep it simple.

But for anything that benefits from parallel research, multiple perspectives, and built-in pressure-testing? Agent teams compound fast.

If you're interested in more AI marketing news like this, feel free to follow me @VibeMarketer_. I'll keep dropping updates like these as often as possible. Thanks for reading :)