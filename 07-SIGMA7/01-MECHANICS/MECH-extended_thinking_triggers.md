# MECH: Extended Thinking Triggers

**Scope**: When to enable, token allocation, quality/speed tradeoffs, configuration

---

## Core Concept

```
TERM ExtendedThinking:
sutra: "Hidden chain-of-thought costs tokens but catches errors before they compound"
gloss: Opus 4.5 includes "Thinking Tokens"—hidden reasoning before response.
       Billed as output tokens. Significantly increases quality for complex
       reasoning (debugging, architecture) but adds latency and cost.
       Toggle based on task complexity.
spec:
    type: MECHANISM
    model: Opus 4.5 (primary), Sonnet 4.5 (available)
    billing: "Output tokens (expensive)"
    impact: [improved_reasoning, increased_latency, higher_cost]
    use_for: [complex_debugging, architecture, multi_step_reasoning]
    skip_for: [routine_tasks, simple_lookups, straightforward_edits]
end
```

---

## Thinking Levels

| Level | Tokens | Use When | Example Tasks |
|-------|--------|----------|---------------|
| **default** | Auto | Let model self-regulate | Routine work |
| **think** | ~4K | Standard deliberation | Normal complexity |
| **megathink** | ~10K | Moderate complexity | Multi-step reasoning |
| **ultrathink** | ~32K | Maximum depth | Architecture, forensics |

---

## Trigger Patterns

### Use Extended Thinking For

**Architectural Decisions**
```
ultrathink: Design the authentication system for this application.
Consider OAuth, JWT, session-based approaches. Evaluate tradeoffs.
```

**Complex Debugging**
```
megathink: This test has been failing intermittently for weeks.
Analyze the race condition and propose a fix.
```

**Multi-File Refactoring**
```
think hard: Refactor the data layer to use repository pattern.
Plan changes across all affected files before executing.
```

**Forensic Analysis**
```
ultrathink: Something broke between commits abc123 and def456.
Trace through all changes to identify the root cause.
```

### Skip Extended Thinking For

- Single-file edits with clear requirements
- Simple lookups ("Where is the config file?")
- Routine commits
- Documentation updates
- Format conversions

---

## Configuration

### Via Prompt Prefix

```
think: [your prompt here]
think hard: [your prompt here]
ultrathink: [your prompt here]
```

### Via settings.json

```json
{
  "thinking": {
    "default_level": "think",
    "max_tokens": 10000
  }
}
```

### Via Directive Headers

```yaml
# In blitzkrieg directive
Lane: A
Toolchain: claude_code
Model: opus-4.5
Thinking: ultrathink
```

---

## Cost/Benefit Analysis

### Thinking Tokens Are Output Tokens

| Model | Input/Output per 1M |
|-------|---------------------|
| Opus 4.5 | $15 / $75 |
| Sonnet 4.5 | $3 / $15 |

**32K thinking tokens at Opus output rate**: ~$2.40 per invocation

### Quality Improvement

- **Complex debugging**: 2-3x more likely to find root cause on first attempt
- **Architecture**: Catches integration issues before coding begins
- **Multi-step**: Reduces cascading errors by planning ahead

### Break-Even Calculation

If ultrathink prevents one "redo" iteration:
- Redo cost: ~$5-10 (additional context, exploration, fix)
- Ultrathink cost: ~$2.40
- **Net savings**: $2.60-7.60 per prevented redo

---

## Model Selection Matrix

| Task | Model | Thinking |
|------|-------|----------|
| Strategic planning | Opus | ultrathink |
| Architecture design | Opus | ultrathink |
| Complex debugging | Opus | megathink |
| Feature implementation | Sonnet | think |
| Routine edits | Sonnet | default |
| Quick search | Haiku | default |
| Validation checks | Haiku | default |

---

## Blitzkrieg Integration

```yaml
# Lane A: Strategic/architectural
Lane: A
Model: opus-4.5
Thinking: ultrathink

# Lane B: Tactical execution
Lane: B
Model: sonnet-4.5
Thinking: think

# Lane C: Validation
Lane: C
Model: haiku
Thinking: default
```

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Ultrathink for everything | Cost explosion | Match level to task |
| No thinking for complex | Missed errors compound | Enable for architecture, debugging |
| Ignoring latency impact | User experience | Set expectations, use async |

---

## Cross-References

- [[SYNTHESIS-agents_mcp_foundations]] → Model economics
- [[MECH-task_orchestration]] → Thinking in task directives
- [[PRAC-oracle_to_executor_handoff]] → Oracle uses ultrathink
