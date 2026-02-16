# REF: Hooks & Automation Formalization

**Version**: 1.0.0
**Created**: 2026-02-10
**Linear**: SYN-15 / IMPL-A-0015
**Status**: CANONICAL

---

## Overview

Syncrescendence uses 6 Claude Code hooks plus 1 supplementary script to automate session lifecycle events. All hooks are bash scripts in `00-ORCHESTRATION/scripts/`. They fire automatically based on Claude Code event triggers.

---

## Hooks Inventory

### 1. session_log.sh — Session Metadata

| Property | Value |
|----------|-------|
| **Event** | Stop |
| **Script** | `00-ORCHESTRATION/scripts/session_log.sh` (38 lines) |
| **Output** | `00-ORCHESTRATION/state/DYN-SESSION_LOG.md` |
| **Function** | Captures timestamp, branch, last 5 commits, files changed |
| **Compaction** | None (append-only) |
| **Performance** | <1s |

**Output Format**:
```markdown
### YYYY-MM-DD HH:MM:SS | Branch: main
**Recent commits**:
```
<5 oneline commits>
```
**Changes**: N files changed, X insertions(+), Y deletions(-)
```

---

### 2. ajna_pedigree.sh — Decision Lineage

| Property | Value |
|----------|-------|
| **Event** | Stop |
| **Script** | `00-ORCHESTRATION/scripts/ajna_pedigree.sh` (73 lines) |
| **Output** | `00-ORCHESTRATION/state/DYN-PEDIGREE_LOG.md` |
| **Function** | Captures decision trail: last 10 commits (6h window), categorized file touches (state/CANON/ENGINE), queued intention count |
| **Compaction** | Ad-hoc manual (86 sessions archived 2026-02-09) |
| **Performance** | <2s |

**Output Format**:
```markdown
## Session: YYYY-MM-DD HH:MM:SS
**Branch**: main | **Fingerprint**: abc1234 | **Commits**: N

### Commits
<10 oneline commits from last 6 hours>

### State Files Touched
<filtered list>

### CANON Files Touched
<filtered list>

### ENGINE Files Touched
<filtered list>

### Queued Intentions
N intention(s) captured by Intent Compass this session.
```

---

### 3. create_execution_log.sh — Execution Staging

| Property | Value |
|----------|-------|
| **Event** | Stop (also callable manually) |
| **Script** | `00-ORCHESTRATION/scripts/create_execution_log.sh` (67 lines) |
| **Output** | `00-ORCHESTRATION/state/DYN-EXECUTION_STAGING.md` |
| **Function** | Logs directive ID, outcome, branch, fingerprint, commit count, file changes |
| **Compaction** | **Automatic at 10 entries** via `compact_wisdom.sh` |
| **Performance** | <2s (plus compaction time if triggered) |
| **Args** | `bash create_execution_log.sh "DIRECTIVE_ID" "OUTCOME" ["DETAILS"]` |

**Auto-compact trigger** (line 57): When entry count >= 10, calls `compact_wisdom.sh` and auto-commits.

---

### 4. pre_compaction.sh — Compaction Guard

| Property | Value |
|----------|-------|
| **Event** | PreCompact |
| **Script** | `00-ORCHESTRATION/scripts/pre_compaction.sh` (37 lines) |
| **Output** | Console warnings (no file output) |
| **Function** | Blocks context compaction if repo has uncommitted changes in protected dirs |
| **Checks** | `git diff --quiet`, untracked files in `00-ORCHESTRATION/state/`, `02-ENGINE/`, `05-SIGMA/` |
| **Override** | `COMPACTION_OVERRIDE=1` environment variable |
| **Exit Codes** | 0 = clean (proceed), 2 = dirty (BLOCKS compaction) |
| **Performance** | <1s |

---

### 5. intent_compass.sh — Intention Signal Capture

| Property | Value |
|----------|-------|
| **Event** | UserPromptSubmit |
| **Script** | `00-ORCHESTRATION/scripts/intent_compass.sh` (51 lines) |
| **Output** | `00-ORCHESTRATION/state/DYN-INTENTIONS_QUEUE.md` |
| **Function** | Scans every user prompt for intention-laden language, captures matched signals |
| **Dependency** | `jq` (silent exit if unavailable) |
| **Compaction** | Manual triage into `ARCH-INTENTION_COMPASS.md` |
| **Performance** | <10ms (must not block prompt submission) |

**Signal Patterns** (case-insensitive):
```
I want | we should | we need | don't forget | make sure | priority |
must have | let's | going forward | from now on | always | never again |
remember to | important that | critical that | we'll need | tall order |
massive | manhattan | codify | formalize | operationalize
```

**Output Format**: `- **YYYY-MM-DD HH:MM:SS** | \`<first match, 200 chars max>\``

---

### 6. compact_wisdom.sh — Staging Compactor

| Property | Value |
|----------|-------|
| **Event** | Manual / auto-triggered by `create_execution_log.sh` |
| **Script** | `00-ORCHESTRATION/scripts/compact_wisdom.sh` (77 lines) |
| **Inputs** | `DYN-DIRECTIVE_STAGING.md`, `DYN-EXECUTION_STAGING.md` |
| **Outputs** | `00-ORCHESTRATION/archive/ARCH-DIRECTIVE_COMPENDIUM.md`, `ARCH-EXECUTION_HISTORY.md` |
| **Function** | Appends staging entries to archive compendiums, resets staging files |
| **Auto-commit** | YES (`git add` + `git commit -m "chore: auto-compact wisdom..."`) |

---

### Supplementary: post_commit_ledger.sh

| Property | Value |
|----------|-------|
| **Event** | PostToolUse (after git commit) |
| **Script** | `00-ORCHESTRATION/scripts/post_commit_ledger.sh` |
| **Function** | Advisory: flags when CSV ledgers may need updating based on committed file patterns |
| **Blocking** | No (purely informational) |

---

## Event → Script Matrix

| Event | Scripts Fired | Blocking? |
|-------|--------------|-----------|
| **Stop** | session_log.sh, ajna_pedigree.sh, create_execution_log.sh | No |
| **PreCompact** | pre_compaction.sh | YES (exit 2 blocks) |
| **UserPromptSubmit** | intent_compass.sh | No |
| **PostToolUse** (git commit) | post_commit_ledger.sh | No |

---

## Data Flow: Staging → Archive Pipeline

```
User Prompt
  → intent_compass.sh → DYN-INTENTIONS_QUEUE.md
                           ↓ (manual triage)
                         ARCH-INTENTION_COMPASS.md

Session End
  → session_log.sh → DYN-SESSION_LOG.md (append-only)
  → ajna_pedigree.sh → DYN-PEDIGREE_LOG.md (ad-hoc compact)
  → create_execution_log.sh → DYN-EXECUTION_STAGING.md
                                 ↓ (at 10 entries)
                               compact_wisdom.sh
                                 ↓
                               ARCH-EXECUTION_HISTORY.md

Context Compaction (/compact)
  → pre_compaction.sh → BLOCK if dirty, PASS if clean
```

---

## Compaction Policy

| Staging File | Threshold | Target Archive | Auto-commit |
|-------------|-----------|---------------|-------------|
| DYN-EXECUTION_STAGING.md | 10 entries | ARCH-EXECUTION_HISTORY.md | YES |
| DYN-DIRECTIVE_STAGING.md | 10 entries | ARCH-DIRECTIVE_COMPENDIUM.md | YES |
| DYN-PEDIGREE_LOG.md | Ad-hoc | Inline archival (header note) | Manual |
| DYN-SESSION_LOG.md | None | Append-only (grows) | — |
| DYN-INTENTIONS_QUEUE.md | Manual | ARCH-INTENTION_COMPASS.md | Manual |

---

## Configuration

Hooks are registered in `.claude/settings.json` at the project level. The canonical registration is also documented in `CLAUDE.md` (lines 136-148).

```json
{
  "hooks": {
    "Stop": [
      { "command": "bash 00-ORCHESTRATION/scripts/session_log.sh" },
      { "command": "bash 00-ORCHESTRATION/scripts/ajna_pedigree.sh" },
      { "command": "bash 00-ORCHESTRATION/scripts/create_execution_log.sh" }
    ],
    "PreCompact": [
      { "command": "bash 00-ORCHESTRATION/scripts/pre_compaction.sh" }
    ],
    "UserPromptSubmit": [
      { "command": "bash 00-ORCHESTRATION/scripts/intent_compass.sh" }
    ]
  }
}
```

---

## Verification

Check hooks are firing:
```bash
# Recent session logs (Stop hooks)
tail -20 00-ORCHESTRATION/state/DYN-SESSION_LOG.md

# Recent pedigree entries (Stop hooks)
tail -30 00-ORCHESTRATION/state/DYN-PEDIGREE_LOG.md

# Recent intentions captured (UserPromptSubmit)
tail -10 00-ORCHESTRATION/state/DYN-INTENTIONS_QUEUE.md

# Execution staging entry count
grep -c "^### " 00-ORCHESTRATION/state/DYN-EXECUTION_STAGING.md

# Pre-compaction guard test
COMPACTION_OVERRIDE=0 bash 00-ORCHESTRATION/scripts/pre_compaction.sh; echo "Exit: $?"
```

---

## Cross-References

- `CLAUDE.md` (lines 136-148) — Hooks registration table
- `05-SIGMA/mechanics/MECH-hooks_lifecycle_automation.md` — Generic Claude Code hook theory
- `02-ENGINE/TEMPLATE-EXECUTION_LOG.md` — Execution log format template
- `00-ORCHESTRATION/archive/ARCH-EXECUTION_HISTORY.md` — Compacted execution history
