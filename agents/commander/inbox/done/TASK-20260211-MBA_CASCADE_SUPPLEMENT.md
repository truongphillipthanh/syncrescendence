# TASK-20260211-MBA_CASCADE_SUPPLEMENT

**From**: Commander (Mac mini)
**To**: Commander (MacBook Air)
**Reply-To**: commander
**CC**: commander
**Issued**: 2026-02-11T22:00:00Z
**Kind**: DIRECTIVE
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-11T19:23:08Z
**Claimed-At**: 2026-02-11T19:19:58Z
**Claimed-By**: commander-M1-Mac-mini
**Kanban**: DONE
**Status**: COMPLETE
**IntentionLink**: INT-P015 (Mac mini=stable macro, MBA=kinetic micro), SYN-35 (capability encoding)

---

## Objective

Supplement the completed TASK-20260211-MBA_COMMANDER_SETUP with the comprehensive tooling cascade that was missing. The original TASK established Claude Code, MCP servers, and basic verification. This TASK installs the **full aesthetic CLI tier, Homebrew formulas, config file syncing, expanded skills, and voice layer** — everything needed for the MBA to be a proper kinetic micro node rather than a bare terminal.

**Dependency**: TASK-20260211-MBA_COMMANDER_SETUP (DONE). This task builds on that foundation.

---

## Phase 1: Homebrew Formula Cascade

### 1.1 Core Shell + Aesthetic Tier (MUST HAVE)

These are the formulas that make the terminal usable and beautiful. Install ALL of these:

```bash
# Modern CLI replacements (the "aesthetic tier")
brew install bat          # cat replacement with syntax highlighting
brew install eza          # ls replacement with icons + git status
brew install fd           # find replacement, fast
brew install ripgrep      # grep replacement, fast
brew install sd           # sed replacement, intuitive
brew install dust         # du replacement, visual
brew install duf          # df replacement, visual
brew install procs        # ps replacement, visual
brew install btop         # top replacement, visual (TUI)
brew install ncdu         # disk usage explorer

# Navigation + Search
brew install fzf          # Fuzzy finder (CRITICAL — many tools depend on this)
brew install zoxide       # cd replacement with frecency
brew install atuin        # Shell history search with sync

# Shell experience
brew install starship     # Cross-shell prompt (CRITICAL — powers the prompt theme)
brew install zsh-autosuggestions
brew install zsh-syntax-highlighting

# TUI Tools
brew install lazygit      # Git TUI (Sovereign uses this constantly)
brew install yazi         # File manager TUI
brew install glow         # Markdown renderer in terminal

# Git ecosystem
brew install git-delta    # Diff pager with syntax highlighting
brew install gh           # GitHub CLI
brew install tig          # Git history TUI
```

### 1.2 Development Tier (SHOULD HAVE)

```bash
# Build tools
brew install cmake
brew install jq           # JSON processor (CRITICAL for scripts)
brew install tree         # Directory visualization
brew install tmux         # Terminal multiplexer (CRITICAL)
brew install sesh         # tmux session manager
brew install neovim       # Editor (LazyVim config will follow)

# Language runtimes
brew install node         # Node.js (needed for Claude Code, skills)
brew install python@3.13  # Python 3.13 (avoid 3.14 — chromadb incompatible)

# Networking + Monitoring
brew install curl
brew install wget
brew install htop
brew install fastfetch    # System info
```

### 1.3 AI CLI Tier (SHOULD HAVE)

```bash
brew install aichat       # Multi-model CLI chat
brew install ollama       # Local LLM inference
```

### 1.4 Supplementary (NICE TO HAVE)

```bash
brew install tokei        # Code statistics
brew install hyperfine    # Command benchmarking
brew install tldr         # Simplified man pages
brew install mas          # Mac App Store CLI
brew install topgrade     # Universal package updater
brew install terminal-notifier  # macOS notifications from CLI
```

### 1.5 Cask Applications (CHECK — may already be installed)

```bash
# Core
brew install --cask ghostty        # Terminal emulator
brew install --cask obsidian       # Vault client
brew install --cask cursor         # AI code editor
brew install --cask docker-desktop # Container runtime

# Productivity
brew install --cask raycast        # Launcher (replaces Spotlight)
brew install --cask karabiner-elements  # Keyboard remapping
brew install --cask maccy          # Clipboard manager
brew install --cask jordanbaird-ice     # Menu bar management

# Browsers
brew install --cask brave-browser
```

**Verification**:
```bash
# Confirm aesthetic tier is functional
bat --version && eza --version && fd --version && rg --version && fzf --version && starship --version && lazygit --version
echo "Aesthetic tier: $(brew list --formula | wc -l) formulas installed"
```

---

## Phase 2: Config File Syncing

The Mac mini has carefully tuned config files. Copy these to MBA. The repo syncs via git, but dotfiles live outside the repo. Use `scp` from MBA (if Mac mini is reachable) or manually recreate from the reference below.

### 2.1 Shell Config (~/.zshrc)

**Critical sections to include** (don't blindly copy — adapt paths for MBA hostname):

```bash
# Source from Mac mini:
scp macmini:~/.zshrc ~/.zshrc.macmini-ref

# Key sections to transfer:
# - Homebrew shellenv
# - Starship init
# - Atuin init
# - Zoxide init
# - Zsh-autosuggestions source
# - Zsh-syntax-highlighting source
# - FZF keybindings
# - Aliases: cockpit, doom-dash, ll='eza -la', cat='bat', etc.
# - NVIDIA_API_KEY and other env vars (source from ~/.syncrescendence/.env)
```

**MBA-specific adaptations**:
- `cockpit` alias should point to `mba-cockpit` tmux session (2-pane layout)
- Remove Mac mini-specific aliases (4-pane cockpit, aerospace, etc.)
- Keep all aesthetic aliases (ll, cat=bat, etc.)

### 2.2 Starship Config (~/.config/starship.toml)

```bash
mkdir -p ~/.config
scp macmini:~/.config/starship.toml ~/.config/starship.toml
```

No MBA adaptations needed — starship.toml is portable.

### 2.3 Ghostty Config (~/.config/ghostty/config)

```bash
mkdir -p ~/.config/ghostty
scp macmini:~/.config/ghostty/config ~/.config/ghostty/config
```

**MBA adaptations**: Remove ultrawide-specific window size settings. MBA display is 13" — use default or set to reasonable dimensions like `window-width = 180` `window-height = 50`.

### 2.4 Atuin Config (~/.config/atuin/config.toml)

```bash
mkdir -p ~/.config/atuin
scp macmini:~/.config/atuin/config.toml ~/.config/atuin/config.toml
```

Enable `sync_address` if using atuin sync between machines.

### 2.5 Bat Config

```bash
mkdir -p ~/.config/bat
scp macmini:~/.config/bat/config ~/.config/bat/config
# Theme: Catppuccin Mocha (matches Ghostty + Starship)
bat cache --build
```

### 2.6 Git Config (~/.gitconfig)

```bash
scp macmini:~/.gitconfig ~/.gitconfig
```

Verify `user.email` and `user.name` are correct for MBA. Should be same identity.

### 2.7 tmux Config (~/.tmux.conf)

```bash
scp macmini:~/.tmux.conf ~/.tmux.conf
```

**MBA adaptation**: MBA uses 2-pane layout, not 4x2 grid. The .tmux.conf keybindings should still work but the cockpit-specific prefix+N bindings won't map to 8 panes.

### 2.8 LazyVim Config (~/.config/nvim/)

```bash
# If LazyVim is configured on Mac mini:
rsync -av macmini:~/.config/nvim/ ~/.config/nvim/
```

**Verification**:
```bash
# Test each config
starship --version        # Prompt loads
atuin status              # History sync
bat --list-themes | grep -i catppuccin  # Theme exists
eza -la ~/Desktop/syncrescendence  # Icons + git status
git config user.name      # Identity correct
nvim --headless +q        # LazyVim bootstraps
```

---

## Phase 3: Expanded Skills Installation

The original TASK installed 4 skills. MBA Commander needs at minimum **16 core skills** for kinetic operations.

### 3.1 Core Operational Skills (MUST HAVE)

```bash
# Planning + execution
npx skills add obra/lace@commit-work -g -y
npx skills add obra/lace@dispatching-parallel-agents -g -y
npx skills add obra/lace@writing-plans -g -y
npx skills add obra/lace@executing-plans -g -y
npx skills add obra/lace@brainstorming -g -y

# Quality + verification
npx skills add obra/lace@verification-before-completion -g -y
npx skills add obra/lace@systematic-debugging -g -y
npx skills add obra/lace@requesting-code-review -g -y
npx skills add obra/lace@receiving-code-review -g -y
npx skills add obra/lace@test-driven-development -g -y

# Session management
npx skills add obra/lace@session-handoff -g -y
npx skills add obra/lace@using-git-worktrees -g -y
npx skills add obra/lace@finishing-a-development-branch -g -y

# Python development
npx skills add obra/lace@modern-python -g -y

# Context engineering
npx skills add obra/lace@ask-questions-if-underspecified -g -y
npx skills add obra/lace@using-superpowers -g -y
```

### 3.2 Syncrescendence Custom Skills (SHOULD HAVE)

These are custom skills in the repo that should be symlinked or copied:

```bash
# The claresce skill (our meta-operation)
# This is already in ~/.claude/skills/ if settings.json references it
# Verify:
ls ~/.claude/skills/claresce/ 2>/dev/null || echo "MISSING — needs manual setup"
```

### 3.3 CEK Skills (NICE TO HAVE)

The Mac mini has 63 `cek-*` skills. MBA doesn't need all of them. Install the critical subset:

```bash
# Only if cek skills are available:
npx skills add anthropics/cek@cek-commit -g -y 2>/dev/null
npx skills add anthropics/cek@cek-plan -g -y 2>/dev/null
npx skills add anthropics/cek@cek-brainstorm -g -y 2>/dev/null
npx skills add anthropics/cek@cek-reflect -g -y 2>/dev/null
```

**Verification**:
```bash
echo "Skills installed: $(ls ~/.agents/skills/ 2>/dev/null | wc -l)"
# Should be >= 16
```

---

## Phase 4: Claude Code Settings Sync

### 4.1 settings.json

Check if `~/.claude/settings.json` exists on MBA. If not, create it with these essential entries:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "alwaysThinkingEnabled": true,
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "terminal-notifier -title 'Claude Code' -message 'Session stopped' -sound default"
          },
          {
            "type": "command",
            "command": "cd /Users/home/Desktop/syncrescendence && bash orchestration/scripts/session_log.sh"
          },
          {
            "type": "command",
            "command": "cd /Users/home/Desktop/syncrescendence && bash orchestration/scripts/ajna_pedigree.sh"
          },
          {
            "type": "command",
            "command": "cd /Users/home/Desktop/syncrescendence && bash orchestration/scripts/create_execution_log.sh"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "cd /Users/home/Desktop/syncrescendence && bash orchestration/scripts/intent_compass.sh"
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "cd /Users/home/Desktop/syncrescendence && bash orchestration/scripts/pre_compaction.sh"
          }
        ]
      }
    ],
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "terminal-notifier -title 'Claude Code' -message '$CLAUDE_NOTIFICATION' -sound Basso"
          }
        ]
      }
    ]
  }
}
```

**MBA adaptation**: The hook script paths reference `~/Desktop/syncrescendence` which must exist and be the git-synced repo.

### 4.2 CLAUDE.md Symlink

Verify that `~/Desktop/syncrescendence/CLAUDE.md` is loaded when Commander starts in the repo directory. This is automatic if cwd is the repo root.

---

## Phase 5: Voice Layer (OPTIONAL — for parity)

Mac mini has `whisper-cpp` for STT. MBA can have a lightweight equivalent:

```bash
brew install whisper-cpp  # If available
# Or use the macOS built-in dictation as a lighter alternative
```

This is lowest priority. The MBA's role is kinetic text operations, not voice-first.

---

## Phase 6: Environment Variables

Ensure `~/.syncrescendence/.env` has all required keys:

```bash
# Required on MBA:
grep -c 'NVIDIA_API_KEY' ~/.syncrescendence/.env     # For Ajna (Kimi K2.5)
grep -c 'LINEAR_API_KEY' ~/.syncrescendence/.env      # For any Linear queries
grep -c 'CLICKUP_API_KEY' ~/.syncrescendence/.env     # For any ClickUp queries
grep -c 'GOOGLE_AI_API_KEY' ~/.syncrescendence/.env   # For Gemini/Cartographer

# NOT strictly required on MBA (Commander-mini handles these):
# ATLASSIAN_API_TOKEN, AIRTABLE_API_KEY, TODOIST_API_KEY
```

If `.env` is missing keys, copy from Mac mini:
```bash
scp macmini:~/.syncrescendence/.env ~/.syncrescendence/.env
```

---

## Completion Protocol

### On SUCCESS (Phases 1-4 complete):

1. Write results to:
   ```
   -INBOX/commander/00-INBOX0/RESULT-mba-cascade-20260211.md
   ```
   Include: formula count, skills count, config files synced, any failures.

2. Commit:
   ```bash
   git add -A && git commit -m "feat(SYN-35): MBA cascade supplement — Homebrew + configs + skills"
   git push origin main
   ```

### On PARTIAL:

1. Write results noting what succeeded and what's blocked (e.g., Mac mini unreachable for scp)
2. Commit with: `chore(SYN-35): MBA cascade partial — N/6 phases complete`

---

## Reference: Mac mini Inventory (for comparison)

| Category | Mac mini | MBA Target |
|----------|----------|------------|
| Homebrew formulas | 319 | ~50-60 (essential subset) |
| Homebrew casks | 84 | ~10-15 (essential subset) |
| Skills (agents) | 227 | 16-20 (core operational) |
| Hooks | 7 (4 Stop + 1 UserPromptSubmit + 1 PreCompact + 1 Notification) | 7 (same set) |
| MCP servers | 12 | 3-5 (local-only) |
| launchd agents | 19 | 3-5 (essential only) |
| Config files | 8+ dotfile configs | 8+ (synced from Mac mini) |

The MBA is NOT trying to replicate the Mac mini. It's the kinetic micro node — it needs enough tooling to be comfortable and productive, but the heavy infrastructure stays on Mac mini.
