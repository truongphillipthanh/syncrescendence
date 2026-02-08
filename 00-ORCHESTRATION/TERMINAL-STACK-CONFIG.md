# Syncrescendence Terminal Stack — Configuration Ledger

> Canonical reference for all terminal environment choices.
> Updated: 2026-02-08

## Terminal Emulators

| App | Role | Status |
|-----|------|--------|
| **Ghostty** | Primary terminal | Configured |
| iTerm2 | Secondary (pending config) | Pending |
| Terminal.app | Fallback (pending config) | Pending |

## Shell

| Component | Choice | Notes |
|-----------|--------|-------|
| Shell | **Zsh** (macOS default) | |
| Prompt | **Powerlevel10k** | Lean, Unicode, Transient prompt |
| Autosuggestions | **zsh-autosuggestions** | Fish-style inline suggestions |
| Syntax highlighting | **zsh-syntax-highlighting** | Real-time command coloring |
| History | **Atuin** | Fuzzy search, synced across machines |
| Directory jumper | **zoxide** | Frecency-based `z` command |
| Fuzzy finder | **fzf** | Ctrl+R, file search, piping |
| Env management | **direnv** | Auto-load per-directory env vars |

## Visual Theme

| Surface | Theme |
|---------|-------|
| Ghostty | **Catppuccin Mocha** |
| bat | Catppuccin Mocha |
| btop | Catppuccin Mocha |
| lazygit | Catppuccin Mocha |
| git-delta | Catppuccin Mocha |
| Obsidian | (existing config, not modified) |

## Font

| Setting | Value |
|---------|-------|
| Family | **Liga SFMono Nerd Font** |
| Features | Ligatures enabled (`calt`, `liga`, `dlig`) |
| Installed via | `shaunsingh/SFMono-Nerd-Font-Ligaturized` tap |
| Weights | 12 (Light through Heavy, with italics) |

## Multiplexer

| Component | Choice | Notes |
|-----------|--------|-------|
| Multiplexer | **tmux 3.6a** | Config at `~/.tmux.conf` (DEC-HQ-001: canonical) |
| Session Manager | **sesh 2.22.0** | Config at `~/.config/sesh/sesh.toml` |
| Scrollback | 100,000 lines | |
| Prefix | Ctrl+Space | |
| Pane Navigation | Ctrl+hjkl (vim-tmux-navigator) | |
| Session Switching | `prefix+f` or `Ctrl+f` (sesh + fzf) | |
| Plugins | 11 TPM plugins (Catppuccin, resurrect, continuum, yank, fingers, extrakto, cowboy, notify) | |
| Zellij | Secondary (installed, not the cockpit substrate) | Legacy alias `zj` preserved |

## TUI Applications

| Tool | Replaces | Purpose |
|------|----------|---------|
| **yazi** | Finder/ranger | File manager with image previews |
| **btop** | Activity Monitor | System monitor (mouse, braille graphs) |
| **lazygit** | `git` commands | Visual git interface with delta |
| **glow** | — | Terminal markdown renderer |
| **fx** | — | Interactive JSON viewer |

## Modern CLI Replacements

| Tool | Replaces | Alias |
|------|----------|-------|
| **eza** | `ls` | `ls`, `ll`, `la`, `tree` |
| **bat** | `cat` | `cat` |
| **duf** | `df` | `df` |
| **procs** | `ps` | `ps` |
| **tldr** | `man` | `help` |
| **httpie** | `curl` | `http`/`https` |
| **fd** | `find` | `find` |
| **rg** (ripgrep) | `grep` | `grep` |
| **dust** | `du` | Disk usage by directory |
| **tokei** | `cloc` | Code statistics |

## Agent Ecosystem

| Tool | Purpose |
|------|---------|
| **terminal-notifier** | macOS notifications on agent task completion |
| **git-delta** | Syntax-highlighted diffs for reviewing agent code |
| **gh** | GitHub CLI (PRs, issues, API) — authenticated |
| **gum** | Styled shell script UI for agent launchers |

## CLI Agents

| Agent | Version | Runtime |
|-------|---------|---------|
| **Claude Code** | 2.1.37 | Node 24 (nvm) |
| **Codex CLI** | 0.98.0 | Node 24 (nvm) |
| **Gemini CLI** | 0.27.3 | Homebrew |
| **OpenClaw** | present | Node 24 (nvm) |

## Development Stack (for future projects)

| Layer | Choice | Notes |
|-------|--------|-------|
| JS Runtime | **Bun** 1.2.13 | Default for new projects |
| Node.js | v24.13.0 (nvm) | Legacy/agent runtime |
| Python | 3.13.5 (miniconda3) | Orchestration scripts |
| Rust | 1.93.0 (Homebrew) | Available, not primary |
| Frontend scaffold | **Vite** | Via `bun create vite` |
| CSS | **Tailwind CSS** | Utility-first |
| Linter/Formatter | **Biome** | Replaces ESLint + Prettier |
| Backend (if needed) | **PocketBase** | SQLite-backed, single binary |

## Git Integration

| Setting | Value |
|---------|-------|
| Pager | delta |
| Delta side-by-side | true |
| Delta line numbers | true |
| Delta hyperlinks | true |
| Merge conflict style | diff3 |
| Color moved | default |

## Claude Code Hooks

| Event | Action |
|-------|--------|
| Stop | `terminal-notifier` — "Session stopped" |
| Notification | `terminal-notifier` — message with Basso sound |

## Config File Locations

| File | Purpose |
|------|---------|
| `~/.zshrc` | Shell config (p10k, plugins, aliases, hooks) |
| `~/.p10k.zsh` | Powerlevel10k theme (lean/unicode/transient) |
| `~/.config/ghostty/config` | Ghostty terminal emulator |
| `~/.tmux.conf` | tmux multiplexer (canonical) |
| `~/.config/sesh/sesh.toml` | sesh session manager |
| `~/.config/zellij/config.kdl` | Zellij (secondary) |
| `~/.config/btop/btop.conf` | btop system monitor |
| `~/.config/yazi/yazi.toml` | yazi file manager |
| `~/.config/atuin/config.toml` | Atuin shell history |
| `~/.config/glow/glow.yml` | glow markdown renderer |
| `~/.config/bat/themes/` | bat Catppuccin theme |
| `~/.claude/settings.json` | Claude Code hooks |
| `~/Library/Application Support/lazygit/config.yml` | lazygit |
| `~/.gitconfig` | Git + delta integration |

## Runtime Version Management

| Tool | Purpose | Notes |
|------|---------|-------|
| **mise** | Universal runtime manager | Replaces nvm/pyenv. Activated in .zshrc |
| nvm | Node.js version manager | Legacy, still in .zshrc (mise can subsume) |
| pyenv | Python version manager | Legacy, still in .zshrc (mise can subsume) |
| miniconda3 | Python env manager | Existing, preserved |

## Linter / Formatter

| Tool | Purpose | Notes |
|------|---------|-------|
| **Biome** 2.3.14 | Lint + format (replaces ESLint + Prettier) | Installed globally via Bun |

## MCP Servers (Model Context Protocol)

Claude Code's bridge to external surfaces. Config at `~/.claude.json`.

### Connected (Working)

| Server | Surface | Type | Auth |
|--------|---------|------|------|
| **obsidian** | Syncrescendence vault | stdio (npx) | None (filesystem) |
| **filesystem** | ~/Desktop/syncrescendence + ~/Documents | stdio (npx) | None (sandboxed) |
| **chrome-devtools** | Chrome browser | stdio (npx) | None |
| **playwright** | Any browser (Chromium/Firefox/WebKit) | stdio (npx) | None |

### Needs OAuth (one-time browser auth on first use)

| Server | Surface | URL |
|--------|---------|-----|
| **linear** | Linear (repo-bound work) | `https://mcp.linear.app/mcp` |
| **clickup** | ClickUp (meta-work) | `https://mcp.clickup.com/mcp` |
| **notion** | Notion (dashboards) | `https://mcp.notion.com/mcp` |
| **dropbox** | Dropbox (file storage) | `https://mcp.dropbox.com/mcp` |
| **figma** | Figma (design) | `https://mcp.figma.com/mcp` |

### Tier C: Needs Auth Setup (not yet installed)

| Server | Surface | Blocker |
|--------|---------|---------|
| GitHub MCP | GitHub repos/PRs | Needs Personal Access Token |
| Slack MCP | Slack workspace | Needs Bot Token |
| Discord MCP | Discord server | Needs Bot Token |
| Airtable MCP | Airtable bases | Needs Personal Access Token |
| Brave Search MCP | Web search | Needs Brave API key |

### Tier D: Install When Needed

| Server | Surface | Notes |
|--------|---------|-------|
| Make MCP | Make/Integromat scenarios | Needs API key |
| Canva MCP | Design creation | Official, OAuth |
| Outlook/M365 MCP | Email + calendar | Azure AD auth |
| Box MCP | Box storage | JWT auth |
| Google Drive MCP | GDrive files | OAuth Desktop App |
| ChatGPT bridge | ChatGPT Desktop | osascript-based |
| Perplexity MCP | Perplexity API | Needs API key |
| Grok MCP | xAI API | Needs API key |
| Xcode MCP | iOS/macOS dev | Apple official in Xcode 26.3 |
| Apple Native MCP | Reminders, Notes, Calendar, etc. | AppleScript-based |
| Keyboard Maestro MCP | macOS automation | Anthropic-affiliated |
| Shortcuts MCP | Apple Shortcuts | Also usable via `shortcuts` CLI |
| NotebookLM MCP | Google NotebookLM | FRAGILE — undocumented API |
| Manus MCP | Manus AI | REST API |

### MCP Tool Search

Built-in Claude Code feature. Auto-activates when tool descriptions exceed 10% of context window. Defers tool loading and searches on-demand via regex/BM25. No configuration needed — defaults to `auto`.

### MCP Registries (for discovery)

| Registry | URL | Scale |
|----------|-----|-------|
| mcp.so | mcp.so | 17,500+ |
| Smithery | smithery.ai | 7,300+ |
| PulseMCP | pulsemcp.com/servers | 8,050+ |
| Official | registry.modelcontextprotocol.io | Curated |

## macOS Enhancements (Evaluated)

| Tool | Purpose | Status | Priority |
|------|---------|--------|----------|
| **Raycast** | Spotlight replacement (ClaudeCast, Code Runway extensions) | Recommended | High |
| **AeroSpace** | i3-like tiling WM (no SIP disable needed) | Recommended | High |
| **JankyBorders** | Window focus borders (pairs with AeroSpace) | Recommended | High |
| **Karabiner-Elements** | Hyper Key (Caps Lock → Ctrl+Opt+Cmd+Shift) | Recommended | High |
| **Ice** | Menu bar management (replaces Bartender) | Recommended | Medium |
| **Peek** (or individual QL plugins) | Quick Look for code/markdown/JSON | Recommended | Medium |
| **`defaults write` settings** | Key repeat, Dock auto-hide, Finder show hidden | Recommended | Immediate |
| **Syncthing** | P2P vault sync (no iCloud) | Evaluate | Low |
| **Marta** | Dual-pane file manager | Evaluate | Low |
| **Finicky** | URL router (multi-browser) | Evaluate | Low |
| **SketchyBar** | Custom scriptable menu bar | Evaluate | Low |

## Code Editor (Backlog)

| Candidate | Notes |
|-----------|-------|
| **Nova** (Panic) | macOS-native, gorgeous, $99/yr |
| **Zed** | Rust-native, fast, AI-integrated, free |
| **BBEdit** | Pure Mac, no frills |
| **CotEditor** | Free, lightweight, native |
| Decision: deferred | Non-urgent — CLI agents write the code |

## macOS Power-User Settings (Applied 2026-02-08)

| Category | Settings |
|----------|----------|
| Key Repeat | KeyRepeat=2, InitialKeyRepeat=15 |
| Dock | Auto-hide (0 delay, 0.15s animation), no recents, minimize-to-app |
| Finder | Show all files, path bar, status bar, all extensions, list view |
| Screenshots | ~/Desktop/Screenshots, PNG, no shadow |
| Animations | Window animations off, Quick Look instant, resize instant |
| Save Dialogs | Expanded by default, local save default |
| Security | Quarantine nag disabled |
| Trackpad | Tap to click enabled |

## macOS Power Apps (Installed 2026-02-08)

| App | Version | Config |
|-----|---------|--------|
| **Raycast** | 1.104.5 | In-app config (replace Spotlight Cmd+Space) |
| **AeroSpace** | 0.20.2-Beta | `~/.aerospace.toml` (Alt+hjkl, workspaces, 8px gaps) |
| **JankyBorders** | 1.8.4 | `~/.config/borders/bordersrc` (Catppuccin blue active, brew service) |
| **Karabiner-Elements** | latest | `~/.config/karabiner/karabiner.json` (Hyper Key: CapsLock) |
| **Ice** | latest | Menu bar management (configure in-app) |
| Peek | NOT AVAILABLE via Homebrew | Use Mac App Store or `steipete/tap/peekaboo` |

## Backup Terminals (Configured 2026-02-08)

| Terminal | Theme | Font | Shell Integration |
|----------|-------|------|-------------------|
| **iTerm2** | Catppuccin Mocha (imported) | Liga SFMono Nerd Font 13pt | `~/.iterm2_shell_integration.zsh` sourced |
| **Terminal.app** | Catppuccin Mocha profile (imported) | Liga SFMono Nerd Font 13pt | N/A |

## tmux Cockpit (Designed 2026-02-08)

| Component | Location |
|-----------|----------|
| Design doc | `00-ORCHESTRATION/scripts/DESIGN-TMUX_COCKPIT.md` |
| Launch script | `00-ORCHESTRATION/scripts/cockpit.sh` (3 modes: shell/launch/kill) |
| sesh config | `~/.config/sesh/sesh.toml` (constellation, sync-edit, scratch) |
| Prefix key | Ctrl+Space (preserved from existing config) |
| Layout | 2x2 grid: Commander(blue) / Adjudicator(green) / Cartographer(yellow) / Psyche(mauve) |

## OpenClaw MCP Parity (Researched 2026-02-08)

| Finding | Detail |
|---------|--------|
| Native MCP | NOT supported (creator rejects MCP philosophy) |
| Community bridges | `openclaw-mcp-plugin` (HTTP), `openclaw-mcp-adapter` (tool wrapping) |
| Recommended path | Local MCP Gateway (Lasso or MCP Bridge) — all agents share one proxy |
| Codex CLI gap | stdio only — no HTTP/SSE transport yet |

## MCP Auth Guide (Created 2026-02-08)

Full setup guide at `00-ORCHESTRATION/state/impl/GUIDE-MCP-AUTH-SETUP.md`
- 5 OAuth servers: Linear, ClickUp, Notion, Dropbox, Figma
- 5 Tier C servers: GitHub, Slack, Discord, Airtable, Brave Search (with verified npm packages + config blocks)

## Grand Unification — Declarative State (2026-02-08)

| Component | Location |
|-----------|----------|
| **Brewfile (Golden State)** | `~/Brewfile` |
| Audit script | `00-ORCHESTRATION/scripts/audit_applications.sh` |
| Audit report | `/tmp/app_audit_report.md` (regenerate via script) |
| Topgrade config | `~/.config/topgrade/topgrade.toml` |
| App backup | `/tmp/app_backup_20260207_192345.txt` |

### Audit Results

| Category | Count |
|----------|-------|
| Homebrew Cask (managed) | 54 |
| Mac App Store | 74 |
| Adoption Candidates | 14 (verified real casks) |
| Apple System | 1 |
| Unmanaged | 24 (mostly drivers/helpers) |
| **Total** | **181** |

### Brewfile Composition

| Section | Count |
|---------|-------|
| Taps | 9 |
| Formulae (leaves) | ~90 |
| Casks (managed) | ~62 |
| Adoption candidates (commented) | 14 |
| MAS entries | ~98 |

### Topgrade

| Setting | Value |
|---------|-------|
| Version | 16.9.0 |
| Cleanup | enabled |
| Disabled steps | pip3, gem, containers, vim, node, deno, etc. |
| Custom commands | Bun global update, Atuin sync, tldr cache |
| Greedy cask | false (respects auto-updaters) |

### Usage

```bash
# Check what's missing
brew bundle check --file=~/Brewfile

# Install everything in the Brewfile
brew bundle install --file=~/Brewfile

# Remove things not in the Brewfile
brew bundle cleanup --file=~/Brewfile --force

# Run all updates
topgrade

# Re-audit applications
bash ~/Desktop/syncrescendence/00-ORCHESTRATION/scripts/audit_applications.sh
```

## Sovereign Cockpit Architecture (2026-02-08)

> Clarescence: `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-08-sovereign-cockpit-architecture.md`

The Sovereign Cockpit is a "Headless OS" paradigm: the Sovereign operates primarily through a text-based Action Layer (the Cockpit), using GUI tools strictly for verification and delegation.

### Architecture Layers

| Layer | Surface | Role | Status |
|-------|---------|------|--------|
| **1. Terminal** | Ghostty | GPU-accelerated primary interface | COMPLETE |
| **2. Context Engine** | Zsh + P10k + modern CLI | HUD for git/exec/dir state | COMPLETE |
| **3. Multiplexer** | tmux + sesh | Session persistence, 4-lane cockpit | CONFIGURED (needs plugin install) |
| **4. Runtime** | Bun | JS toolkit (bundler/test/PM) | COMPLETE |
| **5. Prose Engine** | Neovim + LazyVim | Intent composition + Agent Pipe | COMPLETE |
| **6. Voice Layer** | Whisper + Piper + sox | Local speech loop, persona DSP | COMPLETE |
| **7. Dashboard** | Doom Emacs + Org Mode | Read-only state visualization | COMPLETE |
| **8. Simulators** | Cursor, Antigravity, Xcode | Verification + async delegation | AVAILABLE |

### Decision Atoms (DEC-COCKPIT-001 through 006)

| ID | Decision |
|----|----------|
| 001 | Neovim = Prose Engine. Emacs = Dashboard. Cursor = Simulator. No overlap. |
| 002 | Voice Layer is Phase 3 (after tmux + Neovim fluency). Install now, adopt later. |
| 003 | Emacs scope is ABSOLUTE: Org Mode dashboard, read-only. No code editing. |
| 004 | 8 constellation questions answered (see clarescence §VI). Sovereign ratification required. |
| 005 | Cursor disposition: SUNSET as IDE → ACTIVE as Simulator (async delegation). |
| 006 | Tailscale for cross-machine Psyche dispatch. Not filesystem sync. |

### Blitzkrieg Lane ↔ Cockpit Pane Mapping

```
┌─────────────────┬─────────────────┐
│   COMMANDER     │   ADJUDICATOR   │
│   Claude Code   │   Codex CLI     │
│   Lane A (blue) │   Lane B (green)│
├─────────────────┼─────────────────┤
│   CARTOGRAPHER  │   PSYCHE/AJNA   │
│   Gemini CLI    │   OpenClaw      │
│   Lane C (yel)  │   Lane D (mauv) │
└─────────────────┴─────────────────┘
```

### Prose Engine (Neovim/LazyVim)

| Component | Config | Status |
|-----------|--------|--------|
| Binary | NVIM v0.11.6 | INSTALLED |
| Framework | LazyVim (starter template) | INSTALLED (37 plugins) |
| Theme | Catppuccin Mocha (transparent) | CONFIGURED |
| Writing | zen-mode.nvim + twilight.nvim + render-markdown.nvim | CONFIGURED |
| Agent Pipe | Custom Lua plugin — `<leader>ac/aa/ag/ap` to send selection to tmux pane | CONFIGURED |
| Config location | `~/.config/nvim/lua/plugins/` (4 files) | READY |

### Voice Layer

| Component | Tool | Status |
|-----------|------|--------|
| Transcription | whisper-cli (v1.8.3, Metal-accelerated) | INSTALLED |
| Models | ggml-base.en.bin (148M), ggml-small.en.bin (488M) | READY at `~/.local/share/whisper-models/` |
| Synthesis | Piper TTS (pip3, v1.3.0) | INSTALLED |
| Voices | en_US-amy-medium, en_US-ryan-medium, en_GB-alba-medium (63M each) | READY at `~/.local/share/piper-voices/` |
| DSP Personas | sox filter profiles | 4 profiles READY at `~/.config/voice-personas/` |
| Pipeline | `voice-capture.sh`, `voice-speak.sh` | READY at `00-ORCHESTRATION/scripts/` |

### Dashboard (Doom Emacs)

| Component | Config | Status |
|-----------|--------|--------|
| Binary | GNU Emacs 30.2 (emacs-plus@30, 605.5MB) | INSTALLED |
| App | `/Applications/Emacs.app` | COPIED |
| Framework | Doom Emacs (138 packages) | INSTALLED |
| Theme | Catppuccin Mocha | CONFIGURED |
| Font | Liga SFMono Nerd Font 14pt | CONFIGURED |
| Scope | Org Mode (org-roam, journal, noter), state file viewer | CONFIGURED |
| Read-only | Auto-enabled for `00-ORCHESTRATION/state/` files | CONFIGURED |
| Keybindings | `SPC d s` cockpit, `SPC d i` compass, `SPC d e` exec-log, `SPC d l` session-log, `SPC d t` terminal-stack, `SPC d a` agenda, `SPC d r` refresh | CONFIGURED |
| Config location | `~/.config/doom/` (init.el, config.el, packages.el) | READY |
| Doom binary | `~/.config/emacs/bin/doom` | Add to PATH |

### Constellation Clarescence Answers (Sovereign Ratification Required)

| # | Question | Recommended Answer |
|---|----------|--------------------|
| 1 | Ajna concurrent tasks | One-at-a-time with FIFO queue |
| 2 | Psyche topology | MacBook Air confirmed, Tailscale transport |
| 3 | Web platform dispatch | Manual only (not filesystem-kanban) |
| 4 | Cost-aware routing | Deferred (current model assignments are correct) |
| 5 | Escalation rules | 3-tier: PROCEED / NOTIFY / BLOCK |
| 6 | Compass ↔ Ledger sync | Manual weekly reconciliation |
| 7 | State compaction | compact_wisdom.sh at threshold=10 (already built) |
| 8 | Cross-machine race | flock-style locking on TASK claim + Tailscale |

### Session Discipline (Anti-Patterns to Break)

| Anti-Pattern | Solution | Tool |
|-------------|----------|------|
| Sequential single-terminal | 4-pane cockpit, named sessions | tmux + cockpit.sh |
| Context running forever | Clean reinit prompts, `/compact` at 75% | PROMPT-*.md files |
| 2-3 session ceiling | tmux pane splits + sesh instant switching | `Ctrl+f` / `prefix+f` |
| No composition surface | Neovim Prose Engine with Agent Pipe | `<leader>ac` keybinding |

## Pending

- [ ] OAuth authentication for 5 remote MCP servers (see GUIDE-MCP-AUTH-SETUP.md)
- [ ] Tier C MCP servers — create auth tokens, then install (see GUIDE-MCP-AUTH-SETUP.md)
- [ ] Tier D MCP servers (install on demand)
- [ ] Run `prefix+I` in tmux to install TPM plugins (Sovereign interaction)
- [ ] Test cockpit.sh launch (Sovereign interaction)
- [x] Cockpit keybindings appended to ~/.tmux.conf (prefix+1/2/3/4)
- [x] Doom binary added to PATH in ~/.zshrc
- [x] Cockpit aliases added to ~/.zshrc (cockpit, vc, vs)
- [ ] Raycast — disable Spotlight (Cmd+Space), assign to Raycast
- [ ] Adopt Dropbox + Google Drive via brew (uncomment in Brewfile)
- [ ] mise migration (fully replace nvm + pyenv)
- [ ] MCP Gateway deployment (Lasso or MCP Bridge) for cross-agent MCP sharing
- [x] DEC-HQ-001: Zellij→tmux resolved in §Multiplexer
- [x] DEC-HQ-002: Stack Teleology updated (Cursor = ACTIVE/Simulator)
- [x] DEC-HQ-003: Layers 5-7 status → COMPLETE
- [x] DEC-HQ-004: Doom keybindings canonicalized (SPC d prefix)
- [ ] DEC-HQ-005: Register Cockpit buildout in IMPLEMENTATION-MAP.md as Tranche E
- [ ] DEC-HQ-006: Execute 16-minute activation sequence (Sovereign interaction required)
- [ ] Ratify DEC-COCKPIT-001 through 006
- [ ] Ratify 8 constellation clarescence answers
- [ ] MacBook Air tmux/terminal config (Psyche's machine)
- [ ] INT-C005 tmux onboarding (guided tutorial after install)
- [ ] HighCommand QA pass (Agendizer Blitzkrieg + Saner + Reflect phases 5-9)
