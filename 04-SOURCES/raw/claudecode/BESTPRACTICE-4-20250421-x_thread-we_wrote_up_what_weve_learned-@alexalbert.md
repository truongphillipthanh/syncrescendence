---
url: https://x.com/alexalbert__/status/1914333320877584397
author: "@alexalbert__"
captured_date: 2025-04-21
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

Check out the blog post for more details and more best practices:

[Claude Code Best Practices - Anthropic](https://anthropic.com)