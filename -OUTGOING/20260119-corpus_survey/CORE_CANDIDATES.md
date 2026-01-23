# Core Candidates

**Date**: 2026-01-19

This document identifies the smallest set of files that currently behave as a "cognitive core"—the things that actually steer behavior.

---

## 1. Project Instructions Prompt

### Current Path
`02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md`

### Why It's Core
- Defines the Deviser role for ChatGPT
- Specifies trifurcation output shape (readable + transcript + directives)
- Documents Blitzkrieg trigger semantics
- Establishes lane assignments (A/B/C)
- Contains container format spec for automation

### Version
`v3.0.0` (updated 2026-01-19 — retired `===AUDIZABLE===` markers)

### Suggested End-State Location
`00-ORCHESTRATION/core/CORE-PROJECT_INSTRUCTIONS.md`

### Dependencies
- `REF-AUDIZER_PROTOCOL.md` (transcript format)
- `REF-CHATGPT_CONTAINER_PROTOCOL.md` (container grammar)
- `REF-BLITZKRIEG_PROTOCOL_VNEXT.md` (lane model)

---

## 2. Global Memory Prompt

### Current Path
`02-ENGINE/prompts/chatgpt/PROMPT-CHATGPT-GLOBAL_MEMORY_REGISTRATION.md`

### Why It's Core
- Establishes cross-chat preferences in ChatGPT
- Defines trifurcation rule for all chats
- Sets Blitzkrieg semantics globally
- Establishes repo semantics (-INBOX/-OUTGOING)

### Suggested End-State Location
`00-ORCHESTRATION/core/CORE-GLOBAL_MEMORY.md`

### Dependencies
- Project instructions (must be consistent)

---

## 3. Container/Transcript Protocol

### Current Paths
- `00-ORCHESTRATION/state/REF-CHATGPT_CONTAINER_PROTOCOL.md` (container grammar)
- `02-ENGINE/specs/REF-AUDIZER_PROTOCOL.md` (transcript format)

### Why It's Core
- Defines how ChatGPT output is parsed by automation
- Specifies transcript extraction method (final fenced block)
- Documents container markers for Blitzkrieg ingestion
- Critical for ChatGPT ↔ repo synchronization

### Version
Both at `v3.0.0` (updated 2026-01-19)

### Suggested End-State Location
- `00-ORCHESTRATION/core/CORE-CONTAINER_PROTOCOL.md` (merge both)
- Or keep separate: `CORE-TRANSCRIPT_FORMAT.md`, `CORE-CONTAINER_GRAMMAR.md`

### Dependencies
- `ingest_chatgpt_container.py` (parsing implementation)
- Project instructions (specifies format)

---

## 4. Validation Protocol

### Current Path
`00-ORCHESTRATION/state/REF-REPO_VALIDATION_PROTOCOL.md`

### Why It's Core
- Defines when and how to validate repo health
- Specifies validation commands to run
- Documents remediation patterns
- Critical for maintaining constitutional compliance

### Suggested End-State Location
`00-ORCHESTRATION/core/CORE-VALIDATION_PROTOCOL.md`

### Dependencies
- `structural_verify.sh` (implementation)
- `ops_lint.sh` (implementation)

---

## 5. /repo_validate Command

### Current Path
`.claude/commands/project/repo_validate.md`

### Why It's Core
- Provides instant access to validation via `/project:repo_validate`
- Orchestrates both structural and operational validation
- Produces auditable reports to `-OUTGOING/`

### Suggested End-State Location
Keep in `.claude/commands/project/` (command location is fixed)

### Dependencies
- `REF-REPO_VALIDATION_PROTOCOL.md` (procedure)
- `structural_verify.sh`, `ops_lint.sh` (scripts)

---

## 6. Audizer Protocol

### Current Path
`02-ENGINE/specs/REF-AUDIZER_PROTOCOL.md`

### Why It's Core
- Defines transcript transcoding rules
- Specifies TTS optimization guidelines
- Documents follow-along alignment principle
- Critical for audio accessibility

### Version
`v3.0.0` (updated 2026-01-19 — final fence convention)

### Suggested End-State Location
`00-ORCHESTRATION/core/CORE-AUDIZER_PROTOCOL.md`

### Dependencies
- Container protocol (delivery format)
- Project instructions (integration)

---

## 7. Constitutional Document

### Current Path
`CLAUDE.md` (root)

### Why It's Core
- Constitutional rules for all Claude Code sessions
- Defines structural rules (flat principle, numbered directories)
- Specifies semantic rules (distillation, ledger ground truth)
- Documents operational rules (atomic updates, verification)

### Suggested End-State Location
Keep at root (entry point convention)

### Dependencies
- All other core files must comply with constitution

---

## 8. System State

### Current Path
`00-ORCHESTRATION/state/system_state.json`

### Why It's Core
- Current state vector (Oracle number, Blitzkrieg number, mode)
- Ground truth for session initialization
- Updated after significant state changes

### Suggested End-State Location
Keep at `00-ORCHESTRATION/state/` (state location is appropriate)

### Dependencies
- All execution sessions should read this first

---

## Core Files Summary

| # | File | Current Location | Role | Suggested Core Path |
|---|------|------------------|------|---------------------|
| 1 | Project Instructions | `02-ENGINE/prompts/chatgpt/` | ChatGPT Deviser behavior | `00-ORCHESTRATION/core/CORE-PROJECT_INSTRUCTIONS.md` |
| 2 | Global Memory | `02-ENGINE/prompts/chatgpt/` | Cross-chat preferences | `00-ORCHESTRATION/core/CORE-GLOBAL_MEMORY.md` |
| 3 | Container Protocol | `00-ORCHESTRATION/state/` | Parsing grammar | `00-ORCHESTRATION/core/CORE-CONTAINER_PROTOCOL.md` |
| 4 | Audizer Protocol | `02-ENGINE/specs/` | Transcript format | `00-ORCHESTRATION/core/CORE-AUDIZER_PROTOCOL.md` |
| 5 | Validation Protocol | `00-ORCHESTRATION/state/` | Health checking | `00-ORCHESTRATION/core/CORE-VALIDATION_PROTOCOL.md` |
| 6 | /repo_validate | `.claude/commands/project/` | Command interface | Keep current |
| 7 | CLAUDE.md | Root | Constitution | Keep at root |
| 8 | system_state.json | `00-ORCHESTRATION/state/` | State vector | Keep current |

---

## Proposed Core Lattice Structure

```
00-ORCHESTRATION/
├── core/                              # NEW: Cognitive core files
│   ├── CORE-PROJECT_INSTRUCTIONS.md   # ChatGPT Deviser behavior
│   ├── CORE-GLOBAL_MEMORY.md          # Cross-chat preferences
│   ├── CORE-CONTAINER_PROTOCOL.md     # Parsing grammar
│   ├── CORE-AUDIZER_PROTOCOL.md       # Transcript format
│   └── CORE-VALIDATION_PROTOCOL.md    # Health checking
├── state/
│   └── system_state.json              # Keep current
└── ...

./CLAUDE.md                            # Keep at root (constitution)
.claude/commands/project/              # Keep current (command location)
```

---

## Migration Notes

1. **Do not migrate yet** — This is a calibration survey, not execution
2. Create `00-ORCHESTRATION/core/` only after consensus
3. Maintain backlinks from original locations if migrated
4. Update COCKPIT.md navigation after migration
5. Ensure ops_lint.sh covers new `core/` location
