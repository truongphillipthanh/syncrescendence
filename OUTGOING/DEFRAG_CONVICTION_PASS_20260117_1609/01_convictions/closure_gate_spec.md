# Closure Gate Specification
## "No Completion Without Artifacts"
**Generated**: 2026-01-17

---

## I. GATE DEFINITION

The **Closure Gate** is a mandatory checkpoint before any session or task can be marked complete.

```
                     WORK IN PROGRESS
                           │
                           ▼
                    ┌─────────────┐
                    │   CLOSURE   │
                    │    GATE     │
                    └──────┬──────┘
                           │
              ┌────────────┴────────────┐
              │                         │
         ARTIFACTS                 NO ARTIFACTS
         PRESENT?                  PRESENT?
              │                         │
              ▼                         ▼
         ┌────────┐              ┌────────────┐
         │  PASS  │              │   BLOCK    │
         │        │              │            │
         │ May    │              │ "Cannot    │
         │ close  │              │  close:    │
         │        │              │  missing   │
         └────────┘              │  [list]"   │
                                 └────────────┘
```

---

## II. REQUIRED ARTIFACTS BY SESSION TYPE

### Execution Session (Claude Code)

| Artifact | Required | Location | Purpose |
|----------|----------|----------|---------|
| Execution Packet (EXE) | YES | blackboard/executions/ | What was done |
| Git Commits | YES | Repository | Persistent changes |
| State Update | IF CHANGED | system_state.json | Current state |
| Event Log Entry | IF SIGNIFICANT | events.jsonl | Audit trail |
| Continuation Packet (CONT) | IF DELETABLE | blackboard/continuations/ | Handoff |

### Planning Session (ChatGPT)

| Artifact | Required | Location | Purpose |
|----------|----------|----------|---------|
| Plan Packet (PLN) | YES | blackboard/plans/ | Specification |
| Continuation Packet (CONT) | IF DELETABLE | blackboard/continuations/ | Handoff |

### Research Session (Gemini/Perplexity)

| Artifact | Required | Location | Purpose |
|----------|----------|----------|---------|
| Evidence Packet (EVD) | YES | blackboard/evidence/ | Findings |
| Continuation Packet (CONT) | IF DELETABLE | blackboard/continuations/ | Handoff |

### Synthesis Session (Claude Web / Oracle)

| Artifact | Required | Location | Purpose |
|----------|----------|----------|---------|
| Oracle Context | YES | oracle_contexts/ | Session record |
| Directive(s) | IF GENERATED | directives/ | Execution instructions |
| Continuation Packet (CONT) | IF DELETABLE | blackboard/continuations/ | Handoff |

### Audit Session (ChatGPT)

| Artifact | Required | Location | Purpose |
|----------|----------|----------|---------|
| Audit Packet (AUD) | YES | blackboard/audits/ | Verification |
| Continuation Packet (CONT) | IF DELETABLE | blackboard/continuations/ | Handoff |

---

## III. MINIMAL PACKET FIELD REQUIREMENTS

### Evidence Packet (EVD)

```yaml
required_fields:
  - id: "EVD-YYYYMMDD-NNN"
  - created: "ISO 8601 timestamp"
  - source: "platform name"
  - query: "what was investigated"
  - findings: "list with confidence levels"
  - uncertainties: "what remains unclear"

optional_fields:
  - corpus_slice: "files examined"
  - recommended_probe: "next investigation"
```

### Plan Packet (PLN)

```yaml
required_fields:
  - id: "PLN-YYYYMMDD-NNN"
  - created: "ISO 8601 timestamp"
  - objective: "one clear sentence"
  - deliverables: "list with locations"
  - acceptance_criteria: "list with verifications"

optional_fields:
  - evidence_ids: "source evidence packets"
  - stop_conditions: "when to halt"
  - tracks: "parallel work streams"
```

### Execution Packet (EXE)

```yaml
required_fields:
  - id: "EXE-YYYYMMDD-NNN"
  - created: "ISO 8601 timestamp"
  - plan_id: "PLN-YYYYMMDD-NNN or directive"
  - status: "complete|partial|failed"
  - changes: "list of file changes"
  - verification: "list of checks with results"

optional_fields:
  - issues_encountered: "problems and resolutions"
  - commits: "git commit hashes"
```

### Audit Packet (AUD)

```yaml
required_fields:
  - id: "AUD-YYYYMMDD-NNN"
  - created: "ISO 8601 timestamp"
  - execution_id: "EXE-YYYYMMDD-NNN"
  - plan_id: "PLN-YYYYMMDD-NNN"
  - criteria_results: "list with pass/fail"
  - recommendation: "accept|reject|revise"

optional_fields:
  - drift_analysis: "how execution differed"
  - follow_up_actions: "what to do next"
```

### Continuation Packet (CONT)

```yaml
required_fields:
  - id: "CONT-YYYYMMDD-NNN"
  - created: "ISO 8601 timestamp"
  - source: "platform and surface"
  - status: "complete|partial|blocked"
  - summary: "one paragraph"
  - work_completed: "list with locations"
  - work_remaining: "list with priorities"
  - safe_to_delete: "boolean with reason"

optional_fields:
  - decisions_made: "list with rationale"
  - context_for_next: "paragraph"
  - files_to_load: "list of paths"
```

---

## IV. CLOSURE GATE CHECKLIST

Before claiming completion, verify:

### For Execution Sessions
- [ ] Changes committed with semantic prefix
- [ ] Execution packet written to blackboard/executions/
- [ ] Verification commands run with evidence
- [ ] State vector updated (if changed)
- [ ] Event logged (if significant)
- [ ] Continuation packet written (if session deletable)
- [ ] "Safe to delete: YES/NO" stated explicitly

### For Planning Sessions
- [ ] Plan packet written to blackboard/plans/
- [ ] Acceptance criteria have verification methods
- [ ] Continuation packet written (if session deletable)
- [ ] "Safe to delete: YES/NO" stated explicitly

### For Research Sessions
- [ ] Evidence packet written to blackboard/evidence/
- [ ] Each finding has confidence level
- [ ] Uncertainties explicitly stated
- [ ] Continuation packet written (if session deletable)
- [ ] "Safe to delete: YES/NO" stated explicitly

### For Synthesis Sessions
- [ ] Oracle context document created
- [ ] Directive(s) created if action required
- [ ] Artifacts downloadable/exported to repo
- [ ] Continuation packet written (if session deletable)
- [ ] "Safe to delete: YES/NO" stated explicitly

---

## V. GATE FAILURE HANDLING

### When Gate Fails

```
ATTEMPTED CLOSURE
      │
      ▼
  ┌──────────────────────────────────┐
  │ Check required artifacts         │
  └──────────────┬───────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
    ALL PRESENT      MISSING
        │                 │
        ▼                 ▼
     [PASS]          [IDENTIFY]
                          │
                          ▼
                  "Cannot close:
                   Missing:
                   - [artifact 1]
                   - [artifact 2]

                   Creating now..."
                          │
                          ▼
                  [CREATE MISSING]
                          │
                          ▼
                  [RETRY GATE]
```

### Example Gate Failure Message

```markdown
**CLOSURE GATE FAILED**

Cannot close session. Missing artifacts:

- [ ] Execution packet (EXE-YYYYMMDD-NNN) — not written
- [ ] Continuation packet (CONT-YYYYMMDD-NNN) — not written

Creating missing artifacts now...

[Creates EXE packet]
[Creates CONT packet]

Retrying closure gate...

**CLOSURE GATE PASSED**
- Execution packet: blackboard/executions/EXE-20260117-001.md
- Continuation packet: blackboard/continuations/CONT-20260117-001.md
- Safe to delete: YES

Session may now be closed.
```

---

## VI. EXEMPTIONS

The closure gate may be skipped ONLY for:

| Condition | Why Exempt |
|-----------|------------|
| Trivial session (< 5 min, no artifacts) | Overhead exceeds value |
| Pure Q&A (no state change) | Nothing to record |
| Interrupted session with immediate resume | Context preserved |

**Even trivial sessions should state "No artifacts required for this session."**

---

## VII. VERIFICATION COMMAND

After any session end, run:

```bash
# Check recent packets exist
ls -lt 00-ORCHESTRATION/blackboard/*/  | head -10

# Check state vector current
cat 00-ORCHESTRATION/state/system_state.json | head -10

# Check recent events
tail -5 00-ORCHESTRATION/state/events.jsonl

# Check git status
git status --short
```

---

**The Closure Gate enforces: "No work without receipts in the well."**
