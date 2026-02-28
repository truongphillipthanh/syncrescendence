# TASK-20260202-plumbing_hardening

**From**: Psyche (OpenClaw)
**To**: Commander (Claude Code / Ajna-cover integration lane)
**Issued**: 2026-02-02 11:02 PST
**Fingerprint**: 0817cd5
**Priority**: P0
**Status**: COMPLETE
**Timeout**: 60

---

## Objective

Harden the “connect the pipes” infrastructure so agreed architecture is actually enforced:
1) Fix lint + verify scripts so they reflect current repo structure.
2) Add a triage command for packet lifecycle observability.
3) Decide watcher persistence (launchd) and validate watcher handlers.

---

## Context

Psyche produced:
- OpenClaw patch directives: `/Users/system/.openclaw/workspace/PATCHLIST-FOR-COMMANDER.md`
- Running audit list: `/Users/system/.openclaw/workspace/AUDIT-RUNNING-LIST.md`

Repo evidence:
- Watchers are currently **not running** (no process; no launchd job).
- `ops_lint.sh` currently checks **0 files** due to stale assumptions (`engine/prompts/specs/registries` don’t exist; engine is flat).
- `verify_all.sh` permanently warns about root `.md` count (expects <=2, but root has `AGENTS.md`, `CLAUDE.md`, `COCKPIT.md`) and directory count prints 0.
- `verify_all.sh` currently reports 2 uncommitted changes: `.constellation/state/current.yaml` and `.obsidian/workspace.json`.

Important: Ajna token-constrained; Commander is covering integration lane.

---

## Tasks (ordered)

### Task A — Apply Patchlist (lint + verify + triage)
Follow `/Users/system/.openclaw/workspace/PATCHLIST-FOR-COMMANDER.md`.

Minimum required changes:
1. Patch `orchestration/scripts/ops_lint.sh` to lint flat `engine/PROMPT-*` and `engine/REF-*` (so it checks >0 files).
2. Patch `orchestration/scripts/verify_all.sh`:
   - allow 3 root `.md` files (AGENTS/CLAUDE/COCKPIT)
   - fix directory count computation (use find)
3. Add `orchestration/scripts/triage_outgoing.sh` (packet lifecycle spotter). Make executable.

Verification commands:
```bash
bash orchestration/scripts/verify_all.sh
bash orchestration/scripts/ops_lint.sh
bash orchestration/scripts/triage_outgoing.sh
```

### Task B — Watcher activation plan (design decision + validation)
We need always-on watchers, but validate handler correctness first.

1) Validate `watch_dispatch.sh` behavior for `commander` (it calls `claude --print "$(cat file)"`).
2) Validate `watch_dispatch.sh` behavior for `psyche|ajna` (it calls `openclaw process "$file"`) — confirm this is a valid OpenClaw CLI invocation on the target machine(s). If invalid, adjust handler to a working invocation.
3) Propose minimal `launchd` plists (or tmux fallback) for:
   - commander watcher on the commander machine
   - psyche watcher on the psyche machine
   - (optional) canon watcher (`watch_canon.sh`) on a single machine

### Task C — Decide policy for `.obsidian` + `.constellation` dirtiness
Pick one:
- (1) commit them (if shared truth)
- (2) ignore them (if local noise): update `.gitignore`

Provide recommendation + implement.

---

## Expected Output

1) Commit(s) that harden plumbing (lint+verify+triage + any ignore/commit decision).
2) A short RESULT note (can be in commit message body or `-OUTGOING/RESULT-commander-20260202-plumbing_hardening.md`) containing:
   - what changed
   - which watchers are now active and how they persist (launchd/tmux)
   - any open decisions left for Phillip

---

## Completion Protocol

- Update this file Status to COMPLETE.
- Ensure verification commands pass meaningfully (not “passes with 0 files checked”).
- `git add -A && git commit -m "chore: harden plumbing (lint+verify+triage)"`
