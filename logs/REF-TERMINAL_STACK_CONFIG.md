# REF-TERMINAL_STACK_CONFIG.md
## Terminal Stack Configuration Reference

**Version**: 1.0.0
**Created**: 2026-02-15
**Author**: Commander (Claude Opus 4.6)
**Purpose**: Practical terminal stack reference documenting what IS configured on each machine.
**Lineage**: Successor to deleted `orchestration/TERMINAL-STACK-CONFIG.md` (commit `8b8f965`). Companion to `engine/REF-SOVEREIGN_COCKPIT_MANIFEST.md` (verbatim config dump) and `orchestration/DEPLOYMENT-PLAYBOOK.md` (full deployment reference).

> This document is a quick-reference index. For verbatim config contents, see `REF-SOVEREIGN_COCKPIT_MANIFEST.md`. For installation procedures, see `DEPLOYMENT-PLAYBOOK.md`.

---

## Machine Inventory

| Machine | Chip | macOS | Role | Hostname | Home Dir |
|---------|------|-------|------|----------|----------|
| **Mac mini** (M1) | Apple M1 | TBD | HQ, Cockpit host, always-on | TBD | `/Users/home/` |
| **MacBook Air** (M4) | Apple M4 (arm64) | 26.3 (25D122) | Field ops, Ajna home, Commander secondary | Lisas-MacBook-Air | `/Users/system/` |

---

## 1. Terminal Emulators

### Ghostty (Primary)

| Setting | Mac mini (HQ) | MacBook Air (Field) |
|---------|--------------|---------------------|
| Config path | `~/.config/ghostty/config` | `~/.config/ghostty/config` |
| Font | Liga SFMono Nerd Font, Light, 13pt | SF Mono, Light, 13pt |
| Background | `000000` (pure black, OLED) | `1e1e2e` (Catppuccin base) |
| Opacity | 70% | 65% |
| Blur radius | 20 | 10 |
| Scrollback | 100,000,000 lines | Default |
| Titlebar | Hidden | Default |
| Shell integration | zsh (cursor, sudo, title) | Not set |
| Keybindings | Natural text editing (Cmd+Arrow, Opt+Arrow) | Not set |

**MBA gap**: MBA Ghostty config is minimal (47 lines) vs HQ (93 lines). Missing: scrollback-limit, macos-titlebar-style, shell-integration, natural text editing keybindings, copy-on-select.

### Backup Terminals

| Terminal | Mac mini | MBA | Theme | Font |
|----------|---------|-----|-------|------|
| **iTerm2** | Configured (Catppuccin Mocha import) | TBD | Catppuccin Mocha | Liga SFMono Nerd Font 13pt |
| **Terminal.app** | Configured (Catppuccin profile) | TBD | Catppuccin Mocha | Liga SFMono Nerd Font 13pt |

---

## 2. Shell (Zsh)

### Prompt

| Setting | Mac mini | MBA |
|---------|---------|-----|
| Prompt engine | **Starship** 1.24.2 | **Starship** 1.24.2 |
| Config | `~/.config/starship.toml` | `~/.config/starship.toml` |
| Theme | Catppuccin Mocha palette | Catppuccin Mocha palette |
| Format | Lean single-line (dir + git + status) | Lean single-line (dir + git + status) |
| Previous | Powerlevel10k (removed per DEC-LIFESTYLE-001) | N/A |

### Shell Plugins & Intelligence Layer

| Component | Mac mini | MBA |
|-----------|---------|-----|
| **zsh-autosuggestions** | Installed (v0.7.1 Homebrew) | Installed (v0.7.1 Homebrew) |
| **zsh-syntax-highlighting** | Installed (v0.8.0 Homebrew) | Installed (v0.8.0 Homebrew) |
| **zoxide** | Installed | Installed |
| **fzf** | Installed | Installed |
| **Atuin** | Installed (config at `~/.config/atuin/config.toml`) | Installed (config at `~/.config/atuin/config.toml`) |
| **direnv** | Installed | **NOT INSTALLED** |
| **mise** | Installed | **NOT INSTALLED** |
| **nvm** | Legacy, in .zshrc | **NOT INSTALLED** |

### FZF Colors (Catppuccin Mocha)

Both machines should use:
```bash
export FZF_DEFAULT_OPTS=" \
--color=bg+:#313244,bg:#1e1e2e,spinner:#f5e0dc,hl:#f38ba8 \
--color=fg:#cdd6f4,header:#f38ba8,info:#cba6f7,pointer:#f5e0dc \
--color=marker:#b4befe,fg+:#cdd6f4,prompt:#cba6f7,hl+:#f38ba8 \
--color=selected-bg:#45475a \
--multi"
```

**MBA status**: TBD -- need to verify if FZF colors are set in MBA `.zshrc`.

---

## 3. Multiplexer (tmux)

| Setting | Mac mini (HQ) | MacBook Air (Field) |
|---------|--------------|---------------------|
| Version | tmux 3.6a | tmux 3.6a |
| Config | `~/.tmux.conf` | `~/.tmux.conf` |
| Prefix | `Ctrl+Space` | `Ctrl+a` |
| History | 100,000 lines | 50,000 lines |
| Base index | 1 | 1 |
| Mouse | On | On |
| Theme | Catppuccin (via TPM plugin) | Catppuccin Mocha (manual, inline) |
| Pane nav | Ctrl+hjkl (vim-tmux-navigator) | hjkl (bind h/j/k/l) |
| TPM plugins | 11 (catppuccin, resurrect, continuum, yank, fingers, extrakto, cowboy, notify, sensible, tpm, vim-tmux-navigator) | **NONE** (no TPM) |
| sesh | v2.22.0, config at `~/.config/sesh/sesh.toml` | Installed, **no config** (`~/.config/sesh/sesh.toml` missing) |
| Cockpit session | `constellation` (4x2 grid, 8 panes) | N/A (single-pane or 2-pane layout) |

**MBA tmux notes**:
- Prefix is `Ctrl+a` (differs from HQ `Ctrl+Space`)
- No TPM, no plugins -- purely manual Catppuccin status bar
- No `resurrect` / `continuum` for session persistence
- No `sesh.toml` configuration file

---

## 4. Font & Theme

### Font

| Setting | Mac mini | MBA |
|---------|---------|-----|
| Family | **Liga SFMono Nerd Font** (Ligaturized) | **SF Mono** (system, no Nerd Font) |
| Ligatures | Enabled (`calt`, `liga`, `dlig`) | Not applicable |
| Source | `shaunsingh/SFMono-Nerd-Font-Ligaturized` tap | System font |
| Weights | 12 (Light through Heavy, with italics) | System default |

**MBA gap**: Liga SFMono Nerd Font is NOT installed on MBA. This means Nerd Font icons (used by eza, starship, yazi, etc.) will render as missing glyphs. Install via:
```bash
brew tap shaunsingh/SFMono-Nerd-Font-Ligaturized
brew install --cask font-sf-mono-nerd-font-ligaturized
```

### Visual Theme: Catppuccin Mocha

Consistent across both machines where configured:

| Surface | Mac mini | MBA |
|---------|---------|-----|
| Ghostty | Catppuccin Mocha | Catppuccin Mocha |
| Starship | Catppuccin Mocha | Catppuccin Mocha |
| tmux | Catppuccin Mocha (TPM) | Catppuccin Mocha (inline) |
| bat | Catppuccin Mocha theme | Catppuccin Mocha theme (`~/.config/bat/themes/`) |
| btop | Catppuccin Mocha | Catppuccin Mocha (`~/.config/btop/btop.conf`) |
| lazygit | Catppuccin Mocha | Catppuccin Mocha (`~/Library/Application Support/lazygit/config.yml`) |
| fzf | Catppuccin Mocha (env var) | TBD |
| git-delta | Catppuccin Mocha | TBD |
| fastfetch | Catppuccin Mocha | TBD (fastfetch installed) |
| Neovim | Catppuccin Mocha (transparent) | TBD (nvim installed, LazyVim present) |
| yazi | Catppuccin Mocha | **NOT INSTALLED** (no `~/.config/yazi/`) |
| Doom Emacs | Catppuccin Mocha | **NOT INSTALLED** (no Emacs) |

---

## 5. CLI Tools Manifest

### Modern CLI Replacements

| Tool | Replaces | Alias | Mac mini | MBA |
|------|----------|-------|---------|-----|
| **eza** | `ls` | `ls`, `ll`, `la`, `tree` | Installed | Installed |
| **bat** | `cat` | `cat` | Installed | Installed |
| **rg** (ripgrep) | `grep` | `grep` | Installed | Installed |
| **fd** | `find` | `find` | Installed | Installed |
| **dust** | `du` | `du` | Installed | Installed |
| **duf** | `df` | `df` | Installed | Installed |
| **procs** | `ps` | `ps` | Installed | Installed |
| **tldr** | `man` | `help` | Installed | TBD |
| **httpie** | `curl` | `http`/`https` | Installed | TBD |
| **tokei** | `cloc` | — | Installed | TBD |

### TUI Applications

| Tool | Purpose | Mac mini | MBA |
|------|---------|---------|-----|
| **yazi** | File manager | Installed + configured | Installed, **no config** |
| **btop** | System monitor | Installed + configured | Installed + configured |
| **lazygit** | Git interface | Installed + configured | Installed + configured |
| **glow** | Markdown renderer | Installed | Installed |
| **fx** | JSON viewer | Installed | **NOT INSTALLED** |
| **fastfetch** | System info | Installed | Installed |
| **chafa** | Image renderer | Installed | **NOT INSTALLED** |
| **ticker** | Stock/crypto ticker | Installed | **NOT INSTALLED** |
| **clx** (circumflex) | Hacker News TUI | Installed | TBD |
| **mpv** | Media player | Installed | **NOT INSTALLED** |
| **yt-dlp** | Video downloader | Installed | **NOT INSTALLED** |

### CLI Agents

| Agent | Runtime | Mac mini | MBA |
|-------|---------|---------|-----|
| **Claude Code** | Node | Installed (v2.1.37+) | Installed (`~/.local/bin/claude`) |
| **Codex CLI** | Node | Installed (v0.98.0) | Installed (`~/.local/bin/codex`) |
| **Gemini CLI** | Homebrew | Installed (v0.27.3+) | Installed (`/opt/homebrew/bin/gemini`) |
| **OpenClaw** | Node | Installed | Installed (`/opt/homebrew/bin/openclaw`) |

### Development Stack

| Tool | Mac mini | MBA |
|------|---------|-----|
| **Bun** | 1.2.13+ | 1.3.9 |
| **Node.js** | v24.13.0 (nvm) | v25.6.1 (Homebrew direct) |
| **Python** | 3.13.5 (miniconda3) | 3.14.3 (Homebrew) |
| **Rust** | 1.93.0 (Homebrew) | TBD |

---

## 6. Editor Stack

| Layer | Tool | Mac mini | MBA |
|-------|------|---------|-----|
| **Prose Engine** | Neovim + LazyVim | NVIM v0.11.6, 37 plugins, Agent Pipe | nvim installed, LazyVim starter template, **no Agent Pipe** |
| **Dashboard** | Doom Emacs (emacs-mac) | Configured (138 packages), org-mode dashboard | **NOT INSTALLED** (no Emacs, no Doom) |
| **Simulator** | Cursor | Available | TBD |

### Neovim Plugins (Mac mini, significant)

- `zen-mode.nvim` + `twilight.nvim` + `render-markdown.nvim` (writing)
- `agent-pipe.lua` (custom: send selection to tmux pane for agents)
- Catppuccin Mocha theme (transparent background)

**MBA gap**: Neovim is installed with LazyVim but lacks the custom Agent Pipe plugin and writing-focused plugin configuration from the Mac mini.

---

## 7. Voice Layer

| Component | Mac mini | MBA |
|-----------|---------|-----|
| **whisper-cli** | v1.8.3 (Metal) | Installed (`/opt/homebrew/bin/whisper-cli`) |
| Whisper models | ggml-base.en, ggml-small.en at `~/.local/share/whisper-models/` | TBD |
| **Piper TTS** | Installed (pip3, v1.3.0) | **NOT INSTALLED** |
| Piper voices | 3 voices at `~/.local/share/piper-voices/` | N/A |
| DSP Personas | 4 sox profiles at `~/.config/voice/` | N/A |
| `~/bin/stt` | Pipeline script READY | **NOT PRESENT** |
| `~/bin/tts` | Pipeline script READY | **NOT PRESENT** |
| `~/bin/voice-pipe` | Pipeline script READY | **NOT PRESENT** |

---

## 8. macOS Power Apps

| App | Mac mini | MBA |
|-----|---------|-----|
| **Raycast** | v1.104.5+ | Installed |
| **AeroSpace** | v0.20.2-Beta | **NOT INSTALLED** |
| **JankyBorders** | v1.8.4 (brew service) | **NOT INSTALLED** |
| **Karabiner-Elements** | Installed (Hyper Key: CapsLock) | Installed |
| **Ice** | Installed | Installed |

**MBA note**: AeroSpace and JankyBorders are Mac mini-specific (ultrawide tiling). MBA uses native macOS window management. Karabiner-Elements Hyper Key config may need verification on MBA.

---

## 9. Always-On Services (launchd)

### Mac mini (HQ) -- 13 services

| Service | Label | Status |
|---------|-------|--------|
| watch-commander | `com.syncrescendence.watch-commander` | ACTIVE |
| watch-adjudicator | `com.syncrescendence.watch-adjudicator` | ACTIVE |
| watch-cartographer | `com.syncrescendence.watch-cartographer` | ACTIVE |
| watch-ajna | `com.syncrescendence.watch-ajna` | ACTIVE |
| watch-psyche | `com.syncrescendence.watch-psyche` | ACTIVE |
| watch-canon | `com.syncrescendence.watch-canon` | ACTIVE |
| Emacs Server | `com.syncrescendence.emacs-server` | ACTIVE |
| OpenClaw Gateway | `ai.openclaw.gateway` | ACTIVE |
| Chroma Server | `com.syncrescendence.chroma-server` | ACTIVE |
| Webhook Receiver | `com.syncrescendence.webhook-receiver` | ACTIVE |
| Corpus Health | `com.syncrescendence.corpus-health` | ACTIVE |
| QMD Update | `com.syncrescendence.qmd-update` | ACTIVE |
| Watchdog | `com.syncrescendence.watchdog` | ACTIVE |

### MacBook Air (Field) -- 8 services (verified via `launchctl list`)

| Service | Label | PID | Status |
|---------|-------|-----|--------|
| watch-commander | `com.syncrescendence.watch-commander` | 79255 | RUNNING (exit 1) |
| watch-ajna | `com.syncrescendence.watch-ajna` | 31668 | RUNNING (exit 1) |
| watch-adjudicator | `com.syncrescendence.watch-adjudicator` | 44689 | LOADED (exit 0) |
| watch-cartographer | `com.syncrescendence.watch-cartographer` | 44708 | LOADED (exit 0) |
| watch-canon | `com.syncrescendence.watch-canon` | 803 | LOADED (exit 0) |
| skill-sync | `com.syncrescendence.skill-sync` | - | LOADED (exit 0) |
| git-sync | `com.syncrescendence.git-sync` | - | LOADED (exit 0) |
| OpenClaw Gateway | `ai.openclaw.gateway` | 16614 | RUNNING (exit 1) |

**MBA notes**:
- Adjudicator and Cartographer watchers loaded but not actively running (exit 0 = idle)
- Commander and Ajna watchers actively running
- No Chroma, Webhook, Corpus Health, QMD, Watchdog, or Emacs services on MBA
- git-sync and skill-sync are MBA-specific services not on Mac mini

---

## 10. Config File Locations (Quick Reference)

| File | Purpose | Mac mini | MBA |
|------|---------|---------|-----|
| `~/.zshrc` | Shell config | Present | Present |
| `~/.config/starship.toml` | Starship prompt | Present | Present |
| `~/.config/ghostty/config` | Ghostty terminal | Present (93 lines) | Present (47 lines) |
| `~/.tmux.conf` | tmux multiplexer | Present (with TPM) | Present (minimal, no TPM) |
| `~/.config/sesh/sesh.toml` | sesh session mgr | Present | **MISSING** |
| `~/.config/btop/btop.conf` | btop monitor | Present | Present |
| `~/.config/bat/themes/` | bat theme | Present | Present |
| `~/.config/atuin/config.toml` | Atuin history | Present | Present |
| `~/.config/yazi/yazi.toml` | yazi file mgr | Present | **MISSING** |
| `~/.config/nvim/` | Neovim | Present (LazyVim + plugins) | Present (LazyVim starter) |
| `~/.config/doom/` | Doom Emacs | Present (init.el, config.el, packages.el) | **MISSING** |
| `~/.gitconfig` | Git + delta | Present | TBD |
| `~/.claude/settings.json` | Claude Code hooks | Present | Present |
| `~/.openclaw/openclaw.json` | OpenClaw config | Present (GPT-5.3-codex) | Present (Kimi K2.5 via NVIDIA) |
| `~/Library/Application Support/lazygit/config.yml` | lazygit | Present | Present |
| `~/.config/glow/glow.yml` | glow renderer | Present | TBD |
| `~/.config/voice/` | DSP personas | Present (4 profiles) | **MISSING** |

---

## 11. Cockpit Layout (Mac mini Only)

The 4x2 cockpit grid runs on the Mac mini's 5120x1440 ultrawide. It is NOT replicated on MBA.

```
┌──────────┬──────────┬──────────┬──────────┐
│  PSYCHE  │ COMMANDER│ADJUDICATOR│CARTOGR. │  48 rows (agents)
│ OpenClaw │Claude Code│ Codex CLI│Gemini CLI│
│ pane 1   │ pane 3   │ pane 5   │ pane 7   │
├──────────┼──────────┼──────────┼──────────┤
│  nvim    │  nvim    │  nvim    │  nvim    │  15 rows (editors)
│ pane 2   │ pane 4   │ pane 6   │ pane 8   │
└──────────┴──────────┴──────────┴──────────┘

Launch: cockpit / cockpit --launch / cockpit --kill
Script: orchestration/scripts/cockpit.sh
```

MBA operates in single-pane or 2-pane mode -- no cockpit geometry needed.

---

## 12. Aliases (Canonical)

These should be in `~/.zshrc` on both machines:

```bash
# Modern CLI
alias ls='eza --icons --group-directories-first'
alias la='eza --icons --group-directories-first -la'
alias lt='eza --icons --tree --level=2'
alias cat='bat --style=plain'
alias grep='rg'
alias find='fd'
alias du='dust'
alias df='duf'
alias ps='procs'
alias help='tldr'

# TUI
alias y='yazi'
alias top='btop'
alias lg='lazygit'

# Lifestyle
alias fetch='fastfetch'
alias weather='curl -s wttr.in'
alias stocks='ticker'
alias hn='clx'
alias play='mpv'
alias dl='yt-dlp'

# Voice
alias speak='~/bin/tts'
alias listen='~/bin/stt'
alias vpipe='~/bin/voice-pipe'

# Cockpit (Mac mini only)
alias cockpit='bash ~/Desktop/syncrescendence/orchestration/scripts/cockpit.sh'
alias cockpit-launch='bash ~/Desktop/syncrescendence/orchestration/scripts/cockpit.sh --launch'
alias cockpit-resize='bash ~/Desktop/syncrescendence/orchestration/scripts/cockpit.sh --resize'
alias cockpit-kill='bash ~/Desktop/syncrescendence/orchestration/scripts/cockpit.sh --kill'
```

**MBA verification needed**: Run `alias` in zsh to confirm which of these are actually set.

---

## 13. MBA Gap Summary

Items present on Mac mini but missing or incomplete on MBA:

| Category | Gap | Priority | Notes |
|----------|-----|----------|-------|
| Font | Liga SFMono Nerd Font not installed | P1 | Icons broken in eza, starship, yazi |
| Ghostty | Minimal config (47 vs 93 lines) | P2 | Missing scrollback, keybindings, shell integration |
| tmux | No TPM, different prefix, no resurrect/continuum | P2 | Session persistence not available |
| sesh | No config file | P2 | Session manager not configured |
| direnv | Not installed | P2 | Per-directory env vars unavailable |
| mise | Not installed | P3 | Runtime version management via Homebrew direct |
| yazi | No config | P2 | File manager uncustomized |
| fx | Not installed | P3 | JSON viewer missing |
| chafa | Not installed | P3 | Image renderer (yazi previews) missing |
| ticker | Not installed | P3 | Lifestyle tool |
| mpv | Not installed | P3 | Lifestyle tool |
| yt-dlp | Not installed | P3 | Lifestyle tool |
| Doom Emacs | Not installed (no Emacs binary) | P2 | Dashboard layer entirely absent |
| Piper TTS | Not installed | P3 | Voice synthesis missing |
| Voice scripts | ~/bin/stt, tts, voice-pipe missing | P3 | Voice pipeline not deployed |
| AeroSpace | Not installed | N/A | Not needed for MBA (no ultrawide) |
| JankyBorders | Not installed | N/A | Not needed without AeroSpace |

---

## 14. Cross-References

| Document | Path | Scope |
|----------|------|-------|
| Sovereign Cockpit Manifest | `engine/REF-SOVEREIGN_COCKPIT_MANIFEST.md` | Verbatim config dump (~2600 lines) |
| Deployment Playbook | `orchestration/DEPLOYMENT-PLAYBOOK.md` | Full tool inventory + install procedures |
| Stack Teleology | `engine/REF-STACK_TELEOLOGY.md` | Tool disposition analysis (active/sunset/evaluating) |
| Cockpit Protocol | `orchestration/state/ARCH-COCKPIT_OPERATIONAL_PROTOCOL.md` | Operational protocol for cockpit sessions |
| Cockpit Overview | `COCKPIT.md` | 30,000ft system overview with cockpit layout |
| Lifestyle Clarescence | `orchestration/state/impl/clarescence/CLARESCENCE-2026-02-08-cockpit-lifestyle-layer.md` | Decision atoms for lifestyle tools |
| HQ Elucidation | `orchestration/state/impl/clarescence/CLARESCENCE-2026-02-08-headquarters-elucidation.md` | Full HQ audit with drift resolution |
| MBA Ajna Setup | `orchestration/state/impl/clarescence/CLARESCENCE-2026-02-09-mba-ajna-setup.md` | MBA deployment guide |
| Implementation Map | `orchestration/state/IMPLEMENTATION-MAP.md` | Tranche E (IMPL-E-0001 through IMPL-E-0009) |
| Deferred Commitments | `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` | DC-009 (this file's creation) |

---

*This document was created to resolve DC-009 (Deferred Commitment #9): "TERMINAL-STACK-CONFIG.md referenced by 4+ clarescences but file DOES NOT EXIST." All 12 referencing files now have a valid target at this path.*
