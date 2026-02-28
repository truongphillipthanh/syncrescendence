Decision ID: DEC-20260204-213941-ledger-event-set
Choice: Extend `DYN-GLOBAL_LEDGER.md` event set to include **COMPACT** (for staging→archive compactions) and **REGEN** (for CANON regeneration runs). Keep existing core lifecycle events unchanged.
Why (lens 1-2): Systems Thinking (ledger is the spine; compaction/regen are state transitions), Observability (sensors must report key transforms)
Falsifier: If adding event types increases ambiguity or reduces interoperability, then keep Event to the canonical set and represent compaction/regen as `DECISION` events with Task IDs pointing to receipts.
Reversibility type: reversible
Touched surfaces: orchestration/state/DYN-GLOBAL_LEDGER.md; orchestration/scripts/append_ledger.sh; orchestration/scripts/compact_wisdom.sh; orchestration/scripts/watch_canon.sh
Evidence pointers: DYN-GLOBAL_LEDGER.md schema; D-022 (compaction receipts); D-031 (regen observability)

DecisionAtom: DEC-20260204-213941-ledger-event-set
IntentionLink: —
Fingerprint: 9e9b409
