Decision ID: DEC-20260204-175303-techstack-truth-surface
Choice: Unify “model_db” and “Tech Stack DB” by declaring a single canonical boundary: **model intelligence (models/pricing/capabilities/routing)** remains in `orchestration/state/model_intelligence.db` (managed by `model_db.py`), while **apps/workflows/primitives/apparatus** becomes the future “Tech Stack DB” slice. The Tech Stack DB must *not* create a second overlapping models/pricing store; it must import from, or federate to, model_intelligence.
Why (lens 1-2): Systems Thinking (one truth surface per domain), Antifragile (reduce drift/duplication)
Falsifier: If CANON-30300’s intended schema requires cross-table queries that cannot be achieved cleanly via federation/ETL (e.g., apparatus ↔ model pricing joins) without unacceptable complexity, then we should collapse into one DB schema and deprecate `model_db.py` as a standalone.
Reversibility type: costly-reversible
Touched surfaces: orchestration/scripts/model_db.py; CANON-30300-TECH_STACK-*; future `orchestration/state/techstack/*`; Makefile targets (techstack-import/seed)
Evidence pointers: canon/CANON-30300-TECH_STACK-comet-INTELLIGENCE.md; orchestration/scripts/model_db.py (header: “pilot implementation of CANON-30300 subset”); orchestration/state/impl/tooling/INTERDEPENDENCIES-CONFLICTS.md

# Operator notes (digest rationale)
- This keeps **normalization** intact: one canonical store for model economics + routing; everything else can reference it.
- It prevents “two DBs, two truths” while still allowing Tech Stack DB to grow into apps/workflows.
- It matches your near-term swarm shift: routing should move toward **platform-native swarms**, but we still need one consistent place to express cost/capability metadata.

# Implementation implications
- Add an explicit statement to CANON-30300: "models/pricing truth lives in model_intelligence; techstack DB references it."
- Tech Stack DB import should ingest apps/workflows only, and optionally materialize a *read-only* view of models via ETL snapshot.

# Optional (Syncrescendence plumbing)
DecisionAtom: DEC-20260204-175303-techstack-truth-surface
IntentionLink: —
Fingerprint: 9e9b409
