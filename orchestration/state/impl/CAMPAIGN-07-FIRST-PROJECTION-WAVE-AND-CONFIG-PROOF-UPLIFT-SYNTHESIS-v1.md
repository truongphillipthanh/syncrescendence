# Campaign 07 — First Projection Wave And Config Proof Uplift Synthesis v1

**Status**: live synthesis  
**Class**: campaign synthesis  
**Purpose**: reconstitute the true Campaign 07 outcome after landed worker writes, integration repair, and validator reruns

## 1. Executive Reading

Campaign 07 crossed two different thresholds at once.

It completed the proof uplift of `config_surface_state`, and it completed the first lawful exocortex-facing derivative projection for `office_harness_state` only after integration repair corrected worker-lane contract drift.

This matters because the shell is no longer organized only around seed registries, proof families, and doctrine.
It now has the beginnings of a governed family portfolio:

- `tributary_disposition` remains the strongest repo-native proof family
- `office_harness_state` is now both a true proof family and the first family with a lawful exocortex-facing derivative projection
- `config_surface_state` is now also a true repo-native proof family
- `chat_ci` is stronger inside repo sovereignty but remains a derivative config family, not yet a separate exocortex family

The project has therefore moved from "build proof families" into "govern widening across multiple family maturities without creating a second hidden control plane."

## 2. What Landed

### 2.1 Family Register Reconciliation

Campaign 07 correctly promoted:

- `office_harness_state` to `phase1_repo_proof`
- `config_surface_state` to `phase1_repo_proof`

The live register now records both append-only surfaces and phase-1 proof status at:

- `orchestration/state/registry/live-ledger-domain-register.csv`
- `orchestration/state/registry/live-ledger-domain-register-ledger.jsonl`

### 2.2 Config Proof Uplift

Campaign 07 completed the missing proof-family pieces for `config_surface_state`:

- rematerialization law at `orchestration/state/impl/CONFIG-SURFACE-LEDGER-REMATERIALIZATION-v1.md`
- deterministic rebuild operator at `operators/validators/rematerialize_config_surface_state.py`
- materializable ledger event in `orchestration/state/registry/config-surface-state-ledger.jsonl`
- parity-aware validator behavior in `operators/validators/validate_config_surface_state.py`

This means `config_surface_state` is no longer only a machine-addressable seed.
It is now rebuildable from repo-native append-only history.

### 2.3 First Office-Harness Projection Wave

Campaign 07 also landed the first lawful derivative office-harness projection family, but only after integration repair.

The worker pass created the necessary projection contract:

- `orchestration/state/impl/OFFICE-HARNESS-EXOCORTEX-PROJECTION-CONTRACT-v1.md`

But the initial bridge implementation over-projected all five offices and emitted a field-preserving subset that did not obey the contract.

That drift was repaired during integration.

The corrected projection now exists at:

- `orchestration/state/EXOCORTEX-OFFICE-HARNESS-PROJECTION-CC92.json`
- `orchestration/state/OFFICE-HARNESS-EXOCORTEX-PROJECTION-REPORT.json`
- `orchestration/state/OFFICE-HARNESS-EXOCORTEX-PROJECTION-REPORT.md`
- `operators/exocortex/office_harness_projection_bridge.py`

The repaired projection is now:

- scope-limited to `ajna` and `psyche`
- joined to the CC90 surface and teleology registries
- pointer-carrying back to repo-native office-harness law
- bound to the CC91 control-plane artifact by path and version
- derivative and replaceable rather than sovereign

### 2.4 Chat CI Strengthening

Campaign 07 widened `chat_ci` within repo sovereignty through:

- `orchestration/state/registry/CHAT-CI-PROVIDER-PROFILES-v1.json`
- `orchestration/state/registry/CHAT-CI-PROJECTION-PACK-v1.json`

This is a real strengthening of config-surface infrastructure, but it is still repo-native and manual-export only.
It is not yet its own exocortex-facing family.

### 2.5 Shared Family Audit

Campaign 07 also added the shared family portfolio auditor:

- `operators/validators/validate_live_ledger_domain_register.py`
- `orchestration/state/LIVE-LEDGER-DOMAIN-REGISTER-AUDIT-REPORT.json`
- `orchestration/state/LIVE-LEDGER-DOMAIN-REGISTER-AUDIT-REPORT.md`

The worker pass initially under-credited `config_surface_state` because the validator's filename pattern did not recognize `rematerialize_config_surface_state.py`.

That pattern drift was repaired during integration.

The shared audit now passes.

## 3. Validation State

Current validation after integration repair:

- constitution validation: `PASS`, `0` warnings
- tributary disposition validation: `PASS`, `10` rows, `50` ledger events, `0` findings
- office-harness coherence: `0` errors, `0` warnings
- config-surface state validation: `PASS`
- live-ledger domain register audit: `PASS`, `0` findings
- metadata naming: `7` active warnings, `11` tolerated findings

## 4. Holistic Interpretation

The shell now has three repo-native proof families or family-equivalents with clearly different outward states:

1. `tributary_disposition`
   - mature repo-native proof family
   - no new widening in this campaign

2. `office_harness_state`
   - proof-complete family
   - first lawful exocortex-facing derivative projection now exists

3. `config_surface_state`
   - proof-complete family after Campaign 07
   - stronger internal derivative surfaces exist via `chat_ci`
   - outward widening is still not yet formalized at the family level

This is the important transition.
The strategic bottleneck is no longer proof construction alone.
It is family portfolio governance:

- when does a proof family become default-ready
- when does it become projection-open
- what derivative projections are allowed
- how do exocortex-facing projections remain subordinate to repo sovereignty
- how do multiple families widen at different speeds without reintroducing hidden control planes

## 5. Campaign 07 Verdict

Campaign 07 is `complete with integration repair`.

That reading is stricter and more truthful than either naive success or simple partial failure.

The family-register reconciliation, config proof uplift, chat-ci strengthening, and family auditor all landed successfully.
The office-harness projection contract landed successfully.
The worker projection implementation drifted.
The integration pass repaired it.

So the final lawful outcome is:

- `office_harness_state` has a valid first projection wave
- `config_surface_state` is a true phase-1 proof family
- the shell can now move into projection governance rather than more proof-family bootstrapping

## 6. Next Macroscopic Leg

The next macroscopic leg is:

`projection governance + family phase advancement + second widening prep`

That means:

1. move the family register from proof inventory toward true phase governance
2. give the first projection family its own validator and append-only receipt history
3. define the narrow lawful outwardization path for `config_surface_state` through `chat_ci` manual-export discipline
4. create a family-portfolio report so the shell can reason about widening at the portfolio level rather than family by family in isolation

This is the correct acceleration vector because it widens the shell's governed operating surface instead of just adding more seed registries or more doctrine.

## 7. Receipts

- `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-00-COORDINATOR.md`
- `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-01-FAMILY-REGISTER-RECONCILIATION-AND-PHASE-ADVANCEMENT.md`
- `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-02-OFFICE-HARNESS-EXOCORTEX-PROJECTION-CONTRACT.md`
- `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-03-OFFICE-HARNESS-EXOCORTEX-PROJECTION-BRIDGE.md`
- `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-04-CONFIG-SURFACE-REMATERIALIZATION-CONTRACT-AND-BUILDER.md`
- `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-05-CHAT-CI-PROVIDER-PROFILES.md`
- `communications/responses/RESPONSE-CODEX-CAMPAIGN-07-LANE-06-LIVE-LEDGER-DOMAIN-REGISTER-AUDIT.md`
