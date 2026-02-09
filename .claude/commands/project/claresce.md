---
name: claresce
description: Run a clarescence cycle — value-guided progressive refinement
allowed-tools: Read, Write, Edit, Bash(git status:*), Bash(git diff:*), Bash(find:*), Bash(ls:*), Glob, Grep
---
# Clarescence Cycle

Run a clarescence procedure on: $ARGUMENTS (or the current strategic context if not specified)

## Invocation

This command invokes the clarescence skill defined in `.claude/skills/claresce.md`. Follow that skill's full procedure.

## Quick Reference

### Steps
1. **Gather inputs** — Topic, current state (read files, `git status`), options, constraints
2. **Determine fidelity** — Partial (passes 1-3) for tactical, Full (passes 1-10) for substrate-affecting
3. **Run the passes** — Triumvirate Calibration, 18+ Lenses, CANON Coherence, then optionally Omni-Qualities through Authenticity Gate
4. **Produce output** — Write record to `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-YYYY-MM-DD-<slug>.md`
5. **Update backlog** — Adjust `IMPLEMENTATION-MAP.md` and `DYN-GLOBAL_LEDGER.md`

### Fidelity Guide
- **Partial (1-3)**: Local decisions, low blast radius, reversible
- **Full (1-10)**: Architecture changes, irreversible coupling, substrate-affecting

### Output
- Clarescence record with: topic, fidelity, convergent path, rationale, dependencies, falsifier, confidence
- DecisionAtom if a binding decision is made
- Backlog updates

## Skill Reference
Full procedure: `.claude/skills/claresce.md`
Full runbook: `02-ENGINE/REF-CLARESCENCE_RUNBOOK.md`
