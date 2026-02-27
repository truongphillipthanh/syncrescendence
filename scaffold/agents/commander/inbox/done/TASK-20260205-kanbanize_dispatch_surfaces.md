# TASK-20260205-kanbanize_dispatch_surfaces

**From**: dispatch
**To**: Commander (Claude Code Opus)
**Issued**: 2026-02-05 19:23:26
**Fingerprint**: 94d8dde
**Priority**: P1
**Status**: COMPLETE
**Claimed-By**: commander-Psyche
**Claimed-At**: 2026-02-06T03:25:00Z
**Completed-At**: 2026-02-06T03:35:00Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: —

---

## Objective

Read the clarescence + decision atom and propose/implement a concrete kanbanized dispatch architecture for the constellation.

Inputs:
- Clarescence: orchestration/state/impl/clarescence/CLARESCENCE-2026-02-05-kanban-inboxes.md
- DecisionAtom: orchestration/state/impl/tooling/DEC-20260205-192130-kanban-inboxes.md
- Current scripts: orchestration/scripts/dispatch.sh, watch_dispatch.sh, append_ledger.sh
- Neo-Blitzkrieg context: orchestration/state/REF-NEO_BLITZKRIEG_BUILDOUT.md (dispatch modes)

Objective:
1) Convert flat -INBOX/-OUTGOING into a filesystem-kanban design that preserves Inbox 0 and retains directives/receipts/artifacts.
2) Specify a migration plan that is safe with two machines (Ajna home mini, Psyche laptop) and avoids cross-claim.
3) Enumerate and formalize dispatch kinds/categories (Kind field) aligned to Blitzkrieg/Neo-Blitzkrieg lanes: TASK, SURVEY, DIRECTIVE, EVIDENCE, RESULT, RECEIPT, PATCH.
4) Implement minimal viable changes (prefer incremental):
   - update dispatch.sh to write new tasks to -INBOX/<agent>/00-INBOX0/
   - update watch_dispatch.sh to watch only Inbox0 and move tasks between kanban folders
   - implement deterministic RESULT receipt writing into -OUTBOX/<agent>/RESULTS (or equivalent)
   - ensure watchers ignore RECEIPT-* and only execute tasks addressed to them (**To** guard already exists on Psyche; make it canonical for all watchers)

Deliverables:
- A short architecture doc: orchestration/state/DYN-DISPATCH_KANBAN_PROTOCOL.md
- Script patches + a one-time migration script for existing inbox files.
- Smoke test instructions.

Write results to:
-OUTGOING/RESULT-commander-20260205-kanbanize_dispatch_surfaces.md

Constraints:
- Keep hub-spoke dispatch (OpenClaw orchestrates).
- Avoid breaking always-on watchers.
- No secrets in git.

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `orchestration/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `engine/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTGOING/RESULT-commander-20260205-kanbanize_dispatch_surfaces.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: kanbanize_dispatch_surfaces complete" && git push`
