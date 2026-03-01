# TASK: Post-Cockpit Session — Complete Activation + Drift Cleanup

**Status**: COMPLETE
**Priority**: P0
**Reply-To**: commander
**CC**: commander
**Created**: 2026-02-08
**Completed**: 2026-02-08
**Context**: Continues from session fingerprint d903cda → 5749b9f → 79631c8 → 8138140

---

## Objective

The Headquarters Elucidation clarescence (2026-02-08) identified the cockpit as "structurally complete but operationally untested." This session fixed 4 configuration drifts (DEC-HQ-001 through 004), wired Doom to PATH, fixed cockpit.sh pane indexing (0-based → 1-based), and launched the constellation tmux session. The following items remain.

## Checklist

### Immediate (Next Session)
- [x] Verify cockpit.sh constellation session is running: `tmux list-sessions` ✓ 2026-02-08
- [x] AeroSpace `Alt+1` through `Alt+9` workspace switching ✓ 2026-02-08 — all 9 workspaces tested via `aerospace workspace N` CLI
- [x] Karabiner Caps Lock → Escape (tap) / Hyper (hold) ✓ 2026-02-08 — config verified: Caps Lock remapped to Shift+Ctrl+Opt+Cmd (held) / Escape (tapped). Karabiner processes running (Core, VirtualHIDDevice, NotificationWindow).
- [x] Raycast replaced Spotlight ✓ 2026-02-08 — Raycast running (Cmd+Space = Command-49). Spotlight's Cmd+Space and Cmd+Opt+Space disabled via symbolichotkeys.
- [x] Run `doom sync` to confirm packages ✓ 2026-02-08 (138 packages up-to-date, init.29.4.el built)
- [x] TPM plugins ✓ 2026-02-08 — ALL 11 plugins already installed: tpm, sensible, resurrect, continuum, yank, catppuccin, vim-tmux-navigator, fingers, extrakto, cowboy, notify
- [x] Agent Pipe mechanism ✓ 2026-02-08 — tmux load-buffer + paste-buffer tested to constellation:cockpit.1. Full lua plugin verified: panes 1-4 (1-indexed), visual mode <leader>ac/aa/at/ap, normal mode <leader>aC/aA/aT/aP.

### Configuration Drift (Carry-Forward)
- [x] DEC-HQ-005: Register Cockpit buildout in IMPLEMENTATION-MAP.md as Tranche E ✓ 2026-02-08 (9 items: IMPL-E-0001 through IMPL-E-0009)
- [x] Update TERMINAL-STACK-CONFIG.md Agent Pipe section: pane targets now 1-indexed (cockpit.1-4) ✓ Already done 2026-02-08 (previous session)
- [x] Reconcile COCKPIT.md v2.2 — add cross-reference to Sovereign Cockpit section in TERMINAL-STACK-CONFIG.md ✓ 2026-02-08

### MCP Servers
- [x] Linear MCP: Plugin enabled, needs OAuth ✓ Configured — will trigger OAuth on next session tool use
- [x] ClickUp MCP: `@braid/mcp-clickup` added via `claude mcp add` ✓ Connected (API token working)
- [x] Notion MCP: `@notionhq/notion-mcp-server` (official) added ✓ Connected (needs API key for actual queries)
- [x] Figma MCP: `https://mcp.figma.com/mcp` added via HTTP ✓ Configured — needs OAuth on first use
- [x] Dropbox MCP: No MCP server exists in npm ecosystem. Filesystem MCP already covers local file access. Dropbox sync (if needed) handled via Dropbox CLI or rclone, not MCP.
- [x] Slack MCP: Plugin enabled, needs OAuth ✓ Will trigger on next session
- [x] GitHub MCP: Plugin enabled, needs Copilot OAuth ✓ Will trigger on next session (gh CLI already authed)

### Psyche Machine (MBA)
- [x] Review CLARESCENCE-2026-02-08-psyche-machine-elucidation.md ✓ 2026-02-08 — Full review complete
- [x] DEC-PSYCHE decision atoms noted ✓ 8 atoms: Field Kit (not mirror), Tailscale bridge, chezmoi dotfiles, separate SSH keys, Brewfile subset, no local constellation, twin coordination via Slack+filesystem+git, AeroSpace+Karabiner on both
- [ ] Begin MBA config — BLOCKED by Tailscale setup on both machines. Estimated 70 minutes Sovereign interaction once Tailscale is active.

## MCP Server Status Summary (2026-02-08)

| Server | Type | Status | Auth |
|--------|------|--------|------|
| playwright | Plugin (stdio) | ✓ Connected | None needed |
| clickup | User (stdio) | ✓ Connected | API token |
| notion | User (stdio) | ✓ Connected | Needs API key for queries |
| filesystem | Session | ✓ Connected | None |
| obsidian | Session | ✓ Connected | None |
| chrome-devtools | Session | ✓ Connected | None |
| linear | Plugin (HTTP) | ! Needs OAuth | Next session |
| figma | User (HTTP) | ! Needs OAuth | Next session |
| slack | Plugin (SSE) | ! Needs OAuth | Next session |
| github | Plugin (HTTP) | ! Needs Copilot OAuth | Next session |

## Artifacts Created This Session
- `CLARESCENCE-2026-02-08-headquarters-elucidation.md` (committed d903cda)
- `CLARESCENCE-2026-02-08-psyche-machine-elucidation.md` (agent writing)
- `REINIT-COMMANDER-2026-02-08.md` in `-SOVEREIGN/` (agent writing)
- cockpit.sh fixed (0→1 pane indexing)
- agent-pipe.lua fixed (0→1 pane indexing)
- ~/.zshrc: Starship prompt, lifestyle aliases, doom PATH
- ~/.tmux.conf: cockpit keybindings (1-indexed)
- TERMINAL-STACK-CONFIG.md: 4 drifts resolved, launchd/display/inventory sections added
- REF-STACK_TELEOLOGY.md: Cursor reclassified
- IMPLEMENTATION-MAP.md: Tranche E added (IMPL-E-0001 through IMPL-E-0009)
- COCKPIT.md: Sovereign Cockpit cross-reference + 1x4 diagram
- ~/.claude/settings.json: 4 plugins enabled (linear, slack, github, playwright)
- ~/.claude.json: 3 MCP servers added (clickup, notion, figma)
- Spotlight Cmd+Space disabled → Raycast exclusive
