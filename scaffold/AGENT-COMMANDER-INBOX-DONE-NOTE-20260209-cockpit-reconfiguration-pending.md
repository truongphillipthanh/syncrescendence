# NOTE: Cockpit Reconfiguration Pending

**Date**: 2026-02-09
**From**: Commander (self-note)
**Status**: PENDING SOVEREIGN APPROVAL

---

## What Changed

Ajna is moving to MacBook Air, Psyche is taking Pane 1 on Mac mini.

## cockpit.sh Changes Needed

When Sovereign approves cockpit reconfiguration:

1. **Pane 1** label/agent: `Ajna` → `Psyche`
   - CLI stays `openclaw tui` (same platform, different model on gateway)
   - Gateway model config already set to GPT-5.3-codex (Psyche's model)

2. **tmux status bar**: Update any agent name references
3. **Keybind labels**: `prefix+1` now routes to Psyche, not Ajna

## CRITICAL REMINDER
- After ANY cockpit.sh change: `cockpit --kill && cockpit`
- NEVER just re-attach to existing session
- This is SEARED doctrine. 8+ times broken.

## No Change Needed
- Heights (48/15) — unchanged
- Window positioning — unchanged
- Other panes (Commander, Adjudicator, Cartographer) — unchanged
- nvim launch method — unchanged (direct split-window)
