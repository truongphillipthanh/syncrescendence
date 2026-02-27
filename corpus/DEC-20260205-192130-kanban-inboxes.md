Decision ID: DEC-20260205-192130-kanban-inboxes
Choice: Adopt **filesystem kanban** for dispatch surfaces: per-agent `-INBOX/<agent>/00-INBOX0 → 10-IN_PROGRESS → 40-DONE/50_FAILED` folder lifecycle, watchers only consume Inbox0, and receipts/artifacts go to per-agent outboxes.

Why:
- Keeps “Inbox 0” pristine (scales beyond flat inbox/outgoing).
- Makes lifecycle tractable without external PM dependency.
- Reduces cross-claim risk (misrouted CC copies don’t get executed).

Constraints:
- Hub-spoke dispatch preserved (OpenClaw orchestrates; lanes execute).
- Secrets remain local.
- Prefer atomic moves + deterministic naming.

Falsifier:
- If folder kanban becomes unwieldy or conflicts with Linear adoption, move kanban truth surface to Linear and keep file surfaces as adapters.

Evidence pointers:
- Clarescence: `orchestration/state/impl/clarescence/CLARESCENCE-2026-02-05-kanban-inboxes.md`
- Current watcher scripts: `orchestration/scripts/dispatch.sh`, `watch_dispatch.sh`

