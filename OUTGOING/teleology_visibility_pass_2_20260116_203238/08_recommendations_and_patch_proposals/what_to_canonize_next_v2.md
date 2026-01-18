# What to Canonize Next v2
**Generated**: 2026-01-17T05:15:00Z
**Purpose**: Exact files to create, with placement and content specifications

---

## Canonization vs Operationalization

**Canonize** (add to 01-CANON/): Timeless principles, stable frameworks, permanent knowledge
**Operationalize** (add to 02-OPERATIONAL/): Protocols, procedures, living processes

Most items from this visibility pass should be **operationalized**, not canonized.

---

## Priority 1: Immediate Operationalization

### O-001: Session Lifecycle Protocol

**Create**: `02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md`

**Source**: `03_protocols_and_packets/session_lifecycle_protocol_v1.md` from this pass

**Modifications Before Operationalization**:
- Add version header
- Add "last updated" date
- Remove generation timestamp (becomes living doc)
- Ensure all procedures are copy-pasteable

**Verification**:
```bash
# File exists
ls 02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md

# Has required sections
grep -E "Cold Start|Warm Resume|Culmination|Handoff" 02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md
```

---

### O-002: Crashout Recovery Protocol

**Create**: `02-OPERATIONAL/PROTOCOL-CRASHOUT_RECOVERY.md`

**Source**: `06_crashout_forensics/crashout_postmortem.md` → extract "Recovery Protocol" section

**Content**:
```markdown
# Crashout Recovery Protocol
**Version**: 1.0.0
**Purpose**: Step-by-step recovery when context is lost or state incoherent

## Symptoms
[from postmortem]

## Recovery Procedure
[from postmortem - Step 1 through Step 5]

## Post-Incident
[from postmortem]
```

---

### O-003: Continuation Packet Schema

**Update**: `00-ORCHESTRATION/schemas/packet_protocol.json`

**Add**:
```json
{
  "continuation": {
    "description": "Session-to-session handoff packet",
    "id_format": "CONT-YYYYMMDD-NNN",
    "location": "00-ORCHESTRATION/continuations/",
    "required_fields": ["source_session", "state_snapshot", "context_files", "next_objectives"],
    "optional_fields": ["open_questions", "estimated_complexity"]
  }
}
```

**Also Create**: `00-ORCHESTRATION/continuations/` directory

---

### O-004: Kaizen Ledger

**Create**: `00-ORCHESTRATION/state/kaizen.csv`

**Initial Content**:
```csv
id,source_session,date_created,description,priority,status,date_completed,notes
K-001,ORACLE13,2026-01-16,"Create session lifecycle protocol",high,pending,,"From crashout analysis"
K-002,ORACLE13,2026-01-16,"Add continuation packet schema to packet_protocol.json",high,pending,,
K-003,ORACLE13,2026-01-16,"Create crashout recovery protocol",high,pending,,
K-004,ORACLE13,2026-01-16,"Implement operator translation layer guidelines",medium,pending,,
K-005,ORACLE13,2026-01-16,"Add routing constraints to coordination.yaml",medium,pending,,
```

---

### O-005: Retrospective Template

**Create**: `06-EXEMPLA/RETROSPECTIVE_TEMPLATE.md`

**Source**: `02_canon_scan/gaps_to_unified_protocol.md` → proposed template

---

## Priority 2: Routing Enhancements

### O-006: Routing Constraints

**Update**: `config/coordination.yaml`

**Add Section**:
```yaml
routing_constraints:
  context_thresholds:
    large: 100000
    corpus: 500000
  risk_triggers:
    high:
      - path_contains: "01-CANON"
      - operation: delete
    critical:
      - path_contains: "CLAUDE.md"
  escalation_defaults:
    max_retries: 3
```

---

## Priority 3: Canonization (If Warranted)

### C-001: Concentric Rings Model

**Consider Canonizing**: The dual ring-system (Interface + Metabolism)

**Proposed Location**: `01-CANON/CANON-25300-RING_TOPOLOGY-lattice.md`

**Rationale**: This is a stable architectural model that won't change with platform updates.

**Wait Condition**: Only canonize after the model has been used for at least 2 Oracle cycles and proven stable.

---

### C-002: Crashout Failure Pattern

**Consider Canonizing**: The 6-stage failure chain

**Proposed Location**: `01-CANON/CANON-30460-CRASHOUT_PATTERN-asteroid-INTELLIGENCE.md`

**Rationale**: This is a reusable pattern for understanding cognitive-system failures.

**Wait Condition**: Only canonize if the pattern proves generalizable beyond this specific system.

---

## What NOT to Canonize

| Item | Reason |
|------|--------|
| Teleology Atlas (CSV) | Temporal data, changes with platform updates |
| Account/Entitlements | Changes with subscriptions |
| Specific platform features | Updates frequently |
| This visibility pass | It's source material, not conclusion |
| Routing constraints | Operational, not canonical |
| Guardrails | Living rules, not permanent truths |

---

## Canonization Decision Framework

Before canonizing anything, apply:

### Question 1: Is it time-stable?
- Will this be true in 6 months?
- Does it describe principles or implementations?
- If implementations → operationalize, don't canonize

### Question 2: Does it pass 18 Lenses?
- Score ≥12/18 required
- Pay special attention to:
  - Lens 2 (Bitter Lesson): Will this scale?
  - Lens 3 (Antifragile): Does this gain from disorder?
  - Lens 4 (Meet the Moment): Is this relevant now?

### Question 3: Is it referenced by other Canon?
- Canon should be a connected graph
- Orphan Canon indicates scope issue
- If no natural connections → maybe operational instead

---

## Creation Order

| Order | Type | Item | Effort | Dependencies |
|-------|------|------|--------|--------------|
| 1 | Operationalize | Session Lifecycle Protocol | 30m | None |
| 2 | Operationalize | Continuation Packet Schema | 15m | None |
| 3 | Operationalize | Crashout Recovery Protocol | 20m | Session Lifecycle |
| 4 | Create | continuations/ directory | 1m | None |
| 5 | Create | First continuation packet | 10m | Schema |
| 6 | Create | Kaizen Ledger | 10m | None |
| 7 | Create | Retrospective Template | 15m | Kaizen format |
| 8 | Update | Routing Constraints in coordination.yaml | 20m | None |
| 9 | Review | Ring Topology for canonization | 30m | Usage in practice |

**Total Effort**: ~2.5 hours for priorities 1-2

---

## Patch Proposals (Ready to Apply)

### Patch P-001: Add Continuation to packet_protocol.json

```diff
--- a/00-ORCHESTRATION/schemas/packet_protocol.json
+++ b/00-ORCHESTRATION/schemas/packet_protocol.json
@@ -45,6 +45,15 @@
     "capability_event": {
       ...
+    },
+    "continuation": {
+      "description": "Session-to-session handoff packet",
+      "id_format": "CONT-YYYYMMDD-NNN",
+      "location": "00-ORCHESTRATION/continuations/",
+      "producer": "any_platform",
+      "consumer": "new_session",
+      "required_fields": ["id", "timestamp", "source_session", "state_snapshot", "context_files", "next_objectives"],
+      "optional_fields": ["open_questions", "estimated_complexity"]
     }
   }
 }
```

### Patch P-002: Create continuations directory

```bash
mkdir -p 00-ORCHESTRATION/continuations
touch 00-ORCHESTRATION/continuations/.gitkeep
```

### Patch P-003: Initialize kaizen.csv

```bash
cat > 00-ORCHESTRATION/state/kaizen.csv << 'EOF'
id,source_session,date_created,description,priority,status,date_completed,notes
K-001,ORACLE13,2026-01-16,"Create session lifecycle protocol",high,pending,,"From crashout analysis"
K-002,ORACLE13,2026-01-16,"Add continuation packet schema",high,pending,,
K-003,ORACLE13,2026-01-16,"Create crashout recovery protocol",high,pending,,
EOF
```
