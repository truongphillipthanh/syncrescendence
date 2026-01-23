# 05-MEMORY: SHORT-TERM MEMORY

## Purpose (Revised 2026-01-22)
This directory is a STAGING AREA for metabolism, not permanent storage.

## Principle: Integrate or Expel
- Items here have an implicit 30-day TTL
- If not integrated within 30 days, consider deletion
- Git history is the true permanent archive

## What Belongs Here
- Superseded documents awaiting value extraction
- Old scaffolding that might have residual value
- Temporary staging during refactors
- Session artifacts with extracted wisdom (raw materials after EXEMPLA capture)

## What Does NOT Belong Here
- Anything you want to keep forever (that's git history)
- Reference materials (that's 04-SOURCES)
- Constitutional knowledge (that's 01-CANON)

## Lifecycle
1. Document superseded or deprecated
2. Moved here for short-term holding
3. Either:
   - Value extracted → integrated elsewhere (EXEMPLA, CANON, OPERATIONAL)
   - No value → deleted (git preserves history)

## Teleology
"Not a graveyard—a compost heap. Decompose into nutrients or discard."

---

## Structure (FLAT)

All files at root level. Prefix conventions:

### ARCH- Prefix (Implementation Specs)

| File | Source | Purpose |
|------|--------|---------|
| ARCH-ARTIFACT-PATTERN-LANGUAGE.md | Coherence restoration | Pattern language framework |
| ARCH-COGNITIVE-PALACE-FULL.md | Coherence restoration | Full Palace architecture |
| ARCH-constellation-*.jsx | Constellation diagrams | Superseded by implementation |

### SCAFF- Prefix (Oracle Process Archaeology)

Historical working documents from Oracle 4-9, preserved for process learning:
- SCAFF-ALPHA_* — Oracle5 restoration reconnaissance
- SCAFF-BETA_* — Oracle5-6 early specs (superseded by STANDARDS)
- SCAFF-*_REPORT.md — Various audit and status reports

### Session Archives (30-day TTL)

| Directory | Purpose |
|-----------|---------|
| chorus-session-20260122/ | Chorus architecture session artifacts |

---

## Relationship to Other Tiers

```
00-ORCHESTRATION/ — Coordination infrastructure
01-CANON/         — What (constitutional, defended)
02-ENGINE/   — Active (living documents)
03-QUEUE/         — Synthesis inbox (high-signal only)
04-SOURCES/       — Curated references (preservation-worthy)
05-MEMORY/       — Short-term memory (30-day TTL) <- THIS
06-EXEMPLA/       — Wisdom layer (civilizational knowledge transfer)
```

---

## Usage

- **Extract value before 30-day TTL expires**
- **Move wisdom to 06-EXEMPLA**
- **Delete with confidence** — git preserves history

**Do not hoard. Metabolize or release.**

---

*Revised via DIR-20260122-SEMANTIC-ANNEALMENT-INTEGRATED. January 2026.*
