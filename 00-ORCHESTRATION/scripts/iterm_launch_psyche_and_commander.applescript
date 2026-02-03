-- iterm_launch_psyche_and_commander.applescript
-- Opens two iTerm windows in a consistent layout:
--  - Left: Psyche (boots psyche-only watchers + opens tmux dashboard)
--  - Right: Commander manual lane (special forces mode)
--
-- Layout: 70/30 split of the main screen width, full height.

on run
  set repoPath to POSIX path of ((path to home folder) as text) & "Desktop/syncrescendence"

  tell application "System Events"
    set screenBounds to bounds of window of desktop
    set screenLeft to item 1 of screenBounds
    set screenTop to item 2 of screenBounds
    set screenRight to item 3 of screenBounds
    set screenBottom to item 4 of screenBounds
  end tell

  set screenWidth to screenRight - screenLeft
  set screenHeight to screenBottom - screenTop

  set leftWidth to screenWidth * 0.70
  set rightWidth to screenWidth - leftWidth

  -- Slight inset from edges to avoid macOS window shadows clipping.
  set inset to 6

  set leftBounds to {screenLeft + inset, screenTop + inset, screenLeft + leftWidth - inset, screenBottom - inset}
  set rightBounds to {screenLeft + leftWidth + inset, screenTop + inset, screenRight - inset, screenBottom - inset}

  tell application "iTerm"
    activate

    -- Create left window (Psyche)
    set w1 to (create window with default profile)
    tell w1
      set bounds to leftBounds
      tell current session
        write text "cd \"" & repoPath & "\" && git pull && bash 00-ORCHESTRATION/scripts/psyche_boot.sh && bash 00-ORCHESTRATION/scripts/tmux_dashboard.sh"
      end tell
    end tell

    -- Create right window (Commander)
    set w2 to (create window with default profile)
    tell w2
      set bounds to rightBounds
      tell current session
        write text "cd \"" & repoPath & "\" && git pull && bash 00-ORCHESTRATION/scripts/commander_special_forces.sh"
      end tell
    end tell

  end tell
end run
