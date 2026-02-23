✔ You approved codex to always run commands that start with bash /Users/home/.syncrescendence/
  scripts/watchdog.sh
• Ran : > /tmp/syncrescendence-watchdog.log; bash /Users/home/.syncrescendence/scripts/
    [2026-02-11 19:15:44] Psyche pane healthy (cmd=node)
    [2026-02-11 19:15:44] Qdrant (Docker): healthy (HTTP 200)

     M orchestration/state/DYN-EXECUTION_STAGING.md
     M orchestration/state/DYN-GLOBAL_LEDGER.md
     M orchestration/state/DYN-PEDIGREE_LOG.md
     M orchestration/state/DYN-SESSION_LOG.md

─ Worked for 1m 42s ──────────────────────────────────────────────────────────────────────────

• Hardened. Psyche + Adjudicator now self-heal via watchdog, and skill coverage is
  continuously reconciled.
  What I changed:

  - ~/.syncrescendence/scripts/watchdog.sh:13
      - Added explicit PATH so tmux/openclaw/codex resolve under launchd.
  - ~/.syncrescendence/scripts/watchdog.sh:54
      - Added skill repertoire reconciliation:
          - Mirrors missing/broken links from /Users/home/.agents/skills into:
              - /Users/home/.codex/skills
              - /Users/home/.openclaw/skills
  - ~/.syncrescendence/scripts/watchdog.sh:98
      - Added cockpit self-heal:
          - If constellation tmux session is missing, recreate via detached launch.
          - If cockpit layout drifts, rebuild session.
          - If Psyche/Adjudicator pane is not running agent runtime, restart with:
              - Psyche: openclaw tui --session main --thinking high
              - Adjudicator: codex --full-auto -m gpt-5.3-codex -c
                'model_reasoning_effort="high"'
  - ~/.syncrescendence/scripts/watchdog.sh:167
      - Fixed watchdog self-footgun: watcher scan now matches watch-* only (excludes watchdog
        itself).
  - ~/.syncrescendence/scripts/watchdog.sh:233
      - Removed perpetual false warning for missing README.md from critical-file check.

  Cockpit compatibility:

  - orchestration/scripts/cockpit.sh supports detached recovery mode (--launch-detached),
    which watchdog uses for safe non-blocking revive.

  Verification run (fresh):

  - bash -n ~/.syncrescendence/scripts/watchdog.sh -> OK
  - bash -n orchestration/scripts/cockpit.sh -> OK
  - Clean watchdog pass showed:
      - Psyche pane healthy (cmd=node)
      - Adjudicator pane healthy (cmd=node)
      - skills sync (codex): no changes
      - skills sync (openclaw): no changes
      - all local health checks HTTP 200
  - Skill coverage checks:
      - missing .agents -> .codex: none
      - missing .agents -> .openclaw: none
      - broken symlinks in both targets: 0

  No plist schema changes were made, so launchd wiring remains intact.

  If you want, I can also tighten watchdog cadence from 5 minutes to 1 minute for faster
  revive windows.