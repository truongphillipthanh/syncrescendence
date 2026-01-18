# Rings Dependency Graph
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: DAG-like description of what must exist before what

---

## Dependency Overview

The rings model creates a directed acyclic graph (DAG) where each layer depends on artifacts from prior layers. This document specifies the dependencies.

---

## Layer Dependencies

```
┌─────────────────────────────────────────────────────────────────┐
│                        DEPENDENCY DAG                           │
└─────────────────────────────────────────────────────────────────┘

                    [Ring 0: External Reality]
                              │
                              │ signal_detection
                              ▼
                    [Ring 1: Ingest Layer]
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
            raw_transcript        metadata_stub
                    │                   │
                    └─────────┬─────────┘
                              │ triage
                              ▼
                    [Ring 2: Queue Layer]
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
              sources.csv          priority_band
               entry                assignment
                    │                   │
                    └─────────┬─────────┘
                              │ process_selection
                              ▼
                    [Ring 3: Processing Layer]
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
            processed_source      key_insights
                    │                   │
                    └─────────┬─────────┘
                              │ integration_qualification
                              ▼
                    [Ring 4: Integration Layer]
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
            canon_target          source_citation
            identification        preparation
                    │                   │
                    └─────────┬─────────┘
                              │ canonization
                              ▼
                    [Ring 5: Canon Layer]
                              │
                              │ operational_activation
                              ▼
                    [Ring 6: Operational Layer]
                              │
                              │ output_synthesis
                              ▼
                    [Ring 7: Output Layer]
```

---

## Artifact Dependencies

### To Create a Processed Source (Ring 3)
**Required**:
1. Raw source file in `04-SOURCES/raw/`
2. sources.csv entry with triage status
3. Signal tier assignment
4. Value modality assessment
5. Processing function selection

**Formula**:
```
processed_source := f(raw_source, triage_decision, function_selection)
```

### To Create an Integration Packet (Ring 4)
**Required**:
1. Processed source with complete frontmatter
2. Synopsis (2-3 sentences)
3. Key insights (5-10 points)
4. Canon target identification
5. Plan packet (optional, for complex integrations)

**Formula**:
```
integration_packet := f(processed_source, canon_targets, plan_packet?)
```

### To Update Canon (Ring 5)
**Required**:
1. Integration packet with acceptance criteria
2. 18 Lenses evaluation (≥12/18 pass)
3. Principal approval (for paradigm-level)
4. Source citation prepared
5. Version history note drafted

**Formula**:
```
canon_update := f(integration_packet, lenses_eval, approval)
                WHERE lenses_score >= 12
```

### To Complete Operational Task (Ring 6)
**Required**:
1. Canon reference for relevant knowledge
2. Directive (or implicit task specification)
3. Platform routing decision
4. Execution capacity available
5. Zone ownership verified

**Formula**:
```
execution := f(directive, canon_reference, routing_decision, zone_check)
```

---

## Blocking Dependencies

### What Blocks Ring 3 (Processing)
| Blocker | Condition | Unblock |
|---------|-----------|---------|
| No raw source | File doesn't exist | Ingest source first |
| No triage | sources.csv missing entry | Run triage protocol |
| No function | Routing not determined | Apply processing_routing rules |
| Quota exhausted | Platform rate-limited | Wait or switch platform |

### What Blocks Ring 4 (Integration)
| Blocker | Condition | Unblock |
|---------|-----------|---------|
| Incomplete frontmatter | Required fields missing | Complete processing |
| No synopsis | Synopsis field empty | Generate synopsis |
| No insights | Key insights not extracted | Extract insights |
| No canon target | Target not identified | Analyze chain alignment |

### What Blocks Ring 5 (Canon)
| Blocker | Condition | Unblock |
|---------|-----------|---------|
| Failed 18 Lenses | Score < 12 | Revise or reject |
| No approval | Principal hasn't approved | Request approval |
| Redundant | Already in Canon | Skip integration |
| Temporal | Content is time-bound | Reject from Canon |

### What Blocks Ring 6 (Operational)
| Blocker | Condition | Unblock |
|---------|-----------|---------|
| Zone conflict | Another instance owns zone | Wait or coordinate |
| Platform unavailable | Status != available | Wait or reroute |
| Missing context | Required Canon not accessible | Load context |
| Protected zone | Canon deletion attempted | Reject, escalate |

---

## Circular Dependencies (Prohibited)

The following patterns would create deadlocks and are prohibited:

### Anti-Pattern 1: Processing Requires Canon
```
❌ Processing → Canon → Processing
   (Source processing cannot require Canon update first)
```
**Solution**: Processing uses existing Canon as reference; doesn't require new Canon.

### Anti-Pattern 2: Integration Requires Output
```
❌ Integration → Output → Integration
   (Canon update cannot depend on publication)
```
**Solution**: Canon is internal truth; output is derived.

### Anti-Pattern 3: Operational Modifies Canon
```
❌ Operational → Canon (direct modification)
   (Operations reference Canon; don't modify directly)
```
**Solution**: Canon modifications go through Ring 4→5 path with approval.

---

## Parallel Processing Opportunities

### Independent Paths (Can Run Parallel)
```
Source A: Ring 1 → Ring 2 → Ring 3
Source B: Ring 1 → Ring 2 → Ring 3
Source C: Ring 1 → Ring 2 → Ring 3
```
Different sources can process independently until integration.

### Converging Paths (Must Synchronize)
```
Source A: Ring 3 → Ring 4 ─┐
Source B: Ring 3 → Ring 4 ─┼─→ Canon Update (serialized)
Source C: Ring 3 → Ring 4 ─┘
```
Canon updates must serialize to avoid conflicts.

### Stream Isolation (Blitzkrieg Pattern)
```
Stream A: Ring 3 → Ring 4 → Staging Area A
Stream B: Ring 3 → Ring 4 → Staging Area B
                    ↓
            Merge → Ring 5 (Canon)
```
Parallel streams work independently, merge at Canon.

---

## Minimum Viable Path

To get a single source from external reality to Canon:

```yaml
minimum_path:
  1: Detect signal (Ring 0→1)
     - Duration: Immediate
     - Artifact: raw transcript

  2: Triage (Ring 1→2)
     - Duration: ~30 seconds
     - Artifact: sources.csv entry

  3: Process (Ring 2→3)
     - Duration: 2-10 minutes
     - Artifact: processed source

  4: Integrate (Ring 3→4)
     - Duration: 5-15 minutes
     - Artifact: integration packet

  5: Canonize (Ring 4→5)
     - Duration: 2-5 minutes + approval time
     - Artifact: Canon update

total_minimum_time: ~15-35 minutes + approval
```

---

## Dependency Verification Commands

### Check Ring 1 Complete
```bash
ls 04-SOURCES/raw/*.txt 04-SOURCES/raw/*.md | head -5
```

### Check Ring 2 Complete
```bash
grep "triaged" 04-SOURCES/sources.csv | wc -l
```

### Check Ring 3 Complete
```bash
ls 04-SOURCES/processed/SOURCE-*.md | wc -l
```

### Check Ring 4 Complete
```bash
ls 00-ORCHESTRATION/blackboard/executions/*.json | wc -l
```

### Check Ring 5 Current
```bash
git log --oneline 01-CANON/ | head -5
```
