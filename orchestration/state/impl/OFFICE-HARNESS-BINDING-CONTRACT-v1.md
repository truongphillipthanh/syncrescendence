# Office-Harness Binding Contract v1

**Status**: live-v1
**Class**: implementation law
**Purpose**: define durable office identity, mutable harness binding, and the lawful precedence chain for office-to-harness state

## Compact Contract

- office identity is durable repo law
- harness binding is mutable repo-ratified metadata
- repo ratifies
- exocortex coordinates
- ontology projects

No harness, registry, control-plane surface, or projection may rename, split, merge, or silently redefine an office.

## 1. Stable Office Identity

An office is a federal role-bearing shell surface keyed by:

- `office_id`
- office path
- federal role burden

Office identity is stable across harness churn.

Changing a harness does not authorize:

- renaming an office directory
- changing office burden by implication
- creating a new office from a harness label
- promoting a stage0 or runtime surface into office status without repo ratification

`AGENTS.md` remains the constitutional source for:

- the recognized federal office set
- office titles and burden
- certified harness labels

## 2. Mutable Harness Binding

Harness binding is the current operational attachment between a stable office and a certified harness.

Harness binding is mutable because execution reality changes:

- harnesses may be upgraded
- offices may move between lawful surfaces
- machine, provider, or auth facts may change without changing the office itself

The canonical current-state declaration for a binding belongs in repo-resident per-office metadata, not in directory names, chat veneers, runtime habit, exocortex state, or ontology projection.

## 3. Precedence

The office-harness precedence chain is:

1. `AGENTS.md`
2. this contract
3. per-office binding metadata
4. rendered repo registries or ledgers derived from that metadata
5. validator reports
6. exocortex state and ontology projections

Higher layers win over lower layers.

Implications:

- a lower layer may repeat or render office-harness truth
- a lower layer may not redefine office identity or binding law
- playbooks and local office notes may clarify native grain but may not overrule binding law
- exocortex freshness and ontology convenience never outrank repo ratification

## 4. Rebinding Law

Rebinding is lawful only when the office remains stable and the binding changes through repo-resident artifacts.

Minimum rebinding sequence:

1. preserve office identity and path
2. update the per-office binding metadata
3. append any required repo ledger or receipt matter for the rebinding event
4. re-render any derived repo registry surface
5. run coherence validation before downstream reliance

Rebinding does not authorize retroactive reinterpretation of prior office work.

Historical work remains attached to the office that performed it, even if the office later binds to a different harness.

## 5. Ratification-Pointer Obligations

Any authority-bearing office-harness surface must carry ratification pointers.

Authority-bearing means the surface can change or imply:

- which harness currently speaks for an office
- whether a rebinding is operative
- whether downstream systems may rely on the binding
- whether a rendered row or event is merely informative or binding

Minimum pointer fields:

- `ratification_pointer`
- `ratified_by_artifact_path`
- `ratified_by_artifact_id`
- `ratified_at`

Rules:

1. Per-office metadata must identify the repo artifact that ratifies its binding law.
2. Any effective registry row that presents current binding as operative must carry or inherit the pointer family.
3. Any rebinding ledger event that claims authority must carry or resolve to the pointer family.
4. A row, event, or projection without ratification pointers is informative only.
5. Exocortex and ontology surfaces may mirror pointers; they may not originate substitute authority.

## 6. Minimum Obligations For Derived Surfaces

Rendered registries, ledgers, and validators are allowed because they improve queryability and drift detection.

They remain subordinate surfaces.

Minimum obligations:

- validators must compare office identity and harness binding against higher-precedence repo artifacts
- validators must report drift, missing pointer matter, and unlawful rebinding state
- rendered registries must be derived read models, not hand-authored constitutions
- exocortex and ontology projections must preserve the distinction between `operative` and `informative_only`

This contract does not require one specific validator implementation beyond those minimum obligations.

## 7. Repo / Exocortex / Ontology Compatibility

This contract is compatible with the governing split:

- repo ratifies office identity, binding law, and rebinding legitimacy
- exocortex coordinates live execution, routing, and operational visibility around the current binding
- ontology projects the typed relation between office, harness, and ratification lineage

Therefore:

- the repo remains the only source that can make a binding authoritative
- the exocortex may reflect live binding state but must not become the only home of binding legitimacy
- the ontology may project office-harness relations but must not invent new office classes, relation meaning, or binding status

## 8. Current Effect

This contract is immediately binding on:

- per-office office-harness metadata
- `orchestration/state/registry/office-harness-binding-ledger.jsonl`
- `orchestration/state/registry/office-harness-bindings.effective.json`
- `operators/validators/rematerialize_office_harness_bindings.py`
- office-harness coherence validators
- any exocortex or ontology surface that renders current office-harness state
