# DIRECTIVE-045A: Skills Creation + Intention Resolution

**Stream**: A
**Model**: Sonnet 4.5
**Thinking**: Default
**Estimated Duration**: 45 minutes
**Executor**: Claude 2 (Claude Code)

---

## CONTEXT

Read `ORACLE12_PHASE3_PEDIGREE.md` for full context.

Blitzkrieg 45 Stream A creates reusable Skills for Oracle workflow patterns and resolves intentions based on Tech Tree Audit findings.

---

## PHASE 1: Create Intentions Skill

### Objective
Create a Claude Skill that standardizes intention capture during Oracle sessions.

### Location
Create directory: `/home/claude/skills/intentions/`

### File: SKILL.md

Create `/home/claude/skills/intentions/SKILL.md` with this content:

```markdown
---
name: intentions
description: Standardized framework for capturing, categorizing, and tracking strategic intentions during Oracle sessions. Use when Principal expresses new objectives, identifies patterns, captures ideas, or when synthesizing session outcomes into actionable intention records. Triggers on phrases like "we should", "intention", "add to backlog", "urgent", "sprint item", "pattern identified".
---

# Intentions Skill

## Purpose
Oracle sessions generate intentions — strategic objectives, pattern recognitions, and ideas requiring future action. This skill provides consistent structure for capturing intentions without losing fidelity.

## Intention Categories

### URGENT
Blocking current work, time-sensitive opportunities, critical path items.
- ID Format: `INT-NNNN`
- Required fields: Description, Rationale, Blocking item
- Resolution: Immediate action or escalation

### SPRINT  
Current Oracle scope, active project contributions, near-term actionable.
- ID Format: `INT-NNNN`
- Required fields: Description, Project link, Dependencies
- Resolution: Current blitzkrieg or next

### BACKLOG
Future Oracle scope, requires prerequisite work, valuable but not urgent.
- ID Format: `INT-NNNN`
- Required fields: Description, Dependency chain, Estimated Oracle
- Resolution: When dependencies clear

### PATTERNS
Cross-cutting recognitions, methodology improvements, process anti-patterns.
- ID Format: `INT-PNNN`
- Required fields: Pattern description, Resolution status
- Resolution: Document in ARCH- files or CANON

## Capture Protocol

When Principal expresses intention:

1. **Identify Category** — Use urgency × actionability matrix:
   - Urgent + Actionable now = URGENT
   - Not urgent + Actionable now = SPRINT
   - Requires prerequisites = BACKLOG
   - Meta/process insight = PATTERNS

2. **Assign ID** — Next sequential in category

3. **Extract Core** — One sentence essence capturing:
   - What needs to happen
   - Why it matters
   - How we'll know it's done

4. **Link Context** — Reference:
   - Related project (PROJ-NNN)
   - Blocking dependencies
   - Source (Oracle session)

5. **Note Resolution Criteria** — Explicit completion test

## Output Format

For session summaries, produce table:

| ID | Category | Description | Status |
|----|----------|-------------|--------|
| INT-NNNN | SPRINT | Description | Active |

## Integration

All captured intentions update:
`00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md`

When updating:
1. Add to appropriate section
2. Increment intention count
3. Note Oracle source in commit message
```

### Verification
```bash
test -f /home/claude/skills/intentions/SKILL.md && echo "✓ Intentions skill created"
```

---

## PHASE 2: Create Pedigree Skill

### Objective
Create a Claude Skill that standardizes Oracle session context documents.

### Location
Create directory: `/home/claude/skills/pedigree/`

### File: SKILL.md

Create `/home/claude/skills/pedigree/SKILL.md` with this content:

```markdown
---
name: pedigree
description: Standardized framework for creating Oracle session context documents (pedigree files). Use when initializing new Oracle sessions, creating Blitzkrieg context packages, preparing execution engine deployments, or when handing off between instances. Triggers on "create pedigree", "Oracle context", "blitzkrieg package", "handoff document", "context for execution".
---

# Pedigree Skill

## Purpose
Pedigree documents bridge Oracle synthesis and execution engine operation. They provide strategic context in structured format that execution engines can act upon without full Oracle history.

## Pedigree Types

### ORACLE_CONTEXT
Full strategic context for Oracle session reinitialization.

Required sections:
1. **Trajectory** — Where we've been (past Oracles), where we're going (next phases)
2. **Key Findings** — Strategic decisions, patterns identified, architecture choices
3. **Anti-Patterns** — What to avoid, learned failures, category errors
4. **Current State** — Ledger status, active projects, task counts
5. **Next Actions** — Immediate priorities, deployment queue

Naming: `ORACLE[NN]_CONTEXT.md`

### BLITZKRIEG_PEDIGREE
Focused context for parallel execution streams.

Required sections:
1. **Oracle Session** — Source Oracle reference, phase
2. **Blitzkrieg Scope** — What this batch addresses
3. **Stream Definitions** — What each stream executes
4. **Relevant Context** — Extracted subset from ORACLE_CONTEXT
5. **Coordination Notes** — How streams interact, conflict avoidance

Naming: `ORACLE[NN]_[PHASE]_PEDIGREE.md` or `BLITZKRIEG_[NN]_PEDIGREE.md`

### HANDOFF_PEDIGREE
Context for cross-instance or cross-account coordination.

Required sections:
1. **Session State** — What was accomplished, where stopped
2. **Continuation Points** — Specific locations to resume
3. **Warnings** — Context that might be lost, assumptions made
4. **Files Modified** — Explicit ledger of changes

Naming: `HANDOFF_[source]_[target].md`

## Creation Protocol

When creating pedigree:

1. **Identify Type** — Oracle init, blitzkrieg, or handoff
2. **Gather Sources** — Previous pedigrees, execution logs, ledgers
3. **Extract Relevant** — Only what recipient needs
4. **Structure Per Template** — Required sections in order
5. **Verify Completeness** — Can recipient act without asking?

## Quality Tests

Good pedigree passes these:
- [ ] Recipient can execute without additional context queries
- [ ] No orphan references (all PROJ-NNN, TASK-NNN defined)
- [ ] Ledger state matches reality
- [ ] Trajectory clear (past → present → future)

## Integration

Pedigree documents live in:
- `00-ORCHESTRATION/oracle_contexts/` — Oracle context files
- Repository root — Active blitzkrieg pedigrees (temporary)
- `05-ARCHIVE/` — Completed pedigrees after Oracle closes
```

### Verification
```bash
test -f /home/claude/skills/pedigree/SKILL.md && echo "✓ Pedigree skill created"
```

---

## PHASE 3: Resolve Intentions

### Objective
Update ARCH-INTENTION_COMPASS.md to reflect Tech Tree Audit findings from DIRECTIVE-044A.

### Source
Per ARCH-TECH_TREE_AUDIT.md (created by Stream A of Blitzkrieg 44):
- Prompting domain: 10 CANON files + translate.xml = sufficient
- Platforms domain: 77 CANON files = excellent
- Capabilities domain: 73 CANON files = sufficient

### Actions

1. **Read** `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md`

2. **Locate** INT-1210, INT-1211, INT-1212, INT-1213

3. **Update Status** for each:
   - INT-1210: Mark **resolved** — "Resolved per ARCH-TECH_TREE_AUDIT.md: 10 CANON files + translate.xml provide sufficient coverage"
   - INT-1211: Mark **resolved** — "Resolved per ARCH-TECH_TREE_AUDIT.md: 77 CANON files provide excellent coverage"
   - INT-1212: Mark **resolved** — "Resolved per ARCH-TECH_TREE_AUDIT.md: 73 CANON files with correct temporal/evergreen split"
   - INT-1213: Mark **resolved** — "Resolved by DIRECTIVE-044B: CLAUDE.md v2.1.0 + coordination.yaml v2.1.0"

4. **Increment version** if present

### Verification
```bash
grep -c "resolved" 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
# Should show increased count
```

---

## PHASE 4: Ledger Update

### Objective
Update tasks.csv with completed work.

### Tasks to Add

```csv
TASK-092,PROJ-016,Create Intentions skill for Oracle workflow,task,done,P2,Claude_Code_2,null,0.5,0.5,2026-01-12,2026-01-12,Blitzkrieg 45 - /home/claude/skills/intentions/SKILL.md
TASK-093,PROJ-016,Create Pedigree skill for Oracle workflow,task,done,P2,Claude_Code_2,TASK-092,0.5,0.5,2026-01-12,2026-01-12,Blitzkrieg 45 - /home/claude/skills/pedigree/SKILL.md
TASK-094,PROJ-012,Resolve INT-1210-1213 per Tech Tree Audit,task,done,P2,Claude_Code_2,TASK-093,0.25,0.25,2026-01-12,2026-01-12,Blitzkrieg 45 - All 4 intentions marked resolved
```

### Verification
```bash
grep "TASK-09[234]" 00-ORCHESTRATION/state/tasks.csv
```

---

## VERIFICATION CHECKLIST

Before claiming completion:

- [ ] `/home/claude/skills/intentions/SKILL.md` exists and contains frontmatter
- [ ] `/home/claude/skills/pedigree/SKILL.md` exists and contains frontmatter
- [ ] ARCH-INTENTION_COMPASS.md has INT-1210-1213 marked resolved
- [ ] tasks.csv contains TASK-092, TASK-093, TASK-094
- [ ] No subdirectories created outside skills structure (FLAT PRINCIPLE)
- [ ] Execution log created

---

## DELIVERABLES

1. `/home/claude/skills/intentions/SKILL.md`
2. `/home/claude/skills/pedigree/SKILL.md`
3. Updated `ARCH-INTENTION_COMPASS.md`
4. Updated `tasks.csv`
5. `EXECUTION_LOG-2026-01-12-045A.md`

---

## COORDINATION

### Parallel Stream
DIRECTIVE-045B executing simultaneously on Claude 3.
- No file conflicts expected (different scope)
- Stream B handles: DYN-PLATFORM_CATALOG.md, PROJ-017, DYN-BACKLOG.md

### Post-Execution
Skills created in `/home/claude/skills/` are ready for packaging when validated.
To package: Use `/mnt/skills/examples/skill-creator/scripts/package_skill.py`

---

*DIRECTIVE-045A*
*Blitzkrieg 45 Stream A*
*Oracle 12 Phase 3*
