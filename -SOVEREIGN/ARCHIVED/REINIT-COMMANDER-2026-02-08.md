# Commander Reinitialization Protocol
## Post-Session Activation Sequence

**From**: Commander (Claude Code / Opus 4.6)
**To**: Sovereign
**Date**: 2026-02-08
**Fingerprint**: d903cda → 5749b9f
**Purpose**: Bring the Headquarters from CONFIGURED to OPERATIONAL

---

## Phase 0: Verify the Foundation (1 minute)

Open a NEW Ghostty terminal (to pick up .zshrc changes):

1. [ ] Verify P10k no longer warns:
   ```
   # Should start clean, no WARNING banner
   ```

2. [ ] Verify doom is in PATH:
   ```
   which doom
   # Should output: /Users/home/.config/emacs/bin/doom
   ```

3. [ ] Verify cockpit aliases:
   ```
   type cockpit  # Should show: cockpit is an alias for sesh connect constellation
   type vc       # Should show: vc is an alias for nvim .../COCKPIT.md
   type vs       # Should show: vs is an alias for nvim .../ARCH-INTENTION_COMPASS.md
   ```

---

## Phase 1: Grant Permissions (2 minutes)

4. [ ] **AeroSpace**: Open AeroSpace.app → System Settings will prompt for Accessibility → Grant it
   ```
   open -a AeroSpace
   ```

5. [ ] **Karabiner**: Open Karabiner-Elements.app → System Settings will prompt for Input Monitoring → Grant it
   ```
   open -a "Karabiner-Elements"
   ```
   Test: Press Caps Lock → should act as Escape (tap) or Hyper key (hold)

6. [ ] **Raycast → Spotlight swap**:
   - System Settings → Keyboard → Keyboard Shortcuts → Spotlight → Uncheck "Show Spotlight search" (Cmd+Space)
   - Open Raycast → Settings → General → Set Raycast Hotkey to Cmd+Space
   ```
   open -a Raycast
   ```

---

## Phase 2: Install tmux Plugins (2 minutes)

7. [ ] Open tmux and install TPM plugins:
   ```
   tmux
   # Press: Ctrl+Space then Shift+I
   # Wait for "TMUX environment reloaded" message
   # This installs: catppuccin, resurrect, continuum, yank, fingers, extrakto, cowboy, notify, vim-tmux-navigator
   ```

8. [ ] Reload tmux config:
   ```
   # Inside tmux:
   # Press: Ctrl+Space then r
   # Should see "Config reloaded"
   ```

---

## Phase 3: First Cockpit Launch (3 minutes)

9. [ ] Launch the cockpit:
   ```
   cockpit
   # OR: sesh connect constellation
   # OR: bash ~/Desktop/syncrescendence/orchestration/scripts/cockpit.sh
   ```
   Verify: 4 panes in 2x2 grid appear

10. [ ] Test pane switching:
    ```
    # Press: Ctrl+Space then 1 → should focus Commander pane (top-left)
    # Press: Ctrl+Space then 2 → should focus Adjudicator pane (top-right)
    # Press: Ctrl+Space then 3 → should focus Cartographer pane (bottom-left)
    # Press: Ctrl+Space then 4 → should focus Psyche pane (bottom-right)
    ```

11. [ ] Test agents in panes:
    ```
    # In pane 1: claude
    # In pane 2: codex
    # In pane 3: gemini
    # In pane 4: openclaw
    ```

---

## Phase 4: Dashboard Smoke Test (2 minutes)

12. [ ] Open Doom Emacs:
    ```
    emacs &
    # OR: open -a Emacs
    ```

13. [ ] Test dashboard keybindings (inside Emacs):
    ```
    SPC d s  → Opens COCKPIT.md
    SPC d i  → Opens Intention Compass
    SPC d e  → Opens Execution Staging
    SPC d l  → Opens Session Log
    SPC d t  → Opens Terminal Stack Config
    SPC d a  → Opens Org Agenda
    ```

---

## Phase 5: Voice Smoke Test (2 minutes)

14. [ ] Test TTS:
    ```
    echo "The Commander reports all systems nominal" | bash ~/Desktop/syncrescendence/orchestration/scripts/voice-speak.sh --persona commander
    ```

15. [ ] Test STT (requires microphone):
    ```
    bash ~/Desktop/syncrescendence/orchestration/scripts/voice-capture.sh --clipboard
    # Speak → should see transcription → copied to clipboard
    ```

---

## Phase 6: MCP OAuth (5 minutes, first-time only)

16. [ ] Trigger OAuth for each MCP server by using them in Claude Code:
    ```
    claude
    # Then ask: "Check my Linear issues"          → triggers Linear OAuth
    # Then ask: "Check my ClickUp tasks"           → triggers ClickUp OAuth
    # Then ask: "Check my Notion pages"             → triggers Notion OAuth
    # Then ask: "Check my Dropbox files"            → triggers Dropbox OAuth
    # Then ask: "Check my Figma projects"           → triggers Figma OAuth
    ```
    Each will open a browser tab for one-time authorization.

---

## Phase 7: AeroSpace Ultrawide Layout (2 minutes)

17. [ ] Verify AeroSpace workspace switching:
    ```
    # Alt+1 through Alt+9 to switch workspaces
    # Alt+h/j/k/l to move focus between windows
    # Alt+Shift+h/j/k/l to move windows
    # Alt+Enter to open new Ghostty
    # Alt+f for fullscreen toggle
    ```

18. [ ] Set up workspace assignments:
    - WS 1-3 (left zone): Terminal/Cockpit/Editor
    - WS 4-6 (center zone): Browser/Obsidian/PM tools
    - WS 7-9 (right zone): Comms/Monitor/Dashboard

---

## Verification Complete

When all boxes are checked, the Headquarters is OPERATIONAL.

**Total Sovereign time**: ~19 minutes
**After this**: Start a new Claude Code session and run the Blitzkrieg.

---

*"The machine is built. Turn it on."*
