# Receipt-Result-Confirm Cycle v1

## Purpose

Capture the strongest local closure loop recovered from the predecessor commander office.

## Cycle

1. **Dispatch**
   - a task or envelope is sent from one office to another
2. **Receipt**
   - the executing office records claim/completion metadata
3. **Result**
   - the executing office produces the substantive output
4. **Confirm**
   - the origin office receives a closure signal pointing to the result
5. **Promotion**
   - the origin office decides whether the result stays local, becomes federal communications, updates program/executive truth, or compacts into playbook/operator law

## Why It Matters

This separates three things that often get collapsed:

- mechanical execution state
- substantive work product
- closure acknowledgement

When those are collapsed, lineage blurs and offices become hard to trust.

## Local Homes

- dispatch -> `outbox/dispatches/`
- receipt -> `outbox/receipts/`
- result -> `outbox/results/`
- confirm -> receiving office `inbox/done/` or `inbox/active/`
- exec log -> `platform/logs/`
