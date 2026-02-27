# The Cloud Agent Thesis

(Description: Abstract digital visualization with flowing cyan and white wireframe patterns, network-like structures, and geometric shapes against a dark background. A small silhouette figure stands on a reflective horizon with radiating light streams above.)

Most AI coding tools run on your laptop. You open an IDE, the AI reads your files, suggests edits, and you approve them in real time. This is useful. It is also a local maximum.

The endgame is agents that run in the cloud, work asynchronously, and are accessible to your entire team from wherever they already work - Slack, Jira, Linear, a web app, an API, a CLI. Not a copilot sitting in one developer's editor, a teammate sitting on the network.

A senior engineer starts a session from the CLI. A PM tags the agent in Slack. A junior dev kicks off a migration from a Jira ticket. A designer reports a bug and a fix is in review by lunch. Different people, different roles, different entry points - all pushing changes to the same codebase, most without setting up a local environment or even learning Git.

I've been thinking about this since joining Cognition and watching how the team actually uses Devin internally. The patterns that emerged are less about "AI-assisted coding" and more about what happens when an engineering org has access to an agent that anyone can talk to, that works across every codebase, and that doesn't need a local environment to function.

Here's the thesis: cloud agents are a different category from local agents, and the differences compound.

## What a cloud agent actually is

A cloud agent runs on remote infrastructure. It has its own shell, its own IDE, its own browser. It connects to your repos, your CI, your deployment pipeline. You communicate with it the same way you'd communicate with a remote engineer: you send it a message, it does the work, you review the output.

The local agent model - Cursor, Windsurf, Claude Code in your terminal - is a human and an AI sharing a single environment. You're pair programming. The cloud agent model is delegation. You describe the task, the agent executes it independently, and you get back a PR.

These are not competing approaches. They're complementary. The cloud agent pattern doesn't replace the local one - it opens the codebase to everyone else. And it has properties that the local pattern can't replicate, properties that matter more as you scale.

## The properties that matter

### Anyone can use it

At Cognition, non-engineers tag @Devin in Slack to fix documentation, report bugs, or request small features. They don't need Git installed. They don't need a local dev environment. They don't need to know what a branch is.

The bottleneck on most codebases isn't writing code, it's the friction of getting a change made. Someone notices a typo in the docs, but filing a ticket feels like overkill, and they don't have the tooling to fix it themselves. So it stays broken. Multiply this across every person in the company who interacts with the product but doesn't write code - PMs, designers, support, marketing, ops - and you get a permanent drag on quality.

A cloud agent accessible from Slack (or anywhere) eliminates that drag. You tag the agent, describe the fix, and move on. The PR shows up. Someone reviews it. Done.

### It works across codebases

A local agent knows about the repo you have open. A cloud agent can be configured against every repo in the org. You can ask it questions about any codebase, kick off tasks in any of them, and it handles the context switching.

This changes the topology of who can contribute to what. An engineer on Team A can send a quick fix to Team B's repo without cloning it, setting up the environment, or context-switching out of their current work. The organizational boundary around a codebase softens.

### Async by default

When you use a local agent, you're synchronous. You're watching it work, approving edits, steering. This is the right mode for architectural decisions, complex debugging, ambiguous requirements - work where your judgment is the bottleneck.

But a huge category of engineering work doesn't need real-time human steering. Targeted refactors, lint fixes, CVE remediation, test coverage, dependency upgrades, documentation, migrations. The bottleneck on this work isn't figuring out what to do - it's finding the time to do it.

Cloud agents turn this backlog into parallel workstreams. You describe ten tasks, kick off ten sessions, and come back to ten PRs. The constraint shifts from engineer hours to review capacity.

### It compounds at org scale

A local agent makes one developer faster. A cloud agent, once configured and taught your conventions, makes the entire org faster. When someone figures out how to get the agent to handle a particular class of task - say, remediating security vulnerabilities from Sonarqube - they write a Playbook. Now anyone in the company can trigger that same workflow. Expertise gets encoded once and executed repeatedly.

This is the real unlock at enterprise scale. You're not buying seats for individual developers. You're deploying capacity that the whole engineering org draws from, with governance, analytics, and permissions layered on top. The cloud agent becomes infrastructure, not a tool.

## Code Reviews

As you generate more PRs, the bottleneck moves from writing code to reviewing it.

Cloud agents make this problem worse and also make it solvable. Worse, because ten parallel agent sessions means ten PRs to review. Solvable, because the same cloud infrastructure that runs the coding agent can run a review agent - one that organizes diffs logically, detects code movement, catches bugs automatically, and lets you ask questions about the change with full codebase context.

This is not a nice-to-have. If you're running agents at scale and you don't have automated review, you're either rubber-stamping PRs or drowning in review debt. The cloud agent pattern demands a review agent as a corollary.

## Integration surface

A local agent integrates with your filesystem and your terminal. A cloud agent integrates with everything your team uses:

**Slack and Teams** for kicking off tasks and getting updates.

**Jira and Linear** for pulling context from tickets and automatically scoping work.

**GitHub, GitLab, Bitbucket** for PRs and code review.

**Sentry, Datadog, Vercel** for pulling logs and debugging production issues.

**Data warehouses** for querying metrics without pulling an engineer off their work.

Each integration is a new surface area where the agent can be useful. And because the agent runs in the cloud, adding these integrations doesn't require anything from individual developers. It's configured once at the org level.

MCP makes this extensible. Connect a Sentry MCP, and the agent can dig through error logs. Connect a database MCP, and anyone on the team can ask data questions in Slack and get answers with the SQL included so they can validate the logic. The agent becomes a general-purpose interface to your engineering infrastructure.

## What this means for pricing

Local agents are priced per seat because they're tools for individuals. Cloud agents are priced on usage because they're capacity for the org.

Usage-based pricing aligns incentives correctly. As teams use the agent more and get more value, they pay more. This is why you see 5-10x contract expansions mid-year at companies running cloud agents - not at renewal, but proactively as they roll out to more teams and discover more use cases.

The seat model breaks down when the agent isn't tied to a single developer's workflow. Who owns the seat when a PM tags the agent in Slack? When a ticket in Linear triggers an automated session? When a CI failure spawns a debugging agent? The unit of value isn't the person - it's the work done.

## Where cloud agents are strong

The tasks where cloud agents consistently deliver are the ones that are quick to verify and well-scoped:

- Targeted refactors
- Bug fixes with clear reproduction steps
- Test coverage for existing code
- CVE and lint remediation
- Dependency and framework migrations
- Documentation maintenance
- Investigating CI failures
- PR review

The rule of thumb: if a junior engineer could handle it with clear instructions, a cloud agent can handle it. This isn't a ceiling — it's a current snapshot that moves upward with every model improvement.

## Where they're weak

Large tasks with unclear scope need to be decomposed into smaller sessions. Visual design judgment isn't there yet. Mobile testing is limited without a physical device. Anything that requires extensive manual validation needs verification mechanisms in place before you start.

## The org transformation piece

Deploying a cloud agent isn't a tool purchase. It's closer to hiring, because you're adding capacity to the org that needs to be onboarded, managed, and directed.

The companies pulling ahead are treating it that way. Strategic project selection to focus on high-ROI tasks. Knowledge and Playbooks to teach the agent conventions. Analytics to track adoption and measure impact. Permissions and governance for how different teams use the agent. Change management to shift engineering workflows.

The gap between "bought some AI tools" and "transformed how the engineering org works" is where the real divergence happens. Companies on the right side of that gap are reporting 5-6x faster migrations, 70-90% of security vulnerabilities handled automatically, every PR reviewed by an agent. Companies on the wrong side bought seats and are waiting for something to happen.

## The async spectrum

Think of AI coding as a spectrum from fully synchronous (you and the AI in an editor, keystroke by keystroke) to fully asynchronous (you describe the task and walk away).

Local agents own the left side. Cloud agents own the right side. Both matter. But the async side is where leverage multiplies - because one person can have many agents working in parallel, because non-engineers can participate, because the work happens independent of any developer's schedule.

The companies that own both sides of this spectrum - sync for the work that needs human judgment, async for everything else - will compound advantages that single-mode tools can't match.

## Cloud agents ≠ remote copilots

Cloud agents are not just local agents running on someone else's computer. The cloud runtime enables a different interaction model (async), a different access model (anyone on the team), a different integration model (your whole toolchain), and a different scaling model (org-wide capacity, not individual productivity).

Local agents make developers faster. Cloud agents make engineering orgs more capable. That's the thesis.

At @cognition, we built our entire platform around the cloud agent model from the start, and have been running cloud agents in production longer than anyone else.

Devin is accessible everywhere your team works - Slack, CLI, API, Linear, and Jira, and is already deployed at organizations like Goldman Sachs, Citi, Ramp, Cal.com, Exa, and Eight Sleep.

If you're ready to move your engineering org beyond local copilots, try Devin or reach out to see what org-scale deployment looks like.

---

**Engagement metrics:** 19 replies • 47 reposts • 339 likes • 632 bookmarks • 284.1K views  
**Posted:** February 8, 2026 at 10:26 AM