# DESIGN: Handoff Protocol Formalization

## Problem Statement

The current handoff pattern loses decision context:

```
Claude Web (reasoning) → [artifact] → User downloads → Claude Code (executes)
                              ↑
                    Decision rationale lives HERE
                    but doesn't travel with the artifact
```

When a directive lands in Claude Code, it contains *what* to do but not *why* the decision was made. This creates:

1. **Auditability gaps** — Future agents can't trace reasoning
2. **Modification friction** — Claude Code can't intelligently adapt without context
3. **Sovereign burden** — User becomes the sole carrier of rationale across the gap

## Design Constraints

- Handoffs must be **self-contained** (receiving agent has no access to originating conversation)
- Token economics matter (can't embed entire conversation history)
- Must work across all platform combinations (Claude Web → Claude Code, ChatGPT → Claude Code, Gemini → anywhere)
- Must be human-legible (Sovereign reviews everything)

## Proposed Solution: Decision Envelope Protocol

Every handoff artifact includes a **Decision Envelope** header that captures:

```markdown
---
# DECISION ENVELOPE
handoff_id: HO-YYYYMMDD-HHMMSS-[short-hash]
origin_platform: [claude-web|chatgpt|gemini|claude-code]
origin_session: [conversation ID or "unavailable"]
destination_platform: [target platform]
decision_timestamp: YYYY-MM-DDTHH:MM:SSZ

## Decision Context
trigger: [What prompted this work—user request, prior directive output, scheduled task]
alternatives_considered:
  - [Option A]: [why rejected]
  - [Option B]: [why rejected]
selected_approach: [Option C]
selection_rationale: |
  [2-5 sentences explaining WHY this approach, not WHAT it does]

## Assumptions
- [Assumption 1 that, if wrong, invalidates this directive]
- [Assumption 2]

## Constraints Inherited
- [Constraint from prior decisions that shaped this one]

## Dependencies
- prior_handoff: [HO-ID if this continues prior work, else "none"]
- requires_completion_of: [list of prerequisites]
- blocks: [list of downstream work waiting on this]

## Sovereign Checkpoints
- [ ] Reviewed decision rationale
- [ ] Confirmed assumptions still valid
- [ ] Approved for execution

---

# [ACTUAL DIRECTIVE/ARTIFACT CONTENT BELOW]
```

## Token Economics Analysis

| Component | Estimated Tokens | Justification |
|-----------|------------------|---------------|
| Envelope metadata | ~50 | Fixed overhead |
| Decision context | ~150-300 | Scales with complexity |
| Assumptions | ~50-100 | Usually 2-4 items |
| Dependencies | ~30-50 | Usually sparse |
| Checkpoints | ~20 | Fixed |
| **Total overhead** | **~300-500** | <1% of typical directive |

This is acceptable overhead for the auditability gain.

## Relay Capture Protocol

When the Sovereign relays between platforms, they should:

### Option A: Minimal (Current State + Envelope)
1. Receiving platform gets the artifact with envelope
2. Sovereign adds nothing beyond copy-paste
3. Decision context travels in the envelope

### Option B: Annotated Relay
1. Sovereign adds a **Relay Note** when pasting:
   ```
   [RELAY NOTE - 2026-01-20 19:45 PST]
   Relaying from Claude Web (Ajna3 thread). 
   Additional context: [anything not in envelope]
   My modifications: [any changes made during relay]
   ```
2. Receiving agent incorporates relay note into execution log

### Option C: Structured Relay Packet
For complex multi-hop handoffs, use a wrapper:

```markdown
# RELAY PACKET

## Relay Chain
1. Origin: Claude Web (Ajna3) @ 2026-01-20T03:15:00Z
2. Relay 1: Sovereign review @ 2026-01-20T03:20:00Z
   - Modifications: [none | list]
   - Approval: [approved | approved with changes | deferred]
3. Destination: Claude Code @ 2026-01-20T03:25:00Z

## Enclosed Artifacts
- [x] DIR-20260120-EXECUTION-LOG-INFRASTRUCTURE.md (primary)
- [ ] Supporting context (if any)

## Relay Annotations
[Sovereign's notes that don't belong in the directive itself]

---
[ENCLOSED ARTIFACT BEGINS BELOW]
---
```

## Recommendation

Implement in phases:

### Phase 1 (Immediate): Decision Envelope
- Add envelope header to all directive templates
- Update `05-SIGMA/EXEMPLA-TEMPLATE-DIRECTIVE.md` to include envelope
- Producing agents (Claude Web, ChatGPT, Gemini) must populate envelope

### Phase 2 (Near-term): Relay Notes
- Sovereign adopts practice of adding `[RELAY NOTE]` blocks when context warrants
- Receiving agents trained to look for and log relay notes

### Phase 3 (When Needed): Structured Relay Packets
- Only for complex multi-hop scenarios
- Wrapper format for when artifacts pass through 3+ stations

## Anti-Patterns to Avoid

1. **Envelope bloat** — The envelope captures *decision* context, not *conversation* history. It should never exceed ~500 tokens.

2. **Redundant rationale** — If the directive body explains the approach, the envelope shouldn't repeat it. Envelope = *why this approach over others*; Body = *what the approach is*.

3. **Checkpoint theater** — The Sovereign checkpoints are real gates, not rubber stamps. If Sovereign doesn't review, don't check the box.

4. **Dependency sprawl** — If a directive has >3 dependencies, it's probably too coupled. Split it.

## Open Questions for Sovereign Decision

1. **Envelope requirement strictness**: Should *all* handoffs require envelopes, or only directives? (Recommendation: directives and canonization decisions require envelopes; simple queries don't)

2. **Relay note location**: Should relay notes go *inside* the artifact (permanent) or *alongside* it (ephemeral)? (Recommendation: inside, as execution log appendix)

3. **Handoff ID generation**: Who generates the `HO-` ID—the producing agent or the receiving agent? (Recommendation: producing agent, using timestamp + platform + hash)

4. **Cross-platform ID visibility**: Should handoff IDs reference conversation IDs that may not be accessible? (Recommendation: include if available, mark "unavailable" if not—partial traceability beats none)

---

## Implementation Artifacts Needed

If this design is approved:

1. Update `05-SIGMA/EXEMPLA-TEMPLATE-DIRECTIVE.md` with envelope header
2. Create `05-SIGMA/EXEMPLA-TEMPLATE-RELAY_PACKET.md` for Phase 3
3. Update ChatGPT COMPILER instructions to produce envelopes
4. Update Claude Web INTERPRETER config to produce envelopes
5. Update Gemini DIGESTOR prompt to produce envelopes on actionable outputs

---

*This document is itself a handoff artifact. It should be reviewed by Sovereign before implementation begins.*
