
• Done. I fixed the tmux launch path without touching plist watcher wiring.

  What I changed:

  - Updated orchestration/scripts/cockpit.sh:99 so Adjudicator launches as:
      - codex --full-auto -m gpt-5.3-codex -c 'model_reasoning_effort="high"'
  - Updated post-launch logic at orchestration/scripts/cockpit.sh:235 so Adjudicator is no
    longer switched via delayed /model; only Psyche keeps post-launch switch.

  Why:

  - gpt-5.3-codex-high is not a valid model slug here.
  - Valid setup is gpt-5.3-codex + model_reasoning_effort="high".

  Verification:

  - bash -n orchestration/scripts/cockpit.sh passed.
  - com.syncrescendence.watch-adjudicator.plist is unchanged and valid (plutil -lint ... OK).
  - LaunchAgent remains running (state = running).
  - In tmux, Adjudicator pane was idle in zsh; I started it in constellation:cockpit.5 with
    the new explicit command, and it is now active.

  To monitor this session yourself:

  - tmux attach -t constellation
  - tmux capture-pane -p -J -t constellation:cockpit.5 -S -120

  If you want a clean full restart with the new launch logic:

  1. cd /Users/home/Desktop/syncrescendence
  2. bash orchestration/scripts/cockpit.sh --kill
  3. bash orchestration/scripts/cockpit.sh --launch

  Note:

  - Codex startup shows many warnings from invalid cek-* skill YAML files. Functionality
    works, but if you want “fluent/quiet” startup, I can cleanly quarantine only invalid skill
    symlinks while keeping all valid skills loaded.


• Psyche is fixed and running gpt-5.3-codex with high thinking.

  Changes applied:

  - orchestration/scripts/cockpit.sh:96
    Psyche launch is now openclaw tui --session main --thinking high.
  - orchestration/scripts/watch_dispatch.sh:380
    Psyche watcher execution now adds --thinking high (Ajna unchanged).
  - /Users/home/.openclaw/openclaw.json:23 and /Users/home/.openclaw/openclaw.json:25
    Set:
      - agents.defaults.model.primary = openai-codex/gpt-5.3-codex
      - agents.defaults.thinkingDefault = high

  Runtime verification:

  - Restarted Psyche pane in tmux and confirmed status line shows:
    agent main | session main ... | openai-codex/gpt-5.3-codex | think high
  - Restarted com.syncrescendence.watch-psyche so watcher changes are live.
  - Validated syntax/plists:
      - bash -n orchestration/scripts/cockpit.sh
      - bash -n orchestration/scripts/watch_dispatch.sh
      - plutil -lint /Users/home/Library/LaunchAgents/com.syncrescendence*.plist (all OK)

  To monitor directly:

  - tmux capture-pane -p -J -t constellation:cockpit.1 

-S -80
  - tmux attach -t constellation