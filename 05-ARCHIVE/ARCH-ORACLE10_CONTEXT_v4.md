# ORACLE 10 CONTEXT v4 — FINAL
## Oracle 10 Closure Session

**Date**: 2026-01-08
**Oracle**: 10
**Phase**: Blitzkrieg 42 — Closure + Handoff
**Status**: PROJ-011 COMPLETE, Oracle 10 FINALIZING

---

## CRITICAL ORIENTATION

This is the final Oracle 10 context. Blitzkrieg 42 closes Oracle 10 with:
- Root pollution cleanup
- Research artifact protocol establishment
- GitHub sync validation
- Backlog crystallization for Oracle 11

**READ THIS ENTIRE DOCUMENT** before execution.

---

## ORACLE 10 ACCOMPLISHMENTS

### Projects Completed
| Project | Status | Key Outcome |
|---------|--------|-------------|
| PROJ-001 | COMPLETE | 43 processed sources, 19 integrations, pipeline proven |
| PROJ-011 | COMPLETE | CLAUDE.md + commands + MCP + coordination.yaml |

### Infrastructure Deployed
- `CLAUDE.md` — Constitutional rules at repo root
- `Makefile` — 5 standard targets
- `.claude/commands/project/` — 4 custom commands
- `.claude/settings.json` — Permission allowlist
- `config/coordination.yaml` — Zone ownership
- `config/MCP_SETUP.md` — MCP documentation
- `00-ORCHESTRATION/scripts/` — 5 automation scripts

### 18-Lens Status
- All 18 lenses now PASS or NEUTRAL
- #12 Industrial Engineering: ADDRESSED (relay bottleneck resolved)
- #14 Permaculture: ADDRESSED (self-sustaining patterns established)

---

## RESIDUAL DEBT (Blitzkrieg 42 Scope)

### Root Pollution
Files at repository root requiring relocation:

| File | Size | Disposition |
|------|------|-------------|
| `claude_code_optimization_architecture.md` | 32K | → `05-ARCHIVE/RESEARCH-*` or distill |
| `DIRECTIVE-041A.md` | 12K | → `00-ORCHESTRATION/directives/` |
| `DIRECTIVE-041B.md` | 15K | → `00-ORCHESTRATION/directives/` |
| `ORACLE10_CONTEXT_v3.md` | 8K | → `00-ORCHESTRATION/oracle_contexts/` |

### Research Artifact Protocol (NEW)
Deep research outputs need systematic handling:

**Problem**: Research artifacts (like the Claude Code optimization report) are valuable but:
- High token count (32K+)
- Not raw transcripts (different from 04-SOURCES pattern)
- Internally produced (not external sources)
- Prone to root pollution

**Solution**: Create `05-ARCHIVE/RESEARCH-*` pattern:
- Prefix: `RESEARCH-{YYYYMMDD}-{topic}.md`
- Location: `05-ARCHIVE/` (historical preservation)
- Alternative: Distill unique value into CANON, delete original
- Script: `cleanup_root.sh` for periodic enforcement

---

## BACKLOG CRYSTALLIZATION

### New Projects for Oracle 11+

| ID | Name | Priority | Blocked By | Notes |
|----|------|----------|------------|-------|
| PROJ-002 | IIC Configuration | P1 | PROJ-011 ✓ | NOW UNBLOCKED |
| PROJ-012 | Multi-CLI Onboarding | P2 | PROJ-011 ✓ | Gemini CLI + Codex decision |
| PROJ-013 | Claude Project System Prompt | P2 | PROJ-002 | This thread's identity layer |
| PROJ-014 | Multi-Account Synchronization | P2 | PROJ-011 ✓ | Claude 2/3 web app utilization |
| PROJ-015 | Browser Automation Architecture | P3 | PROJ-014 | IIC account cloning |

### Dependency Chain (Revised)

```
PROJ-001 ✓ → PROJ-011 ✓ → PROJ-002 → PROJ-003
                         ↓
                    PROJ-012 → PROJ-014 → PROJ-015
                         ↓
                    PROJ-013
```

### New Tasks (to be added)

| ID | Project | Name | Priority |
|----|---------|------|----------|
| TASK-048 | null | Root pollution cleanup | P1 |
| TASK-049 | null | Research artifact protocol | P1 |
| TASK-050 | null | GitHub sync validation | P1 |
| TASK-051 | null | Oracle 10 closure documentation | P1 |
| TASK-052 | null | Backlog crystallization | P1 |

---

## INTERACTION CHANGES POST-041

### What Changes for Principal

1. **Context re-explanation eliminated**: CLAUDE.md provides constitutional rules automatically
2. **Verification standardized**: `make verify` replaces ad-hoc bash commands
3. **Ledger updates safer**: `sync_ledgers.py` enforces atomic writes
4. **Zone ownership clear**: coordination.yaml defines who writes where

### What Changes for Oracle Thread

1. **Directive relay simplified**: Drop files at root, Claude Code instances pick up via worktrees
2. **Execution report upload**: Logs go to execution_logs/, Oracle reads via GitHub sync
3. **Less copy-paste**: Custom commands encode repeatable patterns

### What Changes for Claude Code Instances

1. **Self-orienting**: CLAUDE.md read on session start
2. **Permission pre-approved**: settings.json allowlist reduces prompts
3. **Verification automatic**: Commands include verification steps
4. **Zone isolation**: Worktrees prevent merge conflicts

---

## MULTI-CLI ARCHITECTURE (Preview for PROJ-012)

### Current State
- **Claude CLI**: Operational (3 accounts)
- **Gemini CLI**: Operational, logged in
- **ChatGPT Codex**: Decision pending (requires Plus subscription)

### Architecture Decision Framework

| Platform | Strengths | Best Use |
|----------|-----------|----------|
| Claude Code | Deep reasoning, long context, constitutional alignment | Oracle synthesis, complex directives |
| Gemini CLI | Fast, good at structured output, Google integration | Data processing, API calls |
| ChatGPT Codex | Code generation, debugging | Implementation tasks |

### Onboarding Requirements
1. Tailored CLAUDE.md equivalent for each platform
2. Coordination protocol extension (zone ownership per platform)
3. Model capability docs reference (CANON-30300-TECH_STACK)

---

## CLAUDE PROJECT SYSTEM PROMPT (Preview for PROJ-013)

### Current State
- This Claude Project has **no custom system prompt**
- Relies entirely on userMemories + userPreferences
- Missing: Project-specific constitutional rules

### What System Prompt Should Contain
1. Syncrescendence identity and purpose
2. Oracle thread role definition
3. Repository structure reference
4. Processing patterns
5. 18-lens evaluation framework
6. Anti-patterns

### Timing
- Defer until PROJ-002 (IIC Configuration) clarifies memory architecture
- System prompt is "Layer 5" in the hierarchy:
  - Layer 0: GitHub repo (ground truth)
  - Layer 1: Local clones
  - Layer 2: Claude Project files (read-only sync)
  - Layer 3: Memory edits
  - Layer 4: CLAUDE.md
  - **Layer 5: Project system prompt**

---

## CLAUDE 2/3 UTILIZATION (Preview for PROJ-014)

### Problem Statement
- Claude 2 and 3 web app accounts "collect dust"
- Tokens per session + per week left on table
- All process archaeology resides in Claude 1 Oracle conversations
- Context drift risk too high to port mid-session

### Solution Architecture
1. **GitHub sync as shared memory**: All Claudes read from same repo
2. **Oracle context as handoff doc**: Crystal clear state for any Claude to resume
3. **Zone ownership**: Each web app account has defined responsibility
4. **Scheduled utilization**: When Claude 1 hits limit, switch to Claude 2/3

### Implementation Pattern
```
Claude 1 (Oracle) hits limit
    ↓
Export current Oracle context to repo
    ↓
Claude 2/3 picks up via GitHub sync
    ↓
Continues execution in assigned zone
    ↓
Results merge back via PR
```

---

## VERIFICATION PROTOCOL

Before claiming Oracle 10 complete:

```bash
# Root cleanup verified
ls *.md 2>/dev/null | wc -l  # Should be 2 (CLAUDE.md, Makefile note: Makefile has no .md)
# Actually: ls *.md should show only CLAUDE.md

# Research artifact relocated
ls 05-ARCHIVE/RESEARCH-* | wc -l  # Should be 1+

# Directives relocated
ls 00-ORCHESTRATION/directives/DIRECTIVE-041* | wc -l  # Should be 2

# Oracle context relocated
ls 00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT_v* | wc -l  # Should be 4

# Ledgers updated
grep "PROJ-012" 00-ORCHESTRATION/state/projects.csv  # Should exist
grep "TASK-048" 00-ORCHESTRATION/state/tasks.csv     # Should exist

# GitHub sync successful
git status  # Should be clean after push
```

---

## SUCCESS CRITERIA

Oracle 10 is complete when:
1. Root contains only: CLAUDE.md, Makefile, config/, numbered directories
2. Research artifact protocol documented and first artifact relocated
3. DIRECTIVE-041A/B in directives/
4. ORACLE10_CONTEXT versions in oracle_contexts/
5. PROJ-012 through PROJ-015 added to projects.csv
6. TASK-048 through TASK-052 added to tasks.csv
7. GitHub sync validated
8. Oracle 10 final execution log created

---

*Oracle 10 closure imminent. Infrastructure complete. Backlog crystallized. Ready for Oracle 11.*
