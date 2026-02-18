# CLARESCENCE: Headquarters Elucidation
## Full-State Audit of the Sovereign Cockpit as Operational Headquarters

**Author**: Commander (Claude Code / Opus 4.6)
**Date**: 2026-02-08
**Fingerprint**: af4e276
**Cross-references**: TERMINAL-STACK-CONFIG.md, COCKPIT.md, ARCH-INTENTION_COMPASS.md, REF-NEO_BLITZKRIEG_BUILDOUT.md, REF-STACK_TELEOLOGY.md, REF-FLEET_COMMANDERS_HANDBOOK.md, DYN-TWIN_COORDINATION_PROTOCOL.md, IMPLEMENTATION-MAP.md

---

## I. Executive Synthesis

The Headquarters is the physical manifestation of the Syncrescendence execution model on the M1 Mac mini. After two sessions of intensive buildout, it has transitioned from a single-terminal improvisation to an 8-layer instrumented cockpit. This clarescence audits what actually exists on disk versus what the architecture documents promise, identifies the gaps between "installed" and "operational," and maps the remaining distance to full Blitzkrieg velocity.

**Verdict**: The headquarters is **structurally complete but operationally untested**. Every layer has been installed and configured. Zero layers have been battle-tested in a real multi-agent session. The distance from "configured" to "operational" is the Sovereign's muscle memory, not more installation.

---

## II. The Five Strata of Reality

### Stratum 1: What Actually Exists on Disk

| Layer | Binary | Config | Verified |
|-------|--------|--------|----------|
| 1. Ghostty | /Applications/Ghostty.app | ~/.config/ghostty/config | YES |
| 2. Zsh + P10k + 6 intelligence tools | All in /opt/homebrew/bin | ~/.zshrc (330+ lines) | YES |
| 3. tmux 3.6a + sesh 2.22.0 | /opt/homebrew/bin/ | ~/.tmux.conf (9 TPM plugins) | YES (plugins need `prefix+I`) |
| 4. AeroSpace + JankyBorders + Karabiner + Raycast + Ice | All installed | ~/.aerospace.toml, bordersrc, karabiner.json | YES (permissions TBD) |
| 5. Neovim 0.11.6 + LazyVim | /opt/homebrew/bin/nvim | 37 plugins, 4 plugin files | YES (headless sync confirmed) |
| 6. whisper-cli + Piper + sox | All installed | Models + personas + scripts | YES (smoke-tested by agents) |
| 7. Emacs 30.2 + Doom | /opt/homebrew/opt/emacs-plus@30 | 138 packages, 3 config files | YES (doom sync clean) |
| 8. Cursor | /Applications/Cursor.app | Existing config | YES |

### Stratum 2: What the Documents Describe but Don't Match

| Document | Claims | Reality | Delta |
|----------|--------|---------|-------|
| TERMINAL-STACK-CONFIG.md | Multiplexer = "Zellij" (line 51) | tmux is the actual cockpit multiplexer | **STALE** — Zellij was the original choice; tmux superseded it. Config file still lists Zellij as primary. |
| TERMINAL-STACK-CONFIG.md | Layer 5-7 status = "BUILDING (swarm)" | All three are INSTALLED and CONFIGURED | **STALE** — status columns not updated for Layers 5-7 architecture section |
| COCKPIT.md (v2.2) | "Current Priorities: 1. Operate minimal cycle" | Cockpit hasn't been test-fired once | **GAP** — no integration test performed |
| REF-STACK_TELEOLOGY.md | Cursor = SUNSET | DEC-COCKPIT-005 reclassifies as ACTIVE (Simulator role) | **CONFLICT** — Stack Teleology needs update |
| REF-STACK_TELEOLOGY.md | VS Code = EVALUATING | VS Code is not installed or mentioned anywhere else | **DEAD REFERENCE** |
| IMPLEMENTATION-MAP.md | 100+ IMPL items at various stages | Zero IMPL items reference the Cockpit layers installed this session | **DISCONNECT** — the IMPL map predates the Cockpit buildout |

### Stratum 3: What's Installed but Not Wired

| Component | Installed | Wired | Gap |
|-----------|-----------|-------|-----|
| tmux TPM plugins | TPM cloned | **NOT INSTALLED** | Run `prefix+I` inside tmux |
| cockpit.sh | Executable at scripts/ | **NEVER LAUNCHED** | Run `./cockpit.sh --launch` to test |
| AeroSpace | Config written | **NO ACCESSIBILITY PERMISSION** | Grant in System Settings |
| Karabiner Hyper Key | Rule in karabiner.json | **NO INPUT MONITORING PERMISSION** | Grant in System Settings |
| Raycast | App installed | **SPOTLIGHT STILL ACTIVE** | Disable Spotlight Cmd+Space |
| Voice pipeline | Scripts ready | **NEVER TESTED end-to-end** | Run `echo "test" \| voice-speak.sh` |
| Agent Pipe (Neovim) | Plugin loaded | **REQUIRES COCKPIT SESSION** | Only works when constellation tmux session is running |
| Doom Emacs | doom sync clean | **NOT IN PATH** | Add `~/.config/emacs/bin` to .zshrc |
| MCP OAuth servers (5) | Endpoints configured in .claude.json | **NEVER AUTHENTICATED** | First use triggers browser OAuth flow |
| sesh → cockpit.sh | sesh.toml points to cockpit.sh | **NEVER TESTED** | Run `sesh connect constellation` |

### Stratum 4: What's Truly Production-Ready (No Further Action)

These work right now, as-is, with no configuration needed:

1. **Ghostty** — Catppuccin Mocha, ligatures, true color
2. **Zsh** — all aliases, intelligence tools, long-command notifications
3. **bat/eza/fd/rg/dust/duf/procs** — all modern CLI replacements
4. **lazygit** — git TUI with delta diffs
5. **btop** — system monitoring
6. **fzf + atuin + zoxide** — search/history/navigation intelligence
7. **Brewfile** — declarative system state (`brew bundle install`)
8. **topgrade** — universal updater
9. **MCP stdio servers** — obsidian, filesystem, chrome-devtools, playwright
10. **Claude Code hooks** — session logs, pedigree, execution logs, intent compass

### Stratum 5: What Doesn't Exist Yet (and Should)

| Missing | Impact | Priority |
|---------|--------|----------|
| `~/.config/emacs/bin` in PATH | Can't run `doom` from shell | **IMMEDIATE** |
| tmux cockpit keybindings in ~/.tmux.conf | No `prefix+1/2/3/4` lane-switching | **HIGH** — referenced in DESIGN doc but never appended |
| `.zshrc` cockpit aliases | No `cockpit`, `vc`, `vs` aliases | **MEDIUM** |
| mise migration | nvm + pyenv still active (legacy) alongside mise | **LOW** |
| MCP Gateway (Lasso/Bridge) | Cross-agent MCP sharing impossible | **DEFERRED** per DEC-COCKPIT-006 |
| MacBook Air (Psyche) config | Twin machine has none of this | **BLOCKED** by Tailscale setup |
| HighCommand QA | Agendizer phases 5-9 still pending review | **BLOCKED** by PROJ-006a |

---

## III. Intention Alignment Audit

Cross-referencing the Headquarters against every active Intention in the Compass:

| Intention | Served by Headquarters? | How |
|-----------|------------------------|-----|
| INT-1202 "capitalize on heavy machinery" | **YES** — the cockpit IS the heavy machinery | 4-lane parallel execution, Agent Pipe composition, sesh instant switching |
| INT-MI19 "Palantir-like ontology" | **PARTIALLY** — Layer 7 (Doom/Org-roam) provides knowledge graph browsing | But the ontology substrate (PROJ-006b) is still blocked by PROJ-003 |
| INT-1203 "5-platform constellation" | **YES** — cockpit maps 4 CLI agents to panes; web platforms accessed via MCP | MCP OAuth pending for full constellation |
| INT-C005 "Learn tmux" | **RESOLVED** — tmux is installed, configured, cockpit designed | But Sovereign hasn't used it yet |
| INT-C007 "Session discipline" | **RESOLVED** — sesh sessions, /compact at 75%, PROMPT-*.md reinit protocol | But anti-pattern must be tested in practice |
| INT-MI17 "On-device automation" | **PARTIALLY** — Karabiner, Keyboard Maestro, Raycast installed | Hazel rules, Stream Deck profiles, Shortcuts not configured |
| INT-MI18 "Web↔CLI bridge" | **NOT YET** — MCP OAuth will provide web↔CLI bridge | Pending first authentication |

---

## IV. Blitzkrieg Readiness Assessment

The Neo-Blitzkrieg requires 4 parallel execution lanes running simultaneously. Can the Headquarters support this?

### Lane Readiness

| Lane | Agent | Pane | Binary | Config | Can Execute? |
|------|-------|------|--------|--------|-------------|
| A (Commander) | Claude Code | cockpit.0 | YES | YES | **YES** — this is what we're using right now |
| B (Adjudicator) | Codex CLI | cockpit.1 | YES | AGENTS.md present | **YES** — needs manual launch in pane |
| C (Cartographer) | Gemini CLI | cockpit.2 | YES | gemini-settings.json | **YES** — needs manual launch in pane |
| D (Psyche/Ajna) | OpenClaw | cockpit.3 | YES | OpenClaw config | **PARTIAL** — OpenClaw works but OAuth credentials sometimes expire |

### Connective Tissue Readiness

| Component | Status | Verdict |
|-----------|--------|---------|
| cockpit.sh (tmux layout) | Script ready, never tested | UNTESTED |
| Agent Pipe (Neovim → tmux) | Plugin loaded, needs cockpit session | UNTESTED |
| Dispatch system (-INBOX/agent/) | Filesystem kanban operational | OPERATIONAL |
| dispatch.sh (task creation) | Script exists, tested | OPERATIONAL |
| Intent Compass hook | Fires on every prompt | OPERATIONAL |
| Pedigree hook | Fires on session stop | OPERATIONAL |
| Execution log hook | Fires on session stop | OPERATIONAL |

### Blitzkrieg Verdict

**4/4 lanes have binaries. 4/4 have configs. 0/4 have been tested in the cockpit layout.**

The Blitzkrieg can theoretically run today. The bottleneck is the Sovereign's first `sesh connect constellation` → `cockpit.sh --launch` → verify all 4 panes respond → test Agent Pipe from Neovim.

---

## V. Configuration Drift Registry

These are contradictions between documents that need reconciliation:

| # | Conflict | Documents | Resolution |
|---|----------|-----------|------------|
| 1 | Zellij vs tmux | TERMINAL-STACK-CONFIG.md §Multiplexer says Zellij; cockpit.sh uses tmux | **tmux wins** — update config ledger |
| 2 | Cursor SUNSET vs SIMULATOR | REF-STACK_TELEOLOGY.md says SUNSET; DEC-COCKPIT-005 says ACTIVE | **DEC-COCKPIT-005 wins** — update Stack Teleology |
| 3 | Layer 5-7 "BUILDING" | TERMINAL-STACK-CONFIG.md §Architecture says BUILDING | **All three are COMPLETE** — update status |
| 4 | Doom keybindings `SPC d` vs `SPC S` | TERMINAL-STACK-CONFIG.md says `SPC S i/m/l/c`; actual config.el uses `SPC d s/i/e/l/t/a/r` | **config.el wins** (it's what's on disk) |
| 5 | COCKPIT.md v2.2 doesn't mention Sovereign Cockpit | COCKPIT.md is the constellation-level overview; Cockpit architecture is in TERMINAL-STACK-CONFIG.md | **Not a conflict** — different scope. But COCKPIT.md should cross-reference the Sovereign Cockpit section. |
| 6 | Doom init.el — my version vs agent's version | My init.el had +roam2, agent's had +roam (correct) | **Agent's version is on disk** — correct |

---

## VI. The Activation Sequence

This is the exact order of operations to bring the Headquarters from "configured" to "operational":

### Phase 0: Permissions (2 minutes, one-time)
```
1. System Settings → Privacy → Accessibility → Enable AeroSpace
2. System Settings → Privacy → Input Monitoring → Enable Karabiner
3. System Settings → Keyboard → Shortcuts → Spotlight → Disable Cmd+Space
4. Open Raycast → Set Cmd+Space as Raycast hotkey
```

### Phase 1: Wire the Last Connections (5 minutes)
```
5. Add to ~/.zshrc:
   export PATH="$HOME/.config/emacs/bin:$PATH"

6. Open tmux, run: prefix+I (install TPM plugins)
   Wait for "TMUX environment reloaded" message

7. Append cockpit keybindings to ~/.tmux.conf:
   bind-key 1 select-pane -t cockpit.0
   bind-key 2 select-pane -t cockpit.1
   bind-key 3 select-pane -t cockpit.2
   bind-key 4 select-pane -t cockpit.3
```

### Phase 2: First Launch (3 minutes)
```
8. sesh connect constellation
   → cockpit.sh auto-launches
   → Verify 4 panes appear in 2x2 grid
   → Verify color-coded borders (blue/green/yellow/mauve)

9. In each pane, test the agent binary:
   Pane 0: claude (should start Claude Code)
   Pane 1: codex (should start Codex CLI)
   Pane 2: gemini (should start Gemini CLI)
   Pane 3: openclaw (or start manually)
```

### Phase 3: Agent Pipe Validation (2 minutes)
```
10. In a separate tmux pane or split: nvim test.md
11. Type some text, visually select it
12. Press <leader>ac → verify text appears in Pane 0 (Commander)
13. Press <leader>ag → verify text appears in Pane 2 (Cartographer)
```

### Phase 4: Voice Smoke Test (2 minutes)
```
14. echo "Hello from the Commander" | voice-speak.sh --persona commander
    → Should hear a deeper, authoritative voice
15. echo "The Cartographer surveys" | voice-speak.sh --persona cartographer
    → Should hear a warm, reverberant voice
```

### Phase 5: Dashboard Verification (2 minutes)
```
16. emacs (or open Emacs.app)
17. SPC d i → should open Intention Compass (read-only)
18. SPC d s → should open COCKPIT.md (read-only)
19. Verify Catppuccin Mocha theme, Liga SFMono font
```

**Total activation time: ~16 minutes of Sovereign interaction.**

---

## VII. The Distance Map

### What's Between Here and Full Velocity

| Distance | Effort | Impact |
|----------|--------|--------|
| **0 → Activation** (Phase 0-5 above) | 16 min Sovereign time | Unlocks parallel Blitzkrieg |
| **Activation → MCP Bridge** | 5 OAuth logins (browser) | Unlocks Linear/ClickUp/Notion/Figma/Dropbox from Claude Code |
| **MCP Bridge → Full Constellation** | Tier C auth tokens (GitHub PAT, Slack bot, etc.) | Unlocks 5 more surfaces |
| **Full Constellation → Twin Parity** | Tailscale + MacBook Air setup | Unlocks Psyche machine |
| **Twin Parity → HighCommand** | PROJ-006a completion + QA | Unlocks INT-MI19 ontology GUI |
| **HighCommand → Gaian** | Modal 1 → Modal 2 → Modal 3 | The long game |

---

## VIII. Decision Atoms

### DEC-HQ-001: Resolve Zellij/tmux Drift
**Decision**: tmux is the canonical multiplexer. Update TERMINAL-STACK-CONFIG.md §Multiplexer to reflect tmux (not Zellij). Zellij remains installed as a secondary option but is not the cockpit substrate.

### DEC-HQ-002: Stack Teleology Reconciliation
**Decision**: REF-STACK_TELEOLOGY.md must be updated to reflect: Cursor = ACTIVE (Simulator), tmux = ACTIVE (Multiplexer primary), Zellij = EVALUATING (secondary). This is a non-trivial update that should be dispatched as a task.

### DEC-HQ-003: Architecture Layer Status Update
**Decision**: Update TERMINAL-STACK-CONFIG.md §Architecture Layers table to show Layers 5-7 as COMPLETE (not BUILDING).

### DEC-HQ-004: Doom Keybinding Canonicalization
**Decision**: The actual config.el keybindings (`SPC d` prefix) are canonical. Update TERMINAL-STACK-CONFIG.md to match what's on disk.

### DEC-HQ-005: IMPLEMENTATION-MAP Integration
**Decision**: The Cockpit buildout should be registered in IMPLEMENTATION-MAP.md as Tranche E (Infrastructure) items. Current IMPL items (A-D) predate this work. A new tranche should capture the cockpit layers, their verification status, and the activation sequence.

### DEC-HQ-006: Activation is the Next Action
**Decision**: No more installation. No more configuration. The next directive should be the 16-minute activation sequence (Phase 0-5 above). The headquarters is built; it needs to be turned on.

---

## IX. The Headquarters in One Sentence

The Sovereign Cockpit is a fully-installed 8-layer terminal-first operating environment that maps the Neo-Blitzkrieg's 4 parallel execution lanes onto a tmux grid, provides a Neovim composition surface with Agent Pipe for cross-lane dispatch, a local voice loop with 4 persona-filtered DSP profiles, a Doom Emacs read-only dashboard for state observation, and a declarative Brewfile-managed system — all unified under Catppuccin Mocha and Liga SFMono — and it has never been turned on.

---

**END CLARESCENCE-2026-02-08-headquarters-elucidation.md**
