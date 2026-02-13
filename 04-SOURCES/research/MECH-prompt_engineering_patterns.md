# MECH: Prompt Engineering Patterns

**Scope**: Clarity, context, task decomposition, format specification, examples, roles

---

## Core Insight

```
TERM PromptingAsArchitecture:
sutra: "The work is in the thinking before you type—clarity determines output"
gloss: Most prompting failures stem from fuzzy mental models, not technique.
       The gap between what you want and what you get has nothing to do with
       model limitations. It's about precision of communication. Clear mental
       image → clear prompt → clear output.
spec:
    type: MECHANISM
    primary_failure: "Fuzzy idea → fuzzy prompt → fuzzy output"
    solution: "Sharpen mental image before typing"
    process: "Think first, type second"
    principle: "Prompting is cognitive architecture; AI is execution engine"
end
```

---

## The Seven Rules

### Rule 1: Clarity Is All You Need

Before typing, ask yourself:
- What's so special about this output?
- How is it different from generic slop?
- Why would someone value this?
- What emotion or outcome am I creating?

**Find references**: Look for assets that make you say "yes, exactly like this." Use AI to reverse-engineer outputs you admire.

**Define everything**: Format, scope, constraints, success criteria, audience, tone, structure, length, style.

### Rule 2: Context Is Everything

```
PROC ContextEngineering:
    1: "Create project in AI tool (GPT Project, Claude Project)"

    2: "Ask AI to interview you about project"
        - Goals, constraints, audience
        - Everything relevant for future prompts

    3: "Save conversation as context.json"

    4: "Upload to project"

    5: "On every prompt, start with 'load context.json'"

    6: "Update context.json when decisions change"

    result: "Model isn't starting from scratch every time"
end
```

### Rule 3: Think in Tasks

Break down the process, not just the result:

**Bad**: "Write a business plan for my startup."
**Good**:
1. Start with executive summary focusing on market timing
2. Move to ideal customer profile with psychological triggers
3. Skip competition (we're creating new category)
4. Include unit economics with sensitivity analysis

Ask AI to explain its approach first, then refine before execution.

### Rule 4: Specify Output Format

Think about what you'll do with the output:
- Pasting into presentation? → Slide-ready sections with headers
- Using in code? → JSON/XML with specific keys
- Reading for research? → Structured summary with main/supporting points

The model has no format preference—tell it exactly what you need.

### Rule 5: Provide Examples

Few-shot learning = providing examples of what you want.

Examples force the model to work within specific tunnel instead of entire training set:
- Want your voice? → 3-5 writing examples with different contexts
- Want your style? → Examples with notes on what makes each work
- Want your analysis? → Past analyses with thought process annotations

Examples turn abstract instructions into concrete templates.

### Rule 6: Role Assignment

Not credentials—capture the vibe of the expert:

**Bad**: "You are a marketing expert."
**Good**: "You are the type of marketer who sees psychological patterns in consumer behavior that others miss completely, the kind who can predict what will go viral three months before it happens because you understand attention economics at a level most people never reach."

The specificity creates constraint that shapes approach.

### Rule 7: Constraint Definition

Include what you DON'T want:
- "No corporate jargon"
- "No deprecated libraries"
- "Never use these overused phrases: [list]"

**Limit to 3-5 constraints max**—more creates noise the model filters out.

---

## Rule Multiplication

Rules don't add—they multiply:
- Clarity + context = exponentially more powerful
- Context + task decomposition = outputs feeling months of familiarity
- Examples + role + format = "how did you do that?"

---

## XML Scaffolding

Structure complex prompts with XML:

```xml
<context>
Project details, background, constraints
</context>

<task>
What you want accomplished
</task>

<format>
Desired output structure
</format>

<examples>
Reference outputs
</examples>

<constraints>
What to avoid
</constraints>
```

**Benefits**: Clear boundaries, easy to update sections, model parses reliably.

---

## Context Priming

Load relevant context before task:

```markdown
Before we begin, read and understand:
- @docs/architecture.md (system design)
- @docs/decisions.md (past choices)
- @.claude/rules/coding.md (conventions)

Now, with this context: [actual task]
```

---

## Chain-of-Thought Patterns

### Explicit Reasoning Request
```
Think through this step by step:
1. First, understand the current state
2. Then, identify what needs to change
3. Finally, plan the implementation

Show your reasoning before giving the answer.
```

### Verification Loop
```
After generating your answer:
1. Check if it meets all stated requirements
2. Identify any edge cases not handled
3. Revise if necessary
4. Explain what you verified
```

---

## Prompt Templates

### For Analysis
```
Analyze [subject] considering:
- [Lens 1]
- [Lens 2]
- [Lens 3]

Format as:
## Summary (2 sentences)
## Key Findings (bulleted)
## Implications (numbered)
## Open Questions (bulleted)
```

### For Implementation
```
Implement [feature] following these constraints:
- [Technical constraint]
- [Style constraint]
- [Scope constraint]

Before coding, outline your approach in 3-5 steps.
After coding, verify against constraints.
```

### For Review
```
Review [artifact] for:
- [Quality dimension 1]
- [Quality dimension 2]
- [Quality dimension 3]

Rate each dimension (pass/concern/fail).
For concerns and fails, explain specifically what's wrong and how to fix.
```

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Vague prompts | Model uses generic training patterns | Specify everything |
| No context | Starting from scratch each time | Use context files |
| Credential-based roles | Shallow persona | Capture vibe, not title |
| Too many constraints | Model ignores most | Max 3-5 |
| No format specification | Unusable output | Design format for use case |

---

## Cross-References

- [[SYNTHESIS-agents_mcp_foundations]] → Agent prompting considerations
- [[MECH-extended_thinking_triggers]] → When to request deeper reasoning
- [[PRAC-oracle_to_executor_handoff]] → Handoff document prompting
