# Ratification-Pointer Rollout v1

**Status**: live-v1
**Class**: implementation law
**Purpose**: define the non-breaking rollout order for ratification pointers on authority-bearing registries and schema surfaces

## Compact Contract

- schema-law transition lands first
- validator compatibility lands second
- header and row-shape change lands last
- legacy authority may be carried temporarily by a repo-native compatibility receipt
- the live tributary proof remains non-breaking during transition

This law applies the ratification-pointer rule from `CONTROL-PLANE-SOVEREIGNTY-CONTRACT-v1.md` to live authority-bearing registry families without letting header churn outrun repo law.

## 1. Governing Scope

The first governed family is the live tributary disposition proof set:

- `orchestration/state/registry/tributary-disposition-schema-v1.md`
- `orchestration/state/registry/tributary-disposition-registry.csv`
- `orchestration/state/registry/tributary-disposition-ledger.jsonl`
- `orchestration/state/TRIBUTARY-DISPOSITION-VALIDATION-REPORT.md`

This family goes first because it already carries live current-state meaning in repo-native form and already proves structural legality.

The baseline proof preserved by this law is:

- validation status `PASS`
- `10` registry rows
- `50` ledger events

Until a later migration receipt explicitly supersedes that proof, rollout work must preserve it.

## 2. Ordered Rollout Law

Ratification pointers must roll out in this exact order:

1. schema-law transition
2. validator compatibility
3. header and row-shape revision

The order is binding.

Starting with a validator-only interpretation is forbidden because tooling may not decide authority before repo law does.

Starting with a header change is forbidden because the current tributary proof depends on the exact `v1` schema and header.

## 3. Phase 1: Schema-Law Transition

The first change is doctrinal, not structural.

Phase 1 must:

- ratify that authority-bearing registry rows and schema changes require the pointer family
- declare the current `v1` tributary CSV header and JSONL event shape unchanged during the compatibility window
- define how legacy `v1` rows may temporarily remain authority-bearing without inline pointer columns
- define how unbound legacy rows are treated

Minimum pointer fields remain:

- `ratification_pointer`
- `ratified_by_artifact_path`
- `ratified_by_artifact_id`
- `ratified_at`

Phase 1 does not authorize editing the live tributary CSV header, rewriting ledger history, or silently reclassifying old rows by convenience.

## 4. Temporary Legacy Compatibility Treatment

During the compatibility window, legacy `v1` rows divide into two classes:

- `authority_bound`
- `informative_only`

The distinction is lawful only if it is derived from repo-ratified pointer matter.

### 4.1 Legacy Authority-Bearing Rows

A legacy `v1` row is temporarily authority-bearing only if a repo-native compatibility receipt binds that row to the full pointer family.

The compatibility receipt must:

- key by `candidate_id`
- identify the exact ratifying repo artifact
- record all minimum pointer fields
- make the row's authority status explicit rather than inferred

This treatment exists because the `v1` header does not yet carry inline pointer columns.

It is a temporary bridge, not a permanent exemption.

### 4.2 Informative-Only Rows

A legacy `v1` row is informative only if it lacks inline pointer matter and is absent from the compatibility receipt.

Informative-only rows may still describe:

- intake
- triage
- candidate disposition work
- historical or analytic context

Informative-only rows must not be relied on as law by:

- downstream operators
- validators reporting operative authority
- exocortex control-plane summaries
- ontology projections

### 4.3 Legacy Schema Changes

Any schema addition, rename, merge, split, or field-family change that affects interpretation is authority-bearing.

During the compatibility window, the schema change itself must be ratified in repo law before any downstream validator or projection treats it as operative.

## 5. Compatibility Receipt Law

The compatibility receipt is the only temporary mechanism allowed to preserve legacy authority without immediate header churn.

Minimum obligations:

- one record per bound `candidate_id`
- one explicit pointer family per bound row
- one explicit effective date for the compatibility treatment
- one explicit statement that unbound rows remain `informative_only`

The compatibility receipt may coexist with the live tributary proof.
It may not rewrite the CSV header, mutate prior ledger lines, or invent substitute authority outside repo ratification.

## 6. Phase 2: Validator Compatibility

Validator compatibility lands only after Phase 1 is ratified.

During Phase 2, validators must:

- continue accepting the exact `v1` tributary header
- continue checking all existing structural invariants unchanged
- read the compatibility receipt when classifying legacy rows
- report the distinction between `authority_bound` and `informative_only`
- fail new authority-bearing additions made after the rollout effective date if they have neither compatibility binding nor inline pointer fields

During this phase, validation reports must keep the proof readable as one surface while making the authority split explicit.

At minimum the report must preserve:

- structural legality
- transition legality
- proof counts
- pointer-binding coverage
- any remaining informative-only rows

Phase 2 is a compatibility expansion, not a schema revision.

## 7. Phase 3: Header And Row-Shape Revision

Header change is the last rollout step.

It becomes lawful only after all of the following exist:

1. the schema-law transition is ratified
2. the validator can read the compatibility treatment
3. the legacy authority-bearing row set is bound by compatibility receipt
4. the current proof baseline has been preserved through the prior phases

Only then may the shell publish a later schema version with inline pointer fields.

That later version must:

- add the pointer family directly to authority-bearing registry rows
- define the matching ledger treatment for migration corrections
- allow a bounded dual-read window for `v1` and the later version
- migrate legacy relied-on rows without rewriting append-only history

`row_corrected` events may record migration corrections.
They may not erase prior events or fabricate retroactive history.

## 8. Non-Breaking Tributary Proof Rule

The live tributary proof remains authoritative during rollout.

Therefore:

- the current `v1` header remains normative until Phase 3
- the current append-only ledger remains untouched except for lawful new append events
- no rollout step may require historical file rewrite to establish present legality
- validation must remain capable of producing a clean report against the live proof family during transition

If a proposed change would break the proof before schema law and validator compatibility are in place, that proposal is unlawful and must be deferred.

## 9. Minimum Receipt Set

This rollout requires the following receipt sequence:

1. a rollout-law artifact that freezes the non-breaking order and baseline proof
2. a compatibility receipt binding the legacy authority-bearing row set
3. a validator rollout receipt that names the effective enforcement date
4. a later migration receipt for the inline-pointer schema version

No dashboard, ontology projection, or downstream registry may treat pointer rollout as complete until that receipt sequence exists.

## 10. Current Effect

This law is immediately binding on:

- the tributary disposition schema family
- future authority-bearing registry families that begin without inline pointer fields
- validator upgrades that classify operative authority
- any later migration that introduces inline pointer columns

The shell therefore adopts one lawful transition rule:

`schema law first -> validator compatibility second -> header change last`
