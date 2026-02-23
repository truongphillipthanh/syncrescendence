---
id: ref-research_pipeline
kind: reference
scope: engine
target: engine
---

# RESEARCH PIPELINE: Systematic Tool/Platform Investigation

**Version**: 1.0.0
**Generated**: 2026-01-30
**Stream**: D (AJNA9-RECAL)
**Purpose**: Repeatable methodology for investigating CLI tools and AI platforms

---

## Overview

Each new CLI/agent tool entering the Constellation has:
- Platform idiosyncrasies (behavior quirks)
- Terminology (their names for concepts)
- Community consensus (best practices)
- Integration points (with our architecture)

This pipeline provides a **repeatable five-phase process** for systematic investigation, synthesis, and operationalization.

**Proven at scale**: The Claude Code research corpus (160+ files, 223K words) was metabolized into 05-SIGMA (22 docs, 22.7K words) using this methodology, achieving 85%+ compression.

---

## Process

### Phase 1: Source Identification

**Goal**: Map the authoritative information landscape for the target tool.

| Source Type | Priority | Examples |
|---|---|---|
| Official documentation | P0 | Docs site, README, API reference |
| GitHub repository | P0 | Source code, issues, discussions, stars/forks trajectory |
| Community forums | P1 | Discord, Reddit, HN threads, X/Twitter |
| Early adopter testimonials | P1 | Blog posts, video walkthroughs, case studies |
| Comparative analyses | P2 | Benchmark reports, security audits, competitive reviews |
| Academic/research | P3 | Papers, whitepapers, technical reports |

**Output**: Source inventory with URLs, dates, and credibility assessment.

**Quality Gate**:
- [ ] Official docs consulted
- [ ] GitHub repo examined (if open source)
- [ ] At least 3 community sources identified
- [ ] Source freshness verified (< 30 days for fast-moving tools)

---

### Phase 2: Gathering

**Goal**: Download and archive all relevant information.

**Process**:
1. Download/archive authoritative sources to `agents/`/inbox
2. Collect testimonials with timestamps and attribution
3. Note version-specific information (pin version numbers)
4. Identify conflicting patterns across sources
5. Tag each source with the Five-Platform Characteristic Cognition framework:

| Platform | What to Preserve |
|---|---|
| Claude-sourced | System design, constraint patterns, safety analysis |
| ChatGPT-sourced | Concrete examples, immediate actionability |
| Gemini-sourced | Theoretical framing, integration patterns |
| Grok-sourced | Failure modes, anti-patterns, edge cases |
| Perplexity-sourced | Research grounding, authoritative citations |

**Output**: Raw source files in `agents/`/inbox with metadata headers.

**Quality Gate**:
- [ ] All P0 sources downloaded
- [ ] Version numbers pinned
- [ ] Conflicts between sources documented
- [ ] Source dates recorded

---

### Phase 3: Synthesis

**Goal**: Extract unique value and compress into SN-format documents.

**Process** (following proven ORACLE-CONTEXT methodology):
1. Read every source file completely
2. Extract unique value (expect 65-70% redundancy across sources)
3. Synthesize into compressed SN-format documents
4. Apply compression quality bar:

| Metric | Target |
|---|---|
| Word reduction | >= 85% (research corpus) or >= 35% (CANON) |
| Truncation markers | 0 |
| Synthesized sutras | 100% (crafted, not truncated) |
| Typed specs | 100% |

5. Organize output by the 05-SIGMA taxonomy:
   - `00-SYNTHESIS/` -- Canonical platform reference
   - `01-MECHANICS/` -- Deep-dive mechanisms
   - `02-PRACTICE/` -- Implementation patterns

**Output**: Synthesis documents ready for 05-SIGMA integration.

**Quality Gate**:
- [ ] All sources read completely
- [ ] Redundancy eliminated (target 65-70% overlap removal)
- [ ] SN format applied (sutra/gloss/spec)
- [ ] Compression target met

---

### Phase 4: Reconciliation

**Goal**: Map new tool's concepts to existing Syncrescendence terminology.

**Process**:
1. Compare tool's terminology against `02-ENGINE/REF-ROSETTA_STONE.md`
2. For each new concept, determine status:
   - ALIGNED: Matches existing term (adopt community language)
   - ADAPTED: Partial overlap (document both, note distinctions)
   - UNIQUE: New concept we lack (consider adoption)
   - IRRELEVANT: Does not apply to our use case
3. Identify conflicts with existing architecture
4. Propose adaptations or integrations
5. Update ROSETTA-STONE with new mappings

**Output**: Terminology mapping + ROSETTA-STONE delta.

**Quality Gate**:
- [ ] All new terms mapped
- [ ] Conflicts identified
- [ ] ROSETTA-STONE update drafted
- [ ] Constellation role assignment proposed (if applicable)

---

### Phase 5: Operationalization

**Goal**: Integrate findings into the operational Constellation.

**Process**:
1. Update platform avatar files (e.g., 02-ENGINE/AVATAR-CODEX.md, AVATAR-GEMINI-WEB.md, AVATAR-GEMINI-CLI.md, or create new)
2. Create/update skills if new capabilities warrant automation
3. Test integration with existing workflows
4. Document learnings in 05-SIGMA
5. Update README.md if Constellation roles change
6. Commit all artifacts with semantic prefix (`feat:`, `docs:`)

**Output**: Updated operational infrastructure.

**Quality Gate**:
- [ ] Platform config created/updated
- [ ] Skills added if needed
- [ ] Integration tested
- [ ] 05-SIGMA documents committed
- [ ] README.md updated if roles changed
- [ ] `make verify` passes

---

## Output File Conventions

| Output | Location | Naming |
|---|---|---|
| Raw research sources | `agents/`/inbox | `RESEARCH-[TOOL]-[DATE]-[source].md` |
| Synthesis documents | `05-SIGMA/synthesis/` | `SYNTHESIS-[tool]_[domain].md` |
| Mechanics documents | `05-SIGMA/mechanics/` | `MECH-[mechanism].md` |
| Practice documents | `05-SIGMA/practice/` | `PRAC-[pattern].md` |
| Platform avatar | `02-ENGINE/` | `AVATAR-[TOOL].md` |
| ROSETTA-STONE updates | `02-ENGINE/` | Append to `REF-ROSETTA_STONE.md` |

---

## Application: OpenClaw Research Scope

### Tool Profile

| Attribute | Value |
|---|---|
| Name | OpenClaw (nee Clawdbot/Moltbot) |
| GitHub | openclaw/openclaw |
| Stars | 114K+ (as of 2026-01-30) |
| Status | v2026.1.29 |
| Category | Model-agnostic persistent-memory AI agent |
| Companion | Lobster (workflow shell) |

### Core Research Questions

| # | Question | Phase | Priority |
|---|---|---|---|
| 1 | **Architecture**: How does OpenClaw compare to our Constellation? Replacement or complement? | Phase 3 | P0 |
| 2 | **Memory**: Persistent memory across sessions -- what substrate? How does it work? | Phase 2-3 | P0 |
| 3 | **Integrations**: 50+ channels (WhatsApp, Slack, Discord, iMessage) -- how map to our roles? | Phase 4 | P1 |
| 4 | **Skills**: Does it use Claude Code skills? Its own format? Both? | Phase 3 | P1 |
| 5 | **Security**: What are actual risks? (Cisco/Checkmarx reports) | Phase 2 | P0 |
| 6 | **Model routing**: Works with Claude, GPT, Gemini, KIMI -- how does routing work? | Phase 3 | P1 |
| 7 | **Lobster**: Typed, local-first macro engine -- comparable to our Makefile + skills? | Phase 3 | P2 |

### Sources to Investigate

| Source | Type | Priority |
|---|---|---|
| GitHub: openclaw/openclaw | Official | P0 |
| GitHub: openclaw/lobster | Official | P1 |
| Docs: openclaw.ai | Official | P0 |
| Discord (8,900+ members) | Community | P1 |
| Cisco blog analysis | Security | P0 |
| Checkmarx report | Security | P0 |
| X/Twitter threads | Community | P2 |
| HN discussions | Community | P2 |

### Integration Hypothesis

OpenClaw may serve as the **local orchestration layer** complementing cloud-based Constellation:

```
Cloud Layer (strategic):
  Claude Web (INTERPRETER) + ChatGPT (COMPILER) + Gemini Web (DIGESTOR) + Grok (RED TEAM)

Local Layer (execution):
  Claude Code (EXECUTOR) + OpenClaw (local memory + messaging channels)

Enterprise Layer (embedded tools):
  Cowork (MCP Apps: Slack, Asana, Figma, Box, Canva embedded in-chat)
```

This hypothesis needs validation through the pipeline. Key test: Does OpenClaw's persistent memory + multi-channel architecture solve problems our current Constellation leaves unaddressed (particularly the messaging/notification gap)?

---

## Research Template

Copy and fill for each new tool investigation:

```markdown
# RESEARCH: [Tool Name]
## Pipeline Application

**Date Initiated**: YYYY-MM-DD
**Target Tool**: [Name] v[Version]
**Researcher**: [Platform/Agent]

### Phase 1: Source Inventory
| Source | URL | Date | Credibility |
|---|---|---|---|

### Phase 2: Gathering Status
- [ ] Official docs
- [ ] GitHub repo
- [ ] Community (3+ sources)
- [ ] Version pinned: v[X.Y.Z]

### Phase 3: Synthesis
- Compression ratio: [X]%
- Unique insights: [N]
- Outputs: [list files]

### Phase 4: Reconciliation
| Their Term | Our Term | Status |
|---|---|---|

### Phase 5: Operationalization
- [ ] Platform config: [file]
- [ ] Skills: [list]
- [ ] SIGMA7 docs: [list]
- [ ] README.md updated: [yes/no]
- [ ] make verify: [pass/fail]

### Decision
**Integrate?**: [Yes/No/Defer]
**Role**: [Proposed Constellation role, if any]
**Rationale**: [Brief]
```

---

## Version History

**v1.0.0** (2026-01-30): Genesis establishment
- Five-phase pipeline formalized
- Quality gates defined per phase
- OpenClaw research scope specified as first application
- Reusable template included
- Derived from proven ORACLE-CONTEXT methodology
