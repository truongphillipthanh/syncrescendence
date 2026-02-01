---
directive_id: DIR-20260123-LOW-HANGING-FRUIT
lane: A
toolchain: claude_code
model: opus-4.5
thinking: ultrathink
success_criteria:
  - All nomenclature violations fixed (0 lowercase unprefixed files)
  - All orphaned files relocated
  - Flat principle violations addressed
  - Duplicates consolidated
  - Git commit with verification
inputs:
  - CLAUDE.md
  - 00-ORCHESTRATION/state/REF-STANDARDS.md
outputs:
  - EXECUTION_LOG-20260123-LOW-HANGING-FRUIT.md → -OUTGOING/
---

# DIR-20260123: LOW-HANGING FRUIT EXECUTION

## CONTEXT

Prior Gemini CLI surveys (2026-01-19, 2026-01-20) identified mechanical violations requiring no Sovereign judgment. These are syntax-level fixes—nomenclature, location, duplication—not semantic decisions.

**Philosophy**: Clear the noise so the signal becomes visible for true annealment.

## PHASE 1: NOMENCLATURE NORMALIZATION

### 1.1 Lowercase → Prefixed (00-ORCHESTRATION/state/)

```bash
# Execute these renames
mv "00-ORCHESTRATION/state/burndown.csv" "00-ORCHESTRATION/state/DYN-BURNDOWN.csv"
mv "00-ORCHESTRATION/state/projects.csv" "00-ORCHESTRATION/state/DYN-PROJECTS.csv"
mv "00-ORCHESTRATION/state/tasks.csv" "00-ORCHESTRATION/state/DYN-TASKS.csv"
```

### 1.2 Lowercase → Prefixed (04-SOURCES/)

```bash
mv "04-SOURCES/creator_bios.md" "04-SOURCES/REF-CREATOR_BIOS.md"
mv "04-SOURCES/filename_mapping.csv" "04-SOURCES/REF-FILENAME_MAPPING.csv"
mv "04-SOURCES/sources.csv" "04-SOURCES/DYN-SOURCES.csv"
```

### 1.3 Lowercase → Prefixed (02-ENGINE/)

```bash
mv "02-ENGINE/coordination.yaml" "02-ENGINE/COORDINATION.yaml"
```

### 1.4 Template Normalization (06-EXEMPLA/)

```bash
mv "06-EXEMPLA/mcp.json.template" "06-EXEMPLA/TEMPLATE-MCP_CONFIG.json"
```

### 1.5 Update All References

After each rename, grep the entire repo and update references:

```bash
# For each renamed file, find and replace references
grep -r "burndown.csv" --include="*.md" --include="*.yaml" --include="*.sh" | xargs -I {} sed -i 's/burndown.csv/DYN-BURNDOWN.csv/g' {}
# Repeat for all renames
```

## PHASE 2: ORPHAN RELOCATION

### 2.1 Root-Level Strays

```bash
# AGENTS.md belongs in 02-ENGINE/registries/
mv "./AGENTS.md" "02-ENGINE/registries/REF-AGENTS.md"
```

### 2.2 Orchestration Strays

```bash
# Unprefixed files in 00-ORCHESTRATION/ root
mv "00-ORCHESTRATION/cognitive_core.md" "00-ORCHESTRATION/state/ARCH-COGNITIVE_CORE.md"
mv "00-ORCHESTRATION/decision_atoms.md" "00-ORCHESTRATION/state/REF-DECISION_ATOMS.md"
mv "00-ORCHESTRATION/lens_governance.md" "00-ORCHESTRATION/state/REF-LENS_GOVERNANCE.md"
mv "00-ORCHESTRATION/model_orchestration.md" "00-ORCHESTRATION/state/REF-MODEL_ORCHESTRATION.md"
```

### 2.3 Misplaced Oracle Contexts

```bash
# ORACLE12 context at wrong level
mv "00-ORCHESTRATION/ORACLE12_CONTEXT.md" "00-ORCHESTRATION/oracle_contexts/ORACLE12_CONTEXT.md"
```

## PHASE 3: FLAT PRINCIPLE ENFORCEMENT

### 3.1 Identify Nested Directories

```bash
find . -mindepth 3 -type d | grep -v node_modules | grep -v .git
```

### 3.2 Flatten 04-SOURCES/raw/claudecode/

The nested structure violates FLAT PRINCIPLE:
```
04-SOURCES/raw/claudecode/1-GettingStarted/
04-SOURCES/raw/claudecode/2-BuilderTool/
04-SOURCES/raw/claudecode/3-BestPractice_ProTiips/
```

**Action**: Flatten with prefix encoding:

```bash
# Move all nested files to 04-SOURCES/raw/ with category prefix
for f in 04-SOURCES/raw/claudecode/1-GettingStarted/*; do
  mv "$f" "04-SOURCES/raw/CLAUDECODE-GETSTARTED-$(basename $f)"
done
for f in 04-SOURCES/raw/claudecode/2-BuilderTool/*; do
  mv "$f" "04-SOURCES/raw/CLAUDECODE-BUILDERTOOL-$(basename $f)"
done
for f in 04-SOURCES/raw/claudecode/3-BestPractice_ProTiips/*; do
  mv "$f" "04-SOURCES/raw/CLAUDECODE-BESTPRACTICE-$(basename $f)"
done
# Remove empty directories
rmdir 04-SOURCES/raw/claudecode/1-GettingStarted
rmdir 04-SOURCES/raw/claudecode/2-BuilderTool
rmdir 04-SOURCES/raw/claudecode/3-BestPractice_ProTiips
rmdir 04-SOURCES/raw/claudecode
```

### 3.3 Flatten Other Nested Directories

Apply same pattern to any other violations found in Phase 3.1.

## PHASE 4: DUPLICATE CONSOLIDATION

### 4.1 COCKPIT.md Duplicates

```bash
# Compare root COCKPIT.md with -INBOX/COCKPIT.md
diff COCKPIT.md -INBOX/COCKPIT.md

# If -INBOX version is newer, replace root
# If identical or root is newer, delete -INBOX version
rm -INBOX/COCKPIT.md  # After verification
```

### 4.2 Oracle Context Duplicates

```bash
# Multiple ORACLE10_CONTEXT versions exist
# Keep ORACLE10_CONTEXT_FINAL.md, archive others
mv "00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT.md" "05-MEMORY/ORACLE10_CONTEXT-superseded.md"
```

## PHASE 5: -INBOX MECHANICAL TRIAGE

These items have CLEAR destinations per survey recommendations:

### 5.1 Move Directives to Proper Location

```bash
mv "-INBOX/DIR-20260120-EXECUTION-LOG-INFRASTRUCTURE.md" "00-ORCHESTRATION/directives/"
```

### 5.2 Move Prompts to Proper Location

```bash
mv "-INBOX/GEMINI-CORPUS-SENSING-PROMPT.md" "02-ENGINE/prompts/GEMINI-CORPUS-SENSING.md"
```

### 5.3 Move CSVs to Proper Location

```bash
mv "-INBOX/accounts.csv" "02-ENGINE/registries/DYN-ACCOUNTS.csv"
mv "-INBOX/platforms.csv" "02-ENGINE/registries/DYN-PLATFORMS.csv"
mv "-INBOX/roles.csv" "02-ENGINE/registries/DYN-ROLES.csv"
```

### 5.4 Archive Temporary Context Files

```bash
mv "-INBOX/last_5_interactions.zip" "05-MEMORY/"
mv "-INBOX/most_recent_completion.zip" "05-MEMORY/"
mv "-INBOX/previous_thread.md" "05-MEMORY/ARCH-previous_thread-20260123.md"
mv "-INBOX/final_interactions.md" "05-MEMORY/ARCH-final_interactions-20260123.md"
```

### 5.5 Move Diagrams to Assets

```bash
mkdir -p "04-SOURCES/assets/diagrams"  # Exception to flat - assets are binary
mv "-INBOX/diagrams/previous.png" "04-SOURCES/assets/diagrams/"
mv "-INBOX/diagrams/proposed.png" "04-SOURCES/assets/diagrams/"
rmdir "-INBOX/diagrams"
```

## PHASE 6: CREATE MISSING ROOT FILES

### 6.1 GEMINI.md

Create `GEMINI.md` at root for Gemini CLI context:

```markdown
# Syncrescendence - Gemini CLI Configuration

**Version**: 1.0.0
**Last Updated**: 2026-01-23

## Identity
This is Syncrescendence. You are ORACLE—full-spectrum sensing across the corpus.

## Your Capabilities
- 1M token context window
- Corpus-wide analysis
- Evidence pack generation

## Navigation
- `01-CANON/` — Canonical knowledge (read-only analysis)
- `04-SOURCES/` — Source material for processing
- `00-ORCHESTRATION/state/` — Current system state

## Output Format
All outputs should be evidence packs:
- Structured findings
- Token counts
- Specific file references
- Actionable recommendations

## Constraints
- Do not modify files directly
- Produce reports to `-OUTGOING/`
- Reference specific line numbers when citing
```

### 6.2 CODEX.md

Create `CODEX.md` at root for Codex CLI context (similar structure).

## VERIFICATION

After all phases complete:

```bash
# 1. No lowercase unprefixed files in state/
ls 00-ORCHESTRATION/state/*.csv | grep -v "^[A-Z]"  # Should return nothing

# 2. No orphans at 00-ORCHESTRATION root
ls 00-ORCHESTRATION/*.md | wc -l  # Should be 0 (all in subdirs)

# 3. No nested directories beyond depth 2
find . -mindepth 4 -type d | grep -v .git | wc -l  # Should be 0

# 4. AGENTS.md moved
test -f "02-ENGINE/registries/REF-AGENTS.md" && echo "PASS" || echo "FAIL"

# 5. Root files exist
test -f "GEMINI.md" && test -f "CODEX.md" && echo "PASS" || echo "FAIL"
```

## GIT COMMIT

```bash
git add -A
git commit -m "chore: LOW-HANGING-FRUIT execution - nomenclature, orphans, flat principle

- Renamed lowercase files to prefixed convention
- Relocated orphaned files to proper directories  
- Flattened 04-SOURCES/raw/claudecode/ structure
- Consolidated duplicate COCKPIT.md
- Triaged -INBOX mechanical items
- Created GEMINI.md and CODEX.md root files
- Verified all changes

DIR-20260123-LOW-HANGING-FRUIT complete"
```

## EXECUTION LOG TEMPLATE

Upon completion, create:

```markdown
# EXECUTION_LOG-20260123-LOW-HANGING-FRUIT.md

## Summary
- Files renamed: [count]
- Files relocated: [count]
- Directories flattened: [count]
- Duplicates resolved: [count]
- New files created: 2 (GEMINI.md, CODEX.md)

## Verification Results
[Paste verification output]

## Commit Hash
[hash]

## Issues Encountered
[Any blockers or decisions needed]
```
