# CLARESCENCE: Cockpit Lifestyle Layer

```
CLARESCENCE: Cockpit Lifestyle Layer (Starship + Ricing + emacs-mac)
Fidelity: partial
Passes run: 1-3
Convergent Path: Install 6 missing lifestyle tools, switch P10k→Starship, replace emacs-plus→emacs-mac
Rationale (digest):
  - P10k lean ≈ Starship functionally; Starship eliminates instant-prompt complexity, is cross-shell, faster
  - emacs-mac (Yamamoto port) has superior macOS integration over emacs-plus (pixel scrolling, native image, multi-TTY)
  - 6 "ricing" tools fill the gap between Architecture Layer (done) and Lifestyle Layer (missing)
  - Nushell, brow.sh, aichat rejected as architectural conflicts (agent compatibility, novelty, redundancy)
  - newsboat/kew deferred (netnewswire + native media already cover these)
Dependencies created/updated: DEC-LIFESTYLE-001 through 005
Falsifier: If Starship's Catppuccin theme cannot match P10k's git segment density, or if emacs-mac's Doom compatibility breaks
Confidence: high
```

---

## Pass 1: Triumvirate Calibration

**Destination**: The Sovereign Cockpit lacks a "Lifestyle Layer" — the visual/fun/monitoring tools that make the terminal feel like a command center rather than a text editor. YouTube ricing stacks (Devin Stark, The Linux Cast) demonstrate this as the final 20% that creates the "lived-in" quality.

**Current state**:
- Architecture layers 1-8 COMPLETE (Ghostty→Zsh→tmux→Bun→Neovim→Voice→Emacs→Cursor)
- yazi, btop already installed but not all wired with aliases
- P10k lean style chosen — functionally identical to Starship but with instant-prompt baggage
- Starship v1.24.2 already installed via brew but not configured
- emacs-plus@30 installed; user wants emacs-mac (Yamamoto port) instead
- Missing: fastfetch, chafa, ticker, circumflex, mpv, yt-dlp

**Fit verdict**: HIGH FIT. These are purely additive (no substrate changes), low blast radius, instantly reversible via `brew uninstall`.

## Pass 2: 18+ Lenses (Scorecard)

| Lens | Pass? | Note |
|------|-------|------|
| Sovereignty | PASS | All tools are local/offline-capable |
| Portability | PASS | All in Brewfile, Starship config is single TOML |
| Agent compatibility | PASS | Zsh stays as shell; Starship just changes the prompt |
| Aesthetic coherence | PASS | Catppuccin Mocha palettes available for Starship, btop, fastfetch |
| Cognitive load | PASS | Aliases abstract complexity |
| Reversibility | PASS | `brew uninstall`, revert .zshrc, done |
| Energy cost | PASS | ~10 minutes to install and configure |
| Maintenance burden | PASS | topgrade handles updates |
| Conflict risk | WARN | emacs-mac may need emacs-plus unlink first |

Score: 8/9 lenses pass, 1 warning (manageable).

## Pass 3: CANON Coherence

**TERMINAL-STACK-CONFIG.md** says:
- Prompt: "Powerlevel10k — Lean, Unicode, Transient prompt"
- emacs: "GNU Emacs 30.2 (emacs-plus@30)"

**Reality**: User explicitly disagrees with keeping P10k. Lean P10k = Starship minus the complexity. Starship is already on disk.

**Divergence resolution**: Update TERMINAL-STACK-CONFIG.md to reflect Starship as prompt, emacs-mac as Emacs variant.

---

## Decision Atoms

### DEC-LIFESTYLE-001: Starship replaces Powerlevel10k

**Decision**: Switch prompt from Powerlevel10k (lean) to Starship.
**Truth surface**: `~/.config/starship.toml` becomes canonical prompt config. `~/.p10k.zsh` archived.
**Rationale**:
- P10k lean style is functionally equivalent to Starship's default
- Starship eliminates instant-prompt preamble + console output warnings
- Starship is cross-shell (works if user ever tries fish/nushell)
- Single TOML config vs 1700-line .p10k.zsh
- Already installed (`/opt/homebrew/bin/starship` v1.24.2)
**Reversibility**: Revert .zshrc, re-source .p10k.zsh. ~2 minutes.
**Falsifier**: If Starship cannot display git branch + status + execution time + dir in a lean single-line format with Catppuccin colors.

### DEC-LIFESTYLE-002: emacs-mac replaces emacs-plus

**Decision**: Install `emacs-mac` (Yamamoto's macOS port) alongside or replacing `emacs-plus@30`.
**Truth surface**: `/Applications/Emacs.app` from emacs-mac cask.
**Rationale**:
- Native pixel-smooth scrolling
- Better font rendering (Core Text)
- Native SVG/image support (no librsvg dependency)
- Better macOS integration (fullscreen, tabs, touch bar)
- Doom Emacs fully compatible with both
**Reversibility**: `brew uninstall --cask emacs-mac && brew link emacs-plus@30`
**Falsifier**: If emacs-mac's Doom compatibility breaks or Catppuccin theme doesn't render correctly.

### DEC-LIFESTYLE-003: Lifestyle tools manifest

**Decision**: Install the following via Homebrew:
| Tool | Purpose | Alias |
|------|---------|-------|
| fastfetch | System info display (neofetch replacement) | `fetch` |
| chafa | Image-to-terminal renderer (for yazi previews) | — |
| ticker | Live stock/crypto ticker | `stocks` |
| circumflex | Hacker News TUI | `hn` |
| mpv | Media player (CLI + GUI) | `play` |
| yt-dlp | Video downloader | `dl` |

**Aliases to add**: `weather` → `curl wttr.in`, `fetch` → `fastfetch`, `stocks` → `ticker`, `hn` → `circumflex`, `play` → `mpv`, `dl` → `yt-dlp`

### DEC-LIFESTYLE-004: Rejected tools

| Tool | Rejection reason |
|------|-----------------|
| Nushell | Breaks agent compatibility (Claude/Codex trained on bash/zsh) |
| brow.sh | Novelty toy, breaks on modern sites |
| aichat | Redundant with Claude Code + Ollama |
| newsboat | Redundant with NetNewsWire (installed) |
| kew | Niche; Apple Music / Spotify covers this |

### DEC-LIFESTYLE-005: zsh-autosuggestions already wired

Gemini flagged this as missing. It is NOT missing — already in `.zshrc` line 21-23 with Catppuccin Overlay0 color (#6c7086). No action needed.
