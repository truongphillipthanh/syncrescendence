# DYN-DISPATCH_KANBAN_PROTOCOL.md

**Version**: 1.1.0
**Created**: 2026-02-05
**Status**: ACTIVE
**Decision**: DEC-20260205-192130-kanban-inboxes
**Clarescence**: CLARESCENCE-2026-02-05-kanban-inboxes

---

## 1. Overview

Filesystem kanban for dispatch surfaces. Each agent's inbox becomes a kanban board implemented as numbered subdirectories. Files move between folders as they progress through the lifecycle. Folder location IS the canonical state.

**Design principles:**
- Inbox 0 stays pristine (only unclaimed new tasks)
- Folder = state (no filename suffix encoding)
- Atomic `mv` = claim lock (same-filesystem rename is atomic)
- Hub-spoke preserved (OpenClaw orchestrates; lanes execute)
- Header fields provide metadata; folder provides state

---

## 2. Per-Agent Kanban Structure

```
-INBOX/<agent>/
  00-INBOX0/          # New, unclaimed tasks only
  10-IN_PROGRESS/     # Claimed; currently executing
  20-WAITING/         # Waiting on external dependency
  30-BLOCKED/         # Cannot proceed (auth, install, etc.)
  40-DONE/            # Completed successfully
  50_FAILED/          # Completed unsuccessfully
  90_ARCHIVE/         # Cold storage (old responses, bootstrap docs)
  RECEIPTS/           # CC receipts; watchers MUST ignore this folder
```

**Rules:**
- Watchers ONLY watch `00-INBOX0/`.
- RECEIPTS/ is never executed. Used for CC-piped copies of completed tasks.
- Manual triage may move items to `20-WAITING/` or `30-BLOCKED/`.
- `90_ARCHIVE/` is for non-actionable historical files.

---

## 3. Per-Agent Outbox Structure

```
-OUTBOX/<agent>/
  RESULTS/            # RESULT-*.md receipt files
  ARTIFACTS/          # Any produced files (patches, drafts, data)
```

**Rules:**
- Watchers write RESULT files deterministically to `-OUTBOX/<agent>/RESULTS/`.
- `-OUTGOING/` remains as staging-for-commit (Sovereign relay surface).
- Artifacts that need Sovereign relay go to `-OUTGOING/`; everything else goes to `-OUTBOX/`.

---

## 4. Dispatch Kinds

Every dispatch file MUST include a `**Kind**:` header field.

| Kind | Description | Produced By | Consumed By |
|------|-------------|-------------|-------------|
| `TASK` | Execution request (do something) | dispatch.sh, Sovereign | Lane watchers |
| `SURVEY` | Read-only reconnaissance (report on something) | dispatch.sh | Cartographer, any |
| `DIRECTIVE` | Wisdom-stream instruction (guidance, not execution) | Sovereign, OpenClaw | Any agent |
| `EVIDENCE` | Sensing output (observation, measurement) | Cartographer, any | OpenClaw, Sovereign |
| `RESULT` | Execution receipt (what happened) | Watchers | Sovereign, CC targets |
| `RECEIPT` | CC copy of a completed task (read-only) | Watchers | Informational only |
| `PATCH` | Code or config change proposal | Commander, Adjudicator | Sovereign for approval |
| `NOTE` | Informational; no action required | Any | Any |
| `CONFIRM` | Completion confirmation (reply-to-sender) | Watchers | Dispatching agent |

**Filename conventions:**
- `TASK-YYYYMMDD-topic_slug.md`
- `SURVEY-YYYYMMDD-topic_slug.md`
- `RESULT-<agent>-YYYYMMDD-topic_slug.md`
- `RECEIPT-<source_agent>-TASK-YYYYMMDD-topic_slug.md`
- `EVIDENCE-<agent>-YYYYMMDD-topic_slug.md`
- `DIRECTIVE-YYYYMMDD-topic_slug.md`
- `PATCH-YYYYMMDD-topic_slug.md`
- `CONFIRM-<executor_agent>-YYYYMMDD-topic_slug.md`
- `EXECLOG-<executor_agent>-YYYYMMDD-topic_slug.log`

---

## 5. Task Schema (Header Fields)

All dispatch files use markdown bold-colon headers:

```markdown
# TASK-20260205-example_topic

**From**: dispatch
**To**: Commander (Claude Code Opus)
**Issued**: 2026-02-05 19:23:26
**Fingerprint**: 94d8dde
**Kind**: TASK
**Priority**: P1
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: —
**Claimed-At**: —
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: —
**Receipts-To**: -OUTBOX/commander/RESULTS/
```

**New fields (added by this protocol):**
- `**Kind**:` — One of: TASK, SURVEY, DIRECTIVE, EVIDENCE, RESULT, RECEIPT, PATCH, NOTE, CONFIRM
- `**Kanban**:` — Current kanban lane: INBOX0, IN_PROGRESS, WAITING, BLOCKED, DONE, FAILED
- `**Receipts-To**:` — Relative path where RESULT receipt will be written
- `**Reply-To**:` — Agent slug that receives CONFIRM + RESULT upon completion (mandatory for bidirectional feedback)

**Status values** (header truth, mirrors folder location):
- `PENDING` → file in `00-INBOX0/`
- `IN_PROGRESS` → file in `10-IN_PROGRESS/`
- `WAITING` → file in `20-WAITING/`
- `BLOCKED` → file in `30-BLOCKED/`
- `COMPLETE` → file in `40-DONE/`
- `FAILED` → file in `50_FAILED/`

---

## 6. Lifecycle

### 6.1 Dispatch (new task creation)
1. `dispatch.sh` writes file to `-INBOX/<agent>/00-INBOX0/`
2. Sets `Status: PENDING`, `Kanban: INBOX0`
3. Appends `DISPATCH` event to ledger

### 6.2 Claim (watcher picks up task)
1. Watcher detects file in `00-INBOX0/`
2. Atomic `mv` from `00-INBOX0/TASK-*.md` → `10-IN_PROGRESS/TASK-*.md`
3. If `mv` fails → another watcher claimed it; skip
4. Updates header: `Status: IN_PROGRESS`, `Kanban: IN_PROGRESS`, `Claimed-By`, `Claimed-At`
5. Appends `CLAIM` event to ledger

### 6.3 Process (execution)
1. Watcher routes to agent-specific CLI (claude, codex, gemini, openclaw)
2. Captures stdout/stderr and exit code

### 6.4 Complete / Fail
1. On success: `mv 10-IN_PROGRESS/TASK-*.md → 40-DONE/TASK-*.md`
2. On failure: `mv 10-IN_PROGRESS/TASK-*.md → 50_FAILED/TASK-*.md`
3. Updates header: `Status: COMPLETE|FAILED`, `Kanban: DONE|FAILED`, `Completed-At`, `Exit-Code`
4. Writes RESULT receipt to `Receipts-To` path (deterministic naming)
5. CC copies: finalized task → `-INBOX/<cc>/RECEIPTS/RECEIPT-<agent>-TASK-*.md`
6. Appends `COMPLETE|FAILED` event to ledger

### 6.5 Completion Feedback (Reply-To-Sender) — MANDATORY

Every task completion MUST notify the dispatching agent. This is non-negotiable.

**Mechanism:**
1. Watcher parses `**Reply-To**:` header (set by dispatch.sh v2+)
2. Fallback: extract agent slug from `**From**:` header
3. Last resort: defaults to `commander` (hub-spoke)
4. Watcher writes to `Reply-To` agent's INBOX0:
   - `CONFIRM-<executor>-<date>-<slug>.md` — structured completion confirmation
   - `RESULT-<executor>-<date>-<slug>.md` — full execution receipt
   - `EXECLOG-<executor>-<date>-<slug>.log` — raw stdout/stderr

**What the sender receives:**
- Status (COMPLETE / FAILED / BLOCKED)
- Exit code
- Execution log tail (last 120 lines)
- Path to full result and finalized task

**CONFIRM files in INBOX0 are safe.** Watchers skip `CONFIRM-*`, `RESULT-*`, and `EXECLOG-*` prefixes.

**Manual dispatch rule:** When writing task files by hand (not via dispatch.sh), you MUST include:
```
**Reply-To**: <your-agent-slug>
**CC**: <your-agent-slug>
```

### 6.6 Manual transitions
- `PENDING → WAITING`: Sovereign moves file to `20-WAITING/` (external blocker)
- `PENDING → BLOCKED`: Sovereign moves file to `30-BLOCKED/` (hard blocker)
- `WAITING/BLOCKED → INBOX0`: Sovereign moves file back when unblocked
- Any → `90_ARCHIVE/`: Manual archival of cold files

---

## 7. Cross-Claim Prevention

1. **To: guard**: Watchers MUST verify the `**To**:` field matches their agent before claiming.
2. **Atomic mv**: Only one watcher can successfully `mv` a file from `00-INBOX0/`.
3. **RECEIPTS/ isolation**: CC-piped copies land in `RECEIPTS/`, never in `00-INBOX0/`.
4. **Per-host tagging**: `Claimed-By` records `<agent>-<hostname>` for forensic traceability.

---

## 8. RESULT Receipt Determinism

Every task execution MUST produce a RESULT receipt, even if the tool only prints stdout.

**RESULT file location**: `{Receipts-To}/RESULT-{agent}-{task_slug}.md`

**RESULT file format**:
```markdown
# RESULT-<agent>-YYYYMMDD-topic_slug

**Task**: TASK-YYYYMMDD-topic_slug.md
**Agent**: <agent>
**Exit-Code**: <0|1|...>
**Completed-At**: <ISO 8601>
**Duration**: <seconds>

---

## Output

<stdout/stderr captured from CLI execution>
```

---

## 9. Ledger Event Extensions

Existing ledger events remain valid. No new event types needed.

| Event | Trigger |
|-------|---------|
| `DISPATCH` | Task written to `00-INBOX0/` |
| `CLAIM` | Task moved to `10-IN_PROGRESS/` |
| `COMPLETE` | Task moved to `40-DONE/` |
| `FAILED` | Task moved to `50_FAILED/` |

---

## 10. Queue Status

Use `queue_status.sh` (or manual `ls`) to check kanban state:

```bash
for agent in commander adjudicator cartographer psyche ajna; do
  echo "=== $agent ==="
  for lane in 00-INBOX0 10-IN_PROGRESS 20-WAITING 30-BLOCKED 40-DONE 50_FAILED; do
    count=$(ls -1 "$REPO_ROOT/-INBOX/$agent/$lane/" 2>/dev/null | grep -c '\.md$' || echo 0)
    [ "$count" -gt 0 ] && echo "  $lane: $count"
  done
done
```

---

## 11. Migration Notes

See `00-ORCHESTRATION/scripts/migrate_kanban.sh` for the one-time migration script.

Migration rules:
- `*.md` with `Status: PENDING` → `00-INBOX0/`
- `*.claimed-by-*` → `10-IN_PROGRESS/` (strip suffix)
- `*.complete` → `40-DONE/` (strip suffix)
- `*.failed` → `50_FAILED/` (strip suffix)
- `RESULT-*`, `RECEIPT-*` → `RECEIPTS/`
- `RESPONSE-*`, bootstrap docs → `90_ARCHIVE/`
- iCloud " 2" duplicates → deleted
- Existing `-OUTGOING/RESULT-*` files → `-OUTBOX/<agent>/RESULTS/`

---

## 12. Compatibility

- Hub-spoke dispatch preserved: Sovereign → OpenClaw → Lanes → OpenClaw → Sovereign
- `append_ledger.sh` unchanged (same event types)
- `dispatch.sh` v2 backwards-compatible (writes to new path, old watchers won't see files)
- `watch_dispatch.sh` v2 must be deployed on all machines simultaneously with migration
- `-OUTGOING/` retained as Sovereign relay surface (not replaced)

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-02-05 | Initial protocol (DEC-20260205-192130-kanban-inboxes) |
| 1.1.0 | 2026-02-07 | Reply-To-Sender: mandatory bidirectional feedback (CONFIRM/RESULT/EXECLOG piped to dispatcher inbox) |
