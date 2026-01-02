# ORACLE9 CONTEXT
## Repository Portability & Hygiene Phase
**Version**: 3.0.0
**Date**: 2026-01-02
**Status**: Constitutional — Include with ALL Oracle9 directives

---

## PURPOSE

> "Directives must be comprehensive—Principal is bottleneck. Have Claudes stage, evaluate against 18 lenses, and execute in one cycle. Minimize relay. Frame holistically, not incrementally."
> — Principal, Oracle9

This document captures Oracle9 mission, decisions, current state, and execution context. **INCLUDE WITH EVERY DIRECTIVE.**

---

## SECTION 1: POSITION IN THE PROGRESSION

### Metascopic (Civilizational)
Syncrescendence is **civilizational sensing infrastructure**—the agentified spiritual successor to DEVONThink/Zotero/Notion, unifying:
- Knowledge synthesis (CANON)
- Operational intelligence (functions, prompts)
- External sensing (SOURCES)
- Task orchestration (project management)
- State persistence (memory across sessions/agents)

The trajectory points toward **structured data formats** (CSV, SQLite) as substrate, with markdown as human-readable projection.

### Macroscopic (Syncrescendence)
| Layer | Status |
|-------|--------|
| CANON | 71 files, FLAT, semantic superlativity achieved ✓ |
| OPERATIONAL | Functions + prompts restructured ✓ |
| SOURCES | 184 content files triaged, 4 processed ✓ |
| Orchestration | State files exist, needs hygiene ✗ |

### Mesoscopic (Oracle Arc)
| Oracle | Phase | Status |
|--------|-------|--------|
| 8 | Annealment | COMPLETE |
| **9** | **Ingestion** | **Pattern proven, hygiene needed** |
| 10 | IIC Configuration | BLOCKED on clean handoff |
| 11+ | Tooling, Automation, Ontology | Future |

### Microscopic (Current Phase)
**DIRECTIVE-034**: Repository portability + hygiene
- Flatten SOURCES/raw (currently 5+ levels deep)
- Sequentialize Oracle contexts
- Triage orchestration/scaffolding
- Enable Project Files upload capability

---

## SECTION 2: CURRENT STATE

### SOURCES/ Structure Issues
```
SOURCES/raw/                    (PROBLEMATIC - nested 5+ levels)
├── 0/                          (categorization layer)
│   ├── creators/
│   ├── daily/
│   ├── frequent/
│   ├── interviewers/
│   │   ├── ai/
│   │   ├── culture/
│   │   ├── holistic/
│   │   ├── philosophy/
│   │   └── science/
│   └── lecture/
├── AGI/
├── Anthropology/
├── Biology/
│   ├── Evolution/
│   ├── Longevity/
│   └── Sustainability/
├── Physical AI/
├── new perspectives/
├── snapshot/
└── transcripts/
```

**Problem**: Deep nesting violates flat hierarchy principle, prevents easy upload to Project Files.

**Solution**: Flatten all 184 content files to SOURCES/raw/ root with standardized naming.

### orchestration/state/ Issues
```
ORACLE_CONTEXT.md        (generic, outdated)
ORACLE_CONTEXT_v2.md     (Oracle7-8)
ORACLE8_STATUS_REPORT.md (point-in-time)
ORACLE9_CONTEXT.md       (v1)
ORACLE9_CONTEXT_v2.md    (v2)
THREAD_CONTEXT.md        (unclear provenance)
```

**Problem**: No sequentialization, unclear versioning, confusing for handoff.

**Solution**: Rename to `ORACLE{NN}_CONTEXT_v{M}.md` pattern.

### orchestration/scaffolding/ Status
17 files requiring triage:
```
ALPHA_ARCHAEOLOGY_REPORT.md     → ARCHIVE (Oracle5 work)
ALPHA_OPERATIONAL_COHERENCE.md  → ARCHIVE
ALPHA_REPOSITORY_AUDIT.md       → ARCHIVE
ALPHA_SYNTHESIS.md              → ARCHIVE
ALPHA_TENSION_MAP.md            → ARCHIVE
BETA_METADATA_SCHEMA.md         → evaluate (may have value)
BETA_NOMENCLATURE_SPEC.md       → evaluate (may have value)
BETA_VALIDATION_REPORT.md       → ARCHIVE
CONTENT_ALIGNMENT_AUDIT.md      → ARCHIVE
COSMOS_ALIGNMENT_REPORT.md      → ARCHIVE
CRYSTALLINE_CHARACTERISTICS.md  → evaluate (quality spec)
DEFRAG_EXECUTION_LOG.md         → ARCHIVE
OPERATIONAL_DOCUMENTS_TODO.md   → DELETE (superseded)
POST_FORGE_TREE.md              → DELETE (superseded by current tree)
RECONNAISSANCE_REPORT.md        → ARCHIVE
REVISION_PRIORITIES.md          → DELETE (superseded)
THREAD_TRAJECTORY.md            → ARCHIVE
```

---

## SECTION 3: WHAT 033A/B ACCOMPLISHED

### Triage Layer (033A)
- **sources.csv**: 184 content files with eight-dimensional classification
- **Tier distribution**: 47 paradigm, 44 strategic, 83 tactical, 10 noise
- **Alias symlinks**: 91 created (paradigm + strategic tiers)
- **Python triage script**: Reusable for future batches

### Processing Layer (033B)
- **4 paradigm sources** fully processed:
  - Richard Sutton interview
  - Andrej Karpathy interview
  - Demis Hassabis interview
  - Karpathy X post on Sutton
- **2 CANON documents** enriched:
  - CANON-00004-EVOLUTION (External Source Validations section)
  - CANON-30400-AGENTIC_ARCHITECTURE (Practitioner Validations section)
- **PROCESSING_PATTERN.md**: Documents repeatable methodology

### What Remains
- 43 paradigm sources unprocessed
- 44 strategic sources unprocessed
- SOURCES/raw not flat
- Oracle contexts not sequentialized
- Scaffolding not triaged

---

## SECTION 4: THE 18 EVALUATIVE LENSES

| # | Lens | Question |
|---|------|----------|
| 1 | Syncrescendent Route | Continuous, cyclic, recursive? |
| 2 | Bitter Lesson | General-method, large-context-ready? |
| 3 | Antifragile | Gains from disorder? |
| 4 | Meet the Moment | Timely + future-positioned? |
| 5 | Steelman & Redteam | Survives strongest attack? |
| 6 | Personal Idiosyncrasies | Honors macroscopic-holistic cognition? |
| 7 | Potency w/o Resolution Loss | Maximum compression, full fidelity? |
| 8 | Elegance + Dev Happiness | Minimal surface, predictable patterns? |
| 9 | Agentify + Human-Navigable | 2 decisions to any file? |
| 10 | First Principles | Does it need to exist? |
| 11 | Systems Thinking | Parts relate to whole? |
| 12 | Industrial Engineering | Throughput optimization? |
| 13 | Complexity Theory | Essential vs accidental? |
| 14 | Permaculture | Self-sustaining? |
| 15 | Design Thinking | Human-centered? |
| 16 | Agile | Shippable increments? |
| 17 | Lean | Waste elimination? |
| 18 | Six Sigma | Defect reduction? |

**Threshold**: 12/18 must pass. All directive decisions MUST be evaluated.

---

## SECTION 5: NAMING CONVENTIONS

### Source Files (Target State)
```
SOURCE-{YYYYMMDD}-{platform}-{format}-{creator}-{title_slug}.{ext}
```

### Oracle Contexts
```
ORACLE{NN}_CONTEXT_v{M}.md
```
Example: `ORACLE09_CONTEXT_v3.md`

### Directives
```
DIRECTIVE-{NNN}{A|B}_{BRIEF_NAME}.md
```

### Execution Logs
```
EXECUTION_LOG-{YYYY-MM-DD}-{NNN}{A|B}.md
```

---

## SECTION 6: CONSTITUTIONAL RULES

1. **Metabolism applies to CONTENT, not INFRASTRUCTURE**
2. **Repository is Foyer** — all context accessible to any agent
3. **Globe before trees** — holistic framing before tactical work
4. **Verify, don't trust** — examine filesystem, not reports
5. **Principal is bottleneck** — comprehensive directives, minimize relay
6. **18-lens mandatory** — every decision evaluated against full framework
7. **Flat hierarchy** — SOURCES/raw should be flat like CANON/

---

## SECTION 7: SUCCESS CRITERIA FOR DIRECTIVE-034

- [ ] SOURCES/raw flattened (184 files at root level)
- [ ] Source filenames standardized
- [ ] sources.csv updated with new paths
- [ ] Symlinks rebuilt
- [ ] Oracle contexts sequentialized
- [ ] Scaffolding triaged (ARCHIVE or DELETE)
- [ ] Repository uploadable to Project Files
- [ ] Clean Oracle10 handoff prepared

---

## VERSION HISTORY

- v1.0.0 (2026-01-01): Initial creation from Oracle9 initialization
- v2.0.0 (2026-01-01): Post-032A/B — execution focus, structured index
- v3.0.0 (2026-01-02): Post-033A/B — hygiene focus, portability preparation

---

**THIS DOCUMENT MUST ACCOMPANY EVERY ORACLE9 DIRECTIVE.**
