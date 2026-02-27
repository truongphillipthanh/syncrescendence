# The Definitive Claude Code Guide

This guide synthesizes convergent patterns across practitioner reports, official documentation, and expert analyses. Where sources agree, unified principles emerge. Where productive tensions exist, they are preserved as control dials rather than false choices. The goal is not exhaustive documentation but distilled wisdom—the patterns that appear when independent practitioners converge on the same solutions.

---

## I. The Paradigm Shift: From Autocomplete to Orchestration Engine

The fundamental reconceptualization that separates productive Claude Code users from frustrated ones: you are no longer writing code. You are directing an autonomous execution engine that writes code. This requires a corresponding shift in where you apply your cognitive effort.

Claude Code is not a "copilot" where you drive and AI assists. It is an operating system process that you shape with durable state, tight feedback loops, and well-scoped autonomy. The context window is the entire project, not just open files. The filesystem becomes ground truth rather than the chat window.

The Operator Metaphor emerges across practitioners: Boris Cherny describes working as a "fleet commander" managing multiple Claude instances. Steipete notes he "doesn't read much code anymore" but instead watches streams and understands system architecture. Optimization moves from the artifact to the process.

Human-in-the-Loop versus Human-on-the-Loop captures the distinction. IDE integrations keep you in the loop—every keystroke flows through you. Claude Code puts you on the loop—you set direction, observe execution, intervene when needed.

| Human-in-the-Loop (IDE) | Human-on-the-Loop (Claude Code) |
|------------------------|--------------------------------|
| Single-file modifications | Multi-file orchestration |
| Real-time pair programming | Autonomous task execution |
| Immediate feedback cycles | Batch processing with verification |
| Context = open files | Context = entire project |

---

## II. The Prime Directive: Durable Cognition Over Ephemeral Cognition

Claude is brilliant in-the-moment and forgetful by default. The stable trick—repeated everywhere in different disguises—is to push anything you care about into durable artifacts that Claude can re-read:

Project norms and constraints live in CLAUDE.md and optionally modular rules folders. Work plans persist in plan files that act as external working memory. Work decomposition becomes Tasks with dependencies and validation. Progress checkpoints manifest as commits, PRs, issue references, codemaps, and changelogs.

Once you do that, the chat session becomes what it should have always been: a scratchpad for temporary reasoning, not the canonical record of truth.

This is why compounding engineering works: every failure gets transmuted into an instruction, a rule, a hook, a skill, or a test—something the agent can re-ingest next time without you repeating yourself.

---

## III. CLAUDE.md: The Highest Leverage Point

Every source in the corpus identifies CLAUDE.md as the critical configuration surface. It is not documentation—it is the constitutional foundation that shapes every interaction.

### The Hierarchy of Truth

Files load recursively upward from the working directory. Subdirectory CLAUDE.md files load on-demand when Claude accesses those paths.

1. **Enterprise/Global Policy**: `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) for organization-wide constraints
2. **User Memory**: `~/.claude/CLAUDE.md` for personal preferences across all projects
3. **Project Memory**: `./CLAUDE.md` at repository root, committed and team-shared
4. **Modular Rules**: `.claude/rules/*.md` for thematic breakdown that scales
5. **Local Overrides**: `./CLAUDE.local.md` gitignored for per-developer tweaks

### The Paradox of Less

Research converges on a counterintuitive finding: more instructions produce worse results. Frontier models reliably follow approximately 150-200 instructions; Claude Code's system prompt already consumes roughly 50. This leaves room for perhaps 100-150 project-specific rules before instruction-following degrades uniformly across all instructions.

Claude may ignore CLAUDE.md contents it deems "not highly relevant to the current task." The more irrelevant content you include, the more likely it ignores the relevant parts.

Target fewer than 300 lines, ideally fewer than 100. Include only universally applicable rules. Tell Claude why, not just what. Reference external docs rather than embedding them.

### What Belongs in CLAUDE.md

Include build commands, critical architectural constraints, project-specific gotchas discovered through iteration, technology stack and key dependencies, and how to verify changes.

Exclude code style rules (use linters and hooks instead), generic programming advice, task-specific instructions (use Skills or progressive disclosure), and exhaustive API documentation (let Claude search).

### The Compounding Engineering Pattern

CLAUDE.md should evolve through use, not be designed up front. Every source converges on this feedback loop: Claude makes a mistake, you correct it, you add a rule preventing recurrence, and future sessions benefit.

Boris Cherny's team tags `@claude` on PRs to update CLAUDE.md. The `#` key during sessions appends notes directly to the file. The result: CLAUDE.md becomes a living knowledge base that compounds value over time.

The anti-pattern is spending days crafting a "perfect" CLAUDE.md before using Claude Code. The reality: the model won't perfectly follow elaborate rulebooks. Iterate, don't architect.

---

## IV. Plan Mode: The Explore-Plan-Execute Discipline

Plan Mode is the most consistently recommended feature across all sources. Activated by Shift+Tab twice, it transforms Claude into a research and analysis engine that cannot modify files.

### The Workflow

The sequence runs: Explore by entering Plan Mode so Claude reads the codebase and understands context. Plan by requesting Claude produce a markdown checklist. Review by iterating on the plan with follow-up questions. Commit by writing the plan to a persistent file. Execute by exiting Plan Mode so Claude implements step-by-step. Verify by running tests, checking results, and updating the plan file.

### Why This Works

Separation of cognitive modes: LLMs perform better when planning and execution are isolated. Plan Mode uses Opus for deep reasoning; execution can switch to Sonnet for speed.

Checkpoint creation: A written plan survives context compaction. Even if the conversation is summarized, Claude can re-read the plan file and reorient.

Human veto opportunity: You review the approach before destructive changes. This prevents wild goose chase implementations where Claude dives into coding without understanding implications.

### When to Use Plan Mode

Any task touching more than three files. Architectural decisions. Complex refactors. Unfamiliar codebases. Debugging when root cause is unclear. Any change that is structural, risky, or ambiguous.

### The "Think" Hierarchy

The words in your prompt directly influence reasoning depth:

| Keyword | Reasoning Budget |
|---------|-----------------|
| "think" | ~4,000 tokens |
| "think hard" | Escalated |
| "think harder" | Further escalated |
| "ultrathink" | Maximum (~31,999) |

Don't ultrathink everything—the cost compounds. Reserve deep thinking for architectural decisions, novel algorithms, and genuinely complex reasoning. Simple tasks don't benefit from extended thinking.

### The Deeper Point

Plan Mode is essentially a structured prompt that enforces separation of deliberation from action. You can achieve this manually with a plan file, or via Plan Mode, or both. Ronacher's key point is that Plan Mode is mostly prompt scaffolding plus tool availability. Treat it as a convenience feature, not magic.

---

## V. Context Management: The Scarcest Resource

The 200,000 token context window is not free memory—it's a degrading resource. Quality begins to decline well before the limit is reached.

### The Compaction Problem

When context approaches capacity, Claude Code auto-compacts: it summarizes conversation history to free space. This process is lossy. Key decisions, constraints, and nuances may be lost in summarization.

The compaction death spiral unfolds: Context fills, auto-compact fires, Claude loses critical instructions, quality degrades, user provides more instructions, context fills faster, and the cycle repeats.

### Mitigation Strategies

**Strategy A: Proactive Manual Compaction**. Don't wait for auto-compact. Run `/compact` manually at logical breakpoints with explicit summarization directives: `/compact "Summarize the planning discussion, but preserve the list of 5 architectural constraints and the path to plan.md"`

**Strategy B: External State Persistence**. State must never reside solely in context. Write critical state to files: `plan.md` for current implementation plan, `decisions.md` for architectural choices, `SCRATCHPAD.md` for working notes. After compaction, Claude reads these files and reorients.

**Strategy C: Session Scoping**. One conversation per task. Don't build auth system and refactor database in the same session. Contexts bleed together; Claude gets confused.

**Strategy D: The Copy-Paste Reset**. When context is bloated: copy critical information from terminal, run `/compact` for summary, run `/clear` to wipe context, paste back only what matters. Fresh context with preserved state outperforms degraded context.

### Context Commands

`/context` shows token usage. `/compact [directive]` performs manual compaction with instructions. `/clear` executes nuclear reset while CLAUDE.md still loads. `/export` dumps conversation to markdown.

### The Real Win

The real win is to avoid depending on compaction at all: store the plan, constraints, and progress externally. Then you can safely reset, compact, or move between sessions without losing the plot.

---

## VI. Parallel Orchestration: The Fleet Commander Pattern

The signature pattern of power users: running multiple Claude instances simultaneously.

### The Basic Setup

Boris Cherny's configuration: 5 terminal tabs with local Claude Code instances, 5-10 web sessions on claude.ai/code, system notifications for attention-needed states, and git worktrees for isolation.

Why this works: Claude instances are often waiting—for your input, for test suites, for compilation. Parallelism fills these gaps with productive work on other tasks.

### Isolation via Git Worktrees

```bash
git worktree add ../project-alpha -b feature/auth
git worktree add ../project-beta -b feature/api
git worktree add ../project-gamma -b feature/tests
```

Each Claude instance operates in its own worktree. No file conflicts, no race conditions. Changes merge through normal git flow.

### Zone Ownership

For teams or complex orchestration, define exclusive write zones:

```yaml
alpha_agent:
  writable:
    - src/backend/
    - tests/backend/
beta_agent:
  writable:
    - src/frontend/
    - tests/frontend/
```

Orthogonal zones prevent merge conflicts. A central coordinator assigns tasks that respect zone boundaries.

### The Oracle Pattern

Hierarchical orchestration with a strategic planner:

1. **Oracle (Opus)**: Maintains master_plan.md. Does not edit code. Produces task files for workers.
2. **Workers (Sonnet/Haiku)**: Execute individual tasks. Report results. Update status.
3. **Feedback loop**: Oracle reads results, adjusts plan, issues new tasks.

Communication happens through files, not complex networking. The filesystem becomes a coordination bus.

### The 3 Amigos Pattern

Functional specialization across agent roles:

1. **PM Agent**: Context = requirements, PRDs. Output = specifications.
2. **UX Agent**: Context = design system. Output = mockups/prototypes.
3. **Dev Agent**: Context = codebase + specs + mockups. Output = code.

Linear handoff ensures the developer agent receives fully specified work, maximizing one-shot success probability.

### Subagents for Bounded Work

Delegate exploration, test writing, security review, refactor passes to subagents. Keep the main agent as the integrator. Spawn a reviewer subagent that independently checks work: "Create a code-review subagent that analyzes this PR for security issues and style violations without modifying any files." Separate context, fresh perspective.

### The Ralph Wiggum Loop

A script that loops Claude through a task list until completion. The archetype of "build while you sleep."

What makes it work: tasks are small, explicit, and have validation; each loop starts with a fresh or clean context; progress is committed to the repo, not stored in chat; the system stops only when all tasks validate.

Critical nuance: The loop must wipe context between iterations. Accumulating context leads to "context rot" where the model gets confused. A fresh start for every sub-task is superior to one long conversation.

Use Ralph when you want an overnight proof-of-concept machine. Don't use it as your only engineering process for high-stakes code without guardrails.

### The Integration Gate

Parallelize ruthlessly, but integrate conservatively. Boris-style "run 5 Claudes in parallel" is the throughput pattern. Worktrees, subagents, and multiple sessions amplify it.

But integration is a single narrow gate: CI plus tests plus review plus merge discipline. You can have ten brains exploring; you still want one bloodstream.

---

## VII. Verification Loops: The Self-Correction Imperative

The single most impactful pattern for quality: give Claude a way to verify its own work.

The golden rule: Never trust the agent's self-assessment.

### Test-Driven Development

The convergent recommendation: write tests first, commit them, let Claude implement until tests pass.

1. Write failing tests (or have Claude write them)
2. Commit the tests
3. Claude implements code
4. Tests run automatically
5. If tests fail → Claude reads output → Claude fixes → loop
6. Tests pass → task complete

This closes the feedback loop. Claude doesn't declare victory until success criteria are met.

### Define "Done" in Machine-Verifiable Terms

Every robust workflow adds explicit validation: tests, type checks, linting, formatting, smoke runs, browser automation, or at least concrete reproduction steps.

Where humans say "looks right", machines need "run X; expect Y". Tasks and Ralph-style loops make this explicit with validation steps and pass/fail flags.

### Hooks for Automated Verification

Configure hooks in `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.py)",
        "hooks": [
          {"type": "command", "command": "python -m black \"$file\""},
          {"type": "command", "command": "python -m pytest tests/"}
        ]
      }
    ]
  }
}
```

After every file write, formatters and tests run automatically. Errors surface immediately for Claude to address.

### The Browser Verification Pattern

For UI work, Claude can use the Chrome extension to control a browser: navigate to preview URLs, take screenshots, compare against mockups, iterate until visual match. Boris notes this verification loop improves final results by 2-3x.

### Add Signals or Your Agent Will Not Improve

In the "agents don't work" writings, the repeated critique is: retrieval and memory aren't enough without feedback loops.

In Claude Code, signals come from hooks, tests, CI outcomes, static analysis, runtime checks, user acceptance steps, and even postmortem notes appended to CLAUDE.md.

---

## VIII. Model Selection Strategy

Different models serve different purposes. The convergent pattern: use expensive models for thinking, cheap models for execution.

### The Opus-Sonnet Split

| Opus 4.5 | Sonnet 4.5 |
|----------|------------|
| Complex reasoning | Execution tasks |
| Architectural decisions | Boilerplate generation |
| Novel problem-solving | Routine implementation |
| Plan creation | Plan execution |

Practical workflow: Start session in Plan Mode with Opus. Generate plan. Switch to Sonnet for implementation. Your CLAUDE.md ensures both models follow the same constraints.

### When to Use Opus

Multi-step refactors. Debugging complex issues. Architectural trade-off analysis. Tasks requiring deep codebase understanding. Any situation where getting it right once beats multiple iterations.

### When to Use Sonnet/Haiku

Clear, well-specified tasks. Code generation from templates. Running tests and reporting results. Simple searches and file operations.

### Model in Subagents

Spawn subagents with appropriate models:

```javascript
{ "model": "haiku" }   // Fast tasks: running commands, simple searches
{ "model": "sonnet" }  // Most implementation work
{ "model": "opus" }    // Complex reasoning, architecture
```

---

## IX. The Permission Spectrum: Autonomy vs. Safety

A productive tension exists between speed (let Claude work uninterrupted) and safety (verify before destructive actions).

### The Allowlist Pattern

Pre-approve safe operations in `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Edit",
      "Read",
      "Glob",
      "Grep",
      "Bash(npm run:*)",
      "Bash(make:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(git push --force:*)"
    ]
  }
}
```

Routine operations proceed without prompts. Dangerous operations remain gated.

### The Petr Baudis Pattern

```
ask Bash --cmd '/\brm\b/'
ask Bash --cmd '/\bgit\b/'
ask Bash --cmd '/\bcurl\b/'
allow Bash --cmd '*'
```

Allow most commands, prompt only for truly dangerous patterns. This assumes Claude isn't actively adversarial—reasonable for most use cases.

### Dangerously Skip Permissions

`--dangerously-skip-permissions` removes all safety gates. Use only inside isolated containers, for automated pipelines, when human review happens post-execution, and never with network access on untrusted tasks.

---

## X. Extensibility: Skills, Commands, Hooks, MCP

Claude Code's Unix-philosophy architecture enables deep customization.

### Slash Commands

Saved prompts invoked by typing `/commandname`:

```markdown
<!-- .claude/commands/commit.md -->
---
name: commit-push-pr
description: Commit changes, push to branch, create PR
allowed-tools: Bash(git:*), Bash(gh:*)
---
1. Stage all changes
2. Generate semantic commit message from diff
3. Commit and push to current branch
4. Create PR using gh CLI with description from commit
```

Use for workflows you repeat daily. Boris runs `/commit-push-pr` dozens of times per day.

### Skills: Progressive Disclosure for Workflows

Skills are the "don't load it until you need it" mechanism. Passive knowledge that activates when relevant:

```markdown
<!-- .claude/skills/sql-expert.md -->
---
name: SQL Expert
description: When generating SQL queries, follow our database conventions
---
- Use parameterized queries only
- Follow our naming conventions: snake_case for tables, columns
- Always include WHERE clauses (no full table scans)
- Reference schema at @docs/schema.md
```

Claude proposes using relevant Skills when queries match the description. Skills inject context only when needed, preserving instruction budget.

In earlier workflows, people built slash commands in `~/.claude/commands` to inject context or run a workflow. The sources describe the merge: slash commands become callable as Skills, and Skills can be invoked with the `/` syntax.

A good skill is not a prompt snippet. It's a mini-protocol: purpose, prerequisites, steps, validation, and sometimes references to other files for layered context.

### Hooks: Enforcement, Telemetry, and "Don't Make Future-You Pay"

Hooks convert "please remember" into "the system guarantees."

**PreToolUse**: Run before any tool executes. Block dangerous operations, add validation. Include tmux reminders for long runs and warnings on risky commands.

**PostToolUse**: Run after tool completion. Format files, run tests, send notifications. This is the "last 10%" that avoids CI failures.

**PreCompact**: Summarization directives to preserve constraints and plan paths.

**Stop**: Intervene when Claude finishes a turn. The Ralph Wiggum pattern: prevent Claude from stopping if work isn't verified.

At a higher level, hooks are also how you get signals: they can log outcomes, nudge behaviors, and create consistent rhythms.

### MCP Servers

External tool integrations via Model Context Protocol:

GitHub for reading issues, creating PRs, posting comments, and reducing hallucinations about codebase state. Slack for searching messages and posting updates. Databases (Postgres/SQLite) allowing Claude to query real data to verify migrations or logic. Google Drive for fetching specifications. Sentry/Datadog for checking error logs and metrics. Browser (Puppeteer/Chrome) for end-to-end testing and visual verification.

Configure in `.mcp.json` or via `claude mcp add`. Claude discovers available tools dynamically via Tool Search lazy-loading—no need to preload all definitions, which explains why Claude can access many MCP tools without context bloat.

Tools are not free—every enabled capability taxes context. MCP servers and plugins add power but also expand the tool schema and steal context budget. The power users repeatedly emphasize disabling what you don't need.

---

## XI. The Task System: Dependency-Aware Orchestration

Claude Code's task system transforms flat to-do lists into structured workflows with dependencies, persistence, and parallel execution.

### Core Concepts

**Tasks have dependencies**: `#3 Create auth routes [blocked by #1, #2]`. Task #3 cannot begin until #1 and #2 complete. Dependencies are enforced, not advisory.

**Tasks persist**: Set `CLAUDE_CODE_TASK_LIST_ID` environment variable for cross-session persistence. Tasks survive compaction within sessions.

**Tasks enable parallelism**: Multiple subagents work the same task list. Each claims tasks by owner, marks progress, respects dependencies.

### Task Properties

The recurring properties across sources:

- identity (id)
- intent (subject/description)
- state (pending/in-progress/done)
- ownership (optional role/agent)
- dependency graph (blocks / blockedBy)
- optional metadata (priority/estimate/tags)

Tasks make projects legible to the machine. They are not a productivity ornament; they are an execution substrate. If you want the Ralph loop, Tasks are its native food.

### Example Workflow

"I want to add user authentication with email/password and OAuth"

Claude creates:
- #1: Investigate current auth patterns [no dependencies]
- #2: Design auth schema [blocked by #1]
- #3: Implement session storage [blocked by #2]
- #4: Create login/logout routes [blocked by #3]
- #5: Add OAuth providers [blocked by #3]
- #6: Write integration tests [blocked by #4, #5]

Claude works through tasks in dependency order, spawning parallel agents for tasks that can run simultaneously (#4 and #5 after #3 completes).

### When to Use Tasks

Multi-step work with 3+ steps. Anything with dependencies. Work spanning sessions. Complex refactors. Delegating to multiple agents.

### When Not to Use Tasks

Quick one-off questions. Single-file edits. Anything you'll finish in one shot.

---

## XII. Anti-Patterns: What Not to Do

### PKM for Its Own Sake

The warning from Zvi/Nabeel: much of what "feels productive" with Claude Code produces no valuable output. Organizing folders, churning through notes, creating elaborate systems for systems' sake—these activities demonstrate what's possible but don't ship work.

Test: Does this activity result in a tangible artifact (committed code, shipped feature, published document)?

### Over-Engineering the Process

Creating elaborate multi-agent orchestration systems before you've shipped a single feature with basic Claude Code. The tools should solve observed problems, not theoretical ones.

### Ignoring Context Degradation

Running 100K+ token sessions without compaction, wondering why Claude "forgot" earlier instructions. Context management is active discipline, not passive hope.

### Stuffing CLAUDE.md

Adding every conceivable rule, style guideline, and documentation snippet to CLAUDE.md. The result: Claude ignores most of it, and you can't predict which parts.

### Skipping Plan Mode

Jumping straight to implementation for complex tasks. This trades a 5-minute planning investment for hours of debugging and rework.

### Fighting the Model

Insisting on approaches the model handles poorly rather than reframing the problem. If Claude struggles after three explanations, changing the angle (different metaphor, different structure) often unlocks progress.

---

## XIII. Productive Tensions

These are areas where the field hasn't converged, and both approaches have merit. A mature workflow is not choosing one side; it's building the dial and knowing when to turn it.

### Opus Everywhere vs. Model Selection

Some practitioners (Boris, Steipete) use Opus for nearly everything, accepting higher cost for higher reliability. Others strictly optimize model selection per task. Your choice depends on cost sensitivity, task complexity distribution, and tolerance for iteration.

### Full Autonomy vs. Step-by-Step Verification

`--dangerously-skip-permissions` in sandboxed containers enables Claude to work uninterrupted for hours. But some practitioners prefer step-by-step approval even when it's slower. The right answer depends on risk tolerance, sandboxing capabilities, and task reversibility (can git reset undo mistakes?).

### Long Sessions vs. Fresh Context

Some maximize session length, relying on CLAUDE.md and external files to maintain coherence. Others prefer short sessions with explicit handoffs. Longer sessions accumulate context; shorter sessions avoid degradation. External state makes both approaches safe. No universal optimum exists.

### Compaction vs. Reset

Compaction is convenience; reset is clarity. The unifying solution is externalized state: if your plan and tasks are in files, you can reset context aggressively without losing orientation.

### Monolithic vs. Modular Instructions

One CLAUDE.md is simple; modular rules/skills scale better for large projects. Both work; choose based on project size and team needs.

### More Tools vs. Less Context

MCPs add reach but cost attention. Enable surgically.

### Bigger Tasks vs. Smaller Tasks

Big tasks feel efficient but cause failure cascades; small tasks are reliable but require coordination (Tasks).

### Slash Commands vs. Natural Language

Power users have dozens of slash commands. Others find typing "commit/push" just as fast as `/commit` and more flexible. Commands are valuable for complex sequences, less so for simple operations.

### Plan Mode vs. YOLO Mode

Plan Mode enthusiasts like the enforced read-only constraint and phased planning. YOLO (auto-approve) users prefer full autonomy and speed, and use handoff files as a manual planning scaffold.

A unified practice: Start in Plan Mode (or manual plan drafting) whenever the change is structural, risky, or ambiguous. Switch to auto-approve execution only after the plan is durable and validations are clear. When the context gets noisy, don't beg compaction to be smart—re-read the plan file and continue.

---

## XIV. Power-User Extensions

These show up less often, but they are coherent and useful.

### Custom File Suggestion Indexing for Huge Repos

For very large codebases, default file traversal can be slow; one pattern is to override file suggestion with a custom script that builds a local index (using FTS) and returns ranked results.

### GitHub Pages Branch Previews for Web Work

If you're driving Claude Code via the web/app and can't easily preview locally, deploy a `claude/...` branch to GitHub Pages for fast iteration and phone-based review.

### Meeting-to-PRD Pipelines

Record a conversation, transcribe it, then have Claude produce: documentation, backlog tasks, decisions with rationale, and linked notes (Obsidian-style). This turns collaboration exhaust into project structure.

### RAG Over Your Own Chat History

Treat your past sessions as a dataset: retrieve, summarize, find patterns, and generate personal process improvements. This is meta, but it's how you get compounding learning at the human layer too.

### Building Codebases for Agent Navigation

Steipete's insight: you build codebases for agent navigation, not human navigation. Code organization, naming conventions, and documentation structure should optimize for how Claude reads and understands the system.

---

## XV. A Practical Ontology of Claude Code

Across the corpus, the same entities keep showing up. This minimal map makes everything else predictable:

**Surfaces (where you drive it):** terminal CLI; Claude Code on the web; desktop/mobile wrappers.

**Sessions (the ephemeral layer):** what Claude has in its context window right now. Powerful, but perishable. Subject to compaction and degradation as it grows.

**Durable memory (the project constitution):** CLAUDE.md plus any additional "always on" rule files.

**Progressive disclosure (optional context on demand):** Skills (which now unify the old slash command concept). These let you keep context out of the window until you need it.

**Automation rails (mechanical enforcement):** hooks that fire on lifecycle events to format, test, warn, summarize, or enforce constraints.

**Work decomposition (coordination):** Tasks (newer primitive) or task lists in plan files; can encode dependencies, ownership, and status.

**Parallelism (throughput):** multiple concurrent Claude instances; subagents; git worktrees; explicit handoffs/teleporting between sessions.

**Tooling extensions (reach):** MCP servers and plugins that connect Claude to external systems.

If you keep those separate in your head, most "what should I do?" questions reduce to: Is this ephemeral reasoning, durable memory, optional context, enforcement, coordination, throughput, or reach? Put it in the right bucket.

---

## XVI. The Daily Practice

A synthesis of recommended workflows from across the corpus.

### Session Start

1. Review CLAUDE.md for any needed updates
2. Check current branch and working state
3. Define the session's goal clearly
4. Enter Plan Mode for non-trivial tasks

### During Work

1. Let Claude explore before coding
2. Write plans to external files
3. Verify changes run tests
4. Compact proactively at logical breakpoints
5. Use `#` to add learnings to CLAUDE.md
6. Interrupt early when heading wrong direction (Esc)

### Session End

1. Run final verification
2. Commit work with meaningful messages
3. Update session state files if continuing later
4. Note any CLAUDE.md updates needed

### Weekly Review

1. Prune outdated CLAUDE.md rules
2. Evaluate slash command usage
3. Check for repeated corrections → new rules
4. Update documentation from decisions.md

---

## XVII. The Canonical Workflow (One Loop to Rule Most Work)

Here's a unified loop that subsumes most corpus patterns:

1. **Orient**: Claude reads CLAUDE.md, scans the repo structure, and identifies the relevant files.

2. **Plan**: A plan is written to a durable file (often PLAN.md). The plan includes: goal and non-goals, files to touch, step sequence, validation steps, risk notes.

3. **Decompose**: Convert the plan into Tasks (or an equivalent task table) with dependencies and verification.

4. **Execute in small increments**: Claude implements one task at a time, running validations after each.

5. **Enforce mechanically**: PostToolUse hooks format and run quick checks; CI catches what local checks miss.

6. **Integrate**: Commit with meaningful messages; open a PR; keep diffs reviewable.

7. **Compound**: When something surprises you (a mistake, a convention mismatch, a repeated annoyance), update CLAUDE.md (norms), a Skill (reusable workflow), a hook (enforcement), or a test (correctness).

That last step is what makes tomorrow faster than today.

---

## XVIII. A Minimal Starter Constitution

If you do nothing else, implement these in this order:

1. A solid CLAUDE.md that covers stack, repo map, commands to run, style rules, and how we validate.
2. A plan file habit: write PLAN.md before execution on non-trivial work.
3. A formatting hook plus a fast check hook (typecheck/lint/tests) so CI failures become rare.
4. A small set of Skills for your most common workflows (refactor pass, add tests, PR prep, release checklist).
5. Worktrees for parallelism once you're doing multi-threaded work.
6. Only then: expand MCP/plugin footprint.

---

## XIX. The Meta-Principle

The practitioners who extract the most value from Claude Code share one characteristic: they treat the development process itself as something to be engineered. They iterate on their workflow as carefully as their code. They invest in CLAUDE.md, hooks, and commands as deliberately as they invest in test infrastructure.

The corpus does not converge on "the perfect prompt." It converges on something more annoying and more powerful: Treat your agent workflow like engineering. Build the rails. Encode the rules. Automate the checks. Externalize the state. Create feedback loops.

Claude Code is not a tool to be mastered once. It's a capability to be continuously refined. The compounding engineering pattern applies not just to CLAUDE.md but to your entire approach: every friction point, every repeated correction, every workflow bottleneck is an opportunity for systematic improvement.

Do that, and Claude Code stops being a toy you steer and becomes a system you operate.

The guides, workflows, and patterns in this document are starting points. Your optimum configuration will emerge through use—through the unique intersection of your domain, your preferences, and your codebase. The only universal advice: keep refining.

---

## Quick Reference

### Essential Commands

| Command | Function |
|---------|----------|
| `Shift+Tab` (x2) | Toggle Plan Mode |
| `Esc` | Interrupt current action |
| `Esc Esc` | Edit previous prompt |
| `#` | Append to CLAUDE.md |
| `/compact [directive]` | Manual compaction |
| `/clear` | Reset context |
| `/context` | Show token usage |
| `/permissions` | Manage tool allowlist |
| `/help` | List available commands |

### Thinking Levels

| Keyword | Reasoning Budget |
|---------|-----------------|
| "think" | ~4,000 tokens |
| "think hard" | Escalated |
| "think harder" | Further escalated |
| "ultrathink" | Maximum (~31,999) |

### File Hierarchy

```
~/.claude/CLAUDE.md         # User global (personal preferences)
./CLAUDE.md                 # Project (committed, team-shared)
./.claude/rules/*.md        # Modular project rules
./CLAUDE.local.md           # Local overrides (gitignored)
./.claude/commands/*.md     # Custom slash commands
./.claude/skills/*.md       # Passive knowledge
./.claude/settings.json     # Runtime configuration
./.mcp.json                 # MCP server definitions
```

### Configuration Pattern

```json
{
  "permissions": {
    "allow": ["Edit", "Read", "Bash(npm run:*)"],
    "deny": ["Bash(rm -rf:*)"]
  },
  "hooks": {
    "PostToolUse": [
      {"matcher": "Write(*.py)", "hooks": [{"type": "command", "command": "black $file"}]}
    ]
  }
}
```

### Glossary

**Context window:** the tokens Claude can "see" right now; gets noisy as it fills.

**Compaction:** summarization of conversation to free space; useful but lossy.

**Plan Mode:** a prompt scaffold enforcing phased planning and read-only behavior until a plan is written.

**YOLO / auto-approve:** maximum autonomy for tool usage; fast but riskier.

**CLAUDE.md:** durable instruction file auto-loaded per session; your project constitution.

**Skill:** a reusable, on-demand workflow/context package; callable via `/`.

**Hook:** event-triggered automation around tool usage or session lifecycle.

**Subagent:** a delegated agent process with bounded scope/tools.

**MCP:** protocol/servers that connect Claude to external services/tools.

**Worktree:** git mechanism for multiple working directories/branches in parallel.

**Tasks:** dependency-aware work decomposition primitive for long projects.

**Ralph Loop:** autonomous execution cycle that works through task lists with context resets.

---

*This guide synthesizes patterns from: Anthropic official documentation, Boris Cherny's workflow revelations, Zvi Mowshowitz's analysis, Eyad Khrais's production practices, Steipete's inference-speed shipping, HumanLayer's CLAUDE.md research, the Gemini architectural analysis, Ronacher's Plan Mode deep dive, Numman Ali's task system documentation, and numerous practitioner reports across the corpus.*
