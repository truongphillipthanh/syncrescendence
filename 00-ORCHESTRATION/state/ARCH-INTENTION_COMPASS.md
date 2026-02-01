# INTENTION ARCHAEOLOGY COMPASS
## Oracle Pedigree Extraction Instrument
**Last Updated**: 2026-02-01
**Oracle Lineage**: 0 → 12
**Status**: Rolling snapshot
**Authority**: Oracle 12

---

## PURPOSE

The Intention Archaeology Compass is a unified instrument that extracts, categorizes, and tracks Sovereign intentions across Oracle sessions. It serves as both:
- **Cache**: Quick reference for active intentions
- **Rolling Snapshot**: Historical record of intention evolution

From Oracle 12 (Sovereign's words):
> "The intention archaeology compass should be unified. All intentions are compounding vectors that are interdependent... In essence, it's a cache, but it's also a rolling snapshot."

---

## SCHEMA

Each intention entry contains:

```yaml
- id: INT-XXXX
  oracle: [origin Oracle number]
  timestamp: [ISO datetime or Oracle reference]
  category: [urgent|sprint|backlog|pattern|capture]
  priority: [P0|P1|P2|P3]
  status: [active|resolved|superseded|deferred]
  text: "[Sovereign's actual words]"
  interpretation: "[Oracle's understanding]"
  blocked_by: [null|dependency]
  integrated_into: [null|CANON/task/decision]
  notes: "[additional context]"
```

### Category Definitions

| Category | Description | Action Horizon |
|----------|-------------|----------------|
| **urgent** | Address NOW | Same session |
| **sprint** | Integrate at checkpoint | Current Oracle |
| **backlog** | Future work | Future Oracles |
| **pattern** | Meta-observations | Ongoing |
| **capture** | Undifferentiated inbox | Pending triage |

---

## ACTIVE INTENTIONS

### URGENT (Address NOW)

| ID | Oracle | Text | Status | Notes |
|----|--------|------|--------|-------|
| INT-1201 | 12 | "accounts become self-sustaining by month end" | failed | Jan 31 deadline missed. Reset target pending sovereign input. |
| INT-1202 | 12 | "capitalize on these heavy machinery to construct as much of Syncrescendence" | active | Maximum velocity during capability window |
| INT-1209 | 12 | "Temporal intelligence refresh pipeline" | active | Automation candidate for model/platform features that expire; cadenced update system for ARCH- archived research |

### SPRINT (Current Cycle)

| ID | Oracle | Text | Status | Integrated Into |
|----|--------|------|--------|-----------------|
| INT-1203 | 12 | "design/architect for 3 Claude + 1 Gemini + 1 ChatGPT paid" | active | [[CANON-25200-CONSTELLATION_ARCH-lattice]] |
| INT-1204 | 12 | "update [[CANON-25100-CONTEXT_TRANS-lattice]] with Oracle Pedigree section" | resolved | [[CANON-25100-CONTEXT_TRANS-lattice]] v2.1.0 |
| INT-1205 | 12 | "intention archaeology compass should be unified" | resolved | This document |
| INT-1206 | 11 | "Complete Efficacy, Mastery, Transcendence IIC configs" | active | PROJ-002 |
| INT-1101 | 11 | "Multi-CLI integration validation" | resolved | DIRECTIVE-042B |
| INT-1210 | 12 | "Canonize Model Manual/Prompting conceptual space" | resolved | ARCH-TECH_TREE_AUDIT.md: 10 CANON files + translate.xml provide sufficient coverage |
| INT-1211 | 12 | "Canonize Platform Features/Ecosystem Leverage" | resolved | ARCH-TECH_TREE_AUDIT.md: 77 CANON files provide excellent coverage |
| INT-1212 | 12 | "Canonize Model Qualities/Capabilities/Benchmarks" | resolved | ARCH-TECH_TREE_AUDIT.md: 73 CANON files with correct temporal/evergreen split |
| INT-1213 | 12 | "Blitzkrieg model specification protocol" | resolved | CLAUDE.md v2.1.0 + coordination.yaml v2.1.0 per DIRECTIVE-044B |

### BACKLOG (Future Work)

| ID | Oracle | Text | Status | Priority | Notes |
|----|--------|------|--------|----------|-------|
| INT-1207 | 12 | "Manus before Perplexity" | deferred | P3 | Platform prioritization |
| INT-1208 | 12 | "promos for Perplexity and additional Gemini account" | deferred | P3 | Cost optimization future |
| INT-0801 | 8+ | "Tech Lunar 306K specs to CANON-30xxx" | deferred | P2 | PROJ-008 |
| INT-0802 | 8+ | "Modal 2 visual capabilities" | deferred | P3 | PROJ-009 |
| INT-1102 | 11 | "Skills conversion for top 5 functions" | deferred | P3 | PROJ-016 |
| INT-0701 | 7 | "Browser automation for account cloning" | deferred | P3 | PROJ-015 |
| INT-1214 | 12 | "Deep Research: Claude Code + Anthropic Ecosystem" | deferred | P2 | Prompt prepared |
| INT-1215 | 12 | "Deep Research: OpenAI Codex + ecosystem" | deferred | P3 | Requires community sampling |
| INT-1216 | 12 | "Deep Research: Google Jules + Gemini CLI" | deferred | P3 | Requires community sampling |
| INT-1217 | 12 | "Plan Mode as Oracle replacement" | deferred | P3 | Evaluate CLI Plan vs web app strategic synthesis |
| INT-1218 | 12 | "Permission fatigue mitigation" | deferred | P3 | --dangerously-skip-permissions vs allowlisting |

### PATTERNS (Meta-Observations)

| ID | Oracle | Pattern | Status | Notes |
|----|--------|---------|--------|-------|
| INT-P001 | 3 | "Orchestration is OPERATIONAL, not CANON" | resolved | Constitutional rule |
| INT-P002 | 4 | "Metabolism applies to CONTENT, not infrastructure" | resolved | Constitutional rule |
| INT-P003 | 6 | "Verify before declare" | resolved | Constitutional rule |
| INT-P004 | 7 | "Globe before trees" | active | Holistic framing first |
| INT-P005 | 10 | "automation infrastructure must precede content work" | resolved | PROJ-011 complete |
| INT-P006 | 12 | "Multi-agent 90.2% outperforms single-agent" | active | Constellation justification |
| INT-P007 | 12 | "Pedigree supersedes handoff for repository-centric work" | active | New paradigm |
| INT-P008 | 12 | "Temporal vs evergreen distinction" | resolved | Archive temporal intelligence with expiration warning; CANON = evergreen only |

### CAPTURE (Pending Triage)

| ID | Oracle | Raw Capture | Status |
|----|--------|-------------|--------|
| INT-C001 | 12 | "audit and anneal the corpus again for alignment/congruence" | pending |
| INT-C002 | 12 | "attached reports ought to be canonized" | pending |
| INT-C003 | 13 | "Revenue target reset — new deadline TBD by Sovereign" | pending |
| INT-C004 | 13 | "Corpus hygiene sprint: triage -INBOX, refresh stale state, compress" | pending |

---

## HISTORICAL EXTRACTIONS

### Oracle 0: Vision

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0001 | "civilizational sensing infrastructure" | resolved | Core framing established |
| INT-0002 | "skate to where the puck is going" | active | Ongoing design principle |
| INT-0003 | "leverage The Bitter Lesson" | active | Lens 2 institutionalized |

### Oracle 1: Research

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0101 | "consumer/prosumer focus" | resolved | Ecosystem cartography scope |
| INT-0102 | "multi-platform strategy" | active | 5-platform constellation |

### Oracle 2: Infrastructure

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0201 | "flat + symlink architecture" | resolved | Decision 2.1 |
| INT-0202 | "designing the librarian, not compressing the library" | active | Context engineering thesis |
| INT-0203 | "human navigation: comprehensible in 5 minutes" | active | Design constraint |

### Oracle 3: Orchestration Peak

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0301 | "orchestration infrastructure pattern" | resolved | THE MODEL established |
| INT-0302 | "Reception Calibration vs Archetype Engineering" | resolved | Three-layer architecture |
| INT-0303 | "visibility bridge via execution logs" | active | Visibility flow |

### Oracle 4: Metabolic Defrag

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0401 | "canonize or delete, no middle ground" | superseded | Too aggressive |
| INT-0402 | "79% file reduction" | resolved | Defrag completed |
| INT-0403 | "nine evaluative lenses" | resolved | Extended to 18 in Oracle 6 |

### Oracle 5: Recovery + Genesis

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0501 | "orchestration is protected infrastructure" | resolved | Constitutional rule |
| INT-0502 | "Genesis layer creation" | resolved | CANON-0000x series |
| INT-0503 | "most extreme dynamic progressive route" | active | Decision principle |

### Oracle 6: Semantic Annealment

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0601 | "extended nine lenses to 18" | resolved | STANDARDS.md |
| INT-0602 | "bifurcation: filesystem vs Obsidian" | resolved | Decision 6.2 |
| INT-0603 | "aliases for Finder, not Obsidian" | active | Design principle |

### Oracle 7: Ground Truth

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0701 | "REVIEW EVERY CONVERSATION" | resolved | Forensic audit completed |
| INT-0702 | "maximum resolution documentation" | active | ORACLE_DECISIONS.md created |
| INT-0703 | "repository is Foyer" | active | All context accessible |

### Oracle 8-9: [Recovery Phase]

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-0801 | "complete PROJ-001 transcript ingestion" | resolved | 43 sources processed |
| INT-0901 | "directory restructuring to 00-06" | resolved | Numbered scheme deployed |

### Oracle 10: Infrastructure Completion

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-1001 | "PROJ-011 automation infrastructure" | resolved | CLAUDE.md + Makefile + commands |
| INT-1002 | "multi-Claude coordination" | resolved | coordination.yaml |
| INT-1003 | "worktree-based isolation" | active | Zone ownership pattern |

### Oracle 11: Blitzkrieg

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-1101 | "parallel stream execution" | resolved | 4 streams completed |
| INT-1102 | "IIC configuration reconnaissance" | resolved | 14500+ lines reviewed |
| INT-1103 | "Gemini CLI validation" | resolved | APPROVED |

### Oracle 12: Constellation Architecture

| ID | Text | Status | Outcome |
|----|------|--------|---------|
| INT-1201 | "self-sustaining by month end" | active | Revenue target |
| INT-1202 | "5-platform constellation" | active | [[CANON-25200-CONSTELLATION_ARCH-lattice]] |
| INT-1203 | "ChatGPT Plus integration" | active | coordination.yaml update |
| INT-1204 | "Oracle Pedigree protocol" | resolved | [[CANON-25100-CONTEXT_TRANS-lattice]] update |
| INT-1205 | "unified intention compass" | resolved | This document |

---

## INTEGRATION PROTOCOL

### 1. Extraction (During Oracle Session)

When Sovereign speaks:
1. Capture exact words in quotes
2. Assign temporary INT-XXXX ID
3. Note Oracle number
4. Add to CAPTURE category if unclear

### 2. Categorization (Session Checkpoint)

Move from CAPTURE to appropriate category:
- **urgent**: Requires immediate action
- **sprint**: Part of current cycle
- **backlog**: Future work
- **pattern**: Meta-observation

### 3. Resolution Tracking

When intention is addressed:
1. Update status to `resolved`
2. Add `integrated_into` reference
3. Document outcome

### 4. Supersession

When intention is replaced:
1. Update status to `superseded`
2. Reference replacing intention
3. Document rationale

---

## DEPENDENCY MAP

```
INT-1201 (sustainability) ──────────────────► Revenue generation
     │
     ├── INT-1202 (heavy machinery) ──────► Maximum velocity
     │        │
     │        └── INT-1203 (5 platforms) ─► [[CANON-25200-CONSTELLATION_ARCH-lattice]]
     │
     └── INT-1206 (IIC configs) ──────────► PROJ-002 completion
              │
              └── INT-1101 (multi-CLI) ───► Gemini validated

INT-P006 (multi-agent 90.2%) ─────────────► Constellation justification
     │
     └── INT-P007 (pedigree) ─────────────► New paradigm
```

---

## PATTERN ANALYSIS

### Recurring Themes

1. **Velocity**: "capitalize", "heavy machinery", "accelerating pace"
2. **Architecture**: "constellation", "5-platform", "specialization"
3. **Sustainability**: "self-sustaining", "month end"
4. **Holism**: "unified", "integrated", "globe before trees"

### Anti-Patterns Identified

1. **Oracle 4 Category Error**: Applied metabolism to infrastructure
2. **Oracle 6 Verification Failure**: Evaluated reports, not reality
3. **Fragmented Intention Tracking**: Pre-compass scattered approach

### Success Patterns

1. **Oracle 3 Model**: Orchestration infrastructure pattern
2. **Oracle 10-11 Blitzkrieg**: Parallel stream execution
3. **Oracle 12 Constellation**: Purpose-specialized platforms

---

## MAINTENANCE SCHEDULE

| Action | Frequency | Responsible |
|--------|-----------|-------------|
| Extract intentions | Every Oracle session | Active Oracle |
| Categorize captures | Session checkpoint | Active Oracle |
| Resolve completed | Immediately on completion | Executing instance |
| Pattern analysis | Monthly | Any Oracle |
| Archive old resolved | Quarterly | Any Oracle |

---

## VERSION HISTORY

**v1.0.0** (2026-01-11): Genesis establishment
- Complete extraction from Oracle 0-12
- Schema defined with 5 categories
- Integration protocol documented
- Pattern analysis included
- Authority: Oracle 12 / DIRECTIVE-043A

---

**END ARCH-INTENTION_COMPASS.md**
