# TASK: Fix Mac Mini Cartographer Watcher Plist

**Task ID**: TASK-CARTOGRAPHER-PLIST-FIX-20260213-R1
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-13T04:39:27Z
**Claimed-At**: 2026-02-13T04:39:13Z
**Claimed-By**: psyche-M1-Mac-mini
**Kanban**: DONE
**From**: Commander (COO)
**To**: Psyche (CTO)
**Date**: 2026-02-13
**Reply-To**: commander
**CC**: commander
**Status**: COMPLETE

> **NOTE**: This is a re-dispatch. The original (TASK-CARTOGRAPHER-PLIST-FIX-20260213) was consumed but Psyche hit ChatGPT rate limit and could not execute. The work was NOT performed.

## Objective

Add missing environment variables to the Mac mini's `watch-cartographer` LaunchAgent plist. Without `SYNCRESCENDENCE_GEMINI_MODEL` and `HOME`, the Cartographer watcher either picks up wrong defaults or Gemini CLI cannot locate its config directory. This is the same class of fix already applied on the MBA.

## Context

On the MBA (MacBook Air), we fixed `com.syncrescendence.watch-cartographer.plist` by adding two keys to the `EnvironmentVariables` dict:

```xml
<key>SYNCRESCENDENCE_GEMINI_MODEL</key>
<string>gemini-2.5-pro</string>
<key>HOME</key>
<string>/Users/system</string>
```

The Mac mini plist at `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-cartographer.plist` currently only has `PATH` and `NODE_NO_WARNINGS` in its EnvironmentVariables dict -- it is missing both `SYNCRESCENDENCE_GEMINI_MODEL` and `HOME`.

The repo template at `orchestration/scripts/launchd-mini/com.syncrescendence.watch-cartographer.plist` has the same gap.

Additionally, we created `.gemini/commands/initialize.md` in the repo, which gives Cartographer a `/initialize` slash command for session orientation. Once git-sync propagates the latest push to the Mac mini, this file should be in place automatically.

## Steps

1. **Edit the installed plist** at `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-cartographer.plist`. Add two keys inside the existing `<dict>` under `EnvironmentVariables`:

```xml
        <key>SYNCRESCENDENCE_GEMINI_MODEL</key>
        <string>gemini-2.5-pro</string>
        <key>HOME</key>
        <string>/Users/home</string>
```

The resulting EnvironmentVariables block should look like:

```xml
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
        <key>NODE_NO_WARNINGS</key>
        <string>1</string>
        <key>SYNCRESCENDENCE_GEMINI_MODEL</key>
        <string>gemini-2.5-pro</string>
        <key>HOME</key>
        <string>/Users/home</string>
    </dict>
```

2. **Unload and reload** the LaunchAgent:

```bash
launchctl unload /Users/home/Library/LaunchAgents/com.syncrescendence.watch-cartographer.plist
launchctl load /Users/home/Library/LaunchAgents/com.syncrescendence.watch-cartographer.plist
```

3. **Update the repo template** at `orchestration/scripts/launchd-mini/com.syncrescendence.watch-cartographer.plist` with the same env var additions, so future installs are correct.

4. **Also update** `orchestration/scripts/launchd-psyche/com.syncrescendence.watch-cartographer.plist` with the same changes (this template currently has `/Users/system` paths which is wrong for Mac mini -- it should use `/Users/home`).

5. **Verify git-sync** has propagated `.gemini/commands/initialize.md` to the Mac mini repo:

```bash
ls -la /Users/home/Desktop/syncrescendence/.gemini/commands/initialize.md
```

## Verification

1. Confirm the plist is loaded:
```bash
launchctl list | grep watch-cartographer
```

2. Confirm env vars are visible in the watcher process:
```bash
tail -20 /tmp/syncrescendence-watch-cartographer.log
```

3. Confirm the `/initialize` command file exists on Mac mini:
```bash
cat /Users/home/Desktop/syncrescendence/.gemini/commands/initialize.md | head -5
```

4. Test Cartographer dispatch by placing a trivial task in its inbox and confirming it picks it up with the correct model.

## Artifacts

- **Modified**: `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-cartographer.plist` (installed plist)
- **Modified**: `orchestration/scripts/launchd-mini/com.syncrescendence.watch-cartographer.plist` (repo template)
- **Modified**: `orchestration/scripts/launchd-psyche/com.syncrescendence.watch-cartographer.plist` (repo template)
- **Verified**: `.gemini/commands/initialize.md` present on Mac mini via git-sync
- **Result file**: Reply with `RESULT-CARTOGRAPHER-PLIST-FIX-20260213-R1.md` to `-INBOX/commander/00-INBOX0/`
