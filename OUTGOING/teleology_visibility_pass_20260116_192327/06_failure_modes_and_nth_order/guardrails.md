# Guardrails: Hard Rules Preventing Crashout
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: Inviolable rules that prevent catastrophic system failures

---

## Overview

These guardrails are absolute. They prevent the class of failures from which recovery is difficult or impossible. Violation should trigger immediate stop and escalation.

---

## Guardrail 1: Repository is Ground Truth

**Rule**: The repository is always authoritative. No platform memory, cache, or state supersedes repo state.

**Implementation**:
- When platform claims conflict with repo, trust repo
- Memory/cache treated as performance optimization, not source of truth
- "I remember" must be verified against repo before action

**Violation Detection**:
- Action taken based on memory claim without repo verification
- Platform state used as authority for decisions
- Chat history treated as documentation

**Consequence of Violation**: Drift between actual state and believed state; compounding errors

---

## Guardrail 2: Protected Zones Require Approval

**Rule**: Modifications to protected zones require explicit Principal approval.

**Protected Zones**:
- `01-CANON/` — Canonical knowledge
- `00-ORCHESTRATION/oracle_contexts/` — Oracle session history
- `00-ORCHESTRATION/state/` — Living infrastructure
- `CLAUDE.md` — Constitutional rules
- `config/coordination.yaml` — Platform coordination

**Implementation**:
- CLAUDE.md constitutional rules enforce this
- Execution packets reference approval
- Git commits cite approval source

**Violation Detection**:
- Modification without approval record
- Bulk changes without review
- Automated modifications without human gate

**Consequence of Violation**: Uncontrolled Canon drift; constitutional corruption

---

## Guardrail 3: Verification Before Completion

**Rule**: Never claim completion without verification commands passing.

**Implementation**:
- Every execution ends with verification step
- "Done" requires artifact existence check
- Ledger updates require state validation

**Violation Detection**:
- Execution log lacks verification output
- tasks.csv marked DONE but artifact missing
- "I completed..." without evidence

**Consequence of Violation**: False completion accumulates; system believes work done that isn't

---

## Guardrail 4: Atomic Ledger Updates

**Rule**: Ledger updates must use atomic temp-file-then-rename pattern.

**Implementation**:
```yaml
ledger_protocol:
  backup_before_write: true
  temp_file_pattern: "{name}.csv.tmp"
  backup_pattern: "{name}.csv.bak.{timestamp}"
  validation_required: true
  atomic_rename: true
```

**Violation Detection**:
- Direct write to CSV without backup
- No validation of temp file
- Concurrent writes detected

**Consequence of Violation**: Corrupted ledgers; data loss; conflicting states

---

## Guardrail 5: No Direct Inter-Instance Communication

**Rule**: Claude Code instances NEVER communicate directly. All coordination through repository.

**Implementation**:
- No shared memory between instances
- Git branches for isolation
- Blackboard packets for inter-instance data

**Violation Detection**:
- Instance references action by other instance not in repo
- State assumptions without repo verification
- "The other instance said..."

**Consequence of Violation**: Race conditions; conflicting modifications; corrupted state

---

## Guardrail 6: Secrets Never in Repository

**Rule**: API keys, credentials, tokens NEVER committed to repository.

**Implementation**:
- Environment variables for secrets
- .gitignore for sensitive files
- No credentials in code, comments, or documentation

**Violation Detection**:
- Secret string patterns in git diff
- Hardcoded credentials in code
- Secrets in commit messages

**Consequence of Violation**: Credential exposure; security breach; financial loss

---

## Guardrail 7: Role Separation Enforced

**Rule**: Platforms operate within assigned roles. No role boundary crossing.

**Role Assignments**:
| Role | Platform | Boundary |
|------|----------|----------|
| Oracle (sensing) | Gemini | Observe only, never execute |
| Deviser (planning) | ChatGPT | Plan only, never execute |
| Executor (action) | Claude Code | Execute plans, never redefine scope |
| Auditor (verify) | ChatGPT | Verify only, never modify |

**Violation Detection**:
- Web platform attempts file modification
- Executor redefines objectives mid-task
- Auditor makes changes during audit

**Consequence of Violation**: Role confusion; unverified actions; scope creep

---

## Guardrail 8: Flat Directory Principle

**Rule**: No subdirectories within top-level directories. Use prefixes instead.

**Implementation**:
- ARCH-, DYN-, REF-, SCAFF- prefixes
- Flat file structure
- Maximum depth = 2 (root/directory/file)

**Violation Detection**:
- find . -mindepth 3 -type d returns results
- mkdir creates nested structure
- Subdirectory proposed in plan

**Consequence of Violation**: Navigation complexity; principle erosion; inconsistent structure

---

## Guardrail 9: Commit Discipline

**Rule**: Frequent commits with semantic prefixes; never go dark for extended periods.

**Implementation**:
```yaml
commit_format:
  pattern: "{type}({scope}): {description}"
  types: [feat, fix, docs, chore, refactor, test]
```

**Violation Detection**:
- >50 files changed in single commit
- Commit message lacks prefix
- Work session without commits

**Consequence of Violation**: Lost granularity; difficult rollback; unclear history

---

## Guardrail 10: Principal in the Loop for Irreversible Actions

**Rule**: Any action that cannot be easily undone requires Principal approval.

**Irreversible Actions**:
- Canon deletion (protected zone)
- Account configuration changes
- External publication
- Credential rotation
- Major architectural changes

**Implementation**:
- Plan packet specifies irreversibility
- Explicit approval in chat before action
- Event log records approval

**Violation Detection**:
- Irreversible action without approval record
- "I'll just..." for major changes
- Assumed consent

**Consequence of Violation**: Unrecoverable state; trust erosion; data loss

---

## Enforcement Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                     GUARDRAIL PRIORITY                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Level 1 (ABSOLUTE): Violations must halt immediately          │
│    - G6: Secrets in repo                                        │
│    - G10: Irreversible without approval                         │
│                                                                 │
│  Level 2 (CRITICAL): Violations require immediate correction   │
│    - G1: Repository ground truth                                │
│    - G2: Protected zones                                        │
│    - G4: Atomic ledger updates                                  │
│                                                                 │
│  Level 3 (IMPORTANT): Violations should be corrected soon      │
│    - G3: Verification before completion                         │
│    - G5: No direct inter-instance communication                 │
│    - G7: Role separation                                        │
│                                                                 │
│  Level 4 (STANDARD): Violations noted for future correction    │
│    - G8: Flat directory principle                               │
│    - G9: Commit discipline                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Guardrail Verification Commands

```bash
# G2: Check protected zone modifications
git diff --name-only HEAD~10 | grep -E '^(01-CANON/|00-ORCHESTRATION/state/|CLAUDE.md)'

# G4: Check for ledger backups
ls 00-ORCHESTRATION/state/*.bak.* 2>/dev/null | wc -l

# G6: Check for potential secrets
git grep -E '(api_key|secret|password|token).*=' --cached

# G8: Check for nested directories
find . -mindepth 3 -type d -not -path './.git/*' -not -path './OUTGOING/*'

# G9: Check recent commit patterns
git log --oneline -20 | grep -v -E '^[a-f0-9]+ (feat|fix|docs|chore|refactor|test)\('
```
