# Semantic Notation Block Templates
## Version 1.0.0

**Purpose**: Standard block structures for SN-encoded documents

**Usage**: Copy template, fill in fields, use SN operators from symbols.yaml

---

## TERM Block (Ontology/Definitions)

**Use when**: Defining what something IS (concepts, entities, types)

```
TERM <Name>:
    sutra: "<one-line mnemonic (max 100 chars)>"
    gloss:
        <Human prose explanation, 2-4 sentences>
        <Focus on WHY this matters, not just WHAT it is>
    spec:
        properties:
            <name>: <type or description>
            <name>: <type or description>
        relations:
            <edge_type>: <target>
            <edge_type>: <target>
        examples:
            - <concrete example>
end
```

**Example**:
```
TERM AxiologicalConstants:
    sutra: "Five fitness functions: optionality, comprehensibility, exit, distribution, documentation"
    gloss:
        Minimal universal values any consciousness must preserve.
        Meta-protocol, not commandments—evolutionary pressure shaping fitness landscape.
    spec:
        properties:
            count: 5
            modality: MUST
            scope: [all_substrates, all_implementations]
        relations:
            governs: ConsciousnessArchitecture
            updates_via: collective_intelligence
        examples:
            - "Preserve optionality: avoid irreversible lock-ins"
end
```

---

## NORM Block (Constitutional Constraints)

**Use when**: Defining what MUST/SHOULD/MAY be true (rules, invariants, constraints)

```
NORM <Name>:
    sutra: "<deontic one-liner describing requirement>"
    spec:
        modality: MUST | SHOULD | MAY | MUST_NOT
        subject: <who/what is constrained>
        action: <what must/should/may be done>
        scope: [<where this applies>]
        invariant: "<what must remain true>"
        violation: "<what happens if violated>"
    gloss:
        <Why this norm exists>
        <Rationale and consequences>
end
```

**Example**:
```
NORM FlatPrinciple:
    sutra: "All directories MUST be flat; use naming prefixes instead of nesting"
    spec:
        modality: MUST
        subject: all_directories
        action: forbid(subdirectories) ∧ require(prefix_naming)
        scope: [00-ORCHESTRATION, 01-CANON, 02-OPERATIONAL, 04-SOURCES, 05-ARCHIVE, 06-EXEMPLA]
        invariant: "∀ dir ∈ scope: depth(dir) = 1"
        violation: "Breaks agent navigation | increases decision depth"
    gloss:
        Flat structure ensures agents reach any file in ≤2 decisions.
        Prefixes (ARCH-, DYN-, REF-, SCAFF-) provide semantic organization without hierarchy.
end
```

---

## PROC Block (Procedures/Orchestrations)

**Use when**: Defining HOW something happens (workflows, processes, algorithms)

```
PROC <Name>(<inputs>) -> <outputs>:
    sutra: "<action summary in verb form>"
    spec:
        requires: [<prerequisite norms or terms>]
        inputs:
            <name>: <type>
        outputs:
            <name>: <type>
        steps:
            1. <step> >> <result>
            2. <step> | <constraint> >> <result>
            3. <conditional>:
                   <step> >> <result>
               else:
                   <alternative> >> <result>
        produces: [<artifacts>]
        consumes: [<resources>]
    gloss:
        <Why this procedure exists>
        <Key decision points and edge cases>
end
```

**Example**:
```
PROC SourceProcessing(raw_source) -> integrated_knowledge:
    sutra: "Triage >> process >> integrate >> update >> archive"
    spec:
        requires: [TRIAGE_PROTOCOL, DYN-SOURCES.csv]
        inputs:
            raw_source: {platform, format, url}
        outputs:
            integrated_knowledge: Κ | Ο | Σ
        steps:
            1. raw_source >> triage | signal_tier >> {paradigm, strategic, tactical, noise}
            2. paradigm | strategic >> process_function(format) >> processed_source
            3. processed_source >> integrate(CANON_targets) >> updated_CANON
            4. update(DYN-SOURCES.csv) | status := integrated
            5. tactical >> archive_metadata_only
        produces: [processed_source, updated_CANON, ledger_entry]
        consumes: [raw_source]
    gloss:
        Complete source-to-synthesis cycle.
        Filters noise early, preserves paradigm/strategic for integration.
end
```

---

## PASS Block (Deterministic Transforms)

**Use when**: Defining pure functional transforms (input → output, no side effects)

```
PASS <Name>:
    sutra: "<transform summary>"
    spec:
        input: <type>
        output: <type>
        transform: <input> >> <intermediate> >> <output>
        invariant: "<what is preserved across transform>"
        properties:
            deterministic: true | false
            reversible: true | false
            lossy: true | false
    gloss:
        <What this transform achieves>
        <When to use vs alternatives>
end
```

**Example**:
```
PASS Canonicalize:
    sutra: "Raw markdown >> structured frontmatter >> CANON-NNNNN format"
    spec:
        input: markdown_document
        output: CANON_document
        transform:
            raw_markdown
            >> extract(metadata)
            >> validate(schema)
            >> assign(CANON_ID)
            >> format(tier, version)
            >> canonical_CANON
        invariant: "semantic_content preserved; structure standardized"
        properties:
            deterministic: true
            reversible: false (metadata added)
            lossy: false (no content removed)
    gloss:
        Elevates raw documents to canonical status.
        Irreversible by design—once canonical, remains canonical.
end
```

---

## ARTIFACT Block (Named Outputs)

**Use when**: Documenting concrete outputs (files, datasets, indices)

```
ARTIFACT <Name>:
    sutra: "<what this is and why it exists>"
    spec:
        type: document | dataset | index | config | binary
        path: <filesystem location>
        format: <file format>
        produced_by: <PROC that creates it>
        consumed_by: [<PROCs that use it>]
        update_frequency: continuous | on_demand | periodic
        size: <typical size>
    gloss:
        <Purpose and usage context>
        <How to regenerate if lost>
end
```

**Example**:
```
ARTIFACT DYN-TASKS.csv:
    sutra: "Ground truth task ledger; canonical backlog state"
    spec:
        type: dataset
        path: 00-ORCHESTRATION/state/DYN-TASKS.csv
        format: CSV (UTF-8, quoted fields)
        produced_by: update_ledgers | manual_edit
        consumed_by: [dashboard, task_query, blitzkrieg_routing]
        update_frequency: continuous (after each task state change)
        size: ~10KB (100-200 tasks typical)
    gloss:
        Single source of truth for task state.
        Never trust execution reports—verify against this ledger.
        Atomic updates via temp file >> validate >> rename pattern.
end
```

---

## TEST Block (Validation/Invariants)

**Use when**: Defining how to verify correctness (assertions, invariants, validation)

```
TEST <Name>:
    sutra: "<what is being verified>"
    spec:
        target: <TERM, NORM, PROC, or PASS being tested>
        assertion: <condition that must be true>
        evidence: <how to verify (command, query, inspection)>
        failure_mode: <what happens if assertion fails>
        remedy: <how to fix if test fails>
    gloss:
        <Why this test matters>
        <What it catches>
end
```

**Example**:
```
TEST FlatPrincipleCompliance:
    sutra: "Verify all directories are flat (depth = 1)"
    spec:
        target: FlatPrinciple (NORM)
        assertion: "∀ dir ∈ {00-06}: ¬∃ subdir"
        evidence: "find {00,01,02,03,04,05,06}-* -type d -mindepth 2 | wc -l == 0"
        failure_mode: "Agent navigation broken | decision depth > 2"
        remedy: "mv subdirectory/* parent/ && rmdir subdirectory"
    gloss:
        Critical structural invariant for agent autonomy.
        Violations break Agentify + Human-Navigable lens (#9).
        Run after any directory structure changes.
end
```

---

## Composition Patterns

### Chaining Blocks

```
PROC <HighLevel>:
    steps:
        1. input >> PROC <SubProc1> >> intermediate
        2. intermediate >> PASS <Transform> >> processed
        3. processed | NORM <Constraint> >> output
end
```

### Referencing Terms in Specs

```
PROC Example:
    spec:
        requires: [TERM AxiologicalConstants, NORM FlatPrinciple]
        produces: [ARTIFACT DYN-TASKS.csv]
end
```

### Nested Definitions

```
TERM Constellation:
    spec:
        members:
            - TERM Oracle
            - TERM Interpreter
            - TERM Compiler
        relations:
            coordinates: PROC Chorus
end
```

---

## Style Guidelines

### Sutra Writing
- Maximum 100 characters
- Use active verbs
- Focus on essence, not exhaustive detail
- Should be memorable/quotable

### Gloss Writing
- 2-4 sentences (not more)
- Explain WHY, not just WHAT
- Mention key tradeoffs or edge cases
- Use conversational but precise tone

### Spec Writing
- YAML-like structure (not strict YAML)
- Use SN operators (::, >>, |, =>) liberally
- Reference other blocks by name
- Prefer symbols from glossary (α, Ψ, Κ) over prose

### Operator Usage
- `::` for definitions ("X :: Y" = "X is defined as Y")
- `>>` for transforms ("A >> B" = "A transforms into B")
- `|` for constraints ("X | Y" = "X constrained by Y")
- `=>` for implications ("X => Y" = "X implies Y")
- `:=` for binding/assignment ("var := value")

---

## Anti-Patterns (DON'T)

❌ **Redundant gloss**: Don't just restate the sutra in prose
❌ **Exhaustive specs**: Don't enumerate every edge case
❌ **Missing sutra**: Every block needs one-line summary
❌ **Prose operators**: Don't write "transforms into" when ">>" works
❌ **Flat glossaries**: Don't define 50 terms in one file; use hierarchical TERM blocks

---

## Conversion Workflow

When converting existing prose to SN:

1. **Identify block types**
   - Definitions → TERM
   - Rules/constraints → NORM
   - Procedures → PROC
   - Pure transforms → PASS
   - File references → ARTIFACT
   - Verification → TEST

2. **Extract sutra** (one-liner essence)

3. **Distill gloss** (2-4 sentences, WHY not WHAT)

4. **Structure spec** (YAML-like, use operators)

5. **Test round-trip**:
   ```bash
   cat original.md | sn_encode.py - | sn_decode.py -
   ```

6. **Measure compression**:
   ```bash
   echo "$(wc -c < original.md) → $(wc -c < encoded.md) bytes"
   ```

---

## Version History

- **v1.0.0** (2026-01-23): Initial template set

---

**Status**: Canonical template library for Semantic Notation blocks.
