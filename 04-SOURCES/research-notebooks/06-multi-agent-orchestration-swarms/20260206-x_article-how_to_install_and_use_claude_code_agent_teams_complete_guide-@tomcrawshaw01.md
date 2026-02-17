---
url: https://x.com/tomcrawshaw01/status/2019778646043758957
author: Tom (@tomcrawshaw01)
captured_date: 2026-02-06
---

# How to Install and Use Claude Code Agent Teams (Complete Guide)

(Description: A dark-themed header image displaying the text "AGENT TEAMS" in large white letters. Below the title is a network diagram showing a central orange node with connections to five smaller orange nodes labeled "research", "code", "test", "review", and "display".)

OpenClaw's community was already orchestrating multi-agent sessions with custom skills. Now Anthropic shipped it natively into Claude Code. Here's how to set it up and start using it today.

## OpenClaw built it first, now Anthropic made it official

The OpenClaw community figured this out first. They built custom skills that let you orchestrate multiple Claude Code sessions working together on the same project, coordinating tasks, sharing context, running in parallel.

It was clever, it worked, and it clearly caught Anthropic's attention.

Because they just shipped the same thing natively into Claude Code. No plugins, no workarounds, no custom skills. It's built right in now and they're calling it "agent teams."

Instead of one agent doing everything in a straight line while you sit there watching it think, a lead agent now breaks your task into pieces, spins up multiple teammates, and they all go to work at the same time while actually coordinating with each other.

Think of it like going from one freelancer doing everything solo to a project manager who shows up with a full crew and delegates across all of them.

It's in research preview right now, most people don't know about it yet, and this guide covers everything you need to install it, configure it, and actually use it properly.

## One agent used to do everything solo, now it shows up with a team

Up until this update, Claude Code worked like a single employee. You'd give it a job, it would start at step one, finish it, move to step two, finish that, and keep going until the whole thing was done. Sequentially. One task at a time.

Agent teams change that completely. You describe what you want, and instead of one agent grinding through it alone, a lead agent looks at the task, breaks it into pieces, and spins up separate teammates to handle different parts at the same time.

One teammate might be researching your codebase while another is debugging a function while another is writing tests. They each have their own context window, their own workspace, and they can message each other directly to share what they're finding.

The lead agent stays on top of all of it, coordinating the work, managing a shared task list, and pulling everything together once the teammates finish.

You can even jump in and talk to any teammate directly if you want to redirect them or ask a follow-up question without going through the lead.

## "But wait, aren't sub-agents already a thing?" - yes, and here's the difference

If you've been using Claude Code for a while, you've probably already used sub-agents. They spin up inside your session, do a focused task, and report the result back to the main agent. Simple, effective, and relatively cheap on tokens.

Agent teams are a different animal. Each teammate is a fully independent Claude Code session with its own context window. They don't just report back to the lead, they talk to each other directly, share findings, challenge each other's work, and self-coordinate through a shared task list.

Sub-agents are like sending an assistant to go grab you an answer. Agent teams are like putting a group of specialists in a room and letting them work through a problem together.

The practical difference comes down to one question: do your workers need to communicate with each other? If the answer is no and you just need a quick result, sub-agents are the move. If the answer is yes and the work benefits from collaboration, that's where agent teams come in.

Sub-agents are cheaper on tokens and better for focused tasks. Agent teams cost more but they handle complex, multi-part work that would take a single agent significantly longer to get through.

## When agent teams actually make sense and when they're overkill

Agent teams are not a "use this for everything" feature. They add coordination overhead and they burn through tokens significantly faster than a single session. So you want to be intentional about when you spin one up.

The sweet spots are tasks where parallel exploration genuinely adds value. Research and review is a great one, where multiple teammates investigate different angles of a problem at the same time and then compare notes. Building new features where each teammate owns a separate module or file is another.

Debugging is where it gets really interesting. Instead of one agent going down a single path and potentially wasting time on the wrong theory, you can spin up multiple teammates to test competing hypotheses in parallel. The one that finds the answer first wins, and the others can stop.

Cross-layer work is solid too. One teammate on the frontend, one on the backend, one writing tests. Each owns their own piece without stepping on each other.

Where agent teams don't make sense is anything sequential. If step two depends on step one being finished first, there's no benefit to parallelizing. Same-file edits are a bad idea because two teammates touching the same file leads to overwrites. And simple tasks where the coordination overhead costs more than just letting one agent handle it quickly.

Before you spin up a team, ask yourself if the work can genuinely be split into independent pieces. If yes, go for it. If not, a single session or sub-agents will serve you better and cost you less.

## How to enable agent teams in your settings (takes 30 seconds)

Agent teams are experimental and disabled by default, so you need to flip them on before you can use them. There are two ways to do it.

The first way is through your settings.json file. Open it up and add this:
```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

The second way is to set it as an environment variable directly in your shell. Either approach works, but settings.json is cleaner if you want it to persist across sessions.

That's it. Once that's in place, Claude Code will recognize agent team commands and you can start spinning up teams. If you want to dig into the full documentation beyond what this guide covers, Anthropic has it all here: https://code.claude.com/docs/en/agent-teams

## Starting your first agent team and what to actually say

You don't need to learn any special syntax. You just describe what you want in plain language and tell Claude to create a team.

Here's an example prompt that works well because it gives the lead clear, independent roles to assign:

> I'm designing a CLI tool that helps developers track TODO comments across their codebase. Create an agent team to explore this from different angles: one teammate on UX, one on technical architecture, one playing devil's advocate.

From there Claude creates the team, spins up teammates for each role, gives them their assignments through a shared task list, and lets them get to work. You'll see the lead's terminal listing all active teammates and what they're working on.

The key to a good first prompt is giving the lead enough to work with. Be specific about what each teammate should focus on and make sure their roles don't overlap too much. If the tasks are too vague, the lead has to figure out the structure on its own, which eats into your tokens and usually produces a less focused result.

You can also tell it exactly how many teammates you want and which model to use:

> Create a team with 4 teammates to refactor these modules in parallel. Use Sonnet for each teammate.

Once the team is running, you have two display modes to choose from. The default is in-process mode where all teammates run inside your main terminal and you use Shift+Up/Down to cycle between them. If you want to see everyone's output at once, split-pane mode gives each teammate their own pane, but it requires tmux or iTerm2.

## How to control your team once it's running

Once your team is live, there are a few things you'll want to know how to do right away.

First, you can talk to any teammate directly. You don't have to go through the lead. In in-process mode, hit Shift+Up or Shift+Down to select a teammate and just start typing. In split-pane mode, click into their pane and interact with them like any normal Claude Code session.

Second, there's something called delegate mode and it solves a common problem. Sometimes the lead decides to start doing the work itself instead of waiting for teammates to finish. Delegate mode locks the lead into coordination-only, so it can only spawn teammates, assign tasks, send messages, and manage the task list. Press Shift+Tab to toggle it on once your team is running.

Third, tasks can be assigned by the lead or self-claimed by teammates. When a teammate finishes their current task, they can automatically pick up the next unassigned one from the shared list. If you want more control, just tell the lead which task goes to which teammate.

And fourth, when a teammate is done with their work, you can ask the lead to shut them down. The lead sends a shutdown request, the teammate confirms, and they exit gracefully. When the whole team is finished, tell the lead to clean up and it will remove all shared team resources. Just make sure all teammates are shut down first before you run cleanup.

## Best practices so you don't waste tokens figuring this out yourself

Agent teams burn through tokens fast because every teammate is its own Claude Code session running in parallel. A few things will save you a lot of money and frustration.

Give your teammates detailed spawn prompts. They load project context automatically from your CLAUDE.md and MCP servers, but they don't inherit the lead's conversation history. So if there's specific context they need to do their job well, put it in the prompt when the lead spawns them. The more specific you are upfront, the less back-and-forth they need.

Size your tasks properly. Too small and the coordination overhead costs more than the benefit. Too large and teammates work too long without check-ins, which increases the risk of wasted effort. The sweet spot is self-contained units that produce a clear deliverable like a function, a test file, or a review.

Keep each teammate working on different files. Two teammates editing the same file leads to overwrites and that's a headache you don't need. Break the work so each one owns their own set of files.

If you're new to agent teams, start with research and review tasks before jumping into parallel implementation. Have teammates review a PR from different angles, or investigate a bug with competing theories. These tasks show you the value of parallel work without the coordination complexity of building code simultaneously.

And check in on your team regularly. Letting them run unattended for too long increases the chance of wasted effort, especially if one teammate goes down a path that isn't productive.

## What doesn't work yet (so you don't blame the tool)

This is an experimental feature and there are some rough edges you should know about before you start relying on it.

Session resumption doesn't work with in-process teammates. If you use /resume or /rewind, your teammates won't come back. The lead might try to message them but they won't exist anymore. If this happens, just tell the lead to spawn new ones.

Task status can lag. Sometimes a teammate finishes their work but doesn't mark the task as completed, which blocks any tasks that depend on it. If something looks stuck, check whether the work is actually done and either update the status manually or tell the lead to nudge the teammate.

You can only run one team per session and teammates can't spawn their own teams. The session that creates the team stays the lead for its entire lifetime, so there's no promoting a teammate or transferring leadership mid-session.

Split-pane mode only works with tmux or iTerm2. It's not supported in VS Code's integrated terminal, Windows Terminal, or Ghostty. The default in-process mode works everywhere though.

None of these are dealbreakers, but knowing about them upfront means you won't waste time troubleshooting something that's just a current limitation of the preview.

## This is just the beginning and it's only going to get better

Agent teams are in research preview, which means Anthropic is actively developing this and what you see today is the baseline, not the ceiling. As they iron out the rough edges around session resumption, task coordination, and shutdown behavior, this is going to become a standard part of how people work with Claude Code.

The people who install this early and start building muscle memory with it now are going to have a serious edge when it moves out of preview and becomes a default feature.

If you want to stay on top of stuff like this as it drops, I break down the workflows, tools, and implementation methods I'm actually using in production every week inside The AI Operator's Playbook. You also get 15 production-ready n8n workflows and 6 implementation playbooks from 8 years of building automations when you join.

👉 https://learnn8nautomation.com/newsletter

---

**Engagement Metrics**

- Replies: 56
- Reposts: 473
- Likes: 3.7K
- Bookmarks: 10.3K
- Views: 1.1M
- Posted: 6:22 AM · Feb 6, 2026