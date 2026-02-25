# SIEGE CC___ — <Agent> <TOPIC>

**Destination**:
  - **App**: <Codex Desktop App | Fresh Claude Code session>
  - **Relay**: <paste prompt | open file in app | `@ engine/02-ENGINE/certescence/siege/CC___/PROMPT-...-SIEGE-CC___.md`>
  - **Results land at**: <agent commits to repo | writes RESULT file to outbox>
  - **After completion**: Commander reads results from `agents/commander/outbox/` or git log

**Agent**: <Agent name> (<Model>)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: ____-__-__
**CC Session**: CC___
**Reply-To**: commander
**CC**: commander

---

## TASKS

### TASK 1: ___

**Context**: <Why this task exists — link to ascertescence finding or Sovereign directive>

**Build/Modify**: `<file path>`

**Requirements**:
1. ___
2. ___
3. ___

**Verify**: <How to prove it works>

**Commit as**: `<semantic prefix>: <message>`

---

### TASK 2: ___

...

---

## CONSTRAINTS
- Commit each task separately with semantic prefix
- Do not modify AGENTS.md or CLAUDE.md
- Do not create new top-level directories
- Run verification before claiming done
- Write RESULT files to `agents/commander/outbox/RESULT-<AGENT>-CC<N>-<TOPIC>.md`
