# TASK: Self-Capability Encoding + Config Cascade Playbook

**Priority**: P1
**Reply-To**: commander
**CC**: commander
**Created**: 2026-02-09

## Objective
Two deliverables:

### Part 1: Capability Encoding
You (Psyche) have full access to manipulate the computer you run on (MacBook Air). This includes:
- **AppleScript** via `osascript` — control any macOS application
- **launchctl** — manage system services and daemons
- **Homebrew** — install any CLI tool
- **Filesystem** — full read/write access
- **Terminal commands** — all standard Unix tools
- **Docker** — container orchestration
- **Git** — version control operations
- **Python/Node/Go** — run any code

Encode this awareness into your MEMORY.md so future sessions know your full capability range.

### Part 2: Configuration Cascade Playbook
Document every CLI tool, config, and permission that Commander installed on Mac mini so you can replicate on MacBook Air:
1. Read the Sovereign Cockpit docs (COCKPIT.md)
2. Check what's already installed on MBA vs Mac mini
3. Create a step-by-step playbook for cascade installation
4. Include: Homebrew formulas, npm globals, pip packages, launchd plists, Ghostty config, tmux config, Neovim setup

## Deliverables
- [ ] Updated MEMORY.md with capability awareness
- [ ] Config cascade playbook as `SOVEREIGN-CASCADE-PLAYBOOK.md` in -SOVEREIGN/

## Context
The Sovereign needs you to know you can manipulate the machine. You're not limited to text I/O — you have root-level system access. Use it.
