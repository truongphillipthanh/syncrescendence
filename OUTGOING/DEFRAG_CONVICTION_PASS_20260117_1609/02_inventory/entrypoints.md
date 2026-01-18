# Canonical Entrypoints
## "If you start here, you understand the system"
**Generated**: 2026-01-17

---

## I. PRIMARY ENTRYPOINTS (Read These First)

### Entrypoint 1: CLAUDE.md
**Path**: `/CLAUDE.md`
**Purpose**: Constitutional rules for Claude Code execution
**Audience**: Any Claude Code session
**Contains**:
- 9 absolute rules (Structural, Semantic, Operational)
- Directory structure
- Anti-patterns
- Blitzkrieg model specification
- Session management

**When to Read**: At the start of ANY Claude Code session

---

### Entrypoint 2: REF-STANDARDS.md (18 Lenses)
**Path**: `/00-ORCHESTRATION/state/REF-STANDARDS.md`
**Purpose**: Evaluative framework for all decisions
**Audience**: Anyone making strategic decisions
**Contains**:
- 18 evaluative lenses with scoring criteria
- Application methodology
- Worked examples

**When to Read**: Before any constitutional or architectural decision

---

### Entrypoint 3: TELEOLOGY_PASS_4 Index
**Path**: `/OUTGOING/TELEOLOGY_PASS_4_20260117_1430/00_INDEX.md`
**Purpose**: Operational architecture overview
**Audience**: Anyone needing to understand current system state
**Contains**:
- Concierge cockpit constitution
- Chorus protocol
- Ring7 substrate
- Packet templates
- Crashout prevention

**When to Read**: When understanding how the system operates

---

## II. SECONDARY ENTRYPOINTS (Context-Specific)

### For Oracle Sessions
**Path**: `/00-ORCHESTRATION/oracle_contexts/ORACLE[N]_CONTEXT.md`
**Purpose**: Session continuity for Oracle synthesis
**When to Read**: Before starting Oracle synthesis session

### For Execution Sessions
**Path**: `/00-ORCHESTRATION/state/system_state.json`
**Purpose**: Current system state vector
**When to Read**: Before any execution work

### For Source Processing
**Path**: `/00-ORCHESTRATION/state/REF-PROCESSING_PATTERN.md`
**Purpose**: Source-to-synthesis cycle methodology
**When to Read**: Before processing any sources

### For Multi-Platform Coordination
**Path**: `/00-ORCHESTRATION/state/REF-MULTI_CLI_COORDINATION.md`
**Purpose**: Parallel execution zone ownership
**When to Read**: Before multi-agent work

---

## III. ENTRYPOINT FLOW

```
START
  │
  ▼
┌─────────────────────────────────────────────────┐
│ 1. Read CLAUDE.md                               │
│    (Constitutional rules)                       │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│ 2. Check system_state.json                      │
│    (Current state: Oracle #, Blitzkrieg #)     │
└─────────────────────┬───────────────────────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   STRATEGIC WORK           EXECUTION WORK
          │                       │
          ▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│ REF-STANDARDS   │     │ Relevant        │
│ (18 lenses)     │     │ directive       │
└─────────────────┘     └─────────────────┘
          │                       │
          ▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│ TELEOLOGY_PASS_4│     │ REF-PROCESSING  │
│ (operational    │     │ (if processing  │
│  architecture)  │     │  sources)       │
└─────────────────┘     └─────────────────┘
```

---

## IV. QUICK REFERENCE TABLE

| Question | Entrypoint |
|----------|------------|
| "What are the rules?" | CLAUDE.md |
| "How do I decide?" | REF-STANDARDS.md |
| "What's the current state?" | system_state.json |
| "How does the system operate?" | TELEOLOGY_PASS_4/00_INDEX.md |
| "What happened in Oracle 12?" | ORACLE12_CONTEXT.md |
| "How do I process sources?" | REF-PROCESSING_PATTERN.md |
| "How do multi-agent sessions work?" | REF-MULTI_CLI_COORDINATION.md |
| "What are the packet formats?" | TELEOLOGY_PASS_4/05_PACKET_TEMPLATES.md |
| "How do I prevent crashout?" | TELEOLOGY_PASS_4/06_CRASHOUT_PREVENTION.md |

---

## V. RECOMMENDED COCKPIT INDEX

The system would benefit from a single "cockpit index" file at root that:
1. Links to all primary entrypoints
2. Shows current state summary
3. Provides daily ritual checklist
4. Lists recent Oracle and Blitzkrieg numbers

**Proposed Location**: `/COCKPIT.md` (new file)
**See**: `06_patch_proposals/proposed_new_entrypoint.md`

---

## VI. ANTI-ENTRYPOINTS (Where NOT to Start)

| File | Why NOT to Start Here |
|------|----------------------|
| Individual CANON files | Too narrow; miss constitutional context |
| Execution logs | Historical; not governance |
| Directives (except current) | Time-specific; may be superseded |
| Root orphan files | Not authoritative; need relocation |
| Old OUTGOING bundles | Superseded by later passes |

---

**Good entrypoints lead to understanding. Bad entrypoints lead to confusion.**
