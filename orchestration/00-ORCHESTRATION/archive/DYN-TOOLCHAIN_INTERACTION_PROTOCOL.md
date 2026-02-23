# Toolchain Interaction Protocol
## Dispatch System Reference — File-Based Agent Coordination

**Version**: 1.0.0
**Last Updated**: 2026-02-10
**Linear**: SYN-14
**Status**: Operational

---

## Overview

The dispatch system uses a file-based kanban to coordinate work across the Constellation's five agents. Tasks flow through structured directories, with atomic moves preventing double-processing and structured headers enabling bidirectional feedback.

**Core Scripts**:
- `orchestration/scripts/dispatch.sh` — Task creation and dispatch
- `orchestration/scripts/watch_dispatch.sh` — Autonomous task processing (fswatch + polling)
- `orchestration/scripts/append_ledger.sh` — Event logging

---

## Dispatch Modes

Tasks are classified by the `**Kind**` header:

| Kind | Purpose | Response Expected |
|------|---------|-------------------|
| `TASK` | Standard work item | RESULT + CONFIRM |
| `SURVEY` | Read-only exploration, no writes | RESULT + CONFIRM |
| `DIRECTIVE` | High-priority command from Sovereign | RESULT + CONFIRM |
| `EVIDENCE` | Supporting material for a decision | Acknowledgment |
| `RESULT` | Output from completed task | None (terminal) |
| `RECEIPT` | Proof of delivery/processing | None (terminal) |
| `PATCH` | Code or content modification | RESULT + CONFIRM |
| `NOTE` | Informational, no action required | None (optional ack) |

**Usage**: `bash dispatch.sh <agent> "TOPIC" "DESCRIPTION" [CC] [KIND] [FROM]`

---

## File Format

### Task File (TASK-*.md)

```markdown
# TASK-YYYYMMDD-topic_slug

**From**: Agent Name (Model)
**To**: Target Agent Name (Model)
**Reply-To**: agent_slug
**Issued**: YYYY-MM-DD HH:MM:SS
**Fingerprint**: git_short_hash
**Kind**: TASK
**Priority**: P1
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: —
**Claimed-At**: —
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: agent_slug_or_dash
**Receipts-To**: -OUTBOX/agent/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

[Task description]

---

## Context Files

[Reference files]

## Expected Output

[Where to write results]

## Completion Protocol

[Steps to complete]
```

### Result File (RESULT-*.md)

```markdown
# RESULT-agent-YYYYMMDD-topic_slug

**Task**: TASK-YYYYMMDD-topic_slug.md
**Agent**: agent_slug
**Exit-Code**: 0
**Completed-At**: ISO8601

---

## Output

[Raw task output]
```

### Confirm File (CONFIRM-*.md)

```markdown
# CONFIRM-agent-YYYYMMDD-topic_slug

**Kind**: CONFIRM
**Task**: TASK-YYYYMMDD-topic_slug.md
**From-Agent**: executing_agent
**To-Agent**: dispatching_agent
**Status**: COMPLETE|BLOCKED|FAILED
**Exit-Code**: 0|124|non-zero
**Completed-At**: ISO8601
**Finalized-Task-Path**: `path/to/finalized/task`
**Result-Path**: `path/to/result`
**Execution-Log**: `path/to/execlog`

---

## Execution Log Tail

[Last 120 lines of execution output]
```

### Receipt File (RECEIPT-*.md)

Receipts are copies of finalized task files delivered to CC'd agents. Naming: `RECEIPT-<executing_agent>-TASK-*.md`. Stored in `-INBOX/<cc_agent>/RECEIPTS/`.

---

## Filesystem Kanban

Each agent has a 6-folder kanban structure:

```
-INBOX/<agent>/
  00-INBOX0/       ← New tasks land here (PENDING)
  10-IN_PROGRESS/  ← Claimed and executing
  20-WAITING/      ← Awaiting external input (manual)
  30-BLOCKED/      ← Timed out (exit code 124)
  40-DONE/         ← Successfully completed (exit code 0)
  50_FAILED/       ← Failed (non-zero, non-124 exit code)
  RECEIPTS/        ← CC'd task copies for awareness
  90_ARCHIVE/      ← Historical reference
```

**Flow**: INBOX0 → IN_PROGRESS → DONE | BLOCKED | FAILED

**Atomic claim**: `mv` from INBOX0 to IN_PROGRESS. First mover wins; concurrent watchers cannot double-claim.

---

## Return Channels

### Primary: Reply-To Routing

The `**Reply-To**` header (set by dispatch.sh) determines where completion artifacts are sent. Priority chain:

1. `Reply-To` header (explicit agent slug)
2. `From` header (extracted agent slug from avatar name)
3. Fallback: `commander` (hub-spoke default)

### Secondary: CC Piping

The `**CC**` header lists comma-separated agent slugs that receive a copy of the finalized task file in their `RECEIPTS/` folder.

### Cross-Machine: SSH/SCP

If the reply target or CC'd agent is on a remote machine (MBA for Ajna), the watcher attempts:
- `ssh -o BatchMode=yes -o ConnectTimeout=3 <agent>` to verify connectivity
- `scp -q -o BatchMode=yes -o ConnectTimeout=5` to deliver files

Failure is silent (best-effort). Local copy always succeeds.

---

## Error Codes

| Exit Code | Meaning | Kanban Destination | Ledger Event |
|-----------|---------|-------------------|--------------|
| `0` | Success | 40-DONE | COMPLETE |
| `124` | Timeout (wall-clock exceeded) | 30-BLOCKED | BLOCKED |
| `126` | JSON decode error | 50_FAILED | FAILED |
| `127` | Command not found | 50_FAILED | FAILED |
| Any other | Generic failure | 50_FAILED | FAILED |

---

## Timeout System

### Configuration

- `**Timeout**: 30` — Value in the task header
- Values <= 240 are interpreted as **minutes** (legacy compatibility)
- Values > 240 are interpreted as **seconds**
- Default: 600 seconds (10 minutes) if header is missing or dash

### Enforcement

Python `subprocess.run()` with `timeout=` parameter provides a hard wall-clock limit. On expiry, exit code 124 is returned (matching Unix `timeout` convention).

### Escalation

When a task times out (exit code 124):
1. Task moves to 30-BLOCKED
2. CONFIRM file sent with `**Status**: BLOCKED`
3. If `**Escalation-Contact**` is set and `**Escalation-Delay**` minutes have passed since task creation, an ESCALATION file is written to the contact's INBOX0
4. Escalation format: `ESCALATION-<agent>-<date>-<slug>.md`

---

## Ledger Events

Events are appended by `append_ledger.sh` to the dispatch ledger:

| Event | When | Fields |
|-------|------|--------|
| `DISPATCH` | Task created | caller, target_agent, task_file |
| `CLAIM` | Task moved to IN_PROGRESS | agent, agent, task_file |
| `COMPLETE` | Task succeeded (exit 0) | agent, —, task_file |
| `BLOCKED` | Task timed out (exit 124) | agent, —, task_file |
| `FAILED` | Task failed (exit non-zero) | agent, —, task_file |
| `ESCALATION` | Timeout escalated | agent, escalation_contact, task_file |

---

## Agent CLI Mapping

Each agent maps to a CLI tool in `run_executor()`:

| Agent | CLI Command | Notes |
|-------|-------------|-------|
| `commander` | `claude -p <task_content>` | Claude Code (Opus 4.6) |
| `adjudicator` | `codex exec <task_content>` | Codex CLI (Sonnet) |
| `cartographer` | `gemini -p <task_content>` | Gemini CLI (2.5 Pro) |
| `psyche` | `openclaw agent --agent main --message <content> --timeout <t>` | OpenClaw (GPT-5.3-codex) |
| `ajna` | Same as psyche | OpenClaw (Kimi K2.5 via NVIDIA) |

---

## Guards

The watcher enforces multiple safety guards before processing:

1. **File type**: Only `*.md` files are processed
2. **Ignore patterns**: RECEIPT-*, RESULT-*, CONFIRM-*, EXECLOG-* are skipped
3. **Addressee**: `**To**` header must contain the agent's name (case-insensitive word boundary match)
4. **Completion**: Tasks with non-empty `**Completed-At**` or `**Exit-Code**` are skipped
5. **Status**: Only `Status.*PENDING` tasks are claimed

---

## Examples

### Standard Task Dispatch

```bash
# Commander dispatches a survey to Cartographer
bash dispatch.sh cartographer "CORPUS_SURVEY" "Survey canon/ for orphaned references. Report as table."
```

Creates: `-INBOX/cartographer/00-INBOX0/TASK-20260210-corpus_survey.md`
Reply-To: commander (auto-injected)
CC: commander (auto-injected)

### Cross-Agent Dispatch with CC

```bash
# Commander dispatches QA to Adjudicator, CC'd to Psyche
bash dispatch.sh adjudicator "QA_REVIEW" "Run make verify and report failures" "psyche"
```

Creates task in Adjudicator's INBOX0. On completion, CONFIRM goes to Commander, RECEIPT goes to Psyche.

### Manual Task File

For agents that need custom headers, create the file directly:

```bash
cat > -INBOX/psyche/00-INBOX0/TASK-20260210-custom.md << 'EOF'
# TASK-20260210-custom

**From**: Commander (Claude Code Opus)
**To**: Psyche (OpenClaw GPT-5.3-codex)
**Reply-To**: commander
**CC**: adjudicator
**Issued**: 2026-02-10 15:00:00
**Fingerprint**: 4b47dca
**Kind**: DIRECTIVE
**Priority**: P0
**Status**: PENDING
**Timeout**: 60

---

## Objective

Execute emergency reconciliation of all ledger files.
EOF
```

---

## Anti-Patterns

1. **Dispatching without Reply-To**: Never create tasks without `**Reply-To**` and `**CC**` headers. Use dispatch.sh (auto-injects both) or set them manually.
2. **Processing INBOX0 manually**: Let the watcher handle task claims. Manual `mv` can race with the watcher.
3. **Ignoring CONFIRM/RESULT files**: Always triage completion signals — acknowledge successes, investigate failures.
4. **Recursive dispatch**: Agent A dispatches to Agent B who dispatches back to A. Add circuit breakers if chaining.
5. **Stale INBOX0 accumulation**: Tasks sitting in INBOX0 for >24h without a running watcher indicate infrastructure failure.

---

## Cross-References

- `CLAUDE.md` — Anti-pattern: "Dispatching without Reply-To"
- `COCKPIT.md` — Agent role assignments and pane mapping
- `AGENTS.md` — Agent capabilities and model specifications
- `orchestration/scripts/dispatch.sh` — Task creation script
- `orchestration/scripts/watch_dispatch.sh` — Autonomous task processor
- `orchestration/scripts/append_ledger.sh` — Event logger

---

*Toolchain Interaction Protocol v1.0.0 | Syncrescendence*
