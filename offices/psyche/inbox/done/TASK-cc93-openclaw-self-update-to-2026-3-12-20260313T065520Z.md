# TASK

**Kind**: TASK
**Line-ID**: psyche-cc93-openclaw-self-update-to-2026-3-12-20260313T065520Z
**From**: commander
**To**: psyche
**Reply-To**: communications/handoffs
**CC**: 
**Issued-At**: 2026-03-13T06:55:20Z
**Priority**: high
**Decision-Envelope**: runtime-repair
**Objective-Lock**: update local OpenClaw to 2026.3.12, restart gateway, verify runtime health, and emit evidence
**Expected-Output**: receipt plus result artifact with version, gateway status, and channel/browser health
**Receipts-Required**: Yes
**Completion-Condition**: OpenClaw 2026.3.12 verified on Mac mini with evidence
**Escalation-Path**: offices/psyche/inbox/blocked

## Payload

Execute on the Mac mini local surface:

1. Run `openclaw --version` and `openclaw update --yes --json`.
2. If update succeeds, run `openclaw gateway restart`.
3. Verify with `openclaw --version`, `openclaw gateway status --json`, `openclaw health`, and `openclaw channels status --probe --json`.
4. If browser is configured, also run `openclaw browser status --json` or the configured profile equivalent.
5. Write a result artifact under `communications/responses/` or `offices/psyche/outbox/results/` containing before/after version, gateway PID/status, and probe results.
6. If blocked by auth, path drift, or service failure, write a blocked artifact with the exact error and last working state instead of guessing.
