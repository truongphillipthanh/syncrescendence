# ORACLE 11 INITIALIZATION
## Session Handoff from Oracle 10

**Oracle**: 11
**Predecessor**: Oracle 10 (COMPLETE)
**Date Initialized**: 2026-01-08
**Status**: READY

---

## CRITICAL ORIENTATION

You are initiating Oracle 11, a strategic synthesis session for Syncrescendence. Oracle 10 completed foundational infrastructure work. Oracle 11 focuses on **information architecture** (IIC) and **execution capacity expansion** (multi-CLI, multi-account).

**Before proceeding**: Run `make verify` to confirm repository state.

---

## I. WHAT YOU INHERIT

### 1.1 Completed Infrastructure (Oracle 10)

| Component | Location | Purpose |
|-----------|----------|---------|
| **CLAUDE.md** | Root | Constitutional rules for Claude Code instances |
| **Makefile** | Root | Standard targets (verify, sync, update-ledgers, tree, clean) |
| **Custom commands** | `.claude/commands/project/` | 4 automated workflows |
| **coordination.yaml** | `config/` | Zone ownership for multi-Claude coordination |
| **MCP documentation** | `config/MCP_SETUP.md` | MCP server configuration guide |
| **Automation scripts** | `00-ORCHESTRATION/scripts/` | 6 scripts for common operations |

### 1.2 Repository Structure

```
syncrescendence/
├── 00-ORCHESTRATION/     # Strategic coordination
│   ├── directives/       # 41 directive files (017-042)
│   ├── execution_logs/   # 44 execution records
│   ├── oracle_contexts/  # 8 Oracle context documents
│   ├── scripts/          # 6 automation scripts
│   └── state/            # Ledgers + references (23 files)
├── 01-CANON/             # 77 canonical documents
├── 02-OPERATIONAL/       # Functions, prompts, profiles
├── 03-QUEUE/             # Pending items by modal
├── 04-SOURCES/           # 185 raw, 46 processed
├── 05-ARCHIVE/           # 31 preserved files
├── 06-EXEMPLA/           # Templates
├── config/               # MCP + coordination (3 files)
├── CLAUDE.md             # Constitutional rules
└── Makefile              # 5 targets
```

### 1.3 Ledger State

| Ledger | Rows | Key Stats |
|--------|------|-----------|
| projects.csv | 16 | 2 complete, 4 not_started (unblocked), 9 blocked |
| tasks.csv | 53 | 48 done, 5 remaining |
| sources.csv | 185 | 46 processed, 139 raw |
| sprints.csv | 1 | SPRINT-001 complete (142% velocity) |

---

## II. YOUR MANDATE

### 2.1 Primary Focus: PROJ-002 (IIC Configuration)

**Priority**: P1 — Highest impact unblocked project

**Scope**: Configure Intelligence Information Constellation across 5 chains:
- Acumen (Information chain)
- Coherence (Insight chain)
- Efficacy (Expertise chain)
- Mastery (Knowledge chain)
- Transcendence (Wisdom chain)

**Key Deliverables**:
- IIC account specifications for each chain
- Memory architecture decisions (what goes where in layer hierarchy)
- Platform grammar refinements
- Feed curation rules

**Relevant CANON**:
- CANON-31115-IIC_IMPL-lunar-ACUMEN-planetary-INFORMATION
- CANON-31140-IIC-lunar-ACUMEN-planetary-INFORMATION
- CANON-31141-FIVE_ACCOUNT-satellite-IIC
- CANON-31142-PLATFORM_GRAMMAR-satellite-IIC
- CANON-31143-FEED_CURATION-satellite-IIC

### 2.2 Secondary Focus: PROJ-012 (Multi-CLI Onboarding)

**Priority**: P2 — Expands execution capacity

**Current State**:
- Gemini CLI: Operational, logged in, ready for integration
- ChatGPT Codex: Decision pending (requires Plus subscription)

**Key Tasks**:
- Create `GEMINI.md` (equivalent of CLAUDE.md for Gemini CLI)
- Extend coordination.yaml with platform-specific zones
- Test multi-CLI workflow with simple directive
- Evaluate Codex subscription value

**Decision Framework**:
| Platform | Strengths | Best Use |
|----------|-----------|----------|
| Claude Code | Deep reasoning, constitutional alignment | Oracle synthesis, complex directives |
| Gemini CLI | Fast structured output, Google integration | Data processing, API calls |
| ChatGPT Codex | Code generation, debugging | Implementation tasks |

### 2.3 Tertiary Focus: PROJ-014 (Multi-Account Sync)

**Priority**: P2 — Utilizes idle resources

**Problem**: Claude 2/3 web accounts collect dust while Claude 1 hits limits

**Solution Pattern**:
```
Claude 1 hits limit → Export Oracle context → Push to GitHub
→ Claude 2/3 reads via Project sync → Continues in assigned zone
→ Results merge via PR → Claude 1 resumes when limit resets
```

**Key Tasks**:
- Define handoff protocol formalization
- Test cross-account context resumption
- Create utilization schedule

---

## III. DEPENDENCY CHAIN

```
ORACLE 10 (COMPLETE)          ORACLE 11                    ORACLE 12+
────────────────────          ─────────                    ──────────
PROJ-001 ✓ ─────────┐
                    ├───────► PROJ-002 (IIC) ───────────► PROJ-013 (System Prompt)
PROJ-011 ✓ ─────────┤
                    ├───────► PROJ-003 (Tooling)
                    │
                    ├───────► PROJ-012 (Multi-CLI)
                    │
                    └───────► PROJ-014 (Multi-Account) ──► PROJ-015 (Browser)
```

### 3.1 What's Unblocked Now

| Project | Status | Why Unblocked |
|---------|--------|---------------|
| PROJ-002 | READY | PROJ-001 ✓ + PROJ-011 ✓ |
| PROJ-003 | READY | PROJ-011 ✓ |
| PROJ-012 | READY | PROJ-011 ✓ |
| PROJ-014 | READY | PROJ-011 ✓ |

### 3.2 What Remains Blocked

| Project | Blocked By | Notes |
|---------|------------|-------|
| PROJ-013 | PROJ-002 | System prompt requires IIC memory architecture decisions |
| PROJ-015 | PROJ-014 | Browser automation requires multi-account patterns |
| PROJ-008 | Resources | Tech Lunar (306K specs) deferred |
| PROJ-009 | Modal sequence | Modal 2 requires Modal 1 foundation |

---

## IV. CONSTITUTIONAL RULES

From CLAUDE.md (must be honored in all directives):

### Structural (ABSOLUTE)
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of subdirectories.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00-06. Do not create unnumbered directories at root.
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit Principal approval for deletions.

### Semantic (ABSOLUTE)
4. **DISTILLATION SEMANTICS**: "Metabolize/distill" = READ → EXTRACT unique value → COMPRESS → DELETE originals. NOT organizational restructuring.
5. **CATEGORY ERROR**: Metabolism applies to CONTENT, not ORCHESTRATION. State/ and logs/ are living infrastructure—never delete.
6. **LEDGER GROUND TRUTH**: tasks.csv is authoritative. Verify actual state, not execution reports.

### Operational (ABSOLUTE)
7. **ATOMIC UPDATES**: CSV updates use temp file → validate → rename pattern.
8. **VERIFICATION BEFORE COMPLETION**: Never claim done without running verification commands.
9. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes (feat:, fix:, docs:, chore:, refactor:).

---

## V. 18-LENS QUICK REFERENCE

Apply to all significant decisions:

| # | Lens | Key Question |
|---|------|--------------|
| 1 | Syncrescendent Route | Does this advance civilizational sensing? |
| 2 | Bitter Lesson | Does this scale with compute? |
| 3 | Antifragile | Does this strengthen through stress? |
| 4 | Meet the Moment | Is this the right work for NOW? |
| 5 | Steelman/Redteam | What's the strongest counter-argument? |
| 6 | Personal Idiosyncrasies | Does this honor Principal's cognitive style? |
| 7 | Potency Without Loss | Maximum throughput without waste? |
| 8 | Elegance | Simplest solution that works? |
| 9 | Agentify | Can fresh agents navigate this? |
| 10 | First Principles | What's irreducibly true? |
| 11 | Systems Thinking | What are second-order effects? |
| 12 | Industrial Engineering | Where's the bottleneck? |
| 13 | Complexity Theory | Emergence vs complication? |
| 14 | Permaculture | Is this self-sustaining? |
| 15 | Design Thinking | What does user actually need? |
| 16 | Agile | Minimum viable increment? |
| 17 | Lean | What waste to eliminate? |
| 18 | Six Sigma | Defect rate and root cause? |

---

## VI. INTERACTION PATTERNS (Post-Oracle 10)

### 6.1 What Changed

| Aspect | Before Oracle 10 | After Oracle 10 |
|--------|------------------|-----------------|
| Context setup | Manual re-explanation | CLAUDE.md provides automatically |
| Verification | Ad-hoc bash commands | `make verify` standardizes |
| Ledger updates | Manual, error-prone | `sync_ledgers.py` atomic |
| Processing | Custom instructions | `/project:process-source` command |
| Batch work | Individual items | `/project:blitzkrieg` mode |
| Zone ownership | Verbal assignment | `coordination.yaml` defines |

### 6.2 Principal Workflow

```
OLD: Explain context → Issue directive → Wait → Manually integrate → Update ledgers
NEW: Issue directive → Claude Code self-orients via CLAUDE.md → Executes → Ledgers update atomically
```

### 6.3 Blitzkrieg Methodology

Continue using parallel A/B streams:
- Stream A: Infrastructure/hygiene focus
- Stream B: Content/documentation focus
- Both operate independently
- Git handles merge

---

## VII. DECISIONS PENDING

### 7.1 ChatGPT Plus Subscription

**Question**: Subscribe to Plus ($20/month) for Codex CLI access?

**Considerations**:
- Pro: Additional execution capacity, code generation strength
- Con: Cost, another platform to coordinate
- Recommendation: Test Gemini CLI first (PROJ-012), then decide

### 7.2 Claude Project System Prompt

**Question**: What should this Oracle thread's system prompt contain?

**Context**: Currently blank, relies on userMemories + userPreferences

**Blocked By**: PROJ-002 (IIC) — Memory architecture decisions determine what belongs where

**Defer Until**: PROJ-002 completion

### 7.3 Browser Automation Architecture

**Question**: Clone browsers for IIC accounts to bypass vendor lock-in?

**Context**: First-party features may provide value worth moat

**Blocked By**: PROJ-014 (Multi-Account) — Need patterns first

**Defer Until**: PROJ-014 completion

---

## VIII. KEY REFERENCES

### 8.1 Essential Documents

| Document | Path | Purpose |
|----------|------|---------|
| ORACLE10_CULMINATION | `00-ORCHESTRATION/oracle_contexts/` | Session evaluation |
| ORACLE10_CONTEXT_FINAL | `00-ORCHESTRATION/oracle_contexts/` | Detailed state summary |
| DYN-BACKLOG | `00-ORCHESTRATION/state/` | Full project/task registry |
| REF-RESEARCH_ARTIFACTS | `00-ORCHESTRATION/state/` | Deep research handling |
| coordination.yaml | `config/` | Multi-Claude coordination |

### 8.2 Key CANON for PROJ-002

| Document | Purpose |
|----------|---------|
| CANON-31115-IIC_IMPL | IIC implementation details |
| CANON-31140-IIC | Core IIC specification |
| CANON-31141-FIVE_ACCOUNT | Five-account constellation |
| CANON-31142-PLATFORM_GRAMMAR | Platform-specific rules |
| CANON-31143-FEED_CURATION | Feed curation protocols |
| CANON-25000-MEMORY_ARCH | Memory architecture |
| CANON-25100-CONTEXT_TRANS | Context transfer patterns |

---

## IX. FIRST SESSION CHECKLIST

Before beginning substantive work:

- [ ] Run `make verify` — Confirm clean state
- [ ] Review `DYN-BACKLOG.md` — Current project/task state
- [ ] Review `coordination.yaml` — Zone ownership
- [ ] Confirm Gemini CLI operational — Test simple command
- [ ] Assess Claude 2/3 availability — Check current limits

### Recommended First Blitzkrieg (043)

**Stream A**: PROJ-002 Discovery
- Read all IIC-related CANON documents
- Map memory layer hierarchy
- Identify first configuration decisions

**Stream B**: PROJ-012 Validation
- Test Gemini CLI with simple task
- Draft GEMINI.md initial version
- Document capability comparison

---

## X. SUCCESS METRICS FOR ORACLE 11

| Metric | Target |
|--------|--------|
| PROJ-002 status | IN_PROGRESS or COMPLETE |
| IIC accounts configured | 2+ of 5 chains |
| Gemini CLI validated | Yes |
| Multi-CLI directive tested | Yes |
| Claude 2/3 utilization | Established pattern |
| Codex decision | Made |
| System prompt | Drafted (if PROJ-002 complete) |

---

*Oracle 11 initialized. Infrastructure inherited. Focus on information architecture and execution expansion.*

**Ready to begin**.
