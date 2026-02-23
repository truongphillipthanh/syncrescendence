# Agents Configuration

This file configures AI agents (Codex CLI, etc.) for the Syncrescendence repository.

## Repository Overview

Syncrescendence is a knowledge management system demonstrating AI-amplified individual capability at institutional scale. It uses a numbered directory structure with flat file organization.

## Directory Structure

- `00-ORCHESTRATION/` — Strategic coordination (directives, logs, state)
- `01-CANON/` — Verified canonical knowledge (PROTECTED)
- `02-ENGINE/` — Functions, prompts, model profiles, queue items
- `04-SOURCES/` — Source documents (raw/, processed/)
- `05-SIGMA/` — Operational knowledge corpus + memory + exempla
- `agents/<agent>/outbox/` — Agent output staging
- `agents/`/inbox — Incoming artifacts from external platforms

## Constitutional Rules

### ABSOLUTE: Structure
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes instead of subdirectories.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00-06 plus agents/
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit approval for deletions.

### ABSOLUTE: Operations
4. **ATOMIC UPDATES**: CSV updates use temp file → validate → rename pattern.
5. **VERIFICATION BEFORE COMPLETION**: Never claim done without running verification.
6. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes (feat:, fix:, docs:, chore:, refactor:).

## Common Tasks

### Run Verification
```bash
make verify
```

### Update Ledgers
```bash
make update-ledgers
```

### Generate Tree
```bash
make tree
```

### Create Handoff Token
```bash
make token PHASE=current NEXT=next
```

## File Naming Conventions

- CANON: `CANON-NNNNN-TITLE-variant.md`
- Sources: `SOURCE-YYYYMMDD-platform-format-creator.md`
- Directives: `DIRECTIVE-NNN-TITLE.md`
- State files: `DYN-*.md` (dynamic), `REF-*.md` (reference)

## Dispatch System

The `.dispatch/` directory contains watch folders for agent coordination:
- `claude-lead/` — Primary Claude agent work
- `claude-parallel/` — Secondary Claude agents
- `codex/` — Codex CLI tasks
- `gemini/` — Gemini CLI tasks

Each agent folder has: `pending/`, `processing/`, `complete/`

## Anti-Patterns (PROHIBITED)

- Creating subdirectories anywhere
- Skipping verification to "save time"
- Modifying state/ without validation
- Claiming integration without grep verification
