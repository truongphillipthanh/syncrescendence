# Syncrescendence Cockpit
## System Navigation Index
**Last Updated**: 2026-01-18

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
| [coordination.yaml](./02-OPERATIONAL/coordination.yaml) | Platform constellation | Multi-agent work |

---

## Quick Navigation

### For Oracle Sessions
1. Load ORACLE[N]_CONTEXT.md from 00-ORCHESTRATION/oracle_contexts/
2. Check system_state.json for current state
3. Reference REF-STANDARDS.md for decisions

### For Execution Sessions
1. Read CLAUDE.md (constitution)
2. Check relevant DIRECTIVE-NNN.md in 00-ORCHESTRATION/directives/
3. Write to appropriate zone per coordination.yaml

### For Source Processing
1. Consult REF-PROCESSING_PATTERN.md
2. Update sources.csv with atomic writes
3. Process raw/ to processed/

### For Structural Maintenance
1. Run `./00-ORCHESTRATION/scripts/structural_verify.sh`
2. Review REF-STABILIZATION_PROCEDURE.md for defrag
3. Verify `-OUTGOING/` and `-INBOX/` exist; legacy `OUTGOING/` and `outgoing/` are prohibited (Constitutional Rule #4)

---

## Daily Ritual

1. [ ] Check git status for uncommitted work
2. [ ] Review system_state.json for current Oracle/Blitzkrieg
3. [ ] Scan 00-ORCHESTRATION/directives/ for pending work
4. [ ] Verify no orphan files at root (`ls *.md | grep -v CLAUDE | grep -v COCKPIT`)
5. [ ] Run structural_verify.sh if significant changes made

---

## Emergency Reference

| Situation | Action |
|-----------|--------|
| Crashout | Read crashout_postmortem.md, ground in repo |
| Memory mismatch | Trust repo, not platform memory |
| Collision | Check coordination.yaml zones |
| Uncertainty | Apply 18 lenses (REF-STANDARDS.md) |
| Structural drift | Run structural_verify.sh |

---

## Directory Map

```
.
├── CLAUDE.md              # Constitution (v2.2.0)
├── COCKPIT.md             # You are here
├── Makefile               # Build/verify commands
├── 00-ORCHESTRATION/      # Directives, logs, state, scripts
├── 01-CANON/              # Protected knowledge
├── 02-OPERATIONAL/        # Prompts, functions, coordination.yaml
├── 03-QUEUE/              # Pending work
├── 04-SOURCES/            # Source documents (raw/, processed/)
├── 05-ARCHIVE/            # Historical preservation
├── 06-EXEMPLA/            # Templates
├── -OUTGOING/             # Export staging, reinit capsules (EXCEPTION)
└── -INBOX/                # Incoming artifacts from external platforms (EXCEPTION)
```

**Root Exceptions**: Only `-OUTGOING/` and `-INBOX/` (dash-prefixed) are sanctioned beyond 00-06. Legacy `OUTGOING/` and lowercase `outgoing/` are PROHIBITED.

---

**This is your cockpit. Everything else is reachable from here.**
