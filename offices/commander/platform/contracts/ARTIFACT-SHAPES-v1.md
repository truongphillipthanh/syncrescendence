# Commander Artifact Shapes v1

Commander uses these local forms:

- `TASK` / dispatch envelope
- `RECEIPT`
- `RESULT`
- `CONFIRM`
- `ALERT`
- `BRIEFING`
- `EXECLOG`

Local routing:

- dispatches -> [outbox/dispatches](/Users/system/syncrescendence/offices/commander/outbox/dispatches)
- receipts -> [outbox/receipts](/Users/system/syncrescendence/offices/commander/outbox/receipts)
- results -> [outbox/results](/Users/system/syncrescendence/offices/commander/outbox/results)
- confirms / alerts / briefings arrive through inbox state lanes
- raw execution traces belong in [platform/logs](/Users/system/syncrescendence/offices/commander/platform/logs)

Federal promotion still applies. These are local forms first, not automatic federal truth.
