# Syncrescendence Knowledge Management System

**Version**: 2.3.0
**Last Updated**: 2026-01-18

## Identity
This is Syncrescendence, a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale. You are executing directives as part of a multi-Claude coordination system.

## Constitutional Rules

### Structural (ABSOLUTE)
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of subdirectories.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00-06 plus sanctioned exceptions. Do not create unnumbered directories at root.
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit Principal approval for deletions.
4. **SANCTIONED EXCEPTIONS**: `-OUTGOING/` and `-INBOX/` are the only non-numbered directories permitted at root. Legacy `OUTGOING/` and lowercase `outgoing/` are PROHIBITED.

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
- `02-ENGINE/` — Functions, prompts, model profiles
- `03-QUEUE/` — Pending items by modal
- `04-SOURCES/` — Source documents (raw/, processed/)
- `05-MEMORY/` — Historical preservation
- `06-EXEMPLA/` — Templates and examples
- `-OUTGOING/` — Export staging, reinit capsules, cross-platform handoffs
- `-INBOX/` — Incoming artifacts from external platforms

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

Blitzkrieg vNext supports three parallel execution lanes (A/B/C) across multiple toolchains.
Full protocol: `00-ORCHESTRATION/state/REF-BLITZKRIEG_PROTOCOL_VNEXT.md`

### Lane Model

| Lane | Primary Use | Default Assignment |
|------|-------------|--------------------|
| **A** | Strategic/architectural | claude_code (Opus) |
| **B** | Tactical execution | claude_code (Sonnet) or codex_cli |
| **C** | Validation/secondary | gemini_cli or claude_code (Haiku) |

### Toolchain Options

| Toolchain | Models Available |
|-----------|------------------|
| `claude_code` | opus-4.5, sonnet-4.5, haiku |
| `codex_cli` | codex, gpt-4o |
| `gemini_cli` | gemini-2.0-flash, gemini-pro |
| `chatgpt` | gpt-4o, gpt-4o-mini |
| `other` | operator-configured |

### Model Selection Criteria

| Model | Use When | Characteristics |
|-------|----------|-----------------|
| **opus-4.5** | Architectural decisions, complex synthesis | Deep reasoning, worth cost for strategic work |
| **sonnet-4.5** | Well-defined tasks, execution-heavy work | Fast, capable, cost-effective |
| **haiku** | Quick validations, simple lookups | Fastest, lowest cost |

### Extended Thinking Specification

| Level | Tokens | Use When |
|-------|--------|----------|
| `ultrathink` | ~32K | Architectural synthesis, complex multi-file changes |
| `megathink` | ~10K | Moderate complexity, multi-step reasoning |
| `think` | ~4K | Standard deliberation |
| `default` | auto | Let model self-regulate |

### Directive Header Format (vNext)

```yaml
Lane: A | B | C
Toolchain: claude_code | codex_cli | gemini_cli | chatgpt | other
Model: opus-4.5 | sonnet-4.5 | haiku | <custom>
Thinking: ultrathink | megathink | think | default
Success_Criteria: [Measurable completion conditions]
Inputs: [Files this lane reads]
Outputs: [Files this lane produces]
```

### Default Behavior

- **Oracle strategic synthesis**: Lane A, claude_code, opus-4.5 (ultrathink)
- **Tactical execution**: Lane B, claude_code, sonnet-4.5 (think)
- **Validation/secondary**: Lane C, gemini_cli or haiku (default)

### Blitzkrieg Commands

- `/project:blitzkrieg_issue <slug>` — Create bundle skeleton with directive templates
- `/project:blitzkrieg_finalize` — Generate return packet, audio scripts, agent relay JSON

## Semantic Notation (SN)

Syncrescendence uses Semantic Notation for ~80% token compression while preserving semantics.

### Core Elements
- **Symbols**: Ψ (Syncrescendence), Κ (CANON), Ο (ENGINE), Σ (SOURCE), Δ (DIRECTIVE), Λ (LOG)
- **Operators**: `::` (expands to), `|` (constrained by), `>>` (transforms into), `:=` (binds), `=>` (implies), `<->` (corresponds)
- **Block Types**: TERM (definitions), NORM (rules), PROC (workflows), PASS (transforms), ARTIFACT (outputs), TEST (validation)
- **Structure**: sutra (1-line essence), gloss (2-4 sentences WHY), spec (YAML-like structured detail)

### Usage
- **Encoding**: `00-ORCHESTRATION/scripts/sn_encode.py` (prose → SN)
- **Decoding**: `00-ORCHESTRATION/scripts/sn_decode.py` (SN → prose)
- **Templates**: `00-ORCHESTRATION/notation/block_templates.md`
- **Symbol glossary**: `00-ORCHESTRATION/notation/symbols.yaml`

### Platform Integration
- ChatGPT: Ideation + compilation to target languages
- Grok: Colloquial voice preservation in gloss sections
- Gemini: Oracle-level SN audits with 1M+ context
- Perplexity: Current intelligence with SN formatting

See `CHATGPT.md`, `GROK.md`, `GEMINI.md`, `PERPLEXITY.md` for platform-specific SN integration.

## Session Management
- Use /compact before context fills
- Update session state in 00-ORCHESTRATION/state/
- Name sessions descriptively for resumption
