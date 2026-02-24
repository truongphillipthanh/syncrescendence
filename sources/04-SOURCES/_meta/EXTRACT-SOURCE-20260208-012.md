# Extraction: SOURCE-20260208-012

**Source**: `SOURCE-20260208-x-article-yjstacked-how_to_build_a_one_person_company_with_multi_agent_swarms_claude_code.md`
**Atoms extracted**: 69
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (29)

### ATOM-SOURCE-20260208-012-0006
**Lines**: 91-92
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> Claude Code manages team state and task coordination internally, storing teams in `~/.claude/teams/` and tasks in `~/.claude/tasks/`.

### ATOM-SOURCE-20260208-012-0010
**Lines**: 124-125
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.30, epistemic_stability=0.80

> Agent Teams introduce significant coordination overhead and use substantially more tokens due to running multiple teammates in parallel.

### ATOM-SOURCE-20260208-012-0012
**Lines**: 134-143
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Agent Teams are effective for research and review with competing perspectives because multiple teammates can investigate different hypotheses simultaneously and actively try to disprove each other, leading to a more robust understanding of the root cause.

### ATOM-SOURCE-20260208-012-0013
**Lines**: 145-152
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Agent Teams are suitable for multi-module feature development because each teammate can operate in its own context window, focusing on a specific layer (e.g., API, database, tests) without context pollution.

### ATOM-SOURCE-20260208-012-0015
**Lines**: 154-161
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Agent Teams accelerate debugging by allowing teammates to test different hypotheses in parallel, which is dramatically faster than sequential debugging as dead ends can be ruled out simultaneously.

### ATOM-SOURCE-20260208-012-0016
**Lines**: 163-170
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Agent Teams are effective for cross-layer coordination (e.g., frontend, backend, tests) because specialized teammates can coordinate on contracts (API shape, response formats, error codes) through messaging while working on their respective layers.

### ATOM-SOURCE-20260208-012-0018
**Lines**: 181-186
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> When a Claude Code team is created, the team lead automatically generates a task list with dependencies, spawns specialized teammates, and initializes their inboxes for communication.

### ATOM-SOURCE-20260208-012-0026
**Lines**: 283-286
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agent Team members automatically inherit project context from `CLAUDE.md`, configured MCP servers, and available project skills.

### ATOM-SOURCE-20260208-012-0027
**Lines**: 288-291
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agent Team members do not inherit the team lead's conversation history, other teammates' conversation history, or prior context from unrelated sessions.

### ATOM-SOURCE-20260208-012-0029
**Lines**: 297-302
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Claude Code supports persistent memory for agents through project memory via `CLAUDE.md` files, agent-specific memory in `~/.claude/agent-memory/<agent>/` for subagents, and memory tools accessed via `/memory` commands.

### ATOM-SOURCE-20260208-012-0031
**Lines**: 313-314
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agent Teams is an experimental feature with known limitations, including no session resumption, no nested teams, and potential shutdown coordination issues.

### ATOM-SOURCE-20260208-012-0035
**Lines**: 335-338
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agent Teams consume significantly more tokens than single sessions because each teammate runs in its own context window, leading to proportionally higher token usage for multi-teammate teams.

### ATOM-SOURCE-20260208-012-0039
**Lines**: 348-351
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agent Teams are cost-effective when tasks genuinely parallelize, coordination overhead is minimal, and time savings justify the increased token cost.

### ATOM-SOURCE-20260208-012-0040
**Lines**: 353-356
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agent Teams are not cost-effective when sequential dependencies cause teammates to wait, same-file edits create merge conflicts, or a single focused session could complete the task faster.

### ATOM-SOURCE-20260208-012-0041
**Lines**: 360-363
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Claude Code supports two display modes for Agent Teams: in-process (default), where all teammates run in the main terminal, and split panes (tmux or iTerm2), where each teammate gets its own visible pane.

### ATOM-SOURCE-20260208-012-0044
**Lines**: 384-386
**Context**: consensus / limitation
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.50, epistemic_stability=0.80

> The 'Split Panes' mode for Claude Code teammates works best on macOS and has known limitations on other operating systems.

### ATOM-SOURCE-20260208-012-0046
**Lines**: 403-408
**Context**: anecdote / evidence
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> Anthropic used 16 parallel Claude agents, nearly 2,000 Claude Code sessions over two weeks, 2 billion input tokens, and 140 million output tokens, costing just under $20,000, to build a 100,000-line Rust-based C compiler.

### ATOM-SOURCE-20260208-012-0047
**Lines**: 410-415
**Context**: anecdote / evidence
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> The C compiler built by Anthropic's parallel Claude agents could compile the Linux 6.9 kernel (x86, ARM, RISC-V), QEMU, FFmpeg, SQLite, postgres, redis, achieved a 99% pass rate on the GCC torture test suite, and could compile and run Doom.

### ATOM-SOURCE-20260208-012-0048
**Lines**: 417-425
**Context**: anecdote / evidence
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> In Anthropic's C compiler project, agents were specialized: some implemented features, one consolidated duplicate code, another improved performance, a third optimized assembly output, one maintained documentation, and another critiqued design from a Rust developer perspective.

### ATOM-SOURCE-20260208-012-0049
**Lines**: 429-430
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> Parallelization of agents enabled faster debugging by allowing multiple agents to test different hypotheses simultaneously.

### ATOM-SOURCE-20260208-012-0050
**Lines**: 431-432
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> Agent specialization for specific concerns like documentation, code quality, and performance helped maintain quality and prevented deferring these tasks.

### ATOM-SOURCE-20260208-012-0051
**Lines**: 433-434
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> Agents can coordinate autonomously using shared progress documents and task lists without a central orchestrator.

### ATOM-SOURCE-20260208-012-0052
**Lines**: 435-436
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> High-quality test suites are essential for autonomous agent progress without human oversight.

### ATOM-SOURCE-20260208-012-0053
**Lines**: 439-444
**Context**: anecdote / limitation
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> Limitations encountered in Anthropic's C compiler project included new features frequently breaking existing functionality near the end, advanced features like 16-bit x86 code generation remaining beyond Opus 4.6's capabilities, and generated code quality being reasonable but not expert-level.

### ATOM-SOURCE-20260208-012-0062
**Lines**: 512-515
**Context**: anecdote / limitation
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.50, epistemic_stability=0.80

> The old subagent pattern for OAuth2 implementation (research, then implement, then test) is sequential, lacks parallelization, and requires the main agent to act as an intermediary for all coordination.

### ATOM-SOURCE-20260208-012-0064
**Lines**: 526-528
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> Using Agent Teams for OAuth2 implementation allows for parallel research and planning, direct communication between agents, and enables testers to start edge case tests while the implementer finishes core logic.

### ATOM-SOURCE-20260208-012-0065
**Lines**: 531-532
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> Agent Teams is a specialized tool for use cases where parallel work genuinely adds value, not a replacement for single-session Claude Code.

### ATOM-SOURCE-20260208-012-0068
**Lines**: 547-548
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> Agent Teams changes the economics of AI-assisted development, compressing tasks that would take days of sequential work into hours of parallel execution.

### ATOM-SOURCE-20260208-012-0069
**Lines**: 550-551
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> The constraint in AI-assisted development is no longer Claude's capabilities, but the user's ability to decompose problems into structures that coordinated agents can execute.

## Concept (3)

### ATOM-SOURCE-20260208-012-0001
**Lines**: 17-20
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> Agent Teams is an experimental Claude Code feature that allows multiple Claude Code instances to coordinate on the same codebase, with a 'team lead' coordinating work and 'teammates' working independently in their own context windows and communicating directly.

### ATOM-SOURCE-20260208-012-0002
**Lines**: 30-40
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The key difference between Agent Teams and Subagents is their communication architecture: Agent Teams allow direct peer-to-peer messaging between teammates, a shared task list, independent context windows, file locking, and self-claiming tasks, whereas Subagents can only report results back to a main agent.

### ATOM-SOURCE-20260208-012-0054
**Lines**: 453-464
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=1.00

> Claude Code supports 'hook events' that trigger when specific team actions occur, such as `TeammateIdle` (when a teammate is about to go idle) and `TaskCompleted` (when a task is marked complete).

## Framework (6)

### ATOM-SOURCE-20260208-012-0008
**Lines**: 100-108
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The coordination flow for Agent Teams involves a Team Lead receiving a prompt and creating a task list, teammates being spawned with specialized prompts, each teammate claiming the next unassigned/unblocked task, teammates sending findings to the lead and messaging each other, file locking to prevent conflicts, and tasks unblocking as dependencies complete.

### ATOM-SOURCE-20260208-012-0009
**Lines**: 110-119
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Agent Teams' task claiming system uses dependencies and blocking to prevent teammates from working on the same task, with task states including `pending` (not started, waiting for dependencies), `in_progress` (currently being worked on), `completed` (finished and verified), and `blocked_by` (array of task IDs that must complete first).

### ATOM-SOURCE-20260208-012-0037
**Lines**: 344-366
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=1.00

> Claude Code offers two primary teammate modes: 'In-Process' (default, all teammates run in the main terminal) and 'Split Panes' (each teammate gets a visible pane, requiring tmux or iTerm2).

### ATOM-SOURCE-20260208-012-0061
**Lines**: 500-507
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=1.00

> Stick with subagents if a task is simple, focused, happens in one context, and doesn't require peer-to-peer coordination; migrate to Agent Teams if subagents need to share findings mid-task, multiple pieces can be worked independently, or manual coordination between subagents is occurring.

### ATOM-SOURCE-20260208-012-0066
**Lines**: 535-539
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=1.00

> Use Agent Teams when multiple independent pieces can be worked simultaneously, teammates need to challenge each other's assumptions, cross-layer coordination requires specialists, and the coordination overhead and 5x token cost are justified by time savings.

### ATOM-SOURCE-20260208-012-0067
**Lines**: 541-545
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=1.00

> Use a single session when work is sequential with many dependencies, the same file needs multiple edits, the task is simple and focused, or if unsure whether parallelization helps (start single, scale to teams if needed).

## Praxis Hook (31)

### ATOM-SOURCE-20260208-012-0003
**Lines**: 49-65
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> To enable Agent Teams in Claude Code, add the environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` set to `1` either in your `settings.json` file (located in `~/.claude/`) or by exporting it in your shell (e.g., `export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`).

### ATOM-SOURCE-20260208-012-0004
**Lines**: 67-76
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> To visually coordinate multi-agent activity in Claude Code, install a terminal multiplexer like `tmux` for macOS/Linux or use iTerm2 on macOS, which Claude Code can auto-detect.

### ATOM-SOURCE-20260208-012-0005
**Lines**: 80-86
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.80

> Verify Agent Teams access by starting Claude Code and asking, "Do you have access to agent teams?" An expected response confirms availability; otherwise, double-check environment variables and restart the terminal.

### ATOM-SOURCE-20260208-012-0007
**Lines**: 96-98
**Context**: method / limitation
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.80

> Interact with Claude Code teams through its interface and commands, rather than directly manipulating the internal file structure in `~/.claude/teams/` and `~/.claude/tasks/`, as these are implementation details and not stable public APIs.

### ATOM-SOURCE-20260208-012-0011
**Lines**: 127-130
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.80

> Only use Agent Teams when parallel exploration adds real value, such as for research and review with competing perspectives, multi-module feature development, debugging with competing hypotheses, or cross-layer coordination.

### ATOM-SOURCE-20260208-012-0014
**Lines**: 151-159
**Context**: method / limitation
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Avoid using Agent Teams for sequential tasks with many dependencies, same-file edits from multiple teammates, or simple, focused tasks like fixing a typo, as the coordination overhead outweighs the benefits or wastes tokens.

### ATOM-SOURCE-20260208-012-0017
**Lines**: 165-177
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To use Claude Code's Agent Teams, start Claude Code, then create a team with a clear prompt specifying the task, number of teammates, their specializations, and coordination mechanisms.

### ATOM-SOURCE-20260208-012-0019
**Lines**: 188-199
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Monitor Agent Team progress in standard mode by pressing `Shift + Up/Down` to switch between team members and view their actions and messages, or in split pane mode (tmux/iTerm2) to see multiple agents simultaneously.

### ATOM-SOURCE-20260208-012-0020
**Lines**: 201-207
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To interact with a specific Agent Team member, switch to their view (e.g., `Shift+Down`) and send a message directly.

### ATOM-SOURCE-20260208-012-0021
**Lines**: 209-218
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Always use the team lead to initiate shutdown and clean up resources for an Agent Team, as teammates may leave resources in an inconsistent state if they attempt cleanup themselves.

### ATOM-SOURCE-20260208-012-0022
**Lines**: 224-244
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When creating an Agent Team, use a prompt that specifies clear specialization for each teammate, specific tasks, a defined coordination mechanism (e.g., inbox messaging), and an outcome-focused goal.

### ATOM-SOURCE-20260208-012-0023
**Lines**: 246-256
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Use descriptive names for Agent Team members (e.g., `security-reviewer`, `test-writer`) to make inbox messages and task assignments self-documenting and clarify who performed which work.

### ATOM-SOURCE-20260208-012-0024
**Lines**: 258-266
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> The team lead should structure tasks with explicit dependencies, so that subsequent tasks automatically unblock and can be claimed by available teammates once their prerequisites are completed.

### ATOM-SOURCE-20260208-012-0025
**Lines**: 268-279
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Review Agent Team work by switching between teammates using `Shift+Up/Down` (in-process mode) or clicking into their panes (split-pane mode), asking Claude for status updates, and checking team configuration and task files in `~/.claude/teams/{team-name}/config.json` and `~/.claude/tasks/{team-name}/`.

### ATOM-SOURCE-20260208-012-0028
**Lines**: 293-295
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Include all task-specific details in the spawn prompt for Agent Team members, as they do not inherit prior conversation history from the team lead or other teammates.

### ATOM-SOURCE-20260208-012-0030
**Lines**: 304-309
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Use `CLAUDE.md` to provide project context that persists across sessions, and regularly review and update project documentation to manage memory.

### ATOM-SOURCE-20260208-012-0032
**Lines**: 318-320
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To work around the limitation of no session resumption in Agent Teams, complete team work in a single session or extract results to persistent files before shutting down.

### ATOM-SOURCE-20260208-012-0033
**Lines**: 324-326
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> If deeper hierarchy is needed within an Agent Team, use subagents within a single teammate as a workaround for the limitation of no nested teams.

### ATOM-SOURCE-20260208-012-0034
**Lines**: 330-333
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Always confirm that Agent Team members are idle before initiating shutdown, as they can reject shutdown requests if they are in the middle of critical tasks.

### ATOM-SOURCE-20260208-012-0036
**Lines**: 340-342
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Mitigate high token costs by only using Agent Teams for tasks where parallel exploration genuinely adds value; for sequential work, use a single session.

### ATOM-SOURCE-20260208-012-0038
**Lines**: 346-346
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> To switch between team members in the 'In-Process' teammate mode, use `Shift+Up/Down` in your main terminal.

### ATOM-SOURCE-20260208-012-0042
**Lines**: 369-373
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> To enable 'Split Panes' teammate mode in Claude Code, add `"teammateMode": "tmux"` to your `settings.json` file.

### ATOM-SOURCE-20260208-012-0043
**Lines**: 370-374
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To enable split-pane mode for Agent Teams, add `"teammateMode": "tmux"` to your `settings.json` and ensure tmux is installed or you are using iTerm2 on macOS.

### ATOM-SOURCE-20260208-012-0045
**Lines**: 387-387
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> For enhanced support with 'Split Panes' mode in iTerm2, the recommended setup is using `tmux -CC`.

### ATOM-SOURCE-20260208-012-0055
**Lines**: 458-459
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> Use the `TeammateIdle` hook to provide feedback or additional tasks to keep a teammate working.

### ATOM-SOURCE-20260208-012-0056
**Lines**: 463-464
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> Use the `TaskCompleted` hook to validate work meets quality standards before accepting completion.

### ATOM-SOURCE-20260208-012-0057
**Lines**: 472-476
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> If teammates are not spawning in Claude Code, check if the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` environment variable is set, restart the terminal, and verify the Claude Code version supports Agent Teams.

### ATOM-SOURCE-20260208-012-0058
**Lines**: 479-481
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> To avoid merge conflicts from simultaneous edits by multiple teammates, structure tasks so teammates work on separate files or use task dependencies to serialize same-file edits.

### ATOM-SOURCE-20260208-012-0059
**Lines**: 484-488
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> If teammates are stuck waiting, review task dependencies (`cat ~/.claude/teams/{team}/tasks/*.json`), unblock tasks manually if dependencies are incorrect, or have the team lead restructure the task list.

### ATOM-SOURCE-20260208-012-0060
**Lines**: 491-495
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> To reduce high token usage, reduce the number of teammates if work isn't genuinely parallel, use a lower Opus 4.6 effort level for routine tasks, or switch to a single session for sequential work.

### ATOM-SOURCE-20260208-012-0063
**Lines**: 517-524
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=1.00, epistemic_stability=1.00

> To implement OAuth2 using Agent Teams, spawn specialized teammates like a Researcher (investigates best practices), an Implementer (builds auth flow), and a Test writer (creates test coverage), allowing them to coordinate directly via messaging and shared task lists.
