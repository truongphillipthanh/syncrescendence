# DIRECTIVE-042A: ROOT CLEANUP + RESEARCH PROTOCOL + GITHUB SYNC
## Stream A — Oracle 10 Closure (Hygiene)

**Issued**: 2026-01-08
**Stream**: A (Claude 2)
**Priority**: P1 — Oracle Closure
**Estimated Duration**: 45-60 minutes
**Parallel**: DIRECTIVE-042B executing simultaneously on Claude 3
**Scope**: Oracle 10 Finalization

---

## PREAMBLE

You are Claude 2, executing Stream A of Blitzkrieg 42 — the final blitzkrieg of Oracle 10. Your mandate: Clean root pollution, establish research artifact protocol, and validate GitHub sync.

**READ ORACLE10_CONTEXT_v4.md first.**

---

## PHASE 1: ROOT POLLUTION CLEANUP (15 minutes)

### 1.1 Assess Current Root

```bash
ls *.md 2>/dev/null
# Expected pollution:
# - claude_code_optimization_architecture.md
# - DIRECTIVE-041A.md
# - DIRECTIVE-041B.md
# - ORACLE10_CONTEXT_v3.md
# Acceptable:
# - CLAUDE.md (constitutional, stays at root)
```

### 1.2 Relocate Directives

```bash
mv DIRECTIVE-041A.md 00-ORCHESTRATION/directives/
mv DIRECTIVE-041B.md 00-ORCHESTRATION/directives/
```

### 1.3 Relocate Oracle Context

```bash
mv ORACLE10_CONTEXT_v3.md 00-ORCHESTRATION/oracle_contexts/
```

### 1.4 Handle Research Artifact

The `claude_code_optimization_architecture.md` requires special handling — see Phase 2.

### 1.5 Verification

```bash
ls *.md 2>/dev/null
# Should show ONLY: CLAUDE.md

ls 00-ORCHESTRATION/directives/DIRECTIVE-041* | wc -l
# Should be 2

ls 00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT* | wc -l
# Should be 4 (root, v2, v3, plus any others)
```

---

## PHASE 2: RESEARCH ARTIFACT PROTOCOL (20 minutes)

### 2.1 Create Protocol Documentation

Create `00-ORCHESTRATION/state/REF-RESEARCH_ARTIFACTS.md`:

```markdown
# Research Artifact Protocol

## Purpose
Handle deep research outputs systematically to prevent root pollution and ensure knowledge preservation.

## Artifact Types

### Type 1: Deep Research Reports
- **Source**: Claude Desktop "Research" feature, extended analysis
- **Characteristics**: 20K-100K+ tokens, structured reports, comprehensive
- **Example**: `claude_code_optimization_architecture.md`

### Type 2: Oracle Session Outputs
- **Source**: Oracle thread synthesis, strategic analysis
- **Characteristics**: 5K-20K tokens, context-specific
- **Example**: `ORACLE10_CONTEXT_v*.md`

### Type 3: Execution Artifacts
- **Source**: Claude Code execution, temporary files
- **Characteristics**: Variable size, often superseded
- **Example**: Directive files dropped at root

## Disposition Decision Tree

```
Is this a deep research report (Type 1)?
├─ YES: Does it contain unique value not in CANON?
│   ├─ YES: Archive as RESEARCH-{date}-{topic}.md in 05-ARCHIVE/
│   └─ NO: Distill into relevant CANON, delete original
└─ NO: Is this an Oracle context (Type 2)?
    ├─ YES: Move to 00-ORCHESTRATION/oracle_contexts/
    └─ NO: Is this a directive/execution artifact (Type 3)?
        ├─ YES: Move to appropriate 00-ORCHESTRATION/ subdirectory
        └─ NO: Evaluate case-by-case, default to 05-ARCHIVE/
```

## Naming Convention

### Research Archives
`RESEARCH-{YYYYMMDD}-{topic_slug}.md`

Examples:
- `RESEARCH-20260108-claude_code_optimization.md`
- `RESEARCH-20260115-mcp_architecture_analysis.md`

### Distillation Candidates
If research report value can be compressed into CANON:
1. Extract key insights
2. Add to relevant CANON document (e.g., CANON-30340-IMPLEMENTATION_PATTERNS)
3. Delete or archive original (append `-DISTILLED` suffix if archiving)

## Root Cleanup Script

See `00-ORCHESTRATION/scripts/cleanup_root.sh` for automated enforcement.

## Periodic Maintenance

Run weekly or before each Oracle session:
```bash
./00-ORCHESTRATION/scripts/cleanup_root.sh
make verify
```
```

### 2.2 Create Cleanup Script

Create `00-ORCHESTRATION/scripts/cleanup_root.sh`:

```bash
#!/bin/zsh
# cleanup_root.sh
# Enforce root cleanliness by relocating pollution files

set -e

echo "=== Root Cleanup Script ==="
echo ""

# Define acceptable root files
ACCEPTABLE=(
    "CLAUDE.md"
    "Makefile"
    "README.md"
    ".gitignore"
)

# Find .md files at root
echo "Scanning root for .md files..."
ROOT_MD=$(ls *.md 2>/dev/null || true)

for file in $ROOT_MD; do
    # Skip acceptable files
    if [[ " ${ACCEPTABLE[@]} " =~ " ${file} " ]]; then
        echo "  ✓ $file (acceptable)"
        continue
    fi
    
    echo "  ⚠ Found pollution: $file"
    
    # Determine disposition based on filename pattern
    if [[ "$file" == DIRECTIVE-* ]]; then
        echo "    → Moving to 00-ORCHESTRATION/directives/"
        mv "$file" 00-ORCHESTRATION/directives/
    elif [[ "$file" == ORACLE*CONTEXT* || "$file" == ORACLE*_INIT* ]]; then
        echo "    → Moving to 00-ORCHESTRATION/oracle_contexts/"
        mv "$file" 00-ORCHESTRATION/oracle_contexts/
    elif [[ "$file" == EXECUTION_LOG-* ]]; then
        echo "    → Moving to 00-ORCHESTRATION/execution_logs/"
        mv "$file" 00-ORCHESTRATION/execution_logs/
    elif [[ "$file" == *research* || "$file" == *optimization* || "$file" == *analysis* ]]; then
        # Research artifacts get dated prefix
        DATE=$(date +%Y%m%d)
        SLUG=$(echo "$file" | sed 's/.md$//' | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
        NEWNAME="RESEARCH-${DATE}-${SLUG}.md"
        echo "    → Archiving as 05-ARCHIVE/$NEWNAME"
        mv "$file" "05-ARCHIVE/$NEWNAME"
    else
        echo "    → Default: Archiving to 05-ARCHIVE/"
        mv "$file" 05-ARCHIVE/
    fi
done

echo ""
echo "=== Cleanup Complete ==="

# Verify
echo ""
echo "Root .md files remaining:"
ls *.md 2>/dev/null || echo "  (none except acceptable)"
```

### 2.3 Make Script Executable

```bash
chmod +x 00-ORCHESTRATION/scripts/cleanup_root.sh
```

### 2.4 Execute Cleanup for Research Artifact

```bash
# Move the research artifact with proper naming
DATE=$(date +%Y%m%d)
mv claude_code_optimization_architecture.md \
   05-ARCHIVE/RESEARCH-${DATE}-claude_code_optimization.md
```

### 2.5 Verification

```bash
ls 05-ARCHIVE/RESEARCH-* | wc -l
# Should be 1

cat 00-ORCHESTRATION/state/REF-RESEARCH_ARTIFACTS.md | head -30
# Should show protocol documentation
```

---

## PHASE 3: GITHUB SYNC VALIDATION (15 minutes)

### 3.1 Stage All Changes

```bash
git add -A
git status
```

### 3.2 Commit with Semantic Message

```bash
git commit -m "chore(Oracle10): Root cleanup + research artifact protocol

- Relocate DIRECTIVE-041A/B to directives/
- Relocate ORACLE10_CONTEXT_v3 to oracle_contexts/
- Archive research artifact as RESEARCH-20260108-claude_code_optimization.md
- Add REF-RESEARCH_ARTIFACTS.md protocol documentation
- Add cleanup_root.sh automation script

Part of Oracle 10 closure, Blitzkrieg 42 Stream A."
```

### 3.3 Push to Remote

```bash
git push origin develop
# Or: git push origin main (depending on branch strategy)
```

### 3.4 Verify Sync

```bash
git status
# Should show: nothing to commit, working tree clean

git log --oneline -3
# Should show recent commits including this one
```

---

## PHASE 4: UPDATE LEDGERS (10 minutes)

### 4.1 Add Tasks

Add to `00-ORCHESTRATION/state/tasks.csv`:

```csv
TASK-048,null,Root pollution cleanup,hygiene,done,P1,Claude_Code_2,null,0.25,{actual},2026-01-08,2026-01-08,Relocated 4 files from root
TASK-049,null,Research artifact protocol,documentation,done,P1,Claude_Code_2,null,0.5,{actual},2026-01-08,2026-01-08,REF-RESEARCH_ARTIFACTS.md + cleanup_root.sh
TASK-050,null,GitHub sync validation,verification,done,P1,Claude_Code_2,null,0.25,{actual},2026-01-08,2026-01-08,First successful sync post-041
```

### 4.2 Verification

```bash
grep "TASK-04[89]" 00-ORCHESTRATION/state/tasks.csv
grep "TASK-050" 00-ORCHESTRATION/state/tasks.csv
```

---

## PHASE 5: CREATE EXECUTION LOG (5 minutes)

Create `00-ORCHESTRATION/execution_logs/EXECUTION_LOG-2026-01-08-042A.md` with:

```markdown
# EXECUTION LOG: DIRECTIVE-042A
## Stream A — Root Cleanup + Research Protocol

**Date**: 2026-01-08
**Directive**: DIRECTIVE-042A
**Stream**: A
**Duration**: ~{actual} minutes
**Status**: COMPLETE

---

## Phases Completed

### Phase 1: Root Cleanup ✓
- Relocated DIRECTIVE-041A.md → directives/
- Relocated DIRECTIVE-041B.md → directives/
- Relocated ORACLE10_CONTEXT_v3.md → oracle_contexts/
- Research artifact handled in Phase 2

### Phase 2: Research Protocol ✓
- Created REF-RESEARCH_ARTIFACTS.md
- Created cleanup_root.sh
- Archived claude_code_optimization_architecture.md as RESEARCH-20260108-claude_code_optimization.md

### Phase 3: GitHub Sync ✓
- All changes committed
- Pushed to remote
- Working tree clean

### Phase 4: Ledgers Updated ✓
- TASK-048, TASK-049, TASK-050 added and marked done

---

## Verification Outputs

```
# Root .md files
$ ls *.md
CLAUDE.md

# Research archive
$ ls 05-ARCHIVE/RESEARCH-*
05-ARCHIVE/RESEARCH-20260108-claude_code_optimization.md

# Git status
$ git status
nothing to commit, working tree clean
```

---

## Success Criteria Checklist

- [x] Root contains only CLAUDE.md (among .md files)
- [x] Research artifact relocated with proper naming
- [x] REF-RESEARCH_ARTIFACTS.md created
- [x] cleanup_root.sh created and executable
- [x] GitHub sync successful
- [x] Tasks added to ledger
- [x] Execution log created

---

*Stream A complete. Root clean. Protocol established. Sync validated.*
```

---

## SUCCESS CRITERIA

Stream A is complete when:
- [ ] `ls *.md` shows only `CLAUDE.md`
- [ ] `ls 05-ARCHIVE/RESEARCH-*` shows 1+ files
- [ ] `cat 00-ORCHESTRATION/state/REF-RESEARCH_ARTIFACTS.md` shows protocol
- [ ] `ls 00-ORCHESTRATION/scripts/cleanup_root.sh` exists and is executable
- [ ] `git status` shows clean working tree
- [ ] Tasks TASK-048, TASK-049, TASK-050 in ledger
- [ ] Execution log created

---

*Root pollution eliminated. Research protocol established. GitHub sync validated.*
