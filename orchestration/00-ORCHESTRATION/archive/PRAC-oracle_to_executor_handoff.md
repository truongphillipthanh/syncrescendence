> **ARCHIVED**: 2026-02-23 | Reason: ORPHANED — referenced scripts/paths no longer exist
> **Origin**: praxis/05-SIGMA/practice/
> **Archived by**: Commander (DC-205 Phase 2C decruft)

# PRAC: Oracle-to-Executor Handoff

**Scope**: Handoff document creation, timing, template, verification

---

## The Problem

Web app (Oracle) holds strategic context across 11+ conversation threads. CLI (Executor) cannot see this. When session ends, context dies. Rate limits force account switches. Context must survive.

**Solution**: Structured handoff documents committed to repository.

---

## When to Create Handoff

- Before context window approaches limit (70%)
- Before rate limit forces session end
- At natural strategic breakpoints
- Before switching accounts
- End of work session (daily minimum)

**Don't wait for forced stop**—proactive handoff preserves more context.

---

## Handoff Document Template

```markdown
# Oracle Handoff: [Session ID or Date]
Generated: [timestamp]
Source Threads: [conversation IDs if applicable]
Oracle: [Account/Platform used]

## Corpus State Snapshot
- Canonical documents: [count]
- Processing queue: [count by state]
- Recent taxonomy decisions: [last 3]
- Active issues: [list]

## Accumulated Strategic Insights
[Compress 10,000+ tokens of conversation into ~2000]

Key learnings from this session:
1. [Insight with rationale]
2. [Insight with rationale]
3. [Insight with rationale]

Validated patterns:
- [Pattern that worked]
- [Pattern that failed]

## Active Directives
- [Directive 1]: [brief rationale]
- [Directive 2]: [brief rationale]

## Decisions Made
| Decision | Options Considered | Rationale |
|----------|-------------------|-----------|
| [Choice] | [A, B, C] | [Why this one] |

## Constraints Discovered
- [Constraint]: [Why it matters]
- [Constraint]: [Why it matters]

## Continuation Vector
[Specific next step for Executor]

Priority: [1-3]
Scope: [Files/areas to touch]
Guard rails: [What NOT to do]

## Files Modified This Session
- [file1]: [change description]
- [file2]: [change description]
```

---

## Storage Location

```
orchestration/
└── oracle_contexts/
    └── handoffs/
        ├── HANDOFF-20260125-oracle11.md
        ├── HANDOFF-20260124-oracle10.md
        └── ...
```

Or project-specific:
```
.claude/
└── context/
    └── handoffs/
```

---

## Compression Technique

Oracle conversations are verbose. Compress by extracting:

| Keep | Discard |
|------|---------|
| Decisions | Discussion leading to decision |
| Constraints | Reasoning about constraints |
| Patterns | Examples of patterns |
| Next steps | Abandoned approaches |
| Files changed | Exploration before changes |

**Target**: ~2000 tokens from 10,000+ raw conversation.

---

## Executor Ingestion

```markdown
# In CLAUDE.md or start of session

@orchestration/oracle_contexts/handoffs/HANDOFF-20260125-oracle11.md

Continue from the Continuation Vector above.
```

Executor has equivalent strategic context without full conversation history.

---

## Verification Before Commit

Before ending Oracle session:

```bash
# Check handoff document exists
ls orchestration/oracle_contexts/handoffs/HANDOFF-*.md

# Verify committed
git status

# If uncommitted
git add orchestration/oracle_contexts/handoffs/
git commit -m "docs: Oracle handoff $(date +%Y%m%d)"
git push
```

**Don't close session until handoff is pushed**—context dies with session.

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Waiting too long | Forced stop loses context | Proactive at 70% |
| Too verbose | Token budget for Executor | Compress to 2000 tokens |
| No continuation vector | Executor doesn't know priority | Always include next step |
| Not committed | Session ends, file lost | Push before closing |
| No file list | Executor unaware of changes | List all touched files |

---

## Quick Reference

1. **Create** handoff document from template
2. **Compress** insights to ~2000 tokens
3. **Include** continuation vector with priority
4. **Commit** to repository
5. **Push** before session ends
6. **Verify** Executor can load via @import

---

## Cross-References

- [[SYNTHESIS-cross_platform_patterns]] → Oracle-Executor architecture
- [[MECH-git_worktree_coordination]] → Repository structure
- [[PRAC-ledger_management_patterns]] → State tracking
