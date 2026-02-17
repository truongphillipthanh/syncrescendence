# TASK-20260217-force_offline_test

**Priority**: P0
**Kind**: TASK
**From-Agent**: commander
**To-Agent**: commander
**Reply-To**: commander
**CC**: commander
**Status**: PENDING
**Created**: 2026-02-17T00:30:00Z

---

## Objective

FORCE OFFLINE TEST. Execute the following kill sequence. WARNING: This will kill YOUR session (Commander dies when tmux dies). The recovery chain must bring everything back.

Execute this EXACT sequence:

```bash
echo "=== FORCE OFFLINE TEST — $(date) ===" | tee /tmp/force-offline-test.log

# 1. Kill all auto-ingest loops
echo "[KILL] Auto-ingest loops..." | tee -a /tmp/force-offline-test.log
for agent in commander adjudicator psyche cartographer ajna; do
    lockfile="$HOME/Desktop/syncrescendence/-INBOX/${agent}/.auto_ingest.lock"
    if [ -f "$lockfile" ]; then
        pid=$(cat "$lockfile")
        kill "$pid" 2>/dev/null && echo "  Killed ${agent} auto-ingest (PID $pid)" | tee -a /tmp/force-offline-test.log
        rm -f "$lockfile"
    fi
done

# 2. Stop Docker
echo "[KILL] Docker..." | tee -a /tmp/force-offline-test.log
osascript -e 'quit app "Docker"' 2>/dev/null
sleep 2

# 3. Record timestamp
echo "[KILL] tmux constellation — $(date)" | tee -a /tmp/force-offline-test.log

# 4. Kill tmux (THIS KILLS COMMANDER — last command to execute)
tmux kill-server 2>/dev/null
```

After executing, you will be terminated. The launchd recovery chain should bring everything back. MBA Commander will monitor.
