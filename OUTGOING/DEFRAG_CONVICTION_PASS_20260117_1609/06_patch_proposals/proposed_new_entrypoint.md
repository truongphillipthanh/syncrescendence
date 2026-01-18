# Proposed New Entrypoint: COCKPIT.md
## Stable Wellhead for System Navigation
**Generated**: 2026-01-17T16:09:00Z
**Status**: PROPOSAL - Copy-paste ready

---

## I. RATIONALE

Currently the system has multiple entrypoints:
- CLAUDE.md (Claude Code constitution)
- REF-STANDARDS.md (18 lenses)
- TELEOLOGY passes (operational architecture)
- system_state.json (current state)

**Problem**: No single "start here" document for human orientation.

**Solution**: A COCKPIT.md that provides:
1. One-glance system state
2. Links to primary entrypoints
3. Daily ritual checklist
4. Quick reference table

---

## II. PROPOSED CONTENT

Create `/COCKPIT.md` with the following content:

```markdown
# Syncrescendence Cockpit
## System Navigation Index
**Last Updated**: [Auto-update with each significant commit]

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
```

---

## III. IMPLEMENTATION

**If approved, create with:**

```bash
cat > COCKPIT.md << 'EOF'
[paste content above]
EOF
git add COCKPIT.md
git commit -m "feat(docs): add COCKPIT.md as stable navigation entrypoint"
```

---

## IV. MAINTENANCE

COCKPIT.md should be updated when:
- Oracle number increments
- Blitzkrieg completes
- Directory structure changes
- New protected zones established

**Frequency**: Weekly or per-milestone

---

## V. ALTERNATIVE: NO NEW FILE

If Principal prefers no new root file:
- Keep navigation distributed across existing docs
- Accept that entrypoints remain implicit
- Document entrypoints in existing REF-STANDARDS.md or CLAUDE.md

**Recommendation**: Create COCKPIT.md. The system benefits from a single, stable wellhead.

---

**This is a proposal. Principal decides whether to implement.**
