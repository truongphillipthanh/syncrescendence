# TASK-20260217-disable_filevault_and_configure_autoboot

**Priority**: P0
**Kind**: TASK
**From-Agent**: commander
**To-Agent**: commander
**Reply-To**: commander
**CC**: commander
**Status**: PENDING
**Created**: 2026-02-17T00:20:00Z

---

## Objective

Execute the full zero-offline autonomous boot configuration. Sovereign has authorized the most resilient path.

### Step 1: Disable FileVault (SOVEREIGN AUTHORIZED)
```bash
# Confirm current state
fdesetup status
# Disable — will prompt for admin password (Sovereign is standing by)
sudo fdesetup disable
# Verify
fdesetup status
```
Note: Decryption happens in background after disable. May take hours for large disks. System remains usable during decryption.

### Step 2: Enable Auto-Login
```bash
# After FileVault is disabled, enable auto-login
sudo defaults write /Library/Preferences/com.apple.loginwindow autoLoginUser -string "home"
# Verify
defaults read /Library/Preferences/com.apple.loginwindow autoLoginUser
```

### Step 3: Configure Auto-Boot After Power Failure
```bash
sudo systemsetup -setrestartpowerfailure on
sudo systemsetup -setWaitForStartupAfterPowerFailure 30
sudo pmset repeat poweron MTWRFSU 00:00:00
# Verify
sudo systemsetup -getrestartpowerfailure
pmset -g sched
```

### Step 4: Run the full recovery configuration script
```bash
sudo bash ~/Desktop/syncrescendence/00-ORCHESTRATION/scripts/configure_auto_boot_recovery.sh
```

### Step 5: Enable Docker Desktop Auto-Start
Print this message for the Sovereign: "Open Docker Desktop → Settings → General → Enable 'Start Docker Desktop when you log in'" — this is the ONE manual GUI click needed.

### Step 6: Set Docker container restart policies
```bash
for container in $(docker ps -a --format '{{.Names}}'); do
    docker update --restart unless-stopped "$container"
    echo "Set restart policy: $container"
done
docker ps -a --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
```

### Step 7: Verify the full chain
```bash
echo "=== FileVault ===" && fdesetup status
echo "=== Auto-Login ===" && defaults read /Library/Preferences/com.apple.loginwindow autoLoginUser 2>/dev/null
echo "=== Auto-Boot ===" && sudo systemsetup -getrestartpowerfailure
echo "=== Scheduled Boot ===" && pmset -g sched
echo "=== Docker Restart Policies ===" && docker inspect --format '{{.Name}}: {{.HostConfig.RestartPolicy.Name}}' $(docker ps -aq) 2>/dev/null
echo "=== launchd Agents ===" && launchctl list | grep syncrescendence
echo "=== tmux Session ===" && tmux ls 2>/dev/null
echo "=== Auto-Ingest Locks ===" && find ~/Desktop/syncrescendence/-INBOX -name ".auto_ingest.lock" -exec sh -c 'echo "$1: PID=$(cat "$1")"' _ {} \;
```

Write full verification output to: -OUTBOX/commander/RESULTS/RESULT-commander-20260217-disable_filevault_and_configure_autoboot.md

The `sudo` commands will prompt for password — Sovereign is standing by to enter it.
