# ORACLE 10 CONTEXT v3
## Post-PROJ-001 Completion — Automation Infrastructure Phase

**Date**: 2026-01-08
**Oracle**: 10
**Phase**: Blitzkrieg 41 — PROJ-011 Execution
**Status**: PROJ-001 COMPLETE, PROJ-011 ACTIVE

---

## CRITICAL ORIENTATION

You are a Claude Code instance executing Syncrescendence directives. This context document provides everything needed to execute your assigned stream without Principal relay.

**READ THIS ENTIRE DOCUMENT** before executing any commands.

---

## SESSION STATE

### Completed (Oracle 10, Blitzkrieg 39-40)
| Metric | Value |
|--------|-------|
| Processed sources | 43 |
| CANON integrations | 19 |
| CANON files enriched | 11 |
| PROJ-001 status | **COMPLETE** |
| PROJ-002 status | READY (unblocked) |
| Sprint velocity | 57 points (142%) |
| Root pollution | 0 files |
| Structural violations | 0 |

### Now Active (Blitzkrieg 41)
**PROJ-011: Automation Infrastructure** — NEW PROJECT, P0 PRIORITY

This project was created to address two failing 18-lens evaluations:
- **Industrial Engineering**: Principal relay bottleneck (CLAUDE.md + commands fix this)
- **Permaculture**: System not self-sustaining (MCP + automation scripts fix this)

---

## PROJECT DEPENDENCY REFRAME

### Old (Flawed) Chain
```
PROJ-001 → PROJ-002 (IIC) → PROJ-003 (Tooling) → PROJ-004 (Automation)
```
Problem: Automation comes LAST, so every intermediate project suffers relay friction.

### New (Correct) Chain
```
PROJ-001 ✓ → PROJ-011 (Automation) → PROJ-002 (IIC) → PROJ-003 (Tooling)
```
Rationale: Automation infrastructure benefits ALL subsequent work.

---

## REPOSITORY STRUCTURE (Post-040)

```
syncrescendence/
├── 00-ORCHESTRATION/
│   ├── directives/          # 37 directive files
│   ├── execution_logs/      # 35 execution logs
│   ├── oracle_contexts/     # Oracle context versions
│   ├── scripts/             # Python automation scripts
│   └── state/               # Ledgers, references, archaeology
│       ├── ARCH-*           # Archaeological/historical documents
│       ├── DYN-*            # Dynamic state (tree, backlog, dashboard)
│       ├── REF-*            # Reference documents (standards, patterns)
│       ├── projects.csv     # Project registry
│       ├── tasks.csv        # Task tracking
│       ├── sources.csv      # Source document registry
│       ├── sprints.csv      # Sprint tracking
│       └── burndown.csv     # Burndown data
├── 01-CANON/                # 60+ canonical documents
├── 02-ENGINE/          # Functions, prompts, model profiles
├── 03-QUEUE/                # Pending items by modal
├── 04-SOURCES/              # Source documents (raw/ and processed/)
├── 05-MEMORY/              # Historical preservation (ARCHIVE-*, SCAFF-*)
└── 06-EXEMPLA/              # Templates and examples
```

---

## CONSTITUTIONAL RULES

These rules are ABSOLUTE and must be encoded in CLAUDE.md:

### Structural Rules
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of subdirectories.
2. **NUMBERED DIRECTORIES**: Top-level directories are numbered 00-06. Do not create unnumbered directories at root.
3. **PROTECTED DIRECTORIES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit Principal approval for deletions.

### Semantic Rules
4. **DISTILLATION SEMANTICS**: "Metabolize/distill" means READ all files, EXTRACT unique value, COMPRESS into single document, DELETE originals. It does NOT mean organizational restructuring.
5. **CATEGORY ERROR**: Metabolism applies to CONTENT, not ORCHESTRATION INFRASTRUCTURE. State/ and logs/ are living infrastructure—never delete.
6. **LEDGER GROUND TRUTH**: tasks.csv is authoritative for work status. Verify actual state, not execution reports.

### Processing Rules
7. **ATOMIC LEDGER UPDATES**: CSV updates must use temp file → validate → rename pattern.
8. **VERIFICATION BEFORE COMPLETION**: Never claim task done without running verification commands.
9. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes (feat:, fix:, docs:, chore:, refactor:).

### Anti-Patterns (PROHIBITED)
- Creating subdirectories anywhere
- Modifying state/ files without validation
- Skipping verification to "save time"
- Claiming integration without grep verification
- Deferring ledger updates to "later"

---

## 18-LENS QUICK REFERENCE

Apply these lenses to all significant decisions:

| # | Lens | Key Question |
|---|------|--------------|
| 1 | Syncrescendent Route | Does this advance civilizational sensing? |
| 2 | Bitter Lesson | Does this scale with compute, not hand-crafted rules? |
| 3 | Antifragile | Does this strengthen through stress? |
| 4 | Meet the Moment | Is this the right work for NOW? |
| 5 | Steelman/Redteam | What's the strongest counter-argument? |
| 6 | Personal Idiosyncrasies | Does this honor the Principal's cognitive style? |
| 7 | Potency Without Loss | Maximum throughput without waste? |
| 8 | Elegance | Simplest solution that works? |
| 9 | Agentify | Can fresh agents navigate this? |
| 10 | First Principles | What's irreducibly true? |
| 11 | Systems Thinking | What are second-order effects? |
| 12 | Industrial Engineering | Where's the bottleneck? |
| 13 | Complexity Theory | Emergence (useful) vs. complication (waste)? |
| 14 | Permaculture | Is this self-sustaining? |
| 15 | Design Thinking | What does the user actually need? |
| 16 | Agile | What's the minimum viable increment? |
| 17 | Lean | What's the waste to eliminate? |
| 18 | Six Sigma | What's the defect rate and root cause? |

**Currently Failing**: #12 (Industrial Engineering), #14 (Permaculture)
**Blitzkrieg 41 directly addresses both.**

---

## CUSTOM COMMANDS SPECIFICATION

These commands will be created in `.claude/commands/project/`:

### `/project:verify`
Run comprehensive verification suite:
- Lint, typecheck, schema validation
- Ledger integrity checks
- Internal link validation
- Git status confirmation
- Output formatted report

### `/project:process-source`
Process a source document from intake:
- Locate in 04-SOURCES/raw/
- Extract metadata
- Apply processing template
- Stage to processed/
- Update sources.csv atomically
- Verify before completing

### `/project:update-ledgers`
Safely update CSV ledgers:
- Create backup
- Acquire lock
- Apply changes
- Validate schema
- Atomic write
- Release lock

### `/project:blitzkrieg`
Rapid batch processing:
- Triage pending items
- Process in parallel
- Batch ledger updates
- Run verification
- Generate summary report

---

## MCP CONFIGURATION REQUIREMENTS

### GitHub MCP Server
```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PAT}"}
    }
  }
}
```

### Multi-Account Coordination
- 3 Claude Pro accounts operating in parallel
- Git worktrees for conflict-free execution
- Zone-based ownership via coordination.yaml
- Append-only patterns for shared files

---

## VERIFICATION PROTOCOL

Before claiming ANY task complete, execute:

```bash
# Structure verification
find . -type d -name "scaffolding" | wc -l  # Must be 0
ls *.md 2>/dev/null | wc -l                  # Must be 0 (at root)

# Ledger verification
wc -l 00-ORCHESTRATION/state/tasks.csv       # Check row count
wc -l 00-ORCHESTRATION/state/projects.csv    # Check row count

# Content verification
ls 04-SOURCES/processed/*.md | wc -l         # Count processed
grep -l "SOURCE-" 01-CANON/*.md | wc -l      # Count integrations
```

---

## EXECUTION ANTI-PATTERNS

**NEVER**:
- Claim completion without running verification
- Create recommendations instead of executing
- Defer ledger updates
- Process incrementally when batch is possible
- Skip reading this context document

**ALWAYS**:
- Execute directly
- Update ledgers atomically
- Verify with bash commands
- Complete all phases before reporting
- Include verification outputs in execution log

---

## BLITZKRIEG 41 TARGETS

| Metric | Target | Owner |
|--------|--------|-------|
| CLAUDE.md deployed | Yes | 041A |
| Custom commands | 4 | 041A |
| Makefile targets | 5+ | 041A |
| MCP configured | Yes | 041B |
| coordination.yaml | Yes | 041B |
| Automation scripts | 3+ | 041B |
| PROJ-011 status | COMPLETE | Both |
| 18-lens #12 | PASS | Both |
| 18-lens #14 | PASS | Both |

---

## SUCCESS CRITERIA

Blitzkrieg 41 is complete when:
1. `cat CLAUDE.md` shows constitutional rules
2. `ls .claude/commands/project/` shows 4 command files
3. `cat Makefile` shows verify, sync, update-ledgers targets
4. `cat .claude/settings.json` shows permission allowlist
5. `cat config/coordination.yaml` shows zone ownership
6. MCP configuration documented
7. Ledgers updated with PROJ-011 and task completions
8. Execution logs created with verification outputs

---

*Globe maintained. Infrastructure first. Automation enables everything.*
