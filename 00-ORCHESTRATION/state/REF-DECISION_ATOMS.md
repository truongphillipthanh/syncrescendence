# Decision Atom Schema

A decision atom is the smallest unit of durable choice. No durable change exists without one.

## Required fields
- **Decision ID**: stable identifier (e.g., `DEC-20260119-001`).
- **Choice**: the explicit action being taken.
- **Why (1-2 lenses)**: name the primary lens(es) that justify the choice.
- **Falsifier**: what would make this decision wrong.
- **Reversibility type**: reversible, costly-reversible, or irreversible.
- **Touched surfaces**: files, systems, or workflows impacted.
- **Evidence pointers**: minimal set of links to sources or packs.

## Template
```markdown
Decision ID: DEC-YYYYMMDD-HHMMSS[-slug]  # stable identifier
Choice:                                   # explicit action
Why (lens 1-2):                           # name the primary lens(es)
Falsifier:                                # what would make this wrong
Reversibility type: reversible | costly-reversible | irreversible
Touched surfaces:                         # files/systems/workflows impacted
Evidence pointers:                        # minimal links (paths/URLs)

# Optional (Syncrescendence plumbing)
DecisionAtom: DEC-YYYYMMDD-HHMMSS[-slug]  # same as Decision ID; used in TASK/PROMPT headers
IntentionLink: INT-XXXX                   # optional link to ARCH-INTENTION_COMPASS
Fingerprint: <git-short-hash>             # optional, if a repo state checkpoint exists
```

## Enforcement rules
- If **Falsifier** is empty, the decision is invalid.
- If **Reversibility type** is missing, risk is undefined and execution must halt.
- If **Evidence pointers** are missing, the decision is not durable and must remain provisional.

## Example (minimal)
```markdown
Decision ID: DEC-20260119-001
Choice: Place the cognitive nucleus in 00-ORCHESTRATION root (flat principle compliance).
Why (lens 1-2): Syncrescendent Route, Agentify + Human-Navigable
Falsifier: A sanctioned exception permits a new /core directory without violating flat principle.
Reversibility type: reversible
Touched surfaces: 00-ORCHESTRATION/*
Evidence pointers: CLAUDE.md, 00-ORCHESTRATION/state/REF-STANDARDS.md
```
