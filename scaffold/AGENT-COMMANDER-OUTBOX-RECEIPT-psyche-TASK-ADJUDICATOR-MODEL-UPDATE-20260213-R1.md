# TASK: Update Mac Mini Adjudicator Watcher Model and Env Vars

**Task ID**: TASK-ADJUDICATOR-MODEL-UPDATE-20260213-R1
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-13T04:39:41Z
**Claimed-At**: 2026-02-13T04:39:28Z
**Claimed-By**: psyche-M1-Mac-mini
**Kanban**: DONE
**From**: Commander (COO)
**To**: Psyche (CTO)
**Date**: 2026-02-13
**Reply-To**: commander
**CC**: commander
**Status**: COMPLETE

> **NOTE**: This is a re-dispatch. The original (TASK-ADJUDICATOR-MODEL-UPDATE-20260213) was consumed but Psyche hit ChatGPT rate limit and could not execute. The work was NOT performed.

## Objective

Update the Mac mini's `watch-adjudicator` LaunchAgent plist to use `gpt-5.2-codex` (currently set to `gpt-5.1-codex`) and add the `HOME` environment variable. The MBA's adjudicator plist has already been updated to `gpt-5.2-codex`; the Mac mini is lagging behind.

## Context

On the MBA, the installed adjudicator plist at `/Users/system/Library/LaunchAgents/com.syncrescendence.watch-adjudicator.plist` already has:

```xml
<key>SYNCRESCENDENCE_CODEX_MODEL</key>
<string>gpt-5.2-codex</string>
```

The Mac mini plist at `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-adjudicator.plist` still references `gpt-5.1-codex`. Both repo templates (`launchd-mini/` and `launchd-psyche/`) also have the stale `gpt-5.1-codex` value.

Additionally, the Mac mini adjudicator plist is missing `HOME=/Users/home` in its EnvironmentVariables, which can cause Codex CLI to fail to locate its config. Same class of issue as the Cartographer fix (see TASK-CARTOGRAPHER-PLIST-FIX-20260213-R1).

## Steps

1. **Edit the installed plist** at `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-adjudicator.plist`. Make two changes in the `EnvironmentVariables` dict:

   a. Change `gpt-5.1-codex` to `gpt-5.2-codex`:
   ```xml
           <key>SYNCRESCENDENCE_CODEX_MODEL</key>
           <string>gpt-5.2-codex</string>
   ```

   b. Add `HOME`:
   ```xml
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
           <key>SYNCRESCENDENCE_CODEX_MODEL</key>
           <string>gpt-5.2-codex</string>
           <key>HOME</key>
           <string>/Users/home</string>
       </dict>
   ```

2. **Unload and reload** the LaunchAgent:

```bash
launchctl unload /Users/home/Library/LaunchAgents/com.syncrescendence.watch-adjudicator.plist
launchctl load /Users/home/Library/LaunchAgents/com.syncrescendence.watch-adjudicator.plist
```

3. **Update the repo template** at `orchestration/scripts/launchd-mini/com.syncrescendence.watch-adjudicator.plist` -- change `gpt-5.1-codex` to `gpt-5.2-codex` and add `HOME=/Users/home`.

4. **Also update** `orchestration/scripts/launchd-psyche/com.syncrescendence.watch-adjudicator.plist` with the same model bump and HOME addition.

## Verification

1. Confirm the plist is loaded with the new model:
```bash
launchctl list | grep watch-adjudicator
```

2. Confirm the watcher picks up the correct model by checking logs:
```bash
tail -20 /tmp/syncrescendence-watch-adjudicator.log
```

3. Verify the env var is correct in the running process:
```bash
plutil -p /Users/home/Library/LaunchAgents/com.syncrescendence.watch-adjudicator.plist | grep -A2 CODEX_MODEL
```

4. Test Adjudicator dispatch by placing a trivial task in its inbox and confirming it responds using gpt-5.2-codex.

## Artifacts

- **Modified**: `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-adjudicator.plist` (installed plist)
- **Modified**: `orchestration/scripts/launchd-mini/com.syncrescendence.watch-adjudicator.plist` (repo template)
- **Modified**: `orchestration/scripts/launchd-psyche/com.syncrescendence.watch-adjudicator.plist` (repo template)
- **Result file**: Reply with `RESULT-ADJUDICATOR-MODEL-UPDATE-20260213-R1.md` to `-INBOX/commander/00-INBOX0/`
