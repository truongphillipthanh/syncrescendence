---
id: CLARESCENCE-2026-02-12-mba-commander-reinit
type: clarescence
fidelity: operational
passes_run: 0+1-7
date: 2026-02-12
agent: commander
topic: Commander reinit prompt for MacBook Air — session bootstrap context
predecessors:
  - CLARESCENCE-2026-02-11-mba-commander-init.md
  - CLARESCENCE-2026-02-09-mba-ajna-setup.md
  - CLARESCENCE-2026-02-12-post-da11-next-path.md
---

# CLARESCENCE: MBA Commander Reinit Prompt

**Date**: 2026-02-12
**Fidelity**: Operational (Passes 0+1-7)
**Agent**: Commander (Mac mini, producing artifact for MBA instance)
**IntentionLink**: INT-1504, INT-P015, INT-1202, SYN-35

---

## Convergent Path

Produce a comprehensive reinit prompt that transforms a bare Claude Code session on MBA into a fully oriented Constellation Commander/COO, aware of its machine role, fleet state, active decisions, and coordination protocols.

---

## Decision Atom

**DA-13**: The MBA Commander reinit prompt is a persistent session bootstrap file at `-INBOX/commander/MBA-COMMANDER-REINIT.md`, designed to be pasted into a new Commander session on the MacBook Air.

- **Canonical truth surface**: `-INBOX/commander/MBA-COMMANDER-REINIT.md` (repo)
- **Reversibility**: Full — delete the file
- **Falsifier**: If MBA Commander auto-loads sufficient context from CLAUDE.md + memory/MEMORY.md without a reinit prompt, this artifact is redundant
- **Confidence**: High (90%) — CLAUDE.md provides structural rules but not operational state or machine-specific identity

---

## Rationale

1. CLAUDE.md loads constitutional rules but NOT machine identity, fleet state, or active decisions
2. memory/MEMORY.md on MBA is a thin stub (written by mba-commander-init.sh) — lists machine differences but not operational context
3. A reinit prompt bridges the gap: constitutional law (CLAUDE.md) + machine identity + fleet state + active directives
4. INT-P015 requires MBA Commander to wake up knowing it's the "kinetic micro" engine
5. Prior clarescence (2026-02-11) produced init scripts but not the cognitive bootstrap

---

## Artifact: MBA Commander Reinit Prompt

See: `-INBOX/commander/MBA-COMMANDER-REINIT.md`

---

## Energy Cost

- Clarescence: ~15 minutes, ~8K tokens
- Prompt artifact: ~3K tokens (persistent, reusable)
- Total: one-time investment, amortized over every MBA Commander session

---

## Dependencies

- DA-13 → SYN-35 (MBA setup completion)
- DA-13 builds on DA-01–DA-04 (prior MBA Commander init)
- DA-13 references DA-12 (current execution vector)
