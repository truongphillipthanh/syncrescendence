# Endeavor: Ajna ↔ Psyche OpenClaw Outfitment Synchronization

**Date started:** 2026-02-05

## Objective (what we’re establishing)
Create a *reinstall-proof* procedure to ensure the two always-on OpenClaw nodes:
- **Ajna** (Mac mini, user `home`, always-on home base)
- **Psyche** (MacBook Air, user `system`, portable interface)

…share the **same capability surface** (skills + plugin scaffolding), while retaining **role differences** and keeping **secrets local**.

Concretely, we want three guarantees:
1) **Outfitment parity:** Ajna has the same `~/.openclaw/workspace/skills/` payload as Psyche (supermemory, hindsight, etc.).
2) **Provider parity:** Ajna runs `openai-codex` via OAuth (`openai-codex:default`) and can execute agent turns.
3) **Receipt piping:** when Psyche dispatches tasks to Ajna, Ajna’s receipts/results can be automatically delivered into Psyche’s inbox (no manual hunting).

## Constraints
- **Do not copy secrets via git**: no API keys, no Slack tokens, no gateway tokens.
- Prefer **renames over deletions** when disabling duplicate plugin copies.
- Use **repo as blueprint**; treat local OpenClaw dirs as install surfaces.

## Current architecture surfaces
### Repo (ground truth)
- Dispatch/task mailboxes:
  - `-INBOX/<agent>/TASK-*.md`
  - `-OUTGOING/RESULT-*.md`
- Watcher runtime:
  - `00-ORCHESTRATION/scripts/watch_dispatch.sh`
  - launchd plists:
    - `00-ORCHESTRATION/scripts/launchd-mini/` (hardcoded `/Users/home/...`)
    - `00-ORCHESTRATION/scripts/launchd-psyche/` (hardcoded `/Users/system/...`)

### OpenClaw local surfaces (per host)
- Config: `~/.openclaw/openclaw.json`
- OAuth creds dir: `~/.openclaw/credentials`
- Workspace skills (the thing we mirror): `~/.openclaw/workspace/skills/`

## What we did (sequence)
### 1) Define sync policy
- Doc: `00-ORCHESTRATION/state/impl/tooling/OUTFITMENT-SYNC.md`

### 2) Implement “skill payload mirror” (no secrets)
- Script: `00-ORCHESTRATION/scripts/sync_openclaw_skills.sh`
- Uses SSH + rsync allowlist; excludes `node_modules/` and `dist/`.

### 3) Establish SSH trust + auth for Ajna → Psyche
- Ajna generated a dedicated keypair for the link:
  - comment: `ajna->psyche`
  - fingerprint: `SHA256:XJeE+B/803pJG/rwsfSUm3eHxI9oSrePBVDwYbtCc64`
- Psyche authorized it:
  - `/Users/system/.ssh/authorized_keys` contains the `ajna->psyche` public key.
- Ajna confirmed `ssh psyche "echo OK_PSY"` works.

### 4) Run outfitment sync on Ajna
Receipt: `-OUTGOING/RESULT-ajna-20260205-outfitment_sync_and_smoketest_v3.md`
- Synced skills include:
  - `supermemory` (~373M)
  - `hindsight` (~321M)
  - plus smaller skills (prompt-guard, qmd-skill, etc.)

### 5) Fix Ajna OAuth + plugin load issues after sync
From the v3 receipt:
- `openclaw doctor` initially reported:
  - CRITICAL: missing `~/.openclaw/credentials`
  - ERROR: `hindsight-openclaw` missing `dist/index.js`
- Ajna created credentials dir and ran the hindsight integration `install.sh` to build/deploy.
- After fix: plugins errors resolved; a WARN remained about duplicate plugin id (`hindsight-openclaw`) because it existed both as workspace path and as deployed extension.

### 6) Establish receipt piping
- Added `**CC**:` header field in `dispatch.sh` and parsing in `watch_dispatch.sh`.
- For CC targets, watcher copies receipts; and can also **scp** receipts to the CC host (best-effort) when SSH alias exists.
- Proven artifact landing in Psyche inbox:
  - `-INBOX/psyche/RESULT-ajna-20260205-cc_pipe_test2.md` (contains `CC_PIPE_TEST2_OK`)

## Verification checklist (reinstall-proof)
Run on Ajna after any reinstall:
1) `openclaw --version`
2) `openclaw doctor --fix --non-interactive`
   - ensure `~/.openclaw/credentials` exists
3) `bash 00-ORCHESTRATION/scripts/sync_openclaw_skills.sh --pull --from psyche --persona ajna`
4) `du -sh ~/.openclaw/workspace/skills/* | sort -h | tail`
5) `openclaw gateway status`
6) `openclaw agent --agent main --message "Reply EXACTLY: SYNC_OK" --timeout 180`
7) Dispatch CC proof:
   - `bash 00-ORCHESTRATION/scripts/dispatch.sh ajna "CC_PIPE_PROOF" "Reply EXACTLY: CC_PIPE_OK" "psyche"`
   - confirm receipt appears in `-INBOX/psyche/`

## Known sharp edges / follow-ups
- **Duplicate plugin id (hindsight-openclaw)**: decide canonical load path (prefer extension deploy) and disable the other copy via rename.
- **Watcher receipts**: some runs relied on manual scp backstop; automated CC scp should be re-verified once `watch_dispatch.sh` updates are fully deployed and stable.
- **Stash hygiene**: Ajna used `git stash` multiple times to pull; define policy for always-on node.
