# QUEUE PREP: Screenplay Formatting
## Preparation for Claude 3 Execution
**Created**: 2025-12-31
**Created by**: Claude 2 (DIRECTIVE-025A)

---

## Source Files

**Current Location**: `QUEUE/specialized/modal2_production/screenplay_formatting/`

| File | Size | Description |
|------|------|-------------|
| Technology Lunar - Agentic ScreenplayFormatting.md | ~36K | Main specification |
| Technology Lunar - Screenplay Formatting - agentic_screenplay_format.md | ~11K | Format details |
| Technology Lunar - Screenplay Formatting - screenplay_manual.md | ~18K | Manual/reference |
| Technology Lunar - Screenplay Formatting - culmination.md | ~7K | Summary/overview |
| Technology Lunar - Screenplay Formatting - validation.md | ~4K | Validation rules |

**Total**: ~76K characters across 5 files

---

## Oracle7 Disposition

**Decision**: QUEUE (Modal 2)
**Rationale**: Future modality — screenplay formatting for AI orchestration is Modal 2 content

### What This Is

An adaptation of traditional screenplay format for AI systems orchestration:
- Coordinates AI agents, tools, and human operators
- Uses screenplay conventions (slug lines, action lines, dialogue)
- Designed for both human readability and machine parseability
- Compatible with professional screenplay software

### Why QUEUE Not CANON

1. **Modal 2 content**: This is production/creation modality, not core framework
2. **Future use**: Not currently active in Principal's workflows
3. **Specialized**: Very specific use case (screenplay-style orchestration notation)
4. **Experimental**: Novel format, not battle-tested

---

## Recommended Consolidation

### Consolidate 5 Files → 1 QUEUE Item

**Proposed**: `QUEUE-36200-SCREENPLAY_ORCHESTRATION-Modal2.md`

### Rationale

1. The 5 files have significant overlap
2. Single consolidated file is more maintainable
3. QUEUE items should be atomic and self-contained
4. Easier to evaluate expiration

### Consolidation Strategy

1. **Primary content**: Technology Lunar - Agentic ScreenplayFormatting.md (most comprehensive)
2. **Supplement from**: Other 4 files where they add unique value
3. **Remove**: Redundant explanations, duplicate sections
4. **Target size**: ~30K (60% reduction from 76K)

---

## QUEUE Frontmatter Draft

```yaml
---
queue_id: "36200"
title: "Screenplay Orchestration Format"
category: specialized
modality: Modal2  # Production/Creation
status: queued
created: 2025-12-31
expiration: "2-cycles-from-Modal2-activation"
priority: low
summary: >
  Screenplay-format notation system for AI systems orchestration.
  Adapts industry-standard screenplay conventions for coordinating
  AI agents, tools, and human operators.
dependencies: []
activation_trigger: "Modal 2 production workflows begin"
---
```

---

## Content Outline for Consolidated Version

### 1. PURPOSE STATEMENT

- What this format is
- What it's for (copiloting, autonomous agents, swarms, etc.)
- Compatibility (Final Draft, WriterDuet, etc.)

### 2. CORE FORMATTING ELEMENTS

- Scene Structure (Slug Lines for agent context)
- Action Lines (system state)
- Character Identification (agent designation)
- Dialogue (prompts, commands, outputs)
- Parentheticals (metadata, constraints)
- Transitions (handoffs, state changes)

### 3. PRODUCTION ELEMENTS

- Title Page (deployment metadata)
- Scene Numbers (execution sequence)
- Revision Marks (version control)
- Production Notes (operational constraints)

### 4. ORCHESTRATION PATTERNS

- Simple Copilot (human-AI pair)
- Autonomous Agent (single agent)
- Multi-Agent Swarm (coordinated agents)
- Portal Prompts (human-operated multi-LLM)

### 5. VALIDATION RULES

- Format validation checklist
- Common errors
- Linting rules

---

## Expiration Policy

**Expiration**: 2 cycles from Modal 2 activation

### What This Means

1. When Modal 2 (production/creation) workflows begin, this content becomes active
2. If not used within 2 review cycles after activation, delete
3. If used, promote to CANON or keep in QUEUE based on utility

### Review Trigger

- [ ] Modal 2 workflows activated
- [ ] Content reviewed for utility
- [ ] Decision: Promote to CANON / Keep in QUEUE / Delete

---

## Execution Instructions for Claude 3

1. **Consolidate** 5 files into single `QUEUE-36200-SCREENPLAY_ORCHESTRATION-Modal2.md`
2. **Apply** QUEUE frontmatter as drafted above
3. **Target** ~30K characters consolidated
4. **Remove** redundant content across files
5. **Delete** original 5 files from `QUEUE/specialized/modal2_production/screenplay_formatting/`
6. **Place** consolidated file in `QUEUE/` root (or `QUEUE/specialized/`)
7. **Delete** empty directory

---

## Verification Checklist

- [ ] All 5 source files reviewed for unique content
- [ ] Consolidated file contains all essential content
- [ ] Redundancy eliminated
- [ ] QUEUE frontmatter complete with expiration
- [ ] Original files deleted
- [ ] Empty directory removed

---

**READY FOR CLAUDE 3 EXECUTION**
