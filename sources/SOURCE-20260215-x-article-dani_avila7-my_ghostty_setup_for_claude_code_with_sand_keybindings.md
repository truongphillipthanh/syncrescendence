---
url: https://x.com/dani_avila7/status/2023151176758268349
author: "Daniel San (@dani_avila7)"
captured_date: 2026-02-15
id: SOURCE-20260215-006
original_filename: "20260215-x_article-my_ghostty_setup_for_claude_code_with_sand_keybindings-@dani_avila7.md"
status: triaged
platform: x
format: article
creator: dani_avila7
signal_tier: tactical
topics: [claude-code, developer-tools, tutorial, git-workflows]
teleology: implement
notebooklm_category: coding-tools
aliases: ["dani_avila7 - Ghostty SAND keybindings for Claude Code"]
synopsis: "Explains why Ghostty terminal is superior to VSCode's terminal for Claude Code sessions (VSCode crashes under AI-scale output), and introduces the SAND mnemonic for panel management: Split, Across, Navigate, Destroy. Shows how to run multiple Claude Code instances in parallel using git worktrees."
key_insights:
  - "VSCode terminal crashes on long Claude Code sessions even on M4 - a dedicated terminal like Ghostty is more stable"
  - "SAND mnemonic (Split/Across/Navigate/Destroy) makes Ghostty panel management second nature"
  - "Combining Ghostty splits with git worktrees enables multi-agent parallel development from one terminal"
---
# My Ghostty setup for Claude Code with SAND Keybindings
## First... Why I Switched to Ghostty
After months using Claude Code daily I realized I was barely using VSCode or Cursor, just the terminal and git panel, everything else Claude Code handled.
The problem is VSCode's terminal is fragile, long Claude Code sessions crash it, even on an M4. It's not hardware, it's a terminal not built for AI-scale output... I needed a real terminal
(Description: A screenshot showing a VSCode terminal crash dialog with a warning icon and message "The window has crashed (reason: 'crashed'; code: '0')" with "Close" and "Reopen" buttons)
Ghostty came up, community matters and it's built by [@mitchellh](https://x.com/@mitchellh), co-founder of HashiCorp, someone with a serious track record. Ghostty felt future-proof.
(Description: A macOS terminal window displaying the Ghostty logo, showing a sleek dark interface with ASCII art rendering of a stylized face in blue outlined squares)
This is the first of three articles about my workflow with Ghostty and Claude Code I start with my "SAND" keybindings that make panel management second nature
1. My Ghostty setup for Claude Code with SAND Keybindings
2. Monitoring Claude Code changes with Lazygit
3. Parallel agents with Git worktrees and Claude Code
## Getting Started with Ghostty
Download Ghostty from [ghostty.org](https://ghostty.org/) (macOS and Linux). Once installed, you need a configuration file at ~/.config/ghostty/config.
The easiest way to set it up? Open Claude Code and tell it:
> Configure Ghostty with this config: https://gist.github.com/davila7/5b07f55a6e65a06c121da9702d10c2e2
Claude will read the gist, create the config file, and you're done. If you prefer to do it manually:
```bash
mkdir -p ~/.config/ghostty
curl -o ~/.config/ghostty/config https://gist.githubusercontent.com/davila7/5b07f55a6e65a06c121da9702d10c2e2/raw/config
```
## How I Manage Panels in Ghostty
Using Ghostty with Claude Code works best with split panels you might have Claude on one side, git changes on another, maybe a file browser on a third If you can't split, navigate, and close panels without thinking you end up fumbling with shortcuts instead of coding.
I kept forgetting Ghostty's keybindings so I organized them into a mnemonic SAND Four letters, four actions every panel operation falls into one of these categories
## S - Split: Create new panels
Split your terminal into multiple panels.
- Cmd+D splits right (vertical)
- Cmd+Shift+D splits down (horizontal)
(Description: A video demonstrating terminal splitting in Ghostty, showing Claude Code on the left side with a Claude Code panel (version v2.1.42) and demonstrating vertical and horizontal split operations)
## A - Across: Move between tabs
Navigate across tabs.
- Cmd+T opens a new tab
- Cmd+Shift+Left/Right moves between them
(Description: A video showing Ghostty with multiple tabs at the top, displaying lazygit interface showing git status, branches, and commit history with code files visible in the background)
## N - Navigate: Jump between split panels
Move focus between your splits.
- Cmd+Alt+Arrows jumps in any direction
- Cmd+Shift+E equalizes all splits
(Description: A video showing the Navigate function with multiple split panels containing code, git status information, and file listings. Shows cursor movement between split sections and panel resizing)
- Cmd+Shift+F zooms into one panel (press again to restore)
(Description: A video showing Claude Code maximized in fullscreen mode with code editor displaying JavaScript/TypeScript with syntax highlighting, showing the zoom functionality)
## D - Destroy: Close panels and tabs
Close what you don't need.
- Cmd+W closes the current panel or tab
(Description: A video demonstrating closing panels and tabs in Ghostty, showing a terminal environment with colored window decorations and header controls at the top)
## My Workflow Layout
This is what my daily setup looks like, and it scales from 1 to 3 Claude Code instances running in parallel... remember use SAND!
Start simple: one Claude Code panel on the left, S (Cmd+D) to split right, and run [lazygit](https://github.com/jesseduffield/lazygit) there to monitor every commit and diff Claude makes in real time.
(Description: A terminal screenshot showing Claude Code on the left panel with a code editor displaying JavaScript configuration files, and a file tree on the right showing project structure with Claude Code visible at the top)
Then S again (Cmd+Shift+D) to split the right panel down and open [yazi](https://github.com/sxyazi/yazi) as a file browser:
(Description: A terminal screenshot showing three panels: Claude Code v2.1.42 on the left, with code visible in the center panel, and a file browser on the right showing directory listing with various project files and folders highlighted in blue)
But when you're working on multiple tasks, you can split the left side into 2 or 3 Claude Code instances, each running on a different Git worktree:
(Description: A terminal screenshot displaying three Claude Code instances running in parallel on separate panels, each showing different code files and configurations, demonstrating the multi-agent setup with split panels containing code editors and file content)
If some Claude Code panels get too big because you need more context you can press Cmd+Shift+E to equalize all windows and bring them back to a balanced layout
That's the power of combining Ghostty with worktrees you go from a single agent to a multi-agent setup without leaving your terminal
## Tip:
stick a post-it with the letters SAND somewhere you can see it every time you see it, practice the commands after a week you'll have Ghostty fully under control from the keyboard
(Description: A photograph of a yellow sticky note on a white/gray background with the word "SAND" written in gray text)
And if you ever forget a shortcut, just press Cmd + Shift + P to open the Command Palette and see the full list of available commands.
(Description: A video showing the Command Palette in Ghostty displaying a list of available commands with keyboard shortcuts, including options for various terminal operations, split management, and navigation functions)
## Next Articles
This was the first article ehe next two will show how I work with Ghostty and Claude Code
One article will cover **Lazygit**, watch Claude Code's commits, diffs, and branch changes in real time
The other will cover git **worktrees and parallel agents**, run multiple Claude Code instances on different tasks and use **yazi** to browse project files
Follow me to catch the next articles! 👇