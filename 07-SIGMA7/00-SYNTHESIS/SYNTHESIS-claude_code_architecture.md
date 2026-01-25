# Claude Code Architecture: Canonical Reference

**Version**: 1.0.0 | **Stream**: A | **Compression**: 91K → ~7K words

---

## Executive Frame

Claude Code represents a paradigm shift from copilot-as-autocomplete to **agentic harness**—a terminal-native execution engine granting LLMs agency over filesystem, shell, and external integrations. While IDE tools (Cursor, Windsurf) operate Human-in-the-Loop with context limited to open files, Claude Code operates **Human-on-the-Loop**: perceive state → reason → act → observe → iterate.

Three enduring principles persist regardless of feature evolution:
1. **Context is finite** and requires active curation (the compaction problem)
2. **Separating planning from execution** improves outcomes (Plan Mode pattern)
3. **Hierarchical natural-language instructions** scale better than brittle programmatic controls (CLAUDE.md as "soft programming")

---

## TERM Blocks: Core Concepts

```
TERM AgenticLoop:
sutra: "Perceive-reason-act-observe-iterate: the recursive decision engine"
gloss: Claude Code wraps LLM in runtime with tool access, enabling autonomous
       multi-step workflows. Unlike chat, it changes world state through files,
       commands, and integrations, course-correcting on errors.
spec:
    type: TERM
    cycle: [perception, reasoning, action, observation, iteration]
    tool_classes: [filesystem, bash, MCP, desktop, subagents]
    mode: HOTL (Human-on-the-Loop) not HITL
    differentiator: "Agent can be tasked with hours of execution, maintaining
                    internal state and self-correcting on failures"
end
```

```
TERM ContextManagement:
sutra: "200K ceiling, 75% sweet spot—context rot is real, externalize state"
gloss: Token scarcity governs all. Quality degrades before capacity exhausts.
       Auto-compaction at 95% is lossy; manual compaction with focus instructions
       at 70% preserves critical state. CLAUDE.md persists through compaction.
spec:
    type: TERM
    context_limit: 200K tokens (Sonnet 4.5), 500K (Enterprise)
    optimal_utilization: 75% maximum for quality preservation
    compaction_trigger: auto at ~95%, manual recommended at 70%
    anti_pattern: "Running until exhaustion destroys reasoning quality"
    key_insight: "Structured context (CLAUDE.md, files) more stable than
                 massive raw transcript"
    symptoms_of_rot: [forgetting instructions, looping, slower responses,
                     increased errors]
end
```

```
TERM CLAUDEmd:
sutra: "Soft programming via hierarchical natural language—every mistake becomes a rule"
gloss: Primary persistent memory mechanism. Loaded at session start, survives
       compaction. Hierarchical loading enables granular context engineering from
       organization → project → directory → local scope.
spec:
    type: TERM
    loading_order:
        1: Enterprise/Organization (~/.../CLAUDE.md)
        2: Project root (./CLAUDE.md or ./.claude/CLAUDE.md)
        3: Project rules (.claude/rules/*.md)
        4: User global (~/.claude/CLAUDE.md)
        5: Project local (./CLAUDE.local.md, gitignored)
        6: Subdirectory (recursive refinement)
    import_syntax: "@path/to/file (max 5 hops depth)"
    conditional_rules: "YAML frontmatter with paths: ['src/api/**/*.ts']"
    content_limit: "~150-200 instructions for reliable following"
    compounding_pattern: "Every error → add rule → system improves forever"
end
```

```
TERM SkillSystem:
sutra: "Progressive disclosure: metadata at startup, full instructions on activation"
gloss: Skills are folders with SKILL.md providing procedural knowledge agents
       load on-demand. Unlike slash commands (deterministic invocation), skills
       activate semantically when task matches description.
spec:
    type: TERM
    structure: "skill-name/SKILL.md + optional scripts/, references/, assets/"
    frontmatter_required: [name, description]
    frontmatter_optional: [license, compatibility, metadata, allowed-tools]
    discovery: "Load name+description (~100 tokens) at startup for all skills"
    activation: "When task matches description, load full SKILL.md"
    invocation_modes:
        user_invocable: "/ prefix or user-invocable: true"
        model_invocable: "Automatic when relevant (default)"
        disable: "disable-model-invocation: true"
    subagent_pairing: "agent: Explore | context: fork | model: haiku"
    hot_reload: "Changes in ~/.claude/skills immediately available"
end
```

```
TERM TaskSystem:
sutra: "Dependency-aware orchestration: blocked tasks cannot begin until prerequisites complete"
gloss: Jan 2026 evolution from flat todo lists. Tasks have subjects, descriptions,
       owners, and blockedBy relationships. Persists within sessions (survives
       compaction) and across sessions (via CLAUDE_CODE_TASK_LIST_ID env var).
spec:
    type: TERM
    tools: [TaskCreate, TaskUpdate, TaskGet, TaskList]
    status_states: [pending, in_progress, completed]
    dependency_model: "addBlockedBy: ['1', '2'] → task cannot start until
                      tasks 1 AND 2 completed"
    persistence:
        within_session: "Survives context compaction"
        across_sessions: "Set CLAUDE_CODE_TASK_LIST_ID env or in settings.json"
    storage: "~/.claude/tasks/<list-id>/*.json"
    agent_assignment: "owner field labels which agent handles task"
    parallel_spawn: "Multiple Task tool calls in one message = parallel agents"
    visual_tracking: "ctrl+t toggles task dashboard in terminal"
end
```

```
TERM HookLifecycle:
sutra: "Deterministic control points: validate before, polish after, checkpoint before compact"
gloss: Hooks inject logic at specific lifecycle events. PreToolUse guards against
       dangerous operations; PostToolUse auto-formats; PreCompact saves state;
       Stop audits session end.
spec:
    type: TERM
    hook_types:
        PreToolUse: "Before tool executes; exit code 2 blocks action"
        PostToolUse: "After tool completes; receives results"
        UserPromptSubmit: "When user sends message"
        PreCompact: "Before context compaction"
        Stop: "When session ends"
        Notification: "On permission requests"
    configuration: "settings.json or .claude/hooks/"
    matcher_syntax: "tool == 'Bash' && tool_input.command matches 'rm'"
    governance_patterns:
        - "Prevent force-pushes to main"
        - "Auto-format on Write (prettier, black)"
        - "Run tests before commits"
        - "Backup state before compaction"
end
```

```
TERM PlanMode:
sutra: "Decompose before acting: Opus plans, Sonnet executes, file anchors survive compaction"
gloss: Explicit separation of planning (research, decomposition) from execution
       (implementation). Plan written to file (PLAN.md) serves as external working
       memory immune to context decay.
spec:
    type: TERM
    activation: "Shift+Tab twice or /plan"
    model_pattern:
        planning: "Opus 4.5 with Thinking tokens (deep reasoning)"
        execution: "Sonnet 4.5 (faster, cheaper)"
    workflow:
        1: "Agent explores code"
        2: "Agent writes PLAN.md (checklist of steps)"
        3: "User approves"
        4: "Agent executes Step 1"
        5: "Agent marks Step 1 complete in PLAN.md"
    compaction_immunity: "Even if context wiped, agent reads PLAN.md to reorient"
    differentiator: "Creates checkpoint; human reviews before destructive changes"
end
```

```
TERM AccessPoints:
sutra: "CLI executes, Desktop integrates GUI, Web offloads—Teleport bridges all"
gloss: Three interfaces serve different roles. CLI is primary scriptable runtime.
       Desktop adds OS integration and Computer Use. Web provides cloud sandbox
       for long-running tasks. Teleport enables session mobility between interfaces.
spec:
    type: TERM
    cli:
        role: "Primary execution engine, fully scriptable"
        key_flags: ["-p (headless)", "--dangerously-skip-permissions",
                   "--session <name>", "--continue", "--teleport"]
        parallelism: "Multiple instances via tabs, tmux, worktrees"
    desktop:
        role: "GUI wrapper + Computer Use (mouse/keyboard control)"
        unique: [worktree_management, tabbed_sessions, visual_compaction]
    web:
        role: "Cloud sandbox for background execution"
        unique: [mobile_access, persistent_sessions, teleport_target]
    teleport:
        mechanism: "& prefix sends to web; --teleport moves between interfaces"
        pattern: "Start local, identify long task, teleport to cloud, continue work"
end
```

```
TERM SubagentDelegation:
sutra: "Ephemeral specialists: isolated context, discrete artifacts, clean return"
gloss: Task tool spawns subagents with specific prompts, tools, and constraints.
       Operates in separate context to prevent pollution. Returns artifacts to
       main agent upon completion.
spec:
    type: TERM
    subagent_types:
        general_purpose: "Full read/write/execute capabilities"
        bash: "Terminal only, fast, focused"
        explore: "Read-only codebase navigation (quick/medium/thorough)"
        plan: "Read-only architectural design"
    model_selection:
        haiku: "Simple tasks, fast/cheap"
        sonnet: "Most implementation work"
        opus: "Complex reasoning, architecture"
    when_use: "Task needs specialist context; isolation prevents pollution;
               output is discrete artifact"
    when_avoid: "Requires holistic reasoning; iterative refinement needed;
                critical context would be hidden"
    context_modes:
        fresh: "Default—new context with prompt only"
        fork: "Copies current context to subagent"
end
```

```
TERM MCPIntegration:
sutra: "USB-C for AI: external tools as structured APIs, lazy-loaded to preserve context"
gloss: Model Context Protocol connects Claude to external services. Tool Search
       mechanism provides lightweight search tool (~500 tokens) instead of loading
       all tool schemas (70K+ tokens), enabling lazy loading.
spec:
    type: TERM
    architecture: "Host (Claude Code) → Client (internal) → Server (external process)"
    configuration: [".mcp.json (project)", "~/.claude.json (user)",
                   "managed-mcp.json (enterprise)"]
    key_servers:
        github: "PR management, issue tracking, code review"
        filesystem: "Cross-directory file access"
        slack: "Communication, notifications"
        notion: "Documentation, wikis"
        database: "BigQuery, Postgres, MongoDB"
        memory: "Structured key-value persistence via SQLite"
    context_tax: "Each tool schema consumes tokens"
    mitigation: "Tool Search lazy loads—only needed tools enter context"
    governance: "Have 20-30 configured, keep <10 enabled per project"
end
```

```
TERM WorktreeIsolation:
sutra: "Parallel agents on same repo: separate checkouts, no file conflicts, clean merges"
gloss: Git worktrees enable multiple Claude instances to work on same repository
       without race conditions. Each agent gets isolated directory while sharing
       .git history.
spec:
    type: TERM
    setup: "git worktree add ../agent-backend feature/backend-refactor"
    pattern: "Each agent launched in respective worktree directory"
    benefits: [no_file_locks, independent_branches, isolated_changes]
    merge_strategy: "Long isolated branches with infrequent merges"
    coordination: "Oracle assigns orthogonal zones (backend vs frontend vs docs)"
end
```

---

## Orchestration Patterns

### The Oracle Pattern
Centralized command hierarchy for multi-agent systems:
- **Oracle (Opus)**: Maintains master_plan.md, outputs delegation via task files
- **Workers (Sonnet)**: Watch task directories, execute, write to results/
- **Feedback**: Oracle reads results, updates plan, issues new tasks
- **Coordination**: File-based bus enables async coordination without networking

### The 3 Amigos Pattern
Functional specialization by role:
- **PM Agent**: User requirements → Specifications
- **UX Agent**: Design system → Prototypes
- **Dev Agent (Claude Code)**: Specs + Mockups → Code

Linear handoff ensures Dev receives fully specified tickets, maximizing one-shot success.

### Boris Cherny's Fleet Commander
- 5 local terminal tabs + 5-10 web sessions concurrently
- Opus 4.5 with Thinking tokens exclusively
- Git worktrees for isolation
- PostToolUse hooks for auto-formatting
- Every mistake → add to CLAUDE.md

### The Ralph Pattern (Fresh Context Loops)
External bash loop that:
1. Reads prompt file
2. Runs Claude Code
3. Waits for completion
4. Loops again with **fresh context**

**Critical**: No compaction, no growing memory files, static prompt. AI operates in smartest mode because whiteboard wiped after every task.

**Anti-pattern**: Anthropic's official plugin uses compaction instead of wipe—defeats the purpose.

---

## Anti-Patterns and Failure Modes

### Context Failures
- **Infinite Compaction Loop**: Claude reads same files, attempts compact, restarts → Press Esc, /clear, fresh session
- **Context Confusion**: Claude "forgets" what it built after compaction → Manual compact with focus instructions
- **Over-reliance on Auto-Compact**: Leads to corruption → Proactive manual compaction

### Execution Failures
- **Test Death Spiral**: Changes tests to match bad code instead of fixing code → TDD first, review test changes skeptically
- **Gives Up Early**: Task too large for single context → Break into smaller separable tasks
- **Looping on Failures**: Same failing approach repeatedly → Interrupt, request post-mortem + new plan

### Orchestration Anti-Patterns
- **PKM-style Systems for Systems' Sake**: 90% of Claude Code posts are organizing without behavior change → "Does this config change agent behavior or just feel organized?"
- **Overstuffing CLAUDE.md**: Beyond 150-200 instructions, instruction-following degrades
- **Over-Parallelization**: Beyond 5-10 agents, coordination overhead exceeds benefit; human attention becomes bottleneck

### Security Anti-Patterns
- **--dangerously-skip-permissions Without Isolation**: Never on real machine; requires Docker/VM
- **Sharing ~/.claude.json Across Trust Boundaries**: Permissions leak between contexts
- **Network Access Without Review**: MCP servers can exfiltrate data

---

## Model Economics

| Model | Cost (Input/Output per 1M) | Role | Use When |
|-------|---------------------------|------|----------|
| **Opus 4.5** | $15/$75 | Senior Principal Engineer | Oracle, Architect phases, complex reasoning |
| **Sonnet 4.5** | $3/$15 | Senior Engineer | Execution, routine implementation |
| **Haiku** | Cheapest | Fast worker | Simple searches, quick validations |

**Pattern**: Opus generates PLAN.md, Sonnet executes it.

**Thinking Tokens**: Enable for Plan Mode and debugging; disable for routine tasks to save cost.

---

## Enduring Principles

1. **Context is finite**: Quality degrades before capacity exhausts. Design for strategic compaction and external memory.

2. **Plan before execute**: Forcing decomposition prevents cascading errors. Build into workflows at multiple levels.

3. **Hierarchical behavioral constitution**: Natural language instructions in layered files scale better than programmatic control. Git-tracked memory compounds institutional knowledge.

4. **Graduated autonomy**: Normal → Auto-Accept → Plan Mode → Headless. Build trust through validation, expand as patterns prove reliable.

5. **Specialist isolation**: Bounded contexts produce higher quality reasoning. Design for subagents, clear handoffs, artifact-based coordination.

6. **Verification as core primitive**: Trust but verify. Independent checks on every "Task Complete" signal. 2-3x quality improvement from systematic verification.

7. **File-based handoffs**: Using filesystem as coordination layer enables multi-agent systems without complex protocols. Version controlled, human inspectable, works across platforms.

---

## Cross-References

- [[MECH-skill_system_architecture]] — Progressive disclosure, SKILL.md format, subagent pairing
- [[MECH-task_orchestration]] — Dependency management, parallel spawning, persistence
- [[MECH-context_compaction_strategies]] — 75% rule, manual vs auto, focus instructions
- [[MECH-hooks_lifecycle_automation]] — PreToolUse guards, PostToolUse polish, governance patterns
- [[MECH-headless_mode_automation]] — -p flag, output formats, CI/CD integration
- [[PRAC-parallel_claude_orchestration]] — Multi-instance patterns, worktrees, teleport
- [[PRAC-ralph_pattern_execution]] — Fresh context loops, static prompts, one-shot tasks

---

*"The agentic loop perceives, reasons, acts, observes, iterates—your job is to distill this into memorable wisdom."*
