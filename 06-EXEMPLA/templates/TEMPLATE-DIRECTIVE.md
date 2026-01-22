# DIRECTIVE: DIR-YYYYMMDD-NAME

---
## DECISION ENVELOPE
handoff_id: HO-YYYYMMDD-HHMMSS-[source]
origin_platform: [claude-web|chatgpt|gemini|claude-code]
origin_session: [thread name or ID]
destination_platform: [target platform]
decision_timestamp: YYYY-MM-DDTHH:MM:SSZ

### Decision Context
trigger: [What prompted this work]
alternatives_considered:
  - [Option A]: [why rejected]
selected_approach: [Chosen option]
selection_rationale: |
  [2-5 sentences explaining WHY]

### Assumptions
- [Assumption that could invalidate directive if wrong]

### Constraints Inherited
- [Constraint from prior decisions]

### Dependencies
- prior_handoff: [HO-ID or "none"]
- blocks: [downstream work]

### Principal Checkpoints
- [ ] Reviewed decision rationale
- [ ] Approved for execution
---

## PREAMBLE
```bash
# Initialize execution log
```

## OBJECTIVE
[What success looks like]

## CONSTRAINTS
[Hard boundaries]

## DELIVERABLES
- [ ] Item 1

## VERIFICATION
```bash
# Commands to prove completion
```

## POSTAMBLE
```bash
# Finalize and commit
```
