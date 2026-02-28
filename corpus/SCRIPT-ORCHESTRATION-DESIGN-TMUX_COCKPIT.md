# Syncrescendence Multi-Agent Tmux Cockpit Design

**Version**: 1.0
**Date**: 2026-02-07
**Status**: Design complete, ready for implementation
**Depends on**: tmux 3.6a (installed), sesh 2.22.0 (installed), tpm (installed), Catppuccin tmux plugin (installed)

---

## 0. System State Assessment

| Component | Status | Path |
|-----------|--------|------|
| tmux 3.6a | Installed | `/opt/homebrew/bin/tmux` |
| sesh 2.22.0 | Installed | `/opt/homebrew/bin/sesh` |
| tpm | Installed | `~/.tmux/plugins/tpm/` |
| Catppuccin tmux | Installed | `~/.tmux/plugins/tmux/` |
| tmux-resurrect | Installed | `~/.tmux/plugins/tmux-resurrect/` |
| tmux-continuum | Installed | `~/.tmux/plugins/tmux-continuum/` |
| tmux-fingers | Installed | `~/.tmux/plugins/tmux-fingers/` |
| extrakto | Installed | `~/.tmux/plugins/extrakto/` |
| tmux-cowboy | Installed | `~/.tmux/plugins/tmux-cowboy/` |
| tmux-notify | Installed | `~/.tmux/plugins/tmux-notify/` |
| tmux-yank | Installed | `~/.tmux/plugins/tmux-yank/` |
| vim-tmux-navigator | Installed | `~/.tmux/plugins/vim-tmux-navigator/` |
| Existing cockpit scripts | Present | `orchestration/scripts/tmux_mba_cockpit.sh`, `tmux_dashboard.sh` |
| Existing tmux.conf | Complete | `~/.tmux.conf` (Catppuccin + sesh + tpm, Ctrl+Space prefix) |
| sesh config | Missing | `~/.config/sesh/sesh.toml` (needs creation) |

**Key finding**: The existing `~/.tmux.conf` is already well-configured with Catppuccin Mocha, tpm, and all essential plugins. The prefix is `Ctrl+Space` (not `Ctrl+b` or `Ctrl+a`). The design below preserves this existing config and builds the cockpit layer on top of it.

---

## 1. Layout Diagrams (ASCII)

### Overview Mode: 2x2 Grid (4 agents visible)

```
+------------------------------------------------------------------+
| [constellation] 1:cockpit*                    Feb 07 18:30  mini |
+--------------------------------+---------------------------------+
|                                |                                 |
|        COMMANDER               |         ADJUDICATOR             |
|      Claude Code (Opus)        |         Codex CLI               |
|      EXECUTOR-LEAD             |         PARALLEL-EXEC           |
|                                |                                 |
|   Color: #89b4fa (blue)        |   Color: #a6e3a1 (green)        |
|   Pane 0                       |   Pane 1                        |
|                                |                                 |
+--------------------------------+---------------------------------+
|                                |                                 |
|        CARTOGRAPHER            |         PSYCHE/AJNA             |
|       Gemini CLI               |         OpenClaw                |
|       SENSOR                   |         LOCAL ORCH              |
|                                |                                 |
|   Color: #f9e2af (yellow)      |   Color: #cba6f7 (mauve)        |
|   Pane 2                       |   Pane 3                        |
|                                |                                 |
+--------------------------------+---------------------------------+
| CMD  ADJ  CRT  PSY | session: constellation | 15:42 07-Feb      |
+------------------------------------------------------------------+
```

Pane assignment:
- Pane 0 (top-left): Commander -- the primary orchestrator, gets focus by default
- Pane 1 (top-right): Adjudicator -- mechanical execution partner
- Pane 2 (bottom-left): Cartographer -- corpus surveys, long-context
- Pane 3 (bottom-right): Psyche/Ajna -- extraction, QA, local orchestration

### Focus Mode: Single agent full-screen

```
+------------------------------------------------------------------+
| [constellation] 1:cockpit*  [A:idle C:run P:idle]  07-Feb 18:30  |
+------------------------------------------------------------------+
|                                                                  |
|                                                                  |
|                        COMMANDER                                 |
|                    Claude Code (Opus)                             |
|                                                                  |
|                                                                  |
|     $ claude --model opus "Commander, pivot to..."               |
|                                                                  |
|                                                                  |
|                                                                  |
|                                                                  |
|                                                                  |
|                                                                  |
+------------------------------------------------------------------+
| CMD* ADJ  CRT  PSY | session: constellation | 15:42 07-Feb      |
+------------------------------------------------------------------+
```

In focus mode, the status bar shows abbreviated state indicators for the three backgrounded agents:
- `A:idle` = Adjudicator idle
- `C:run` = Cartographer running
- `P:idle` = Psyche idle

Toggle: `prefix + z` (tmux native zoom, already bound by default)

### Secondary Window: Watchers (optional, window 2)

```
+------------------------------------------------------------------+
| [constellation] 2:watchers                     07-Feb 18:30      |
+--------------------------------+---------------------------------+
|                                |                                 |
|    INBOX WATCHER               |     GIT STATUS                  |
|    (triage_outgoing.sh)        |     (auto-refresh 15s)          |
|                                |                                 |
+--------------------------------+---------------------------------+
|                                |                                 |
|    AGENT LOGS                  |     SYSTEM MONITOR              |
|    (tail -F agent logs)        |     (btop / activity)           |
|                                |                                 |
+--------------------------------+---------------------------------+
```

---

## 2. Tmux Configuration Delta

The existing `~/.tmux.conf` is comprehensive. The following additions are cockpit-specific bindings that should be appended. They do not conflict with existing config.

```tmux
# ── Constellation Cockpit Bindings ──────────────────────────────────────────

# Quick-jump to agent panes in cockpit window (prefix + agent initial)
# These select the cockpit window (1) then jump to the named pane
bind C select-window -t :cockpit \; select-pane -t 0  # Commander
bind A select-window -t :cockpit \; select-pane -t 1  # Adjudicator
bind G select-window -t :cockpit \; select-pane -t 2  # cartographer (G for Gemini)
bind P select-window -t :cockpit \; select-pane -t 3  # Psyche

# Toggle between overview (tiled) and focus (zoom) with prefix + o
bind o if-shell "#{==:#{window_zoomed_flag},1}" \
  "resize-pane -Z" \
  "resize-pane -Z"

# Broadcast input to all agent panes (prefix + B) -- toggle
bind B setw synchronize-panes \; display "Sync #{?synchronize-panes,ON,OFF}"

# Quick switch to watchers window
bind W select-window -t :watchers

# Send interrupt to all panes (prefix + X) -- emergency stop
bind X confirm-before -p "Send C-c to ALL panes? (y/n)" \
  "run 'for i in 0 1 2 3; do tmux send-keys -t :cockpit.$i C-c; done'"
```

### Pane Border Colors per Agent (requires tmux 3.4+)

tmux 3.6a supports per-pane styling via `select-pane -P`. The cockpit launch script applies these colors at pane creation time:

| Pane | Agent | Border Color | Background tint |
|------|-------|-------------|-----------------|
| 0 | Commander | `#89b4fa` (blue) | `#1e1e2e` (base, no tint) |
| 1 | Adjudicator | `#a6e3a1` (green) | `#1e1e2e` |
| 2 | Cartographer | `#f9e2af` (yellow) | `#1e1e2e` |
| 3 | Psyche/Ajna | `#cba6f7` (mauve) | `#1e1e2e` |

---

## 3. Cockpit Launch Script

File: `orchestration/scripts/cockpit.sh`

```bash
#!/usr/bin/env bash
# cockpit.sh — Syncrescendence Constellation Cockpit
# Creates a tmux session with 4 agent panes in 2x2 grid
# plus an optional watchers window.
#
# Usage:
#   bash cockpit.sh              # Create/attach cockpit
#   bash cockpit.sh --launch     # Create cockpit AND launch agent CLIs
#   bash cockpit.sh --kill       # Kill the constellation session

set -euo pipefail

REPO="${SYNCRESCENDENCE_PATH:-$HOME/Desktop/syncrescendence}"
SESSION="constellation"

# ── Colors (Catppuccin Mocha) ───────────────────────────────────────────────
BLUE="#89b4fa"
GREEN="#a6e3a1"
YELLOW="#f9e2af"
MAUVE="#cba6f7"
BASE="#1e1e2e"
SURFACE1="#45475a"

# ── Agent launch commands ───────────────────────────────────────────────────
CMD_COMMANDER="cd '$REPO' && echo '--- COMMANDER (Claude Code / Opus) ---' && exec zsh"
CMD_ADJUDICATOR="cd '$REPO' && echo '--- ADJUDICATOR (Codex CLI) ---' && exec zsh"
CMD_CARTOGRAPHER="cd '$REPO' && echo '--- CARTOGRAPHER (Gemini CLI) ---' && exec zsh"
CMD_PSYCHE="cd '$REPO' && echo '--- PSYCHE/AJNA (OpenClaw) ---' && exec zsh"

if [[ "${1:-}" == "--launch" ]]; then
    CMD_COMMANDER="cd '$REPO' && claude --model opus"
    CMD_ADJUDICATOR="cd '$REPO' && codex --model claude-sonnet-4-5-20250929"
    CMD_CARTOGRAPHER="cd '$REPO' && gemini"
    CMD_PSYCHE="cd '$REPO' && openclaw tui --session main"
fi

if [[ "${1:-}" == "--kill" ]]; then
    tmux kill-session -t "$SESSION" 2>/dev/null && echo "Session '$SESSION' killed." || echo "No session '$SESSION' found."
    exit 0
fi

# ── Preflight ───────────────────────────────────────────────────────────────
if ! command -v tmux >/dev/null 2>&1; then
    echo "Error: tmux not found. Install: brew install tmux"
    exit 1
fi

# ── Create or attach ────────────────────────────────────────────────────────
if tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "Session '$SESSION' exists. Attaching..."
    tmux attach -t "$SESSION"
    exit 0
fi

echo "Creating constellation cockpit..."

# ── Window 1: cockpit (2x2 agent grid) ─────────────────────────────────────
tmux new-session -d -s "$SESSION" -c "$REPO" -n cockpit -x 200 -y 50

# Pane 0: Commander (top-left) -- created with the session
tmux send-keys -t "$SESSION":cockpit.0 "$CMD_COMMANDER" C-m

# Pane 1: Adjudicator (top-right)
tmux split-window -h -t "$SESSION":cockpit.0 -c "$REPO" -l 50%
tmux send-keys -t "$SESSION":cockpit.1 "$CMD_ADJUDICATOR" C-m

# Pane 2: Cartographer (bottom-left)
tmux select-pane -t "$SESSION":cockpit.0
tmux split-window -v -t "$SESSION":cockpit.0 -c "$REPO" -l 50%
tmux send-keys -t "$SESSION":cockpit.2 "$CMD_CARTOGRAPHER" C-m

# Pane 3: Psyche (bottom-right)
tmux select-pane -t "$SESSION":cockpit.1
tmux split-window -v -t "$SESSION":cockpit.1 -c "$REPO" -l 50%
tmux send-keys -t "$SESSION":cockpit.3 "$CMD_PSYCHE" C-m

# ── Apply per-pane border colors ────────────────────────────────────────────
# tmux 3.4+ supports pane-border-style per pane
tmux select-pane -t "$SESSION":cockpit.0 -T "Commander"
tmux select-pane -t "$SESSION":cockpit.1 -T "Adjudicator"
tmux select-pane -t "$SESSION":cockpit.2 -T "Cartographer"
tmux select-pane -t "$SESSION":cockpit.3 -T "Psyche"

# Enable pane titles display
tmux set-option -t "$SESSION" pane-border-status top
tmux set-option -t "$SESSION" pane-border-format " #{pane_title} "
tmux set-option -t "$SESSION" pane-border-style "fg=$SURFACE1"
tmux set-option -t "$SESSION" pane-active-border-style "fg=$BLUE"

# ── Window 2: watchers (monitoring grid) ────────────────────────────────────
tmux new-window -t "$SESSION" -n watchers -c "$REPO"

# Pane 0: INBOX watcher / triage
tmux send-keys -t "$SESSION":watchers.0 \
  "cd '$REPO' && while true; do clear; echo '[INBOX triage]'; ls -la agents/commander/inbox/pending/ 2>/dev/null; echo; bash orchestration/scripts/triage_outgoing.sh 2>/dev/null || true; sleep 10; done" C-m

# Pane 1: git status
tmux split-window -h -t "$SESSION":watchers.0 -c "$REPO"
tmux send-keys -t "$SESSION":watchers.1 \
  "cd '$REPO' && while true; do clear; echo '[git status]'; git status --short; echo; git log --oneline -5; sleep 15; done" C-m

# Pane 2: Agent logs
tmux select-pane -t "$SESSION":watchers.0
tmux split-window -v -t "$SESSION":watchers.0 -c "$REPO"
tmux send-keys -t "$SESSION":watchers.2 \
  "tail -n 200 -F /tmp/syncrescendence-watch-*.log 2>/dev/null || echo 'No agent logs found. Waiting...'" C-m

# Pane 3: System monitor
tmux select-pane -t "$SESSION":watchers.1
tmux split-window -v -t "$SESSION":watchers.1 -c "$REPO"
tmux send-keys -t "$SESSION":watchers.3 \
  "btop 2>/dev/null || top" C-m

tmux set-option -t "$SESSION":watchers pane-border-status top
tmux set-option -t "$SESSION":watchers pane-border-format " #{pane_title} "

tmux select-pane -t "$SESSION":watchers.0 -T "INBOX Triage"
tmux select-pane -t "$SESSION":watchers.1 -T "Git Status"
tmux select-pane -t "$SESSION":watchers.2 -T "Agent Logs"
tmux select-pane -t "$SESSION":watchers.3 -T "System Monitor"

# ── Focus on cockpit window, Commander pane ─────────────────────────────────
tmux select-window -t "$SESSION":cockpit
tmux select-pane -t "$SESSION":cockpit.0

# ── Attach ──────────────────────────────────────────────────────────────────
echo "Constellation cockpit ready. Attaching..."
tmux attach -t "$SESSION"
```

---

## 4. sesh Integration

sesh discovers tmux sessions automatically. However, a `sesh.toml` config allows pre-registering the constellation session for startup commands and custom behavior.

File: `~/.config/sesh/sesh.toml`

```toml
# Syncrescendence sesh configuration
# sesh connect "constellation" will create the session via cockpit.sh if it doesn't exist

[[session]]
name = "constellation"
path = "~/Desktop/syncrescendence"
startup_command = "bash ~/Desktop/syncrescendence/orchestration/scripts/cockpit.sh"

[[session]]
name = "sync-edit"
path = "~/Desktop/syncrescendence"

[[session]]
name = "scratch"
path = "~/Desktop"
```

### Usage patterns

```bash
# Quick-switch to constellation (creates if needed)
sesh connect constellation

# List all sessions (tmux + sesh-configured + zoxide)
sesh list -i | fzf

# From inside tmux, use the existing keybinding:
# prefix + f  (already bound in ~/.tmux.conf to sesh+fzf)

# Connect with startup command override
sesh connect constellation -c "bash ~/Desktop/syncrescendence/orchestration/scripts/cockpit.sh --launch"

# Switch sessions without detaching (inside tmux)
sesh connect --switch constellation
```

### Workflow: Sovereign quick-access

1. Open Ghostty
2. Press `prefix + f` (Ctrl+Space, f) to open sesh+fzf session picker
3. Type `con` to fuzzy-match "constellation"
4. Press Enter -- cockpit attaches (or creates via startup_command)
5. `prefix + C/A/G/P` to jump directly to Commander/Adjudicator/Cartographer/Psyche
6. `prefix + z` to zoom/unzoom the active agent pane (focus/overview toggle)
7. `prefix + W` to switch to watchers window
8. `prefix + f` again to switch to any other sesh session

---

## 5. Plugin Recommendations

### Currently Installed (keep all)

| Plugin | Rationale for Cockpit |
|--------|----------------------|
| `catppuccin/tmux` | Theme consistency across all panes. Mocha flavor matches Ghostty/Obsidian. |
| `tmux-resurrect` | Saves cockpit layout + pane contents across reboots. Critical for persistent agent sessions. |
| `tmux-continuum` | Auto-saves every 15min. Cockpit is automatically restorable after crashes. |
| `tmux-yank` | System clipboard integration. Copy agent output with `y` in copy mode. |
| `vim-tmux-navigator` | Ctrl+h/j/k/l pane navigation works even when nvim is running in a pane. |
| `tmux-fingers` | Press `prefix+F` to highlight copyable text (URLs, paths, hashes) with letter hints. Crucial for grabbing output from agent panes without scrolling. |
| `extrakto` | `prefix+Tab` opens fzf over pane content. Extract any text (URLs, file paths, commit hashes) from agent output. |
| `tmux-cowboy` | `prefix+*` sends SIGKILL to hung foreground process. Emergency stop for frozen agents. |
| `tmux-notify` | macOS notification when a command finishes in a non-focused pane. Alerts the Sovereign when an agent completes a task in a background pane. |
| `tmux-sensible` | Sane defaults (utf-8, longer history, faster key repeat). |

### Recommended Additions (not yet installed)

| Plugin | Rationale | Install |
|--------|-----------|---------|
| `tmux-plugins/tmux-logging` | `prefix+Shift+P` starts logging all pane output to file. Essential for agent session archaeology -- review what an agent did while you were focused on another. | `set -g @plugin 'tmux-plugins/tmux-logging'` |
| `tmux-plugins/tmux-pain-control` | Standardizes pane resizing to `prefix+Shift+h/j/k/l` (resize by 5 cells). More ergonomic than Alt+arrow for cockpit layout adjustments. | `set -g @plugin 'tmux-plugins/tmux-pain-control'` |
| `sainnhe/tmux-fzf` | `prefix+F` (capital) opens fzf for switching sessions/windows/panes, killing, and more. Complements sesh for in-tmux navigation. Note: conflicts with tmux-fingers if same key. Rebind to `prefix+Shift+F`. | `set -g @plugin 'sainnhe/tmux-fzf'` and `set -g @tmux-fzf-launch-key 'S-f'` |

To install after adding to `~/.tmux.conf`: press `prefix + I` (capital I) inside tmux.

---

## 6. Keybinding Reference Card

| Binding | Action |
|---------|--------|
| `Ctrl+Space` | Prefix |
| `prefix + f` | sesh session picker (fzf) |
| `prefix + C` | Jump to Commander pane |
| `prefix + A` | Jump to Adjudicator pane |
| `prefix + G` | Jump to Cartographer pane |
| `prefix + P` | Jump to Psyche pane |
| `prefix + z` | Toggle focus/overview (zoom) |
| `prefix + o` | Same as z (alias) |
| `prefix + W` | Switch to watchers window |
| `prefix + B` | Broadcast input to all panes (toggle) |
| `prefix + X` | Emergency: send Ctrl+C to all agent panes |
| `prefix + F` | Fingers: hint-based text copy |
| `prefix + Tab` | Extrakto: fzf text extraction from pane |
| `prefix + *` | Cowboy: kill hung process |
| `prefix + r` | Reload tmux config |
| `Ctrl+h/j/k/l` | Navigate panes (vim-style, no prefix) |
| `Alt+arrows` | Resize panes |
| `prefix + \|` | Split horizontal |
| `prefix + -` | Split vertical |

---

## 7. Implementation Checklist

- [ ] Append cockpit bindings to `~/.tmux.conf` (Section 2)
- [ ] Write `cockpit.sh` to `orchestration/scripts/cockpit.sh` (Section 3)
- [ ] Create `~/.config/sesh/sesh.toml` (Section 4)
- [ ] Run `prefix + I` inside tmux to install any new plugins
- [ ] Test: `bash cockpit.sh` creates session with 4 panes
- [ ] Test: `bash cockpit.sh --launch` starts agent CLIs
- [ ] Test: `sesh connect constellation` creates/attaches
- [ ] Test: `prefix + C/A/G/P` jump to correct panes
- [ ] Test: `prefix + z` toggles focus/overview
- [ ] Test: `prefix + W` switches to watchers
- [ ] Verify tmux-resurrect saves/restores the layout
- [ ] Verify tmux-notify fires on background pane completion

---

## 8. Relationship to Existing Scripts

| Existing Script | Status | Recommendation |
|-----------------|--------|----------------|
| `tmux_mba_cockpit.sh` | 3-pane layout (Psyche + logs + Commander) | Keep as-is for MBA-specific use case. `cockpit.sh` is the full constellation equivalent. |
| `tmux_dashboard.sh` | 4-pane monitoring (triage, logs, gateway, git) | Functionality absorbed into window 2 (watchers) of `cockpit.sh`. Can be retired once cockpit.sh is validated. |
| `launch_mba_single_window_tmux.sh` | Launcher: git pull + psyche_boot + tmux_mba_cockpit | Keep. Could be adapted to call `cockpit.sh --launch` instead. |

The new `cockpit.sh` supersedes the dashboard but complements the MBA cockpit. Both can coexist as separate tmux sessions (different session names).
