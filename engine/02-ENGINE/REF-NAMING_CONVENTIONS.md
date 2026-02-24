---
id: ref-naming_conventions
kind: reference
scope: constellation
target: all-agents
dc: DC-300
---

# Naming Conventions Specification

**Version**: 1.0.0
**Updated**: 2026-02-24
**Authority**: Council 25 / Commander
**Cadence**: on-change

---

## 1. Prefix Matrix

All prefixed files use `UPPER_SNAKE_CASE` names. The prefix encodes semantic type, mutability, and lifecycle.

| Prefix | Semantic Meaning | Scope | Mutability | Primary Location(s) | Examples |
|--------|-----------------|-------|------------|---------------------|----------|
| `ARCH-` | Architectural decision, design doc, or structural rationale | orchestration | Append-only (archive when superseded) | `orchestration/00-ORCHESTRATION/archive/`, `orchestration/state/` | `ARCH-MEMORY_ARCHITECTURE.md`, `ARCH-INTENTION_COMPASS.md` |
| `DYN-` | Dynamic state: ledgers, logs, registries, queues, configs that change frequently | engine, orchestration | Mutable (high-frequency writes) | `engine/02-ENGINE/`, `orchestration/state/` | `DYN-LEDGER-TOKEN_ECONOMICS.md`, `DYN-SESSION_LOG.md`, `DYN-CONSTELLATION_CONFIGURATION.json` |
| `REF-` | Reference material: guides, handbooks, specifications, mappings | engine, praxis, sources | Stable (updated deliberately) | `engine/02-ENGINE/`, `praxis/05-SIGMA/` | `REF-ROSETTA_STONE.md`, `REF-FLEET_COMMANDERS_HANDBOOK.md`, `REF-NAMING_CONVENTIONS.md` |
| `FUNC-` | Executable function prompt (callable by agents) | engine | Stable (versioned) | `engine/02-ENGINE/` | `FUNC-optimize.xml`, `FUNC-harmonize.xml`, `FUNC-absorb.xml` |
| `PROMPT-` | Dispatch prompt for a specific agent on a specific task | engine, -SOVEREIGN | Immutable once dispatched | `engine/02-ENGINE/`, `-SOVEREIGN/` | `PROMPT-ORACLE-SCAFFOLD_CONSENSUS.md`, `PROMPT-UNIFIED-Grok-unified-prompt.md` |
| `CANON-` | Verified canonical knowledge (immutable truth) | canon | Immutable (PROTECTED) | `canon/01-CANON/` | `CANON-00001-ORIGIN-cosmos.md`, `CANON-35000-WISDOM-chain.md` |
| `SOURCE-` | Raw source material (transcripts, articles, research) | sources | Immutable (raw input) | `sources/04-SOURCES/` | `SOURCE-YOUTUBE-transcript.md`, `SOURCE-RESEARCH-paper.md` |
| `EXTRACT-` | Extracted atoms from source mining pipeline | sources | Immutable (pipeline output) | `sources/04-SOURCES/` subdirs | `EXTRACT-atom-001.md` |
| `AVATAR-` | Agent personality/identity profile for a platform | engine | Stable (updated per IIC change) | `engine/02-ENGINE/` | `AVATAR-CHATGPT.md`, `AVATAR-GEMINI-CLI.md` |
| `IIC-` | Individual Intelligence Configuration (agent spec) | engine | Stable (versioned) | `engine/02-ENGINE/` | `IIC-COMMANDER.md`, `IIC-ADJUDICATOR.md` |
| `TEMPLATE-` | Reusable structural template | engine, orchestration | Stable | `engine/02-ENGINE/`, `orchestration/00-ORCHESTRATION/templates/` | `TEMPLATE-IIC.md`, `TEMPLATE-EXECUTION_LOG.md` |
| `MODEL-` | Model capability profiles and indexes | engine | Mutable (tracks frontier) | `engine/02-ENGINE/` | `MODEL-INDEX.md` |
| `RESPONSE-` | Triangulated agent response (inbox artifact) | agents | Immutable (evidence) | `-INBOX/commander/00-INBOX0/` | `RESPONSE-ORACLE-SCAFFOLD_CONSENSUS.md` |
| `QUEUE-` | Pending work items in sovereign queue | -SOVEREIGN | Mutable (consumed on processing) | `-SOVEREIGN/` | `QUEUE-DC205-BATCH.md` |
| `SOVEREIGN-` | Sovereign decision records | -SOVEREIGN | Immutable (decisions are final) | `-SOVEREIGN/` | `SOVEREIGN-DECISION-001.md` |
| `MECH-` | Mechanism deep-dive (how something works) | praxis | Stable | `praxis/05-SIGMA/mechanics/` | `MECH-MEMORY_COMPACTION.md` |
| `PRAC-` | Practice pattern (how to do something) | praxis | Stable | `praxis/05-SIGMA/practice/` | `PRAC-SESSION_STARTUP.md` |
| `SYNTHESIS-` | Cross-domain synthesis document | praxis | Stable | `praxis/05-SIGMA/syntheses/` | `SYNTHESIS-PLATFORM_COMPARISON.md` |
| `EXEMPLA-` | Worked example / case study | praxis | Immutable | `praxis/05-SIGMA/` | `EXEMPLA-INT2210_POSTMORTEM.md` |
| `MOC-` | Map of Content (index/navigation) | any | Mutable | varies | `MOC-ENGINE.md` |
| `SCAFF-` | Scaffold validation / structural enforcement | orchestration | Stable | `orchestration/00-ORCHESTRATION/scripts/` | `SCAFF-VALIDATE.sh` |
| `HANDOFF-` | Cross-platform handoff token | agents | Immutable (snapshot) | `agents/<name>/outbox/` | `HANDOFF-20260223-143000-p1-to-p2.md` |
| `DECISION-` | Decision atom (triangulated conclusion) | orchestration | Immutable | `orchestration/00-ORCHESTRATION/archive/` | `DECISION-DC204-DISPATCH.md` |
| `ALERT-` | Urgent notification requiring sovereign attention | -SOVEREIGN | Mutable (consumed) | `-SOVEREIGN/` | `ALERT-WORKER_CRASH.md` |
| `RECEIPT-` | Execution receipt / proof of work | agents | Immutable | `agents/<name>/outbox/` | `RECEIPT-DC208-BATCH3.md` |

---

## 2. Prefix Selection Rules

Choose the prefix by answering these questions in order:

1. **Is it raw input material?** --> `SOURCE-`
2. **Is it extracted from sources by pipeline?** --> `EXTRACT-`
3. **Is it verified, immutable canonical knowledge?** --> `CANON-`
4. **Is it a callable function/skill?** --> `FUNC-`
5. **Is it a dispatch prompt for an agent?** --> `PROMPT-`
6. **Is it an agent identity profile?** --> `AVATAR-` or `IIC-`
7. **Is it a reusable structural template?** --> `TEMPLATE-`
8. **Does it change frequently (state, logs, ledgers)?** --> `DYN-`
9. **Is it an architectural decision or design?** --> `ARCH-`
10. **Is it a stable reference document?** --> `REF-`
11. **Is it a mechanism/practice/synthesis?** --> `MECH-` / `PRAC-` / `SYNTHESIS-`
12. **Is it a response from a triangulated agent?** --> `RESPONSE-`
13. **Is it a sovereign decision or queue item?** --> `SOVEREIGN-` / `QUEUE-`

If none apply, the file likely belongs in an agent scratchpad without a prefix.

---

## 3. Directory Placement Rules

Prefixes are bound to directories. Do not place a prefixed file outside its sanctioned location.

| Directory | Sanctioned Prefixes |
|-----------|-------------------|
| `canon/01-CANON/` | `CANON-` only |
| `engine/02-ENGINE/` | `REF-`, `DYN-`, `FUNC-`, `PROMPT-`, `AVATAR-`, `IIC-`, `TEMPLATE-`, `MODEL-` |
| `sources/04-SOURCES/` | `SOURCE-`, `EXTRACT-`, `REF-` (mappings only), `DYN-` (source index only) |
| `praxis/05-SIGMA/` | `REF-`, `MECH-`, `PRAC-`, `SYNTHESIS-`, `EXEMPLA-`, `MOC-` |
| `orchestration/00-ORCHESTRATION/` | `ARCH-`, `DYN-`, `TEMPLATE-`, `SCAFF-`, `DECISION-` |
| `orchestration/state/` | `ARCH-`, `DYN-` |
| `-SOVEREIGN/` | `PROMPT-`, `QUEUE-`, `SOVEREIGN-`, `ALERT-` |
| `-INBOX/*/00-INBOX0/` | `RESPONSE-` |
| `agents/<name>/outbox/` | `RECEIPT-`, `HANDOFF-`, `RESULT-` |
| `agents/<name>/scratchpad/` | No prefix required (working files) |

---

## 4. Numbered-Layer Exceptions

Per DC-204T evidence analysis (Council 22, 2026-02-23), the following numbered-prefix directories are **sanctioned structural containers**. They exist because their parent semantic directories require a canonical implementation layer.

| Layer | Directory | Rationale |
|-------|-----------|-----------|
| `00-` | `orchestration/00-ORCHESTRATION/` | Canonical strategic-coordination layer (state, scripts, archive, templates) |
| `02-` | `engine/02-ENGINE/` | Canonical engine implementation layer (147+ files) |
| `05-` | `praxis/05-SIGMA/` | Canonical praxis container (mechanics, practice, syntheses) |
| `01-` | `canon/01-CANON/` | Canonical knowledge container |
| `04-` | `sources/04-SOURCES/` | Canonical source material container |
| `00-` | `-INBOX/*/00-INBOX0/` | Canonical inbox container |

**Rule**: No new numbered-prefix directories may be created without Sovereign approval and DC evidence. These are architectural, not cosmetic.

---

## 5. Case and Formatting Rules

### Files
- **Prefixed files**: `PREFIX-UPPER_SNAKE_CASE.ext` (e.g., `REF-NAMING_CONVENTIONS.md`, `DYN-LEDGER-TOKEN_ECONOMICS.md`)
- **Sub-prefix chaining**: Use hyphens to chain a category after the prefix (e.g., `DYN-LEDGER-*`, `PROMPT-UNIFIED-*`, `PROMPT-ORACLE-*`)
- **Constitutional files**: `UPPER_SNAKE_CASE` without prefix for root-level governance docs (`CLAUDE.md`, `GEMINI.md`, `AGENTS.md`)
- **Scripts**: `lowercase_snake_case.sh` / `.py` (e.g., `memsync_daemon.py`, `journal_append.sh`)
- **Config files**: `lowercase` or standard naming (`.json`, `.yaml`, `.csv`)

### Directories
- **Top-level**: lowercase semantic names (`orchestration`, `canon`, `engine`, `sources`, `praxis`, `agents`, `collab`)
- **Special**: dash-prefixed directories are architectural namespaces (`-SOVEREIGN`, `-INBOX`)
- **Numbered layers**: `NN-UPPER` pattern (e.g., `00-ORCHESTRATION`, `02-ENGINE`)
- **Agent offices**: `agents/<lowercase-name>/` with standard substructure
- **Praxis subdirs**: `lowercase/` under `05-SIGMA/` (e.g., `mechanics/`, `practice/`, `syntheses/`)

---

## 6. CANON- Numbering Scheme

Canon files follow a hierarchical numbering system encoding their position in the ontological tree:

```
CANON-NNNNN-TITLE-tier.md
```

- **NNNNN**: 5-digit address in the knowledge lattice (00001-99999)
- **TITLE**: `UPPER_SNAKE_CASE` topic name
- **tier**: lowercase celestial tier (cosmos, lattice, chain, comet, ring, planetary, satellite, lunar, asteroid)
- Compound tiers chain with hyphens: `CANON-31142-PLATFORM_GRAMMAR-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md`

---

## 7. Anti-Patterns (DO NOT)

These anti-patterns are documented from real incidents. Violating them risks data loss or structural incoherence.

### 7.1 Renaming Without Authority (INT-2210)
**Do not** rename directories or reorganize file placement without scaffold_validate passing, memory operational, and rollback tested. The INT-2210 disaster (2026-02-22) deleted 3,966 lines and required a 6-commit revert because a "tidy-up" was treated as license to restructure.

### 7.2 Subdirectory Proliferation
**Do not** create subdirectories where prefixes suffice. The Flat Principle exists to prevent navigation depth. If you need to group files, use a shared prefix segment (e.g., `DYN-LEDGER-*`) not a `ledgers/` subdirectory.

### 7.3 Prefix Invention
**Do not** invent new prefixes without adding them to this specification first. One-off prefixes (e.g., `CLAUDECRON-`, `GROK-`, `FLEET-`) create semantic orphans that no agent knows how to route.

### 7.4 Wrong-Directory Placement
**Do not** place `ARCH-` files in `engine/` or `FUNC-` files in `orchestration/`. Prefix-directory binding (Section 3) is not advisory; it is structural law.

### 7.5 Lowercase Prefixed Files
**Do not** use lowercase for prefixed filenames. `ref-naming.md` is wrong; `REF-NAMING.md` is correct. Case signals that the file participates in the naming system.

### 7.6 Deleting State Files
**Do not** delete `DYN-` or `ARCH-` files during "cleanup." These are living infrastructure. Archive superseded `ARCH-` files; compact `DYN-` files. Deletion is destruction, not cleaning (INT-2210 lesson: "The janitor who tears down walls isn't cleaning -- he's demolishing").

### 7.7 Unprefixed Files in Prefixed Zones
**Do not** add unprefixed `.md` files to `engine/02-ENGINE/` or `canon/01-CANON/`. Every file in a canonical layer must participate in the prefix system so agents can route by pattern.

---

## 8. Validation

`scaffold_validate.sh` (DC-301) should enforce:
- No prefixed files outside their sanctioned directories
- No unprefixed `.md` files in canonical layers
- No new numbered-prefix directories without registry entry
- CANON- files follow the NNNNN-TITLE-tier pattern
- DYN- files exist only in mutable zones (engine, orchestration)

---

*This specification is the ground truth for file naming. When in doubt, consult this document. When this document is insufficient, escalate to Sovereign for a naming decision and update this spec.*
