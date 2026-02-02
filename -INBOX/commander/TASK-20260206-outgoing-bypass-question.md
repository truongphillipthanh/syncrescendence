# TASK-20260206-outgoing-bypass-question

**From**: Sovereign (via Ajna)
**To**: Commander
**Issued**: 2026-02-06
**Priority**: P1 — Architectural question, affects IO plumbing
**Status**: COMPLETE — Resolved by IO Model v2 (TASK-20260206-io_model_v2_and_claim_locking.md)

---

## Sovereign's Question

"Since we can connect to each platform's inbox via a GitHub connector, and simply upload from a folder, we have to figure out the true nature of the OUTGOING folder — why not bypass it altogether?"

## Context

The current IO model:
- `-INBOX/{agent}/` — inbound tasks TO that agent
- `-OUTGOING/` — results FROM agents, waiting for relay

But if agents can write directly to another agent's inbox (e.g., Ajna writes to `-INBOX/psyche/`), and platforms watch their own inbox folders, then `-OUTGOING/` becomes a dead letter box — an unnecessary hop.

## Questions to Resolve

1. **Is -OUTGOING still needed?** What's its actual function vs direct inbox-to-inbox delivery?
2. **Who triages -OUTGOING today?** If it's manual (Sovereign moves files), that's friction we should eliminate.
3. **Should the model be: agents write directly to the destination inbox?** e.g., Ajna → `-INBOX/psyche/`, Psyche → `-INBOX/ajna/`
4. **What about -SOVEREIGN/?** Decision briefs requiring Phillip — this seems like a different pattern (human-in-the-loop, not agent-to-agent).
5. **GitHub connector implications**: If each platform watches its own inbox via GitHub, the graph is: agent → writes to target inbox → target's GitHub connector picks it up. No -OUTGOING needed.

## Requested Output

Disposition recommendation for -OUTGOING: keep/repurpose/deprecate, with rationale.
Update to IO plumbing docs if deprecating.
