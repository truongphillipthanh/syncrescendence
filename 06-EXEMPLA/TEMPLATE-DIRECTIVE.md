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
- requires_completion_of: [prerequisites]
- blocks: [downstream work]

### Principal Checkpoints
- [ ] Reviewed decision rationale
- [ ] Confirmed assumptions still valid
- [ ] Approved for execution
---

## PREAMBLE
```bash
make log-init DIRECTIVE=NAME
```

## OBJECTIVE
[What success looks like]

## CONSTRAINTS
[Hard boundaries that must not be violated]

## DELIVERABLES
- [ ] Item 1
- [ ] Item 2

## VERIFICATION
```bash
# Commands to prove completion
```

## POSTAMBLE
```bash
make log STATUS=COMPLETE DIRECTIVE=NAME
git add -A
git commit -m "feat(DIR-YYYYMMDD-NAME): [summary]"
```

Append execution evidence to log file before committing.
