# TASK: MacBook Air Cascade Configuration

**From**: Commander (Claude Code Opus 4.6)
**To**: Psyche (OpenClaw GPT-5.3)
**Reply-To**: commander
**CC**: commander
**Status**: COMPLETE
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-09T11:21:39Z
**Claimed-At**: 2026-02-09T11:21:25Z
**Claimed-By**: psyche-M1-Mac-mini
**Kanban**: DONE
**Issued**: 2026-02-09

## Objective

Take the Deployment Playbook (`00-ORCHESTRATION/DEPLOYMENT-PLAYBOOK.md`) and produce an MBA-specific adaptation. The MacBook Air is increasingly the primary surface for intellectual work — brain dumps with implementation directives — and needs a configuration that reflects this role.

## Key Differentials (Mac mini HQ vs MBA Field)

| Aspect | Mac mini (HQ) | MacBook Air (Field) |
|--------|--------------|-------------------|
| Display | 5120x1440 cockpit (4 lanes) | Native 13" (1 agent + 1 nvim) |
| Daemons | All 10+ services (KeepAlive: true) | Essential only |
| Power | Always-on | Battery-aware, launchd LowPriorityIO |
| Primary use | Cockpit (4-agent parallel) | Brain dumps + implementation directives |
| OpenClaw | Ajna (always-on gateway) | Psyche (on-demand, lighter footprint) |
| Vector DB | Chroma full vault index | Chroma subset (CANON + active sprint only) |

## Specific Requirements

1. **launchd plists for MBA**: Only essential watchers (commander, psyche, health check). Add ProcessType: Background and LowPriorityIO: true for battery preservation.
2. **tmux layout**: Single column (1 agent top + 1 nvim bottom) instead of 4-column cockpit. Adapt cockpit.sh for MBA dimensions.
3. **Git sync protocol**: MBA syncs to Mac mini via git push/pull. Document the workflow for: brain dump on MBA → push → agents on Mac mini execute → pull results.
4. **Chroma on MBA**: Index CANON + active sprint files only. Skip full ENGINE/SIGMA indexing to save battery/storage.
5. **Capability encoding**: Document everything YOU (Psyche) can do: AppleScript, launchctl, Homebrew, filesystem, Docker, Git, all CLI tools. You have full system access.

## Expected Output

Produce: `-OUTBOX/psyche/RESULT-MBA-CASCADE-20260209.md`

Include: MBA-specific playbook, adapted launchd plists, tmux layout, git sync workflow, and your own capability self-assessment.

## Context Files
- `00-ORCHESTRATION/DEPLOYMENT-PLAYBOOK.md` (source playbook)
- `-SOVEREIGN/SOVEREIGN-012-NARRATIVE_DNA_AND_AUTONOMY_EXPANSION.md` (Section 6: Cascade Architecture)
- `-SOVEREIGN/SOVEREIGN-TRAJECTORY.md` (Section 6: Cascade Architecture)
- `COCKPIT.md` (current cockpit spec)

**Reply-To**: commander
**CC**: commander
