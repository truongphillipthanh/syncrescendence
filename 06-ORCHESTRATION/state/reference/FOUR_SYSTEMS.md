# Four-System Intelligence Architecture
## Operational Modes of the Intelligence Apparatus

**Version**: 1.0.0
**Created**: 2026-01-01
**Authority**: Oracle9
**Source**: Gemini conversation (2025-06-17)

---

## Overview

The intelligence apparatus operates in **four modes**, not four pipelines.

These are complementary operational patterns, not separate systems.

---

## System 1: Automatic-Push (Scheduled Monitoring)

### Purpose
Proactively monitor trusted, high-cadence sources and deliver synthesis.

### Characteristics
- **Trigger**: Schedule (daily, weekly)
- **Sources**: Known high-signal, periodic publications
- **Processing**: Automated transcription + synthesis
- **Output**: Daily/weekly intelligence brief

### Example Workflow
```
6:00 AM: Scheduled trigger
  ↓
Poll Feedly RSS for new items from:
  - Bloomberg Technology
  - No Priors podcast
  - Lex Fridman new episodes
  ↓
Download and process new items
  ↓
Generate "State of the Union" brief
  ↓
Deliver to inbox / review queue
```

### IIC Mapping
Maps to **Daily Intelligence Brief** in Acumen IIC architecture.

---

## System 2: Curation-Push (Serendipitous Discovery)

### Purpose
Frictionless save-to-queue from mobile browsing, high-fidelity processing.

### Characteristics
- **Trigger**: User save action (Watch Later, bookmark, etc.)
- **Sources**: Serendipitous finds during browsing
- **Processing**: Multi-modal transcription when queued item processed
- **Output**: Clean source in SOURCES/processed/

### Example Workflow
```
User browsing on phone
  ↓
Sees interesting YouTube video
  ↓
Saves to Watch Later playlist
  ↓
(Later) Agent polls Watch Later
  ↓
Processes via Gemini
  ↓
Deposits in SOURCES/processed/
  ↓
Awaits triage and integration
```

### IIC Mapping
Maps to **Serendipitous Encounters** stream in Acumen IIC.

---

## System 3: On-Demand-Pull (Active Research)

### Purpose
Query-driven deep dives on specific topics.

### Characteristics
- **Trigger**: User research query
- **Sources**: Trans-platform search based on query
- **Processing**: Full synthesis across sources
- **Output**: Research packet / synthesis document

### Example Workflow
```
User: "What's the latest on multimodal reasoning?"
  ↓
Search across:
  - YouTube (relevant videos)
  - ArXiv (recent papers)
  - X (discourse threads)
  ↓
Process and synthesize
  ↓
Deliver research packet
```

### IIC Mapping
Maps to **Active Research** mode in Coherence IIC.

---

## System 4: Triage & Qualification (Gatekeeper)

### Purpose
Pre-filter answering: "Is this worth my attention?"

### Characteristics
- **Trigger**: Any source entering the system
- **Sources**: All sources before processing
- **Processing**: Quick classification + tier assignment
- **Output**: Routing decision

### Critical Questions
- Is the dialogue the story? → Read transcript
- Are the comments the story? → Read discourse
- Are the visuals the story? → Watch video
- Is the delivery the story? → Listen to audio

### Example Workflow
```
New source arrives
  ↓
Quick scan (30 sec)
  ↓
Assign signal_tier:
  - paradigm → full processing
  - strategic → queue processing
  - tactical → archive
  - noise → prune
  ↓
Assign value_modality:
  - dialogue_primary → transcript sufficient
  - visual_primary → watch recommended
  ↓
Route accordingly
```

### IIC Mapping
Maps to **Priority Band** system in Acumen IIC.

---

## How Systems Interact

```
┌─────────────────────────────────────────────────────────────┐
│                    INCOMING SOURCES                         │
└──────────────────────────┬──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   ┌─────────┐       ┌─────────┐       ┌─────────┐
   │ System  │       │ System  │       │ System  │
   │    1    │       │    2    │       │    3    │
   │ Auto-   │       │ Curation│       │ On-     │
   │ Push    │       │  Push   │       │ Demand  │
   └────┬────┘       └────┬────┘       └────┬────┘
        │                 │                 │
        └────────────────┬┘─────────────────┘
                         │
                         ▼
                  ┌─────────────┐
                  │   System 4   │
                  │   Triage &   │
                  │ Qualification│
                  └──────┬──────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   ┌─────────┐     ┌─────────┐     ┌─────────┐
   │ PARADIGM│     │STRATEGIC│     │TACTICAL │
   │ Process │     │  Queue  │     │ Archive │
   └─────────┘     └─────────┘     └─────────┘
```

---

## MVP Implementation

For Oracle9 MVP:

| System | Implementation | Status |
|--------|----------------|--------|
| System 1 | Manual batch processing | Manual |
| System 2 | transcripts.zip = accumulated queue | Ready |
| System 3 | On-demand triage + processing | Manual |
| System 4 | Triage protocol documented | Ready |

Future automation:
- Gemini RPA for YouTube processing
- n8n for RSS/Feedly polling
- Scheduled triggers for daily brief

---

## Holistic Not Componential

**Principal's instruction**:
> "This insight should be factored in holistically, not componentially."

These four systems are **modes of operation**, not separate pipelines.

The same source might:
- Enter via System 2 (saved during browsing)
- Pass through System 4 (triage)
- Get enhanced via System 3 (research query adds context)
- Inform System 1 (becomes part of monitored feeds)

Think of four lenses on the same apparatus, not four machines.

---

## System Selection Guide

| Situation | Primary System | Notes |
|-----------|----------------|-------|
| New episode from subscribed podcast | System 1 | Automatic processing |
| Interesting video found on X | System 2 | Save for later processing |
| "What does Anthropic say about..." | System 3 | Active research query |
| New source enters apparatus | System 4 | Always runs first |
| Daily check of feeds | System 1 | Scheduled |
| Browsing discovers gem | System 2 | Queue for processing |
| Deep dive on topic | System 3 | Cross-platform synthesis |

---

## Cross-References

- **Sources Schema**: See `SOURCES_SCHEMA.md` for dimension definitions
- **Triage Protocol**: See `TRIAGE_PROTOCOL.md` for qualification procedures
- **Processing Routing**: See `PROCESSING_ROUTING.md` for function selection
- **ORACLE9 Context**: See `ORACLE9_CONTEXT_v2.md` for architectural decisions
- **IIC Architecture**: See CANON documents on IIC (Acumen, Coherence)
