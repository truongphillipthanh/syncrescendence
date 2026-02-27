# TASK-20260206-enable_claude_code_agent_teams_userwide

**From**: phillip
**To**: Psyche (MBA)
**Issued**: 2026-02-06
**Kind**: TASK
**Priority**: P0
**Exit-Code**: 0
**Completed-At**: 2026-02-07T06:47:41Z
**Claimed-At**: 2026-02-07T06:47:41Z
**Claimed-By**: psyche-Lisas-MacBook-Air
**Status**: COMPLETE
**Kanban**: DONE

---

## Objective

Enable Claude Code "agent teams" user-wide on Psyche (MacBook Air) by setting:

- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

User-wide means modifying `~/.claude/settings.json`.

## Steps

1. Inspect existing file:
   - `cat ~/.claude/settings.json` (create if missing)
2. Add/merge into JSON:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Do **not** remove existing keys (merge).

3. Save a timestamped backup of the prior file:
   - `~/.claude/settings.json.bak.<YYYYMMDD-HHMMSS>`

4. Confirm by printing the resulting file.

## Completion

- Set **Status** above to COMPLETE
- Write a short RESULT receipt to `-INBOX/psyche/RECEIPTS/RESULT-psyche-20260206-enable_claude_code_agent_teams_userwide.md` including:
  - whether file existed
  - backup path
  - final JSON snippet
