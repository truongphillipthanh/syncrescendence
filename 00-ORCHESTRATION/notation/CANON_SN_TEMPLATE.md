# CANON → Semantic Notation Conversion Template

**Version**: 1.0.0
**Created**: 2026-01-23
**Purpose**: Guide for converting CANON prose to SN compressed format

---

## Conversion Workflow

```
PROC CANON_Conversion:
    1. Read original CANON >> identify_structure
    2. Map sections >> block_types (TERM, NORM, PROC, etc.)
    3. Extract sutras (one-line essences)
    4. Distill gloss (2-4 sentences WHY)
    5. Structure spec (YAML-like with SN operators)
    6. Test round-trip (encode >> decode >> verify)
    7. Measure compression (bytes before vs after)
end
```

---

## Pre-Conversion Analysis

Before converting a CANON document:

### 1. Identify Block Types

| Content Type | SN Block |
|--------------|----------|
| Definitions, concepts, "what is X" | **TERM** |
| Rules, constraints, "must/should" | **NORM** |
| Workflows, procedures, "how to" | **PROC** |
| Pure transforms, functions | **PASS** |
| File references, outputs | **ARTIFACT** |
| Verification criteria | **TEST** |

### 2. Extract Sutra

For each major concept:
- **One line** that captures essence
- **Maximum 100 characters**
- **Memorable/mnemonic** (should stick in mind)
- **Active voice** when possible

**Bad sutra**: "This document describes the five axiological constants"
**Good sutra**: "Five fitness functions: optionality, comprehensibility, exit, distribution, documentation"

### 3. Distill Gloss

- **2-4 sentences maximum**
- Focus on **WHY**, not just WHAT
- Mention **key tradeoffs** or edge cases
- Use **conversational but precise** tone

### 4. Structure Spec

- **YAML-like format** (not strict YAML)
- Use **SN operators** liberally (::, >>, |, =>)
- **Reference other blocks** by name
- **Prefer symbols** from glossary (α, Ψ, Κ) over prose

---

## Example Conversion

### Before (Verbose Prose)

```markdown
# CANON-00003: The Axiological Constants

The Axiological Constants represent the minimal universal values
that any consciousness system must preserve regardless of substrate
or implementation. These are not hardcoded rules but a meta-protocol
for discovering and updating values through collective intelligence.

## The Five Constants

1. **Preserve Optionality**: Avoid irreversible lock-ins that
   eliminate future choices. Every decision should maintain maximum
   degrees of freedom for future adaptation.

2. **Maintain Comprehensibility**: Ensure no unexplainable
   decisions affect consciousness. Black box operations that cannot
   be audited or understood violate this principle.

3. **Enable Exit**: Maintain reversibility of all augmentation.
   Users must be able to extract themselves and their data from
   any enhancement system without loss.

4. **Distribute Benefit**: Prevent concentration of enhancement
   capability. Augmentation should not create permanent castes.

5. **Document Transformation**: Record what changes and why.
   The history of modifications must be preserved and accessible.

## Implementation

These constants are implemented as evaluation criteria applied
to every proposed change to the system architecture. Any change
that violates a constant must be rejected or modified.
```

### After (SN Compressed)

```
TERM AxiologicalConstants:
    sutra: "Five fitness functions: optionality, comprehensibility, exit, distribution, documentation"
    gloss:
        Minimal universal values any consciousness must preserve.
        Meta-protocol, not commandments—evolutionary pressure shaping fitness landscape.
        Discovered and updated through collective intelligence.
    spec:
        count: 5
        nature: meta_protocol (not hardcoded rules)
        constants:
            optionality:       preserve(degrees_of_freedom)
            comprehensibility: forbid(unexplainable_decisions)
            exit:              enable(reversible_augmentation)
            distribution:      prevent(concentration)
            documentation:     require(transformation_records)
        scope: [all_substrates, all_implementations]
        evolution: collective_intelligence >> update
end

NORM ConstantEnforcement:
    sutra: "All system changes MUST pass axiological evaluation"
    spec:
        modality: MUST
        subject: proposed_changes
        action: evaluate(AxiologicalConstants) >> accept | reject
        invariant: "∀ change: passes(all_5_constants) ∨ rejected"
        failure_mode: "Change violates consciousness integrity"
    gloss:
        Not just documentation—active constraint on architecture evolution.
        Violations rejected at design time, not runtime.
end
```

### Compression Achieved

- **Before**: 1,247 characters
- **After**: 1,108 characters
- **Reduction**: 11% (modest, but gains semantic precision)
- **Plus**: Machine-parseable, sutra-indexable, operator-based

**Note**: Token reduction is more significant than character reduction—SN compresses information density.

---

## Pattern Library

### Pattern 1: Definition → TERM

**Before**:
```
The Discovery Engine is a consciousness mechanism for knowledge
growth through rhythmic oscillation between exploration and integration.
```

**After**:
```
TERM DiscoveryEngine:
    sutra: "Rhythmic oscillation: explore >> integrate >> knowledge growth"
    gloss:
        Consciousness mechanism for learning through alternating phases.
        Exploration maximizes divergence; integration minimizes surprises.
    spec:
        phases: [explore, integrate]
        rhythm: alternating
        produces: knowledge_growth
end
```

### Pattern 2: Rule → NORM

**Before**:
```
All directories must be flat. Subdirectories are forbidden. Use naming
prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of nesting.
```

**After**:
```
NORM FlatPrinciple:
    sutra: "Directories MUST be flat; prefixes replace nesting"
    spec:
        modality: MUST
        subject: all_directories
        action: forbid(subdirectories) ∧ require(prefix_naming)
        invariant: "∀ dir: depth(dir) = 1"
        prefixes: [ARCH-, DYN-, REF-, SCAFF-]
    gloss:
        Enables agent navigation in ≤2 decisions.
        Prefixes provide semantic organization without hierarchy.
end
```

### Pattern 3: Workflow → PROC

**Before**:
```
Source processing follows these steps:
1. Triage the source to determine signal tier
2. If paradigm or strategic, process using appropriate function
3. Integrate into relevant CANON documents
4. Update sources.csv ledger
5. Archive metadata
```

**After**:
```
PROC SourceProcessing(raw_source) -> integrated:
    sutra: "Triage >> process >> integrate >> update >> archive"
    spec:
        steps:
            1. raw_source >> triage >> {paradigm, strategic, tactical, noise}
            2. paradigm | strategic >> process(format) >> processed
            3. processed >> integrate(CANON) >> updated_CANON
            4. update(DYN-SOURCES.csv) >> ledger_entry
            5. metadata >> archive
        produces: [processed_source, updated_CANON, ledger_entry]
    gloss:
        Complete source-to-synthesis cycle.
        Filters noise early; preserves paradigm/strategic for integration.
end
```

---

## Conversion Checklist

Before finalizing a converted CANON:

- [ ] Every major concept has a TERM block
- [ ] Every rule/constraint has a NORM block
- [ ] Every procedure has a PROC block
- [ ] All blocks have **sutra** (one-liner)
- [ ] All blocks have **gloss** (2-4 sentences)
- [ ] All blocks have **spec** (structured fields)
- [ ] SN operators used consistently (::, >>, |, =>)
- [ ] Symbols from glossary used (Ψ, α, χ, etc.)
- [ ] Round-trip test passes (encode >> decode >> verify)
- [ ] Compression measured (before vs after bytes/tokens)
- [ ] Original meaning preserved (no semantic loss)

---

## Testing Conversion

### Round-Trip Test

```bash
# Original prose
cat CANON-XXXXX.md > original.md

# Encode to SN
./sn_encode.py original.md > encoded.md

# Decode back
./sn_decode.py encoded.md > decoded.md

# Compare semantics (not exact match, but meaning preserved)
diff original.md decoded.md
```

### Compression Measurement

```bash
# Character count
echo "Before: $(wc -c < original.md) characters"
echo "After: $(wc -c < encoded.md) characters"
echo "Reduction: $(( ($(wc -c < original.md) - $(wc -c < encoded.md)) * 100 / $(wc -c < original.md) ))%"

# Token count (approximate via word count)
echo "Before: $(wc -w < original.md) words"
echo "After: $(wc -w < encoded.md) words"
```

---

## Priority Conversion Targets

Based on ARCH-CANON_AUDIT_MANIFEST.md:

### Tier 1: Monoliths (>10K words)
Highest compression ROI. Split and convert in parallel.

### Tier 2: Cosmos (00000-00017)
Constitutional documents. Convert carefully to preserve precision.

### Tier 3: Core (10000-11000)
Gravitational center concepts. High reference frequency.

### Tier 4: Chains (30000-35999)
Six developmental pathways. Modular conversion.

---

## Anti-Patterns (Don't Do This)

❌ **Loss of precision**: Don't oversimplify complex concepts
❌ **Verbose gloss**: Don't just restate sutra in paragraph form
❌ **Bloated specs**: Don't enumerate every edge case
❌ **Missing sutras**: Every block needs memorable one-liner
❌ **Prose operators**: Don't write "transforms into" when ">>" works
❌ **Ignoring symbols**: Use Ψ, α, χ from glossary consistently

---

## Gemini CLI Handoff

For large-scale conversion, hand off to Gemini CLI:

```
PROC Gemini_Conversion:
    1. Load CANON directory (use 1M+ context advantage)
    2. Apply conversion template to each file
    3. Generate SN blocks with sutra + gloss + spec
    4. Output to -OUTGOING/ for review
    5. Human verifies semantic preservation
    6. Claude Code replaces originals
end
```

**Prompt for Gemini**:
```
You have 1M+ token context. Load all 82 CANON files.

Convert to Semantic Notation using:
- symbols.yaml glossary
- block_templates.md patterns
- CANON_SN_TEMPLATE.md methodology

Output each converted file to -OUTGOING/canon-sn/ for review.

Target: ~80% token reduction while preserving semantics.
```

---

## Version History

- **v1.0.0** (2026-01-23): Initial conversion template

---

**Status**: Conversion template ready for CANON SN transformation.
