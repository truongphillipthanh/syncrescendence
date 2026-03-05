# tmux Constellation Revival Stage 1

**Date**: 2026-03-02  
**Purpose**: revive the Mac mini constellation as a repo-driven execution surface without pretending full agent automation is already back

## What Is True Right Now

- The Mac mini is reachable over the declared neural bridge: `ssh mini`
- Remote binaries exist at Homebrew paths:
  - `/opt/homebrew/bin/tmux`
  - `/opt/homebrew/bin/openclaw`
  - `/opt/homebrew/bin/codex`
  - `/opt/homebrew/bin/gemini`
- OpenClaw exists on the Mac mini and still has a workspace under `/Users/home/.openclaw/workspace`
- The canonical repo checkout now exists at `/Users/home/syncrescendence`
- That canonical checkout now tracks `origin/main` via Homebrew `git`
- A legacy hidden repo path exists at `/Users/home/.syncrescendence`, but Apple-toolchain Git operations there are still blocked by the remote Xcode license gate

## Why Stage 1 Exists

The point is not to fully reactivate Psyche, Adjudicator, and Cartographer in one jump.

The point is to re-establish the Mac mini as a deterministic, repo-driven execution surface:

1. hydrate the repo onto the mini from the authoritative local checkout
2. deploy Psyche's repo-generated OpenClaw surface
3. create a reproducible `tmux` session skeleton called `constellation`
4. run explicit office inbox watchers in each agent window (`psyche`, `adjudicator`, `cartographer`) so dispatch files in `offices/<office>/inbox/pending/` trigger claim/wake behavior
5. keep `ops` as the manual control shell

This avoids two bad shortcuts:

- reviving tmux before repo truth is present on the mini
- relying on stale hidden-path state instead of the canonical repo checkout

## Collision Rule

The collision risk is real only when multiple LaunchAgents/scripts target the same tmux state without isolation.

- Same LaunchAgent `Label`: launchd treats this as one job namespace and later loads can override/rebind unexpectedly.
- Same tmux server/session/socket: competing scripts can kill/recreate each other's sessions.

Stage-1 now mitigates this by:

1. fixed label (`com.syncrescendence.constellation-stage1`) for one canonical job
2. dedicated tmux socket (`/tmp/tmux-syncrescendence-mini.sock`)
3. idempotent bootstrap behavior (existing session is kept unless `FORCE_REBUILD=1`)
4. lock directory guard to avoid concurrent bootstraps

## Stage 1 Commands

From the MacBook Air repo:

```bash
make bootstrap-mini
make revive-mini-constellation
make constellation-mini-status
```

Dispatch a wake file into an office inbox:

```bash
make dispatch-office-task OFFICE=psyche TITLE="runtime-check" PAYLOAD_FILE=/abs/path/payload.md
```

## What These Commands Do

### `make bootstrap-mini`

- renders configs for the `mac-mini` machine manifest
- rsyncs the repo to `/Users/home/syncrescendence` on the mini
- deploys `configs/psyche/AGENTS.md` to `/Users/home/.openclaw/workspace/AGENTS.md`

### `make revive-mini-constellation`

- runs the remote stage-1 tmux bootstrap script
- creates or recreates a detached `tmux` session named `constellation`
- creates windows for:
  - `psyche`
  - `adjudicator`
  - `cartographer`
  - `ops`
- `psyche`, `adjudicator`, and `cartographer` run `operators/runtime/office_inbox_watch.py` in restart loops
- watchers claim tasks from `inbox/pending` into `inbox/active` and emit receipts into `outbox/receipts`
- `ops` remains an interactive login shell for manual intervention

### `make install-mini-constellation-launchagent`

- installs `com.syncrescendence.constellation-stage1.plist` into the mini user's LaunchAgents directory
- bootstraps and kickstarts the job
- ensures the detached stage-1 `constellation` session can be reasserted on login without manual recreation

### `make constellation-mini-status`

- reports remote repo path presence
- reports tmux session presence
- lists windows if the session exists

## What Stage 1 Does Not Claim

- Psyche is not fully reanimated
- Slack/Discord dispatch is not validated end-to-end
- Ajna reset is not solved here
- no cron or always-on automation fabric is restarted
- no higher-order agent automation fabric is assumed

## Wake-on-Inbox Semantics

Wake is file-system dispatch:

1. place a task envelope into `offices/<office>/inbox/pending/`
2. office watcher claims it into `inbox/active/`
3. watcher emits a receipt into `outbox/receipts/`
4. pane logs become the immediate wake trace

This yields deterministic wake-on-dispatch without hidden background daemons.

Mini runtime note:

- use Homebrew Python for remote operator calls (`/opt/homebrew/bin/python3`) to avoid Apple toolchain/Xcode-license path issues on `/usr/bin/python3`.

Inspection note:

- stage1 uses tmux socket `/tmp/tmux-syncrescendence-mini.sock`
- inspect with:

```bash
tmux -S /tmp/tmux-syncrescendence-mini.sock list-windows -t constellation
```

## Git Note

The canonical checkout at `/Users/home/syncrescendence` is already Git-native and tracks `origin/main` through Homebrew `git`.

Apple's default developer-toolchain Git still triggers the Xcode license gate on this machine. If that Apple path must be used later, the required human action is:

```bash
sudo xcodebuild -license
```

That is no longer a blocker for the canonical repo path or for the stage-1 tmux surface.
