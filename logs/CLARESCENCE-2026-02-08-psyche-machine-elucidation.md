---
id: CLARESCENCE-2026-02-08-psyche-machine-elucidation
kind: clarescence
scope: orchestration + engine
status: active
created: 2026-02-08
author: Commander (Claude Code / Opus 4.6)
related:
  - CLARESCENCE-2026-02-08-headquarters-elucidation.md
  - CLARESCENCE-2026-02-08-sovereign-cockpit-architecture.md
  - orchestration/state/DYN-TWIN_COORDINATION_PROTOCOL.md
  - engine/REF-STACK_TELEOLOGY.md
  - orchestration/TERMINAL-STACK-CONFIG.md
---

# CLARESCENCE: Psyche's Machine Elucidation
## M4 MacBook Air Configuration Relative to the M1 Mac Mini Headquarters

**Author**: Commander (Claude Code / Opus 4.6)
**Date**: 2026-02-08
**Cross-references**: CLARESCENCE-2026-02-08-headquarters-elucidation.md, CLARESCENCE-2026-02-08-sovereign-cockpit-architecture.md, DYN-TWIN_COORDINATION_PROTOCOL.md, REF-STACK_TELEOLOGY.md, TERMINAL-STACK-CONFIG.md

---

## I. Executive Synthesis

The Headquarters (M1 Mac mini) is a stationary workhorse with an 8-layer Sovereign Cockpit, 6 launchd watchers, 4 CLI agents, and a 5120x1440 ultrawide. Psyche's Machine (M4 MacBook Air) is currently bare. The question is not "should the MBA mirror the mini?" but "what is the minimum configuration that allows the Sovereign to operate at full velocity while mobile, dispatch to Headquarters remotely, and coordinate the twin OpenClaw instances?"

**Verdict**: The MBA should be a **Field Kit** -- not a mirror. It carries Layers 1-3 of the cockpit (Ghostty, Zsh+P10k, tmux+sesh), a lean Neovim for prose, and Tailscale for remote dispatch to the always-on Mac mini. It does NOT carry the voice layer, Doom Emacs dashboard, or the full agent constellation. Those are Headquarters functions. The MBA is where the Sovereign thinks and dispatches; the Mac mini is where the swarm executes.

---

## II. The Two Machines -- Role Separation

| Dimension | Mac mini (Headquarters) | MacBook Air (Psyche's Machine) |
|-----------|------------------------|-------------------------------|
| **Chip** | M1, 8GB | M4, 16GB |
| **Display** | Samsung C49RG9x 5120x1440 ultrawide | 13.6" built-in (2560x1664) + occasional external |
| **Role** | Stationary Workhorse. Always-on. | Mobile Primary. Thinking surface. |
| **Repo** | Origin. Ground truth host. | Clone. Pull-only (or Tailscale remote). |
| **OpenClaw** | Ajna (Opus 4.5) -- orchestrator | Psyche (GPT-5.2) -- synthesis/QA |
| **Agent Fleet** | 4 CLI agents (Claude Code, Codex, Gemini, OpenClaw) | Claude Code only (remote dispatch for the rest) |
| **Always-on** | Yes (launchd watchers, OpenClaw gateway) | No (lid-close = sleep) |
| **Cockpit Layers** | All 8 | Layers 1-3 + lean Layer 5 |
| **Account** | Account 2 primary | Account 3 primary |

### The Operating Model

```
┌─────────────────────────────────────────────────┐
│  MacBook Air (FIELD KIT)                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │ Ghostty  │  │  Claude   │  │  OpenClaw    │  │
│  │ tmux     │  │  Web      │  │  (Psyche)    │  │
│  │ neovim   │  │  (think)  │  │  GPT-5.2     │  │
│  └────┬─────┘  └──────────┘  └──────────────┘  │
│       │                                          │
│       │  Tailscale SSH                           │
│       ▼                                          │
│  ┌──────────────────────────────────────────┐   │
│  │  Mac mini (HEADQUARTERS) via Tailscale   │   │
│  │  - Claude Code sessions                  │   │
│  │  - Codex CLI / Gemini CLI                │   │
│  │  - Ajna (OpenClaw Opus 4.5)              │   │
│  │  - launchd watchers                      │   │
│  │  - Full repo (origin)                    │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

---

## III. Layer-by-Layer Field Kit Specification

### Layer 1: Terminal (Ghostty) -- INCLUDE

| Component | Headquarters Config | Field Kit Config | Notes |
|-----------|-------------------|------------------|-------|
| Ghostty | ~/.config/ghostty/config | **IDENTICAL** | Same binary, same config file |
| Theme | Catppuccin Mocha | **IDENTICAL** | Visual consistency across machines |
| Font | Liga SFMono Nerd Font | **IDENTICAL** | Install via `shaunsingh/SFMono-Nerd-Font-Ligaturized` tap |
| Font size | 13pt | **14pt** | Slightly larger for 13" Retina screen |

**Effort**: 5 minutes. Install Ghostty, copy config, adjust font size.

### Layer 2: Shell (Zsh + P10k + tools) -- INCLUDE (SUBSET)

| Component | Headquarters | Field Kit | Rationale |
|-----------|-------------|-----------|-----------|
| Zsh | Full .zshrc (330+ lines) | **IDENTICAL** .zshrc | Muscle memory must be identical |
| Powerlevel10k | Lean + Unicode + Transient | **IDENTICAL** | Same prompt everywhere |
| zsh-autosuggestions | Yes | **YES** | Core shell intelligence |
| zsh-syntax-highlighting | Yes | **YES** | Core shell intelligence |
| Atuin | Yes (synced history) | **YES** | History sync IS the cross-machine benefit |
| zoxide | Yes | **YES** | Frecency navigation |
| fzf | Yes | **YES** | Universal fuzzy finder |
| direnv | Yes | **YES** | Per-directory env |
| bat/eza/fd/rg/dust/duf/procs | Yes | **YES** | Modern CLI replacements are non-negotiable |
| lazygit | Yes | **YES** | Git TUI |
| btop | Yes | **YES** | System monitoring |
| topgrade | Yes | **YES** | Universal updater |

**What to EXCLUDE from shell**: Voice pipeline scripts (voice-speak.sh, voice-capture.sh), cockpit.sh constellation launcher, agent-specific aliases that assume local panes.

**Effort**: 15 minutes. Brewfile subset install + .zshrc copy.

### Layer 3: Multiplexer (tmux + sesh) -- INCLUDE (SIMPLIFIED)

| Component | Headquarters | Field Kit | Rationale |
|-----------|-------------|-----------|-----------|
| tmux | Full config (11 plugins, cockpit layout) | **SAME .tmux.conf** minus cockpit-specific pane bindings | Prefix, navigation, and muscle memory must match |
| sesh | sesh.toml with constellation session | **SAME sesh** with field-kit session instead of constellation | Different session topology for single-machine use |
| TPM plugins | All 11 | **ALL 11** | resurrect/continuum are MORE important on a laptop (sleep/wake cycles) |

**Field Kit sesh session** (replaces the 4-pane constellation):

```toml
[[session]]
name = "field"
startup_command = "tmux split-window -h && tmux select-pane -t 0"
# Left pane: Neovim (prose/code)
# Right pane: Claude Code or SSH to Headquarters
```

**Effort**: 10 minutes. Copy tmux.conf, modify sesh.toml.

### Layer 4: Runtime (Bun) -- INCLUDE

| Component | Headquarters | Field Kit |
|-----------|-------------|-----------|
| Bun | Installed | **INSTALL** |
| mise | Installed (managing Node, Python) | **INSTALL** |

**Effort**: 2 minutes. `brew install bun mise`.

### Layer 5: Editor (Neovim + LazyVim) -- INCLUDE (LEAN)

| Component | Headquarters | Field Kit | Rationale |
|-----------|-------------|-----------|-----------|
| Neovim + LazyVim | Full config (37 plugins, Agent Pipe) | **SAME config directory** | Muscle memory. Same keybindings. |
| Agent Pipe | Sends to local tmux cockpit panes | **MODIFIED**: send to local Claude Code or SSH tunnel | No local 4-pane constellation to target |
| zen-mode, twilight | Yes | **YES** | The MBA IS the thinking surface -- zen mode matters more here |
| render-markdown | Yes | **YES** | Core prose capability |

**Agent Pipe modification for Field Kit**: Instead of targeting `cockpit.0`/`cockpit.1`/etc., the field kit Agent Pipe targets:
- `field.1` (right pane = Claude Code) for local dispatch
- Or pipes over Tailscale SSH to a Headquarters tmux pane

**Effort**: 10 minutes. Copy ~/.config/nvim/, adjust Agent Pipe target pane names.

### Layer 6: Voice (Whisper/Piper/sox) -- EXCLUDE

| Component | Headquarters | Field Kit | Rationale |
|-----------|-------------|-----------|-----------|
| whisper-cli | Installed | **NO** | Voice capture in public/mobile is impractical |
| Piper TTS | Installed | **NO** | TTS output in public is impractical |
| sox DSP | Installed | **NO** | No voice layer = no DSP needed |

**If the Sovereign later wants voice on MBA**: Install whisper-cli only (input capture with headphones). Omit Piper/sox (output). This is a future upgrade, not the minimum viable kit.

### Layer 7: Dashboard (Doom Emacs) -- EXCLUDE

| Component | Headquarters | Field Kit | Rationale |
|-----------|-------------|-----------|-----------|
| Doom Emacs | Installed (read-only dashboard) | **NO** | The dashboard observes the constellation. The constellation runs on the Mac mini. Observe it remotely via SSH + tmux attach. |

**Alternative on MBA**: Use `ssh mini -t tmux attach-session -t dashboard` to view the Doom dashboard remotely through Tailscale. Zero config needed on MBA.

### Layer 8: Simulators (Cursor) -- EXCLUDE

| Component | Headquarters | Field Kit | Rationale |
|-----------|-------------|-----------|-----------|
| Cursor | Installed (Simulator role) | **NO** | Neovim covers editing on MBA. Cursor's delegation role belongs at Headquarters. |

---

## IV. Tailscale -- The Bridge Between Machines

Tailscale is the critical infrastructure that transforms the MBA from "isolated laptop" into "remote cockpit for the Headquarters."

### What Tailscale Enables

| Capability | How | Command from MBA |
|-----------|-----|-----------------|
| **SSH to Mac mini** | Tailscale SSH (no key exchange needed) | `ssh mac-mini` (Tailscale MagicDNS) |
| **tmux attach to Headquarters sessions** | SSH + tmux | `ssh mac-mini -t tmux attach-session -t constellation` |
| **Dispatch tasks to agents** | Write to -INBOX via SSH | `ssh mac-mini "cat > ~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/TASK-xxx.md" < task.md` |
| **View Doom dashboard remotely** | SSH + tmux | `ssh mac-mini -t tmux attach-session -t dashboard` |
| **Git operations on origin repo** | SSH + git | `ssh mac-mini "cd ~/Desktop/syncrescendence && git log --oneline -5"` |
| **Port forwarding (OpenClaw gateway)** | Tailscale + SSH tunnel | `ssh -L 18789:localhost:18789 mac-mini` |
| **File transfer** | Tailscale + scp/rsync | `scp file.md mac-mini:~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/` |

### Tailscale Setup Sequence

```bash
# On Mac mini (if not already done):
1. Install Tailscale (App Store or brew)
2. tailscale up --ssh
3. Note the Tailscale IP / MagicDNS hostname

# On MacBook Air:
1. Install Tailscale (App Store or brew)
2. tailscale up --ssh
3. Verify: tailscale status (should see both machines)
4. Test: ssh mac-mini (should connect without password)

# Add to MBA ~/.ssh/config:
Host mini
    HostName mac-mini  # or Tailscale IP
    User <username>
    # Tailscale SSH handles auth
```

### Aliases for MBA .zshrc

```bash
# Headquarters remote access
alias hq='ssh mini'
alias hq-cockpit='ssh mini -t tmux attach-session -t constellation'
alias hq-dashboard='ssh mini -t tmux attach-session -t dashboard'
alias hq-dispatch='function _dispatch() { scp "$1" mini:~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/; }; _dispatch'
alias hq-status='ssh mini "cd ~/Desktop/syncrescendence && git log --oneline -3 && echo --- && git status -s"'
alias hq-agents='ssh mini "tmux list-sessions"'
```

**Effort**: 10 minutes per machine. Most is already installed; needs `tailscale up --ssh` on both.

---

## V. Dotfile Synchronization Strategy

### The Problem

Two machines need overlapping-but-not-identical configs. The Headquarters has 8 layers; the MBA has 3-5. Naive mirroring creates maintenance burden. No sync creates drift.

### Three Options Evaluated

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **chezmoi** | Template-based, supports machine-specific overrides via `.chezmoi.toml` | Another tool to learn, template complexity | SELECTED |
| **Bare git repo** | Simple, git-native, no new tools | No machine-specific logic without branching | REJECTED (branching = merge hell) |
| **Brewfile + manual copy** | Zero new tools | Manual = drift guaranteed | REJECTED |

### chezmoi Architecture

```
~/.local/share/chezmoi/           # Source of truth (git repo)
├── .chezmoiignore                # Machine-specific ignore rules
├── dot_zshrc.tmpl                # .zshrc with {{ if eq .machine "hq" }} blocks
├── dot_tmux.conf                 # Identical across machines
├── dot_config/
│   ├── ghostty/config.tmpl       # Font size differs per machine
│   ├── nvim/                     # Identical (LazyVim config)
│   └── sesh/sesh.toml.tmpl       # Session topology differs per machine
└── .chezmoidata.yaml
    # machine: hq | field
    # has_voice: true | false
    # has_dashboard: true | false
```

**Machine detection** (in `~/.config/chezmoi/chezmoi.toml`):

```toml
# On Mac mini:
[data]
machine = "hq"
has_voice = true
has_dashboard = true

# On MacBook Air:
[data]
machine = "field"
has_voice = false
has_dashboard = false
```

**Template example** (dot_zshrc.tmpl):

```
# -- Core shell config (both machines) --
source ~/.powerlevel10k/powerlevel10k.zsh-theme
# ... (shared config)

{{ if eq .machine "hq" }}
# -- Headquarters-only --
export PATH="$HOME/.config/emacs/bin:$PATH"
alias cockpit='./cockpit.sh --launch'
alias vc='tmux select-pane -t cockpit.0'
source ~/voice-aliases.sh
{{ end }}

{{ if eq .machine "field" }}
# -- Field Kit only --
alias hq='ssh mini'
alias hq-cockpit='ssh mini -t tmux attach-session -t constellation'
alias hq-dispatch='function _dispatch() { scp "$1" mini:~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/; }; _dispatch'
{{ end }}
```

**Effort**: 30 minutes initial setup. 2 minutes per future sync (`chezmoi update`).

---

## VI. Brewfile Strategy -- Subset, Not Mirror

The Headquarters Brewfile contains ~288 formulae and ~64 casks. The MBA needs a fraction.

### Brewfile.field (MBA subset)

```ruby
# === LAYER 1: Terminal ===
cask "ghostty"

# === LAYER 2: Shell Intelligence ===
brew "zsh-autosuggestions"
brew "zsh-syntax-highlighting"
brew "powerlevel10k"
brew "atuin"
brew "zoxide"
brew "fzf"
brew "direnv"

# === Modern CLI Replacements ===
brew "eza"
brew "bat"
brew "fd"
brew "ripgrep"
brew "dust"
brew "duf"
brew "procs"
brew "tldr"
brew "httpie"
brew "sd"
brew "jq"
brew "yq"

# === TUI Applications ===
brew "yazi"
brew "btop"
brew "lazygit"
brew "glow"
brew "fx"
brew "git-delta"

# === LAYER 3: Multiplexer ===
brew "tmux"
brew "sesh"

# === LAYER 4: Runtime ===
brew "bun"
brew "mise"

# === LAYER 5: Editor ===
brew "neovim"

# === Infrastructure ===
brew "tailscale"  # or App Store
brew "topgrade"
brew "chezmoi"

# === CLI Agents ===
# Claude Code (npm install -g @anthropic-ai/claude-code)
# OpenClaw (already installed)

# === GUI Apps ===
cask "raycast"

# === Font ===
tap "shaunsingh/SFMono-Nerd-Font-Ligaturized"
cask "font-sf-mono-nerd-font-ligaturized"
```

**Estimated formulae count**: ~40 formulae, ~3 casks. About 14% of the Headquarters Brewfile.

**Effort**: 5 minutes to create the file, 10 minutes to `brew bundle install`.

---

## VII. OpenClaw Twin Coordination

Per DYN-TWIN_COORDINATION_PROTOCOL.md, the two OpenClaw instances have distinct identities and roles.

### Current State

| Dimension | Ajna (Mac mini) | Psyche (MBA) |
|-----------|-----------------|--------------|
| Model | Opus 4.5 | GPT-5.2 |
| Channel | Webchat + iMessage | Slack |
| Gateway port | 18789 | 18789 (local) |
| Role | Orchestrator: commits, refactors, sub-agents | Synthesizer: extraction, QA, specs |
| Always-on | Yes (launchd) | No (only when MBA is awake) |

### Coordination Mechanisms

| Mechanism | How It Works | Status |
|-----------|-------------|--------|
| **Slack channel** | Psyche posts to Slack; Ajna reads via OpenClaw Slack skill or Sovereign relays | OPERATIONAL |
| **-INBOX/outputs/** | Twin writes TWIN-{FROM}-{TO}-{topic}.md files; other twin picks up | OPERATIONAL (filesystem) |
| **Tailscale dispatch** | MBA Psyche SCPs task files to Mac mini -INBOX/ | REQUIRES Tailscale setup |
| **Git** | Only Ajna commits (DYN-TWIN protocol rule) | OPERATIONAL |

### Key Design Decision

The two OpenClaw instances do NOT need to talk directly to each other over the network. They coordinate through:
1. **Slack** (Psyche's native channel) -- for conversational coordination
2. **Filesystem** (-INBOX/outputs/) -- for structured task handoff
3. **Git** (Ajna commits; Psyche reads) -- for state synchronization

Tailscale enables the MBA to write to the Mac mini filesystem directly, which is the missing transport for mechanism 2.

---

## VIII. Display Topology

### MBA Display Scenarios

| Scenario | Config | Workspace Layout |
|----------|--------|-----------------|
| **13" built-in only** | Single display, AeroSpace tiling optional | Full-screen Ghostty. tmux splits for multi-pane. Alt-Tab to Chrome (Claude Web). |
| **13" + external monitor** | Dual display | External: Ghostty (full tmux field session). Built-in: Chrome (Claude Web + OpenClaw). |
| **Clamshell + external** | Single external | Same as Headquarters layout but fewer panes. |

### AeroSpace on MBA

| Question | Answer |
|----------|--------|
| Install AeroSpace? | **YES** -- same tiling WM on both machines reduces context-switch cost |
| Same config? | **YES** -- identical ~/.aerospace.toml. Keybindings are muscle memory. |
| Karabiner Hyper Key? | **YES** -- identical karabiner.json. Hyper key is the universal modifier. |

---

## IX. Security -- Shared Secrets Management

### What Needs to Be Shared

| Secret | Mac mini | MBA | Sharing Method |
|--------|---------|-----|---------------|
| SSH keys | ~/.ssh/ (origin, GitHub) | Needs own keypair | **SEPARATE KEYS** -- MBA gets its own keypair, added to GitHub/servers independently |
| API tokens (Anthropic, OpenAI, Google, xAI) | In .zshrc / .env files | Needs same tokens | **1Password / Keychain** -- retrieve at setup time, store in MBA .env |
| OpenClaw config | Port 18789 config | Port 18789 config | **SEPARATE CONFIGS** -- different models, different personas |
| Obsidian vault | ~/Desktop/syncrescendence | Git clone or Tailscale mount | **GIT CLONE** for offline access; pull from mini as origin |
| Claude Code CLAUDE.md | In repo | In repo (via git clone) | **GIT** -- automatic |
| Atuin encryption key | In ~/.config/atuin/ | Needs same key | **MANUAL COPY** once -- enables cross-machine history sync |
| chezmoi repo | Source of truth | chezmoi init from same repo | **GIT** -- automatic |

### Security Rules

1. **NEVER share SSH private keys between machines.** Generate new keypair on MBA. Add MBA public key to GitHub, authorized_hosts on mini.
2. **API tokens go in .env files excluded from git** (.gitignore already covers this). Copy manually or via 1Password.
3. **Tailscale SSH eliminates password auth.** No SSH keys needed for inter-machine access -- Tailscale handles identity.
4. **Atuin sync key**: Copy `~/.config/atuin/key` from mini to MBA once. This enables encrypted shell history sync across both machines.

---

## X. The Minimum Viable Field Kit -- Execution Checklist

This is the exact sequence to bring the MBA from bare to operational.

### Phase 0: Foundation (15 minutes)

```
1.  Install Homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2.  Install Tailscale (App Store) and run: tailscale up --ssh
    On Mac mini: tailscale up --ssh (if not done)
    Verify: tailscale status (see both machines)

3.  Test: ssh mac-mini (should connect)
```

### Phase 1: Brewfile (10 minutes)

```
4.  Create ~/Brewfile.field with the subset from Section VI
5.  brew bundle install --file=~/Brewfile.field
6.  Wait for installs (~40 formulae + 3 casks)
```

### Phase 2: Shell (10 minutes)

```
7.  Clone chezmoi dotfiles repo (or manual copy):
    chezmoi init <dotfiles-repo-url>
    chezmoi apply

    OR (manual path):
    scp mac-mini:~/.zshrc ~/.zshrc
    scp mac-mini:~/.p10k.zsh ~/.p10k.zsh
    - Edit .zshrc: remove HQ-only blocks, add field-kit aliases

8.  Install P10k:
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k

9.  Install zsh plugins:
    git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.zsh/zsh-syntax-highlighting

10. Copy Atuin encryption key from Mac mini:
    scp mac-mini:~/.config/atuin/key ~/.config/atuin/key
    atuin login (or atuin import auto)

11. Source and verify: exec zsh
```

### Phase 3: Terminal + Theme (5 minutes)

```
12. Open Ghostty, verify Catppuccin Mocha + Liga SFMono
13. Adjust font-size = 14 in ~/.config/ghostty/config (for Retina 13")
14. Test: bat, eza, lazygit all showing Catppuccin colors
```

### Phase 4: Multiplexer (5 minutes)

```
15. Copy tmux config:
    scp mac-mini:~/.tmux.conf ~/.tmux.conf

16. Clone TPM:
    git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

17. Open tmux, run prefix+I (install all plugins)
    Wait for "TMUX environment reloaded"

18. Create ~/.config/sesh/sesh.toml with field session (Section III, Layer 3)
19. Test: sesh connect field
```

### Phase 5: Editor (10 minutes)

```
20. Copy Neovim config:
    scp -r mac-mini:~/.config/nvim ~/.config/nvim

21. Open nvim, wait for LazyVim to sync all plugins
22. Verify Catppuccin Mocha, treesitter, render-markdown
23. Modify Agent Pipe targets: field.1 instead of cockpit.0
```

### Phase 6: Git Clone + Repo (5 minutes)

```
24. Generate new SSH keypair:
    ssh-keygen -t ed25519 -C "mba-psyche"

25. Add public key to GitHub (Settings → SSH Keys)

26. Clone the repo:
    cd ~/Desktop
    git clone git@github.com:<user>/syncrescendence.git

27. Verify: cd syncrescendence && git log --oneline -5
```

### Phase 7: Window Management (5 minutes)

```
28. Install AeroSpace (if in Brewfile, already done)
29. Copy config: scp mac-mini:~/.aerospace.toml ~/.aerospace.toml
30. Grant Accessibility permission (System Settings → Privacy)
31. Install Karabiner-Elements (if desired)
32. Copy config: scp mac-mini:~/.config/karabiner/karabiner.json (same path on MBA)
33. Grant Input Monitoring permission
```

### Phase 8: Verification (5 minutes)

```
34. Open Ghostty → tmux → neovim → write some Markdown
35. Split pane, SSH to Mac mini: ssh mini
36. Attach to Headquarters tmux: tmux attach-session -t constellation
37. Verify you can see all 4 Headquarters agent panes from MBA
38. Test dispatch: echo "test" > /tmp/test-task.md && hq-dispatch /tmp/test-task.md
39. Verify file appears in Mac mini -INBOX/commander/00-INBOX0/
```

**Total setup time: ~70 minutes of Sovereign interaction.**

After this, the MBA is a fully operational Field Kit.

---

## XI. What the MBA Does NOT Get (and Why)

| Excluded Component | Rationale |
|-------------------|-----------|
| Voice layer (Whisper/Piper/sox) | Impractical for mobile use. View via SSH if needed. |
| Doom Emacs dashboard | Dashboard observes the Headquarters constellation. View it remotely via `hq-dashboard`. |
| Cursor | Simulator role belongs at Headquarters. Neovim covers editing on MBA. |
| 4-agent cockpit layout | No local Codex/Gemini/OpenClaw constellation. Those run on the always-on mini. |
| launchd watchers (6) | Watchers monitor the repo on the Mac mini. MBA does not host the origin repo. |
| Full Brewfile (~288 formulae) | ~248 of those are Headquarters-specific. MBA gets the ~40 that matter. |
| Keyboard Maestro / Hazel / Stream Deck | Automation layer is Headquarters-specific. MBA uses Raycast for quick actions. |

---

## XII. Future Upgrades (Not Now, But Planned)

| Upgrade | Trigger | Effort |
|---------|---------|--------|
| Local Claude Code agent on MBA | When M4 performance proves sufficient for parallel local execution | 10 min (already in Brewfile) |
| Voice input only (Whisper, no TTS) | When Sovereign wants hands-free capture with headphones | 15 min |
| Obsidian Sync (or Syncthing) | When git clone lag becomes annoying for vault browsing | 10 min |
| Second OpenClaw instance coordination | When twin workload requires real-time handoff | Per DYN-TWIN protocol |
| clamshell + ultrawide on MBA | When Sovereign acquires a second external display for MBA | AeroSpace config already handles it |

---

## XIII. Decision Atoms

### DEC-PSYCHE-001: Field Kit, Not Mirror
**Decision**: The MBA runs a lean Field Kit (Layers 1-3, lean Layer 5). It is NOT a mirror of the 8-layer Headquarters. The always-on Mac mini handles heavy execution; the MBA handles mobile thinking, Claude Web, and remote dispatch.

### DEC-PSYCHE-002: Tailscale is the Bridge
**Decision**: Tailscale SSH is the transport between MBA and Mac mini. Not filesystem sync (Dropbox/iCloud). Not manual SCP without Tailscale. Tailscale provides MagicDNS hostnames, zero-config SSH, and encrypted transport. This resolves the cross-machine race condition concern (DEC-COCKPIT-006 from the Sovereign Cockpit Architecture clarescence).

### DEC-PSYCHE-003: chezmoi for Dotfile Sync
**Decision**: Use chezmoi with machine-specific templates (`machine = "hq" | "field"`) to manage shared-but-differentiated configs across both machines. This avoids both manual drift and mirror complexity.

### DEC-PSYCHE-004: Separate SSH Keys Per Machine
**Decision**: Each machine gets its own SSH keypair. No copying private keys. Both public keys added to GitHub and any servers independently. Tailscale SSH handles inter-machine auth without keys.

### DEC-PSYCHE-005: Brewfile Subset
**Decision**: The MBA uses a dedicated Brewfile.field (~40 formulae, ~3 casks) rather than the full Headquarters Brewfile (~288 formulae, ~64 casks). The subset includes Layers 1-5 tooling plus infrastructure (Tailscale, chezmoi, topgrade).

### DEC-PSYCHE-006: No Local Agent Constellation on MBA
**Decision**: The MBA runs Claude Code locally (for direct work) and dispatches to the Mac mini constellation via Tailscale. It does NOT run Codex CLI, Gemini CLI, or a full 4-pane cockpit locally. The M4 chip is capable, but the always-on Mac mini is the correct host for the always-on constellation.

### DEC-PSYCHE-007: OpenClaw Twins Coordinate via Slack + Filesystem + Git
**Decision**: The two OpenClaw instances (Ajna on mini, Psyche on MBA) do not need direct network communication. They coordinate through: (1) Slack (Psyche's native channel), (2) -INBOX/outputs/ filesystem kanban (via Tailscale), (3) git (Ajna commits, Psyche reads). This is the existing DYN-TWIN protocol, now with Tailscale as the filesystem transport.

### DEC-PSYCHE-008: AeroSpace + Karabiner on Both Machines
**Decision**: Window management and keyboard remapping configs are IDENTICAL across both machines. Muscle memory is non-negotiable. The MBA gets the same AeroSpace tiling and Karabiner Hyper Key as the Headquarters.

---

## XIV. Psyche's Machine in One Sentence

The M4 MacBook Air is a lean Field Kit carrying Layers 1-3 of the Sovereign Cockpit (Ghostty, Zsh+P10k, tmux+sesh), a prose-focused Neovim, and a Tailscale bridge to the always-on Mac mini Headquarters -- enabling the Sovereign to think anywhere and dispatch everywhere, with 70 minutes of setup and zero configuration drift via chezmoi.

---

**END CLARESCENCE-2026-02-08-psyche-machine-elucidation.md**
