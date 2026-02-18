# EXECUTION LOG: DIRECTIVE-[NNN][A|B]
## [Directive Title]

**Date**: YYYY-MM-DD
**Executor**: Claude Code [N] / Claude [Platform]
**Status**: COMPLETE | PARTIAL | BLOCKED
**Commit**: [hash]

---

## CONTEXT

[Brief context from directive—what was being executed and why]

---

## PHASES COMPLETED

### Phase N: [Phase Name]

**Before**: [State before action]
**Action**: [What was done]
**After**: [State after action]
**Files affected**: [Count or list]

---

## FILES CREATED/MODIFIED

| File | Action | Location |
|------|--------|----------|
| ... | Created/Modified/Moved | path |

---

## FILES DELETED

| Item | Type | Count | Reason |
|------|------|-------|--------|
| ... | Directory/File | N | [Rationale] |

---

## REPOSITORY HYGIENE CHECK

### Pre-Commit Verification
- [ ] `ls -la` at root - no orphans
- [ ] `tree -L 2` - structure correct
- [ ] Fresh-agent test - ≤2 decisions to any file

### Deferred Items
| Item | Reason | Target |
|------|--------|--------|
| [none or list] | ... | ... |

---

## METRICS

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| ... | ... | ... | ... |

---

## GIT COMMIT

```
[commit hash] [commit message]

[files changed summary]
```

---

*Execution log created YYYY-MM-DD*
*DIRECTIVE-[NNN] execution [complete/partial]*
