# SOVEREIGN DECISION REQUIRED: Mac Mini Plist Fixes

**Date**: 2026-02-13
**From**: Commander (COO)
**Priority**: P1
**Status**: BLOCKED — Psyche rate-limited, SSH timed out

## Context

MBA plist fixes were completed successfully this session:
- **watch-cartographer**: Added `SYNCRESCENDENCE_GEMINI_MODEL=gemini-2.5-pro` + `HOME=/Users/system`
- **watch-adjudicator**: Updated `SYNCRESCENDENCE_CODEX_MODEL` from `gpt-5.1-codex` to `gpt-5.2-codex`

Mac mini needs the same fixes, but:
1. **Psyche is rate-limited** (ChatGPT Plus quota hit, ~5151 min / ~3.5 days wait)
2. **SSH from MBA timed out** (Mac mini may be asleep or unreachable)
3. **Dispatches consumed but NOT executed** — watch_dispatch.sh false-positive (rate-limit not in fatal error patterns)

## Required Actions on Mac Mini

### Fix 1: Cartographer Plist
File: `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-cartographer.plist`

Add to `<dict>` under `EnvironmentVariables`:
```xml
<key>SYNCRESCENDENCE_GEMINI_MODEL</key>
<string>gemini-2.5-pro</string>
<key>HOME</key>
<string>/Users/home</string>
```

Then: `launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.watch-cartographer.plist && launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.watch-cartographer.plist`

### Fix 2: Adjudicator Model Update
File: `/Users/home/Library/LaunchAgents/com.syncrescendence.watch-adjudicator.plist`

Change: `gpt-5.1-codex` → `gpt-5.2-codex` in `SYNCRESCENDENCE_CODEX_MODEL`

Then: same launchctl bootout/bootstrap cycle.

### Fix 3: Harden watch_dispatch.sh Output Validation
File: `orchestration/scripts/watch_dispatch.sh` (line ~609)

Add `usage limit` and `hit your.*limit` to the fatal error regex so rate-limited executions are correctly marked FAILED.

## Options for Sovereign

1. **Wait** — Psyche rate limit resets in ~3.5 days, re-dispatch then
2. **Manual** — Wake Mac mini, open terminal, paste the commands above
3. **SSH** — If Mac mini is asleep, wake it (press key or wake via network), then Commander can SSH and execute
4. **Ajna relay** — If Ajna (OpenClaw on MBA) has access, dispatch through Ajna → Psyche
