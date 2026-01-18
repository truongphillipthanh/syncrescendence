# Concentric Rings v2
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: Revised architectural model based on repository artifacts and research

---

## Overview

The concentric rings model describes information flow from external reality through progressive transformation into canonical knowledge. Each ring has defined membranes, artifacts, and integration points.

---

## Ring Definitions

### Ring 0: External Reality
**What Lives Here**: The world outside the system
- YouTube videos, podcasts, articles
- X/Twitter discourse
- ArXiv papers
- Real-time events
- Physical reality (health metrics, environment)

**Membrane → Ring 1**: Signal Detection
- YouTube subscription notifications
- RSS feed updates
- Manual saves (Watch Later, bookmarks)
- Health app integrations
- Serendipitous encounters

**Principal Position**: Occasionally present (browsing, saving)

---

### Ring 1: Ingest Layer
**What Lives Here**: Raw captured signals before qualification
- `04-SOURCES/raw/` — Unprocessed transcripts, downloads
- Watch Later queue
- Saved bookmarks
- Email forwards to ingest

**Artifacts Produced**:
- Raw transcript files (txt, md)
- Metadata stubs
- Filename standardization

**Processing Agent**: Gemini (video), manual capture, automation triggers

**Membrane → Ring 2**: Triage
- Signal tier assignment (paradigm/strategic/tactical/noise)
- Value modality assessment (dialogue/visual/audio primary)
- Routing decision

**Principal Position**: Minimal (save action triggers entry; triage may require judgment)

---

### Ring 2: Queue Layer
**What Lives Here**: Triaged items awaiting processing
- `03-QUEUE/` — Categorized by modal stage
- sources.csv entries with status=triaged
- Signal tier determines processing priority

**Artifacts Produced**:
- Triage reports
- Queue position assignments
- Priority bands

**Processing Agent**: System 4 (Triage & Qualification)

**Membrane → Ring 3**: Processing Selection
- Function routing (transcribe_interview, readize, etc.)
- Resource allocation
- Batch grouping

**Principal Position**: Optional review of triage decisions

---

### Ring 3: Processing Layer
**What Lives Here**: Active transformation of sources
- `04-SOURCES/processed/` — Processed source files
- Gemini AI Studio batch operations
- Claude Code execution sessions

**Artifacts Produced**:
- Processed SOURCE-YYYYMMDD-*.md files
- Complete frontmatter
- Key insights extraction
- Synopsis generation

**Processing Agent**: Gemini (transcription), Claude Code (integration)

**Membrane → Ring 4**: Integration Qualification
- Acceptance criteria check
- Canon target identification
- Citation preparation

**Principal Position**: Minimal (verification of paradigm sources)

---

### Ring 4: Integration Layer
**What Lives Here**: Synthesis into canonical knowledge
- `01-CANON/` modifications
- Canon version updates
- Cross-reference additions

**Artifacts Produced**:
- Canon updates with source citations
- Execution logs
- Integration verification

**Processing Agent**: Claude Code (executor), ChatGPT (auditor)

**Membrane → Ring 5**: Canonization
- 18 Lenses evaluation
- Principal approval for Canon changes
- Protected zone governance

**Principal Position**: Required (approval for Canon modifications)

---

### Ring 5: Canon Layer
**What Lives Here**: Verified, crystallized knowledge
- `01-CANON/` — Protected canonical documents
- Version-controlled truth
- Chain-organized wisdom

**Artifacts Produced**:
- Stable knowledge artifacts
- Referenced by all other layers
- Ground truth for system

**Processing Agent**: Commit + verification only

**Membrane → Ring 6**: Operational Activation
- Knowledge applied to decision-making
- Strategy updates
- Protocol refinements

**Principal Position**: Governance (constitutional stewardship)

---

### Ring 6: Operational Layer
**What Lives Here**: Active application of knowledge
- `02-OPERATIONAL/` — Functions, prompts, protocols
- `00-ORCHESTRATION/state/` — Living infrastructure
- Active decision-making

**Artifacts Produced**:
- Execution logs
- State updates
- Directive completions

**Processing Agent**: All platforms per routing

**Membrane → Ring 7**: Output & Synthesis
- Publication readiness
- External communication
- Field node interface

**Principal Position**: Active direction (directive issuance)

---

### Ring 7: Output Layer
**What Lives Here**: External-facing synthesis
- Publication drafts
- Research outputs
- Gaian Field Node interface (future)

**Artifacts Produced**:
- External communications
- Synthesized briefs
- Public artifacts

**Processing Agent**: Principal-directed

**Membrane → Reality**: Publication
- Quality gate
- Principal approval
- External distribution

**Principal Position**: Final approval (publication authority)

---

## Membrane Specifications

### What Crosses Each Membrane

| Membrane | Inward Flow | Outward Flow | Crossing Criteria |
|----------|-------------|--------------|-------------------|
| 0→1 | Detected signals | Nothing (one-way) | Signal detected by monitoring |
| 1→2 | Raw sources | Rejected noise | Triage assignment |
| 2→3 | Prioritized queue items | Deprioritized items | Processing slot available |
| 3→4 | Processed sources | Failed processing | Acceptance criteria met |
| 4→5 | Integration candidates | Rejected integrations | 18 Lenses evaluation |
| 5→6 | Canonical knowledge | Nothing (reference only) | Operational need |
| 6→7 | Operational outputs | Revisions | Publication readiness |
| 7→0 | Published artifacts | Nothing (one-way) | Principal approval |

### What Cannot Cross

| Membrane | Blocked | Reason |
|----------|---------|--------|
| 5 (Canon) | Unverified claims | Canon requires verification |
| 5 (Canon) | Temporal content | Canon must be time-stable |
| 5 (Canon) | Execution without approval | Protected zone |
| 6 (Ops) | Direct external commands | Only via Principal |
| 7 (Output) | Unreviewed content | Publication authority required |

---

## Gating Criteria by Membrane

### 0→1 (Signal Detection)
```yaml
criteria:
  - Source matches subscription/monitoring list
  - OR Manual save action by Principal
  - OR Automation trigger fires
```

### 1→2 (Triage)
```yaml
criteria:
  - Signal tier assigned (paradigm/strategic/tactical/noise)
  - Value modality assessed
  - sources.csv entry created
  - If noise: archive metadata only
```

### 2→3 (Processing Selection)
```yaml
criteria:
  - Processing slot available
  - Priority band allows processing
  - Function selected from routing
```

### 3→4 (Integration Qualification)
```yaml
criteria:
  - Processed file complete
  - Frontmatter valid (all required fields)
  - Synopsis present (2-3 sentences)
  - Key insights extracted (5-10 points)
  - Canon target identified
```

### 4→5 (Canonization)
```yaml
criteria:
  - Integration adds unique value (not redundant)
  - Source citation included
  - Version history updated if substantive
  - 18 Lenses evaluation passed (≥12/18)
  - Principal approval if paradigm-level
```

### 5→6 (Operational Activation)
```yaml
criteria:
  - Operational need identified
  - Knowledge reference sufficient (not copied)
  - No modification of Canon (read-only)
```

### 6→7 (Output Synthesis)
```yaml
criteria:
  - Synthesis complete
  - Quality gate passed
  - Format appropriate for audience
```

### 7→0 (Publication)
```yaml
criteria:
  - Principal approval obtained
  - External-ready format
  - No sensitive information exposed
```

---

## Principal Position Summary

| Ring | Principal Role | Frequency |
|------|----------------|-----------|
| 0 (External) | Signal origination | Occasional |
| 1 (Ingest) | Save action | Occasional |
| 2 (Queue) | Triage review | Optional |
| 3 (Processing) | Paradigm verification | Rare |
| 4 (Integration) | Integration review | Optional |
| 5 (Canon) | Approval authority | Required for changes |
| 6 (Operational) | Directive issuance | Active |
| 7 (Output) | Publication authority | Required |

**Design Principle**: Principal involvement increases at membrane crossings, not within rings. Autonomous operation within rings; governance at transitions.

---

## Ring Artifacts Summary

| Ring | Primary Location | Artifact Type |
|------|------------------|---------------|
| 1 | 04-SOURCES/raw/ | Raw transcripts |
| 2 | 03-QUEUE/, sources.csv | Queue entries |
| 3 | 04-SOURCES/processed/ | Processed sources |
| 4 | 00-ORCHESTRATION/blackboard/ | Integration packets |
| 5 | 01-CANON/ | Canonical documents |
| 6 | 02-OPERATIONAL/, 00-ORCHESTRATION/state/ | Protocols, state |
| 7 | (future publication layer) | External outputs |
