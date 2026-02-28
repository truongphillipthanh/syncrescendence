# Sovereign Directive – TEST-220222

**Objective Lock**: Validate full ingest → dispatch → receipt loop end-to-end.
**Priority**: P0
**Expected Receipts**: commit hash + verification command in ACTIVE-TASKS.md

## Task
1. Commander: triage this file, move to active/, confirm Objective Lock.
2. Dispatch copy to Adjudicator inbox/pending/ via outbox/.
3. Adjudicator: validate Translation Layer + Receipts format.
4. Return verified artifact to Commander inbox/done/.
5. Update ACTIVE-TASKS.md + log to memory/$(date +%Y-%m-%d)-ingest.log
6. Produce final receipt commit.

**Verification command**: git log --oneline -1 | grep "TEST-220222"
