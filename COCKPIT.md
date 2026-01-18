# Syncrescendence Cockpit
## System Navigation Index
**Last Updated**: 2026-01-17

---

## Current State

| Metric | Value |
|--------|-------|
| Current Oracle | 13 |
| Last Blitzkrieg | 046B |
| System Mode | Operational |
| Protected Zones | Intact |

---

## Primary Entrypoints

| Document | Purpose | When to Read |
|----------|---------|--------------|
| [CLAUDE.md](./CLAUDE.md) | Constitutional rules | Every Claude Code session |
| [REF-STANDARDS.md](./00-ORCHESTRATION/state/REF-STANDARDS.md) | 18 evaluative lenses | Before strategic decisions |
| [system_state.json](./00-ORCHESTRATION/state/system_state.json) | Current state vector | Before any execution |
| [coordination.yaml](./config/coordination.yaml) | Platform constellation | Multi-agent work |

---

## Quick Navigation

### For Oracle Sessions
1. Load ORACLE[N]_CONTEXT.md from oracle_contexts/
2. Check system_state.json for current state
3. Reference REF-STANDARDS.md for decisions

### For Execution Sessions
1. Read CLAUDE.md (constitution)
2. Check relevant DIRECTIVE-NNN.md
3. Write to appropriate zone per coordination.yaml

### For Source Processing
1. Consult REF-PROCESSING_PATTERN.md
2. Update sources.csv with atomic writes
3. Process raw/ to processed/

---

## Daily Ritual

1. [ ] Check git status for uncommitted work
2. [ ] Review system_state.json for current Oracle/Blitzkrieg
3. [ ] Scan 00-ORCHESTRATION/directives/ for pending work
4. [ ] Verify no orphan files at root (ls *.md)

---

## Emergency Reference

| Situation | Action |
|-----------|--------|
| Crashout | Read crashout_postmortem.md, ground in repo |
| Memory mismatch | Trust repo, not platform memory |
| Collision | Check coordination.yaml zones |
| Uncertainty | Apply 18 lenses (REF-STANDARDS.md) |

---

## Directory Map

```
.
├── CLAUDE.md              # Constitution
├── COCKPIT.md             # You are here
├── config/                # Platform coordination
├── 00-ORCHESTRATION/      # Directives, logs, state
├── 01-CANON/              # Protected knowledge
├── 02-OPERATIONAL/        # Prompts, functions
├── 03-QUEUE/              # Pending work
├── 04-SOURCES/            # Source documents
├── 05-ARCHIVE/            # Historical preservation
├── 06-EXEMPLA/            # Templates
└── OUTGOING/              # Teleology passes
```

---

**This is your cockpit. Everything else is reachable from here.**
