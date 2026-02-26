# IMPLEMENTATION-BACKLOG.md
## Canon→Implementation Backlog
### Status: Tranche C (In Progress) | Last Updated: 2026-02-26

---

## READY FOR QUEUE

### Priority: Critical (Foundation)
- [ ] **IMP-2026-0017**: IIC Constellation Architecture — Six IIC constellation design
  - Owner: Ajna | Effort: L | Dependencies: None
  - Venue: repo (canonical documentation) → Linear (tracking)
  
- [ ] **IMP-2026-0018**: Acumen IIC Specification — Reconnaissance system + qualification metrics
  - Owner: Psyche | Effort: L | Dependencies: IMP-2026-0017
  - Venue: repo + Linear

### Priority: High (Infrastructure)
- [ ] **IMP-2026-0009**: Layer 0 Device-OS Mapping — Multi-ecosystem strategy
  - Owner: Psyche | Effort: M | Dependencies: None

- [ ] **IMP-2026-0010**: Layer 1 Identity Federation — Email/IIC design template
  - Owner: Psyche | Effort: M | Dependencies: IMP-2026-0009

- [ ] **IMP-2026-0013**: Layer 4 Application AI — Chain→AI mapping + configs
  - Owner: Psyche | Effort: L | Dependencies: IMP-2026-0010

### Priority: Medium (Operations)
- [ ] **IMP-2026-0001**: Seven Pulses Daily Tracking — Morning/Midday/Evening templates
  - Owner: Adjudicator | Effort: M | Dependencies: None

- [ ] **IMP-2026-0004**: Three-Rail System — Life/Development/Demonstration tracking
  - Owner: Psyche | Effort: M | Dependencies: IMP-2026-0001

- [ ] **IMP-2026-0026**: Tier 1-4 Qualification — Content qualification matrix
  - Owner: Psyche | Effort: M | Dependencies: IMP-2026-0018

### Priority: Standard (Production)
- [ ] **IMP-2026-0006**: Content Production Protocol — Modal-aligned strategy
  - Owner: Commander | Effort: L | Dependencies: IMP-2026-0004

- [ ] **IMP-2026-0007**: Production Rhythms — Cadence templates
  - Owner: Commander | Effort: M | Dependencies: IMP-2026-0006

---

## NOT YET READY (Blocked/Needs Design)

### Blocked: Seven-Layer Stack (Layers 5-7)
- [ ] **IMP-2026-0014**: Layer 5 Content Platforms — Needs Phase/Stage assessment
- [ ] **IMP-2026-0015**: Layer 6 Production Infrastructure — Needs tool inventory
- [ ] **IMP-2026-0016**: Layer 7 Meta-Intelligence — Needs Graphiti/Mem0 integration design

### Blocked: IIC Integration
- [ ] **IMP-2026-0019-0022**: Coherence/Mastery/Efficacy/Transcendence IICs — Blocked on Acumen IIC completion
- [ ] **IMP-2026-0023**: IIC Communication Protocol — Needs cross-IIC testing
- [ ] **IMP-2026-0024**: Synthesis Cycles — Needs operational validation

---

## DECISION ATOMS REQUIRED

### Architecture Decisions
1. **Sovereignty Tier for Syncrescendence Framework**: High (markdown/git) or Medium (tool-native + exports)?
   - Source: CANON-31130:900-1000
   - Status: **OPEN** — Recommend High for canonical docs

2. **IIC-to-Agent Mapping**: Map 5 personal IICs to constellation agents?
   - Source: CANON-31140
   - Status: **OPEN** — Recommend: Ajna→Coherence, Psyche→Efficacy, Commander→Efficacy+Coherence, Adjudicator→Mastery, Cartographer→Acumen

3. **Layer 7 Implementation**: Obsidian vs Notion vs custom for knowledge graph?
   - Source: CANON-31130:720-810
   - Status: **OPEN** — Recommend hybrid: Obsidian (local) + Qdrant (semantic)

---

## TRANCHE PROGRESS

| Tranche | Status | Files Processed | Entries Extracted |
|---------|--------|-----------------|---------------------|
| A (Spine) | Not started | — | — |
| B (Execution) | Not started | — | — |
| C (Canon) | **IN PROGRESS** | 3/7 partial | 28 entries |
| D (Tooling) | Not started | — | — |

### Tranche C Remaining
- CANON-31141-FIVE_ACCOUNT — IIC detailed spec
- CANON-30430-MEMORY_SYSTEMS — Memory architecture
- CANON-30420-MULTI_AGENT_ORCHESTRATION — Agent coordination
- CANON-30300-TECH_STACK — Tool inventory

---

## METRICS
- Total Backlog Items: 28
- Ready for Queue: 8
- Blocked: 8
- Needs Design: 12
