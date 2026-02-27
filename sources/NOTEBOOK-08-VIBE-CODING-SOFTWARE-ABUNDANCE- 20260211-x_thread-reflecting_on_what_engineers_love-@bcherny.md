---
url: https://x.com/bcherny/status/2021699851499798911
author: Boris Cherny (@bcherny)
captured_date: 2026-02-11
---

# Claude Code Customization Thread

Reflecting on what engineers love about Claude Code, one thing that jumps out is its customizability: hooks, plugins, LSPs, MCPs, skills, effort, custom agents, status lines, output styles, etc.

Every engineer uses their tools differently. We built Claude Code from the ground up to not just have great defaults, but to also be incredibly customizable. This is a reason why developers fall in love with the product, and why Claude Code's growth continues to accelerate.

I wanted to share a few ways we're seeing people and teams customize their Claudes.

---

## 1/ Configure your terminal

- **Theme:** Run `/config` to set light/dark mode
- **Notifs:** Enable notifications for iTerm2, or use a custom notifs hook
- **Newlines:** If you use Claude Code in an IDE terminal, Apple Terminal, Warp, or Alacrity, run `/terminal-setup` to enable shift+enter for newlines (so you don't need to type \\)
- **Vim mode:** run `/vim`

(Description: Code block showing Claude Code v2.1.38 configuration menu with Theme selection options including Dark mode, Light mode with checkmark, Dark mode (colorblind-friendly), Light mode (colorblind-friendly), Dark mode (ANSI colors only), and Light mode (ANSI colors only), followed by JavaScript code: `function greet() { console.log("Hello, World!"); }`)

---

## 2/ Adjust effort level

Run `/model` to pick your preferred effort level. Set it to:
- Low, for less tokens & faster responses
- Medium, for balanced behavior
- High, for more tokens & more intelligence

Personally, I use High for everything.

(Description: Configuration menu showing "High effort (default) ← → to adjust" with text "Fast mode is ON and available with Opus 4.6 off fast mode. Now 50% off through Feb 16." and "Enter to confirm · Esc to exit")

---

## 3/ Install Plugins, MCPs, and Skills

Plugins let you install LSPs (now available for every major language), MCPs, skills, agents, and custom hooks.

Install a plugin from the official Anthropic plugin marketplace, or create your own marketplace for your company. Then, check the

(Description: Screenshot showing Plugins interface with Code review tab, displaying Marketplace (claude-code-marketplace) as the source)

---

## 4/ Create custom agents

To create custom agents, drop `.md` files in `.claude/agents`. Each agent can have its own custom system prompt and configuration.

(Description: Configuration interface showing custom agent setup options)

---

## 5/ Pre-approve common permissions

Claude Code uses a sophisticated permission system with a combo of prompt injection detection, static analysis, sandboxing, and human oversight.

Out of the box, we pre-approve a small set of safe commands. To pre-approve more, run `/permissions`

(Description: Permissions dialog showing Allow/Ask/Deny/Work tabs with searchable list of bash commands including:
- Bash(gh issue view:*)
- Bash(gh pr checks:*)
- Bash(gh pr comment:*)
- Bash(gh pr diff:*)
- Bash(gh pr list:*)
- Bash(gh pr view:*)
- Bash(gh repo view:*)
- Bash(gh run list:*)

Text noting: "Claude Code won't ask before using all pre-approved permissions")

---

## 6/ Enable sandboxing

Opt into Claude Code's open source sandbox runtime (github.com/anthropic-experimental/sandbox-runtime) to improve safety while reducing permission prompts. Run `/sandbox` to enable it. Sandboxing runs on:

1. Sandbox BashTool, with auto-allow (commands will try to run outside of the sandbox fallback to regular permissions respected)
2. Sandbox BashTool, with regular permissions
3. No Sandbox

Auto-allow mode: Commands will try to run in the sandbox. If they can't, they fallback to regular permissions respected.

(Description: Sandbox configuration options showing three modes for BashTool behavior)

---

## 7/ Add a status line

Custom status lines show up right below the composer, and let you show model, directory, remaining context, cost, and pretty much anything else you want to see while you work.

Everyone on the Claude Code team has a different statusline. Use `/statusline` to

(Description: Terminal interface showing custom status line with format: `[Opus] 🗂️ my-app | 🌿 feature/auth` followed by progress bar showing `42% | $0.08 | ⏱️ 7m 3s`)

---

## 8/ Customize your keybindings

Did you know every key binding in Claude Code is customizable? `/keybindings` to re-map any key. Settings live reload so you can see how it feels immediately.

(Description: Claude Code Docs page showing "Configuration" section with "Customize keyboard shortcuts" header and text "Customize keyboard shortcuts in Claude Code with a keybindings configuration file." linking to "Customize keyboard shortcuts - Claude Code Docs")

---

## 9/ Set up hooks

Hooks are a way to deterministically hook into Claude's lifecycle. Use them to:
- Automatically route permission requests to Slack or Opus
- Nudge Claude to keep going when it reaches the end of a turn (you can even kick off an agent or use a prompt to decide

(Description: Claude Code Docs page showing "Reference" section with "Hooks reference" header and descriptive text about hook events, configuration schema, and JSON input/output formats, linking to "Hooks reference - Claude Code Docs")

---

## 10/ Customize your spinner verbs

It's the little things that make CC feel personal. Ask Claude to customize your spinner verbs to add or replace the default list with your own verbs. Check the settings.json into source control to share verbs with your team.

(Description: Terminal interface showing Claude Code v2.1.22 update prompt with custom spinner verb configuration: `in my settings, make my spinner verbs star trek themed.` followed by bullet point for Update(~/.claude/settings.json) and "Beaming up..." status message with "Esc to interrupt" prompt)

---

## 11/ Use output styles

Run `/config` and set an output style to have Claude respond using a different tone or format.

We recommend enabling the "explanatory" output style when getting familiar with a new codebase, to have Claude explain frameworks and code patterns as it works.

(Description: Code block showing Insight section with three technical details:
- **Rate limiting at the middleware layer:** Using fixed-window counters with rate-limit header tracking and Redis storage with 24-hour TTL
- **Idempotency keys on mutations:** POST/PUT/PATCH endpoints with Redis storage for key tracking
- **Cursor-based pagination over offset:** /items endpoint with page/offset parameters)

---

## 12/ Customize all the things!

Claude Code is built to work great out of the box. When you do customize, check your settings.json into git so your team can benefit, too. We support configuring for your codebase, for a sub-folder, for just yourself, or via enterprise-wide.

(Description: Claude Code Docs page showing "Configuration" section with "Claude Code settings" header and text "Configure Claude Code with global and project-level settings, and environment variables." linking to "Claude Code settings - Claude Code Docs")