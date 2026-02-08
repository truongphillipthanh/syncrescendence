# TASK: Post-Cockpit Session — Complete Activation + Drift Cleanup

**Status**: IN_PROGRESS
**Priority**: P0
**Reply-To**: commander
**CC**: commander
**Created**: 2026-02-08
**Context**: Continues from session fingerprint d903cda → 5749b9f → (pending commit)

---

## Objective

The Headquarters Elucidation clarescence (2026-02-08) identified the cockpit as "structurally complete but operationally untested." This session fixed 4 configuration drifts (DEC-HQ-001 through 004), wired Doom to PATH, fixed cockpit.sh pane indexing (0-based → 1-based), and launched the constellation tmux session. The following items remain.

## Checklist

### Immediate (Next Session)
- [x] Verify cockpit.sh constellation session is running: `tmux list-sessions` ✓ 2026-02-08
- [ ] If AeroSpace accessibility was granted, test `Alt+1` through `Alt+9` workspace switching (SOVEREIGN — interactive)
- [ ] If Karabiner Input Monitoring was granted, test Caps Lock → Escape (tap) / Hyper (hold) (SOVEREIGN — interactive)
- [ ] If Raycast replaced Spotlight, test `Cmd+Space` → Raycast (SOVEREIGN — interactive)
- [x] Run `doom sync` to confirm packages after PATH addition ✓ 2026-02-08 (138 packages, init.29.4.el)
- [ ] Run tmux `prefix+I` to install TPM plugins (catppuccin, resurrect, continuum, etc.) (SOVEREIGN — interactive)
- [ ] Test Agent Pipe from Neovim: open nvim in a spare pane, select text, `<leader>ac` → verify text in Commander pane (SOVEREIGN — interactive)

### Configuration Drift (Carry-Forward)
- [x] DEC-HQ-005: Register Cockpit buildout in IMPLEMENTATION-MAP.md as Tranche E ✓ 2026-02-08 (9 items: IMPL-E-0001 through IMPL-E-0009)
- [x] Update TERMINAL-STACK-CONFIG.md Agent Pipe section: pane targets now 1-indexed (cockpit.1-4) ✓ Already done 2026-02-08 (previous session)
- [x] Reconcile COCKPIT.md v2.2 — add cross-reference to Sovereign Cockpit section in TERMINAL-STACK-CONFIG.md ✓ 2026-02-08

### MCP OAuth
- [ ] Linear MCP: use Linear-related query in Claude Code to trigger OAuth
- [ ] ClickUp MCP: same
- [ ] Notion MCP: same
- [ ] Dropbox MCP: same
- [ ] Figma MCP: same

### Psyche Machine (MBA)
- [ ] Review CLARESCENCE-2026-02-08-psyche-machine-elucidation.md
- [ ] Ratify DEC-PSYCHE decision atoms
- [ ] Begin MBA config (after Tailscale setup)

## Artifacts Created This Session
- `CLARESCENCE-2026-02-08-headquarters-elucidation.md` (committed d903cda)
- `CLARESCENCE-2026-02-08-psyche-machine-elucidation.md` (agent writing)
- `REINIT-COMMANDER-2026-02-08.md` in `-SOVEREIGN/` (agent writing)
- cockpit.sh fixed (0→1 pane indexing)
- agent-pipe.lua fixed (0→1 pane indexing)
- ~/.zshrc: P10k quiet, doom PATH, cockpit aliases
- ~/.tmux.conf: cockpit keybindings (1-indexed)
- TERMINAL-STACK-CONFIG.md: 4 drifts resolved, launchd/display/inventory sections added
- REF-STACK_TELEOLOGY.md: Cursor reclassified
