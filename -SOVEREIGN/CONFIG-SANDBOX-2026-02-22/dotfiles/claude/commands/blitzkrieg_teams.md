---
name: blitzkrieg_teams
description: Deploy parallel agent teams for multi-lane Blitzkrieg execution
allowed-tools: Read, Write, Edit, Bash(git status:*), Bash(git diff:*), Bash(git add:*), Bash(git commit:*), Glob, Grep
---
# Blitzkrieg Agent Teams

Deploy parallel agent teams for: $ARGUMENTS (or the current directive if not specified)

## Invocation

This command invokes the Blitzkrieg Teams skill defined in `.claude/skills/blitzkrieg_teams.md`. Follow that skill's full procedure.

## Quick Reference

### Steps
1. **Decompose** — List subtasks, identify dependencies, group into independent lanes, assign file scopes
2. **Select pattern** — Scout (research), Strike (implement), or Mixed
3. **Create team** — TeamCreate + TaskCreate + Task (spawn) + TaskUpdate (assign)
4. **Monitor** — TaskList + SendMessage for progress/blockers
5. **Integrate** — Verify lanes, combine outputs, git commit (team lead only)
6. **Shutdown** — SendMessage shutdown_request to all teammates

### Team Patterns
- **blitz-research**: 2-3 Explore agents for parallel information gathering
- **blitz-implement**: 2-4 general-purpose agents for parallel implementation
- **blitz-mixed**: Explore + general-purpose for research-then-implement

### Safety Rails
- Max 4 agents per team
- Explicit file scopes per agent (no overlap)
- Only team lead does git operations
- Verify before marking complete

## Skill Reference
Full procedure: `.claude/skills/blitzkrieg_teams.md`
