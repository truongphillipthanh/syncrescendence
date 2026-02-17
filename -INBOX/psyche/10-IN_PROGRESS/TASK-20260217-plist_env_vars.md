# TASK: Option B — Add Neural Bridge env vars to supervisor plist

**Status**: IN_PROGRESS
**Priority**: P0
**Claimed-At**: 2026-02-17T06:46:08Z
**Claimed-By**: psyche-M1-Mac-mini
**Kanban**: IN_PROGRESS
**Reply-To**: commander
**CC**: commander
**To**: psyche
**Timeout**: 300

## Context

Option A (eval in supervisor.sh) FAILED — env vars did not propagate to child processes despite code being correct. Reason unclear. Falling back to Option B: inject vars directly into the launchd plist.

plist EnvironmentVariables are injected BY LAUNCHD into the process environment BEFORE the script runs. This is the most reliable mechanism.

## Step 1: Edit the plist

Edit `~/Library/LaunchAgents/com.syncrescendence.auto-ingest-supervisor.plist`. 

In the existing `<dict>` under `<key>EnvironmentVariables</key>`, ADD these 5 keys after the existing HOME entry:

```xml
<key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA</key>
<string>macbook-air</string>
<key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER</key>
<string>local</string>
<key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR</key>
<string>local</string>
<key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER</key>
<string>local</string>
<key>SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE</key>
<string>local</string>
```

## Step 2: ALSO add to watchdog plist

Check if `~/Library/LaunchAgents/com.syncrescendence.watchdog.plist` exists. If it does, add the same 5 env vars there too (the watchdog also needs them for the SSH health check).

## Step 3: Reload

```bash
# Unload and reload supervisor
launchctl bootout "gui/$(id -u)/com.syncrescendence.auto-ingest-supervisor" 2>/dev/null || true
sleep 2
launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/com.syncrescendence.auto-ingest-supervisor.plist
sleep 10
```

## Step 4: Verify (THE ONLY CHECK THAT MATTERS)

```bash
LOOP_PID=$(pgrep -f 'auto_ingest_loop.sh' | head -1)
echo "LOOP_PID=$LOOP_PID"
ps eww -p $LOOP_PID | tr ' ' '\n' | grep SYNCRESCENDENCE_REMOTE
```

Expected output MUST include exactly:
```
SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA=macbook-air
SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER=local
SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR=local
SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER=local
SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE=local
```

If these 5 lines appear in ps eww output: PASS. Commit.
If they do NOT appear: FAIL. Do not claim success.

## Step 5: Commit (only if Step 4 PASSES)

```bash
cd ~/Desktop/syncrescendence
git add -A && git commit -m 'fix(bridge): plist EnvironmentVariables for Neural Bridge SCP routing (Option B)'
```

**Reply-To**: commander
**CC**: commander
