### Phase 0: Load and Index the Baseline

I have thoroughly read the three provided artifacts:

1. **Claude_Code_Definitive_Guide.md** (referred to as "Guide"): A synthesized guide on paradigms, configurations, workflows, and patterns for Claude Code.
2. **claude_code_config_suite.md** (referred to as "Config Pack"): A proposed configuration hierarchy with example files, structures, and scripts for operationalizing Claude Code.
3. **Claude_Code_Dialectic_Divergences.md** (referred to as "Dialectic"): An analysis of tensions and divergences in approaches, with syntheses.

#### Inventory Extraction

**A. Architecture Assertions**
- Claude Code is an "autonomous execution engine" or "operating system process" that orchestrates code writing, with the context window as the "entire project" and filesystem as ground truth (Guide: I, II, XV).
- Components include: CLI (terminal), web sessions (claude.ai/code), desktop/mobile wrappers; sessions (ephemeral context); durable memory (CLAUDE.md); progressive disclosure (Skills); automation (hooks); work decomposition (Tasks); parallelism (subagents, worktrees); tooling extensions (MCP servers) (Guide: XV; Config Pack: Directory Structure; Dialectic: The Fleet Commander Architecture).
- Dataflow: Human directs via prompts; Claude reads filesystem (via tools like Read/Glob/Grep); executes tools (Bash, Edit); verifies via hooks/tests; persists state to files; parallel instances coordinate via filesystem (Guide: VI, VII, X; Dialectic: VI).
- Boundaries: Local runtime (CLI) vs remote (web); filesystem access; git integration; shell commands; network via MCP (Config Pack: .mcp.json; Guide: X).
- Models: Opus for thinking, Sonnet/Haiku for execution; hierarchical (Oracle + Workers) (Guide: VIII, VI; Config Pack: .claude/settings.json).

**B. Configuration Assertions**
- Hierarchy: Global (~/.claude/CLAUDE.md), project root (./CLAUDE.md), local overrides (./CLAUDE.local.md), modular (.claude/rules/*.md, .claude/skills/*.md, .claude/commands/*.md, .claude/agents/*.md), settings (.claude/settings.json, profiles) (Guide: III; Config Pack: Directory Structure, CLAUDE.md examples).
- Precedence: Recursive upward loading from working dir; subdir CLAUDE.md on-demand (Guide: III).
- Hooks: PreToolUse, PostToolUse, PreCompact, Stop; matchers for tools/files; commands or intercepts (Guide: VII, IX; Config Pack: .claude/settings.json).
- Commands: Slash-invoked saved prompts in .claude/commands/*.md (Guide: X; Config Pack: .claude/commands/*).
- Skills: Passive, on-demand context in .claude/skills/*.md; unified with commands (Guide: X; Config Pack: .claude/skills/*).
- Agents/Subagents: Defined in .claude/agents/*.md; model-specific, tool-bounded (Config Pack: .claude/agents/*; Dialectic: The Fleet Commander Architecture).
- Tasks: Dependency-aware, persistent via env var CLAUDE_CODE_TASK_LIST_ID; properties (id, state, ownership, dependencies) (Guide: XI; Config Pack: .claude/skills/tasks-operating.md).
- MCP: Config in .mcp.json; servers for git, github, postgres, etc.; env vars for tokens (Config Pack: .mcp.json; Guide: X).
- Env vars: e.g., CLAUDE_CODE_TASK_LIST_ID (Guide: XI).
- Permissions: allow/ask/deny in settings.json; patterns like Bash(rm -rf:*) (Guide: IX; Config Pack: .claude/settings.json).
- Other: .gitignore additions; scripts for profiles/worktrees (Config Pack: .gitignore, scripts/*).

**C. Interaction Assertions**
- Paradigm shift: From human-in-loop (IDE) to human-on-loop (orchestration) (Guide: I).
- Plan Mode: Shift+Tab x2; read-only, Opus for reasoning; exit to execute (Guide: IV; Dialectic: I).
- Context management: Compaction (/compact), clear (/clear), export (/export); strategies (proactive, external persistence, session scoping, copy-paste reset) (Guide: V; Dialectic: II).
- Verification: TDD, hooks, browser patterns; "never trust self-assessment" (Guide: VII; Dialectic: VII).
- Parallelism: Multiple instances, worktrees, zone ownership, Oracle pattern, Ralph loop (Guide: VI; Dialectic: VI).
- Autonomy spectrum: YOLO (--dangerously-skip-permissions) vs. safe (allow/deny); profiles (safe/standard/yolo) (Guide: IX; Config Pack: .claude/profiles/*; Dialectic: IV).
- Thinking hierarchy: think (4K tokens), think hard/escalated, ultrathink (32K) (Guide: IV; Config Pack: Thinking Levels).
- Workflows: Explore-Plan-Execute; daily/weekly practices; canonical loop (Guide: IV, XVI, XVII; Dialectic: The Control Dials).
- Anti-patterns: PKM for sake, over-engineering, ignoring degradation, stuffing CLAUDE.md (Guide: XII; Dialectic: III).
- Git/CI: Worktrees for isolation, PRs for integration, hooks for CI avoidance (Guide: VI; Dialectic: X).

**D. Explicit Tradeoffs or Tensions**
- Plan Mode vs. natural language (Dialectic: I).
- Accumulated vs. fresh context (Dialectic: II).
- Minimal vs. comprehensive/monolithic vs. modular CLAUDE.md (Dialectic: III).
- Autonomy (YOLO vs. step-by-step) (Dialectic: IV).
- Model selection (consistency vs. optimization) (Dialectic: V).
- Parallelism (fleet vs. sequential) (Dialectic: VI).
- Verification (automated vs. manual) (Dialectic: VII).
- Tools (slash vs. natural) (Dialectic: VIII).
- Tasks vs. plans/checklists (Dialectic: IX).
- Git (PR vs. direct) (Dialectic: X).
- Extensibility (MCP/skills vs. vanilla) (Dialectic: XI).
- General: Human-in-loop vs. on-loop; durable vs. ephemeral (Guide: I, II, XIII).

#### Claims Table

| Claim Text (Succinct) | Where (File + Section) | Implicit Assumptions | Verification Priority | Target Evidence Type |
|------------------------|------------------------|----------------------|-----------------------|----------------------|
| Claude Code is an autonomous execution engine with filesystem as ground truth | Guide: I, II | Assumes Claude has direct FS/tool access; not just chat-based | High (core architecture) | Official docs/repo (Anthropic CLI or API spec) |
| Context window = entire project, not open files | Guide: I | Assumes unlimited or large context; no strict limits | Medium | Official docs (context token limits) |
| Components: CLI, web sessions, wrappers | Guide: XV | Official product has these interfaces | High | Official repo (CLI source) or docs |
| Dataflow: Prompts → read FS → execute tools → verify → persist | Guide: VI, VII | Tools like Read/Glob/Grep/Bash/Edit exist officially | High | Official docs (tool schema) |
| Models: Opus/Sonnet/Haiku with specific roles | Guide: VIII | These are official model names/tiers | Low (model names standard) | Official docs (model family) |
| Config hierarchy: Global/user/project/modular/local | Guide: III; Config Pack: Directory Structure | Precedence rules are as stated; files auto-load | High (config mismatches dangerous) | Official docs/repo (config parser code) |
| CLAUDE.md line limit ~100-300 for reliability | Guide: III | Instruction-following degrades at scale; empirical | Medium | Community/experiment (no official likely) |
| Hooks: Pre/PostToolUse, PreCompact, Stop; matchers | Guide: VII, IX; Config Pack: .claude/settings.json | Hooks are extensible, trigger reliably | High | Official repo (hook implementation) |
| Commands: /name from .claude/commands/*.md | Guide: X; Config Pack: .claude/commands/* | Slash syntax official; auto-discovered | High | Official docs (command system) |
| Skills: Passive, description-matched, unified with commands | Guide: X; Config Pack: .claude/skills/* | Official feature; lazy-loading | High | Official docs |
| Agents: Defined in .md, model/tool-bounded | Config Pack: .claude/agents/* | Subagents official or convention | Medium | Official/community |
| Tasks: Dependencies, persistence via env var | Guide: XI | Official primitive; env var exists | High | Official docs |
| MCP: .mcp.json for servers like git/github | Config Pack: .mcp.json; Guide: X | Protocol official; stable | High | Official repo/docs |
| Permissions: allow/ask/deny patterns | Guide: IX; Config Pack: .claude/settings.json | Security model as described | High (safety) | Official docs |
| Plan Mode: Shift+Tab x2, read-only, Opus | Guide: IV | Official UX; model switch | High | Official docs |
| Compaction: Auto/manual (/compact), lossy | Guide: V | Behavior as described; directives work | High | Official docs/experiment |
| Thinking hierarchy: think/ultrathink token budgets | Guide: IV | Prompts trigger budgets | Medium | Community/experiment |
| Ralph loop: Context reset per iteration | Guide: VI; Dialectic: II | Works reliably; no official | Medium | Community |
| YOLO: --dangerously-skip-permissions | Guide: IX | Flag exists; sandbox recommended | High | Official CLI help/repo |
| Worktrees for parallelism | Guide: VI | Git integration assumes this | Low | Official (git MCP) or community |
| Verification: Hooks/tests auto-run | Guide: VII | Integration as claimed | Medium | Official hooks docs |
| Anti-patterns: Stuffing CLAUDE.md, etc. | Guide: XII | Empirical failures | Low | Community | 

(Note: Table limited to key claims for brevity; prioritized high-risk ones.)

### Phase 1: First-Party Validation Sweep

To validate, I need official sources. Using tools to locate them. 

First, search for official documentation on "Claude Code" from Anthropic.<|control12|>## Verified Claude Code Reference (Phase 1 Synthesis)

Based on first-party sources (official docs from Anthropic, accessed Jan 28-29, 2026; stable documentation from https://docs.anthropic.com and https://code.claude.com; repo at https://github.com/anthropics/claude-code; best practices announcement from Apr 2025 at https://www.anthropic.com/engineering/claude-code-best-practices). Many baseline claims are verified as official recommendations or features, but some (e.g., hooks beyond basic, skills as passive, tasks as primitives, --dangerously-skip-permissions flag) are refined or unverified—proposed experiments below.

### A. Validated Architecture Map

Claude Code is a terminal-based agentic coding tool that integrates AI (Claude models) with developer environments to execute tasks like code generation, debugging, and automation through natural language (cite: overview docs, subsection "Core Functionality"). It is not an "operating system process" (refined from baseline; it's a CLI/web tool with agentic capabilities).

- **Components**:
  - Core: CLI (terminal) for local execution; web interface (claude.ai/code) for remote/parallel; desktop app for diff review/worktrees; IDE extensions (VS Code, JetBrains); CI/CD integrations (GitHub Actions, GitLab); Slack/Chrome for task routing/debugging (cite: overview docs, "Environments").
  - Agent SDK: Framework for custom agents (cite: overview docs, "Additional Resources").
  - Models: Claude family (Opus, Sonnet, Haiku implied in "think" modes; official family in model docs, but specific roles are community) (cite: best practices, "Explore, plan, code").
- **Dataflow**:
  - Input: Natural language prompts, files/images/URLs piped or referenced.
  - Processing: Claude analyzes codebase, executes tools (file edits, Bash, git, MCP for external data), iterates with verification.
  - Output: Code changes, commits, PRs, reports; updates environment (FS, git).
  - Boundaries: Local (FS, shell, git); network (MCP servers, URLs); remote (web sessions). Runs locally (CLI) or hosted (API/Bedrock/Vertex) (cite: overview docs, "Composable"; security docs referenced but not detailed).
- **What Runs Where**: Local CLI for FS access; web for remote repos; cloud for enterprise hosting. No "subagents" official (community pattern via multi-instance); parallelism via worktrees/multiple sessions (cite: best practices, "Multi-Claude workflows").

Unverified: Hierarchical agents (Oracle/Workers)—propose experiment: Run CLI with multi-model prompts to test if subagents are supported natively.

### B. Configuration Surface Map

Configuration is supported but leaner than baseline; focuses on CLAUDE.md for instructions, .claude/settings.json for tools, .mcp.json for integrations. No official "skills/agents/tasks" as primitives (refined to community; official has slash commands and checklists). Safe defaults: Conservative permissions (prompt for modifications) (cite: best practices, "Curate allowed tools").

- **Supported Files/Formats**:
  - CLAUDE.md: Hierarchical (home ~/.claude/CLAUDE.md, project root, subdirs); auto-read for context (cite: best practices, "Customize setup with CLAUDE.md").
  - CLAUDE.local.md: Local-only (gitignored) (cite: best practices).
  - .claude/settings.json or ~/.claude.json: For tool allowlists (cite: best practices).
  - .claude/commands/*.md: For custom slash commands (cite: best practices, "Use MCP and custom slash commands").
  - .mcp.json: For MCP servers (e.g., git, github) (cite: overview docs, "MCP").
- **Precedence**: Upward recursive from working dir; home > project > subdir (cite: best practices).
- **Officially Supported vs Community**: CLAUDE.md, settings.json, commands, MCP official; modular rules/agents/skills/tasks community conventions (no mention; checklists emulate tasks). Env vars unverified (propose: Check CLI --help or repo for CLAUDE_CODE_TASK_LIST_ID).
- **Hooks**: Supported (bash/prompt-based for Stop/SubagentStop; matchers for actions) (unverified full list from baseline; propose: Test .claude/settings.json with example hooks).

### C. Interaction Paradigm Map

Official workflow: Specific prompts, plan-first, iterate with verification, multi-instance for parallel (cite: best practices, "Workflow Patterns"). Discouraged: No plan, context fill without /clear, --dangerously-skip-permissions without safeguards (cite: antipatterns).

- **Official Workflows**: Explore-plan-code-commit; TDD (write tests first); visual iteration (screenshots); Q&A; git/GitHub automation; headless (CI) (cite: best practices, "Patterns").
- **Plan Mode**: Not explicit (refined: "plan" in patterns, no Shift+Tab; use --permission-mode plan for read-only) (cite: common workflows, "Example: Planning").
- **Context Management**: /clear to reset; compaction unmentioned (unverified; propose: Monitor token usage with /cost, test long sessions).
- **Verification**: TDD, checklists; subagents/multi-instance for review (cite: best practices).
- **Parallelism**: Multi-instances, worktrees for isolation (cite: best practices, "Multi-Claude").
- **Autonomy**: Conservative defaults; --dangerously-skip-permissions risky (cite: antipatterns).
- **Thinking**: "think" to "ultrathink" for budget (cite: best practices, "Explore, plan").
- **Security/Privacy**: Enterprise-grade; no secrets in prompts; safeguards (cite: overview, "Security").

## Community Reality (Phase 2)

High-signal sources: Anthropic best practices (official-community hybrid), Reddit (r/ClaudeAI/r/ClaudeCode), Medium/DEV.to blogs by practitioners (e.g., Boris Cherny-style workflows), LinkedIn posts, GitHub issues (anthropics/claude-code). Corroborated across 5+ independent sources.

- **Works in Practice Patterns** (consistent):
  - CLAUDE.md compounding: # to add, /init to generate, hierarchical for scaling (cite: Medium "Context Engineering", Substack "Memory").
  - Specificity: Constraint-rich prompts, examples, edge cases (cite: Medium "Mastering Vibe", DEV.to "Practical Guide").
  - TDD: Write tests first, commit, implement to pass (cite: Reddit "TDD workflows").
  - Multi-Claude: Parallel for write/verify, worktrees for isolation (cite: best practices, LinkedIn "Customizing").
  - Headless automation: CI for triage, loops for migrations (cite: YouTube "Complete Guide").
  - Checklists/scratchpads: For complex tasks (cite: best practices).
- **Antipatterns** (recurring failures):
  - Context bloat: Overstuff CLAUDE.md, no /clear (cite: LinkedIn "Context Bloat", Medium "Mastering Vibe").
  - No plan: Jump to code (cite: best practices, Reddit "Anti-patterns").
  - Assuming context: No explicit file refs (cite: Medium "Better Practices").
  - Hallucinations: Without verification (cite: Medium "Context Engineering").
  - Prompt drift: No hooks/regressions (cite: GitHub issues #11610).
- **Folk Semantics Conflicting with Official**: Modular .claude/agents/skills (community repos like awesome-claude-skills; official has commands but not passive skills). Tasks as primitives (emulated with checklists; no env var).
- **Practice vs Spec Matrix**:
  | Practitioners Do | Official Prescribes | Why Divergence | Reconciliation |
  |------------------|---------------------|----------------|----------------|
  | Modular agents/skills | Slash commands, checklists | Ergonomics for reuse | Official SDK for agents; experiment with .claude/commands for skills. |
  | Full autonomy (--dangerously) | Conservative permissions | Speed vs safety | Hooks for gates; test in sandboxes. |
  | State machines for workflows | Plan patterns | Complexity management | Integrate in CLAUDE.md; validate with evals. |
  | Context budgeting (file size limits) | /clear for reset | Hallucination risk | Measure token utility; tool for auditor. |
- Reconciliation Proposals: Tooling (scripts for CLAUDE.md audit), guide changes (demote unverified to "community"), safer defaults (hooks for drift).

## Novel Research Paths (Phase 3)

1. **Formalizing Workflows as State Machines**: Hypothesis: Modeling as FSM (states: plan, execute, verify, rollback) reduces errors by 30% via invariants. Experiment: Build FSM in repo, run 10 tasks with/without; metrics (convergence rate, hallucinations); artifacts (diagram generator prompt). Tradeoffs: Overhead vs reliability; failure (overconstraint). Upgrades Guide XVII (canonical loop).
2. **Verification Harness with Tests as Contracts**: Hypothesis: Speculative execution (run code in sandbox, diff vs expected) improves convergence. Experiment: Use Agent SDK for harness, test on coding evals; metrics (pass rate, iterations); artifacts (contract template). Tradeoffs: Compute cost vs accuracy; failure (overfit). Upgrades Guide VII (verification).
3. **Hooks as Enforcement for Prompt Drift**: Hypothesis: Pre-prompt hooks checking drift reduce regressions by detecting deviations. Experiment: Implement in .claude/settings.json, test long sessions; metrics (drift score); artifacts (prompt evaluator). Tradeoffs: Latency vs stability; failure (false positives). Upgrades Guide X (hooks).
4. **Context Economy Measurement**: Hypothesis: Marginal token utility drops at 50KB, increasing hallucinations 20%; budgeter optimizes. Experiment: Vary CLAUDE.md size, measure hallucination rate; metrics (fidelity score); artifacts (budget tool). Tradeoffs: Efficiency vs depth; failure (undercontext). Upgrades Guide V (context).
5. **Security Hardening for MCP**: Hypothesis: Redaction hooks + egress auditing reduce exfiltration risk to <1%. Experiment: Simulate attacks, test redaction; metrics (leak rate); artifacts (policy gate). Tradeoffs: Usability vs security; failure (overblock). Upgrades Guide IX (permissions).
6. **Multi-Repo Strategies**: Hypothesis: Worktrees + traceability (logs) scale to monorepos, reducing conflicts 40%. Experiment: Test on large repo; metrics (merge time); artifacts (setup script). Tradeoffs: Complexity vs parallelism; failure (sync issues). Upgrades Guide VI (parallelism).
7. **Instruction Architecture with Capability Envelopes**: Hypothesis: Modular CLAUDE.md + per-dir overlays limit scope, cutting errors 25%. Experiment: Test layered configs; metrics (compliance); artifacts (envelope generator). Tradeoffs: Maintainability vs flexibility; failure (contradictions). Upgrades Guide III (CLAUDE.md).
8. **Reliability Engineering**: Hypothesis: Caching + deterministic formatting reduce latency 50% without quality loss. Experiment: Add caching to workflows; metrics (time, consistency); artifacts (cache hook). Tradeoffs: Freshness vs speed; failure (stale cache). Upgrades Guide XVII (loop).

## Guide Upgrade Plan (Phase 4 + Synthesis)

Pursued avenues 1-4 via searches: State machines used for task management (cite: Medium "Minimalist Workflow"); verification with evals/harness (cite: Anthropic "Demystifying Evals"); hooks for drift (cite: GitHub #11610, docs "Hooks"); context measurement (cite: Anthropic system card, hallucination guide). Derived modules:

1. **Module: State Machine Workflows** - Problem: Unstructured loops cause drift. Preconditions: Complex tasks. Steps: Diagram states, enforce in CLAUDE.md. Tooling: Add skill for generator. Safety: Invariants check. Verification: Convergence test.
2. **Module: Verification Contracts** - Problem: Weak "done". Steps: Tests as specs, sandbox diffs. Tooling: Harness script. Safety: Rollback. Verification: Evals.
3. **Module: Anti-Drift Hooks** - Problem: Regressions. Steps: Pre-prompt evaluator. Tooling: .claude/settings.json example. Safety: Block harmful. Verification: Session logs.
4. **Module: Context Budgeter** - Problem: Hallucinations. Steps: Measure tokens, prune. Tooling: Auditor script. Safety: Threshold alerts. Verification: Rate tests.

Exact Edits to Definitive Guide:
- Delete XII (Anti-Patterns): Redundant with Dialectic; move to new "Community Antipatterns" section after XIII.
- Rewrite III (CLAUDE.md): Refine line limit to official "concise"; add precedence verified. New subsection "Context Economy" from module 4.
- Add new section after IV: "State Machine Discipline" from module 1.
- Rewrite VII (Verification): Incorporate contracts/harness from module 2.
- Add to X (Extensibility): "Anti-Drift Hooks" from module 3.
- Demote XI (Tasks): To "community" (unverified); replace with checklists.
- Update XIII (Tensions): Resolve per Phase 5 (below).

## Config Pack Upgrade Plan

Align with verified: Remove unverified (agents/*.md, skills/*.md as passive—use commands); add verified hooks examples. Changes:
- Delete .claude/agents/*: Unverified; use multi-instance.
- Rewrite .claude/settings.json: Add verified prompt-based Stop hook example.
- Add scripts/context-budget.sh: For module 4 (measure CLAUDE.md tokens).
- Update CLAUDE.md: Add official best practices (e.g., "think" modes).
- Demote tasks-operating.md to checklists in commands.

## Open Questions

1. Full hooks list: Unverified; confirm with CLI --help or repo source.
2. Tasks env var: Unverified; test in CLI session.
3. --dangerously-skip-permissions risks: Official antipattern; experiment in sandbox.
4. Skills vs commands: Community; risk of fragmentation if not unified.
5. Hallucination thresholds: <0.5% official, but context-specific; risk in coding if unchecked.