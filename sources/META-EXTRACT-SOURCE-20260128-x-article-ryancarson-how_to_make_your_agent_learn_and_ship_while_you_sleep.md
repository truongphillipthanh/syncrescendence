# Extraction: SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep

**Source**: `SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep.md`
**Atoms extracted**: 17
**Categories**: claim, framework, praxis_hook

---

## Claim (2)

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0007
**Lines**: 74-74
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> The `AGENTS.md` files function as a dynamic knowledge base that is automatically updated and expanded nightly by the AI agent's review process.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0015
**Lines**: 242-247
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> An agent's `AGENTS.md` files can serve as institutional memory, allowing the agent to become an expert in a codebase by incorporating learned patterns and avoiding past issues.

## Framework (3)

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0002
**Lines**: 17-26
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> An autonomous AI agent system can be built using three open-source projects: Compound Engineering Plugin (for extracting and persisting learnings), Compound Product (for automation, turning reports into PRs), and Ralph (an autonomous agent loop for continuous task execution).

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0004
**Lines**: 34-44
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> An autonomous AI agent system can operate with a two-part nightly loop: a 'Compound Review' job (e.g., 10:30 PM) to extract learnings and update knowledge bases, followed by an 'Auto-Compound' job (e.g., 11:00 PM) to implement prioritized tasks and create pull requests, leveraging the fresh learnings.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0014
**Lines**: 233-240
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> A self-improving agent workflow can involve a nightly cycle where the agent first reviews daily threads, updates its knowledge base (e.g., `AGENTS.md`), pushes changes, then pulls the updated context, implements a top priority, and opens a pull request.

## Praxis Hook (12)

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0001
**Lines**: 7-10
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.60

> To enable an AI agent to learn and ship autonomously, set up a nightly loop where the agent reviews daily work, extracts lessons, updates its instructions, and then picks up the next feature from a backlog.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0003
**Lines**: 28-30
**Context**: method / limitation
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When using Claude Code instead of Amp for an autonomous agent workflow, replace `amp execute` with `claude -p "..." --dangerously-skip-permissions` and update references to `AGENTS.md` to `CLAUDE.md`.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0005
**Lines**: 48-62
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To set up the 'Compound Review' script for an AI agent, create a shell script that navigates to the project directory, ensures the main branch is up to date, and then executes an `amp execute` command (or equivalent for Claude Code) to instruct the agent to review threads from the last 24 hours, extract key learnings from any threads where the Compound Engineering skill was not used, update relevant `AGENTS.md` files, and then commit and push these changes to main.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0006
**Lines**: 64-66
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Make the `daily-compound-review.sh` script executable using `chmod +x scripts/daily-compound-review.sh`.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0008
**Lines**: 79-108
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To set up the 'Auto-Compound' script for an AI agent, create a shell script that sources environment variables, fetches the latest main branch (including `AGENTS.md` updates), identifies the top priority item from reports, creates a new feature branch, generates a Product Requirements Document (PRD) for the priority item, converts the PRD into tasks, runs an iterative execution loop for these tasks, and finally pushes the branch and creates a draft pull request.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0009
**Lines**: 112-112
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> On macOS, use `launchd` instead of `cron` for scheduling AI agent tasks, as it is native and handles edge cases better.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0010
**Lines**: 115-142
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To schedule the 'Compound Review' script at 10:30 PM on macOS, create a `launchd` plist file (`com.yourproject.daily-compound-review.plist`) in `~/Library/LaunchAgents/` specifying the script path, working directory, `StartCalendarInterval` for 22:30, and paths for standard output/error logs and environment variables.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0011
**Lines**: 145-172
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To schedule the 'Auto-Compound' script at 11:00 PM on macOS, create a `launchd` plist file (`com.yourproject.auto-compound.plist`) in `~/Library/LaunchAgents/` specifying the script path, working directory, `StartCalendarInterval` for 23:00, and paths for standard output/error logs and environment variables.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0012
**Lines**: 174-176
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Load `launchd` plist files using `launchctl load ~/Library/LaunchAgents/com.yourproject.daily-compound-review.plist` and `launchctl load ~/Library/LaunchAgents/com.yourproject.auto-compound.plist`.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0013
**Lines**: 200-229
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> To ensure automated tasks run on a Mac, use `caffeinate` via a `launchd` plist to keep the machine awake during the automation window. For example, a plist can be configured to run `caffeinate -i -t 32400` (keeping the Mac awake for 9 hours) starting at 5 PM.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0016
**Lines**: 250-260
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> To debug `launchd` jobs, check scheduled jobs with `launchctl list | grep yourproject`, view logs using `tail -f` on the specified log files, and manually test jobs with `launchctl start com.yourproject.jobname`.

### ATOM-SOURCE-20260128-x-article-ryancarson-how_to_make_your_agent_learn_and_ship_while_you_sleep-0017
**Lines**: 264-270
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.40, actionability=0.80, epistemic_stability=0.60

> To extend an automated agent system, consider adding Slack notifications for PR creation or job failures, implementing multiple priority tracks for different reports, enabling automatic PR merging for small changes with passing CI, or having the agent generate weekly summaries/changelogs.
