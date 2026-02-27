---
id: SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned
platform: x
format: thread
creator: alexalbert
title: we wrote up what weve learned
status: triaged
original_filename: "3-BestPractice_ProTiips--4-20250421-x_thread-we_wrote_up_what_weve_learned-@alexalbert.md"
url: https://x.com/alexalbert__/status/1914333320877584397
author: "@alexalbert__"
captured_date: 2025-04-21
signal_tier: strategic
topics:
  - "claude-code"
  - "best-practices"
  - "developer-tools"
  - "git-workflows"
  - "ai-engineering"
teleology: implement
notebooklm_category: claude-code
aliases:
  - "Alex Albert - Claude Code Best Practices"
synopsis: "Anthropic employee Alex Albert shares internal Claude Code best practices including CLAUDE.md as hidden gem, explore-plan-code workflow, TDD integration, headless mode for CI, multi-Claude review workflows, and git worktree parallelism."
key_insights:
  - "The explore-plan-code workflow dramatically improves quality over letting Claude jump straight to implementation"
  - "Multi-Claude workflow: one writes code while another independently reviews, catching issues the first missed"
  - "Git worktrees enable parallel Claude sessions on separate branches with zero merge conflicts"
---
# Claude Code: Best Practices for Agile Coding

We wrote up what we've learned about using Claude Code internally at Anthropic.

Here are the most effective patterns we've found (many apply to coding with LLMs generally):

(Description: Screenshot of Anthropic blog post card showing "Claude Code: Best practices for agentive coding" with Anthropic branding and icons. Published Apr 18, 2025. Text reads: "Claude Code is a command line tool for agentive coding. This post covers tips and tricks that have proven effective for using Claude Code across various codebases, languages, and environments.")

---

**1/ CLAUDE md files are the main hidden gem.** Simple markdown files that give Claude context about your project - bash commands, code style, testing patterns. Claude loads them automatically and you can add to them with # key

---

**2/ The explore-plan-code workflow is worth trying.** Instead of letting Claude jump straight to coding, have it read files first, make a plan (add "think" for deeper reasoning), then implement.

Quality improves dramatically with this approach.

---

**3/ Test-driven development works very well for keeping Claude focused.** Write tests, commit them, let Claude implement until they pass.

---

**4/ A more tactical one, ESC interrupts Claude, double ESC edits previous prompts.** These shortcuts save lots of wasted work when you spot Claude heading the wrong direction

---

**5/ We're using Claude for codebase onboarding now.** Engineers ask it "why does this work this way?" and it searches git history and code for answers which has cut onboarding time significantly.

---

**6/ For automation, headless mode (claude -p) handles everything from PR labeling to subjective code review beyond what linters catch.**

Or try the --dangerously-skip-permissions mode. Spin up a container and let Claude loose on something like linting or boilerplate generation

---

**7/ The multi-Claude workflow is powerful: one writes code, another follows up behind and reviews.**

You can also use git worktrees for parallel Claude sessions on different features.

---

Claude Code - Hidden-Gem Power Tips
• Seed every repo with a tuned CLAUDE. md - Claude pulls it into every prompt; use # in-session to append live notes, add "IMPORTANT / YOU MUST" for stronger adherence, and run /init to scaffold one instantly.
• Escalate Claude's reasoning on demand - insert the words "think" → "think hard" →
"think harder" → "ultrathink" to unlock larger thinking budgets before it acts.
• Stop or rewind in one keystroke - Esc halts any phase without losing context; double- Esc lets you edit an earlier prompt and branch a new path.
• Bullet-proof autonomy with Safe YOLO - run claude dangerously-skip-permissions only inside an isolated container (no internet) to let Claude mass-fix lint errors or boilerplate unattended.
• Lightning CLAUDE.md hierarchy - supports *root, parent, child, or * ~/. claude locations, so monorepos inherit both global and per-package guidance automatically.
• One-word tool whitelisting - /allowed-tools Edit Bash(git commit:*) (or --allowedTools) removes future permission prompts for trusted actions.
• Turbo-charge context with images - paste screenshots or give file paths; Claude compares mock vs. output visually and iterates UI until pixels match.
• Use the gh CLI as a super-power - Claude speaks gh fluently: drafts PRs, fixes review comments, triages issues, and writes commit messages that cite history.
• Sub-agent sanity checks - ask Claude to spin up sub-agents that independently verify plans or guard against over-fitting to your tests.
• Markdown checklists as scratchpads - have Claude dump giant lint/problem lists to a
•md file, tick off items as it auto-fixes, and keep progress auditable.
• Shift-Tab toggles "auto-accept" - let Claude run without pauses when you trust the current context, then flip it off to resume step-wise control.
• Parallel velocity via git worktrees - spawn several worktrees, one Claude per terminal, each on a separate branch; no merge conflicts, maximum throughput.
• Headless mode for CI bots - claude -p "<prompt>" —output-format stream-json plugs into pipelines to label new GitHub issues or run subjective linting.
• Invoke the golden workflow - Explore → Plan (no code) → Implement → Commit; the upfront plan request dramatically lifts success rates.
• TDD on steroids - let Claude write failing tests, commit them, then iterate code until green; ask a second Claude to review the implementation cold.
• Power-phrase file targeting - tab-complete file names in prompts so Claude jumps to exactly the right locations, saving context budget.
• **Debug MCP setups with **--mcp-debug - prints a verbose trace of server discovery and tool hand-offs to surface config mistakes instantly. Keep these in your muscle memory and Claude Code jumps from helpful to game-changing.

Check out the blog post for more details and more best practices:

[Claude Code Best Practices - Anthropic](https://anthropic.com)