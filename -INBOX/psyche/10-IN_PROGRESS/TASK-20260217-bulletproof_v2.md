# TASK: Bulletproof Neural Bridge — plist env vars + comprehensive commit

**Status**: PENDING
**Priority**: P0
**Reply-To**: commander
**CC**: commander
**To**: psyche
**Timeout**: 600

## Objective

Add Neural Bridge env vars to the auto-ingest supervisor plist EnvironmentVariables (belt-and-suspenders alongside the working eval in supervisor.sh), then reload the supervisor, verify env vars propagate, and commit all pending Neural Bridge changes.

Context: Option A (eval in supervisor.sh) IS working — confirmed by auto_ingest_loop startup log. Option B (plist vars) adds resilience. watch_dispatch.sh has been killed and unloaded on both machines.

Step 1: Edit ~/Library/LaunchAgents/com.syncrescendence.auto-ingest-supervisor.plist. Add 5 keys inside the EnvironmentVariables dict after HOME: SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA=macbook-air, SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER=local, SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR=local, SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER=local, SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE=local.

Step 2: Reload supervisor with launchctl bootout/bootstrap. Wait 10s.

Step 3: Verify by checking auto_ingest log: tail -3 ~/Desktop/syncrescendence/-INBOX/psyche/auto_ingest.log — must show Neural Bridge env line.

Step 4: Commit all uncommitted changes: git add -A && git commit -m 'fix(bridge): plist EnvironmentVariables + watch_dispatch deprecation — bulletproof Neural Bridge'

**Reply-To**: commander
**CC**: commander
