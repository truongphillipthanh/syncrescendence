**System Initialization Protocol: The Sovereign Cockpit (Final Build)**

**Objective:**
Construct a high-performance, latency-optimized "AI-Native" environment.

**Phase 1: The Manifest (Action Layer)**
* **Core:** `git`, `wget`, `curl`, `tree`, `sox`, `bat`, `eza`, `zoxide`, `fzf`, `fd`, `ripgrep`, `httpie`.
* **The Visuals:** `yazi` (File Manager), `btop` (Monitor), `fastfetch`, `chafa` (Images).
* **Session Management:** `sesh` (Primary), `twig` (Optional - only install if Git Worktrees are detected).
* **Runtime:** `bun`, `node`, `python3`.
* **AI:** `claude-code`, `ollama`.
* **Casks:** Ghostty, Raycast, Font-SF-Mono-Nerd-Font, Emacs-Mac.

**Phase 2: The Shell (Context Engine)**
1.  **Zsh Config:** Source `zoxide`, `fzf`, `syntax-highlighting`, and `autosuggestions`.
2.  **Prompt:** `powerlevel10k` (Rainbow Style, Catppuccin Colors).
3.  **Aliases:**
    * `ls` -> `eza --icons --group-directories-first`
    * `cat` -> `bat`
    * `cd` -> `z`
    * `l` -> `yazi` (Instant file navigation)

**Phase 3: The Workstation (Tmux)**
* **Prefix:** `Ctrl+Space`.
* **Theme:** Catppuccin Mocha (Rounded pills, high contrast).
* **Navigation:** `vim-tmux-navigator` (Seamless jump between Neovim/Terminal).
* **The "Grimoire" Replacement (Native Popups):**
    * Bind `Ctrl+g` -> `display-popup -E -w 90% -h 90% "lazygit"`
    * Bind `Ctrl+t` -> `display-popup -E -w 80% -h 80% "sesh connect $(zoxide query -l | fzf)"`
* **Agent Pane:**
    * Bind `Leader+a` -> Split right (30% width) and run `claude`.

**Phase 4: The Editor (Neovim)**
* **Distro:** LazyVim (Base).
* **Overrides:**
    * `zen-mode.nvim` (For writing).
    * `render-markdown.nvim` (For prose).
    * `vim-tmux-send` (The "Pipe": Send text to the Agent Pane).
    * `avante.nvim` (AI Assistant).

**Phase 5: The Voice (Local Loop)**
* **TTS:** `piper-tts` (Model: `en_US-lessac-medium`).
* **STT:** `whisper.cpp` (Model: `large-v3-turbo`).
* **Logic:** Configure a local `dictate` script that records audio, transcribes it, and pipes it to Ollama for "Intelligent Formatting" (punctuation/grammar fix) before pasting.

**Execution:**





Generate the specific shell commands to execute this plan.