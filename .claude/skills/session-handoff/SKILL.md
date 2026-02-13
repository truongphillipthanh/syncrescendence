---
name: session-handoff
description: Session terminal node protocol; ensures clean state persistence and pedigree chain continuity when an agent session ends
wraps: session-handoff (vibeship)
provenance: vibeship (MIT)
vetted: 2026-02-12
pipeline_stages: [COMMIT, MEMORY]
---

# Session Handoff

## Syncrescendence Integration

**Agents:** All constellation agents (Ajna, Psyche, Commander, Adjudicator, Cartographer)

This skill defines the terminal node protocol for agent sessions. When a session ends -- whether by completion, timeout, or explicit shutdown -- the agent must execute a clean handoff sequence that preserves state and maintains pedigree chain continuity.

### How it fits the pipeline

- **COMMIT stage (final):** Any uncommitted work must be committed or explicitly stashed with a note before session termination. No silent work loss.
- **MEMORY stage (final):** The agent persists a session summary to its memory namespace, capturing:
  - What was accomplished (completed directives)
  - What remains (open tasks, blockers)
  - Key decisions made and their rationale
  - Any state changes that the next session must be aware of
- **Pedigree hook chain feed:** The session handoff record becomes an input to the pedigree system, creating a traceable lineage from session to session.
- **Next-session bootstrap:** The handoff artifact is designed to be the first thing the next session reads, enabling cold-start continuity without re-deriving context from scratch.

### Config notes

- Handoff files are written to the agent's state directory under `00-ORCHESTRATION/state/`.
- The handoff format must include: session ID, timestamp, agent identity, completed items, pending items, and blockers.
- Commander's handoff additionally includes the current plan state and dispatch queue status.
- Cartographer's handoff includes any updated dependency graphs or architecture maps.

## Original Reference

@~/.agents/skills/session-handoff/SKILL.md
