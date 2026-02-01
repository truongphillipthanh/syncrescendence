url: https://x.com/bcherny/status/2007179832300581177
author: Boris Cherny (@bcherny)
captured_date: 2026-01-17
```

# How I Use Claude Code: My Setup and Workflow

I'm Boris and I created Claude Code. Lots of people have asked how I use Claude Code, so I wanted to show off my setup a bit.

My setup might be surprisingly vanilla! Claude Code works great out of the box, so I personally don't customize it much. There is no one correct way to use Claude Code: we intentionally build it in a way that you can use it, customize it, and hack it however you like. Each person on the Claude Code team uses it *very* differently.

So, here goes.

---

## 1/ Running Multiple Claudes in Parallel

I run 5 Claudes in parallel in my terminal. I number my tabs 1-5, and use system notifications to know when a Claude needs input: https://code.claude.com/docs/en/terminal-config#iterm-2-system-notifications

(Description: Terminal screenshot showing iTerm2 progress indicator and build output. Console displays multiple import statements, bash script commands for SDK compilation including agent generation, typecheck verification, and linting operations. Output shows successful build completion with timestamps.)

---

## 2/ Web-Based Claude Sessions

I also run 5-10 Claudes on claude.ai/code, in parallel with my local Claudes. As I code in my terminal, I will often hand off local sessions to web (using &), or manually kick off sessions in Chrome, and sometimes I will --teleport back and forth. I also start a few sessions from my phone (from the Claude iOS app) every morning and throughout the day, and check in on them later.

(Description: Claude Code web interface research preview showing session management. Displays "Strengthen prompting to encourage claude to enter plan mode more often" with dropdown menus for claude-cli-internal, main branch, and Default settings. Below shows Sessions panel with Claude Code tasks including "Verify guide agent URLs are correct," "Deprecate datsync and migrate to read/write," "Add /fuzz command with parallel agent research," and "Fix background bash freezing issue.")

---

## 3/ Using Opus 4.5 with Thinking

I use Opus 4.5 with thinking for everything. It's the best coding model I've ever used, and even though it's bigger & slower than Sonnet, since you have to steer it less and it's better at tool use, it is almost always faster than using a smaller model in the end.

---

## 4/ Team CLAUDE.md File

Our team shares a single CLAUDE.md for the Claude Code repo. We check it into git, and the whole team contributes multiple times a week. Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time.

Other teams maintain their own CLAUDE.md's. It is each team's job to keep theirs up to date.

(Description: Bash script showing Claude development workflow. File content displays:
```
claude-cli $ cat CLAUDE.md
# Development Workflow

**Always use `bun`, not `npm`.**
```sh
# 1. Make changes

# 2. Typecheck (fast)
bun run typecheck

# 3. Run tests
bun run test -- --t "test name"         # Single suite
bun run test:file -- "glob"             # Specific files

# 4. Lint before committing
bun run lint:file -- "files.ts"          # Specific files
bun run lint                             # All files

# 5. Before creating PR
bun run lint:claude 66 bun run test
```
)

---

## 5/ Code Review Integration with Claude Agent

During code review, I will often tag @.claude on my coworkers' PRs to add something to the CLAUDE.md as part of the PR. We use the Claude Code Github action (/install-github-action) for this. It's our version of @danshipper's Compounding Engineering.

(Description: GitHub pull request discussion screenshot. Shows bcherny commenting "no: use a string literal, not to enum" with @claude mention. Claude responds 3 days ago (edited) with "Finished @bcherny's task in 38s — View job". Below shows PR checklist for "Adding enum guidance to CLAUDE.md" with checkboxes for: Read current CLAUDE.md to understand existing guidance, Update CLAUDE.md to strengthen "no enum" guidance, Commit the change. Updated CLAUDE.md line 36 from: `- Prefer 'type' over 'interface': avoid 'enum' (use string unions)` to `- Prefer 'type' over 'interface': answer use 'mun'ex (use string literal unions instead!)`.)

---

## 6/ Plan Mode for Structured Thinking

Most sessions start in Plan mode (shift+tab twice). If my goal is to write a Pull Request, I will use Plan mode, and go back and forth with Claude until I like its plan. From there, I switch into auto-accept edits mode and Claude can usually 1-shot it. A good plan is really important!

(Description: Claude Code prompt showing plan mode request: "i want to improve progress notification rendering for skills. can you make it look and feel a bit more like subagent progress?" with response showing "plan mode on (shift+tab to cycle)")

---

## 7/ Slash Commands for Workflow Automation

I use slash commands for every "inner loop" workflow that I end up doing many times a day. This saves me from repeated prompting, and makes it so Claude can use these workflows, too. Commands are checked into git and live in .claude/commands/.

For example, Claude and I use a /commit-push-pr slash command dozens of times every day. The command uses inline bash to pre-compute git status and a few other pieces of info to make the command run quickly and avoid back-and-forth with the model: https://code.claude.com/docs/en/slash-commands#bash-command-execution

(Description: Terminal showing slash command definition:
```
> /commit-push-pr [
  /commit-push-pr         Commit, push, and open a PR
```
)

---

## 8/ Subagents for Specialized Tasks

I use a few subagents regularly: code-simplifier simplifies the code after Claude is done working, verify-app has detailed instructions for testing Claude Code end to end, and so on. Similar to slash commands, I think of subagents as automating the most common workflows that I do for most PRs.

(Description: File directory tree showing `.claude/agents/` structure with the following subagents listed:
- build-validator.md
- code-architect.md
- code-simplifier.md
- oncall-guide.md
- verify-app.md
)

---

## 9/ PostToolUse Hook for Code Formatting

We use a PostToolUse hook to format Claude's code. Claude usually generates well-formatted code out of the box, and the hook handles the last 10% to avoid formatting errors in CI later.

(Description: JSON configuration showing PostToolUse hook setup:
```json
"PostToolUse": [
  {
    "matcher": "Write|Edit",
    "hooks": [
      {
        "type": "command",
        "command": "bun run format || true"
      }
    ]
  }
]
```
)

---

## 10/ Permissions Configuration

I don't use --dangerously-skip-permissions. Instead, I use /permissions to pre-allow common bash commands that I know are safe in my environment, to avoid unnecessary permission prompts. Most of these are checked into .claude/settings.json and shared with the team.

(Description: Claude Code permissions configuration interface showing:
- `/permissions` command with tabs: Allow, Ask, Deny, Workspace
- "Claude Code won't ask before using allowed tools"
- Search field
- Numbered list of pre-allowed bash commands (items 12-21 visible):
  - 12. Bash(bq query:*)
  - 13. Bash(bun run build:*)
  - 14. Bash(bun run lint:file:*)
  - 15. Bash(bun run test:*)
  - 16. Bash(bun run test:file:*)
  - 17. Bash(bun run typecheck:*)
  - 18. Bash(bun test:*)
  - 19. Bash(cc:*)
  - 20. Bash(comm:*)
  - 21. Bash(find:*)
)

---

## 11/ External Tools Integration

Claude Code uses all my tools for me. It often searches and posts to Slack (via the MCP server), runs BigQuery queries to answer analytics questions (using bq CLI), grabs error logs from Sentry, etc. The Slack MCP configuration is checked into our .mcp.json and shared with the team.

(Description: Configuration file showing `.mcp.json` setup with "mcpServers" object containing "slack" configuration)

---

**Thread posted:** January 2, 2026 at 11:58 AM  
**Views:** 7.4M | **Replies:** 1.2K | **Reposts:** 7.8K | **Likes:** 51K | **Bookmarks:** 99K