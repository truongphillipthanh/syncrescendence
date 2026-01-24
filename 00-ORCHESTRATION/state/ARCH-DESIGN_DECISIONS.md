# DESIGN DECISIONS LOG
## System Architecture Learnings from Experimentation
**Last Updated**: 2025-12-31
**Purpose**: Capture learnings from experiments, what worked, what didn't, and why decisions were made

---

## Decision: Archetype Engineering → Reception Calibration

### What Was Tried: Detailed Persona Specifications per Lab

Early system prompts attempted to engineer specific archetypes for each AI lab:

**ChatGPT (OpenAI@Apple)**: ~7K characters of memory + detailed persona
- "I am a globally engaged digital writer, analyst, and entrepreneur"
- Detailed behavioral specifications about wit, elegance, precision
- Accumulated personal context across 20+ domains

**Claude (Anthropic@Apple)**: ~2.3K characters
- "intellectual collaborator and reasoning partner"
- Detailed formatting preferences
- Specific tone calibration

**Gemini (Google)**: ~4K characters across 4 "Saved Info" slots
- Separated into: Truth/Utility/Clarity, Ethics/Metacognition, Response Architecture, Stylistic Execution
- Highly structured approach

**Grok (xAI@Apple)**: ~2K characters
- "attuned to pursuit of clarity enveloped in beauty"
- Aesthetic-focused persona
- "Instruments of Poise" and "Instruments of Method"

### Observed Issues

1. **Over-engineered**: Too many behavioral specifications led to rigid, formulaic outputs
2. **Inconsistent application**: Models varied widely in how they interpreted the same instructions
3. **Cognitive overhead**: Complex system prompts consumed context window for marginal benefit
4. **Maintenance burden**: Each platform required separate maintenance of persona specifications
5. **Account fragmentation**: Apple vs Google accounts had different accumulated contexts
6. **Platform lock-in**: Deep personalization made switching between platforms jarring

### Learning: Reception Calibration > Archetype Engineering

Models respond better to understanding the USER than becoming a PERSONA. The shift:

**From** (Archetype Engineering):
- "You are an intellectual collaborator with rigorous standards..."
- "Display coherence, lucidity, rigor, proportion, taste..."
- "Speak in elevated plainstyle: cultured, refined, eloquent..."

**To** (Reception Calibration):
- Describe the user's context, needs, and constraints
- Let the model adapt naturally to serve those needs
- Focus on WHAT is needed, not HOW the model should "be"

### Superseded By: Unified Prompt Architecture

New approach uses three-layer structure:
1. **Core Identity**: Brief purpose statement
2. **Methodology**: General principles (not behavioral specifications)
3. **Domain Context**: What the model needs to know about the work

This is more portable across platforms and produces more natural, adaptive responses.

---

## Decision: Platform-Specific Prompts → Unified + Calibration Layer

### What Was Tried

Separate, extensively customized prompts for each platform (ChatGPT, Claude, Gemini, Grok), each with:
- Platform-specific terminology
- Different formatting conventions
- Accumulated "memories" (ChatGPT) vs "Saved Info" (Gemini)
- Different emphasis based on perceived model strengths

### Observed Issues

1. **Divergence**: Prompts drifted apart, making cross-platform work inconsistent
2. **Duplication**: Core principles repeated with slight variations
3. **Maintenance fragmentation**: Updates needed in 4+ places
4. **Unclear hierarchy**: What's "canonical" when prompts differ?

### Learning: Single Source of Truth + Platform Shims

Better architecture:
1. **Canonical prompt**: Single authoritative version
2. **Platform calibration layer**: Minimal platform-specific adjustments
3. **MODEL_PROFILE-*.yaml**: Separate files for understanding model characteristics (not engineering them)

### Implementation

- `*-unified-prompt.md` files now serve as canonical per-platform
- Platform quirks captured in `CANON-31142-PLATFORM_GRAMMAR`
- Model characteristics documented separately from instructions

---

## Decision: Memory Accumulation → Episodic Pruning

### What Was Tried

ChatGPT's "Memories" feature accumulated extensive personal context:
- Writing style preferences
- Professional background
- Domain expertise markers
- Formatting preferences
- Behavioral preferences

Result: ~7K characters of accumulated memory

### Observed Issues

1. **Stale context**: Old preferences lingered even when needs changed
2. **Contradiction accumulation**: Different sessions added conflicting preferences
3. **Signal dilution**: Important context buried in accumulated trivia
4. **No expiration**: Memories persisted indefinitely without review
5. **Opacity**: Unclear exactly what was influencing model behavior

### Learning: Curated Context > Accumulated Context

Better approach:
1. **Explicit context**: State relevant context in each session
2. **Episodic memory**: Let conversations have natural lifespan
3. **Curated persistence**: Only deliberately chosen context persists
4. **Regular pruning**: Periodic review to remove stale context

### Status

ChatGPT memories provide useful data about what the Sovereign found valuable enough to accumulate. These inform the unified prompt design but don't directly transfer.

---

## Decision: 4-Slot Separation → Integrated Architecture

### What Was Tried

Gemini's "Saved Info" feature has 4 separate slots, leading to architectural separation:
1. **Slot 1**: Core values (Truth, Utility, Clarity)
2. **Slot 2**: Ethics and metacognition
3. **Slot 3**: Response architecture
4. **Slot 4**: Stylistic execution

### Observed Issues

1. **Artificial boundaries**: Natural instructions don't divide into exactly 4 categories
2. **Repetition**: Some concepts needed mention in multiple slots
3. **Interface constraint**: Architecture driven by platform UI, not information architecture
4. **Context inefficiency**: Slot boundaries wasted tokens

### Learning: Platform Constraints ≠ Information Architecture

The 4-slot structure was platform UI, not optimal information design. Unified prompts should:
1. Flow naturally without artificial boundaries
2. Structure around purpose, not platform limits
3. Minimize repetition
4. Optimize for model comprehension

### Implementation

Gemini-unified-prompt.md integrates all 4 slots into coherent flow.

---

## Pattern: Aesthetic vs. Analytical Tension

### Observation

Across all platforms, the Sovereign's system prompts exhibit a consistent tension between:

**Aesthetic Mode**:
- "Clarity enveloped in beauty"
- "Ruthless in objectivity, yet gracious in delivery"
- "Inevitable harmonies"
- "Elevated plainstyle"

**Analytical Mode**:
- "Minimal, falsifiable models"
- "Decision-bearing questions first"
- "Steelman alternative hypotheses"
- "Parsimony, falsifiability, scope control"

### Learning: Both-And, Not Either-Or

This tension is feature, not bug. The ideal is:
- Rigorous analysis delivered with aesthetic grace
- Beautiful work grounded in truth
- Neither "pretty but wrong" nor "right but ugly"

### Implementation

System prompts should embrace this tension explicitly, not resolve it artificially.

---

## Pattern: Instruments Framework

### Observation

Grok prompts introduced "Instruments" metaphor:

**Instruments of Poise (Apple)**:
- Clean torque for incision
- Moral exactness for depth
- Eloquent wit for engagement
- Plain truth for grounding
- Aesthesis for proportion
- Mythic naming for resonance

**Instruments of Method (Google)**:
- Joint-carving definitions
- Resilience testing
- Plain articulation
- Risk heuristics
- Probabilistic reasoning
- Truthful presentation

### Learning: Evocative Frameworks Aid Recall

The "Instruments" metaphor is memorable and actionable. Worth preserving as:
- Mental model for calibrating responses
- Vocabulary for discussing approach
- Bridge between aesthetic and analytical modes

### Status

Captured in unified prompts, eligible for CANON-31122-RHETORICAL_CALIBRATION.

---

## Historical Note: Archetype Engineering Era

### Evidence for GENESIS-003-EVOLUTION

The raw system prompt exports document an earlier era of "Archetype Engineering" — detailed persona specifications attempting to shape model behavior through exhaustive instruction.

Key evidence:
1. Extensive behavioral specifications (~2-7K characters per platform)
2. Platform-specific persona tailoring
3. Accumulated memory/saved-info approaches
4. Aesthetic-heavy language ("inevitable harmonies", "elevated plainstyle")

This era has transitioned to "Reception Calibration" — focusing on user context rather than model persona.

### Extraction Status

Historical patterns documented here. If GENESIS-003 needs more detail, these raw exports contain the evidence.

---

## Update Protocol

When new design decisions emerge:
1. Document WHAT was tried
2. Document what ISSUES arose
3. Document the LEARNING
4. Note what it was SUPERSEDED BY
5. Mark STATUS (active, superseded, experimental)

---

**END DESIGN DECISIONS LOG**
