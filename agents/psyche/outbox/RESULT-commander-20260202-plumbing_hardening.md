# RESULT: Plumbing Hardening (TASK-20260202)

**From**: Commander (Claude Code Opus)
**To**: Psyche / Sovereign
**Completed**: 2026-02-02
**Fingerprint**: (pending commit)

---

## Task A — Patches Applied

### 1. `ops_lint.sh` — FIXED
- Replaced stale subdirectory scans (`prompts/`, `specs/`, `registries/`) with flat `engine/` scans
- Now checks `PROMPT-*.md` and `REF-*.md` at `engine/` root
- **Result**: 20 files checked (was 0). 8 pass, 12 fail on missing frontmatter.
- **Frontmatter debt**: 10 REF files + 2 PROMPT files lack `id/kind/scope/target` YAML frontmatter. This is pre-existing debt — the convention was never enforced. Flagged as backlog; does not block plumbing.

### 2. `verify_all.sh` — FIXED
- Root `.md` threshold: `<=2` → `<=3` (AGENTS.md, CLAUDE.md, COCKPIT.md)
- Directory count: `ls -d */` → `find . -maxdepth 1 -type d` (excludes hidden dirs)
- **Result**: All checks pass. Directory count correctly shows 8. No false warnings.

### 3. `triage_outgoing.sh` — CREATED
- Scans `-INBOX/` for PENDING/IN_PROGRESS tasks
- Scans `-OUTGOING/` for PENDING prompts
- Scans `-SOVEREIGN/` for PENDING briefs (excludes README.md)
- Falls back to grep if rg unavailable
- **Result**: Correctly surfaces 1 pending task + 3 pending SOVEREIGN briefs.

### 4. Makefile targets — ADDED
- `make verify-full` → runs `verify_all.sh`
- `make lint` → runs `ops_lint.sh`
- `make triage` → runs `triage_outgoing.sh`

---

## Task B — Watcher Validation + Persistence

### Handler Validation

| Agent | Old Invocation | Issue | Fixed Invocation |
|-------|---------------|-------|------------------|
| commander | `claude --print "$(cat)"` | Works but `--print` is long form | `claude -p "$content"` |
| adjudicator | `codex "$(cat)"` | Correct | Unchanged |
| cartographer | `gemini "$(cat)"` | Correct | Unchanged |
| psyche/ajna | `openclaw process "$file"` | **INVALID** — `process` not a valid OpenClaw command | `openclaw agent --local -m "$content"` |

### Persistence: launchd Plists Created

Four plist templates in `orchestration/scripts/launchd/`:

| Plist | Agent | Machine |
|-------|-------|---------|
| `com.syncrescendence.watch-commander.plist` | Commander | Primary (this machine) |
| `com.syncrescendence.watch-ajna.plist` | Ajna | M1 Mac mini |
| `com.syncrescendence.watch-psyche.plist` | Psyche | M4 MacBook Air |
| `com.syncrescendence.watch-canon.plist` | CANON regen | Any single machine |

### Activation (Sovereign action required)

To install on this machine:
```bash
cp orchestration/scripts/launchd/com.syncrescendence.watch-commander.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.syncrescendence.watch-commander.plist
```

To install Ajna watcher on M1 Mac mini:
```bash
cp orchestration/scripts/launchd/com.syncrescendence.watch-ajna.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist
```

**Note**: Plists assume repo at `~/Desktop/syncrescendence`. Adjust `WorkingDirectory` and `ProgramArguments` paths if repo location differs per machine.

**Watchers are NOT yet active** — plists are committed but not installed. Sovereign decides when to activate.

---

## Task C — .obsidian + .constellation Policy

**Decision** (implemented in Blitzkrieg 51, prior to this task):

| Path | Policy | Rationale |
|------|--------|-----------|
| `.obsidian/workspace.json` | **IGNORE** (`.gitignore`) | Local editor state. Changes on every Obsidian interaction. Not shared truth. |
| `.constellation/state/current.yaml` | **COMMIT** (shared truth) | Tracks latest fingerprint/commit. Used by all platforms for state verification. Auto-updated by hooks. |

This eliminates the permanent "2 uncommitted changes" noise from `verify_all.sh`.

---

## Open Decisions for Sovereign

1. **Frontmatter debt**: 12 files in `engine/` lack YAML frontmatter. Add frontmatter to enforce lint, or exempt REF files from the requirement?
2. **Watcher activation timing**: Install launchd plists now, or wait for full pipeline validation?
3. **OpenClaw memory_search**: Embeddings API key broken (401). Treat repo as recall mechanism until fixed?
4. **Gemini CLI API key**: Still needed for Cartographer lane (SOVEREIGN-pending since Oracle 13).

---

## Verification Commands

```bash
make verify-full   # Structure + ledger + content + git
make lint          # engine frontmatter enforcement (20 files, 12 debt)
make triage        # Packet lifecycle across all pipes
```
