# The Claude Code Dialectic: Reasoning Through Divergent Approaches

This document isolates the recurring fault lines across the research corpus—places where credible practitioners recommend different operating styles. The goal is not to pick a winner globally but to understand what each side optimizes for, what it sacrifices, and how to compose a framework that preserves the useful tensions without turning your workflow into theology.

Where the corpus is explicitly contradictory, the dialectic is treated as real rather than averaged away. The debates are not disagreements to resolve but dimensions to navigate.

---

## I. Plan Mode: Structured UX vs. Natural Language Planning

### Thesis: Plan Mode as Essential Discipline

The majority position treats Plan Mode as foundational. Anthropic's official guidance, Boris Cherny's workflow, Eyad Khrais's production practices, and the "Mastering the Vibe" article all recommend Plan Mode as the default for non-trivial work. Shift+Tab twice, iterate until the plan is good, then switch to execution/auto-accept for near one-shot implementation.

**Arguments for structured Plan Mode:**

Separation of cognitive modes improves output quality. The mode forces checkpoint creation before destructive changes. The UI transition creates a psychological commitment to planning. Human review opportunity exists before implementation begins. The plan file survives context compaction. No edits occur until explicit approval—a strong safety property.

### Antithesis: Plan Mode as UX Overhead

Armin Ronacher's investigation reveals Plan Mode is "just a prompt" with "some UX around it." The core difference from natural language planning: system reminders that it's read-only, tool restrictions, and a workflow for exiting to implementation.

**Arguments against structured Plan Mode:**

You can achieve identical results by asking Claude to write a plan.md file. Natural language planning gives you a visible, editable file you control. The Claude-integrated experience hides the plan "in a folder you never see." Some agents (pi, Amp) are removing their plan modes entirely. The UX friction may be unnecessary for experienced users. Conversational planning optimizes for flow and speed, but depends more on model obedience and user vigilance.

Ronacher's workflow: iterate with the agent on creating a markdown handoff file, answer clarifying questions in an editor, refine until satisfied—all without mode switching.

### Synthesis

The debate reveals Plan Mode's value lies not in the mechanism but in the forcing function. The question is whether you need external structure to impose planning discipline.

Plan Mode's benefits are behavioral, not technical. If you naturally write detailed plans before implementation, natural language achieves the same result. If you tend to jump straight to coding, Plan Mode's constraints prevent that pattern.

Treat Plan Mode as a risk gate, not a religion. When the work is cross-cutting, destructive, or ambiguous, Plan Mode is cheap insurance. When the task is tight and reversible, conversational planning is sufficient—provided you still externalize state and maintain verification.

**Decision framework:**

Use Plan Mode if you catch yourself skipping planning phases, or if working in teams where consistent process matters. Use natural language planning if you're disciplined about explicit plan creation and want more control over file location and naming. Either way: The plan must be written to a persistent file, not held only in context.

---

## II. Context Management: Accumulated State vs. Fresh Start

This is one of the most explicit debates in the corpus.

### Thesis: Accumulated Context with Smart Compaction

The default Claude Code approach and most practitioner guidance assumes long sessions with accumulated context. State builds up; compaction summarizes when needed; external files provide persistence anchors. Several sources advocate proactive manual `/compact` at logical breakpoints, with a summarization directive that preserves constraints and pointers to state files. Some claim compaction quality has materially improved, including notes that "v2.1.3 solved the compaction issue" when combined with Plan Mode and comprehensive to-do anchoring.

**Arguments for accumulated context:**

Maintains conversational continuity and nuance. Allows complex multi-step reasoning across many turns. Compaction (done well) preserves essential decisions. External files rescue critical state from compaction loss. Familiar interaction paradigm from chatbot experience. Compaction can function like a review pass—re-reading code and catching bugs.

### Antithesis: Fresh Context Every Loop (The Ralph Pattern)

The Ralph Wiggum approach inverts this entirely: wipe context after every single task. Each iteration starts fresh. No compaction, no growing memory files.

**Arguments for fresh context:**

Models demonstrably degrade as context fills—"the whiteboard gets cluttered." Compaction is lossy; the AI guesses what's important and often guesses wrong. Fresh starts mean maximum reasoning capacity applied to each task. Eliminates the "compaction death spiral" entirely. The difference between a $30 correct implementation and a $300 broken mess can depend on this choice.

Jeff Huntley's canonical Ralph: one bash while loop, static prompt, clean task list, fresh start every iteration. Nothing grows between loops except task completion flags. The critique of compaction is brutal: the model doesn't reliably know what's important; it guesses, and the wrong guess compounds.

### Synthesis

These approaches optimize for different work types:

| Accumulated Context | Fresh Context |
|---------------------|---------------|
| Exploratory work | Well-specified tasks |
| Ambiguous requirements | Clear acceptance criteria |
| Iterative refinement | Batch execution |
| Human-in-the-loop | Autonomous operation |
| Continuity matters | Throughput matters |

The choice depends on whether the task's value comes from accumulated understanding or focused execution. Architectural exploration benefits from context accumulation. Implementing a task list benefits from fresh starts.

**State Externalization resolves the tension.** Do not rely on chat history (compacted or otherwise) for project state. Treat the chat window as ephemeral RAM. Treat the filesystem as the hard drive.

**Implementation:** Before clearing context or compacting, force the agent to dump its current status into a structured file. When the fresh session starts, the first instruction is to read that file. This combines the freshness of a wiped window with the continuity of compaction.

**Two-tier compaction policy:**

Interactive sessions: proactive manual compaction at phase boundaries, but only after writing/refreshing external state. Unattended loops (Ralph-like): reset by default, and treat external artifacts as the single source of truth. If you cannot afford rigorous external state, you cannot afford unattended loops.

**Decision framework:**

Use accumulated context for planning phases, research, ambiguous problems, and work requiring iterative refinement with human judgment. Use fresh context loops for execution phases with well-specified tasks, overnight batch processing, and autonomous operation. Hybrid: Plan with accumulated context (where continuity helps), then execute with fresh context loops (where focus helps).

---

## III. CLAUDE.md: Minimal vs. Comprehensive, Monolithic vs. Modular

### Thesis: Minimal, Hand-Crafted CLAUDE.md

Humanlayer's research argues for fewer than 100 lines. The reasoning: models follow approximately 150-200 instructions reliably; Claude Code's system prompt uses roughly 50; every additional instruction competes for attention and degrades uniformly when limits are exceeded.

**Arguments for minimal CLAUDE.md:**

Preserves instruction-following capacity for user prompts. Forces ruthless prioritization of truly universal rules. Claude may ignore contents deemed "not highly relevant." Avoids diluting critical instructions with noise. Hand-crafting ensures every line earns its place.

### Antithesis: Comprehensive Documentation

Some approaches suggest CLAUDE.md should contain extensive project documentation, style guides, architectural context.

**Arguments for comprehensive CLAUDE.md:**

New team members benefit from extensive context. Reduces repeated explanations across sessions. Documentation and agent instructions serve dual purposes. Some complex projects genuinely require extensive context.

### Cross-Cutting Tension: Monolithic vs. Modular

**Pole A: One shared CLAUDE.md (team-level, frequently updated).** Boris describes a single team CLAUDE.md checked into git, with compounding engineering: anytime Claude does something incorrectly, add it to CLAUDE.md.

**Pole B: Modular rules (includes, subdirectory CLAUDE.md, domain ownership).** Other sources advocate splitting rules into multiple files so different owners maintain different domains (frontend style, security constraints), and using subdirectory CLAUDE.md files to provide local context only where needed.

A monolith optimizes for discoverability ("there is one constitution"). It fails under merge conflicts and entropy. Modular governance optimizes for scaling and locality, but risks fragmentation and contradictions. Minimalism improves salience and reduces token tax; maximalism increases coverage but dilutes attention and increases compaction risk.

### Synthesis

The research converges against comprehensive CLAUDE.md. The debate is really about where comprehensive context should live. Progressive disclosure solves this. CLAUDE.md contains pointers; detailed documentation lives in referenced files that Claude reads on-demand.

**Architecture:**

```
CLAUDE.md (< 100 lines)
├── Project overview and purpose
├── Build/test commands  
├── Critical constraints (the "gotchas")
└── Pointers to detailed docs
    ├── @docs/architecture.md
    ├── @docs/style-guide.md
    └── @docs/schema.md
```

**Adopt a layered constitution:** A short root CLAUDE.md with invariants, safety rules, repo-wide workflow, and references. Domain-owned modular docs (included or linked) for deep specifics. Subdirectory CLAUDE.md only when local context truly differs. Keep the root file legible in one sitting, and push depth outward.

**Decision framework:**

Always keep CLAUDE.md minimal, focused on universally-applicable rules. Always use progressive disclosure for detailed context. Never auto-generate CLAUDE.md—it's the highest leverage point. Always hand-craft every line; if you can't justify a rule, remove it.

---

## IV. Autonomy: YOLO Mode vs. Step-by-Step Verification

### Thesis: Maximum Autonomy in Sandboxes

`--dangerously-skip-permissions` combined with containerization enables fully autonomous operation. Claude works uninterrupted; human reviews results after completion.

**Arguments for full autonomy:**

Eliminates permission prompt fatigue. Enables overnight/background operation. Maximizes Claude's throughput. Containers limit blast radius. Git enables rollback of mistakes.

### Antithesis: Active Collaboration with Verification

Other practitioners prefer reviewing each significant action, treating Claude as a junior developer requiring supervision.

**Arguments for step-by-step verification:**

Catches mistakes before they compound. Maintains human understanding of changes. Appropriate for production systems. Some decisions require human judgment. Easier to course-correct early.

### Synthesis

The appropriate autonomy level depends on three factors:

**Reversibility:** Can mistakes be easily undone? Version-controlled code has high reversibility—more autonomy acceptable. Production database has low reversibility—step-by-step required.

**Blast radius:** What's the worst-case outcome? Sandboxed container has limited blast radius—more autonomy acceptable. Access to credentials or production has large blast radius—verification required.

**Task specification quality:** How well-defined is success? Clear acceptance tests mean high specification—autonomous execution appropriate. Ambiguous requirements mean low specification—iterative collaboration needed.

**Sandboxed Autonomy with Guardrails:** Use Plan Mode for the architectural phase (high-level decisions). Use autonomous loops for the implementation phase (writing functions, passing tests), but only within a strictly defined sandbox or git worktree. Configure allowedTools in settings.json to whitelist safe commands while requiring prompts for dangerous ones. Use git worktrees to isolate the autonomous agent so it cannot break the main branch.

**Graduated autonomy as operating system:** Default: allow-list routine edits and safe commands; prompt for anything destructive or networked. High-risk: Plan Mode plus explicit approvals. Sandbox runs: skip permissions acceptable only with isolation, backups, and automated validation gates.

**Decision framework:**

High autonomy: Sandboxed execution + version control + clear acceptance criteria + reversible actions. Low autonomy: Production systems + irreversible actions + ambiguous requirements + security-sensitive operations. Hybrid: Autonomous execution within sessions, human approval at phase boundaries (PR review, deployment gates).

---

## V. Model Selection: Consistency vs. Optimization

### Thesis: One Model for Everything

Boris Cherny uses "Opus 4.5 with Thinking" exclusively. Steipete uses "gpt-5.2-codex high" for nearly everything. Both report productivity benefits from consistency.

**Arguments for single-model simplicity:**

Reduces decision overhead—no time spent choosing models. Builds intuition for one model's behavior patterns. Eliminates context-switching cognitive load. Higher-capability models reduce iteration even for simple tasks. Getting it right once beats multiple iterations. Opus with thinking, though slower per step, reduces steering and tool errors and is often faster overall.

### Antithesis: Task-Appropriate Model Selection

Other practitioners (MinChoi's supervisor pattern, various sources) advocate matching model to task: Haiku for simple commands, Sonnet for implementation, Opus for architecture.

**Arguments for model selection:**

Cost optimization can be 10-50x for equivalent results. Speed optimization—Haiku responds faster for simple tasks. Some tasks genuinely don't benefit from deep reasoning. Parallelism is cheaper with smaller models. API users face real budget constraints.

### Synthesis

The economics differ dramatically between subscription and API users:

**Subscription users (Claude Pro Max at $200/month):** Marginal cost of model selection is near zero. Time spent choosing models has real cost. Consistency wins unless hitting rate limits.

**API users (pay per token):** Model selection has direct financial impact. Opus at $75/M output tokens vs. Haiku at $1.25/M = 60x cost difference. Selection overhead pays for itself quickly.

Select model by uncertainty and blast radius. High uncertainty or high risk: pay for thinking. Low uncertainty, reversible edits: cheaper model is fine, but keep verification gates.

**Decision framework:**

Subscription users: Default to your best available model; don't optimize prematurely. API users: Build selection into workflow—lightweight router or explicit task typing. Either way: Don't ultrathink simple tasks; the reasoning budget has cost even on subscription.

---

## VI. Parallelism: Fleet Commander vs. Sequential Focus

### Thesis: Multi-Agent Orchestration

Boris Cherny runs 5 terminal tabs + 5-10 web sessions. Molly Cantillon runs 8 parallel instances. The "fleet commander" metaphor treats development as real-time strategy.

**Arguments for parallel agents:**

Exploits wait times (thinking, testing, building). Throughput scales with orchestration skill. Different tasks can proceed independently. Web + local enables "cloud bursting." Matches the economics of AI labor.

### Antithesis: Sequential Deep Work

Some practitioners find coordination overhead exceeds benefits. Others note that parallel agents create merge conflicts, require zone ownership discipline, and demand substantial orchestration skill.

**Arguments for sequential focus:**

Simpler mental model. No merge conflict management. No zone ownership complexity. Deep context on one problem. Lower skill floor.

### Synthesis

Parallelism has diminishing returns and increasing overhead:

| Parallel Instances | Overhead | When Appropriate |
|-------------------|----------|------------------|
| 1 | None | Learning, small tasks |
| 2-3 | Low | Independent features |
| 5-8 | Moderate | Skilled orchestrators with worktree discipline |
| 10+ | High | Teams with explicit zone ownership, mature tooling |

Parallelism is a skill that develops over time. Starting with 8 agents creates chaos; building up from 2 allows skill development.

Run parallel agents only when outputs are separable and mergeable (research variants, independent modules, test generation, doc drafting). Use shared artifacts (task list, plan file, constraints) as the coordination bus. When outputs are entangled, prefer sequential execution with explicit checkpoints.

**Implementation:** Never run multiple agents on the same folder. Use `git worktree add` to create isolated environments for each agent. Use the CLI to start heavy tasks, then `--teleport` them to the Web interface if you need to free up your local machine.

**Decision framework:**

Start sequential: Learn Claude Code's behavior with focused attention. Add parallelism gradually: 2 agents → 3 → 5 as orchestration skill develops. Prerequisites for parallelism: Git worktrees, zone ownership, notification system. Know your limit: If coordination overhead exceeds productivity gains, scale back.

---

## VII. Verification: Automated Hooks vs. Manual Review

### Thesis: Automated Verification via Hooks

PostToolUse hooks run formatters, linters, and tests automatically after every change. PreToolUse hooks can block dangerous operations.

**Arguments for automated verification:**

Catches issues immediately. No human attention required for routine checks. Consistent application of standards. Enables autonomous operation. Compounds with every edit. Turns agents from "clever autocomplete" into something closer to an engineer.

### Antithesis: Manual Verification for Control

Some practitioners prefer reviewing changes directly, maintaining human understanding of what's happening.

**Arguments for manual verification:**

Human judgment catches issues automation misses. Maintains understanding of codebase evolution. Appropriate skepticism of AI output. Not all checks can be automated. Hooks can fail silently, slow the loop, or become a brittle maze.

### Synthesis

These aren't mutually exclusive. The question is which checks deserve automation and which require human judgment.

**Automate:** Formatting (always deterministic). Linting (well-defined rules). Unit tests (fast, deterministic). Type checking (algorithmic verification).

**Human review:** Architectural decisions. Security implications. User-facing behavior changes. Integration correctness.

**Verification tiers:** Prototype tier: lightweight checks (formatting, typecheck). Feature tier: unit tests + lint. Release tier: integration/e2e + human review. Make hooks enforce the tier automatically; do not rely on "remembering" to run tests.

Use hooks sparingly and only for high-leverage invariants: formatting, lint, test, secret scanning, and "do not touch" constraints. Treat hook configuration as production code: version it, test it, and keep it minimal.

**Decision framework:**

Automate deterministic checks: If a rule can be expressed algorithmically, automate it. Reserve human review for judgment: Decisions requiring context, trade-offs, or domain knowledge. Layer both: Automated hooks catch mechanical issues; human review catches conceptual issues.

---

## VIII. Tools: Slash Commands vs. Natural Language

### Thesis: Slash Commands for Efficiency

Power users create extensive command libraries. Boris runs `/commit-push-pr` dozens of times daily. Commands encode common workflows into single invocations.

**Arguments for slash commands:**

Muscle memory speed for frequent operations. Guaranteed consistent prompt structure. Shareable across team members. Documentation of standard workflows. Arguments allow parameterization.

### Antithesis: Natural Language Flexibility

Steipete finds "commit/push" just as fast as `/commit` and more flexible. Natural language adapts to variations without command modification.

**Arguments for natural language:**

No command maintenance overhead. Handles edge cases without predefined logic. Faster for one-off variations. Lower learning curve. Models understand intent regardless of phrasing.

### Synthesis

Commands and natural language serve different workflow shapes:

| Slash Commands | Natural Language |
|----------------|------------------|
| Highly repetitive operations | Variable operations |
| Multi-step sequences | Simple requests |
| Team standardization | Individual exploration |
| Operations needing arguments | Context-dependent requests |

**Decision framework:**

Create a command when you do something more than 3x daily with consistent structure. Use natural language for variable operations or first-time requests. Don't over-invest: If you're creating commands you rarely use, stop. Review periodically: Remove commands that haven't been used in weeks.

---

## IX. Tasks System vs. Plans/Checklists

### Thesis: The Tasks System (Dependency Management, Persistence, Agent Assignment)

The corpus highlights Tasks as a move beyond flat to-do lists: explicit blocking dependencies, persistence across compaction and even across sessions via a task list ID, and coordination for parallel workers.

**Arguments for Tasks:**

Optimizes for complex graphs of work: prerequisites, parallel assignment, progress visibility, and orchestration that the agent can't "forget." Tasks make projects legible to the machine. They are not a productivity ornament; they are an execution substrate. If you want the Ralph loop, Tasks are its native food.

### Antithesis: Plain PLAN.md / Checklist Files

Many practitioners have long used PLAN.md or SCRATCHPAD.md as the external working memory and coordination bus. A plan file is universal, versionable, and tool-agnostic.

**Arguments for plan files:**

Optimizes for simplicity and portability. Universal format readable by humans and any tool. No new surface area: config, identifiers, or systems to keep sane. The failure mode is that the model treats them as "suggestions" unless you actively enforce updates and completion criteria.

### Synthesis

Use Tasks when the work genuinely has dependency structure or multi-agent parallelism. Use PLAN.md when the work is linear. Hybrid is often strongest: Tasks as the orchestration layer, PLAN.md as the narrative spec and state anchor that survives across tooling and humans.

**Decision framework:**

Use Tasks for: Multi-step work with dependencies. Work spanning sessions. Delegating to multiple agents. Complex graphs requiring explicit blocking. Use PLAN.md for: Linear sequences. Simple projects. Portability across tools. When Tasks add more complexity than value.

---

## X. Git Discipline: PR-Centric vs. Direct-to-Branch

### Thesis: PR-First, Reviewable Increments

Boris describes using Claude in code review by tagging @.claude to update CLAUDE.md and fix issues as part of PR flow. PRs provide auditability and team safety.

**Arguments for PR discipline:**

Creates reviewable, auditable history. Enables team collaboration and review. Forces meaningful commit boundaries. Makes rollback clear and simple. Integrates with CI/CD pipelines.

### Antithesis: Direct Iterative Hacking

Many practitioners operate fast locally, then consolidate. Direct iteration is fast but increases risk of "mystery state."

**Arguments for direct iteration:**

Maximizes speed during exploration. Reduces ceremony during prototyping. Allows rapid experimentation. Consolidation can happen later.

### Synthesis

Treat git as the recovery substrate. For any agentic run of non-trivial scope, produce reviewable commits on a branch. Even solo, this keeps a crisp trail and makes rollback cheap.

**Decision framework:**

PR discipline for: Team work. Non-trivial scope. Production-bound code. When auditability matters. Direct iteration for: Solo prototyping. Exploratory work. When speed matters more than history. Always: Commit frequently enough to enable rollback.

---

## XI. Extensibility: MCP/Skills vs. Staying Vanilla

### Thesis: Extend Claude with MCP and Skills Packages

MCP is positioned as the standard for connecting agents to tools and data; Skills as portable bundles of instructions/scripts/resources that can be discovered and reused.

**Arguments for extensibility:**

Unlocks deep integration (tickets, docs, CI, knowledge bases). Enables workflows impossible with vanilla setup. Skills provide progressive disclosure. MCP standardizes tool connections.

### Antithesis: Keep Configuration Light

Boris explicitly describes his setup as surprisingly vanilla: minimal customization, lean on defaults, add only what compounding engineering reveals.

**Arguments for vanilla:**

Claude is useful out of the box. Extensibility multiplies failure modes: auth issues, prompt injection risk via tool outputs, cognitive overhead. Simpler systems are more reliable. Every extension is maintenance burden.

### Synthesis

Earn complexity. Start vanilla, then add one integration at a time when there is a clear, repeated pain. Prefer "read-only" integrations first. Promote integrations to "write" capability only behind strong permissions and verification.

**Decision framework:**

Default vanilla: Use built-in capabilities first. Add incrementally: One integration at a time for observed repetition. Read before write: Start with read-only integrations. Permission gate writes: Promote to write capability only with verification. Remove unused: If an integration hasn't been used in weeks, remove it.

---

## The Definitive Solution: A Unified Operating Model

The synthesis is not a single "best" workflow. It's a control system with dials. The corpus converges on a meta-principle:

**You are not prompt-engineering; you are designing a socio-technical control loop.**

### The Control Dials

**Risk / Blast Radius:** How bad is a wrong action?

**Novelty / Uncertainty:** How unclear is the solution path?

**Scope / Entanglement:** How many parts of the system are coupled?

**Horizon:** Will this survive across days/sessions/agents?

**Verification Strength:** Can the agent prove correctness?

These dials determine the right settings for the debated axes.

### Recommended Defaults (The Stable Middle)

Use these as a baseline profile:

Start complex work in Plan Mode; simple work can be conversational. Externalize state: PLAN.md + progress updates + constraints (root CLAUDE.md). Manual compaction at phase boundaries; never let auto-compaction surprise you mid-thought. Allow-list safe tools; never skip permissions outside isolation. Verification hooks: format + lint + tests appropriate to the repo. PR/branch discipline for any meaningful agent run. Parallelism only when outputs are separable; coordinate through artifacts. Keep CLAUDE.md short and constitutional; push depth into modular docs. Introduce MCP/Skills incrementally based on observed repetition.

### Two Specialized Profiles

**Profile A: Overnight / Ralph-like Loop (Unattended Automation)**

Reset per task. Strict external state. Sandbox isolation. Automated checks. Final human review gate. If you can't externalize rigorously, do not run unattended.

**Profile B: Rapid Prototyping / Vibe Mode**

Conversational planning. Permissive allow-lists for reversible edits. Light verification. Fast iteration. Explicitly time-box it, and promote into the Stable Middle profile when it becomes real software.

### The Fleet Commander Architecture

**The Constitution (Memory Architecture):**

Root CLAUDE.md contains only the Prime Directives (Project Goal, Tech Stack definitions, File Structure map). Max 100 lines. Dynamic Skills in `.claude/skills` allow the agent to pull context only when needed. State Files maintain a `status.md` or `plan.md` in the root. The agent must update this file before every context clear/compaction.

**The Operational Loop (The Architect-Builder Protocol):**

Phase 1 The Architect (Opus 4.5 + Plan Mode): Trigger via Shift+Tab x2. Task is to define the Spec. No code is written. The output is a checklist in plan.md. Human role is to approve the plan.

Phase 2 The Builder (Sonnet 4.5 + Auto-Accept): Trigger by switching model to Sonnet (faster/cheaper). Task is to execute the plan. Use a sub-agent loop or Ralph loop to iterate on tests until green. Human role is Fleet Commander—monitor via notifications while running parallel tabs.

**The Safety Harness (Permissions and Hooks):**

Do not use `--dangerously-skip-permissions` globally. Do configure `.claude/settings.json` to allow `ls`, `grep`, `cat`, and `git diff` without asking. Implement a PostToolUse hook that runs a linter/formatter after every file edit. This prevents the agent from wasting tokens fixing its own syntax errors.

**Scaling (Parallelism):**

Worktrees: Never run multiple agents on the same folder. Use `git worktree add` to create isolated environments for each Agent. Handoffs: Use the CLI to start heavy tasks, then `--teleport` them to the Web interface if you need to free up your local machine.

### The State Triangle (Minimal Artifact Set)

To keep dialectical complexity from metastasizing, standardize on three files:

**CLAUDE.md:** Invariants, workflow, "never do X," tool permissions guidance.

**PLAN.md (or SPEC.md):** Current intent, checklist, decisions, acceptance criteria.

**PROGRESS.md (or CHANGELOG.md):** What changed, what's next, what's blocked.

If you adopt Tasks, it becomes a fourth corner—but PLAN.md remains the narrative anchor.

---

## Implementation Sequence

**Phase 1: Make state durable.** Create the State Triangle. Run `/init`, then delete ruthlessly.

**Phase 2: Make correctness cheap.** Add the lightest verification hooks that catch 80% of mistakes (format/typecheck/test).

**Phase 3: Make autonomy safe.** Move from prompting-based safety to allow-lists and Plan Mode gates.

**Phase 4: Make throughput real.** Add parallelism and/or Tasks only after artifacts + verification are stable.

**Phase 5: Make it compound.** Every repeated mistake becomes a rule (CLAUDE.md) or automation (hook/command/skill).

---

## Summary Table: When to Use What

| Situation | Recommended Approach |
|-----------|---------------------|
| Learning Claude Code | Plan Mode, sequential, step-by-step |
| Exploratory research | Accumulated context, natural language, manual review |
| Well-specified implementation | Fresh context loops, autonomous, parallel |
| Production systems | Step-by-step verification, minimal autonomy |
| Frequent operation (>3x/day) | Slash command |
| One-off request | Natural language |
| Subscription user | Model consistency |
| API user | Task-appropriate model selection |
| Simple project | Minimal CLAUDE.md (<50 lines) |
| Complex project | Progressive disclosure from minimal CLAUDE.md |
| Linear work | PLAN.md |
| Dependency graphs | Tasks system |
| Team collaboration | PR discipline, modular CLAUDE.md |
| Solo prototyping | Direct iteration, conversational planning |

---

## The Meta-Principle

The corpus does not converge on a single workflow because no single workflow is optimal. The skill is recognizing which approach fits the current situation and switching fluidly between modes.

**The practitioner's progression:**

1. Start with structured approaches (Plan Mode, sequential focus, step-by-step verification)
2. Build intuition for when structure helps vs. hinders
3. Selectively relax constraints as skill develops
4. Maintain structured approaches where they add genuine value
5. Recognize that context determines optimal approach

The debates in the corpus are not disagreements to resolve but dimensions to navigate. Mastery comes not from picking a side but from developing the judgment to apply each approach in its appropriate context.

### The Final Dialectical Claim

The corpus is arguing about surface features (Plan Mode, compaction, tasks), but the deeper disagreement is this:

**Do you want the agent's intelligence to come from a continuously-extended conversation, or from a well-instrumented environment that forces it to behave intelligently?**

The strongest solution forward is the second: build the environment so intelligence is structural, not merely performed.

This solution resolves the tensions by acknowledging that Claude is not a chatbot; it is a stochastic operating system. It requires file-system-based memory (not chat memory), role-based workflows (Architect vs. Builder), and strict resource management (Progressive Disclosure).
