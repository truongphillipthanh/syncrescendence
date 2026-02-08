# Fleet Commander's Handbook
## Sovereign Cockpit Operations Manual

> Version 1.1 | 2026-02-08
> Reference card. Not a tutorial. Press keys, get results.

---

## 1. Cockpit Quick Start

```
cockpit            # alias: sesh connect constellation
```

This launches the tmux `constellation` session via `sesh.toml` startup command. Four panes, 1x4 horizontal lanes (vertical columns across the ultrawide):

```
┌────────────┬────────────┬────────────┬────────────┐
│  1  CMD    │  2  ADJ    │  3  CART   │  4  PSY    │
│  Claude    │  Codex CLI │  Gemini    │  OpenClaw  │
│  Code      │            │  CLI       │            │
│  (blue)    │  (green)   │  (yellow)  │  (mauve)   │
└────────────┴────────────┴────────────┴────────────┘
```

**Switch panes** (prefix = `Ctrl+Space`):

| Keys | Target |
|------|--------|
| `prefix` `1` | Commander |
| `prefix` `2` | Adjudicator |
| `prefix` `3` | Cartographer |
| `prefix` `4` | Psyche |

**Other quick aliases:**

| Alias | Action |
|-------|--------|
| `vc` | Open COCKPIT.md in nvim |
| `vs` | Open Intention Compass in nvim |

---

## 2. AeroSpace (Window Management)

i3-like tiling. All bindings use `Alt` (Option).

### Workspace Switching

| Keys | Workspace | Zone |
|------|-----------|------|
| `Alt+1` | Terminal | A (left) |
| `Alt+2` | Cockpit | A (left) |
| `Alt+3` | Editor | A (left) |
| `Alt+4` | Browser | B (center) |
| `Alt+5` | Obsidian | B (center) |
| `Alt+6` | PM (Linear/Notion) | B (center) |
| `Alt+7` | Comms | C (right) |
| `Alt+8` | Monitor | C (right) |
| `Alt+9` | Dashboard (Emacs) | C (right) |

### Ultrawide Zone Map (5120x1440)

```
┌──────────────────┬──────────────────┬──────────────────┐
│   ZONE A (left)  │  ZONE B (center) │  ZONE C (right)  │
│   ~1700px        │  ~1700px         │  ~1700px         │
│  1=Terminal       │  4=Browser       │  7=Comms         │
│  2=Cockpit        │  5=Obsidian      │  8=Monitor       │
│  3=Editor         │  6=PM            │  9=Dashboard     │
└──────────────────┴──────────────────┴──────────────────┘
```

### Focus & Movement

| Keys | Action |
|------|--------|
| `Alt+h/j/k/l` | Focus left/down/up/right |
| `Alt+Shift+h/j/k/l` | Move window left/down/up/right |
| `Alt+Shift+1-9` | Move window to workspace N |

### Layout

| Keys | Action |
|------|--------|
| `Alt+Enter` | New Ghostty window |
| `Alt+f` | Fullscreen toggle |
| `Alt+Shift+Space` | Float/tile toggle |
| `Alt+/` | Toggle tiles horizontal/vertical |
| `Alt+,` | Toggle accordion horizontal/vertical |
| `Alt+-` | Shrink window (-50) |
| `Alt+=` | Grow window (+50) |
| `Alt+Shift+c` | Reload AeroSpace config |

### Window Borders (JankyBorders)

- Active: Catppuccin blue (`#89b4fa`), 3px round
- Inactive: Catppuccin surface (`#45475a`)
- Runs as brew service, no interaction needed

---

## 3. tmux (Session & Pane Management)

**Prefix: `Ctrl+Space`** (abbreviated `pfx` below)

### Splits & Windows

| Keys | Action |
|------|--------|
| `pfx` `\|` | Split horizontal (side by side) |
| `pfx` `-` | Split vertical (top/bottom) |
| `pfx` `c` | New window |

All splits inherit current working directory.

### Pane Navigation (vim-tmux-navigator)

Works identically inside vim/nvim and bare shell:

| Keys | Action |
|------|--------|
| `Ctrl+h` | Pane left |
| `Ctrl+j` | Pane down |
| `Ctrl+k` | Pane up |
| `Ctrl+l` | Pane right |

### Pane Resize

| Keys | Action |
|------|--------|
| `Alt+Up` | Grow up 2 |
| `Alt+Down` | Grow down 2 |
| `Alt+Left` | Grow left 2 |
| `Alt+Right` | Grow right 2 |

### Session Switching

| Keys | Action |
|------|--------|
| `pfx` `f` | sesh + fzf session picker |
| `Ctrl+f` | Instant session widget (from shell) |
| `t` | Fuzzy session finder function (from shell) |

### Copy Mode & Text Extraction

| Keys | Action |
|------|--------|
| `pfx` `[` | Enter copy mode (vim keys: hjkl, /, ?, n, N, v, y) |
| `pfx` `F` | **Fingers** -- hint labels on all copyable text, tap letter to yank |
| `pfx` `Tab` | **Extrakto** -- fzf popup over pane output, search/select URLs, paths, hashes |

### Utilities

| Keys | Action |
|------|--------|
| `pfx` `*` | **Cowboy** -- SIGKILL the foreground process (kill hung agents) |
| `pfx` `r` | Reload tmux config |
| `pfx` `I` | Install/update TPM plugins |

### Session Persistence

- **Resurrect**: `pfx+Ctrl+s` save, `pfx+Ctrl+r` restore
- **Continuum**: Auto-saves every 15 minutes, auto-restores on tmux start
- Captures pane contents and nvim sessions

### Preconfigured Sessions (sesh.toml)

| Session | Path | Purpose |
|---------|------|---------|
| `constellation` | ~/Desktop/syncrescendence | 4-pane cockpit (auto-launches via cockpit.sh) |
| `sync-edit` | ~/Desktop/syncrescendence | Editing session (bare) |
| `scratch` | ~/Desktop | Throwaway |

---

## 4. Ghostty (Terminal)

### Visual

| Setting | Value |
|---------|-------|
| Font | Liga SFMono Nerd Font, 13pt, Light |
| Theme | Catppuccin Mocha |
| Opacity | 70% (most transparent in the stack) |
| Blur | radius 20 |
| Scrollback | 100MB |
| Copy | Select text = auto-copies to clipboard |

### Text Editing Keys

| Keys | Action |
|------|--------|
| `Alt+Left` | Word jump backward |
| `Alt+Right` | Word jump forward |
| `Alt+Backspace` | Delete word backward |
| `Cmd+Left` | Jump to line start |
| `Cmd+Right` | Jump to line end |
| `Cmd+Backspace` | Kill to line start |

### Shell Integration

- Prompt marking (jump between commands)
- Cursor styling per mode
- Directory tracking
- Window title = current directory

### Option Key

`macos-option-as-alt = true` -- Option sends Esc+ for TUI compatibility (btop, yazi, zellij).

---

## 5. Neovim / LazyVim (Prose Engine)

Launch: `nvim <file>` from any pane.

Theme: Catppuccin Mocha, transparent background. Leader: `Space`.

### Writing Mode

| Keys | Action |
|------|--------|
| `Space` `z` | Zen mode (90-col centered, dim unfocused, hide tmux bar) |

### Agent Pipe (send text to cockpit panes)

**Visual mode** (select text first):

| Keys | Target |
|------|--------|
| `Space` `a` `c` | Send selection to Commander (pane 1) |
| `Space` `a` `a` | Send selection to Adjudicator (pane 2) |
| `Space` `a` `g` | Send selection to Cartographer (pane 3) |
| `Space` `a` `p` | Send selection to Psyche (pane 4) |

**Normal mode** (sends entire buffer):

| Keys | Target |
|------|--------|
| `Space` `a` `C` | Buffer to Commander |
| `Space` `a` `A` | Buffer to Adjudicator |
| `Space` `a` `G` | Buffer to Cartographer |
| `Space` `a` `P` | Buffer to Psyche |

### Markdown

- `render-markdown.nvim`: In-buffer rendering with heading icons, bullets
- `MarkdownPreview`: Browser preview (uses Bun)

---

## 6. Doom Emacs (Observation Layer)

**Build: emacs-mac (Yamamoto port, v29.4)** -- replaces emacs-plus@30. The mac-port provides pixel-smooth scrolling, native image rendering, and better macOS integration (native fullscreen, proper trackpad support). Same Doom config, same keybindings.

Launch: `open -a Emacs` or `emacs`

**Role: READ-ONLY dashboard.** Files in `00-ORCHESTRATION/state/` auto-lock to read-only. Evil mode = vim keybindings everywhere. Leader: `SPC`.

### Dashboard Keybindings (SPC d prefix)

| Keys | Opens |
|------|-------|
| `SPC d s` | COCKPIT.md (constellation state) |
| `SPC d i` | Intention Compass |
| `SPC d e` | Execution Staging Log |
| `SPC d l` | Session Log |
| `SPC d t` | Terminal Stack Config |
| `SPC d a` | Org Agenda |
| `SPC d r` | Refresh current buffer |

### Core Navigation

| Keys | Action |
|------|--------|
| `SPC .` | Find file |
| `SPC ,` | Switch buffer |
| `SPC /` | Search project (ripgrep) |
| `SPC SPC` | Find file in project |

### Git

| Keys | Action |
|------|--------|
| `SPC g g` | Magit status |

### Windows

| Keys | Action |
|------|--------|
| `SPC w v` | Split vertical |
| `SPC w s` | Split horizontal |
| `SPC w d` | Close window |
| `SPC w w` | Cycle windows |

### Modes

| Keys | Action |
|------|--------|
| `SPC t z` | Zen mode (olivetti centered writing, 100 cols) |
| `SPC o p` | Treemacs (file tree sidebar) |
| `SPC o t` | vterm (embedded terminal) |

### Visual

| Setting | Value |
|---------|-------|
| Theme | Catppuccin Mocha, black surfaces (#000000) |
| Font | Liga SFMono Nerd Font 13pt Light |
| Opacity | 70% |
| Line numbers | Relative |
| Org directory | ~/Desktop/syncrescendence/ |

---

## 7. Shell Tools (Modern CLI)

All aliases defined in `~/.zshrc`. Every tool uses Catppuccin Mocha theme.

### Replacement Table

| Old | New | Alias | What It Does |
|-----|-----|-------|-------------|
| `ls` | eza | `ls` | Icons, git status, group dirs first |
| `ls -la` | eza | `ll` | Long format + git + headers |
| `ls -la` (all) | eza | `la` | Long + all hidden files |
| `tree` | eza | `lt` | Tree view, 2 levels deep |
| `cat` | bat | `cat` | Syntax highlighting, Catppuccin Mocha |
| `cd` | zoxide | `z` | Frecency-based smart jump |
| `grep` | ripgrep | `rg` | Fast regex search |
| `find` | fd | `fd` | Simple file finder |
| `top` | btop | `top` | Visual system monitor (mouse, braille) |
| `ps` | procs | `ps` | Process tree with ports |
| `du` | dust | `du` | Disk usage tree |
| `df` | duf | `df` | Visual disk free |
| `man` | tldr | `help` | Quick reference (not full man page) |
| `curl` | httpie | `http` / `https` | API requests with syntax highlighting |

### TUI Launchers

| Alias | Tool | What It Does |
|-------|------|-------------|
| `fm` | yazi | File manager (image previews via chafa, vim keys) |
| `lg` | lazygit | Git TUI (delta diffs, staging, branches) |
| `md` | glow | Render markdown in terminal |
| `loc` | tokei | Code statistics by language |
| `json` | fx | Interactive JSON viewer (pipe API output) |
| `zj` | zellij | Secondary multiplexer (legacy) |

### Lifestyle Layer

Ambient information and media tools for non-work context switching.

| Alias | Tool | What It Does |
|-------|------|-------------|
| `fetch` | fastfetch | System info display (hardware, OS, uptime, resources) |
| -- | chafa | Image-to-terminal renderer (used by yazi for image previews) |
| `stocks` | ticker | Live stock/crypto prices (config: `~/.ticker.yaml` for watchlist) |
| `hn` | circumflex (`clx`) | Hacker News TUI (browse, read, comment) |
| `play` | mpv | Media player (CLI: `mpv --vo=tct` for terminal video playback) |
| `dl` | yt-dlp | Video/audio downloader (YouTube, etc.) |
| `weather` | curl wttr.in | Inline weather forecast (`curl -s wttr.in`) |

### Search & History

| Keys | Tool | What It Does |
|------|------|-------------|
| `Ctrl+R` | atuin | Visual history search (SQLite-backed, synced) |
| `Ctrl+T` | fzf | Fuzzy file search |
| `Alt+C` | fzf | Fuzzy cd into subdirectory |

### Shell Intelligence

| Feature | Tool |
|---------|------|
| Autosuggestions | zsh-autosuggestions (gray inline completions, accept with Right arrow) |
| Syntax highlighting | zsh-syntax-highlighting (valid=green, invalid=red) |
| Env per directory | direnv (auto-loads `.envrc` on cd) |
| Runtime management | mise (replaces nvm/pyenv) |
| Prompt | Starship (Catppuccin Mocha palette, lean single-line) |

---

## 8. Starship Prompt

**Replaced Powerlevel10k.** Starship is a cross-shell, Rust-based prompt with zero startup overhead and no instant-prompt complexity.

### Config

`~/.config/starship.toml` -- Catppuccin Mocha palette.

### Layout

Lean single-line format:

```
directory git-branch git-status cmd-duration time $
```

### What Shows

| Segment | When |
|---------|------|
| Directory | Always (truncated to 3 components) |
| Git branch | Inside a git repo |
| Git status | Dirty/staged/untracked indicators |
| Exec time | Commands taking >2 seconds |
| Time | Current time (right-aligned) |

### No Instant Prompt

Unlike P10k, Starship has no instant prompt mechanism -- it is fast enough natively that none is needed. No `.p10k.zsh` sourcing, no cache files.

---

## 9. Voice Layer

Voice input/output scripts in `~/bin/`, wired to the cockpit for hands-free agent interaction.

### Scripts

| Script / Alias | What It Does |
|----------------|-------------|
| `stt` / `listen` | Record from mic via sox, transcribe via whisper-cli (local Whisper model). Outputs plain text to stdout. |
| `tts` / `speak` | Synthesize speech via piper with selectable voice profile. Reads from stdin or argument. |
| `voice-pipe` / `vp` | Record, transcribe, then send the transcribed text to a target cockpit tmux pane. Usage: `vp 1` (send to Commander), `vp 2` (Adjudicator), etc. |

### DSP Voice Profiles

Stored at `~/.config/voice/`. Each profile tunes piper voice parameters (speed, pitch, model) per cockpit role:

| Profile | Role | Character |
|---------|------|-----------|
| `commander` | CMD (pane 1) | Authoritative, measured pace |
| `adjudicator` | ADJ (pane 2) | Precise, clipped delivery |
| `cartographer` | CART (pane 3) | Exploratory, wider dynamic range |
| `psyche` | PSY (pane 4) | Contemplative, slower cadence |

### Workflow

1. Press-to-record: `listen` captures mic input until silence/keypress
2. Whisper transcribes locally (no network round-trip)
3. `vp <pane>` combines both steps and injects the text into the target tmux pane as if typed

---

## 10. Session Management (sesh + zoxide)

### From Shell

| Command/Keys | Action |
|-------------|--------|
| `cockpit` | Connect to constellation session (4-pane cockpit) |
| `t` | Fuzzy session finder (sesh list + fzf) |
| `Ctrl+f` | Instant session switching widget |
| `z <partial>` | Smart directory jump (zoxide) |
| `z -` | Jump to previous directory |
| `zi` | Interactive zoxide picker (fzf) |

### From tmux

| Keys | Action |
|------|--------|
| `pfx` `f` | sesh + fzf session picker (all sessions + zoxide dirs) |
| `pfx` `d` | Detach from current session |
| `pfx` `$` | Rename session |
| `pfx` `s` | List sessions |

### Available Sessions

| Name | Path | Notes |
|------|------|-------|
| `constellation` | syncrescendence | Auto-creates 4-pane cockpit |
| `sync-edit` | syncrescendence | Clean editing session |
| `scratch` | ~/Desktop | Disposable |

---

## 11. Notifications

### Long Command Alert (>30 seconds)

Any shell command running longer than 30 seconds fires a macOS notification on completion via `terminal-notifier`. Shows elapsed time and truncated command. Default sound.

No configuration needed -- baked into `.zshrc` preexec/precmd hooks.

### tmux Background Pane Alerts (tmux-notify)

When a command finishes in a **non-focused** tmux pane, fires macOS notification:
- Message: `Pane #P: done`
- Delay: 10 second sleep before notification (debounce rapid output)
- Verbose mode: on

### Claude Code Hooks

| Event | Notification |
|-------|-------------|
| Session stop | `terminal-notifier`: "Session stopped" |
| Notification | `terminal-notifier` with Basso sound |

---

## 12. Launchd Services (Always-On)

All user-level at `~/Library/LaunchAgents/`.

### Health Check

```bash
launchctl list | grep syncrescendence     # List all watchers
tail -f /tmp/syncrescendence-watch-commander.log   # Stream watcher log
launchctl kickstart -k gui/$(id -u)/com.syncrescendence.watch-commander  # Restart
```

### Running Services

| Service | Label | Log |
|---------|-------|-----|
| watch-commander | com.syncrescendence.watch-commander | /tmp/syncrescendence-watch-commander.log |
| watch-adjudicator | com.syncrescendence.watch-adjudicator | /tmp/syncrescendence-watch-adjudicator.log |
| watch-cartographer | com.syncrescendence.watch-cartographer | /tmp/syncrescendence-watch-cartographer.log |
| watch-ajna | com.syncrescendence.watch-ajna | /tmp/syncrescendence-watch-ajna.log |
| watch-psyche | com.syncrescendence.watch-psyche | /tmp/syncrescendence-watch-psyche.log |
| watch-canon | com.syncrescendence.watch-canon | /tmp/syncrescendence-watch-canon.log |
| OpenClaw Gateway | ai.openclaw.gateway | ~/.openclaw/logs/gateway.log (port 18789) |
| JankyBorders | homebrew.mxcl.borders | brew service |

---

## 13. Config File Locations

Quick reference for when something breaks.

| File | Controls |
|------|----------|
| `~/.tmux.conf` | tmux (prefix, panes, plugins, cockpit bindings) |
| `~/.zshrc` | Shell (aliases, hooks, tools, session functions) |
| `~/.config/starship.toml` | Prompt theme (Catppuccin Mocha palette) |
| `~/.config/ghostty/config` | Terminal (font, theme, opacity, keybinds) |
| `~/.config/sesh/sesh.toml` | Session definitions (constellation, sync-edit, scratch) |
| `~/.aerospace.toml` | Window manager (workspaces, tiling, keys) |
| `~/.config/borders/bordersrc` | Window border colors |
| `~/.config/doom/config.el` | Emacs dashboard (theme, keybindings, org) |
| `~/.config/doom/init.el` | Doom modules |
| `~/.config/nvim/lua/plugins/` | Neovim plugins (agent-pipe, prose, colorscheme) |
| `~/.config/btop/btop.conf` | System monitor |
| `~/.config/yazi/yazi.toml` | File manager |
| `~/.config/atuin/config.toml` | Shell history |
| `~/.config/voice/` | Voice DSP profiles (commander, adjudicator, cartographer, psyche) |
| `~/.ticker.yaml` | Stock/crypto watchlist for ticker |
| `~/bin/stt` | Speech-to-text script (whisper-cli) |
| `~/bin/tts` | Text-to-speech script (piper) |
| `~/bin/voice-pipe` | Voice-to-cockpit-pane pipeline |
| `~/.claude.json` | Claude Code MCP servers |
| `~/.claude/settings.json` | Claude Code hooks |
| `~/.gitconfig` | Git + delta integration |

---

## 14. Emergency Procedures

### Hung Agent (tmux pane frozen)

1. `pfx` `*` (Cowboy -- SIGKILLs foreground process)
2. If pane itself is dead: `pfx` then type `:kill-pane`

### tmux Server Crash

```bash
tmux kill-server          # Nuclear reset
cockpit                   # Relaunch (continuum restores last save)
```

### Plugins Missing (no catppuccin theme, no fingers, etc.)

```bash
# Inside tmux:
pfx + I                   # TPM installs all plugins from .tmux.conf
pfx + r                   # Reload config
```

### AeroSpace Not Tiling

```bash
Alt+Shift+c               # Reload aerospace config
# OR
aerospace reload-config   # From terminal
```

### Doom Emacs Broken

```bash
~/.config/emacs/bin/doom sync       # Resync packages
~/.config/emacs/bin/doom doctor     # Diagnose issues
~/.config/emacs/bin/doom upgrade    # Upgrade packages
```

### LazyVim Broken

```bash
nvim --headless "+Lazy! sync" +qa   # Headless plugin sync
```

### Reset Shell

```bash
source ~/.zshrc                     # Reload all aliases and tools
```

---

## 15. Cheat Sheet (One-Pager)

```
COCKPIT LAUNCH          cockpit
PANE SWITCH             pfx+1/2/3/4 (Cmd/Adj/Cart/Psy)
PANE NAV                Ctrl+h/j/k/l
WORKSPACE               Alt+1-9
FOCUS WINDOW            Alt+h/j/k/l
MOVE WINDOW             Alt+Shift+h/j/k/l
NEW TERMINAL            Alt+Enter
FULLSCREEN              Alt+f
SESSION PICK            pfx+f  OR  Ctrl+f  OR  t
COPY HINT               pfx+F (Fingers)
FUZZY EXTRACT           pfx+Tab (Extrakto)
KILL HUNG               pfx+*
HISTORY SEARCH          Ctrl+R (atuin)
FILE SEARCH             Ctrl+T (fzf)
SMART CD                z <partial>
GIT TUI                 lg
FILE MANAGER            fm
SYSTEM MONITOR          top (btop)
AGENT PIPE (vim)        SPC a c/a/g/p (visual selection)
ZEN MODE (vim)          SPC z
ZEN MODE (emacs)        SPC t z
DASHBOARD (emacs)       SPC d s/i/e/l/t/a/r
MAGIT                   SPC g g
VOICE INPUT             listen / vp <pane>
VOICE OUTPUT            speak
SYSTEM INFO             fetch
STOCKS                  stocks
HACKER NEWS             hn
WEATHER                 weather
```
