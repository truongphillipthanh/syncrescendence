---
url: https://x.com/YJstacked/status/2020396417542463546
author: YJ (@YJstacked)
captured_date: 2026-02-13
---

# How to Build a One Person Company with Multi-Agent Swarms (Claude Code)

(Description: A dark sci-fi illustration depicting a central commanding figure with glowing orange/red geometric patterns and energy, surrounded by a futuristic cityscape with multiple human figures in collaborative poses. The word "Claude" appears in the upper right corner. Lightning and dynamic energy elements frame the composition, suggesting coordination and power.)

## Overview

One Claude session codes while another debugs and a third writes tests. They message each other directly, share a task list, and coordinate without you orchestrating every move.

This isn't theoretical. Agent Teams is an experimental Claude Code feature that fundamentally changes how you build software with AI. Here's the complete setup guide and the patterns that actually work.

Before we start, if you want to work with us and automate business operations, head over to: https://tally.so/r/mZbV0a

## What Agent Teams Actually Do

Agent Teams lets you coordinate multiple Claude Code instances working together on the same codebase. One session acts as the **team lead**, coordinating work and synthesizing results. **Teammates** work independently, each in its own context window, and communicate directly with each other.

### The Key Difference from Subagents: Communication Architecture

Subagents run within a single session and can only report results back to the main agent. That's it. They can't message each other, share discoveries mid-task, or coordinate without the main agent acting as intermediary.

Agent Teams gives you:

- **Direct peer-to-peer messaging** between teammates
- **Shared task list** with dependencies and blocking
- **Independent context windows** for each teammate
- **File locking** to prevent race conditions
- **Self-claiming tasks** when teammates finish work

Think of it this way: subagents are contractors you send on errands. Agent Teams is a project team sitting in the same room, each working on their piece while staying in sync through conversation.

## System Requirements & Setup

### Step 1: Enable the Feature

Agent Teams is **experimental and disabled by default**. Enable it by adding the environment variable to your settings or shell:

**Option A: Add to settings.json**

- Navigate to `~/.claude/`
- Open or create `settings.json`
- Add:
```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

**Option B: Export in your shell**
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

Add this to your `.bashrc`, `.zshrc`, or equivalent to persist across sessions.

### Step 2: Install Split Pane Support (Optional)

For **visual multi-agent coordination**, install a terminal multiplexer:

**macOS/Linux (tmux):**
```bash
brew install tmux
```

**macOS (iTerm2):**
Download from [iterm2.com](https://iterm2.com/). Claude Code will auto-detect and use iTerm2's split pane API.

**Note:** Split panes are optional. Agent Teams works without them, but you won't see teammates working simultaneously in separate panes.

### Step 3: Verify Access

Start Claude Code and ask: "Do you have access to agent teams?"

**Expected response:** Confirmation that agent teams are available and you can create teams.

**If you see "not available" or similar:** Double-check your environment variable is set correctly and restart your terminal.

## How Agent Teams Works Under the Hood

### File System Architecture

Claude Code manages team state and task coordination internally. Teams and tasks are stored in `~/.claude/teams/` and `~/.claude/tasks/` directories respectively.

**Implementation note:** The exact internal file structure (how tasks are represented, messaging mechanisms, state storage) should be treated as implementation details rather than stable public APIs. Interact with teams through Claude Code's interface and commands rather than directly manipulating files.

### The Coordination Flow

1. **Team Lead** receives your prompt and creates a task list with dependencies
2. **Teammates** are spawned with specialized prompts
3. **Each teammate** automatically claims the next unassigned, unblocked task
4. **During work:** Teammates send findings to team lead via inbox; teammates message each other directly to coordinate; tasks automatically unblock when dependencies complete
5. **File locking** prevents multiple teammates from claiming the same task
6. **Session persists** until you manually shut down teammates

### Task Claiming System

Tasks include dependencies and blocking to prevent teammates from working on the same thing. When a teammate finishes work, it automatically picks up the next available task that isn't blocked by dependencies or already claimed by another teammate.

**Task states:**

- `pending`: Not started, waiting for dependencies
- `in_progress`: Currently being worked on
- `completed`: Finished and verified
- `blocked_by`: Array of task IDs that must complete first

**Note:** The exact coordination mechanism (how Claude Code prevents race conditions when claiming tasks) is handled internally by the system. Teams coordinate through the shared task system and avoid overlapping work.

## The Use Cases That Actually Work

Agent Teams adds **significant coordination overhead** and uses **substantially more tokens** when running multiple teammates in parallel.

**Only use Agent Teams when parallel exploration adds real value.**

### ✅ Strong Use Cases

#### 1. Research and Review with Competing Perspectives

Multiple teammates investigate different aspects of a problem simultaneously, then share and challenge each other's findings.

**Example prompt:**
> Users report the app exits after one message instead of staying connected. Spawn 5 agent teammates to investigate different hypotheses. Have them talk to each other to try to disprove each other's theories, like a scientific debate. Update the findings doc with whatever consensus emerges.

**Why this works:** Sequential investigation suffers from anchoring bias. Once one theory is explored, subsequent investigation is biased toward it. With multiple independent investigators actively trying to disprove each other, the theory that survives is much more likely to be the actual root cause.

#### 2. Multi-Module Feature Development

Teammates each own a separate piece without stepping on each other.

**Example prompt:**
> Create a new payment integration feature. Spawn three teammates: - One for the API layer (routes, controllers, validation) - One for database migrations and models - One for comprehensive test coverage. Have them coordinate through the shared task list and ensure changes stay compatible.

**Why this works:** Each teammate operates in its own context window, focused on one layer. No context pollution from frontend concerns bleeding into backend logic or vice versa.

#### 3. Debugging with Competing Hypotheses

Teammates test different theories in parallel and converge on the answer faster.

**Example prompt:**
> Performance regression in the search endpoint. Spawn four teammates to investigate: - Database query performance (indexes, N+1 queries) - Caching layer issues - Network latency and timeouts - Memory leaks in the response serializer. Have them share findings and converge on root cause.

**Why this works:** Parallel hypothesis testing is dramatically faster than sequential debugging. Teammates can rule out dead ends simultaneously instead of one at a time.

#### 4. Cross-Layer Coordination

Changes that span frontend, backend, and tests, each owned by a different teammate.

**Example prompt:**
> Refactor the authentication flow to use OAuth2. Spawn three teammates: - Frontend developer: Update login UI, token storage, redirect flows - Backend developer: Implement OAuth provider, token validation, refresh logic - Test engineer: E2E tests, integration tests, security tests. Coordinate via shared task list to ensure contract compatibility.

**Why this works:** Each teammate specializes in one layer but coordinates on contracts (API shape, response formats, error codes) through messaging.

### ❌ Weak Use Cases (Use Single Session Instead)

- **Sequential tasks with many dependencies:** The coordination overhead outweighs the benefits. Use a single session with step-by-step execution.
- **Same-file edits from multiple teammates:** Merge conflicts and file locking issues. Keep related edits in one session.
- **Simple, focused tasks:** Spinning up a team for "fix this typo" or "add a log statement" wastes tokens on coordination that provides zero value.

## Actually Using Agent Teams

### Basic Workflow

**1. Start Claude Code**
```bash
claude
```

**2. Create a team with a clear prompt**

> Create a team to refactor the payment module. Spawn three teammates: - API layer specialist: Refactor routes, controllers, request validation - Database specialist: Update schema, migrations, query optimization - Test specialist: Update all tests, add edge case coverage. Have them coordinate through the shared task list and message each other to ensure changes are compatible.

**3. Claude creates the team structure**

The team lead will:
- Create a task list with dependencies
- Spawn the three teammates with specialized prompts
- Initialize their inboxes for communication

**4. Monitor progress**

In **standard mode (single pane):**
- Press `Shift + Up/Down` to switch between team members
- View what each agent is currently doing
- Read messages in each agent's inbox

In **split pane mode (tmux/iTerm2):**
- Multiple panes show different agents working simultaneously
- Watch real-time coordination and messaging

**5. Interact with teammates directly**

You can message specific agents without going through the team lead:
```
# Switch to a specific teammate
[Press Shift+Down until you're viewing the right agent]
# Send a message
"Focus on edge cases for null values in the payment amount field"
```

**6. Shutdown when complete**
```
# The lead sends shutdown requests to all teammates
"Shutdown all teammates"
# Teammates can approve or reject with an explanation
# Once all teammates are shut down:
"Clean up team resources"
```

**CRITICAL:** Always use the team lead to clean up. Teammates should not run cleanup because their team context may not resolve correctly, potentially leaving resources in an inconsistent state.

## Advanced Patterns

### Writing Effective Team Prompts

**Bad prompt:**
> "Create a team to work on the codebase"

**Why it fails:** No specialization, no task breakdown, no coordination strategy.

**Good prompt:**
> Create a team to investigate and fix the memory leak in the API server. Spawn four teammates: 1. Profiler: Run memory profiling tools, identify allocation hotspots, document baseline vs under-load measurements. 2. Code reviewer: Audit recent changes to connection pooling, caching, and request handlers for resource cleanup issues. 3. Test writer: Create reproduction tests that trigger the leak, verify the fix, ensure cleanup on error paths. 4. Monitor: Review production metrics, identify patterns in when the leak manifests, correlate with deployment timeline. Have them share findings via inbox and converge on root cause and fix.

**Why it works:**
- Clear specialization for each teammate
- Specific tasks, not vague responsibilities
- Coordination mechanism defined (inbox messaging)
- Outcome-focused (converge on root cause and fix)

### Naming Conventions

**Good teammate names:**
- `security-reviewer`
- `oauth-implementer`
- `test-writer`
- `performance-profiler`

**Bad teammate names:**
- `worker-1`
- `agent-2`
- `helper`

**Why it matters:** Descriptive names make inbox messages and task assignments self-documenting. When you review the team's work, you immediately know who did what.

### Task Dependencies

The team lead should structure tasks with explicit dependencies:
```json
{ "taskId": "1", "description": "Design OAuth2 token validation interface", "status": "completed", "owner": "architect" }
{ "taskId": "2", "description": "Implement token validation", "status": "in_progress", "owner": "backend-dev", "blockedBy": ["1"] }
{ "taskId": "3", "description": "Write integration tests for auth flow", "status": "pending", "owner": null, "blockedBy": ["2"] }
```

When task 2 completes, task 3 automatically unblocks and can be claimed by the next available teammate.

### Reviewing Team Work

Agent Teams coordinates communication between teammates automatically. You can monitor progress by:

**Switching between teammates:**
Press `Shift+Up/Down` to cycle through team members in in-process mode, or click into their panes in split-pane mode.

**Viewing task progress:**
Ask Claude for a status update on the team's current work and task completion.

**Checking team state:**
The team configuration is stored in `~/.claude/teams/{team-name}/config.json` and tasks in `~/.claude/tasks/{team-name}/`.

## Context and Memory Management

### What Teammates Inherit

Teammates automatically load:
- Project context from `CLAUDE.md`
- MCP servers configured in the project
- Skills available in the project

### What Teammates Do NOT Inherit

- The team lead's conversation history
- Other teammates' conversation history
- Prior context from unrelated sessions

**Why this matters:** Include task-specific details in the spawn prompt. Don't assume teammates know what you discussed with the team lead 10 messages ago.

### Auto-Memory Feature

Claude Code supports persistent memory for agents through:
- **Project memory** via `CLAUDE.md` files in project directories
- **Agent-specific memory** stored in `~/.claude/agent-memory/<agent>/` for subagents
- **Memory tools** accessed via `/memory` commands

**Best practices:**
- Use `CLAUDE.md` to provide project context that persists across sessions
- Agent memory is most relevant for subagents rather than Agent Teams
- Regularly review and update project documentation

**To manage memory:**
Use the `/memory` command in Claude Code for memory-related operations.

## Known Limitations

Agent Teams is **experimental** and has documented limitations:

### 1. No Session Resumption

Once you exit Claude Code, the team state is lost. You can't "resume" a team from a previous session.

**Workaround:** Complete team work in a single session, or extract results to persistent files before shutting down.

### 2. No Nested Teams

Teammates cannot spawn their own sub-teams. The architecture is two-level only: one team lead, multiple teammates.

**Workaround:** Use subagents within a single teammate if you need deeper hierarchy.

### 3. Shutdown Coordination

The team lead sends shutdown requests, but teammates can reject them with an explanation (e.g., "I'm in the middle of a critical database migration").

**Best practice:** Always confirm teammates are idle before initiating shutdown.

### 4. Token Cost

Agent Teams uses significantly more tokens than single sessions. Each teammate runs in its own context window, so a multi-teammate team will consume proportionally more tokens.

**Mitigation:** Only use Agent Teams for tasks where parallel exploration genuinely adds value. For sequential work, use a single session.

## Cost and Performance Considerations

### Token Usage Reality Check

- **Single session:** ~50K tokens for a complex refactoring task
- **5-person Agent Team:** Significantly more tokens (roughly proportional to number of active teammates)

**When it's worth it:**
- The task genuinely parallelizes (4 independent modules)
- Coordination overhead is minimal
- The time savings justify the cost

**When it's not:**
- Sequential dependencies mean teammates wait on each other
- Same-file edits create merge conflicts
- A single focused session could complete it faster

## Split Pane Display Modes

Claude Code supports two display modes for teammates:

### 1. In-Process (Default)

All teammates run in your main terminal. Use `Shift+Up/Down` to switch between team members and type to message them directly.

**Characteristics:**
- Works in any terminal
- No extra setup required
- All teammates run in background
- Best for headless environments or when you don't need visual panes

### 2. Split Panes (tmux or iTerm2)

Each teammate gets its own visible pane. You can see everyone working simultaneously and click into a pane to interact directly.

**Configuration:**

Add to your `settings.json`:
```json
{ "teammateMode": "tmux" }
```

**Options:**
- `"auto"` (default): May use split panes if already inside a tmux session
- `"tmux"`: Enables split-pane mode
- `"in-process"`: Forces in-process mode even if tmux is available

**Requirements:**
- tmux installed (`brew install tmux`), or
- iTerm2 on macOS (which may provide enhanced support)

**Tmux notes:**
- Known limitations on certain operating systems
- Works best on macOS
- Using `tmux -CC` in iTerm2 is the recommended setup

**Tmux commands:**
```bash
# List all panes in current window
tmux list-panes

# Switch to pane by number
tmux select-pane -t 1

# Kill a specific pane
tmux kill-pane -t %5

# Rebalance pane layout
tmux select-layout tiled
```

## Real-World Example: Building a C Compiler

Anthropic published a case study of using a custom agent harness (not Agent Teams directly, but a similar parallel agent approach) to build a C compiler from scratch.

### Project Scope

- 16 parallel Claude agents
- Nearly 2,000 Claude Code sessions over two weeks
- 2 billion input tokens, 140 million output tokens
- Total cost: just under $20,000
- Result: 100,000-line Rust-based C compiler

### What It Could Compile

- Linux 6.9 kernel (x86, ARM, RISC-V)
- QEMU, FFmpeg, SQLite, postgres, redis
- 99% pass rate on GCC torture test suite
- Could compile and run Doom

### Agent Specialization

- Some agents focused on implementing compiler features
- One agent consolidated duplicate code
- Another improved compiler performance
- A third optimized generated assembly output
- One agent maintained documentation
- Another critiqued design from a Rust developer perspective

### Key Insights

- **Parallelization enabled speed:** Multiple agents debugging different hypotheses simultaneously was dramatically faster than sequential debugging.
- **Specialization maintained quality:** Dedicated agents for specific concerns (documentation, code quality, performance) prevented the "we'll do it later" problem.
- **Autonomous coordination:** Agents used shared progress documents and task lists to coordinate without a central orchestrator.
- **Testing was critical:** High-quality test suites were essential for autonomous progress without human oversight.

### Limitations Hit

- New features frequently broke existing functionality near the end
- Some advanced features (like 16-bit x86 code generation within size limits) remained beyond Opus 4.6's capabilities
- Generated code quality was reasonable but not expert-level

**Source:** [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler) - Anthropic Engineering blog

**Note:** This project used a custom harness, not the built-in Agent Teams feature, but demonstrates the potential of coordinated parallel agents.

## Hooks for Quality Control

Claude Code supports **hook events** that trigger when specific team actions occur:

### TeammateIdle Hook

Runs when a teammate is about to go idle (no more tasks available).

**Use case:** Provide feedback or additional tasks to keep the teammate working.

### TaskCompleted Hook

Runs when a task is being marked complete.

**Use case:** Validate work meets quality standards before accepting completion.

**Note:** Consult the Claude Code hooks documentation for specific implementation details and exit code behavior.

## Debugging Agent Teams

### Common Issues

#### 1. Teammates not spawning

**Symptom:** Team lead acknowledges the request but no teammates appear.

**Check:**
- Environment variable is set: `echo $CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`
- Restart terminal after setting the variable
- Verify Claude Code version supports Agent Teams

#### 2. Merge conflicts from simultaneous edits

**Symptom:** Multiple teammates edited the same file, causing conflicts.

**Solution:** Structure tasks so teammates work on separate files. Use task dependencies to serialize same-file edits.

#### 3. Teammates stuck waiting

**Symptom:** Teammates idle because all available tasks are blocked.

**Check:**
- Review task dependencies: `cat ~/.claude/teams/{team}/tasks/*.json`
- Unblock tasks manually if dependencies are incorrectly specified
- Have team lead restructure task list if needed

#### 4. High token usage

**Symptom:** Costs exceed expectations.

**Solution:**
- Reduce number of teammates if work isn't genuinely parallel
- Use lower Opus 4.6 effort level for routine tasks
- Switch to single session for sequential work

## Migration Guide: From Subagents to Agent Teams

### When to Migrate

**Stick with subagents if:**
- Task is simple and focused
- All work happens in one context
- No need for peer-to-peer coordination

**Migrate to Agent Teams if:**
- Subagents need to share findings mid-task
- Multiple pieces can be worked independently
- You're manually orchestrating coordination between subagents

### Example Migration

**Old subagent pattern:**
> Create a subagent to research OAuth2 best practices. [Wait for subagent to finish] Create another subagent to implement the auth flow. [Wait for subagent to finish] Create a third subagent to write tests.

**Problem:** Sequential. No parallelization. Main agent acts as intermediary for all coordination.

**New Agent Teams pattern:**
> Create a team for OAuth2 implementation. Spawn three teammates: - Researcher: Investigate OAuth2 best practices, security considerations - Implementer: Build the auth flow based on research findings - Test writer: Create comprehensive test coverage. Have researcher share findings with implementer via messaging. Implementer should ask questions directly to researcher as needed. Test writer should coordinate with implementer on test scenarios.

**Benefits:** Parallel research and planning. Direct communication. Tester can start edge case tests while implementer finishes core logic.

## The Bottom Line

Agent Teams is **not a replacement for single-session Claude Code**. It's a specialized tool for specific use cases where parallel work genuinely adds value.

### Use Agent Teams When

- Multiple independent pieces can be worked simultaneously
- Teammates need to challenge each other's assumptions (research, debugging)
- Cross-layer coordination requires specialists (frontend, backend, tests)
- The coordination overhead and 5x token cost is justified by time savings

### Use a Single Session When

- Work is sequential with many dependencies
- Same file needs multiple edits
- Task is simple and focused
- You're not sure if parallelization helps (start single, scale to teams if needed)

Agent Teams changes the economics of AI-assisted development. Tasks that would take days of sequential work now compress into hours of parallel execution.

The constraint isn't Claude's capabilities anymore. It's your ability to decompose problems into structures that coordinated agents can execute.

### Start Experimenting
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
claude
```

Then ask: "Create a team to [your complex task]. Spawn teammates for [specialist 1], [specialist 2], [specialist 3]. Have them coordinate via messaging and shared task list."

The architecture for coordinated AI agent systems is here. Use it. If you want this set up (DFY) - https://tally.so/r/mZbV0a