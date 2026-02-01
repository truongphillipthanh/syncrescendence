# DIRECTIVE-042D: GEMINI CLI VALIDATION
## Stream D Test Execution for Gemini CLI
**Date**: 2026-01-09
**Priority**: P2
**Project**: PROJ-012 (Multi-CLI Integration)
**Estimated Duration**: 30 minutes

---

## MISSION

Validate Gemini CLI operational capability within the Syncrescendence repository. This is a test directive to confirm:
1. GEMINI.md context loading
2. Repository structure visibility
3. File operations capability
4. Comparative assessment with Claude Code

---

## PREREQUISITES

**Before executing this directive**:

1. Ensure Gemini CLI is installed:
   ```bash
   npm install -g @google/gemini-cli
   # or verify with:
   gemini --version
   ```

2. Authenticate:
   ```bash
   gemini
   # Select "Login with Google" and complete OAuth flow
   ```

3. Place GEMINI.md at repository root (created by Stream B or manually)

4. Navigate to Syncrescendence repository:
   ```bash
   cd /path/to/syncrescendence
   ```

---

## VALIDATION TASKS

### Task 1: Context Verification

**Execute**:
```bash
gemini
```

Then in Gemini CLI:
```
/memory show
```

**Expected Result**: GEMINI.md content displayed, showing:
- Identity section (Syncrescendence)
- Constitutional Rules (9 rules)
- Directory Structure (7 numbered directories)
- Gemini-Specific Notes

**Record**: ✓ Pass / ✗ Fail + notes

### Task 2: Directory Structure Visibility

**Execute in Gemini CLI**:
```
List the top-level directories in this repository and briefly describe each.
```

**Expected Result**: Output showing:
- 00-ORCHESTRATION/
- 01-CANON/
- 02-ENGINE/
- 03-QUEUE/
- 04-SOURCES/
- 05-MEMORY/
- 06-EXEMPLA/

**Record**: ✓ Pass / ✗ Fail + notes

### Task 3: File Reading Capability

**Execute in Gemini CLI**:
```
Read the first 20 lines of tasks.csv and summarize the task structure.
```

**Expected Result**: Gemini should:
- Read the CSV file
- Identify columns (id, project_id, name, type, status, etc.)
- Summarize task count and status distribution

**Record**: ✓ Pass / ✗ Fail + notes

### Task 4: File Creation Capability

**Execute in Gemini CLI**:
```
Create a file called GEMINI_VALIDATION_TEST.md in the current directory with the following content:
# Gemini CLI Validation
**Date**: 2026-01-09
**Status**: Validation test file
**Result**: [Gemini to fill in assessment]
```

**Expected Result**: File created successfully

**Verification**:
```bash
cat GEMINI_VALIDATION_TEST.md
```

**Record**: ✓ Pass / ✗ Fail + notes

### Task 5: Search Capability

**Execute in Gemini CLI**:
```
Search the repository for files containing "IIC" and list the top 5 most relevant.
```

**Expected Result**: Should identify CANON files related to IIC:
- CANON-31140-IIC-lunar-ACUMEN-planetary-INFORMATION.md
- CANON-31141-FIVE_ACCOUNT-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md
- (and others)

**Record**: ✓ Pass / ✗ Fail + notes

### Task 6: Headless Mode Test

**Exit interactive mode** and run:
```bash
gemini -p "List the files in 01-CANON/ that contain 'cosmos' in the filename" --output-format json
```

**Expected Result**: JSON output with list of cosmos-tier CANON files

**Record**: ✓ Pass / ✗ Fail + notes

---

## VALIDATION REPORT TEMPLATE

Create this report after completing all tasks:

```markdown
# GEMINI CLI VALIDATION REPORT
**Date**: 2026-01-09
**Executor**: [Sovereign]
**Gemini CLI Version**: [output of gemini --version]

## Environment
- OS: [macOS/Linux/Windows]
- Terminal: [iTerm/etc.]
- Node.js Version: [node --version]
- Authentication: [Google OAuth / API Key / Vertex AI]

## Task Results

| Task | Description | Result | Notes |
|------|-------------|--------|-------|
| 1 | Context Verification | [✓/✗] | [notes] |
| 2 | Directory Visibility | [✓/✗] | [notes] |
| 3 | File Reading | [✓/✗] | [notes] |
| 4 | File Creation | [✓/✗] | [notes] |
| 5 | Search Capability | [✓/✗] | [notes] |
| 6 | Headless Mode | [✓/✗] | [notes] |

## Overall Assessment

**Pass Rate**: [X/6] tasks passed

**Recommendation**: 
- [ ] APPROVED for production use
- [ ] APPROVED with limitations: [describe]
- [ ] NOT APPROVED: [describe blockers]

## Capability Comparison with Claude Code

| Capability | Claude Code | Gemini CLI | Notes |
|------------|-------------|------------|-------|
| Context loading | ✓ | [✓/✗] | |
| File operations | ✓ | [✓/✗] | |
| Search | ✓ | [✓/✗] | |
| Headless mode | ✓ | [✓/✗] | |
| Extended thinking | ✓ | [✓/✗] | |
| MCP servers | ✓ | [✓/✗] | |

## Recommended Use Cases

If approved, Gemini CLI is recommended for:
- [ ] Parallel execution (Stream D zone)
- [ ] Overflow capacity
- [ ] Specific model access (Gemini 3 Pro for reasoning)
- [ ] Extended context (1M tokens vs 200K)

## Issues Encountered

[Document any issues, errors, or unexpected behavior]

## Next Steps

1. [Action item 1]
2. [Action item 2]
3. [Action item 3]
```

---

## CLEANUP

After validation, clean up test file:
```bash
rm GEMINI_VALIDATION_TEST.md
```

Or keep it as proof of successful validation (move to 05-MEMORY/).

---

## SUCCESS CRITERIA

| Criterion | Target |
|-----------|--------|
| Context loads | GEMINI.md visible in /memory show |
| File operations work | Can read and create files |
| Search works | Can find files by content |
| Headless works | JSON output produced |
| Overall pass rate | ≥5/6 tasks |

---

## LEDGER UPDATE

After validation, update tasks.csv:
```csv
TASK-060,PROJ-012,Validate Gemini CLI operations,task,done,P2,Gemini_CLI,null,0.5,[actual],2026-01-09,2026-01-09,Result: [APPROVED/NOT_APPROVED]
```

---

*This directive validates multi-CLI capability expansion. Successful validation enables 4-instance parallel execution.*
