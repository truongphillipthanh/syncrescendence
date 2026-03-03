# Manus First Dispatch — CC73

**Date**: 2026-03-02  
**Purpose**: First controlled Manus break-in under the new boundary contract

## Why This Exists

Manus should not be onboarded as an isolated autonomous island.

It should enter the system as an **exocortex surface** that:

- performs bounded autonomous work
- returns results as structured checkpoints
- feeds the same reconciliation and ontology pipeline as Ajna/Obsidian/runtime state

## First Objective

Use Manus for the narrowest high-leverage autonomous backend task that tightens the tooling stack:

**Provision and/or scaffold the ontology API deployment path around `syncrescendence.com` without inventing new authority surfaces.**

## First Task Envelope

Ask Manus to do only these things:

1. Read the current deployment shape:
   - `orchestration/state/impl/ONTOLOGY-DOMAIN-STAGE1.md`
   - `orchestration/state/impl/ontology-api.Caddyfile.example`
   - `ontology_v1.py`
   - `Makefile`

2. Determine the minimum deployable path for:
   - local API service
   - reverse proxy
   - health check
   - restart strategy

3. Return only:
   - exact commands
   - exact config file content
   - exact assumptions/blockers
   - no speculative architecture rewrite

4. If Manus can perform the work directly, it must still report the result as a structured checkpoint, not as a new authority surface.

## Constraints

Manus must not:

- invent a second database of record
- invent a second task system
- bypass the repo/event/ontology pipeline
- store secrets in repo artifacts
- mirror raw third-party payloads into markdown

## Required Return Shape

Manus should return:

1. `Objective`
2. `Assumptions`
3. `Commands To Run`
4. `Files To Create Or Update`
5. `Blockers`
6. `Verification`
7. `Boundary Contract Notes`

## Event Return Contract

When Commander relays Manus results back into Syncrescendence, capture them with:

- `surface: "exocortex"`
- `artifact_class: "manus_workflow"`
- `type: "manus_queue_state"` or more specific workflow type
- `durable_capture: "summary_and_typed_record"`

Suggested bridge command:

```bash
python3 manus_checkpoint_bridge.py \
  --workflow ontology_domain_stage1 \
  --status returned_from_manus \
  --summary "Captured Manus ontology deployment checkpoint." \
  --repo-paths orchestration/state/impl/ONTOLOGY-DOMAIN-STAGE1.md \
  --project-ontology \
  --ontology-url domain
```

## Best First Manus Prompt

You are being used as a bounded autonomous backend operator inside Syncrescendence.

Your task is not to redesign architecture. Your task is to operationalize the existing Stage 1 ontology domain plan with the smallest safe deployment surface.

Read these files first:

- `orchestration/state/impl/ONTOLOGY-DOMAIN-STAGE1.md`
- `orchestration/state/impl/ontology-api.Caddyfile.example`
- `ontology_v1.py`
- `Makefile`

Then return:

- the minimum exact deployment sequence
- the exact config changes required
- the blockers if the domain/DNS edge is not actually live yet
- the verification commands

Do not invent a dashboard. Do not invent a second state store. Do not bypass the repo/event/ontology pipeline.
