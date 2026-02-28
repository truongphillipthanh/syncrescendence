**Key Findings on Claude Code Architecture and Advanced Capabilities**

- **Task System**: The Task primitive is a robust, persistent coordination layer with dependency graphs (via `blockedBy`), real-time updates, and sharing across CLI instances using `CLAUDE_CODE_TASK_LIST_ID`. It supports atomic-like updates through broadcasting and owner tracking, reducing race conditions. This makes Tasks a superior alternative to ad-hoc `plan.md` files for multi-agent orchestration.

- **Context Management**: No evidence of automatic compaction or persistence through any compaction process. Sessions rely on manual `/clear` resets to combat context degradation; long sessions still require periodic hard resets to maintain recall quality.

- **Skills and Subagents**: Skills unify with slash commands and support `context: fork` for spawning isolated subagents (no full history inheritance). Nesting/recursion is possible by invoking other skills, though bounded by system limits, enabling fractal-like topologies.

- **Emergent Behaviors**: Community reports demonstrate recursive self-improvement (e.g., agents updating `CLAUDE.md` on errors), headless swarms (via tools like Claude Flow or git worktrees), and agentic file search outperforming traditional RAG in large codebases.

- **Hypotheses Viability**: Git-based communication via worktrees and commit logs is practical; MCP abstractions exist for DevOps tools (Kubernetes, AWS, Docker); dense memory compression is explored in community patterns but lacks official lossless continuity.

**God-Config Recommendations**  
Use `CLAUDE.md` for persistent instructions (e.g., anti-patterns, style guides), enable shared tasks with `CLAUDE_CODE_TASK_LIST_ID`, configure `.mcp.json` for external tools, and set `settings.json` to allow necessary tools while preserving safety.

**Oracle Protocol**  
Delegate via Task creation, assign owners to subagents, monitor with TaskList, and use git worktrees for isolation.

**Recursion Hook**  
Implement PostToolUse logic (via custom skills or scripts) to log failures and prompt updates to `CLAUDE.md`.

---

Claude Code represents Anthropic's official command-line agent for agentic coding, combining file editing, shell execution, Git integration, and external tool access via MCP (Model Context Protocol). It supports complex workflows through skills, subagents, and recent additions like the Task system, evolving from simple prompting to sophisticated multi-agent orchestration.

### Phase 1: Core Mechanics Validation

The Task system is a persistent, graph-based primitive stored in `~/.claude/tasks/`. Tasks survive session termination and support dependencies via `blockedBy`/`blocks` fields. The `CLAUDE_CODE_TASK_LIST_ID` environment variable enables shared task lists across disparate CLI instances (different terminals, worktrees), with real-time broadcast updates and owner tracking to mitigate conflicts. While not formally atomic, the design (immediate notifications, ownership locks) prevents most race conditions in practice. This positions Tasks as a unified coordination bus superior to markdown-based plans: generate tasks from `plan.md`, execute via dependencies, and hydrate progress back to specs.

**Task JSON Schema Overview** (from community-validated sources):

| Field          | Type          | Description                                      | Required |
|----------------|---------------|--------------------------------------------------|----------|
| taskId        | string       | Unique identifier                                | Yes     |
| subject       | string       | Short title                                      | Yes     |
| description   | string       | Detailed work instructions                       | Yes     |
| status        | enum         | pending, in_progress, completed                  | Yes     |
| owner         | string       | Assigned agent/user                              | No      |
| blockedBy     | array[string]| Dependencies (taskIds)                           | No      |
| blocks        | array[string]| Tasks blocked by this one                        | No      |
| createdAt     | timestamp    | Creation time                                    | Yes     |

TaskUpdate supports `addBlockedBy`/`removeBlockedBy`, status changes, and owner assignment.

No official auto-compaction mechanism exists; context management relies on manual `/clear` to reset history and refocus. Community reports indicate no persistence of Tasks/Plans through any implicit compaction, and "context rot" (degraded recall in long sessions) persists, necessitating periodic resets. Optimal TTL appears heuristic: reset after ~50-100 tool calls or when recall noticeably falters, rather than strict token-based.

Skills unify slash commands: a `SKILL.md` directory defines a `/name` command via YAML frontmatter (`name`, `description`, `agent`, `context`). With `context: fork`, a subagent spawns with only the skill prompt (no parent history copy). The `agent` field selects type (e.g., Explore, Plan, custom). Nesting occurs naturally—subagents invoke other skills—enabling fractal topologies, though depth is bounded by context limits and anti-loop safeguards.

### Phase 2: Emergent Patterns

Community patterns demonstrate recursive self-improvement: agents log errors, analyze patterns, and append to `CLAUDE.md` "Anti-Patterns" sections or create Skills for recurring fixes. Examples include auto-linter loops feeding back into instructions, and v2.1 updates enabling skill hot-reload for compounding improvements.

Headless orchestration (`claude -p`) supports daisy-chaining via piping/scripts, with tools like Claude Flow enabling swarms. Git worktrees provide isolation for parallel agents, using filesystem/Git as a message bus.

Agentic retrieval (ripgrep/fd/grep) outperforms injected maps or MCP-RAG in large repos (>100k LoC), reducing tokens dramatically (up to 97% in benchmarks) and lowering hallucinations by grounding in real-time search rather than static indexes.

### Phase 3: Hypothesis Evaluation

**Git-Based Neural Bus**: Viable. Parallel worktrees allow workers to commit progress; an Oracle monitors `git log` for state. This creates a zero-API distributed ledger using Git primitives.

**MCP-as-OS**: Partially realized. MCP servers abstract Kubernetes, AWS, Docker into natural-language tools, enabling Claude to manage infrastructure semantically without raw shell access.

**Hyper-Compacted Memory**: Explored in community prompts emphasizing dense schemas (e.g., 70/80 rule for docs). No official lossless protocol, but custom Librarian agents can compress state into `MEMORY.md` or JSON for reload, approximating save states.

### Phase 4: Synthesis

**God-Config Suite**  
- `CLAUDE.md`: Include anti-patterns, style, security gates, Task usage instructions.  
- `settings.json`: Enable broad tools cautiously; set env for `CLAUDE_CODE_TASK_LIST_ID`.  
- `.mcp.json`: Configure DevOps servers.  
- Skills: Fork-heavy for subagents.

**Oracle Protocol**  
1. Create root tasks with dependencies.  
2. Spawn subagents via skills, assign owners.  
3. Monitor via TaskList in parallel session.  
4. Hydrate completed tasks back to markdown.

**Recursion Hook**  
Use a PostToolUse skill/script that: parses errors, appends to `CLAUDE.md`, reloads via hot-reload.

**Key Citations**  
- [Claude Code Overview](https://code.claude.com/docs/en/overview)  
- [Skills Documentation](https://code.claude.com/docs/en/skills)  
- [Claude Code Tasks Guide](https://www.dplooy.com/blog/claude-code-tasks-complete-guide-to-ai-agent-workflow)  
- [Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)  
- [Recursive Self-Improvement Discussions](https://www.reddit.com/r/ClaudeAI/comments/1laby6h/i_discovered_a_powerful_way_to_continuously)  
- [Claude Flow Swarm](https://github.com/ruvnet/claude-flow)  
- [Token Reduction Benchmark](https://www.reddit.com/r/ClaudeAI/comments/1qiv0d3/open_source_i_reduced_claude_code_input_tokens_by)  
- [MCP Docker Toolkit](https://www.docker.com/blog/add-mcp-servers-to-claude-code-with-mcp-toolkit)