# TEMPLATE-ADR.md
## Architecture Decision Record Template
Version: 1.0.0
Updated: 2026-02-24
**Authority**: DC-304 — ADR format standardization

---

## Template

```markdown
# ADR-XXXX: [Title]

**Status**: proposed | accepted | superseded | deprecated
**Date**: YYYY-MM-DD
**Deciders**: [Sovereign / Agent names]
**Council**: [Council number, if applicable]
**IntentionLink**: INT-XXXX, DC-XXXX

---

## Context

[What is the issue? What forces are at play? Why does this decision need to be made now?
Include the triggering directive or observation.]

## Triangulation Evidence

| Agent | Role | Finding | Confidence |
|-------|------|---------|------------|
| Oracle (Grok) | RECON | [Thesis + industry consensus] | HIGH/MEDIUM/LOW |
| Diviner (Gemini) | REASON | [Novel synthesis] | HIGH/MEDIUM/LOW |
| Adjudicator (Codex) | ENGINEER | [Technical feasibility] | HIGH/MEDIUM/LOW |
| Commander (Claude) | COMPILE | [Synthesis + execution plan] | HIGH/MEDIUM/LOW |

[Delete rows for agents that did not participate. If no triangulation was performed, replace
this section with: **Triangulation**: None — single-agent decision by [agent].]

## Decision

[The decision in one or two sentences. Use active voice: "We will..." / "The system shall..."]

### Rationale

[Why this option over alternatives. Reference triangulation convergence points.]

### Alternatives Considered

| Option | Pros | Cons | Why Rejected |
|--------|------|------|--------------|
| [Alt 1] | ... | ... | ... |
| [Alt 2] | ... | ... | ... |

## Consequences

### Positive
- [Expected benefit]

### Negative
- [Known cost or risk accepted]

### Neutral
- [Side effect that is neither good nor bad]

## Related

| Type | Reference | Relationship |
|------|-----------|-------------|
| ADR | ADR-XXXX | supersedes / superseded-by / relates-to |
| ARCH | ARCH-*.md | implements / informed-by |
| CANON | CANON-*.md | codifies / references |
| DC | DC-XXXX | originates-from / enables |
| INT | INT-XXXX | fulfills / advances |
```

---

## Example: ADR-0001 (DC-204T)

# ADR-0001: Sanctify Numbered Directory Layers

**Status**: accepted
**Date**: 2026-02-23
**Deciders**: Sovereign, Commander
**Council**: Council 22 (retroactive ratification)
**IntentionLink**: DC-204T, DC-146 (superseded), DC-207 (resolved)

---

## Context

The constellation scaffold contained numbered-prefix directories (`00-ORCHESTRATION/`, `02-ENGINE/`, `05-SIGMA/`) inherited from an earlier organizational phase. DC-146 proposed renaming these to semantic names. The INT-2210 disaster (mass rename/delete of 3,966 lines) demonstrated that structural renames carry catastrophic risk. DC-204T re-examined whether the numbered layers should be renamed or sanctified as-is.

Oracle and Diviner independently analyzed the seven architectural patterns of the scaffold. Both confirmed the numbered layers encode real semantic meaning (ordering, provenance, structural archaeology) that would be destroyed by renaming.

## Triangulation Evidence

| Agent | Role | Finding | Confidence |
|-------|------|---------|------------|
| Oracle (Grok) | RECON | Numbered prefixes are load-bearing structural markers, not cosmetic. Renaming risks breaking hook paths and mental models. | HIGH |
| Diviner (Gemini) | REASON | Numbered layers function as geological strata — they encode temporal provenance. Flattening destroys information. | HIGH |
| Commander (Claude) | COMPILE | Convergence is unanimous: sanctify, do not rename. Update AGENTS.md to explicitly bless 00-/02-/05- as sanctioned containers. | HIGH |

## Decision

Sanctify the existing numbered-prefix directories (`00-ORCHESTRATION/`, `02-ENGINE/`, `05-SIGMA/`) as permanent sanctioned structural containers. Do not rename them to semantic equivalents. Update AGENTS.md Constitutional Rule 1 (FLAT PRINCIPLE) to explicitly list them as sanctioned exceptions with rationale.

### Rationale

Three independent assessments converged: the numbered prefixes carry real information (ordering, provenance, structural history). Renaming would break hook paths, invalidate documentation references, and destroy archaeological layering — for purely cosmetic benefit. The INT-2210 disaster proved that structural renames without full-system validation are catastrophic. Cost of renaming exceeds cost of sanctifying.

### Alternatives Considered

| Option | Pros | Cons | Why Rejected |
|--------|------|------|--------------|
| Rename to semantic names (DC-146) | Cleaner naming | Breaks hooks, refs, mental models; INT-2210 risk | Unanimously rejected by triangulation |
| Remove numbered dirs entirely | Radical simplification | Destroys provenance; massive migration | Incompatible with constitutional FLAT principle |
| Keep but undocumented | No work required | Ambiguity invites future rename attempts | Insufficient — explicit sanctioning prevents recurrence |

## Consequences

### Positive
- Eliminates future rename proposals (decision is now canonical)
- Preserves hook path stability
- Maintains structural archaeology for future agents

### Negative
- New agents must learn that 00-/02-/05- are intentional, not legacy debt

### Neutral
- DC-146 is now superseded; DC-207 resolved as a side effect

## Related

| Type | Reference | Relationship |
|------|-----------|-------------|
| DC | DC-204T | originates-from |
| DC | DC-146 | supersedes |
| DC | DC-207 | resolves |
| ARCH | ARCH-MEMORY_ARCHITECTURE.md | relates-to (same triangulation methodology) |
| CANON | CANON-25500-ARCHITECTURE_RATIONALE-lattice.md | codifies |
