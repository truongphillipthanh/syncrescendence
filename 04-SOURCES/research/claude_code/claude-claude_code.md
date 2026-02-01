# Claude Code as orchestration engine for AI-augmented knowledge work

Claude Code represents a paradigm shift from "AI-assisted coding" to **agentic infrastructure**—a model for understanding how autonomous AI tools should be designed, orchestrated, and governed. For someone building multi-Claude cognitive architecture, the key insight is that Claude Code's design patterns generalize beyond software engineering to any knowledge work requiring persistent context, parallel execution, and human-AI coordination.

The core architecture is terminal-native and agentic: Claude Code takes action directly (file edits, bash commands, git commits) rather than merely suggesting changes. This "AI drives, you supervise" model differs fundamentally from Cursor's "you drive, AI assists" paradigm. For multi-Claude orchestration, this means Claude Code instances can function as **execution engines** receiving directives from higher-order "Oracle" sessions—precisely the cognitive architecture described in your research context.

Three enduring principles emerge regardless of feature evolution: context is finite and requires active curation (the compaction problem), separating planning from execution improves outcomes (Plan Mode pattern), and hierarchical natural-language instructions scale better than brittle programmatic controls (CLAUDE.md as "soft programming").

---

## Part 1: Capability architecture

### The agentic terminal paradigm

Claude Code differs architecturally from IDE integrations through its Unix-philosophy design: composable, scriptable, and terminal-native. Where Cursor indexes your codebase via RAG and suggests changes within VS Code's chrome, Claude Code operates directly on your filesystem through shell commands. This makes Claude Code uniquely suited to orchestration—you can script it, pipe to it, run multiple instances, and integrate it into automation workflows.

**Core tool surface** spans read operations (Glob, Grep, Read), write operations (Edit, Write, NotebookEdit), execution (Bash with persistent working directory), web access (WebSearch, WebFetch), and orchestration (Task for subagent spawning, Skill for capability invocation, SlashCommand for custom workflows). The Task tool is particularly significant for multi-Claude architectures: it spawns isolated subagents with their own context windows, returning only condensed results to the main thread.

The **context window** nominally extends to 200K tokens (Sonnet 4 Enterprise offers 500K), but practitioners report quality degradation beginning around **100-150K tokens**—the "context rot" phenomenon where recall accuracy decreases as tokens accumulate. Auto-compaction triggers near capacity but is described by practitioners as "opaque, error-prone, and not well-optimized." The `/compact` command allows manual intervention with optional focus instructions specifying what to preserve.

### Access points and their affordances

Three interfaces serve different orchestration purposes:

| Interface | Best for | Unique capability |
|-----------|----------|-------------------|
| CLI (`claude`) | Automation, scripting, headless execution | `-p` flag for non-interactive mode; `claude mcp serve` to use Claude Code as MCP server |
| Desktop app | Local parallel sessions | Native git worktree management via `.worktreeinclude` |
| Web (claude.ai/code) | Background/mobile work, cloud sessions | Session teleporting for handoff to CLI |

For multi-Claude orchestration, the **CLI's headless mode** (`-p` flag) enables scripted execution: `claude -p "analyze this codebase for security vulnerabilities" --output-format json --max-turns 5`. Combined with `--dangerously-skip-permissions` in sandboxed containers, this enables fully autonomous execution pipelines.

The **teleport** mechanism (`--teleport`) hands off sessions between web and terminal. Boris Cherny, Claude Code's creator, reports using this to start sessions on mobile, let them run, then teleport to terminal for finishing work.

### Extension surface

Claude Code's extensibility operates through four mechanisms:

**MCP (Model Context Protocol)** provides the "USB-C for AI" integration layer—a standardized protocol for connecting Claude to external tools. Configuration spans local (`.mcp.json`), user (`~/.claude.json`), and enterprise (`managed-mcp.json`) scopes. Most valuable servers for knowledge work include GitHub (PR/issue management), Google Drive (document access), Slack (communication), Notion (documentation), and database connectors.

**Skills** are model-invoked capabilities that Claude automatically uses based on semantic matching to their descriptions. Unlike slash commands (explicitly invoked via `/command`), skills activate when Claude determines they're relevant. This distinction matters for orchestration: slash commands provide deterministic invocation points; skills enable emergent capability use.

**Hooks** (PreToolUse, PostToolUse, SessionStart, Stop, etc.) provide deterministic control points in the agentic loop. The PreToolUse hook can block operations via exit code 2, enabling governance patterns like preventing force-pushes to main or requiring lint passes before writes.

**Custom subagents** (`.claude/agents/agent-name.md`) define specialized execution profiles with constrained tools, specific models, and custom system prompts. This enables creating domain-specific execution engines—a "code-reviewer" subagent restricted to read operations, or a "deployer" subagent with elevated permissions but narrow scope.

---

## Part 2: Configuration deep dive

### CLAUDE.md as persistent behavioral constitution

CLAUDE.md represents "soft programming" through natural language—instructions that shape Claude's behavior without code. The hierarchical loading order matters for multi-instance setups:

1. **Enterprise policy** (`/Library/Application Support/ClaudeCode/CLAUDE.md`) — Organization-wide, IT-managed
2. **Project memory** (`./CLAUDE.md` or `./.claude/CLAUDE.md`) — Team-shared, git-tracked
3. **User memory** (`~/.claude/CLAUDE.md`) — Personal global preferences  
4. **Project local** (`./CLAUDE.local.md`) — Personal project-specific, gitignored

The import syntax (`@path/to/file`) enables modular composition with max depth of 5 hops. Boris Cherny's team adds learnings to CLAUDE.md during code review: "Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time."

**Content principles** from Anthropic's internal practices: include project overview, coding standards, tool-specific documentation (only for tools used by 30%+ of team), and workflow guidance. Treat CLAUDE.md like "ad space"—if you can't explain concisely, it's not ready. Keep under ~150-200 instructions to stay within reliable instruction-following limits.

The `.claude/rules/` directory supports YAML frontmatter for conditional rules: `paths: ["src/api/**/*.ts"]` applies rules only when Claude operates in specific directories. This enables context-appropriate behavior without polluting global instructions.

### Settings.json for operational governance

The settings hierarchy mirrors CLAUDE.md: enterprise managed → command line → local project → shared project → user. Key configuration domains:

**Permissions** use prefix matching with tool-specific patterns:
```json
{
  "permissions": {
    "allow": ["Bash(npm run test:*)", "Read(~/.zshrc)"],
    "deny": ["Bash(rm:*)", "Read(./.env)", "Read(./secrets/**)"],
    "ask": ["Bash(git push:*)"],
    "defaultMode": "acceptEdits"
  }
}
```

**Hooks** enable automation without external scripting:
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write(*.py)",
      "hooks": [{"type": "command", "command": "python -m black $file"}]
    }]
  }
}
```

**Sandbox settings** provide isolation for autonomous execution with network controls and command exclusions.

### Session persistence and continuity

Sessions persist to `~/.claude/projects/` as JSONL transcripts. The continuity commands form a workflow:

- `claude --continue` / `claude -c` — Resume most recent conversation in current directory
- `claude --resume <session-id>` — Resume specific session by ID
- `claude --resume` (no args) — Interactive session picker
- `--fork-session` — Create branch from resumed session

Named sessions enable the "Oracle issuing directives to execution engines" pattern: start strategic sessions that can be resumed, fork execution branches, and maintain separate context streams for different knowledge work domains.

**Key distinction**: Claude Code's session memory is file-based and developer-defined; claude.ai's "memory" feature is AI-inferred persistent state. They don't synchronize—for multi-Claude orchestration, rely on CLAUDE.md files and filesystem-based handoffs.

---

## Part 3: Workflow patterns from practitioners

### Boris Cherny's production workflow

The Claude Code creator's setup provides the authoritative reference pattern:

**Parallel execution**: 5 terminal sessions (numbered 1-5) + 5-10 on claude.ai/code + mobile sessions started in morning and checked later. System notifications via iTerm2 signal when Claude needs input.

**Model choice**: Opus 4.5 with thinking for everything—"despite being bigger and slower than Sonnet, you steer it less. Better tool use." This aligns with the orchestration pattern: strategic sessions benefit from maximum reasoning; tactical execution may tolerate lighter models.

**Plan Mode discipline**: Most sessions start in Plan Mode (Shift+Tab twice). Iterate until plan is good, then switch to auto-accept edits mode—"Claude usually one-shots execution." This separation of planning from execution is the core workflow insight for knowledge work: research and design in constrained mode; execute with elevated autonomy.

**Verification as force multiplier**: "Probably the most important thing to get great results out of Claude Code: give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result." For non-coding work, this means establishing validation mechanisms—checkable assertions, reference documents, external confirmation.

### Multi-instance coordination patterns

Practitioners running 5-10+ parallel instances use these coordination approaches:

**Zone ownership** (Molly Cantillon's 8-instance swarm): Each instance operates in isolation on specific domains (`~/nox`, `~/metrics`, `~/email`, `~/growth`, `~/trades`, `~/health`, `~/writing`, `~/personal`), spawning short-lived subagents, exchanging context through explicit filesystem handoffs.

**Git worktrees** for true isolation: Each worktree has independent file state, shared git history—perfect for parallel Claude sessions that must not conflict.

**Terminal grid layout** (Peter Steinberger): 3x3 terminal grid with serialized tasks or changes kept far apart so sessions don't touch each other much.

**When coordination overhead exceeds benefit**: The "reduce" step where a final agent synthesizes work of others is often the most difficult part. Multiple simple sessions beat one overloaded session, but synthesis requires careful design.

### The compounding engineering pattern

Dan Shipper and Kieran Klaassen (Every.to) articulate the meta-pattern:

"In normal engineering, every feature you add makes it harder to add the next feature. In compounding engineering, your goal is to make the next feature easier to build from the feature that you just added."

**Process**: Build feature → Document learnings (what worked, adjustments needed, issues discovered) → Codify into prompts/commands → Next feature uses this knowledge → Repeat.

The **feedback codifier pattern** operationalizes this: after leaving comments on a PR, run an agent that extracts lessons and stores them in CLAUDE.md. The next time Claude reviews code, it already knows those standards.

**Two-agent executor/evaluator pattern**: Split workflow into "executor" (does work) and "evaluator" (reviews it). This maps directly to Oracle/execution engine architecture.

### Friction solutions

**Permission fatigue**: Use `/permissions` to pre-allow safe commands in `.claude/settings.json`. Boris Cherny does NOT use `--dangerously-skip-permissions`—instead, configures explicit allow lists. Pattern: `allow Bash --cmd '*'` with specific `ask` rules for dangerous operations.

**Context bloat management**: Use `/clear` liberally between tasks. The **75% rule** (hyperdev.matsuoka): "Sessions that stop at 75% utilization produce less total output but higher-quality, more maintainable output." Use subagents for verbose operations to keep main context clean. Monitor with `/context` command.

**Looping behavior recovery**: Press Esc to interrupt, use `/clear` to reset without losing CLAUDE.md, switch to Plan Mode for explicit step-by-step reasoning, or prompt with "ultrathink" to trigger deeper reasoning (~31,999 tokens).

---

## Part 4: Integration landscape

### Claude Code vs Cursor positioning

| Dimension | Claude Code | Cursor |
|-----------|-------------|--------|
| Paradigm | "AI drives, you supervise" | "You drive, AI assists" |
| Interface | Terminal-first | IDE-first (VS Code fork) |
| Context strategy | Agentic codebase search | RAG-based local indexing |
| Best for | Complex multi-file refactoring, autonomous tasks, CI/CD integration | Real-time "vibe coding," in-flow editing, visual diff review |

**Hybrid approach** (common in 2025-2026): Cursor for interactive daily work ($20/month); Claude Code for complex refactoring and reasoning (~$100/month for power users). Many developers run Claude Code CLI inside Cursor's terminal.

For multi-Claude orchestration, Claude Code's scriptability and autonomous execution model make it the appropriate execution engine. Cursor serves the "human actively steering" use case.

### MCP ecosystem for knowledge work

Beyond coding tools, valuable MCP servers for knowledge work orchestration:

- **Google Drive** — Document access for content processing workflows
- **Slack** — Communication integration, notification patterns
- **Notion** — Documentation, project management integration
- **Linear/JIRA/Asana** — Issue tracking for task orchestration
- **Database connectors** — Direct data access for analysis workflows
- **Context7 MCP** — Real-time documentation injection (eliminates hallucinated APIs)
- **Claude Context MCP (Zilliz)** — Semantic codebase search with vector embeddings (~40% token reduction)

Configuration pattern: Use project-scoped `.mcp.json` (git-tracked) for team-shared servers; user-scoped `~/.claude.json` for personal integrations.

### GitHub Actions integration

The `anthropics/claude-code-action` provides isolated container environments enabling multiple agents working on different features simultaneously. Workflow patterns include:

- **@claude mentions** on issues/PRs for interactive assistance
- **Auto PR review** on pull_request events for continuous feedback
- **Issue triage and labeling** for automatic categorization  
- **Documentation sync** to auto-update docs when code changes

Key insight for orchestration: GitHub Actions containers provide natural isolation for parallel Claude execution at scale—enabling 20+ simultaneous feature implementations from issues without coordination overhead.

### Hooks automation patterns

**Common patterns**:
- Auto-formatting via PostToolUse on Edit/Write
- Security blocking via PreToolUse on Bash (block `rm -rf /`, force-push to main)
- Auto-approval via PermissionRequest for known-safe tools
- Context injection via SessionStart (load git status, recent issues)

**Prompt-based hooks** (`type: "prompt"`) use an LLM to evaluate allow/block decisions for complex scenarios where rule-based logic is insufficient.

---

## Part 5: Orchestration principles

### Plan Mode → Execution: the fundamental decomposition

Plan Mode represents a generalizable pattern for human-AI collaboration: **separating thinking from doing**.

**Phase structure**:
1. **Research Phase** (Plan Mode): Read-only operations—Gather comprehensive understanding through exploration + clarifying questions
2. **Design Phase**: Create implementation approach with dependencies/execution order
3. **Validation Checkpoint**: Human review and approval via ExitPlanMode tool
4. **Execution Phase**: Systematic task execution with tracking

**Generalizable principle**: Any agentic system benefits from separating research/analysis phases from action phases, with human checkpoints at transition points. For Oracle/execution engine architecture, the Oracle operates perpetually in a "Plan Mode equivalent"—strategic direction without direct action—while execution engines operate in auto-accept mode within their authorized scope.

Peter Steinberger offers an alternative: don't use formal Plan Mode—conversationally ask for a plan and write "build" when ready. This works better with models that follow instructions reliably without mode enforcement.

### Context engineering as the core discipline

Anthropic's official framing: "Context engineering is the natural progression of prompt engineering... curating and maintaining the optimal set of tokens during LLM inference."

**Four strategies** (LangChain framework):

1. **WRITE**: Save context outside the window for later retrieval (scratchpads, memory files, to-do lists)
2. **SELECT**: Choose what enters context window (RAG retrieval, targeted file loading via glob/grep)
3. **COMPRESS**: Reduce token count while preserving signal (summarization, compaction)
4. **ISOLATE**: Keep contexts separate (subagents with fresh windows)

**What should persist vs regenerate**:
- **Persist**: Architectural decisions, user preferences, project-specific knowledge, learned patterns
- **Regenerate**: Current file state, search results, intermediate reasoning, tool outputs

**Critical insight**: "Context failures are not model failures." Most agent errors trace to missing or corrupted context, not underlying model capability. For multi-Claude orchestration, context curation across instances becomes the primary engineering challenge.

### Subagent pattern for context isolation

Subagents provide **context isolation**—each explores extensively (potentially 10,000s of tokens) but returns only condensed summary (1,000-2,000 tokens) to the main thread.

**Orchestration patterns**:
- **Hierarchical/Supervisor**: Central orchestrator decomposes, delegates to specialists, aggregates
- **Parallel**: Independent agents work simultaneously on non-dependent tasks
- **Sequential/Pipeline**: Output of one feeds input of next
- **Group Chat**: Multiple agents collaborate through shared conversation

**For multi-Claude cognitive architecture**: The Oracle functions as supervisor agent—maintaining high-level context, issuing directives, receiving synthesized results. Claude Code instances function as domain specialists with isolated contexts. The challenge is the "reduce" step: synthesizing outputs from parallel specialists.

**Anti-pattern warning** (Shrivu Shankar): "If I make a PythonTests subagent, I've now hidden all testing context from my main agent. It can no longer reason holistically about a change." Subagents trade holistic reasoning for context efficiency—use them for genuinely separable concerns.

### When parallelization helps vs hurts

**Parallelization helps**:
- Independent subtasks with no data dependencies
- Time-sensitive scenarios requiring throughput
- Multiple perspectives needed on same problem
- Large-scale transformations across many files/documents

**Parallelization hurts**:
- Sequential dependencies required
- Shared mutable state
- Cumulative context needed (insights from A inform B)
- Resource constraints (API rate limits, token budgets)

**Coordination overhead pattern**: Different orchestration patterns vary by 200%+ in token consumption depending on coordination layers. Communication overhead, context duplication, synchronization points, and conflict resolution all consume resources.

**Task decomposition rule**: Size tasks to fit ~40% of context window per unit, map dependencies explicitly, match task types to agent capabilities, and establish clear completion criteria.

---

## Part 6: Anti-patterns and failure modes

### Known failure modes

**Infinite compaction loop**: Claude repeatedly reads same files, attempts compaction, restarts. **Recovery**: Press Esc to interrupt, `/clear`, start fresh session.

**Test death spiral**: Claude generates failing tests, then changes tests to match bad code. **Prevention**: Write tests first (TDD), be wary of test file changes, review test assertions carefully.

**Context confusion after compaction**: Claude becomes "dumber," forgets what it built. **Cause**: Compaction loses important details. **Recovery**: Use `/clear` more frequently, break into smaller tasks, use `/compact` manually at strategic points with focus instructions.

**Gives up early**: Claude stops working on complex tasks prematurely. **Cause**: Task too large for single context window. **Recovery**: Break into smaller separable tasks, provide more explicit guidance.

**Hook failure loop**: Stop hook fails repeatedly, prevents completion. **Recovery**: Fix hook configuration syntax, remove failing hooks.

### Anti-patterns from practitioners

**"PKM-style systems for systems' sake"** (Ben Springwater/Nabeel Qureshi): "90% of posts on X seem to be PKM-style creating systems for systems' sake... very few use cases that seem actually useful as opposed to just demonstrating 'what's possible'." Distinguish between architectural exploration and productive work.

**Skipping verification**: Boris Cherny's verification insight provides 2-3x quality improvement—skipping it is the single biggest mistake. Every workflow needs a validation mechanism.

**Overstuffing CLAUDE.md**: "It can be tempting to try and stuff every single command that claude could possibly need to run... We recommend against this." Distill to essentials; use linked documents for details.

**Running until context exhaustion**: "The hardest lesson: sometimes the path to better performance is artificial constraints. Stopping at 75% utilization feels wasteful... But that free space enables the reasoning quality that makes the utilized tokens valuable."

**Custom subagents hiding critical context**: Subagents trade holistic reasoning for efficiency—don't isolate concerns that need integrated reasoning.

### Security considerations for autonomous execution

`--dangerously-skip-permissions` bypasses ALL permission prompts. **Real risks**: file deletion without confirmation, cascade failures from misunderstood instructions, security hole creation, data exfiltration if network available.

**Safe patterns**: Docker/VM isolation (mandatory), AllowedTools whitelist even with bypass, git backup always, clear task scoping, failing tests first.

**Trust boundaries in multi-instance setups**: Each Claude Code instance shares `~/.claude.json` configuration. Multiple instances on same project can conflict—use git worktrees for isolation. Consider per-worktree `.claude/settings.local.json`.

**Enterprise security**: `disableBypassPermissionsMode: "disable"` prevents the flag entirely; managed MCP allowlists/denylists; forced login methods.

---

## Part 7: Evolution trajectory

### Recent development signals

| Period | Development | Significance |
|--------|-------------|--------------|
| Feb-Mar 2025 | Claude Code launch and GA | Research preview → 10x usage surge |
| May 2025 | Claude 4 (Opus 4, Sonnet 4) | "World's best coding model" positioning |
| Sep-Oct 2025 | Context management tools, Agent Skills API | Infrastructure maturation |
| Nov-Dec 2025 | Microsoft/NVIDIA partnerships, MCP → Linux Foundation | Ecosystem standardization, cross-cloud availability |
| Jan 2026 | Claude Code 2.1.0 | Infrastructure-level workflow features |

### Trajectory themes

**Infrastructure-ification**: Claude Code treated as infrastructure, not experiment. The SDK (`@anthropic-ai/claude-agent-sdk`) enables building custom agents programmatically. Native IDE extensions for VS Code and JetBrains indicate platform ambitions.

**Background execution**: GitHub Actions integration for autonomous PR handling signals movement toward always-on agents. Opus 4's ability to work "continuously for several hours" on complex tasks points toward longer autonomous operation.

**Ecosystem standardization**: MCP donation to Linux Foundation (with participation from OpenAI and Google) indicates industry convergence on tool integration protocols. This suggests Claude Code's extension patterns will generalize across AI platforms.

**Competitive positioning**: Claude available on all three major clouds (AWS, Azure, GCP)—unique among frontier AI models. This multi-cloud availability suggests Claude Code patterns may become infrastructure-layer defaults.

### What remains stable

**Enduring principles** regardless of feature evolution:

1. **Context is finite**: Regardless of window size, attention scarcity requires thoughtful curation
2. **Plan before execute**: Separating research from action improves outcomes across domains
3. **Hierarchical instructions**: Layered configuration (global → project → task) scales
4. **Human checkpoints**: Trust builds through graduated autonomy with validation gates
5. **Specialist isolation**: Subagent pattern preserves focus and context quality

**Pattern persistence**: Methods will improve but needs remain—compaction strategies, tool definitions requiring clarity/minimalism, external memory patterns, Supervisor/Parallel/Sequential orchestration fundamentals.

### Applying this to knowledge work orchestration

Claude Code's design validates the cognitive architecture described: strategic "Oracle" sessions issuing directives to execution engines. The patterns that work:

- **Hierarchical context via CLAUDE.md** scales to any persistent instruction need
- **Plan Mode discipline** applies to any domain requiring research before action
- **Subagent isolation** enables parallel execution without context pollution
- **Verification mechanisms** provide quality multipliers across domains
- **File-based handoffs** enable multi-instance coordination without complex protocols

The 75% context rule, compaction timing, and session continuity commands directly support the multi-Claude orchestration vision. The integration landscape (MCP for external tools, hooks for governance, GitHub Actions for isolated execution) provides the infrastructure layer.

The trajectory suggests these patterns will stabilize as industry defaults. What Claude Code teaches about agentic tool design—graduated autonomy, hierarchical configuration, context isolation, verification loops—will remain applicable whether the specific implementation is Claude Code, a successor, or a different platform entirely.

---

*This research synthesizes official Anthropic documentation, practitioner insights from Boris Cherny, Peter Steinberger, Dan Shipper, Zvi Mowshowitz, and community sources. Principles are framed for durability; specific features may evolve.*