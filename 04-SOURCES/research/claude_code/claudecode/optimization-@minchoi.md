The creator of Claude Code literally dropped how he uses Claude Code
Bookmark this.

1. Run 5 Claudes in parallel in terminal tabs 1–5, with notifications when input is needed.
https://code.claude.com/docs/en/terminal-config#iterm-2-system-notifications

2. Run 5-10 Claudes on http://claude.ai/code + local. Hand off via & teleport between them, and start/check sessions daily.

3. Use Opus 4.5 (thinking) for everything, less steering + better tools means it’s usually fastest overall.

4. Team shares one git-tracked (9) Boris Cherny on X: "9/ We use a PostToolUse hook to format Claude's code. Claude usually generates well-formatted code out of the box, and the hook handles the last 10% to avoid formatting errors in CI later. https://t.co/XBMG5fmK4P" / X, updates it often so Claude avoids past mistakes; other teams own theirs.
```
"PostToolUse": [
	{
		"matcher": "Write|Edit",
		"hooks": [
			{
				"type": "command",
				"command": "bun run format || true"
			}
		]
``` 
5. In code review, Tag @.claude on PRs to update http://CLAUDE.md via Claude Code GitHub Action, so called “Compounding Engineering.”

6. Most sessions start in Plan mode (Shift+Tab x2). Refine the PR plan, then switch to auto-accept edits0Claude usually 1-shot3. Use Opus 4.5 (thinking) for everything, less steering + better tools means it’s usually fastest overall.s it.
``` 
> i want to improve progress notification rendering for skills. can you make it look and feel a bit more like subagent progress?
—
“ plan mode on (shift+tab to cycle)
``` 

7/ Use slash commands for daily inner-loop work—versioned in .claude/command(9) Boris Cherny on X: "9/ We use a PostToolUse hook to format Claude's code. Claude usually generates well-formatted code out of the box, and the hook handles the last 10% to avoid formatting errors in CI later. https://t.co/XBMG5fmK4P" / X/. Run /commit-push-pr dozens of times, using inline bash to precompute git info.