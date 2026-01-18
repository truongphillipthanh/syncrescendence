# Concentric Rings v3
**Generated**: 2026-01-17T05:00:00Z
**Purpose**: Dual ring-system with crashout mechanics and membrane specifications

---

## Overview

Syncrescendence operates through **two interlocking ring-systems**:

**A) Interface/Orchestration Rings** — How platforms coordinate (your pain lives here)
**B) Repository/Metabolism Rings** — How knowledge flows (your progress lives here)

Most frustration occurs when Ring A is forced to do Ring B's job.

```
┌─────────────────────────────────────────────────────────────────┐
│                    RING SYSTEM A (Interface)                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                                                          │  │
│  │         A0: Principal Cockpit (Concierge)                │  │
│  │     ┌──────────────────────────────────────────┐        │  │
│  │     │                                          │        │  │
│  │     │     A1: Chorus Dispatch                  │        │  │
│  │     │ ┌────────────────────────────────────┐  │        │  │
│  │     │ │                                    │  │        │  │
│  │     │ │   A2: Execution Surfaces           │  │        │  │
│  │     │ │ ┌──────────────────────────────┐  │  │        │  │
│  │     │ │ │                              │  │  │        │  │
│  │     │ │ │ A3: Sensing/Ingress          │  │  │        │  │
│  │     │ │ │ ┌────────────────────────┐  │  │  │        │  │
│  │     │ │ │ │ A4: External Organs    │  │  │  │        │  │
│  │     │ │ │ └────────────────────────┘  │  │  │        │  │
│  │     │ │ └──────────────────────────────┘  │  │        │  │
│  │     │ └────────────────────────────────────┘  │        │  │
│  │     └──────────────────────────────────────────┘        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│              RING SYSTEM B (Metabolism) nested inside           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Ring System A: Interface/Orchestration

### Ring A0: Principal Cockpit (Concierge)

**What Lives Here**: The single surface Principal interacts with "increasingly exclusively"

**Teleology**: NOT "be smart." Instead:
- Maintain holistic visibility
- Enforce Definition of Done
- Build steelman prompts for chorus
- Culminate every exchange into durable artifacts

**Platforms**: Claude Web App (primary), ChatGPT Web App (secondary)

**Crashout Mechanics**:
| Failure Mode | Detection | Recovery |
|--------------|-----------|----------|
| Memory drift from repo | Model claims contradict repo | Verify against filesystem, trust repo |
| Context loss on export | Artifact doesn't transfer cleanly | Manual extraction + reformation |
| Session fragmentation | Conversation hits limit | Create continuation packet, start new |

**If A0 fails to culminate into artifacts, it becomes a memory sink.**

---

### Ring A1: Chorus Dispatch

**What Lives Here**: Selective multi-platform queries when stakes justify cost

**Teleology**: NOT "use everyone always." Instead:
- Dispatch only when truth contested, stakes high, or modalities diverge
- Reconcile contradictions via structured protocol
- Return unified answer, not debate

**Platforms**: Claude + ChatGPT + Gemini (selective)

**Crashout Mechanics**:
| Failure Mode | Detection | Recovery |
|--------------|-----------|----------|
| Analysis paralysis | Same query 3+ times, no decision | Set deadline, Principal decides |
| Regression to mean | Synthesis worse than individuals | Preserve minority positions |
| Coordination tax | More orchestrating than thinking | Reduce chorus frequency |

**Chorus without reconciliation protocol = coordination tax and analysis paralysis.**

---

### Ring A2: Execution Surfaces

**What Lives Here**: Where reality gets touched

**Teleology**: NOT thinking. Instead:
- Change the world while leaving receipts
- Execute plans, not generate them
- Log every action to event stream

**Platforms**: Claude Code CLI (primary), Codex CLI (GitHub-specific)

**Crashout Mechanics**:
| Failure Mode | Detection | Recovery |
|--------------|-----------|----------|
| Context overflow | Auto-compact triggers | /compact or new session with context |
| Tool rejection | Permission denied | Check command, adjust approach |
| Session loss | Unexpected termination | Read events.jsonl, reconstruct |

**Execution surfaces must leave receipts or become black boxes.**

---

### Ring A3: Sensing/Ingress Surfaces

**What Lives Here**: Feed evidence into the spine, not opinions into chat

**Teleology**: NOT analysis. Instead:
- Gather evidence
- Ground claims in sources
- Produce Evidence Packets with citations

**Platforms**:
- Gemini (corpus-scale + video)
- Perplexity (fast cited recon)
- Grok (real-time temperature)
- NotebookLM (grounded RAG)

**Crashout Mechanics**:
| Failure Mode | Detection | Recovery |
|--------------|-----------|----------|
| Hallucination | Claim without citation | Reject, request grounded version |
| Data leakage | Personal data in context | Anonymize or isolate context |
| Stale information | Outdated facts | Verify recency, refresh |

---

### Ring A4: External Organs

**What Lives Here**: Power tools with ground-truth ambiguity

**Teleology**: NOT authoritative. Instead:
- Ingestion staging area
- Drafting surface
- Retrieval accelerator

**Platforms**: Google Docs, Notion, NotebookLM notebooks

**Crashout Mechanics**:
| Failure Mode | Detection | Recovery |
|--------------|-----------|----------|
| Ground truth confusion | "Is repo or Docs authoritative?" | Repo is always authoritative |
| Sync drift | Doc version differs from repo | Repo wins, update doc |
| Tool sprawl | Too many external surfaces | Consolidate to essential |

**Repository must remain constitutional ground truth; everything else is cache.**

---

## Ring System B: Repository/Metabolism

Nested inside Ring A2 (Execution Surfaces), this is how knowledge flows through the repository.

### Ring B0: External Reality

**What Lives Here**: The world outside the system
- YouTube videos, podcasts, articles
- X/Twitter discourse
- ArXiv papers
- Real-time events

**Membrane → B1**: Signal Detection
- Subscription notifications
- Manual saves (Watch Later, bookmarks)
- Serendipitous encounters

---

### Ring B1: Ingest Layer

**What Lives Here**: Raw captured signals before qualification
- `04-SOURCES/raw/`
- Watch Later queue
- Saved bookmarks

**Artifacts**: Raw transcripts, metadata stubs

**Membrane → B2**: Triage
- Signal tier assignment (paradigm/strategic/tactical/noise)
- Value modality assessment

---

### Ring B2: Queue Layer

**What Lives Here**: Triaged items awaiting processing
- `03-QUEUE/`
- `sources.csv` entries with status=triaged

**Artifacts**: Triage reports, priority assignments

**Membrane → B3**: Processing Selection
- Function routing
- Batch grouping

---

### Ring B3: Processing Layer

**What Lives Here**: Active transformation
- `04-SOURCES/processed/`
- AI Studio batch operations
- Claude Code sessions

**Artifacts**: Processed SOURCE files, frontmatter, key insights

**Membrane → B4**: Integration Qualification
- Acceptance criteria check
- Canon target identification

---

### Ring B4: Integration Layer

**What Lives Here**: Synthesis into canonical knowledge
- `01-CANON/` modifications
- Cross-reference additions

**Artifacts**: Canon updates with citations

**Membrane → B5**: Canonization
- 18 Lenses evaluation
- Principal approval for Canon changes

---

### Ring B5: Canon Layer (PROTECTED)

**What Lives Here**: Verified, crystallized knowledge
- `01-CANON/`
- Version-controlled truth

**Artifacts**: Stable knowledge artifacts

**Membrane → B6**: Operational Activation
- Knowledge applied to decisions

---

### Ring B6: Operational Layer

**What Lives Here**: Active application
- `02-OPERATIONAL/`
- `00-ORCHESTRATION/state/`

**Artifacts**: Execution logs, state updates

**Membrane → B7**: Output Synthesis
- Publication readiness

---

### Ring B7: Output Layer

**What Lives Here**: External-facing synthesis
- Publication drafts
- Research outputs
- Future: Gaian Field Node

---

## Crashout Mechanics: The Failure Chain

The "crashout" you experienced follows this specific failure pattern:

```
┌─────────────────────────────────────────────────────────────────┐
│                    CRASHOUT FAILURE CHAIN                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   1. Conversational surface becomes implicit database           │
│      (state exists "somewhere in chat")                         │
│                         │                                       │
│                         ▼                                       │
│   2. Context discontinuity                                      │
│      (memory doesn't load, UI glitch, thread inaccessible)      │
│                         │                                       │
│                         ▼                                       │
│   3. Assistant responds as if state still shared                │
│      (produces instructions presuming invisible context)        │
│                         │                                       │
│                         ▼                                       │
│   4. High-effort retransmission falls on Principal              │
│      (must re-explain while managing absurdity)                 │
│                         │                                       │
│                         ▼                                       │
│   5. Emotional overload / impatience spike                      │
│      (cost of being precise becomes unbearable)                 │
│                         │                                       │
│                         ▼                                       │
│   6. System appears hostile / technically unintelligible        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Prevention Architecture

| Chain Point | Prevention Mechanism |
|-------------|---------------------|
| 1 | Never let chat be only storage → forced externalization |
| 2 | Continuation packets survive thread deletion |
| 3 | Session lifecycle requires grounding in repo before output |
| 4 | Minimal viable context in repo enables quick reconstruction |
| 5 | Recovery protocol prevents spiral into frustration |
| 6 | Operator translation layer reduces technical unintelligibility |

---

## Membrane Specifications

### Ring A Membranes (Interface)

| Crossing | Inward | Outward | Gate |
|----------|--------|---------|------|
| A4→A3 | Raw inputs | Nothing | Detection |
| A3→A2 | Evidence | Rejected noise | Grounding check |
| A2→A1 | Execution requests | Completed results | Task completeness |
| A1→A0 | Reconciled answers | Chorus queries | Reconciliation |
| A0→Principal | Visibility + artifacts | Directives | Principal judgment |

### Ring B Membranes (Metabolism)

| Crossing | Inward | Outward | Gate |
|----------|--------|---------|------|
| B0→B1 | Detected signals | Nothing | Monitoring |
| B1→B2 | Raw sources | Noise | Triage |
| B2→B3 | Queue items | Deprioritized | Processing slot |
| B3→B4 | Processed sources | Failed processing | Acceptance criteria |
| B4→B5 | Integration candidates | Rejected | 18 Lenses |
| B5→B6 | Canonical knowledge | Nothing | Operational need |
| B6→B7 | Outputs | Revisions | Quality gate |
| B7→B0 | Published | Nothing | Principal approval |

---

## What Cannot Cross

| Membrane | Blocked | Why |
|----------|---------|-----|
| B5 (Canon) | Unverified claims | Canon requires verification |
| B5 (Canon) | Temporal content | Canon must be time-stable |
| B5 (Canon) | Direct execution | Protected zone |
| A0 (Concierge) | Free-form handoffs | Must be packets |
| A2 (Execution) | Plans without verification | Definition of Done |

---

## Principal Position by Ring

| Ring | Principal Role | Frequency |
|------|----------------|-----------|
| A0 | Active governance | Always |
| A1 | Reconciliation review | When chorus used |
| A2 | Verification review | At culmination |
| A3 | Triage judgment | Occasional |
| A4 | Tool selection | Rare |
| B0-B3 | Monitoring | Low |
| B4-B5 | Approval | At canonization |
| B6-B7 | Direction | Active |

**Design Principle**: Principal involvement increases at membrane crossings, not within rings.
