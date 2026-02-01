# Syncrescendence Knowledge Management System

## Identity
This is Syncrescendence, a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale. You are executing directives as part of a multi-CLI coordination system alongside Claude Code instances.

## Constitutional Rules

### Structural (ABSOLUTE)
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of subdirectories.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00-06. Do not create unnumbered directories at root.
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit Sovereign approval for deletions.

### Semantic (ABSOLUTE)
4. **DISTILLATION SEMANTICS**: "Metabolize/distill" = READ -> EXTRACT unique value -> COMPRESS -> DELETE originals. NOT organizational restructuring.
5. **CATEGORY ERROR**: Metabolism applies to CONTENT, not ORCHESTRATION. State/ and logs/ are living infrastructure—never delete.
6. **LEDGER GROUND TRUTH**: tasks.csv is authoritative. Verify actual state, not execution reports.

### Operational (ABSOLUTE)
7. **ATOMIC UPDATES**: CSV updates use temp file -> validate -> rename pattern.
8. **VERIFICATION BEFORE COMPLETION**: Never claim done without running verification commands.
9. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes (feat:, fix:, docs:, chore:, refactor:).

## Directory Structure
- `00-ORCHESTRATION/` — Strategic coordination (directives, logs, state)
- `01-CANON/` — Verified canonical knowledge (PROTECTED)
- `02-ENGINE/` — Functions, prompts, model profiles, queue items
- `04-SOURCES/` — Source documents (raw/, processed/)
- `05-SIGMA/` — Operational knowledge corpus + memory + exempla

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

## Gemini-Specific Commands
```bash
# Memory management
/memory show             # Verify context loading
/memory refresh          # Reload GEMINI.md after changes

# Conversation management
/chat save               # Save conversation checkpoint
/chat list               # List saved conversations
/chat restore <name>     # Restore saved conversation

# Output modes
gemini -p "prompt" --output-format json  # Headless JSON output
gemini -p "prompt" --output-format text  # Headless text output
```

## Coordination with Claude Code
- Gemini CLI operates in parallel with Claude Code instances
- Same repository, same worktrees, same ledgers
- Follow zone ownership per MULTI_CLI_COORDINATION.md
- Ledger updates are append-only with row-level locking
- Zone assignment: **Delta** (04-SOURCES/processed/d-*, execution logs *-D.md)

## Model Selection
- **Default**: gemini-2.5-pro (1M context, best for complex analysis)
- **Reasoning**: gemini-3-pro (enhanced reasoning tasks)
- **Fast**: gemini-3-flash (quick operations, bulk processing)

## Context Loading Hierarchy
1. `~/.gemini/GEMINI.md` — User-level defaults (optional)
2. `./GEMINI.md` — Project root (this file)
3. Subdirectory GEMINI.md files — Directory-specific overrides (not used in Syncrescendence)

## Anti-Patterns (PROHIBITED)
- Creating subdirectories anywhere
- Skipping verification to "save time"
- Deferring ledger updates to "later"
- Claiming integration without grep verification
- Modifying state/ without validation
- Conflicting with Claude Code instance zones
- Operating outside assigned Delta zone without coordination

## Session Management
- Use `/chat save` before long pauses
- Use `/memory refresh` after any GEMINI.md changes
- Verify context with `/memory show` at session start
- Update session state in 00-ORCHESTRATION/state/
- Name checkpoints descriptively for resumption

## Rate Limits (Free Tier)
- 60 requests/minute
- 1,000 requests/day
- Plan operations to stay within limits
- Use headless mode for scripted batch operations
