# DIRECTIVE-045B: SKILLS GENESIS
## Stream B — Claude 3 (Sonnet 4.5)

**Issued**: 2026-01-12
**Stream**: B (Sonnet 4.5 — tactical, template-driven)
**Extended Thinking**: default
**Priority**: MODERATE
**Estimated Duration**: 30-45 minutes
**Parallel**: DIRECTIVE-045A executing simultaneously on Claude 2
**Companion**: ORACLE12_PEDIGREE-045.md (read first)

---

## PREAMBLE

You are Claude 3, executing Stream B of Blitzkrieg 45. Your mandate is to create Claude Code Skills for process-level patterns.

**Context**: The Principal identified that Intentions extraction and Pedigree management are recurring processes that should be codified as Skills for consistent execution across Oracle sessions.

**Your Deliverables**: 
1. Create `intentions.md` Skill for intention extraction and categorization
2. Create `pedigree.md` Skill for Oracle pedigree management

---

## PHASE 1: UNDERSTAND SKILL FORMAT (~10 minutes)

### 1.1 Read Claude Code Skills Documentation

Skills are markdown files in `.claude/skills/` that provide Claude Code with specialized knowledge for specific tasks.

**Skill Structure**:
```markdown
# [SKILL NAME]

## Purpose
[What this skill enables]

## When to Use
[Trigger patterns and conditions]

## Process
[Step-by-step instructions]

## Output Format
[Expected deliverable structure]

## Examples
[Concrete examples of good execution]

## Anti-Patterns
[What to avoid]
```

### 1.2 Study Existing Patterns

Review the ARCH-INTENTION_COMPASS.md structure:
```bash
cat 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
```

Review the Oracle Pedigree pattern in CANON-25100:
```bash
grep -A 50 "PEDIGREE" 01-CANON/CANON-25100-CONTEXT_TRANS-lattice.md
```

---

## PHASE 2: CREATE INTENTIONS SKILL (~15 minutes)

### 2.1 Create Skills Directory

```bash
mkdir -p .claude/skills
```

### 2.2 Create intentions.md

Create `.claude/skills/intentions.md`:

```markdown
# INTENTIONS SKILL
## Oracle Session Intention Extraction and Categorization

**Version**: 1.0.0
**Last Updated**: 2026-01-12
**Authority**: Oracle 12

---

## PURPOSE

Extract, categorize, and track Principal intentions during Oracle sessions. Ensures nothing falls through cracks and maintains continuity across sessions.

---

## WHEN TO USE

Trigger this skill when:
- Starting a new Oracle session (extract from previous session artifacts)
- Principal expresses desires, requirements, or frustrations
- Principal uses indicative language: "we should", "I want", "don't forget", "make sure"
- Session is ending (consolidate captured intentions)
- Reviewing previous Oracle transcripts

---

## PROCESS

### 1. Capture Phase (During Session)

Listen for intention signals:
- Explicit: "I want X", "We need to Y", "Don't forget Z"
- Implicit: Frustration expressions, repeated themes, emphasis patterns
- Strategic: Long-term goals, vision statements, architectural decisions
- Tactical: Immediate needs, blockers, quick fixes

Capture verbatim in temporary notes.

### 2. Categorization Phase (At Checkpoint)

Assign each intention to a category:

| Category | Criteria | Action Horizon |
|----------|----------|----------------|
| urgent | Requires immediate action, blocking | Same session |
| sprint | Part of current work cycle | Current Oracle |
| backlog | Future work, not blocking | Future Oracles |
| pattern | Meta-observation, recurring theme | Ongoing |
| capture | Unclear categorization | Pending triage |

### 3. ID Assignment

Format: `INT-XXYY` where:
- `XX` = Oracle number (e.g., 12)
- `YY` = Sequence within Oracle (e.g., 01, 02)

Patterns use `INT-PXXX` format.

### 4. Integration Phase (Session End)

Update `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md`:
- Add new intentions to appropriate category
- Update status of resolved intentions
- Note integration references for completed items

---

## OUTPUT FORMAT

### Compass Entry
```yaml
- id: INT-XXYY
  oracle: [number]
  category: [urgent|sprint|backlog|pattern|capture]
  priority: [P0|P1|P2|P3]
  status: [active|resolved|superseded|deferred]
  text: "[Principal's actual words or close paraphrase]"
  interpretation: "[Your understanding of intent]"
  blocked_by: [null|dependency]
  integrated_into: [null|reference]
  notes: "[context]"
```

### Quick Capture Format
During session, use abbreviated format:
```
[urgent] Account sustainability by month end
[sprint] Complete IIC configs
[pattern] Always verify before declaring complete
```

---

## EXAMPLES

### Good Extraction

Principal says: "We really need to get these accounts self-sustaining by the end of the month, and I'm worried we're not moving fast enough."

**Extraction**:
```yaml
- id: INT-1201
  oracle: 12
  category: urgent
  priority: P0
  status: active
  text: "accounts become self-sustaining by month end"
  interpretation: "Revenue generation deadline 2026-01-31"
  notes: "Principal expressed urgency and concern about velocity"
```

### Good Resolution

When intention is addressed:
```yaml
- id: INT-1101
  status: resolved
  integrated_into: DIRECTIVE-042B
  notes: "Gemini CLI validated and ready for use"
```

---

## ANTI-PATTERNS

### Don't Do This

1. **Over-capturing**: Not every statement is an intention. Focus on actionable desires.

2. **Losing verbatim**: Don't paraphrase beyond recognition. Principal's words matter.

3. **Category confusion**: "Urgent" means NOW, not just important. Most things are sprint or backlog.

4. **Orphan intentions**: Every intention needs an ID and a category.

5. **False resolution**: Don't mark resolved without evidence of completion.

6. **Ignoring frustrations**: Frustration often signals important unmet intentions.

---

## MAINTENANCE

- Review compass at Oracle start and end
- Archive resolved intentions quarterly
- Pattern analysis monthly
- Dependency tracking continuous

---

*Intentions Skill v1.0.0 | Syncrescendence*
```

### 2.3 Verification

```bash
wc -l .claude/skills/intentions.md
# Should be 150+ lines
```

---

## PHASE 3: CREATE PEDIGREE SKILL (~15 minutes)

### 3.1 Create pedigree.md

Create `.claude/skills/pedigree.md`:

```markdown
# PEDIGREE SKILL
## Oracle Session Context Management

**Version**: 1.0.0
**Last Updated**: 2026-01-12
**Authority**: Oracle 12

---

## PURPOSE

Manage Oracle pedigree—the lineage and context that enables session continuity without explicit handoffs. Pedigree supersedes handoff protocol for repository-centric work.

---

## WHEN TO USE

Trigger this skill when:
- Starting a new Oracle session
- Resuming after compaction
- Preparing context for Claude Code execution
- Creating Blitzkrieg packages
- Transitioning between Oracle sessions

---

## PEDIGREE VS HANDOFF

| Aspect | Handoff | Pedigree |
|--------|---------|----------|
| **Context** | Document-centric | Repository-centric |
| **Assumption** | Next instance lacks context | Repository IS the context |
| **Format** | Detailed narrative | Structured reference |
| **Use Case** | Web app transitions | Claude Code continuity |

**Rule**: Use Pedigree when the repository is authoritative. Use Handoff only for web-app-only sessions.

---

## PEDIGREE COMPONENTS

### 1. Oracle Lineage
```yaml
oracle:
  current: 12
  predecessor: 11
  trajectory: "Vision(0-2) → Structure(3-5) → Recovery(6-7) → Content(8-9) → Infrastructure(10-11) → Expansion(12+)"
```

### 2. Campaign Status
```yaml
campaign:
  active_blitzkrieg: 45
  last_complete: 44
  parallel_streams: [A, B]
```

### 3. Project State
```yaml
projects:
  active: [PROJ-002, PROJ-012, PROJ-014]
  blocked: [PROJ-004, PROJ-005, PROJ-006, PROJ-007, PROJ-015]
  complete: [PROJ-001, PROJ-011]
```

### 4. Key Decisions
```yaml
decisions:
  - "Constellation architecture: 3 Claude + 1 Gemini + 1 ChatGPT"
  - "Model routing: Opus for comprehensive, Sonnet for tactical"
  - "Temporal vs evergreen: Archive temporal, CANON evergreen"
```

### 5. Active Intentions
```yaml
intentions:
  urgent: [INT-1201, INT-1202, INT-1209]
  sprint: [INT-1203, INT-1210-1213]
```

---

## PROCESS

### 1. Session Initialization

When starting Oracle session:

1. Read `ORACLE_ARC.md` for trajectory
2. Read latest `EXECUTION_LOG-*` for recent activity
3. Read `DYN-BACKLOG.md` for project status
4. Read `ARCH-INTENTION_COMPASS.md` for active intentions
5. Synthesize into working context

### 2. Context Document Creation

When creating Blitzkrieg pedigree:

```markdown
# ORACLE [N] PEDIGREE: BLITZKRIEG [M]
## [Title]

**Issued**: [date]
**Oracle**: [N]
**Blitzkrieg**: [M]
**Scope**: [brief description]

---

## STRATEGIC CONTEXT
[Campaign progress, what led here]

## BLITZKRIEG STRUCTURE
[Streams, models, durations]

## KEY DECISIONS
[Decisions made this session]

## DEPENDENCIES
[What this enables, what it requires]

## LEDGER UPDATES EXPECTED
[Projects and tasks affected]

## COMPANION DIRECTIVES
[Links to stream directives]
```

### 3. Cross-Platform Pedigree

When work spans multiple platforms:

```yaml
cross_platform:
  claude_web: "Oracle strategic synthesis"
  claude_code_1: "Stream A execution"
  claude_code_2: "Stream B execution"
  gemini: "Validation and cross-check"
  chatgpt: "Alternative perspective"
```

---

## OUTPUT FORMAT

### Quick Pedigree (In-Context)
```markdown
**Oracle 12 | Blitzkrieg 45 | 2026-01-12**
- Campaign: Expansion phase (12+)
- Last complete: Blitzkrieg 44 (model specification, intention compass)
- Active: PROJ-002 (60%), PROJ-012 (80%), PROJ-014 (40%)
- Focus: IIC completion + Skills genesis
```

### Full Pedigree Document
See template in Process section above.

---

## EXAMPLES

### Good Pedigree Opening

"This is Oracle 12, continuing the Expansion phase. Blitzkriegs 43-44 established constellation architecture and formalized model specification. We're now executing Blitzkrieg 45 to complete IIC configuration and create process Skills."

### Good Cross-Session Reference

"Per Blitzkrieg 44 findings (ARCH-TECH_TREE_AUDIT.md), INT-1210-1212 can be marked resolved—canonical coverage is sufficient."

---

## ANTI-PATTERNS

1. **Starting fresh**: Never begin without reading recent execution logs

2. **Ignoring ledgers**: Always verify tasks.csv and projects.csv for ground truth

3. **Handoff when Pedigree applies**: Repository work uses Pedigree, not Handoff

4. **Over-documentation**: Pedigree is structured reference, not narrative essay

5. **Missing lineage**: Always include Oracle number and trajectory position

---

## MAINTENANCE

- Update ORACLE_ARC.md at session end
- Archive completed pedigrees in execution logs
- Verify ledger updates before claiming completion

---

*Pedigree Skill v1.0.0 | Syncrescendence*
```

### 3.2 Verification

```bash
wc -l .claude/skills/pedigree.md
# Should be 180+ lines
```

---

## PHASE 4: LEDGER UPDATE (~5 minutes)

### 4.1 Update tasks.csv

Add to `00-ORCHESTRATION/state/tasks.csv`:

```csv
TASK-095,PROJ-016,Create intentions.md Skill,skill,done,P2,Claude_Code_3,null,0.5,0.5,2026-01-12,2026-01-12,Blitzkrieg 45 - Intention extraction skill
TASK-096,PROJ-016,Create pedigree.md Skill,skill,done,P2,Claude_Code_3,TASK-095,0.5,0.5,2026-01-12,2026-01-12,Blitzkrieg 45 - Oracle pedigree skill
```

### 4.2 Update projects.csv

Update PROJ-016 status:
- Progress: 0% → 20% (2 of estimated 10 skills)
- Status: not_started → in_progress

---

## PHASE 5: EXECUTION LOG (~5 minutes)

Create `00-ORCHESTRATION/logs/EXECUTION_LOG-2026-01-12-045B.md` documenting:
- Actions taken
- Files created
- Verification evidence
- Duration breakdown

---

## VERIFICATION CHECKLIST

- [ ] `.claude/skills/` directory exists
- [ ] `intentions.md` Skill exists with full content
- [ ] `pedigree.md` Skill exists with full content
- [ ] Skills follow consistent structure
- [ ] tasks.csv updated with TASK-095-096
- [ ] projects.csv updated (PROJ-016 → in_progress)
- [ ] Execution log created
- [ ] No violations of flat principle (skills dir is standard Claude Code location)

---

## DELIVERABLES SUMMARY

| File | Type | Location |
|------|------|----------|
| intentions.md | Skill | .claude/skills/ |
| pedigree.md | Skill | .claude/skills/ |
| EXECUTION_LOG-2026-01-12-045B.md | Log | 00-ORCHESTRATION/logs/ |

---

## CONSTITUTIONAL COMPLIANCE

### Skills Location
`.claude/skills/` is the standard Claude Code location for Skills. This is NOT a violation of flat principle—it's adherence to Claude Code conventions.

### Verification Before Completion
Verify all files exist with `ls` and `wc -l` before claiming completion.

---

*DIRECTIVE-045B | Stream B | Blitzkrieg 45 | Oracle 12*
*Model: Sonnet 4.5 | Thinking: default*
