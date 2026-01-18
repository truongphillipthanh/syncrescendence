# CLAUDE CODE + ANTHROPIC ECOSYSTEM: DEEP RESEARCH PROMPT

## Research Objective

Conduct comprehensive research into Claude Code and the broader Anthropic/Claude ecosystem to understand: (1) core capabilities and architecture, (2) emergent usage patterns from practitioners, (3) generalizable principles for orchestrating AI-augmented workflows, and (4) integration patterns across the Anthropic product surface. This research informs the design of a multi-agent coordination system where Claude Code serves as primary execution engine.

---

## Research Context

This research is being conducted for someone building a **cognitive architecture for AI-augmented knowledge work** — not a traditional software development workflow. The interest is in Claude Code as:

- An **execution engine** for multi-Claude orchestration (3+ Claude accounts coordinating)
- A **repository-integrated assistant** that maintains persistent project context
- An **automation platform** for knowledge work (not just code generation)
- A **model for understanding** how agentic AI tools are designed and can be extended

The use case involves orchestrating strategic synthesis sessions ("Oracles") that issue comprehensive directives to Claude Code instances for parallel execution. The workflow spans content processing, knowledge base maintenance, documentation generation, and eventually automation scripting — with actual software engineering as a later-stage concern.

---

## Primary Research Questions

### 1. Architecture & Capabilities

- What is Claude Code's core architecture? How does it differ from IDE integrations like Cursor/Windsurf?
- What are the actual tool capabilities available to Claude Code? (file operations, bash, web search, subagents, MCP)
- How does context management work? What triggers compaction? How much context degrades performance before the 200K limit?
- What is the relationship between Claude Code CLI, Claude Desktop integration, and claude.ai/code web interface?
- How do Skills, Plugins, and MCP servers interact? What's the capability surface for extending Claude Code?

### 2. Session & Memory Management

- How does CLAUDE.md work hierarchically? (Enterprise → Project → User → Local → Subdirectory)
- What persists across sessions? (CLAUDE.md, settings.json, named sessions, Skills)
- How does `/compact` work? What survives compaction? What are best practices for Plan Mode + compaction?
- How do named sessions, `/resume`, `/teleport`, and `--continue` interact for session continuity?
- What's the relationship between Claude Code's session memory and the web app's "memory" feature?

### 3. Workflow Patterns from Practitioners

- What patterns do power users employ? (Boris Cherny's setup, MinChoi's optimization, parallel instances)
- How are teams using CLAUDE.md as a "learning" mechanism? (Compounding Engineering pattern)
- What are the friction points practitioners have solved? (permission fatigue, context bloat, verification failures)
- What distinguishes productive workflows from "PKM-style systems for systems' sake"?
- How do practitioners handle the "Plan Mode → execution" handoff?

### 4. Multi-Instance Orchestration

- How do practitioners run 5-10 Claude instances in parallel? (terminal tabs, web sessions, hybrid)
- What coordination patterns exist for multi-Claude workflows? (zone ownership, worktrees, handoffs)
- How does the `&` prefix for web handoff work? How does `--teleport` work?
- What are the limits of parallelization? When does coordination overhead exceed benefit?

### 5. Integration Landscape

- How does Claude Code compare to Cursor's Claude integration? When would you use each?
- What MCP servers are most valuable? (GitHub, filesystem, Google Drive, Slack)
- How do hooks (PreToolUse, PostToolUse) enable automation? What are common patterns?
- What's the state of Claude Code's GitHub Actions integration? (@.claude on PRs)
- How does Claude Code on Desktop differ from CLI? What features are Desktop-only?

### 6. Generalizable Principles

- What principles from Claude Code workflows generalize to AI-augmented knowledge work?
- What does "Plan Mode → execution" teach about human-AI task decomposition?
- How do CLAUDE.md patterns inform persistent context engineering across any AI tool?
- What does the compaction problem teach about context window management strategies?
- How does the "subagent" pattern inform multi-agent orchestration design?

---

## Secondary Research Questions

### Advanced Configuration
- What's in settings.json beyond permissions? (hooks, file suggestions, model config)
- How do slash commands work? What's the `.claude/commands/` structure?
- What's the difference between Skills and slash commands? When use each?
- How do custom subagents work? What goes in `.claude/agents/`?

### Performance & Cost
- When is Opus 4.5 worth the cost vs Sonnet 4.5 in Claude Code specifically?
- What's the actual token consumption pattern? How do thinking tokens (`ultrathink`) affect cost?
- How does the headless mode (`-p` flag) differ from interactive for automation?

### Edge Cases & Limitations
- What tasks does Claude Code consistently struggle with? (Known failure modes)
- What are the actual security implications of `--dangerously-skip-permissions`?
- What happens when Claude Code "loops" on a problem? What recovery patterns work?

---

## Sources to Prioritize

### First-Party (Authoritative)
- https://code.claude.com/docs/ — Full documentation site (examine all sections)
- https://docs.anthropic.com/ — API documentation for context
- Anthropic blog posts on Claude Code releases

### Practitioner Insights (High Signal)
- Boris Cherny (@AMonkeyNamedBoris) — Creator of Claude Code, primary source for intended patterns
- MinChoi thread on optimization (parallel workflows, hooks, Plan Mode)
- Zvi Mowshowitz essay "Claude Codes" — Ecosystem overview with critical perspective
- Eyad Khrais tutorial — Production engineering perspective (Amazon/Disney/Capital One background)
- Peter Steinberger (@steipete) — Contrast with GPT/Codex workflows (what's different about Claude Code)

### Community Sources (Verify Quality)
- r/ClaudeAI subreddit — Filter for substantive technical posts, not hype
- X/Twitter #ClaudeCode — Practitioner tips (high noise ratio, look for specifics)
- GitHub discussions/issues for claude-code if public

---

## Output Structure Requested

### Part 1: Capability Architecture
Technical documentation of what Claude Code can do, organized by capability domain.

### Part 2: Configuration Deep Dive
Comprehensive coverage of CLAUDE.md, settings.json, Skills, hooks, and slash commands.

### Part 3: Workflow Patterns
Synthesis of practitioner patterns with assessment of which generalize vs which are context-specific.

### Part 4: Integration Landscape
How Claude Code relates to Cursor, Desktop app, web app, MCP ecosystem, GitHub integration.

### Part 5: Orchestration Principles
Generalizable insights for multi-agent coordination, applicable beyond Claude Code specifically.

### Part 6: Anti-Patterns & Failure Modes
What to avoid, common mistakes, and known limitations.

### Part 7: Evolution Trajectory
Where Claude Code is heading based on recent releases, announced features, competitive positioning.

---

## What This Research Is NOT

- **Not a tutorial** — Assume reader can read documentation; focus on synthesis and insight
- **Not prescriptive** — Don't template specific configurations; illuminate principles
- **Not coding-focused** — Software engineering is downstream; this is about AI orchestration
- **Not comparative to OpenAI/Google** — Those are separate research tracks requiring different sampling
- **Not hype** — Acknowledge limitations and failure modes honestly

---

## Meta-Instruction

You are conducting this research for someone who:
- Has 3 Claude Pro accounts and is building multi-Claude orchestration
- Operates through strategic "Oracle" sessions that issue directives to execution engines
- Is more interested in **architectural principles** than specific code snippets
- Has an AuDHD cognitive architecture preferring "globe before trees" (holistic context before tactical execution)
- Values **enduring insight** over temporal feature documentation

The ideal output would be equally valuable in 3 months when specific features may have changed, because it captures the underlying patterns and principles that inform Claude Code's design and effective usage.

---

*Research prompt prepared 2026-01-11 | Syncrescendence Oracle 12*
