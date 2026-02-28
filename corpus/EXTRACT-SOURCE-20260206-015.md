# Extraction: SOURCE-20260206-015

**Source**: `SOURCE-20260206-x-article-pablostanley-how_i_stopped_worrying_and_learned_to_love_the_terminal.md`
**Atoms extracted**: 27
**Categories**: claim, concept, praxis_hook

---

## Claim (4)

### ATOM-SOURCE-20260206-015-0001
**Lines**: 10-12
**Context**: anecdote / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.50

> The author, a designer, now considers the terminal their design tool of choice, finding traditional GUI tools like Figma to feel "old-school" by comparison.

### ATOM-SOURCE-20260206-015-0003
**Lines**: 33-38
**Context**: anecdote / evidence
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Using the terminal with AI assistance (like Claude Code) enables faster iteration and the ability to ship working prototypes and products (e.g., efecto.app and remoto.sh) because the code is "real from the start," unlike traditional design tools that produce static mockups.

### ATOM-SOURCE-20260206-015-0017
**Lines**: 126-128
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Vercel's `skills.sh` is an open directory for developers to share reusable AI skills, including best practices from companies like Stripe.

### ATOM-SOURCE-20260206-015-0027
**Lines**: 159-159
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.60, actionability=0.80, epistemic_stability=0.90

> The `claude --dangerously-skip-permissions` command will stop Claude from asking for permissions, as its name implies.

## Concept (2)

### ATOM-SOURCE-20260206-015-0002
**Lines**: 25-31
**Context**: anecdote / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The shift in the author's perception of the terminal from a "scary" tool requiring command memorization to a conversational interface, enabled by AI tools like Claude Code, which allows users to describe desired outcomes rather than input specific commands.

### ATOM-SOURCE-20260206-015-0016
**Lines**: 118-121
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Claude Code's "skills" are custom commands defined in `.claude/commands/` that the AI can dynamically invoke based on user intent, such as optimizing images or generating social cards.

## Praxis Hook (21)

### ATOM-SOURCE-20260206-015-0004
**Lines**: 50-62
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To navigate the terminal without memorizing many commands: use `cd` to change directories (dragging and dropping folders into the terminal for full path), `npm run dev` to test locally, `ctrl+r` to search command history, and `claude` to run Claude Code and then converse with it.

### ATOM-SOURCE-20260206-015-0005
**Lines**: 70-73
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When using components, prioritize accessible primitives like shadcn/ui or radix, as they are easily customizable with tailwindcss and generally high-quality out-of-the-box.

### ATOM-SOURCE-20260206-015-0006
**Lines**: 72-75
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> When using AI for development, start with a clear plan using "plan mode" (e.g., Shift+Tab twice in Claude Code) to ensure the AI understands the approach, which improves first-try success rates.

### ATOM-SOURCE-20260206-015-0007
**Lines**: 75-75
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> For icon-only buttons, add `aria-labels` to improve accessibility.

### ATOM-SOURCE-20260206-015-0008
**Lines**: 75-76
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When animating, avoid layout properties like width, height, or margins; instead, use `transform` and `opacity` for smoother transitions.

### ATOM-SOURCE-20260206-015-0009
**Lines**: 76-76
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Use `ease-out` for entrance transitions in animations.

### ATOM-SOURCE-20260206-015-0010
**Lines**: 77-78
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Provide the AI with a mechanism to verify its work; for UI, use a headless browser like Agent Browser that the AI can control to open pages, take screenshots, click elements, and test responsive design by resizing the viewport.

### ATOM-SOURCE-20260206-015-0011
**Lines**: 83-86
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> To increase productivity, run multiple Claude sessions simultaneously (e.g., 3-5 terminal tabs and web sessions) to parallelize tasks like component building, test writing, and research.

### ATOM-SOURCE-20260206-015-0012
**Lines**: 90-96
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> When using multiple AI agents like Claude on the same project, utilize `git worktrees` and separate branches for each agent to prevent file conflicts and allow isolated work, testing, and PR creation.

### ATOM-SOURCE-20260206-015-0013
**Lines**: 103-106
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Use Sharp for programmatic image generation (e.g., grids of avatars, placeholder images, social cards) to avoid manual design tool processes.

### ATOM-SOURCE-20260206-015-0014
**Lines**: 106-107
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Utilize ffmpeg for video and GIF manipulation tasks such as trimming, compressing, format conversion, and frame extraction.

### ATOM-SOURCE-20260206-015-0015
**Lines**: 109-112
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Create and reuse scripts for repetitive image and video tasks (e.g., batch-compressing PNGs, converting screen recordings to GIFs) to build a library of utilities that AI can access.

### ATOM-SOURCE-20260206-015-0018
**Lines**: 132-134
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Use MCP (Multi-Context Protocol) to connect Claude Code with other tools like Figma, Notion, Slack, Google Drive, and Blender, allowing direct context pulling into conversations.

### ATOM-SOURCE-20260206-015-0019
**Lines**: 136-139
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Install the GitHub Action for Claude Code using `/install-github-app` to enable `@claude` mentions in PR comments or issues for feature implementation, bug fixes, and code reviews, adhering to `CLAUDE.md` guidelines.

### ATOM-SOURCE-20260206-015-0020
**Lines**: 141-143
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Install the Vercel plugin for Claude Code using `/plugin install vercel@claude-plugins-official` to enable direct deployment with `/deploy` and log checking with `/vercel-logs`.

### ATOM-SOURCE-20260206-015-0021
**Lines**: 142-144
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To learn more about Claude Code, consult the official Claude Code documentation and the Chrome extension for browser-based testing.

### ATOM-SOURCE-20260206-015-0022
**Lines**: 145-148
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Maintain a `CLAUDE.md` file in your project to document design patterns, preferences, and rules; Claude reads this file at the start of each session and can update it itself, ensuring consistency.

### ATOM-SOURCE-20260206-015-0023
**Lines**: 146-146
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For image-related tasks, consider using Sharp and ffmpeg.

### ATOM-SOURCE-20260206-015-0024
**Lines**: 147-147
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To integrate design tools, investigate MCP.

### ATOM-SOURCE-20260206-015-0025
**Lines**: 148-149
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For a gradual entry into visual-first options with terminal superpowers (github, repos, branching, virtual machines), v0 is a suitable choice.

### ATOM-SOURCE-20260206-015-0026
**Lines**: 155-157
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.70

> To bypass permission prompts in Claude, if confident in the desired outcome and Claude's capability, use the command `claude --dangerously-skip-permissions`.
