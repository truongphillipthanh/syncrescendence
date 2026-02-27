# SENSING: Corpus Staleness Audit

**From**: Scheduler (launchd/claudecron)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Kind**: SURVEY
**Priority**: P2
**Status**: PENDING
**Timeout**: 20
**CC**: commander

---

## Objective

Audit all dynamic (DYN-*) and reference (REF-*) files across the repository for staleness. A file is considered stale if its `last_updated` frontmatter field or git last-modified date exceeds 7 days.

### Scan Scope

#### Primary Targets (DYN-* files)
These are expected to change frequently. Staleness threshold: **7 days**.

```bash
find /Users/home/Desktop/syncrescendence -name 'DYN-*.md' -not -path '*archive*' -not -path '*node_modules*'
```

#### Secondary Targets (REF-* files)
These change less often but should still be reviewed. Staleness threshold: **30 days**.

```bash
find /Users/home/Desktop/syncrescendence -name 'REF-*.md' -not -path '*archive*' -not -path '*node_modules*'
```

#### Tertiary Targets (ARCH-* files)
Architecture docs. Staleness threshold: **60 days**.

```bash
find /Users/home/Desktop/syncrescendence -name 'ARCH-*.md' -not -path '*archive*' -not -path '*node_modules*'
```

### Staleness Detection Methods

1. **Frontmatter `last_updated`** — Parse YAML frontmatter for `last_updated` or `Last Updated` field
2. **Git log** — `git log -1 --format="%ai" -- <file>` for last commit date
3. **Use the more recent of the two** as the file's effective last-modified date

### Classification

| Freshness | Criteria |
|-----------|----------|
| FRESH | Modified within threshold |
| STALE | Exceeds threshold but < 2x threshold |
| CRITICAL | Exceeds 2x threshold |
| UNKNOWN | No date available |

## Expected Output

Write staleness report to `orchestration/state/DYN-CORPUS_STALENESS_REPORT.md`:

```markdown
# Corpus Staleness Report
**Generated**: YYYY-MM-DD HH:MM
**Files Scanned**: N

## Summary
- FRESH: N files
- STALE: N files
- CRITICAL: N files
- UNKNOWN: N files

## Critical Files (Immediate Attention)
| File | Last Modified | Days Stale | Category |
|------|--------------|------------|----------|

## Stale Files
| File | Last Modified | Days Stale | Category |
|------|--------------|------------|----------|

## Recommendations
- Files that should be scheduled for refresh
- Files that may be candidates for archival
- Patterns (e.g., "all DYN-PLATFORM* files are stale")
```

### Additional Checks

1. **Broken internal links** — Scan for `[[...]]` or relative markdown links that point to non-existent files
2. **Empty files** — Flag any DYN/REF/ARCH files with < 10 lines of content
3. **Duplicate coverage** — Note if multiple files cover the same topic

## Completion Protocol

1. Write report to `orchestration/state/DYN-CORPUS_STALENESS_REPORT.md`
2. Update **Status** above from PENDING to COMPLETE
3. Commit: `git add -A && git commit -m "sensing: corpus staleness audit YYYY-MM-DD"`
