# TASK: Fix launchd environment propagation for Neural Bridge

**Status**: IN_PROGRESS
**Priority**: P0
**Claimed-At**: 2026-02-17T06:36:51Z
**Claimed-By**: psyche-M1-Mac-mini
**Kanban**: IN_PROGRESS
**Reply-To**: commander
**CC**: commander
**To**: psyche
**Timeout**: 600

## Context

Adjudicator adversarial audit FAILED the Neural Bridge. Critical finding:

**The CONFIRM SCP-back code in auto_ingest_loop.sh is DEAD under launchd context.**

Why: auto_ingest_supervisor.sh spawns auto_ingest_loop.sh processes. The supervisor runs under launchd via `com.syncrescendence.auto-ingest-supervisor.plist`. launchd does NOT source ~/.zshrc. Therefore, `SYNCRESCENDENCE_REMOTE_AGENT_HOST_*` env vars are EMPTY in all auto_ingest_loop.sh processes. The SCP-back code checks these vars → finds nothing → never fires.

This is not a code bug. It's an environment propagation failure. We've fixed .zshrc THREE TIMES and it keeps "not working" because launchd never reads .zshrc.

## Objective

Fix the environment propagation so that ALL auto_ingest_loop.sh processes have the Neural Bridge env vars, regardless of how they're launched.

## Required Fix (choose ONE approach — recommend Option A)

### Option A: Source env in auto_ingest_supervisor.sh (RECOMMENDED)
Add to the TOP of `00-ORCHESTRATION/scripts/auto_ingest_supervisor.sh`, before spawning loops:

```bash
# Neural Bridge: load cross-machine dispatch env vars
# launchd does NOT source ~/.zshrc — we must load explicitly
if [ -f "${HOME}/.zshrc" ]; then
    # Extract only SYNCRESCENDENCE_REMOTE_AGENT_HOST_* vars (safe partial source)
    eval "$(grep '^export SYNCRESCENDENCE_REMOTE_AGENT_HOST_' "${HOME}/.zshrc")"
fi
```

### Option B: Add env vars to supervisor plist
Add to `~/Library/LaunchAgents/com.syncrescendence.auto-ingest-supervisor.plist` inside `<dict>` under EnvironmentVariables:

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

## ALSO FIX: Secondary issues from Adjudicator audit

1. **authorized_keys malformed line**: Remove the stray `psyche->ajna` text line from `~/.ssh/authorized_keys` (keep only valid ssh- key lines and # comments)
2. **ARCH-NEURAL_BRIDGE.md status**: Change OPERATIONAL to "OPERATIONAL (launchd env pending validation)" — OR change it to OPERATIONAL after you verify the fix works

## Required Verification (ALL MUST PASS)

After applying the fix, you MUST restart the supervisor and verify the env vars propagate:

```bash
# 1. Restart supervisor to pick up changes
launchctl kickstart -k "gui/$(id -u)/com.syncrescendence.auto-ingest-supervisor"

# 2. Wait for loops to respawn
sleep 10

# 3. Get PID of any auto_ingest_loop process
LOOP_PID=$(pgrep -f 'auto_ingest_loop.sh' | head -1)

# 4. Check env vars IN THE RUNNING PROCESS (not in .zshrc, not in your shell — in the actual process)
# This is the ONLY verification that matters:
ps eww -p $LOOP_PID | tr ' ' '\n' | grep SYNCRESCENDENCE_REMOTE
```

Expected output must include:
- `SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA=macbook-air`
- Other agents = `local`

If `ps eww` doesn't show the vars, THE FIX DIDN'T WORK. Do not claim success.

```bash
# 5. Verify authorized_keys is clean
grep -v '^ssh-\|^#\|^$' ~/.ssh/authorized_keys
```
Expected: empty (no non-key, non-comment lines).

## Commit
```bash
git add -A && git commit -m 'fix(bridge): launchd env propagation for Neural Bridge SCP routing'
```

## FAILURE CRITERIA
- If `ps eww` does not show the env vars in the running process, mark FAILED
- If authorized_keys still has malformed lines, mark FAILED
- Do NOT claim success based on grep of config files — only runtime verification counts
