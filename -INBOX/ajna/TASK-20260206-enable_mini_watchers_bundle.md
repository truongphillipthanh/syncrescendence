# TASK-20260206-enable_mini_watchers_bundle

**From**: Psyche
**To**: Ajna (Mac mini)
**Issued**: 2026-02-06
**Priority**: P0
**Status**: PENDING

---

## Objective

Enable the Mac mini as the always-on multi-agent executor by running launchd watchers for:
- ajna
- commander
- adjudicator
- cartographer

(Meanwhile, Psyche laptop stays manual for commander/adjudicator/cartographer.)

---

## Preconditions (macOS)

System Settings → Privacy & Security → Full Disk Access: ON for
- Terminal
- /bin/bash
- /opt/homebrew/bin/fswatch
- /usr/bin/python3
- /opt/homebrew/bin/openclaw
- (recommended) /opt/homebrew/bin/node

---

## Steps

1) Pull latest repo (plists + rearm script were updated)
```bash
cd ~/Desktop/syncrescendence
git pull
```

2) Re-arm watchers in **mini mode**
```bash
bash 00-ORCHESTRATION/scripts/rearm_watchers.sh --mini
```

3) Verify jobs are loaded
```bash
launchctl list | egrep 'com\.syncrescendence\.watch-(ajna|commander|adjudicator|cartographer)'
```

4) Check logs
```bash
tail -n 50 /tmp/syncrescendence-watch-ajna.log 2>/dev/null || true
tail -n 50 /tmp/syncrescendence-watch-commander.log 2>/dev/null || true
tail -n 50 /tmp/syncrescendence-watch-adjudicator.log 2>/dev/null || true
tail -n 50 /tmp/syncrescendence-watch-cartographer.log 2>/dev/null || true

# errors
for f in /tmp/syncrescendence-watch-*.err; do echo "--- $f"; tail -n 50 "$f"; done
```

---

## Concurrency / duplicate-consumer note

This setup assumes ONLY the Mac mini is watching these inboxes.
If another machine also watches the same inbox, you can get duplicate execution unless claim-locking is enabled.

Commander has recently implemented claim-locking and a global ledger; confirm those changes are present on the mini after pull.

---

## Expected Output

Write:
- `-OUTGOING/RESULT-ajna-20260206-enable_mini_watchers_bundle.md`

Include:
- launchctl list output
- confirmation that each watcher is printing “Watching -INBOX/{agent}/ …”
- any permission errors
