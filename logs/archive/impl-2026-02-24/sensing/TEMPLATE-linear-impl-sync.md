---
agent: commander
priority: P1
category: sensing
frequency: daily
schedule: "07:30"
launchd_agent: com.syncrescendence.sensing-linear-impl-sync
description: >
  Reconcile Linear SYN issues with IMPLEMENTATION-MAP.md entries.
  Detect status drift, unmapped issues, and stale links.
---

# SENSING: Linear <-> IMPL-MAP Sync

**From**: Scheduler (launchd/claudecron)
**To**: Commander (Claude Code Opus)
**Reply-To**: commander
**Kind**: TASK
**Priority**: P1
**Status**: PENDING
**Timeout**: 20
**CC**: —

---

## Objective

Synchronize Linear SYN team issue states with IMPLEMENTATION-MAP.md entries. Detect and report drift between the two systems. Do NOT auto-modify either system — produce a reconciliation report only.

### Step 1: Fetch Linear State

Query all SYN team issues (open and recently closed):

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: $LINEAR_API_KEY" \
  -d '{"query":"{ team(id:\"7b039eee-f9c3-4602-8813-0e1520eba386\") { issues(first:100) { nodes { identifier number title state { name type } priority updatedAt labels { nodes { name } } project { name } } } } }"}'
```

### Step 2: Parse IMPLEMENTATION-MAP.md

Read `IMPLEMENTATION-MAP.md` and extract all entries with `linear_id` or `linear:` references. Build a mapping of IMPL-ID -> SYN-XX -> status.

### Step 3: Reconciliation

Identify:

1. **Status Drift** — IMPL says `done` but Linear says `Todo`/`In Progress`, or vice versa
2. **Unmapped IMPL Entries** — IMPL entries with no Linear issue linked (count only, do not create)
3. **Orphan Linear Issues** — SYN issues with no corresponding IMPL entry
4. **Stale Issues** — Linear issues not updated in >14 days that are still `In Progress` or `Todo`
5. **Priority Mismatches** — IMPL priority vs Linear priority labels (P0-P3)

### Step 4: Report

## Expected Output

Write reconciliation report to `orchestration/state/DYN-LINEAR_IMPL_RECONCILIATION.md`:

```markdown
# Linear <-> IMPL Reconciliation Report
**Generated**: YYYY-MM-DD HH:MM
**Linear Issues**: N total (X open, Y done, Z canceled)
**IMPL Entries with Linear Links**: N/M

## Status Drift (Action Required)
| IMPL ID | SYN Issue | IMPL Status | Linear Status | Recommendation |
|---------|-----------|-------------|---------------|----------------|

## Stale Issues (>14 days no update)
| SYN Issue | Title | Status | Last Updated | Days Stale |
|-----------|-------|--------|-------------|------------|

## Unmapped IMPL Entries
- Count: N entries have no Linear issue linked
- (Full list available via `make linear-reconcile`)

## Orphan Linear Issues
| SYN Issue | Title | Notes |
|-----------|-------|-------|

## Summary
- Drift count: N
- Stale count: N
- Health: GOOD/DEGRADED/POOR
```

## Completion Protocol

1. Write report to `orchestration/state/DYN-LINEAR_IMPL_RECONCILIATION.md`
2. Update **Status** above from PENDING to COMPLETE
3. Commit: `git add -A && git commit -m "sensing: linear-impl sync YYYY-MM-DD"`
