# DIRECTIVE-041A: CLAUDE.md + CUSTOM COMMANDS DEPLOYMENT
## Stream A — Automation Infrastructure (Industrial Engineering Lens)

**Issued**: 2026-01-08
**Stream**: A (Claude 2)
**Priority**: P0 — CRITICAL
**Estimated Duration**: 90-120 minutes
**Parallel**: DIRECTIVE-041B executing simultaneously on Claude 3
**Project**: PROJ-011 (Automation Infrastructure)

---

## PREAMBLE

You are Claude 2, executing Stream A of Blitzkrieg 41. You have received this directive alongside ORACLE10_CONTEXT_v3.md. **READ THE CONTEXT FIRST.**

**Your mandate**: Deploy CLAUDE.md, custom commands, Makefile, and settings configuration to address the Industrial Engineering lens failure (Sovereign relay bottleneck).

**Critical understanding**: This is not optional infrastructure — it's the foundation that makes all future work more efficient. Every minute invested here saves hours of relay friction.

---

## PHASE 1: CREATE CLAUDE.md (30 minutes)

### 1.1 Create Repository Root CLAUDE.md

Create `CLAUDE.md` at repository root with this exact content:

```markdown
# Syncrescendence Knowledge Management System

## Identity
This is Syncrescendence, a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale. You are executing directives as part of a multi-Claude coordination system.

## Constitutional Rules

### Structural (ABSOLUTE)
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-) instead of subdirectories.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00-06. Do not create unnumbered directories at root.
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit Sovereign approval for deletions.

### Semantic (ABSOLUTE)
4. **DISTILLATION SEMANTICS**: "Metabolize/distill" = READ → EXTRACT unique value → COMPRESS → DELETE originals. NOT organizational restructuring.
5. **CATEGORY ERROR**: Metabolism applies to CONTENT, not ORCHESTRATION. State/ and logs/ are living infrastructure—never delete.
6. **LEDGER GROUND TRUTH**: tasks.csv is authoritative. Verify actual state, not execution reports.

### Operational (ABSOLUTE)
7. **ATOMIC UPDATES**: CSV updates use temp file → validate → rename pattern.
8. **VERIFICATION BEFORE COMPLETION**: Never claim done without running verification commands.
9. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes (feat:, fix:, docs:, chore:, refactor:).

## Directory Structure
- `00-ORCHESTRATION/` — Strategic coordination (directives, logs, state)
- `01-CANON/` — Verified canonical knowledge (PROTECTED)
- `02-ENGINE/` — Functions, prompts, model profiles
- `03-QUEUE/` — Pending items by modal
- `04-SOURCES/` — Source documents (raw/, processed/)
- `05-MEMORY/` — Historical preservation
- `06-EXEMPLA/` — Templates and examples

## Critical Commands
```bash
make verify              # Run all validation checks
make update-ledgers      # Sync CSV ledgers with validation
make sync                # Pull latest, rebase, push
make tree                # Generate current tree
```

## Processing Patterns
- Source intake: See @00-ORCHESTRATION/state/REF-PROCESSING_PATTERN.md
- Ledger updates: See @00-ORCHESTRATION/state/REF-STANDARDS.md
- Verification: Run before ANY completion claim

## Anti-Patterns (PROHIBITED)
- Creating subdirectories anywhere
- Skipping verification to "save time"
- Deferring ledger updates to "later"
- Claiming integration without grep verification
- Modifying state/ without validation

## Extended Thinking
Use these triggers for complex analysis:
- `think` — Standard extended thinking (~4K tokens)
- `think hard` — Moderate depth (~8K tokens)
- `ultrathink` — Maximum depth (~32K tokens)

Use ultrathink for: architectural decisions, multi-step processing, forensic analysis.
Do NOT use for: simple lookups, single-file edits, routine commits.

## Session Management
- Use /compact before context fills
- Update session state in 00-ORCHESTRATION/state/
- Name sessions descriptively for resumption
```

### 1.2 Verification
```bash
cat CLAUDE.md | head -50
wc -l CLAUDE.md  # Should be ~70-80 lines
```

---

## PHASE 2: CREATE CUSTOM COMMANDS (30 minutes)

### 2.1 Create Directory Structure
```bash
mkdir -p .claude/commands/project
```

### 2.2 Create `/project:verify` Command

Create `.claude/commands/project/verify.md`:

```markdown
---
name: verify
description: Run comprehensive verification across the repository
allowed-tools: Bash(make:*), Bash(find:*), Bash(grep:*), Bash(wc:*), Bash(ls:*), Read
---
# Comprehensive Verification

Run all verification checks for Syncrescendence.

## Execution
```bash
# Structure checks
echo "=== Structure Verification ==="
echo -n "Subdirectories in wrong places: "
find . -mindepth 2 -type d -name "scaffolding" 2>/dev/null | wc -l

echo -n "Files at root: "
ls *.md 2>/dev/null | wc -l || echo "0"

# Ledger checks
echo ""
echo "=== Ledger Verification ==="
echo -n "tasks.csv rows: "
wc -l < 00-ORCHESTRATION/state/tasks.csv

echo -n "projects.csv rows: "
wc -l < 00-ORCHESTRATION/state/projects.csv

echo -n "sources.csv rows: "
wc -l < 04-SOURCES/sources.csv

# Content checks
echo ""
echo "=== Content Verification ==="
echo -n "Processed sources: "
ls 04-SOURCES/processed/*.md 2>/dev/null | wc -l || echo "0"

echo -n "CANON integrations: "
grep -l "SOURCE-" 01-CANON/*.md 2>/dev/null | wc -l || echo "0"

# Git status
echo ""
echo "=== Git Status ==="
git status --short

echo ""
echo "=== Verification Complete ==="
```

## Output
Report showing pass/fail for each category.
```

### 2.3 Create `/project:process-source` Command

Create `.claude/commands/project/process-source.md`:

```markdown
---
name: process-source
description: Process a source document from raw to processed
allowed-tools: Read, Write, Edit, Bash(python:*), Bash(grep:*), Glob
---
# Process Source Document

Process: $ARGUMENTS

## Workflow
1. **Locate**: Find in 04-SOURCES/raw/ using the provided identifier
2. **Read**: Extract full content and metadata
3. **Analyze**: Identify key themes, claims, relevance to chains
4. **Generate**: Create qualified brief with frontmatter
5. **Write**: Save to 04-SOURCES/processed/ with correct naming
6. **Update**: Add entry to sources.csv (status: processed, date_processed: today)
7. **Verify**: Confirm file exists and CSV updated

## Naming Convention
`{YYYYMMDD}-{platform}_{format}-{channel}-{guest_or_title}.md`

## Frontmatter Template
```yaml
---
id: SOURCE-{date}-{platform}-{format}-{channel}-{slug}
title: "{Title}"
date_published: {YYYY-MM-DD}
date_processed: {YYYY-MM-DD}
platform: {youtube|x|substack|arxiv}
format: {video|lecture|panel|thread|article}
creator: "{Channel/Author}"
guest: "{Guest Name if interview}"
signal_tier: {paradigm|strategic|tactical}
chains: [{Intelligence|Information|Insight|Expertise|Knowledge|Wisdom}]
status: processed
---
```

## Output
- Processed file in 04-SOURCES/processed/
- Updated sources.csv entry
- Verification confirmation
```

### 2.4 Create `/project:update-ledgers` Command

Create `.claude/commands/project/update-ledgers.md`:

```markdown
---
name: update-ledgers
description: Safely update CSV ledgers with atomic writes
allowed-tools: Read, Write, Bash(python:*), Bash(cp:*), Bash(mv:*)
---
# Update Ledgers Safely

Update: $ARGUMENTS

## Safety Protocol
1. **Backup**: `cp {ledger}.csv {ledger}.csv.bak.$(date +%Y%m%d%H%M%S)`
2. **Read**: Load current CSV content
3. **Modify**: Apply requested changes
4. **Validate**: Check required columns present, no malformed rows
5. **Write**: Write to temp file `{ledger}.csv.tmp`
6. **Verify**: Confirm temp file valid
7. **Rename**: `mv {ledger}.csv.tmp {ledger}.csv`
8. **Confirm**: Report changes made

## Supported Ledgers
- `00-ORCHESTRATION/state/tasks.csv`
- `00-ORCHESTRATION/state/projects.csv`
- `00-ORCHESTRATION/state/sprints.csv`
- `00-ORCHESTRATION/state/burndown.csv`
- `04-SOURCES/sources.csv`

## Required Columns
- tasks.csv: id, project_id, name, type, status, priority, owner
- projects.csv: id, name, type, status, priority, owner
- sources.csv: id, filename, status, date_processed

## Error Handling
If validation fails:
- Do NOT proceed with rename
- Report specific validation error
- Keep backup intact
```

### 2.5 Create `/project:blitzkrieg` Command

Create `.claude/commands/project/blitzkrieg.md`:

```markdown
---
name: blitzkrieg
description: Rapid batch processing of multiple items
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---
# Blitzkrieg Processing Mode

Ultrathink about optimal strategy, then execute rapid processing.

Target: $ARGUMENTS (or all pending if not specified)

## Pre-flight
1. Count pending items in target area
2. Assess complexity distribution
3. Check context capacity (use /compact if >60% full)
4. Verify ledgers unlocked

## Execution Phases

### Phase 1: Triage (5 min max)
- Categorize by type and complexity
- Identify dependencies
- Flag special handling needs

### Phase 2: Parallel Processing
- Simple items first (momentum)
- Group related items (efficiency)
- Use verification between batches

### Phase 3: Ledger Consolidation
- Batch all updates (single atomic operation per ledger)
- Validate cross-references
- Update processing_log

### Phase 4: Verification
- Run /project:verify
- Report success/failure counts
- Stage failures for review

## Constraints
- Maximum 10 items per session
- Stop on critical validation failure
- Document assumptions

## Output
Summary: X/Y processed, Z minutes, follow-ups needed
```

### 2.6 Verification
```bash
ls -la .claude/commands/project/
cat .claude/commands/project/verify.md | head -20
```

---

## PHASE 3: CREATE MAKEFILE (20 minutes)

### 3.1 Create Makefile at Repository Root

Create `Makefile`:

```makefile
# Syncrescendence Makefile
# Standard targets for repository operations

.PHONY: verify sync update-ledgers tree clean help

# Default target
help:
	@echo "Syncrescendence Repository Commands"
	@echo ""
	@echo "  make verify         - Run all verification checks"
	@echo "  make sync           - Pull, rebase, push"
	@echo "  make update-ledgers - Validate and report ledger status"
	@echo "  make tree           - Generate current directory tree"
	@echo "  make clean          - Remove temporary files"
	@echo ""

# Comprehensive verification
verify:
	@echo "=== Structure Verification ==="
	@echo -n "Unexpected subdirectories: "
	@find . -mindepth 2 -type d -name "scaffolding" 2>/dev/null | wc -l
	@echo -n "Root .md files: "
	@ls *.md 2>/dev/null | wc -l || echo "0"
	@echo ""
	@echo "=== Ledger Verification ==="
	@echo -n "tasks.csv rows: "
	@wc -l < 00-ORCHESTRATION/state/tasks.csv
	@echo -n "projects.csv rows: "
	@wc -l < 00-ORCHESTRATION/state/projects.csv
	@echo ""
	@echo "=== Content Verification ==="
	@echo -n "Processed sources: "
	@ls 04-SOURCES/processed/*.md 2>/dev/null | wc -l || echo "0"
	@echo -n "CANON with integrations: "
	@grep -l "SOURCE-" 01-CANON/*.md 2>/dev/null | wc -l || echo "0"
	@echo ""
	@echo "=== Git Status ==="
	@git status --short
	@echo ""
	@echo "=== Verification Complete ==="

# Git sync with rebase
sync:
	@echo "Pulling latest..."
	git pull --rebase
	@echo "Pushing changes..."
	git push
	@echo "Sync complete."

# Ledger status report
update-ledgers:
	@echo "=== Ledger Status ==="
	@echo ""
	@echo "tasks.csv:"
	@head -1 00-ORCHESTRATION/state/tasks.csv
	@echo "  Total rows: $$(wc -l < 00-ORCHESTRATION/state/tasks.csv)"
	@echo "  Done: $$(grep -c ',done,' 00-ORCHESTRATION/state/tasks.csv || echo 0)"
	@echo "  In Progress: $$(grep -c ',in_progress,' 00-ORCHESTRATION/state/tasks.csv || echo 0)"
	@echo ""
	@echo "projects.csv:"
	@head -1 00-ORCHESTRATION/state/projects.csv
	@echo "  Total rows: $$(wc -l < 00-ORCHESTRATION/state/projects.csv)"
	@echo "  Complete: $$(grep -c ',complete,' 00-ORCHESTRATION/state/projects.csv || echo 0)"
	@echo "  In Progress: $$(grep -c ',in_progress,' 00-ORCHESTRATION/state/projects.csv || echo 0)"
	@echo ""
	@echo "sources.csv:"
	@echo "  Total rows: $$(wc -l < 04-SOURCES/sources.csv)"
	@echo "  Processed: $$(grep -c ',processed,' 04-SOURCES/sources.csv || echo 0)"

# Generate directory tree
tree:
	@echo "Generating tree..."
	@tree -L 2 -I 'node_modules|.git|__pycache__|*.pyc' > 00-ORCHESTRATION/state/DYN-ACTUAL_TREE.md
	@echo "Tree saved to 00-ORCHESTRATION/state/DYN-ACTUAL_TREE.md"

# Clean temporary files
clean:
	@echo "Cleaning temporary files..."
	@find . -name "*.tmp" -delete
	@find . -name "*.bak.*" -mtime +7 -delete
	@find . -name ".DS_Store" -delete
	@echo "Clean complete."
```

### 3.2 Verification
```bash
cat Makefile | head -30
make help
make verify
```

---

## PHASE 4: CONFIGURE SETTINGS (15 minutes)

### 4.1 Create `.claude/settings.json`

```bash
mkdir -p .claude
```

Create `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Edit",
      "Glob",
      "Grep",
      "Bash(make:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(find:*)",
      "Bash(wc:*)",
      "Bash(head:*)",
      "Bash(tail:*)",
      "Bash(cat:*)",
      "Bash(ls:*)",
      "Bash(tree:*)",
      "Bash(cp:*)",
      "Bash(mv:*)",
      "Bash(mkdir:*)",
      "Bash(python:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(git push --force:*)",
      "Bash(git checkout main:*)",
      "Bash(sudo:*)"
    ]
  },
  "project": {
    "name": "Syncrescendence",
    "description": "Civilizational sensing infrastructure"
  }
}
```

### 4.2 Create `.claude/settings.local.json.template`

```json
{
  "account": {
    "name": "Claude Instance [ALPHA|BETA|GAMMA]",
    "worktree": "../syncrescendence-[alpha|beta|gamma]"
  },
  "permissions": {
    "allow": [],
    "deny": []
  }
}
```

### 4.3 Update `.gitignore`

Append to `.gitignore`:
```
# Claude local settings
.claude/settings.local.json
CLAUDE.local.md

# Temporary files
*.tmp
*.bak.*
```

### 4.4 Verification
```bash
cat .claude/settings.json
ls -la .claude/
```

---

## PHASE 5: UPDATE LEDGERS (15 minutes)

### 5.1 Add PROJ-011 to projects.csv

Add row:
```
PROJ-011,Automation Infrastructure,initiative,in_progress,P0,Oracle10,PROJ-001,10,modal1,2026-01-10,2026-01-08,2026-01-08,CLAUDE.md + commands + MCP
```

### 5.2 Update Project Dependencies

Update PROJ-002 blocked_by: `PROJ-001` → `PROJ-011`
Update PROJ-003 blocked_by: `PROJ-002` → `PROJ-011`
Update PROJ-004: Can be deprecated or repurposed (absorbed into PROJ-011)

### 5.3 Add Tasks for Stream A

Add to tasks.csv:
```
TASK-040,PROJ-011,Create CLAUDE.md,infrastructure,done,P0,Claude_Code_2,null,0.5,{actual},2026-01-08,2026-01-08,Constitutional rules deployed
TASK-041,PROJ-011,Create custom commands,infrastructure,done,P0,Claude_Code_2,TASK-040,0.5,{actual},2026-01-08,2026-01-08,4 commands in .claude/commands/project/
TASK-042,PROJ-011,Create Makefile,infrastructure,done,P0,Claude_Code_2,TASK-040,0.25,{actual},2026-01-08,2026-01-08,verify/sync/update-ledgers/tree/clean
TASK-043,PROJ-011,Configure settings,infrastructure,done,P0,Claude_Code_2,TASK-040,0.25,{actual},2026-01-08,2026-01-08,Permission allowlist configured
```

### 5.4 Verification
```bash
grep "PROJ-011" 00-ORCHESTRATION/state/projects.csv
grep "TASK-04" 00-ORCHESTRATION/state/tasks.csv | wc -l
```

---

## PHASE 6: GIT COMMIT + VERIFICATION (10 minutes)

### 6.1 Stage and Commit
```bash
git add CLAUDE.md Makefile .claude/ .gitignore
git add 00-ORCHESTRATION/state/projects.csv 00-ORCHESTRATION/state/tasks.csv
git commit -m "feat(PROJ-011): Deploy CLAUDE.md, custom commands, Makefile

- Add CLAUDE.md with constitutional rules at repo root
- Create .claude/commands/project/ with 4 custom commands
- Add Makefile with verify, sync, update-ledgers, tree, clean targets
- Configure .claude/settings.json with permission allowlist
- Add PROJ-011 to project registry
- Update project dependencies (PROJ-002, PROJ-003 now blocked by PROJ-011)

Addresses Industrial Engineering lens failure (18-lens #12).
Part of Blitzkrieg 41, Stream A."
```

### 6.2 Final Verification
```bash
make verify
```

### 6.3 Create Execution Log

Create `00-ORCHESTRATION/execution_logs/EXECUTION_LOG-2026-01-08-041A.md` with:
- All phases completed
- Verification outputs
- Files created/modified
- Task status updates

---

## SUCCESS CRITERIA

Stream A is complete when:
- [ ] `cat CLAUDE.md` shows constitutional rules (~70-80 lines)
- [ ] `ls .claude/commands/project/` shows 4 .md files
- [ ] `make help` shows 5 targets
- [ ] `make verify` runs without error
- [ ] `cat .claude/settings.json` shows permission allowlist
- [ ] `grep PROJ-011 00-ORCHESTRATION/state/projects.csv` returns row
- [ ] `grep TASK-04 00-ORCHESTRATION/state/tasks.csv | wc -l` returns 4+
- [ ] Git commit completed with semantic message
- [ ] Execution log created with verification outputs

---

## ANTI-PATTERNS

**DO NOT**:
- Skip creating any of the 4 commands
- Use different file paths than specified
- Forget to update ledgers
- Claim complete without running `make verify`
- Create the execution log without actual verification outputs

**DO**:
- Execute each phase completely before moving to next
- Copy exact content for CLAUDE.md and commands
- Verify with bash commands after each phase
- Update ledgers atomically
- Include all outputs in execution log

---

*Industrial Engineering lens addressed. Sovereign relay friction reduced. Infrastructure enables everything.*
