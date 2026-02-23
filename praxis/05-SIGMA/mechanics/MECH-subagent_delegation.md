# MECH: Sub-Agent Delegation

**Scope**: Task tool mechanics, isolation benefits, artifact return, custom agents

---

## Core Concept

```
TERM SubagentMechanism:
sutra: "Isolated context, specialized prompt, discrete output—parallelism without pollution"
gloss: Sub-agents run in separate context windows from main agent. Tokens consumed
       by sub-agent don't count against main agent's limit. 50K tokens in sub-agent
       leaves main agent's 200K intact. Returns short summary, not full transcript.
spec:
    type: MECHANISM
    isolation: "Separate context window"
    token_accounting: "Sub-agent tokens separate from main"
    return: "Artifact or summary, not full history"
    benefit: "Keeps main thread clean, preserves intelligence"
end
```

---

## Built-in Sub-Agent Types

| Agent | Model | Capabilities | Use Case |
|-------|-------|--------------|----------|
| **bash** | Sonnet | Terminal only | Git ops, tests, commands |
| **explore** | Haiku | Read, search | Fast codebase navigation |
| **plan** | Sonnet | Read only | Investigation, requirements |
| **general-purpose** | Sonnet | Full toolset | Multi-step execution |
| **claude-code-guide** | Haiku | Docs access | Feature questions |

---

## Invocation Methods

### Direct (@mention)
```
@explore What testing frameworks does this project use?
```
Agent runs inline, returns result to main thread.

### Background (Ctrl+B)
```
@explore [Ctrl+B] Analyze the authentication module
```
Agent runs in background. Main thread continues. Check progress with down arrow + Enter.

### Implicit (Agent Decides)
```
Use two explore agents in parallel to analyze the codebase
```
Main agent spawns sub-agents as needed.

### Task Tool (Programmatic)
```json
{
  "subagent_type": "general-purpose",
  "model": "haiku",
  "prompt": "You are fact-checker. Complete tasks where owner: fact-checker.",
  "description": "Fact-checker agent"
}
```

---

## Parallel Execution Pattern

Multiple Task tool calls in single message = parallel execution:

```json
// Three agents, running simultaneously
{ "subagent_type": "explore", "prompt": "Analyze backend architecture" }
{ "subagent_type": "explore", "prompt": "Analyze frontend patterns" }
{ "subagent_type": "explore", "prompt": "Analyze test coverage" }
```

**Key insight**: More specific scope = better results. Single agent doing everything vs specialized sub-agents is "night and day" quality difference in complex projects.

---

## Creating Custom Agents

### Via `/agents` Command

1. Run `/agents`
2. Choose project-level or personal-level
3. Describe the agent (personality, expertise, focus)
4. Claude writes system prompt
5. Select available tools
6. Choose model (Opus, Sonnet, Haiku)
7. Name the agent
8. Restart Claude Code to load

### Direct File Creation

Create in `.claude/agents/`:

```markdown
# .claude/agents/code-reviewer.md

You are a senior code reviewer with 20 years of experience.
Focus on:
- Security vulnerabilities
- Performance issues
- Code clarity and maintainability
- Test coverage

Be direct and specific. Reference line numbers.
Don't suggest changes unless they're significant.
```

---

## Context Protection Pattern

```
PROC ContextProtection:
    context: "Complex feature implementation"

    1: "Enter planning mode for decomposition"

    2: "Spawn 3 planning agents in parallel"
        - "Investigate authentication requirements"
        - "Investigate database schema needs"
        - "Investigate API patterns in codebase"

    3: "Agents consume 80K tokens combined"

    4: "Main thread usage increases ~6% (from 20% to 26%)"

    5: "Store plan in /spec folder"

    6: "Execute via coder sub-agents"

    result: "Main thread stays clean, full intelligence preserved"
    comparison: "Without sub-agents: 60%+ main thread usage"
end
```

---

## Coordinator Pattern

Main agent as orchestrator:

```
PROC CoordinatorExecution:
    1: "Main agent reads implementation plan"

    2: "Identifies parallelizable tracks"
        - Track A: Backend models
        - Track B: API endpoints
        - Track C: Frontend components

    3: "Spawns Coder sub-agent per track"

    4: "Upon completion, hands to Code Reviewer agent"

    5: "Reviewer returns feedback"

    6: "Coder addresses issues"

    7: "Cycle continues until feature complete"

    result: "Full application built using ~58% main context"
end
```

---

## When to Use Sub-Agents

### Good For
- Parallel investigation of independent aspects
- Specialized expertise (security review, UI audit)
- Long-running operations (comprehensive analysis)
- Keeping main thread clean for debugging
- Complex features requiring multiple perspectives

### Not For
- Simple single-file operations
- Quick lookups (just ask main agent)
- Tasks requiring iterative main-thread feedback
- When result needs deep integration with conversation

---

## Model Selection

| Model | Use When | Characteristics |
|-------|----------|-----------------|
| **Haiku** | Simple searches, quick validations | Fastest, cheapest |
| **Sonnet** | Most implementation work | Balanced speed/capability |
| **Opus** | Complex reasoning, architecture | Deep thinking, expensive |

**Pattern**: Use Haiku for explore/plan, Sonnet for general-purpose, Opus only when complexity requires.

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Sub-agent for everything | Overhead exceeds benefit | Reserve for parallel/specialist work |
| No context isolation | Pollution defeats purpose | Ensure separate context |
| Ignoring return artifacts | Results lost | Process sub-agent output explicitly |
| Wrong model selection | Overpay or underperform | Match model to task complexity |

---

## Delegation Decision Tree

```
Is the task independent of current conversation?
├── NO → Execute inline (main context)
└── YES →
    Does it require writing/editing files?
    ├── NO → Use Explore agent (read-only, fast, cheap)
    └── YES →
        Is it > 5 minutes of work?
        ├── NO → Execute inline
        └── YES →
            Can multiple tasks run in parallel?
            ├── YES → Fork multiple sub-agents (Blitzkrieg)
            └── NO → Fork single general-purpose agent
```

---

## Skill Context Annotation

Skills can declare their execution context preference:

```markdown
<!-- context: fork -->
<!-- model: haiku -->
<!-- reason: Heavy file scanning, independent of main thread -->
```

| Value | Meaning | Invocation |
|-------|---------|-----------|
| `inline` | Execute in main agent context | Skill tool (default) |
| `fork` | Execute in isolated sub-agent | Task tool with subagent_type |
| `parallel` | Can be batched with other fork tasks | Multiple Task tool calls |

**Mark `fork`** when: read-heavy analysis, output is summary, >10K tokens, no iterative feedback needed.
**Keep `inline`** when: modifies conversation state, feeds next step, requires back-and-forth, <2K tokens.

---

## Constellation Agent Mapping

| Delegation Target | Agent | Model | When |
|-------------------|-------|-------|------|
| `explore` sub-agent | (built-in) | Haiku | Quick searches, file discovery |
| `general-purpose` sub-agent | (built-in) | Sonnet | Implementation tasks |
| Dispatch to Adjudicator | Codex CLI | Sonnet | Quality review, testing |
| Dispatch to Cartographer | Gemini CLI | Gemini Pro 3.1 | Research, 1M context analysis |
| Dispatch to Psyche | OpenClaw | GPT-5.3-codex | Automation, system cohesion |

**Rule**: Intra-session delegation uses sub-agents (Task tool). Cross-session delegation uses dispatch.sh (INBOX files).

---

## Token Savings Examples

| Scenario | Inline Cost | Forked Cost | Savings |
|----------|------------|-------------|---------|
| Audit 79 CANON files | ~80K tokens in main | ~80K in sub + 2K summary | Main context preserved |
| 3 parallel explores | ~45K sequential in main | ~15K each in parallel, 3K total returned | 80% main context saved |
| Research task (read-only) | ~30K polluting main | ~30K isolated + 1K summary | Main stays at peak intelligence |

The savings aren't in total tokens consumed — they're in **main context preservation**. A main agent at 20% usage is dramatically smarter than one at 70%.

---

## Cross-References

- [[SYNTHESIS-agents_mcp_foundations]] → Agent patterns, orchestration
- [[MECH-skill_system_architecture]] → Skills with sub-agent pairing
- [[MECH-task_orchestration]] → Task tool mechanics

---

## Consolidated From

- `praxis/05-SIGMA/practice/PRAC-subagent_delegation_guide.md` — Decision tree, skill context annotation, constellation agent mapping, token savings examples
