# Corpus Index

**Generated**: 2026-01-22
**Commit**: ccbdbea

---

## Directory Structure

```
syncrescendence/
├── 00-ORCHESTRATION/    # Coordination infrastructure
│   ├── directives/      # Active and completed directives
│   ├── execution_logs/  # Execution evidence
│   ├── oracle_contexts/ # Oracle session contexts
│   ├── scripts/         # Automation scripts
│   └── state/           # Dynamic state files (DYN-*)
│
├── 01-CANON/            # Constitutional knowledge (defended)
│   └── CANON-XXXXX-*    # Numbered canonical documents
│
├── 02-ENGINE/      # Living operational layer
│   ├── avatars/         # Avatar self-documentation
│   ├── functions/       # IIC function definitions
│   ├── memory/          # Memory architecture docs
│   ├── prompts/         # Prompt templates
│   ├── protocols/       # Operational protocols
│   └── registries/      # Reference registries (REF-*)
│
├── 02-ENGINE/QUEUE-*     # SYNTHESIS INBOX (absorbed from 03-QUEUE, QUEUE- prefixed)
│
├── 04-SOURCES/          # CURATED REFERENCES (preservation-worthy)
│   ├── raw/             # Unprocessed curated sources
│   └── processed/       # Sources with extracted value
│
├── 05-MEMORY/          # SHORT-TERM MEMORY (30-day TTL)
│
├── 06-EXEMPLA/          # WISDOM LAYER
│   ├── cautionary-tales/
│   ├── defrag-learnings/
│   ├── phase-markers/
│   └── templates/
│
├── -INBOX/              # Incoming artifacts (triage required)
├── -OUTGOING/           # Outbound deliverables
│
└── .constellation/      # Runtime state
    ├── tokens/          # Handoff tokens
    └── state/           # Current state snapshots
```

---

## Key References (Shorthand)

| Shorthand | Full Path | Purpose |
|-----------|-----------|---------|
| `MEM-ARCH` | `01-CANON/CANON-25000-MEMORY_ARCH-lattice.md` | Memory architecture + teleology (merged from 25000+25010) |
| `CONST-ARCH` | `01-CANON/CANON-25200-CONSTELLATION_ARCH-lattice.md` | Constellation architecture + teleology (merged from 25200+25210) |
| `MODAL-SEQ` | `01-CANON/CANON-00012-MODAL_SEQUENCE-cosmos.md` | Modal sequence framework |
| `EVAL-LENS` | `01-CANON/CANON-00007-EVALUATION-cosmos.md` | Evaluation & Resolutions (merged from 00007+00008) |
| `TASKS` | `00-ORCHESTRATION/state/DYN-TASKS.csv` | Active task ledger |
| `PROJECTS` | `00-ORCHESTRATION/state/DYN-PROJECTS.csv` | Project status ledger |

---

## CANON Ranges

| Range | Domain |
|-------|--------|
| 00001-00099 | Genesis (constitutional foundations) |
| 25000-25299 | Architecture (memory, constellation) |
| 30000-31999 | Operations (IIC, functions, chains) |

---

## Navigation Patterns

**For architectural questions**: Start with `CONST-TEL` or `MEM-TEL`
**For operational questions**: Check `02-ENGINE/` first
**For historical context**: Search `05-MEMORY/`
**For wisdom/patterns**: Reference `06-EXEMPLA/`
**For current state**: Check `00-ORCHESTRATION/state/DYN-*`

---

## Wisdom Layer (06-EXEMPLA)

| File | Purpose |
|------|---------|
| `APHORISMS.md` | Compressed wisdom statements |
| `PROVERBS.md` | Operational heuristics with context |
| `cautionary-tales/` | Anti-pattern narratives |
| `defrag-learnings/` | Execution cycle wisdom |
| `phase-markers/` | Transition documentation |

---

## Avatar Registry (02-ENGINE/avatars)

| Avatar | Function | Platform |
|--------|----------|----------|
| `IDEATE-ChatGPT-Acc1` | Ideation, novel abstractions | ChatGPT |

---

*This index is reference documentation. Update when structure changes significantly.*
