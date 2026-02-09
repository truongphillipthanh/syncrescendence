# TASK: MacBook Air Deployment Guide for Ajna (Kimi K2.5)

**Date**: 2026-02-09
**From**: Commander
**To**: Ajna (or Sovereign for manual execution)
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-09T18:58:30Z
**Claimed-At**: 2026-02-09T18:57:56Z
**Claimed-By**: ajna-Lisas-MacBook-Air
**Kanban**: DONE
**Reply-To**: commander
**CC**: commander
**Status**: COMPLETE

---

## Objective

Configure the MacBook Air (Lisas-MacBook-Air) as Ajna's permanent home with Kimi K2.5 via NVIDIA NIM API.

---

## Prerequisites

- MacBook Air has: macOS, basic shell access
- Sovereign has: SSH/physical access to MBA
- Credentials: NVIDIA API key (stored in repo-adjacent .env)

---

## Step-by-Step Deployment

### 1. Install Homebrew + Core Tools
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git node bun tmux neovim
```

### 2. Clone Repository
```bash
cd ~/Desktop
git clone <repo-url> syncrescendence
cd syncrescendence
```

### 3. Install OpenClaw
```bash
npm install -g openclaw@latest
openclaw --version  # Should be 2026.2.6-3+
```

### 4. Configure OpenClaw with NVIDIA Provider
Create `~/.openclaw/openclaw.json`:
```json
{
  "auth": {
    "profiles": {}
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "nvidia/moonshotai/kimi-k2.5"
      },
      "workspace": "/Users/<user>/.openclaw/workspace",
      "memorySearch": {
        "enabled": true,
        "sources": ["memory"],
        "extraPaths": [
          "/Users/<user>/Desktop/syncrescendence/COCKPIT.md",
          "/Users/<user>/Desktop/syncrescendence/CLAUDE.md",
          "/Users/<user>/Desktop/syncrescendence/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md",
          "/Users/<user>/Desktop/syncrescendence/00-ORCHESTRATION/state/DYN-BACKLOG.md"
        ]
      },
      "heartbeat": {
        "every": "30m"
      },
      "maxConcurrent": 2,
      "subagents": {
        "maxConcurrent": 4
      }
    }
  },
  "models": {
    "providers": {
      "nvidia": {
        "baseUrl": "https://integrate.api.nvidia.com/v1",
        "apiKey": "${NVIDIA_API_KEY}",
        "api": "openai-completions",
        "models": [
          {
            "id": "moonshotai/kimi-k2.5",
            "name": "Kimi K2.5",
            "reasoning": true,
            "input": ["text", "image"],
            "contextWindow": 262000,
            "maxTokens": 32768
          }
        ]
      }
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "auth": {
      "mode": "token"
    }
  },
  "plugins": {
    "entries": {
      "discord": {
        "enabled": true
      }
    }
  },
  "skills": {
    "install": {
      "nodeManager": "bun"
    }
  }
}
```

### 5. Store Credentials
```bash
mkdir -p ~/.openclaw
echo 'NVIDIA_API_KEY=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' > ~/.openclaw/.env
chmod 600 ~/.openclaw/.env
```

### 6. Install Universal Skills
```bash
mkdir -p ~/.agents/skills
# Install all 16 universal skills
for skill in tmux dispatching-parallel-agents systematic-debugging using-git-worktrees verification-before-completion writing-plans executing-plans subagent-driven-development session-handoff web-to-markdown skill-judge commit-work mermaid-diagrams; do
  npx skills add "obra/superpowers@$skill" -g -y 2>/dev/null || echo "Skipping $skill"
done
```

### 7. Create OpenClaw Workspace Files
```bash
mkdir -p ~/.openclaw/workspace
# Copy SOUL.md, USER.md, MEMORY.md from Mac mini or create fresh
```

### 8. Set Up Inbox Watcher (launchd)
Create `~/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.syncrescendence.watch-ajna</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>-c</string>
    <string>cd ~/Desktop/syncrescendence && /usr/bin/fswatch -0 -e '.*' -i 'TASK-.*\\.md$' -INBOX/ajna/00-INBOX0/ | while read -d '' event; do echo "$(date): $event" >> /tmp/syncrescendence-ajna-watcher.log; done</string>
  </array>
  <key>KeepAlive</key>
  <true/>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
```

### 9. Set Up OpenClaw Gateway (launchd)
Create `~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.syncrescendence.openclaw-gateway</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/local/bin/openclaw</string>
    <string>gateway</string>
    <string>start</string>
  </array>
  <key>KeepAlive</key>
  <true/>
  <key>RunAtLoad</key>
  <true/>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin</string>
  </dict>
</dict>
</plist>
```

### 10. Bootstrap Services
```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.watch-ajna.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist
```

### 11. Verify
```bash
openclaw gateway status
openclaw chat "Hello, I am Ajna. Confirm model identity."
curl -s http://localhost:18789/health
```

---

## Notes

- **NVIDIA free tier is limited** (~1,000 credits, 40 RPM). Monitor usage.
- **No Docker on MBA** — Docker services (Neo4j, Graphiti, Qdrant) remain on Mac mini
- **No MCP Adapter or Mem0** on MBA initially — these require Docker services on Mac mini
- **Git sync** is the primary communication channel (`-INBOX/ajna/` + `-INBOX/psyche/`)
- **MBA is lower-powered** than Mac mini — reduce maxConcurrent accordingly
