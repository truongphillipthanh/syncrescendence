# CLARESCENCE — Kanbanized Inboxes / Outboxes (Blitzkrieg-scaled Dispatch)

**Date:** 2026-02-05
**Scope:** execution substrate / file-based dispatch surfaces
**Trigger:** Constellation is outgrowing flat `-INBOX/<agent>/` + global `-OUTGOING/` as the primary workflow surfaces.

---

## 0) Intent (plain)
We want each CLI tool’s inbox to remain a pristine **Inbox 0** (only new/untriaged directives), while preserving:
- directives (what was asked)
- receipts (what happened: lifecycle + logs)
- output artifacts (what was produced)

…and we want this to scale to Neo‑Blitzkrieg without devolving into “everyone talking to everyone.”

---

## 1) Current state (truth)
### Surfaces
- Dispatch files are created by `orchestration/scripts/dispatch.sh` into `-INBOX/<agent>/TASK-*.md`
- Watchers (`watch_dispatch.sh`) watch `-INBOX/<agent>/` and:
  - claim via rename `.claimed-by-...`
  - run tool (`claude/codex/gemini/openclaw agent`)
  - rename to `.complete` or `.failed`
  - append lifecycle events to `orchestration/state/DYN-GLOBAL_LEDGER.md`
- Directives & execution logs exist as *separate* staging streams:
  - `create_directive.sh` → `DYN-DIRECTIVE_STAGING.md`
  - `create_execution_log.sh` → `DYN-EXECUTION_STAGING.md` → compacts into history/compendiums

### Dispatch “types/categories” we currently have (implicit)
We do not yet have a formal `Dispatch-Type` field; types are implied by filenames and ledger events.

**Lifecycle event set (ledger):**
- `DISPATCH | CLAIM | COMPLETE | FAILED | DECISION | COMPACT | REGEN`

**Dispatch modes (toolchain):** (ARCH-TOOLCHAIN_CLARESCENCE)
- `Sovereign → OpenClaw`
- `OpenClaw → Commander/Adjudicator/Cartographer` via file tasks or direct exec/subagents
- `Twin relay (Ajna ↔ Psyche)` via Slack

**File “kinds” in practice:**
- `TASK-*` (execution requests)
- `RESULT-*` (receipts / human-readable results)
- `DISPATCH-*` (packets)
- `EVIDENCE-*` (sensing output)
- `DIRECTIVE-*` (wisdom stream)
- plus ad-hoc “SURVEY-*” (Cartographer) noted in clarescence text, though dispatch.sh currently emits TASK files.

---

## 2) Problem statement
Flat inboxes/outgoing cause:
- loss of Inbox 0 semantics (inbox fills with claimed/completed/duplicates)
- misrouting/cross-claim risk (a task addressed to Ajna can end up in Psyche inbox)
- poor tractability: hard to answer “what’s pending / blocked / in progress?”
- receipts and artifacts intermix, creating noisy diffs and compaction hazards

---

## 3) Desired properties (requirements)
1) **Inbox 0 stays clean**: only unclaimed new directives
2) **Kanban lifecycle in filesystem**: Pending → In‑Progress → Waiting/Blocked → Done/Failed/Cancelled
3) **Receipts are durable and discoverable** (not only stdout logs)
4) **Artifacts are separated from receipts** (so outputs don’t clutter inbox)
5) **Hub‑spoke dispatch** preserved (OpenClaw orchestrates; not all agents talk to all agents)
6) **Atomic moves** (no partial state); safe under concurrent watchers
7) **Simple grepability**: a single task id should let you find:
   - directive
   - execution receipt
   - artifacts
   - ledger events

---

## 4) Proposed design (filesystem kanban)
### 4.1 Per‑agent kanban folders
Replace “flat inbox” with subfolders.

Canonical per-agent structure:
```
-INBOX/<agent>/
  00-INBOX0/          # new, unclaimed
  10-IN_PROGRESS/     # claimed; being executed
  20-WAITING/         # waiting on external dependency
  30-BLOCKED/         # cannot proceed (auth/install/etc)
  40-DONE/            # completed successfully
  50_FAILED/          # completed unsuccessfully
  90_ARCHIVE/         # cold storage
  RECEIPTS/           # (optional) CC receipts only, never executed
```

**Watcher rule:** watchers should only watch `00-INBOX0/`.

**Claim rule:** atomic move from `00-INBOX0/` → `10-IN_PROGRESS/` and append `.claimed-by-...`.

**Complete rule:** move to `40-DONE/` or `50_FAILED/`.

**CC receipts:** land in `RECEIPTS/` or as `RECEIPT-*` under the agent root; watchers ignore them.

### 4.2 Output separation
Create a parallel “outbox” per agent (or a single outbox with per-agent subfolders).

Proposed:
```
-OUTBOX/<agent>/
  RESULTS/        # RESULT-*.md (receipts)
  ARTIFACTS/      # any produced files; may include patches, drafts
```

Keep `-OUTGOING/` as *staging-for-commit* (repo sovereignty) rather than a dumping ground.

### 4.3 Task schema improvements
Add explicit header fields:
- `**Kind**:` TASK | SURVEY | DIRECTIVE | EVIDENCE | PATCH | NOTE
- `**Dispatch-Mode**:` file | spawn | exec
- `**Kanban**:` INBOX0 | IN_PROGRESS | WAITING | BLOCKED | DONE | FAILED
- `**Receipts-To**:` relative paths (where RESULT + artifacts will go)

### 4.4 Blitzkrieg / Neo‑Blitzkrieg pathway alignment
Reassert a well-defined pathway:
- Sovereign → OpenClaw always
- OpenClaw dispatches to lanes by role (Commander/Adjudicator/Cartographer)
- Returns come back to OpenClaw (Ajna/Psyche) and then to Sovereign

Filesystem kanban supports this by making *each lane’s inbox* a disciplined queue.

---

## 5) Tradeoffs / falsifiers
- More folders = more complexity; mitigated by deterministic conventions.
- Migration cost: watchers + scripts must be updated; requires careful atomic moves.
- If repo is shared by both machines, per-host outboxes must avoid cross-claim; mitigated by To: guards + CC receipts rules.

Falsifier:
- If `-INBOX` becomes too heavy even with kanbanization, we should move the kanban truth surface into Linear (cloud) and keep `-INBOX` as a thin adapter.

---

## 6) Decision candidates
### Candidate A (recommended)
Filesystem kanban: subfolders per agent + per-agent outbox + explicit Kind/Kanban fields.

### Candidate B
Keep flat inbox but encode status exclusively in frontmatter + ledger, and rely on a dashboard.

**Recommendation:** Candidate A.

---

## 7) Next implementation steps (handoff)
1) Update `dispatch.sh` to write to `-INBOX/<agent>/00-INBOX0/` and include Kind/Kanban fields.
2) Update `watch_dispatch.sh` to:
   - watch only `00-INBOX0/`
   - move files between kanban dirs
   - write RESULT receipts deterministically (even for tools that only print stdout)
3) Create `-OUTBOX/<agent>/RESULTS` and `ARTIFACTS` paths.
4) Add a small `queue_status.sh` that prints counts by lane/state.
5) Migrate existing files into the new structure (one-time script).

---

## Lens pass (compressed)
- **Tractability:** huge win; status becomes visually obvious + scriptable.
- **Integrity:** atomic moves + To: guard reduces misrouting.
- **Velocity:** less hunting; less inbox clutter; fewer duplicate runs.
- **Strategic harmony:** aligns with Neo‑Blitzkrieg lanes and hub‑spoke dispatch.
- **Safety:** receipts/artifacts are separated; compaction less risky.
