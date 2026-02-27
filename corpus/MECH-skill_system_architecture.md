# MECH: Skill System Architecture

**Scope**: Progressive disclosure, SKILL.md format, subagent pairing, hot-reloading

---

## Core Concept

```
TERM SkillArchitecture:
sutra: "Metadata at startup (~100 tokens), full instructions on activation—context preserved until needed"
gloss: Skills solve the context tax problem. Instead of loading 50 tool schemas
       (70K+ tokens) at startup, agents load only name+description, activating
       full instructions when task semantically matches.
spec:
    type: MECHANISM
    problem_solved: "Context bloat from eager-loading all capabilities"
    solution: "Progressive disclosure via semantic matching"
    token_efficiency: "~100 tokens per skill at startup vs 1K-5K for full schema"
end
```

---

## Directory Structure

```
skill-name/
├── SKILL.md                 # Required: instructions + metadata
├── scripts/                 # Optional: executable code
├── references/              # Optional: documentation
└── assets/                  # Optional: templates, resources
```

**Discovery paths**:
- User-level: `~/.claude/skills/`
- Project-level: `.claude/skills/`

---

## SKILL.md Format

### Required Frontmatter

```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents.
---
```

### Optional Frontmatter

```yaml
---
name: code-review
description: Comprehensive code review following team standards
license: Apache-2.0
compatibility: Designed for Claude Code
metadata:
  author: team-name
  version: "1.0"
allowed-tools: Bash(git:*) Bash(jq:*) Read
---
```

### Field Constraints

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | 1-64 chars, lowercase + hyphens, no leading/trailing hyphens |
| `description` | Yes | 1-1024 chars, describe what AND when to use |
| `license` | No | License name or reference to bundled file |
| `compatibility` | No | 1-500 chars, environment requirements |
| `metadata` | No | Arbitrary key-value mapping |
| `allowed-tools` | No | Space-delimited pre-approved tools (experimental) |

### Body Content

No format restrictions. Write whatever helps agents perform effectively.

**Recommended sections**:
- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases

**Size guidance**: Keep under 500 lines. Move detailed reference to separate files.

---

## Invocation Modes

Skills merged with slash commands in Jan 2026. Three invocation modes:

### User-Invocable (Slash Command)
```yaml
---
name: deploy
# user-invocable: true (default)
---
```
User types `/deploy` → skill loads and executes.

### Model-Invocable (Semantic Activation)
```yaml
---
name: pdf-processing
# Model automatically activates when task matches description
---
```
User says "extract tables from this PDF" → model recognizes match → activates skill.

### Disable Either
```yaml
---
name: internal-helper
user-invocable: false         # Cannot invoke with /
disable-model-invocation: true # Model cannot auto-invoke
---
```

---

## Subagent Pairing

Skills naturally pair with subagents for context isolation.

### Search Skills with Explore Agent

```yaml
---
name: deep-research
description: Research a topic thoroughly
agent: Explore
---

# Instructions
- Find relevant files using Glob and Grep
- Read and analyze the code
- Summarize findings with specific file references
```

`agent: <type>` spawns subagent that loads skill into its context.

### Memory Skills with Forked Context

```yaml
---
name: update-memory
description: Update CLAUDE.md with user preferences
context: fork
disable-model-invocation: true
agent: general-purpose
---

# Instructions
Review recent conversation feedback and update CLAUDE.md accordingly.
```

`context: fork` spins off subagent with all current context—great for parallel operations.

### Model Specification

```yaml
---
name: quick-validate
agent: Bash
model: haiku
---
```

| Model | Use When |
|-------|----------|
| `haiku` | Simple searches, quick validations |
| `sonnet` | Most implementation work |
| `opus` | Complex reasoning, architecture decisions |

---

## Hot-Reloading

```
NORM HotReload:
sutra: "Skills modified in ~/.claude/skills immediately available—no restart needed"
gloss: v2.1.0+ automatically detects changes. Create or modify skill files and
       they're immediately usable without session restart.
spec:
    trigger: "File change detected in skill directories"
    scope: [~/.claude/skills, .claude/skills]
    requires: "Claude Code v2.1.0+"
end
```

---

## Progressive Disclosure Flow

```
PROC SkillActivation:
    1: "Session start → Load all skill name+description (~100 tokens each)"
    2: "User issues task"
    3: "Model evaluates task against skill descriptions"
    4: "Match found → Load full SKILL.md into context"
    5: "Execute instructions, optionally loading referenced files"
    6: "Referenced files (scripts/, references/) loaded only when needed"
end
```

---

## Skill vs Legacy Slash Command

| Aspect | Slash Commands (Legacy) | Skills (Current) |
|--------|------------------------|------------------|
| **Invocation** | Deterministic (`/command`) | Semantic + deterministic |
| **Discovery** | Manual listing | Model matches descriptions |
| **Subagents** | No native support | `agent:` and `context:` fields |
| **Hot-reload** | Requires restart | Automatic |
| **File refs** | Single file | Can reference scripts/, references/ |
| **Migration** | N/A | Commands in `~/.claude/commands` continue working |

---

## Best Practices

### Description Writing

**Good**:
```yaml
description: Extracts text and tables from PDF files, fills PDF forms, and
             merges multiple PDFs. Use when working with PDF documents or
             when the user mentions PDFs, forms, or document extraction.
```

**Poor**:
```yaml
description: Helps with PDFs.
```

Include specific keywords that help agents identify relevant tasks.

### Context Management

- Keep SKILL.md under 500 lines
- Move detailed reference to `references/REFERENCE.md`
- Use file references one level deep
- Avoid deeply nested reference chains

### Subagent Selection

| Task Type | Recommended Agent |
|-----------|-------------------|
| Codebase search | `agent: Explore` |
| Parallel operations | `context: fork` |
| Command execution | `agent: Bash` |
| Full implementation | `agent: general-purpose` |

---

## Anti-Patterns

- **Overstuffing descriptions**: Keep under 1024 chars
- **Eager file loading**: Reference files, don't inline
- **Missing keywords**: Vague descriptions prevent semantic matching
- **No validation testing**: Use `skills-ref validate ./my-skill`

---

## Validation

```bash
# Install reference library
pip install skills-ref

# Validate skill
skills-ref validate ./my-skill

# Generate prompt XML for integration
skills-ref to-prompt ./my-skill
```

---

## Cross-References

- [[SYNTHESIS-claude_code_architecture]] → SkillSystem TERM block
- [[MECH-task_orchestration]] → Subagent spawning via Task tool
- [[PRAC-parallel_claude_orchestration]] → Skills in multi-instance workflows
