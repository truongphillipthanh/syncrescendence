# Syncrescendence Knowledge Management System

**Version**: 2.1.0
**Last Updated**: 2026-01-11

## Identity
This is Syncrescendence, a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale. You are executing directives as part of a multi-Claude coordination system.

## Constitutional Rules

### Structural (ABSOLUTE)
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of subdirectories.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00-06. Do not create unnumbered directories at root.
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit Principal approval for deletions.

### Semantic (ABSOLUTE)
4. **DISTILLATION SEMANTICS**: "Metabolize/distill" = READ → EXTRACT unique value → COMPRESS → DELETE originals. NOT organizational restructuring.
5. **CATEGORY ERROR**: Metabolism applies to CONTENT, not ORCHESTRATION. State/ and logs/ are living infrastructure—never delete.
6. **LEDGER GROUND TRUTH**: tasks.csv is authoritative. Verify actual state, not execution reports.

### Operational (ABSOLUTE)
7. **ATOMIC UPDATES**: CSV updates use temp file → validate → rename pattern.
8. **VERIFICATION BEFORE COMPLETION**: Never claim done without running verification commands.
9. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes (feat:, fix:, docs:, chore:, refactor:).

## Directory Structure
- `00-ORCHESTRATION/` — Strategic coordination (directives, logs, state)
- `01-CANON/` — Verified canonical knowledge (PROTECTED)
- `02-OPERATIONAL/` — Functions, prompts, model profiles
- `03-QUEUE/` — Pending items by modal
- `04-SOURCES/` — Source documents (raw/, processed/)
- `05-ARCHIVE/` — Historical preservation
- `06-EXEMPLA/` — Templates and examples

## Critical Commands
```bash
make verify              # Run all validation checks
make update-ledgers      # Sync CSV ledgers with validation
make sync                # Pull latest, rebase, push
make tree                # Generate current tree
```

## Processing Patterns
- Source intake: See @00-ORCHESTRATION/state/REF-PROCESSING_PATTERN.md
- Ledger updates: See @00-ORCHESTRATION/state/REF-STANDARDS.md
- Verification: Run before ANY completion claim

## Anti-Patterns (PROHIBITED)
- Creating subdirectories anywhere
- Skipping verification to "save time"
- Deferring ledger updates to "later"
- Claiming integration without grep verification
- Modifying state/ without validation

## Extended Thinking
Use these triggers for complex analysis:
- `think` — Standard extended thinking (~4K tokens)
- `think hard` — Moderate depth (~8K tokens)
- `ultrathink` — Maximum depth (~32K tokens)

Use ultrathink for: architectural decisions, multi-step processing, forensic analysis.
Do NOT use for: simple lookups, single-file edits, routine commits.

## BLITZKRIEG MODEL SPECIFICATION

When issuing Blitzkrieg directives, Oracle specifies which model to use per stream:

### Model Selection Criteria

| Model | Use When | Characteristics |
|-------|----------|-----------------|
| **Opus 4.5** | Comprehensive directives, architectural decisions, complex synthesis | Deep reasoning, better judgment, worth the cost for strategic work |
| **Sonnet 4.5** | Clear tactical instructions, well-defined tasks, execution-heavy work | Fast, capable, cost-effective when task is well-specified |

### Extended Thinking Specification

Directives may include thinking level guidance:
- `ultrathink` (~32K tokens) — Complex architectural synthesis
- `megathink` (~10K tokens) — Moderate complexity reasoning
- `think` (~4K tokens) — Standard deliberation
- *(none)* — Let model self-regulate

### Directive Header Format

Each directive should include:
```yaml
Stream: A/B
Model: Opus 4.5 / Sonnet 4.5
Thinking: ultrathink / megathink / think / default
Estimated Duration: X minutes
```

### Default Behavior

- **Oracle strategic synthesis**: Opus 4.5 (ultrathink)
- **Blitzkrieg execution**: Sonnet 4.5 unless complexity warrants Opus
- **Repository maintenance**: Sonnet 4.5 (think)

## Session Management
- Use /compact before context fills
- Update session state in 00-ORCHESTRATION/state/
- Name sessions descriptively for resumption
