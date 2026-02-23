# PRAC: Blitzkrieg Worktree Isolation

**Scope**: Git worktree parallelization for multi-agent Blitzkrieg execution
**Linear**: SYN-9 / IMPL-A-0005
**Status**: CANONICAL

---

## The Pattern

Git worktrees give each agent a separate working tree sharing the same `.git` history. No file locks, no race conditions, no coordination overhead.

```
TERM WorktreeBlitzkrieg:
sutra: "One worktree per lane, one agent per worktree—parallel without collision"
gloss: Blitzkrieg dispatches N agents simultaneously. Without isolation, they
       race on the same files. Worktrees eliminate this by giving each agent
       its own filesystem checkout from the same repository.
end
```

---

## Lane-to-Worktree Binding

| Lane | Agent | Role | Worktree | Branch |
|------|-------|------|----------|--------|
| A | Commander | COO | `syncrescendence-alpha` | `alpha/work` |
| B | Adjudicator | CQO | `syncrescendence-beta` | `beta/work` |
| C | Cartographer | CIO | `syncrescendence-gamma` | `gamma/work` |
| D | Psyche | CTO | `syncrescendence-delta` | `delta/work` |

Ajna (CSO) operates from MBA via git sync — not a local worktree.

---

## Zone Ownership

Each lane owns specific file domains to prevent merge conflicts:

| Lane | Primary Zone | Shared (read-only) |
|------|-------------|-------------------|
| A (Commander) | `orchestration/`, `CLAUDE.md`, ledgers | `canon/` (read) |
| B (Adjudicator) | `engine/` (quality), test scripts | `canon/` (read) |
| C (Cartographer) | `sources/research/`, `praxis/` | `canon/` (read) |
| D (Psyche) | `engine/` (automation), `.openclaw/` | `canon/` (read) |

**Rule**: `canon/` is write-protected during Blitzkrieg. Only the Commander (or Sovereign) merges CANON changes post-Blitzkrieg.

---

## Setup

### Prerequisites
- Git 2.30+ (worktree support)
- All agents have Claude Code / CLI access
- Current branch is clean (`git stash` if needed)

### Quick Start

```bash
# From repo root
bash orchestration/scripts/setup-worktrees.sh
```

This creates 3 worktrees (alpha/beta/gamma) alongside the main checkout. For 4-lane Blitzkrieg, add delta manually:

```bash
PARENT=$(dirname "$(git rev-parse --show-toplevel)")
git worktree add "$PARENT/syncrescendence-delta" -b delta/work
```

### Verify

```bash
git worktree list
# /Users/home/Desktop/syncrescendence               abc1234 [main]
# /Users/home/Desktop/syncrescendence-alpha          def5678 [alpha/work]
# /Users/home/Desktop/syncrescendence-beta           ghi9012 [beta/work]
# /Users/home/Desktop/syncrescendence-gamma          jkl3456 [gamma/work]
# /Users/home/Desktop/syncrescendence-delta          mno7890 [delta/work]
```

---

## Execution Workflow

### 1. Dispatch Phase
Sovereign assigns directives to lanes via dispatch.sh or direct instruction.

### 2. Parallel Execution
Each agent works in its worktree independently:
```bash
# Lane A (Commander)
cd ~/Desktop/syncrescendence-alpha
claude -p "Execute directive: ..."

# Lane B (Adjudicator)
cd ~/Desktop/syncrescendence-beta
codex exec "Execute directive: ..."
```

Or via cockpit tmux panes (each pane cds to its worktree).

### 3. Merge Phase
After all lanes complete:
```bash
# Commander merges from main worktree
cd ~/Desktop/syncrescendence
git merge alpha/work --no-ff -m "blitz: merge lane A — [summary]"
git merge beta/work --no-ff -m "blitz: merge lane B — [summary]"
git merge gamma/work --no-ff -m "blitz: merge lane C — [summary]"
git merge delta/work --no-ff -m "blitz: merge lane D — [summary]"
```

Resolve conflicts zone-by-zone. Zone ownership minimizes conflicts.

### 4. Cleanup
```bash
# Remove worktrees after merge
git worktree remove ../syncrescendence-alpha
git worktree remove ../syncrescendence-beta
git worktree remove ../syncrescendence-gamma
git worktree remove ../syncrescendence-delta

# Delete branches
git branch -d alpha/work beta/work gamma/work delta/work
```

---

## When to Use Worktrees vs Single-Tree

| Scenario | Approach |
|----------|----------|
| 2+ agents modifying different files simultaneously | Worktrees |
| Sequential agent handoff (one at a time) | Single tree + dispatch |
| Research-only agents (read, no write) | Single tree (read-safe) |
| Large refactoring across many files | Worktrees (isolation critical) |
| Quick fire-and-forget task | Single tree (overhead not worth it) |

---

## Anti-Patterns

1. **Two agents writing the same file in different worktrees** — zone ownership prevents this. If unavoidable, designate a merge resolver.
2. **Long-lived worktree branches** — merge frequently (every Blitzkrieg, not weekly). Divergence = merge pain.
3. **Worktrees without zone ownership** — random parallelism creates random conflicts. Always define zones first.
4. **Forgetting to cleanup** — orphan worktrees consume disk and create confusion. Always remove after merge.

---

## Integration with Neo-Blitzkrieg

This pattern is Phase 3 of the Neo-Blitzkrieg execution model:
1. **Phase 1**: Directive decomposition (Sovereign)
2. **Phase 2**: Lane assignment (dispatch.sh)
3. **Phase 3**: Worktree isolation (this pattern)
4. **Phase 4**: Parallel execution
5. **Phase 5**: Merge + verification

---

## Cross-References

- `orchestration/scripts/setup-worktrees.sh` — Setup script (70 lines)
- `sources/research/MECH-git_worktree_coordination.md` — Deep mechanics (zone ownership, coordination.yaml schema)
- `sources/research/PRAC-parallel_claude_orchestration.md` — Multi-instance patterns
- `engine/REF-ROSETTA_STONE.md` — Gap Analysis G5
