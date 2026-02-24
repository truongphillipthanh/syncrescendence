# Extraction: SOURCE-20260219-020

**Source**: `SOURCE-20260219-x-thread-jpschroeder-weve_open_sourcing_dmux_our.md`
**Atoms extracted**: 14
**Categories**: claim, praxis_hook

---

## Claim (8)

### ATOM-SOURCE-20260219-020-0003
**Lines**: 27-28
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> The coordinator feature in Dmux is a 'game changer' for OSS maintainers with many related projects.

### ATOM-SOURCE-20260219-020-0004
**Lines**: 37-39
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> Dmux does not add extra layers to existing coding agents because each agent already possesses its own capacity for inter-agent and sub-agent communication.

### ATOM-SOURCE-20260219-020-0005
**Lines**: 43-44
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Tmux is suitable for running AI agent swarms because it operates in a server environment and provides a full programming layer.

### ATOM-SOURCE-20260219-020-0007
**Lines**: 46-49
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> If a terminal crashes, Dmux sessions continue to run, allowing users to resume by opening a new terminal, navigating to the directory, and running dmux.

### ATOM-SOURCE-20260219-020-0008
**Lines**: 53-53
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.50

> Codex is preferred for all tasks except UI development.

### ATOM-SOURCE-20260219-020-0010
**Lines**: 61-62
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> Dmux is designed to be 'dev-centric' and supports TUI interfaces for development tasks.

### ATOM-SOURCE-20260219-020-0013
**Lines**: 79-79
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> AI automatically names agents in Dmux.

### ATOM-SOURCE-20260219-020-0014
**Lines**: 89-91
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Dmux uses the user's existing Claude code and requires an OpenRouter key, which can sustain usage for months on $10.

## Praxis Hook (6)

### ATOM-SOURCE-20260219-020-0001
**Lines**: 3-9
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Dmux is an internal tool for running Codex and Claude Code swarms, utilizing tmux, worktrees, and various AI models (Claude, Codex, Opencode). It includes hooks for worktree automation, A/B testing between Claude and Codex, and worktree management.

### ATOM-SOURCE-20260219-020-0002
**Lines**: 19-26
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Dmux allows users to create a 'coordinator' by setting up a parent directory/repo containing multiple related projects, each with its own git repository and excluded from the parent's .gitignore. Dmux detects these sub-repositories and automatically creates worktrees for them when a worktree is created in the root.

### ATOM-SOURCE-20260219-020-0006
**Lines**: 44-46
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.50, actionability=0.70, epistemic_stability=0.40

> Dmux has an experimental 'autopilot' mode that can read the tmux stream and use an LLM to help steer the AI.

### ATOM-SOURCE-20260219-020-0009
**Lines**: 57-57
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> When in a branch, Dmux creates the worktree as a branch off that existing branch.

### ATOM-SOURCE-20260219-020-0011
**Lines**: 69-69
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Dmux can prompt the user to spin up another agent pane to resolve conflicts.

### ATOM-SOURCE-20260219-020-0012
**Lines**: 73-75
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> If using the Dmux tmux configuration, users can click or use 'ctrl-option' and an arrow to navigate between panes; otherwise, they need to look up pane switching in tmux.
