# Extraction: SOURCE-20260206-005

**Source**: `SOURCE-20260206-x-article-ericbuess-claude_code_agent_teams_what_i_learned_from_testing.md`
**Atoms extracted**: 55
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (34)

### ATOM-SOURCE-20260206-005-0001
**Lines**: 5-6
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> Anthropic has released "Agent Teams" in Claude Code, coinciding with Opus 4.6, which the community refers to as "swarm mode."

### ATOM-SOURCE-20260206-005-0005
**Lines**: 18-18
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> When using agent teams, Claude creates the team, spawns teammates, distributes work, and manages coordination based on natural language descriptions of the task and team structure.

### ATOM-SOURCE-20260206-005-0006
**Lines**: 19-20
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Each teammate in an agent team loads the same project context (CLAUDE.md, MCP servers, skills) but does not inherit the lead's conversation history.

### ATOM-SOURCE-20260206-005-0007
**Lines**: 26-27
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> The terms "swarm mode" and "Agent Teams" refer to the same feature; "Agent Teams" is Anthropic's official name, while "swarm mode" was popularized by the community.

### ATOM-SOURCE-20260206-005-0008
**Lines**: 33-33
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Agent teams are an experimental feature in Claude Code and are disabled by default, requiring manual activation.

### ATOM-SOURCE-20260206-005-0010
**Lines**: 39-41
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> If Agent Teams are not enabled, Claude Code defaults to using 'subagents,' which are single-session helpers without inter-agent messaging, shared task lists, or split panes.

### ATOM-SOURCE-20260206-005-0013
**Lines**: 53-53
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> In-Process Mode works in any terminal and requires no extra setup.

### ATOM-SOURCE-20260206-005-0014
**Lines**: 55-56
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The default display mode for agent teams is "auto," which uses split panes if in a tmux session and falls back to in-process mode otherwise.

### ATOM-SOURCE-20260206-005-0016
**Lines**: 62-62
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Split-Pane Mode requires `tmux` or `iTerm2`.

### ATOM-SOURCE-20260206-005-0017
**Lines**: 66-69
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> Split-pane mode is useful for real-time monitoring of multiple teammates' output, catching mistakes early, or providing mid-task instructions, especially for debugging or visualizing parallel work.

### ATOM-SOURCE-20260206-005-0018
**Lines**: 71-72
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> In-process mode is preferable when only results are needed, as it handles many teammates without screen clutter and has less setup friction.

### ATOM-SOURCE-20260206-005-0019
**Lines**: 78-80
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Split panes are supported in tmux (within any terminal) and iTerm2 (with the it2 CLI and Python API enabled).

### ATOM-SOURCE-20260206-005-0020
**Lines**: 83-85
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> In-process mode only (no split panes) is supported in Ghostty, VS Code terminal, Windows Terminal, and other terminals.

### ATOM-SOURCE-20260206-005-0021
**Lines**: 87-87
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The official documentation states that split-pane mode is not supported in VS Code's integrated terminal, Windows Terminal, or Ghostty.

### ATOM-SOURCE-20260206-005-0023
**Lines**: 95-97
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The `teammateMode` setting in `settings.json` can be set to "tmux" or "in-process," though schema validation errors might require using the CLI flag depending on the Claude Code version.

### ATOM-SOURCE-20260206-005-0024
**Lines**: 95-103
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Claude Code's current experimental phase does not reuse panes; new panes are created for each teammate session, leading to accumulation if not restarted.

### ATOM-SOURCE-20260206-005-0026
**Lines**: 99-100
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The "tmux" value for `teammateMode` auto-detects whether to use tmux or iTerm2 based on the terminal.

### ATOM-SOURCE-20260206-005-0027
**Lines**: 103-105
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The default `teammateMode` of "auto" only triggers split panes if already inside a tmux session; in native iTerm2, it falls back to in-process mode, requiring explicit `--teammate-mode tmux` to get panes.

### ATOM-SOURCE-20260206-005-0028
**Lines**: 113-117
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> iTerm2's native integration for split panes offers macOS-specific benefits like Cmd+click on file paths, proper trackpad scrollback, native text selection, macOS Services menu, and built-in search.

### ATOM-SOURCE-20260206-005-0029
**Lines**: 119-121
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> iTerm2 native pane management allows smooth resizing, respects iTerm2 profile settings (colors, fonts, transparency), and enables detaching panes into separate tabs or windows.

### ATOM-SOURCE-20260206-005-0030
**Lines**: 123-124
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The iTerm2 native approach for split panes has higher setup friction (installing `it2` CLI, enabling Python API, using CLI flag) and is exclusive to macOS.

### ATOM-SOURCE-20260206-005-0031
**Lines**: 128-130
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> tmux offers portability across macOS, Linux, and remote SSH sessions, making it the only option for agent teams with split panes on dev servers.

### ATOM-SOURCE-20260206-005-0032
**Lines**: 130-132
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> tmux is highly scriptable with a rich command language for pane management and supports detaching/reattaching sessions, allowing sessions to survive terminal crashes.

### ATOM-SOURCE-20260206-005-0033
**Lines**: 134-136
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> tmux panes lack native macOS gestures, such as trackpad scrolling (requiring tmux's copy mode), Cmd+click, and native text selection across pane boundaries, and copy/paste requires tmux's own buffer system or mouse mode.

### ATOM-SOURCE-20260206-005-0034
**Lines**: 141-143
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Running `tmux -CC` in iTerm2 combines tmux's session persistence and detach/reattach capabilities with native iTerm2 split pane rendering, offering a hybrid solution for durability and native macOS feel.

### ATOM-SOURCE-20260206-005-0038
**Lines**: 166-170
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Agent teams consume significantly more tokens than single Claude Code sessions due to each teammate having its own context window, inter-teammate messaging, and shared task list polling.

### ATOM-SOURCE-20260206-005-0044
**Lines**: 202-202
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Teams and tasks are stored locally under `~/.claude/teams/` and `~/.claude/tasks/`, organized by team name.

### ATOM-SOURCE-20260206-005-0047
**Lines**: 219-223
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agent memory, managed dynamically by the agent itself, compounds across conversations, creating a knowledge base that can specialize agents (e.g., a code reviewer remembering common issues, a security auditor knowing architecture, a test writer knowing patterns).

### ATOM-SOURCE-20260206-005-0049
**Lines**: 238-249
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Memory frontmatter is particularly useful for specialized agents like code reviewers learning common mistakes, security auditors mapping attack surfaces, test writers learning testing patterns, and onboarding helpers documenting codebases.

### ATOM-SOURCE-20260206-005-0050
**Lines**: 251-256
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> `CLAUDE.md` files are more suitable for information that rarely changes (coding standards, project structure), instructions requiring explicit control, context for the main session, and team-shared information committed to Git.

### ATOM-SOURCE-20260206-005-0051
**Lines**: 261-272
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> Claude Code's hierarchical memory system includes Managed policy (OS-specific, for all users), Project memory (`CLAUDE.md` in project root, team-shared), Project rules (`.claude/rules/`, modular, topic-specific, path-scoped), User memory (`~/.claude/CLAUDE.md`, personal across projects), and Project local (`CLAUDE.local.md` in project root, personal, project-only).

### ATOM-SOURCE-20260206-005-0052
**Lines**: 274-276
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.90

> All Claude Code memory files load automatically at startup, support recursive imports up to 5 hops deep via `@path/to/import` syntax, and can be edited with the `/memory` command or bootstrapped with `/init`.

### ATOM-SOURCE-20260206-005-0053
**Lines**: 280-289
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.80

> Current limitations of Claude Code agent teams include limited teammate resumption after lead session resume, potential task status lag, slow teammate shutdown, a 'one team per session' guideline (though possibly flexible in in-process mode), no nested teams, fixed lead promotion, and split pane support limited to tmux and iTerm2.

### ATOM-SOURCE-20260206-005-0055
**Lines**: 288-288
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.10, epistemic_stability=0.90

> Claude Code Agent Teams were released with Opus 4.6 on February 5, 2026.

## Concept (10)

### ATOM-SOURCE-20260206-005-0002
**Lines**: 12-12
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Agent teams allow for the coordination of multiple Claude Code instances to work collaboratively on a single task.

### ATOM-SOURCE-20260206-005-0003
**Lines**: 14-14
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> In an agent team, one Claude Code session acts as the 'team lead,' responsible for coordinating work, assigning tasks, and synthesizing results.

### ATOM-SOURCE-20260206-005-0004
**Lines**: 15-16
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Teammates in an agent team are independent Claude Code instances, each with their own context window, capable of direct communication with each other.

### ATOM-SOURCE-20260206-005-0011
**Lines**: 45-45
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Agent teams offer two display modes for teammate activity: In-Process Mode and Split-Pane Mode.

### ATOM-SOURCE-20260206-005-0012
**Lines**: 49-51
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> In-Process Mode for agent teams runs all teammates within the main terminal, allowing interaction via Shift+Up/Down, typing messages, viewing sessions with Enter, interrupting with Escape, and toggling a shared task list with Ctrl+T.

### ATOM-SOURCE-20260206-005-0015
**Lines**: 59-60
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Split-Pane Mode for agent teams assigns each teammate its own terminal pane, allowing simultaneous viewing of output and direct interaction by clicking into any pane.

### ATOM-SOURCE-20260206-005-0036
**Lines**: 154-157
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Subagents are single-session helpers that report results back to the caller, cannot message each other, and are managed by the main agent, offering lower token cost and built-in functionality.

### ATOM-SOURCE-20260206-005-0037
**Lines**: 159-162
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Agent Teams are independent Claude Code instances whose teammates message each other directly, share a task list with self-coordination, cost significantly more tokens, and require an experimental flag.

### ATOM-SOURCE-20260206-005-0041
**Lines**: 184-189
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.90

> Agent memory can be stored at a `project` scope (in `.claude/agent-memory/` under the agent's name, shareable via version control) or `local` scope (in `.claude/agent-memory-local/` under the agent's name, project-specific but not version-controlled).

### ATOM-SOURCE-20260206-005-0048
**Lines**: 228-235
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.30, epistemic_stability=0.90

> `CLAUDE.md` files (project, user, rules) are for static instructions and rules, while memory frontmatter on subagents is for dynamic, agent-managed learning that compounds over time.

## Framework (1)

### ATOM-SOURCE-20260206-005-0043
**Lines**: 196-200
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Every agent team comprises four components: a Team lead (main Claude Code session for coordination), Teammates (separate Claude Code instances for tasks), a shared Task list, and a Mailbox for direct inter-agent communication.

## Praxis Hook (10)

### ATOM-SOURCE-20260206-005-0009
**Lines**: 35-37
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To enable Agent Teams, add an `env` block to `settings.json` with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` set to `"1"`, or export the variable in your shell before launching Claude Code.

### ATOM-SOURCE-20260206-005-0022
**Lines**: 89-92
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To get split panes working in iTerm2, install the `it2` CLI, enable the Python API in iTerm2 settings (General > Magic), and launch Claude Code with the `--teammate-mode tmux` flag.

### ATOM-SOURCE-20260206-005-0025
**Lines**: 95-103
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.60, actionability=0.80, epistemic_stability=0.70

> Avoid setting up auto-close automation for Claude Code sessions, as it conflicts with the tool's current behavior and will likely necessitate restarting Claude Code.

### ATOM-SOURCE-20260206-005-0035
**Lines**: 147-149
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For macOS local work, iTerm2 native is preferred; for portability, remote access, or session persistence, use tmux; for both, use `tmux -CC` in iTerm2.

### ATOM-SOURCE-20260206-005-0039
**Lines**: 179-181
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Start with a small 2-teammate agent team for research tasks before scaling up to more agents for feature builds to manage token cost.

### ATOM-SOURCE-20260206-005-0040
**Lines**: 184-193
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Agent teams are effective for research and review, new module/feature development, debugging with competing hypotheses, cross-layer coordination, and parallel code review.

### ATOM-SOURCE-20260206-005-0042
**Lines**: 193-200
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.90

> When an agent's `memory` field is set, its system prompt automatically includes instructions for memory directory interaction, the first 200 lines of `MEMORY.md` are injected into its system prompt, and Read, Write, and Edit tools are enabled for memory file management.

### ATOM-SOURCE-20260206-005-0045
**Lines**: 206-212
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To leverage agent memory effectively, instruct the agent to consult its memory before starting work (e.g., "Review this PR, and check your memory for patterns you've seen before") and to update its memory after completing work (e.g., "Now that you're done, save what you learned to your memory").

### ATOM-SOURCE-20260206-005-0046
**Lines**: 214-217
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Embedding memory instructions directly in the agent file, such as "Update your agent memory as you discover codepaths, patterns, library locations, and key architectural decisions," can enable the agent to proactively maintain its knowledge base.

### ATOM-SOURCE-20260206-005-0054
**Lines**: 281-285
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To discover new features for Claude Code, run `/docs` and ask the Claude Code instance about the features, especially if using the `claude-code-docs` project for a local mirror of documentation.
