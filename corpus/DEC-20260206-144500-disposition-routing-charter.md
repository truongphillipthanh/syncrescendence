# DEC — Disposition + Routing Charter (SaaS↔AI↔SaaS)

## Rename / designation
Replace “teleology” (too metaphysical + too final) with:

- **Disposition**: the tool’s *current* role assignment (ACTIVE / CONFIGURING / EVALUATING / DEFERRED / SUNSET) and the explicit *non-goals*.
- **Routing Charter**: what object types this surface is allowed to originate/own/mirror (TASK/PATCH/RESULT/NOTE/EVIDENCE), and what must RETURN to σ₄.

This name encodes tentativeness and makes change cheap.

## Charter (convergent policy)
### 1) Single internal bus
- **σ₄ repo + ledgers + filesystem kanban** is the internal bus.
- SaaS surfaces may mirror and notify; they do not silently replace canonical state.

### 2) Cheap-first integration ladder
1. **Human-mediated** (copy/link/checklists) for low-frequency or high-ambiguity flows.
2. **Native SaaS integrations** first (Linear↔GitHub, Linear→Slack, ClickUp→Slack).
3. **Make/Zapier** only for repeatable pain points with clear ROI and tolerant failure modes.
4. **Custom API glue** only when we need determinism/security/cost control beyond iPaaS.

### 3) Receipt requirement
Any automation that changes state must emit a durable receipt:
- ledger event and/or RESULT artifact (commit hash + files changed + push confirmation if code).

## Why this is the right designation
- Prevents “tool metaphysics”: we’re assigning *current operating roles*, not eternal purposes.
- Makes drift legible: a disposition change is a one-line diff + a migration note.
- Enforces sovereignty: routing charter makes explicit what can be canonical where.

## Falsifier
This decision is wrong if:
- collaboration friction requires SaaS to become canonical for specific objects (e.g., tasks) to reduce overhead
- native integrations are too weak, forcing Make/Zapier for baseline hygiene

## Next step
Update REF-SAAS_INTEGRATION_ARCHITECTURE.md headings and tables to use Disposition + Routing Charter terminology and add a per-surface charter section.
