  Track 1: Cockpit Model Switching — DONE (committed in 5cea41e)

  - Added POST_LAUNCH_MODEL_SWITCH=true flag to --launch case
  - Backgrounded subshell ((...) &) waits 8s for boot, then:
    - Sends /model gpt-5.3-codex to Adjudicator pane (Codex CLI)
    - Sends /model gpt-5.3-codex to Psyche pane (OpenClaw TUI)
  - Only fires with cockpit --launch, no-op on cockpit (plain create/attach)

  Track 2: MBA Cascade Supplement — DISPATCHED + IN PROGRESS

  The MBA Commander already picked up TASK-20260211-MBA_CASCADE_SUPPLEMENT.md (moved to
  10-IN_PROGRESS). The comprehensive 6-phase cascade covers:
  Phase: 1
  Content: Homebrew formulas
  Target: ~50-60 essential (bat, eza, fd, ripgrep, fzf, zoxide, atuin, starship, lazygit,
  yazi,
     glow, btop, etc.)
  ────────────────────────────────────────
  Phase: 2
  Content: Config file syncing
  Target: 8 dotfiles (.zshrc, starship.toml, ghostty, atuin, bat, .gitconfig, .tmux.conf,
    LazyVim)
  ────────────────────────────────────────
  Phase: 3
  Content: Skills expansion
  Target: 16+ core skills (planning, verification, debugging, git worktrees, Python,
    session-handoff)
  ────────────────────────────────────────
  Phase: 4
  Content: Claude Code settings
  Target: hooks (7), env vars, thinking mode, agent teams flag
  ────────────────────────────────────────
  Phase: 5
  Content: Voice layer
  Target: whisper-cpp (optional)
  ────────────────────────────────────────
  Phase: 6
  Content: Environment variables
  Target: NVIDIA, Linear, ClickUp, Google AI keys
  Also committed in 5cea41e were two MBA scripts the MBA Commander produced from the original
  TASK:
  - mba-cockpit.sh — 2-pane tmux layout (Ajna + Commander)
  - mba-commander-init.sh — one-shot MCP + alias + memory setup (300 lines)