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
Decision ID:
Choice:
Why (lens 1-2):
Falsifier:
Reversibility type:
Touched surfaces:
Evidence pointers:
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
