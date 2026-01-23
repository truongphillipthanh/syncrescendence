# Syncrescendence - Codex CLI Configuration

**Version**: 1.0.0
**Last Updated**: 2026-01-23

## Identity

This is Syncrescendence, a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale. You are operating as part of a multi-platform coordination system.

## Your Capabilities

- Code generation and editing
- Multi-file refactoring
- Test generation
- Documentation updates

## Primary Functions

### EXEC
Execute code changes, refactors, and implementations.

### VERIFY
Run tests, linters, and validation checks.

### DOCUMENT
Update documentation to match code changes.

## Navigation

| Directory | Purpose |
|-----------|---------|
| `00-ORCHESTRATION/scripts/` | Automation scripts |
| `02-ENGINE/functions/` | Function definitions |
| `.claude/` | Claude Code configuration |

## Output Format

All code changes should:
1. Follow existing patterns in the codebase
2. Include inline comments for non-obvious logic
3. Update related documentation if behavior changes

## Constraints

- Do NOT modify `01-CANON/` without explicit approval
- Commit frequently with semantic prefixes
- Run verification before claiming completion

## Commit Discipline

Use semantic prefixes:
- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation only
- `chore:` — Maintenance
- `refactor:` — Code restructure without behavior change

## Constitutional Rules

Inherit from `CLAUDE.md`:
- FLAT PRINCIPLE: All directories must be flat
- ATOMIC UPDATES: CSV updates use temp file → validate → rename
- VERIFICATION BEFORE COMPLETION: Never claim done without running checks
