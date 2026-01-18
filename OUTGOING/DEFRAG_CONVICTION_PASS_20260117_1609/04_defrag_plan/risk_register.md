# Risk Register
## Defrag Operation Risk Assessment
**Generated**: 2026-01-17

---

## I. RISK MATRIX

| Probability | Impact: LOW | Impact: MEDIUM | Impact: HIGH |
|-------------|-------------|----------------|--------------|
| **HIGH** | Accept | Mitigate | Avoid |
| **MEDIUM** | Accept | Mitigate | Mitigate |
| **LOW** | Accept | Accept | Mitigate |

---

## II. IDENTIFIED RISKS

### RISK-001: Loss of Unique Content During Compression
**Category**: Data Loss
**Probability**: LOW
**Impact**: HIGH
**Rating**: MITIGATE

**Description**: Symbolic compression may fail to capture unique value from a document, resulting in loss when original is archived.

**Mitigation**:
1. Always preserve full original in git history before compression
2. Read full document before creating symbolic compression
3. Verify compression captures essence with grep for key terms
4. Require human review of compressions before finalizing

**Residual Risk**: LOW (git history provides full recovery)

---

### RISK-002: Reference Breakage After Relocation
**Category**: Integrity
**Probability**: MEDIUM
**Impact**: MEDIUM
**Rating**: MITIGATE

**Description**: Internal markdown links (`[text](./file.md)`) may break when files are relocated.

**Mitigation**:
1. Before relocation, grep for references to file
2. Update all references as part of relocation
3. Run post-apply verification for broken links
4. Use canonical paths from repo root, not relative paths

**Residual Risk**: LOW (verification catches broken links)

---

### RISK-003: DIRECTIVE-043 Resolution Chooses Wrong Winner
**Category**: Governance
**Probability**: MEDIUM
**Impact**: MEDIUM
**Rating**: MITIGATE

**Description**: Principal may not have full context when choosing which 043A/043B is canonical, leading to wrong selection.

**Mitigation**:
1. Provide content summary of both versions to Principal
2. Show timestamps and authorship
3. Allow Principal to merge instead of choosing
4. Archive (not delete) the loser

**Residual Risk**: LOW (loser preserved in archive)

---

### RISK-004: Canon File Modification Without Full Review
**Category**: Constitutional Violation
**Probability**: LOW
**Impact**: HIGH
**Rating**: MITIGATE

**Description**: CANON-31150 file at root gets relocated without proper review, potentially corrupting canonical record.

**Mitigation**:
1. Flag all Canon operations as PROTECTED
2. Require explicit Principal approval
3. Verify content integrity after move (checksum)
4. Update any references to canonical path

**Residual Risk**: LOW (explicit approval required)

---

### RISK-005: System Prompts Merge Loses Active Prompt
**Category**: Operational Disruption
**Probability**: MEDIUM
**Impact**: MEDIUM
**Rating**: MITIGATE

**Description**: Merging system_prompts/ into 02-OPERATIONAL/prompts/ may overwrite or lose an actively-used prompt.

**Mitigation**:
1. Full audit of both directories before merge
2. Compare file-by-file for conflicts
3. Prefer newer version in conflicts (with Principal review)
4. Keep backup of system_prompts/ until verified

**Residual Risk**: LOW (audit before merge)

---

### RISK-006: Detritus Removal Deletes Needed File
**Category**: Data Loss
**Probability**: LOW
**Impact**: LOW
**Rating**: ACCEPT

**Description**: .DS_Store or .tmp files contain needed data (extremely unlikely).

**Mitigation**:
1. Only delete known detritus patterns
2. Verify nothing valuable in .tmp.driveupload/
3. Git commit before deletion allows recovery

**Residual Risk**: NEGLIGIBLE

---

### RISK-007: Apply Script Runs Prematurely
**Category**: Process Violation
**Probability**: LOW
**Impact**: MEDIUM
**Rating**: MITIGATE

**Description**: Script runs before Principal approval or before proper review.

**Mitigation**:
1. Script checks for APPLY_DEFRAG_APPROVAL.txt
2. Script aborts if approval file missing
3. Script requires specific content in approval file
4. All operations logged

**Residual Risk**: LOW (multiple gates)

---

### RISK-008: Oracle Context Merge Loses Thread State
**Category**: Continuity Loss
**Probability**: LOW
**Impact**: MEDIUM
**Rating**: MITIGATE

**Description**: Merging Oracle 12 files loses active session context.

**Mitigation**:
1. ORACLE13_CONTEXT.md is current—relocate, don't modify
2. Oracle 12 files only archived, not deleted
3. Verify ORACLE12_CONTEXT.md in oracle_contexts/ is primary before merging satellites

**Residual Risk**: LOW (relocate only)

---

### RISK-009: Defrag Creates New Orphans
**Category**: Regression
**Probability**: LOW
**Impact**: LOW
**Rating**: ACCEPT

**Description**: During defrag execution, new files created at wrong locations.

**Mitigation**:
1. Post-apply verification checks for new orphans
2. Defrag pass itself goes to OUTGOING/ (correct location)
3. Any new files created during defrag follow conventions

**Residual Risk**: LOW (verification catches)

---

### RISK-010: Concurrent Edit Conflict
**Category**: Process
**Probability**: LOW
**Impact**: MEDIUM
**Rating**: MITIGATE

**Description**: Another session modifies files during defrag apply.

**Mitigation**:
1. Defrag runs as single atomic operation
2. Git status checked before and after
3. If untracked changes appear, abort and review
4. Use git stash if needed

**Residual Risk**: LOW (git provides conflict detection)

---

## III. RISK SUMMARY

| Risk ID | Category | Rating | Mitigation Status |
|---------|----------|--------|-------------------|
| RISK-001 | Data Loss | MITIGATE | Git history preserves |
| RISK-002 | Integrity | MITIGATE | Reference update protocol |
| RISK-003 | Governance | MITIGATE | Principal decision with context |
| RISK-004 | Constitutional | MITIGATE | Explicit approval required |
| RISK-005 | Operational | MITIGATE | Full audit before merge |
| RISK-006 | Data Loss | ACCEPT | Known detritus only |
| RISK-007 | Process | MITIGATE | Approval file gate |
| RISK-008 | Continuity | MITIGATE | Relocate, don't modify |
| RISK-009 | Regression | ACCEPT | Post-apply verification |
| RISK-010 | Process | MITIGATE | Git conflict detection |

---

## IV. OVERALL RISK ASSESSMENT

**Aggregate Risk Level**: LOW-MEDIUM

**Confidence**: HIGH (all high-impact risks have mitigations)

**Recommendation**: PROCEED with defrag when Principal approves and APPLY is armed.

---

## V. STOP CONDITIONS

Abort defrag if any of these occur:

1. **Git status shows unexpected changes** during execution
2. **Reference grep finds >10 broken links** after relocation batch
3. **Checksum mismatch** on any Canon file move
4. **Principal revokes approval** mid-execution
5. **System_prompts audit reveals active dependencies** not in 02-OPERATIONAL

---

**Risk is manageable. Proceed with appropriate caution.**
