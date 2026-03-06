# Dispatches

This lane is the authoritative home for dispatch-event artifacts inside `communications/`.

Use it for:

- dispatch records for routed packets, tasks, and handoffs
- authoritative send / receipt / retry / failure state for a named communication
- routing metadata that must survive beyond local office queues
- compact dispatch ledgers that other offices or validators may cite

Do not use it for:

- prompt bodies; those stay in `communications/prompts/`
- response bodies; those stay in `communications/responses/`
- generic chronology; that stays in `communications/logs/`
- office-local queue residue that has not crossed a lineage threshold

## Filing Rule

Create a dispatch artifact here when the communication event itself needs durable lineage.

Examples:

- a packet was sent to an external surface and needs an auditable send record
- a routed task crossed office boundaries and needs authoritative receipt state
- retries, failures, or route changes must be preserved outside office-local inbox/outbox state

Do not create a dispatch artifact merely because a prompt exists.
Only create one when dispatch metadata is itself part of the durable record.

## Minimum Metadata

Each dispatch artifact should carry at least:

- `artifact_class: dispatch`
- `dispatch_id`
- `related_packet` or `related_artifact`
- `sender_office`
- `target_surface` or `target_office`
- `dispatch_status`
- `dispatched_at`

Recommended additional fields:

- `route`
- `account_surface`
- `attempt`
- `receipt_state`
- `promotion_scope`

## Naming

Recommended filename pattern:

- `DISPATCH-<sender>-<slug>.md`

If the dispatch is tied to an existing packet ID, reuse that ID or slug in the filename and metadata.

## Relationship To Other Lanes

- `prompts/` contains the request content
- `responses/` contains the answer content
- `dispatches/` contains the routing and receipt record
- `logs/` contains broad chronology

One communication may legitimately have artifacts in all four lanes.
The lanes are complementary, not interchangeable.
