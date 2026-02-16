---
id: DEC-20260206-113900-saas-integration-teleology
kind: decision
scope: orchestration
status: proposed
created: 2026-02-06
updated: 2026-02-06
related:
  - 02-ENGINE/REF-SAAS_INTEGRATION_ARCHITECTURE.md
  - 00-ORCHESTRATION/state/DYN-DISPATCH_KANBAN_PROTOCOL.md
  - 00-ORCHESTRATION/state/ARCH-TOOLCHAIN_CLARESCENCE.md
---

# DEC — SaaS Integration Teleology (Cheap-first, Sovereignty-first)

## Decision
Adopt a **three-tier integration posture** that prioritizes sovereignty and cheap “hits”:

1) **Truth + workflow bus stays local (σ₄)**: repo + ledgers + filesystem-kanban remain canonical. SaaS is never the only copy of state.

2) **Use native integrations first (σ₆/σ₇, near-zero marginal cost)**:
   - Linear ↔ GitHub, Linear → Slack, ClickUp → Slack, etc.
   - Prefer vendor-maintained bridges for reliability and low ops burden.

3) **Use Make/Zapier only for “luxury pain points” (paid hits) with explicit ROI**:
   - Only when (a) native doesn’t exist, (b) the workflow is high-frequency, and (c) the failure mode is tolerable.
   - Minimize scenarios; prefer coarse-grained events (daily digest) unless real-time is mission-critical.

## Rationale
- **σ₇-first**: we already have a deterministic execution substrate (kanban + watchers). Don’t reintroduce brittleness by moving canonical state to SaaS.
- **Token/cost economics**: API calls and automation triggers should be treated as “metered resources”; reserve them for repeatable pain points.
- **Drift control**: keeping σ₄ canonical prevents SaaS divergence from silently rewriting operational truth.

## Teleology (role of each SaaS)
- **Linear**: tasks *on* the corpus (SYN-*). Owns issue lifecycle; GitHub is execution artifact surface.
- **ClickUp**: tasks *about* the corpus (meta-work, ops, coordination) unless a task must touch code.
- **Slack/Discord**: notification + coordination surfaces; never canonical task truth.
- **Drive/NotebookLM**: ingest/synthesis library; outputs must RETURN to repo.

## Guardrails
- Every automated bridge must have:
  - explicit source-of-truth statement
  - idempotency strategy
  - failure policy (retry vs drop vs quarantine)
  - durable receipt (ledger entry or RESULT artifact)

## Falsifier
This decision is wrong if:
- native integrations prove too lossy/laggy and create more manual work than they save
- the repo-centric bus creates excessive friction for collaborators who live in SaaS
- Make/Zapier event volume remains low even for high-value workflows (meaning we under-automated)
