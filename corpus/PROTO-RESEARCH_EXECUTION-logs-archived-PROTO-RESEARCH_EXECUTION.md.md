# PROTO — Research Execution Protocol

**Version**: 1.0.0
**Created**: 2026-02-06
**Authority**: Ajna (Opus 4.5) — formalizing from REF-RESEARCH_PIPELINE + REF-RESEARCH_METHODOLOGY_SYNTHESIS
**Invocation**: When any Constellation member needs to investigate a new tool/platform

---

## Overview

This protocol reconciles two prior documents:
- **REF-RESEARCH_PIPELINE.md** (5-phase operational) — the "what to do"
- **REF-RESEARCH_METHODOLOGY_SYNTHESIS.md** (7-phase academic) — the "how it was proven"

The result is a single actionable protocol with clear phase gates.

---

## The Five Phases

### Phase 1: SOURCE IDENTIFICATION
**Goal**: Map the authoritative information landscape.
**Time**: 1-2 hours

| Source Type | Priority | Examples |
|---|---|---|
| Official documentation | P0 | Docs site, README, API reference |
| GitHub repository | P0 | Source code, issues, discussions |
| Community forums | P1 | Discord, Reddit, HN, X/Twitter |
| Practitioner testimonials | P1 | Blog posts, video walkthroughs |
| Comparative analyses | P2 | Benchmarks, security audits, reviews |

**Output**: Source inventory file at `sources/research/{tool}/SOURCE_INVENTORY.md`

**Gate**:
- [ ] Official docs consulted
- [ ] GitHub repo examined
- [ ] ≥3 community sources identified
- [ ] Source freshness verified (<30 days for fast-moving tools)

---

### Phase 2: GATHERING
**Goal**: Download, archive, and tag all relevant information.
**Time**: 2-4 hours

**Process**:
1. Archive sources to `sources/research/{tool}/`
2. Tag each source with platform cognition characteristic:
   - Claude-sourced: system design, constraint patterns
   - ChatGPT-sourced: concrete examples, actionability
   - Gemini-sourced: theoretical framing, integration patterns
   - Grok-sourced: failure modes, anti-patterns, edge cases
   - Perplexity-sourced: research grounding, citations
3. Pin version numbers
4. Document conflicts between sources

**Output**: Raw source files with metadata headers

**Gate**:
- [ ] All P0 sources downloaded
- [ ] Version numbers pinned
- [ ] Conflicts documented
- [ ] Source dates recorded

---

### Phase 3: SYNTHESIS
**Goal**: Extract unique value, compress into operational documents.
**Time**: 3-6 hours

**Process** (Preservative Coalescence):
1. Read every source file completely
2. Extract unique value (expect 65-70% redundancy)
3. Apply compression: ≥85% word reduction (research) or ≥35% (CANON)
4. Preserve productive tensions — do NOT average away disagreements
5. Structure output with verification status per claim:
   - **CONFIRMED**: Multiple authoritative sources agree
   - **DISPUTED**: Sources disagree; both positions preserved
   - **UNVERIFIED**: Community wisdom only

**Synthesis Template**:
```markdown
# SYNTHESIS: {Tool Name}
## Phase 3 Output

### Architecture & Core Concepts
[compressed findings]

### Capabilities Matrix
| Capability | Status | Confidence | Source |
|---|---|---|---|

### Integration Points (with Syncrescendence)
[how it maps to our architecture]

### Known Limitations
[what it can't do]

### Productive Tensions
[unresolved disagreements worth preserving]
```

**Output**: `sources/research/{tool}/SYNTHESIS-{tool}.md`

**Gate**:
- [ ] All sources read completely
- [ ] Redundancy eliminated (65-70%)
- [ ] Verification status labeled
- [ ] Tensions preserved (not resolved)

---

### Phase 4: RECONCILIATION
**Goal**: Map tool concepts to Syncrescendence terminology.
**Time**: 1-2 hours

**Process**:
1. Compare tool terminology against `REF-ROSETTA_STONE.md`
2. Classify each new concept:
   - **ALIGNED**: Matches existing term (adopt community language)
   - **ADAPTED**: Partial overlap (document both)
   - **UNIQUE**: New concept we lack (consider adoption)
   - **IRRELEVANT**: Does not apply
3. Identify conflicts with existing architecture
4. Draft ROSETTA-STONE delta

**Output**: Terminology mapping + Rosetta delta

**Gate**:
- [ ] All new terms mapped
- [ ] Conflicts identified
- [ ] ROSETTA-STONE update drafted
- [ ] Constellation role confirmed/proposed

---

### Phase 5: OPERATIONALIZATION
**Goal**: Integrate findings into the operational Constellation.
**Time**: 2-4 hours

**Process**:
1. Update/create avatar config (`engine/AVATAR-{TOOL}.md`)
2. Create/update initialization files (root-level stubs if needed)
3. Test integration with existing workflows
4. Commit all artifacts with semantic prefix
5. Update COCKPIT.md if roles change

**Output**: Updated operational infrastructure

**Gate**:
- [ ] Avatar config created/updated
- [ ] Integration tested
- [ ] Artifacts committed
- [ ] COCKPIT.md updated if needed

---

## Medley Specialization (Multi-Platform Research)

When distributing research across the Constellation:

| Platform | Specialized Role | Prompt Style |
|---|---|---|
| Grok (Oracle) | Community discourse mining | "Search X for practitioner reports..." |
| Perplexity (Augur) | Citation triangulation | "Find and cite authoritative sources..." |
| ChatGPT (Vanguard) | Official doc validation | "Validate claims against official docs..." |
| Gemini (Diviner/Cartographer) | Spec extraction + long context | "Extract technical specifications..." |
| Claude (Vizier/Ajna) | Tension-preserving synthesis | "Integrate using preservative coalescence..." |

---

## Output Conventions

| Output | Location | Naming |
|---|---|---|
| Source inventory | `sources/research/{tool}/` | `SOURCE_INVENTORY.md` |
| Raw sources | `sources/research/{tool}/` | `{platform}-{tool}.md` |
| Synthesis | `sources/research/{tool}/` | `SYNTHESIS-{tool}.md` |
| Rosetta delta | `engine/` | Append to `REF-ROSETTA_STONE.md` |
| Avatar config | `engine/` | `AVATAR-{TOOL}.md` |

---

## Version History

**v1.0.0** (2026-02-06): Genesis — reconciled from Pipeline + Methodology
