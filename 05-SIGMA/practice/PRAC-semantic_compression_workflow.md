# PRAC: Semantic Compression Workflow

**Scope**: SN methodology, sutra crafting, quality verification

---

## The Method

```
TERM SemanticCompression:
sutra: "Read → Extract unique value → Compress → Preserve essence at 80% reduction"
gloss: Semantic Notation (SN) achieves ~80% token compression while preserving
       full semantic content. Key: sutra captures essence in one line, gloss
       provides context, spec contains structured detail.
spec:
    type: PRACTICE
    compression_target: 80% reduction
    preservation_requirement: "All unique insights must survive"
    format: "sutra + gloss + spec"
end
```

---

## SN Format Structure

### TERM Block (Definitions)
```
TERM ConceptName:
sutra: "One-line essence, ≤100 chars, memorable aphorism"
gloss: "2-4 sentences explaining WHY this matters, Ψ-specific context,
       not verbatim from source"
spec:
    type: TERM
    field1: value
    field2: [list, of, items]
    field3: "Structured data, not prose sentences"
end
```

### NORM Block (Rules)
```
NORM RuleName:
sutra: "The constraint or principle in memorable form"
gloss: "Why this rule exists, what it prevents"
spec:
    type: NORM
    applies_to: [contexts]
    exceptions: [edge_cases]
end
```

### PROC Block (Workflows)
```
PROC WorkflowName:
    1: "First step"
    2: "Second step"
    3: "Third step"
end
```

---

## Sutra Crafting

### Rules
- **Length**: ≤100 characters
- **Form**: Present tense, active voice
- **Content**: NEW SYNTHESIS, not verbatim quote
- **Quality**: Memorable, aphoristic, captures essence

### Good Examples
```
"Perceive-reason-act-observe-iterate: the recursive decision engine"
"200K ceiling is lie—quality degrades at 150K, collapses at 190K"
"Fresh start every loop—AI operates in smartest mode"
"Wipe the whiteboard after every task"
```

### Bad Examples
```
"This is a system for managing context"  # Too vague
"Claude Code is an agentic coding assistant that runs as a CLI"  # Verbatim
"The tool provides various features for automation"  # No insight
```

---

## Extraction Workflow

```
PROC SemanticExtraction:
    1: "Read source completely—no skimming"
    2: "Identify UNIQUE insights (not common knowledge)"
    3: "For each insight:"
        a: "Distill to sutra (one-line essence)"
        b: "Write gloss (why it matters)"
        c: "Structure spec (typed fields)"
    4: "Cross-reference against existing blocks"
    5: "Eliminate redundancy, merge related concepts"
    6: "Verify all unique insights preserved"
end
```

---

## Quality Verification

### Before Each Block
- [ ] Sutra is ≤100 chars
- [ ] Sutra is NEW SYNTHESIS (not copied)
- [ ] Sutra is memorable and aphoristic
- [ ] Gloss adds Ψ-specific context
- [ ] Gloss is 2-4 sentences
- [ ] Spec fields are TYPED (no prose sentences)
- [ ] Cross-refs use `[[FileName]]` format

### Before Document Complete
- [ ] All unique insights preserved (check against originals)
- [ ] Zero truncation markers
- [ ] Compression ratio achieved (~80%)
- [ ] No redundancy between blocks

---

## Common Patterns

### Platform Insight Preservation
Different platforms provide unique angles:

| Platform | Preserve |
|----------|----------|
| Claude | Safety consciousness, architectural elegance |
| ChatGPT | Implementation pragmatism, code-first examples |
| Gemini | Conceptual synthesis, theoretical framing |
| Grok | Practitioner patterns, community wisdom |

### Anti-Pattern Detection

| Pattern | Problem | Fix |
|---------|---------|-----|
| Verbatim copying | Not compression | Rewrite in own words |
| Prose in spec | Wrong format | Convert to typed fields |
| Vague sutra | No insight | Find unique angle |
| Missing gloss | No context | Add WHY it matters |

---

## Spec Field Types

### Use These
```yaml
spec:
    type: TERM              # Required: block type
    components: [a, b, c]   # Lists
    threshold: 75%          # Numbers with units
    when_use: "Condition"   # Short phrases
    anti_pattern: "X"       # Warnings
```

### Avoid These
```yaml
spec:
    explanation: "This is a long paragraph explaining how the system
                 works in detail with multiple sentences."  # NO
```

---

## Iteration Pattern

```
PROC CompressionIteration:
    1: "First pass: Extract all potential insights"
    2: "Second pass: Merge redundant concepts"
    3: "Third pass: Tighten sutras to ≤100 chars"
    4: "Fourth pass: Verify typed spec fields"
    5: "Final pass: Spot-check against originals"
end
```

---

## Metrics Template

```markdown
## Compression Metrics

| Metric | Value |
|--------|-------|
| Source words | N |
| Output words | N |
| Compression ratio | X% |
| Unique insights | N |
| TERM blocks | N |
| NORM blocks | N |
| PROC blocks | N |

## Verification
- [ ] Spot-checked block 1: [name]
- [ ] Spot-checked block 2: [name]
- [ ] Spot-checked block 3: [name]
```

---

## Cross-References

- [[SYNTHESIS-claude_code_architecture]] → Example of full SN document
- [[00-ORCHESTRATION/scripts/sn_symbols.yaml]] → Symbol glossary
- [[00-ORCHESTRATION/scripts/SN_BLOCK_TEMPLATES.md]] → SN templates
