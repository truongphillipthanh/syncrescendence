# DESIGN DECISIONS LOG
## Syncrescendence Architectural Rationale
**Last Updated**: 2025-12-30
**Maintained by**: Claude agents under Principal direction

---

## Repository Architecture

### Three-Tier Structure (DIRECTIVE-016)

```
syncrescendence/
├── CANON/           # Constitutional (~60 files, ~2.4M chars)
│   ├── cosmos/      # 00xxx - System schema, operations, protocols
│   ├── core/        # 1xxxx - Identity, celestial body, facets
│   ├── lattice/     # 2xxxx - Cognitive palace, memory, context
│   └── chains/      # 3xxxx - Intelligence through Wisdom chain
├── OPERATIONAL/     # Active work (~25 files)
│   ├── prompts/     # Current system prompts
│   ├── functions/   # Active metaprompts
│   └── processing/  # Active work items
├── QUEUE/           # Pending with expiration (~10 files)
└── .decisions/      # Hidden audit trail (this file)
```

### Governing Principles

1. **Metabolism, not archival**: If worth keeping, worth canonizing/operationalizing
2. **Queue Half-Life**: 2 cycles to canonize or delete
3. **Bitter Lesson**: Simple structures that scale with context
4. **Antifragile**: System strengthens through pruning
5. **No Reference Tier**: Reference content either absorbed into CANON or deleted

### Target Metrics
- **~100 files** (from 658)
- **~3M chars** (from 12.7M)
- **3 visible directories** (from 20+)
- **Max 2 levels** depth

---

## System Prompt Architecture

### Superseded: Archetype Engineering (2025-12-29)

**What was tried**: Detailed persona specifications per lab with extensive behavioral instructions

**Problems encountered**:
1. Over-engineering created rigidity rather than flexibility
2. Formulaic outputs (models followed structure too mechanically)
3. Cross-model degradation (prompts didn't adapt to new generations)
4. Fighting model nature rather than leveraging strengths
5. Prompt inflation (synthesized versions 2-18x longer than deployed)
6. Maintenance burden (versioning chaos)

**Learning**: Models respond better to understanding the *user* than becoming a *persona*.

### Active: Reception Calibration Architecture

**Three-layer design**:

**Layer 0 - Principal Profile** (Who the user is):
- Cognitive profile (AuDHD characteristics)
- Communication preferences
- Anti-patterns
- Core values

**Layer 1 - Reception Calibration** (How to interpret requests):
- Ambiguity protocols
- Dynamic inquiry patterns
- Substance-first delivery
- Proportional depth matching

**Layer 2 - Lab Amplification** (Which model strengths to emphasize):
- Minimal platform-specific guidance (~200-300 chars)
- Focus on native model strengths

**Plus**: Agentic-first membrane (model-facing documents for capability self-awareness)

---

## Content Processing Evolution

### Five-Tier Document Lifecycle (Superseded by Three-Tier)

The original five-tier system:
```
QUEUE → OPERATIONAL → CANON
         ↓
      REFERENCE
         ↓
      HISTORY
```

**Problem identified**: Reference and History tiers created accumulation patterns that violated metabolic principle.

### Resolution (DIRECTIVE-016):

Collapsed to three visible tiers + hidden decisions:
- **QUEUE**: Pending items with explicit expiration
- **OPERATIONAL**: Living documents under active use
- **CANON**: Constitutional, immutable
- **.decisions**: Preserved learnings (hidden from main structure)

**Key change**: No reference tier. Content either graduates to CANON/OPERATIONAL or gets deleted. Learnings preserved in DESIGN_DECISIONS.md, not obsolete artifacts.

---

## Function Architecture

### Salvaged Functions (from legacy disposition)

**`harmonize` (Multi-Model Synthesis)**:
- Tetrad (4-model) and Chord (3-model) support
- Productive tension elaboration
- Harmonic assemblage (standalone artifacts)
- Dissonance resolution methodology

**`offload` (AuDHD Cognitive Support)**:
- Torrential stream acceptance
- Parallel solution-thread recognition
- 5-layer progressive summarization
- Compound knowledge lattice building

**`primer` (Topic Orientation)**:
- Zero-knowledge assumption
- 4-phase protocol: Foundations → Concept Architecture → Landscape → Integration
- Navigational competence vs. encyclopedic completeness

### Deprecation Principle

Functions deprecated when:
- Functionality absorbed by system prompts
- Capability superseded by newer function
- No validated use cases over 90 days

---

## CANON Cross-Reference Notes

### Verified Canonical Coverage

| Content Domain | CANON Location | Status |
|----------------|----------------|--------|
| Tone Library | CANON-31120/31121 | Complete |
| Curriculum/Syllabus | CANON-34110/34120 | Complete |
| Strategy | CANON-00005 | Complete |
| Neurodivergent Adaptations | CANON-35120 | Complete |
| Memory Architecture | CANON-25000 | Complete |
| Context Transition | CANON-25100 | Complete |

### Gap Analysis (as of 2025-12-30)

**QUEUE-36000**: Philosophical foundations (Metahumanism synthesis) - pending canonization decision
**QUEUE-35121**: Neurodivergent implementation detail - pending CANON-35120 expansion decision

---

## Metabolic Defrag Execution (DIRECTIVE-016)

### Deletions Executed (2025-12-30)

| Category | Files Deleted | Chars Removed |
|----------|---------------|---------------|
| staging/ | 887 | ~2.0M |
| remnants/annealment | 5 | ~134K |
| remnants/evaluation | 4 | ~147K |
| remnants/convergence | 2 | ~200K |
| review_queue/metahumanism | 8 | ~855K |
| review_queue/cognitive_palace | 14 | ~122K |
| reference/tech_lunar | 25 | ~300K |
| reference/transcendence_lunar | 32 | ~400K |
| reference/oracle0 | 90 | ~509K |
| Empty directories | 67+ | - |
| .DS_Store files | 41 | - |

**Total removed**: ~1,100+ files, ~4.6M+ chars

### Rationale Preserved

**Reference tier deletion**: Source material served CANON synthesis. Synthesis complete. Keeping sources after synthesis is hoarding, not preservation.

**Metahumanism deletion**: Unique value extracted to QUEUE-36000. Original 855K → consolidated 12K. 98% compression with concept preservation.

**Cognitive Palace implementation deletion**: CANON-20000 preserves ontology. Implementation files regenerate when needed. No operational value in cold storage.

---

## Principles Governing Future Decisions

1. **Delete over archive**: Don't preserve obsolete artifacts; preserve learnings here
2. **Metabolism over accumulation**: Regular excretion prevents bloat
3. **Canonize or delete**: No permanent reference tier
4. **Simple structures scale**: 2-level max depth
5. **Anti-fragile**: System strengthens through pruning
6. **Agentic-first**: Design for model consumption
7. **Queue expiration**: 2 cycles or delete

---

**END DESIGN DECISIONS LOG**
