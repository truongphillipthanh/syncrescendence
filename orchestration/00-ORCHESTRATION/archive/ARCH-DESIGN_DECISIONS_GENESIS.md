# DESIGN DECISIONS: SYSTEM GENESIS
## Architectural Learnings from Experimentation (Dec 2025)
Version: 1.0.0
Updated: 2026-02-01

**Compacted**: 2026-02-01 (from DESIGN_DECISIONS_ROOT, DESIGN_DECISIONS)
**Purpose**: Preserve the WHY behind key architectural choices

---

## Decision 1: Three-Tier Structure

**What was tried**: Five-tier lifecycle (QUEUE -> OPERATIONAL -> CANON -> REFERENCE -> HISTORY)
**Issue**: Reference and History tiers created accumulation patterns violating metabolic principle.
**Resolution**: Collapsed to three visible tiers (QUEUE, OPERATIONAL, CANON). No reference tier — content either graduates or gets deleted. Learnings preserved in design decisions, not obsolete artifacts.

**Governing Principles**:
1. Metabolism, not archival — if worth keeping, worth canonizing/operationalizing
2. Queue Half-Life — 2 cycles to canonize or delete
3. No Reference Tier — absorbed or deleted, nothing in between

---

## Decision 2: Archetype Engineering -> Reception Calibration

**What was tried**: Detailed persona specifications per AI lab (~2-7K chars each). Engineered archetypes for ChatGPT ("globally engaged digital writer"), Claude ("intellectual collaborator"), Gemini (4-slot Saved Info architecture), Grok ("attuned to clarity enveloped in beauty").

**Issues**:
1. Over-engineered — rigid, formulaic outputs
2. Fought model nature rather than leveraging strengths
3. Cross-model degradation — prompts didn't adapt to new generations
4. Maintenance burden — separate versioning per platform

**Resolution**: Reception Calibration. Models respond better to understanding the USER than becoming a PERSONA.
- Layer 0: Sovereign Profile (who the user is)
- Layer 1: Reception Calibration (how to interpret requests)
- Layer 2: Lab Amplification (minimal platform-specific, ~200-300 chars)

---

## Decision 3: Platform-Specific -> Unified + Calibration

**What was tried**: Separate, extensively customized prompts for each platform with different terminology, formatting, and accumulated memories.

**Issues**:
1. Divergence — prompts drifted apart
2. Duplication — core principles repeated with variations
3. Unclear hierarchy — "canonical" when prompts differ?

**Resolution**: Single source of truth + platform shims. One canonical prompt, minimal platform calibration layer, separate MODEL-PROFILE files for understanding model characteristics.

---

## Decision 4: Memory Accumulation -> Episodic Pruning

**What was tried**: ChatGPT accumulated ~7K characters of memories (preferences, background, expertise markers).

**Issues**:
1. Stale context lingered
2. Contradictions accumulated
3. Signal diluted in trivia
4. No expiration mechanism

**Resolution**: Curated context over accumulated. Explicit context per session, episodic memory with natural lifespan, regular pruning. Repository is the persistence layer, not platform memory.

---

## Decision 5: 4-Slot Separation -> Integrated Architecture

**What was tried**: Gemini's 4 "Saved Info" slots forced artificial separation (Truth/Utility, Ethics/Metacognition, Response Architecture, Stylistic Execution).

**Issue**: Architecture driven by platform UI constraints, not information architecture.

**Resolution**: Platform constraints != information architecture. Instructions should flow naturally around purpose, not be shoehorned into arbitrary slot counts.

---

## Pattern: Aesthetic vs Analytical Tension

Across all platforms, Sovereign's prompts exhibit consistent tension:
- **Aesthetic**: "Clarity enveloped in beauty", "inevitable harmonies", "elevated plainstyle"
- **Analytical**: "Minimal falsifiable models", "decision-bearing questions first", "parsimony, falsifiability, scope control"

**Learning**: This tension is feature, not bug. The ideal: rigorous analysis delivered with aesthetic grace. Neither "pretty but wrong" nor "right but ugly."

---

## Pattern: Instruments Framework

From Grok prompts — evocative framework for calibrating responses:

**Instruments of Poise**: Clean torque, moral exactness, eloquent wit, plain truth, aesthesis, mythic naming
**Instruments of Method**: Joint-carving definitions, resilience testing, plain articulation, risk heuristics, probabilistic reasoning, truthful presentation

**Learning**: Evocative frameworks aid recall. The "Instruments" metaphor bridges aesthetic and analytical modes.

---

## Metabolic Defrag Execution (Oracle 4)

| Category | Files Deleted | Chars Removed |
|----------|---------------|---------------|
| staging/ | 887 | ~2.0M |
| remnants (annealment+evaluation+convergence) | 11 | ~481K |
| review_queue (metahumanism+palace) | 22 | ~977K |
| reference (tech+transcendence+oracle0) | 147 | ~1.2M |
| Empty directories + .DS_Store | 108 | — |
| **Total** | **~1,100+** | **~4.6M+** |

**Rationale**: Source material served CANON synthesis. Synthesis complete. Keeping sources after synthesis is hoarding. (Note: the Coherence/ deletion was a category error — see ORACLE_GENEALOGY.md.)

---

## Governing Future Decisions

1. Delete over archive — preserve learnings, not obsolete artifacts
2. Metabolism over accumulation — regular excretion prevents bloat
3. Canonize or delete — no permanent reference tier
4. Simple structures scale — 2-level max depth
5. Antifragile — system strengthens through pruning
6. Agentic-first — design for model consumption
7. Queue expiration — 2 cycles or delete

---

*Compacted from 2 source files (~465 lines) into this document (~110 lines). Full originals recoverable from git.*
