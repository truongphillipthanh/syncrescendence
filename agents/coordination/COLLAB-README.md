# Collaboration Directory — Multi-Agent Endeavors

## Purpose
Shared workspace for multi-agent projects (blitzkrieg lanes, research sprints, cross-agent builds).

## Anti-Proliferation Policy (STRICT)

1. **Max 3 active projects**. Archive or complete one before starting a 4th.
2. **Naming convention**: `YYYY-MM-slug` (e.g., `2026-02-repo-rearchitecture`)
3. **Ownership**: Every project MUST have an owner agent declared in `MANIFEST.md`
4. **TTL**: Projects without commits in 7 days get flagged. 14 days = auto-archive.
5. **Archival**: `git mv collab/<slug> collab/_archive/<slug>` with final status in MANIFEST.md
6. **No orphan files**: Every file must be referenced in MANIFEST.md or deleted

## Project Template

```
collab/<YYYY-MM-slug>/
├── MANIFEST.md         # Objective, lanes, agents, sync points, owner, status
├── findings.md         # Shared research/evidence
└── <deliverables>      # Per-agent artifacts
```

## MANIFEST.md Schema

```markdown
# <Project Title>
- **Owner**: <agent-name>
- **Status**: ACTIVE | COMPLETE | ARCHIVED | ABANDONED
- **Created**: <date>
- **Agents**: <comma-separated>
- **Objective**: <single clear statement>
- **Artifacts**: <list of files in this directory>
```
