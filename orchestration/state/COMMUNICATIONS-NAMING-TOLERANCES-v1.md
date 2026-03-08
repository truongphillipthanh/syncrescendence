# Communications Naming Tolerances v1

**Date**: `2026-03-08`  
**Status**: `active`  
**Validator**: [validate_metadata_naming.py](/Users/system/syncrescendence/operators/validators/validate_metadata_naming.py)  
**Scope**: `explicit communications naming tolerances`

## 1. Mechanism

The validator now carries a bounded exact-match tolerance table keyed by:

- repo-relative path
- warning note

This keeps the report-first scan non-blocking while preventing intentional lineage residue from surfacing as generic remediation debt.

The tolerance set is intentionally narrow:

- no wildcard path suppression
- no lane-wide suppression
- no suppression for `acceptable legacy debt`
- no suppression for `rename required`

## 2. Tolerated Findings

These `11` findings are explicitly tolerated.

### prompts

- `communications/prompts/COWORK-PERPLEXITY-PROTOTYPE-PROMPT.md`
  - note: `filename does not match lane naming convention`
  - rationale: intentional cowork lineage artifact name
- `communications/prompts/PACKET-GROK-cc79-harness-aider.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw-lineage harness packet
- `communications/prompts/PACKET-GROK-cc79-harness-claude_code.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw-lineage harness packet
- `communications/prompts/PACKET-GROK-cc79-harness-codex.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw-lineage harness packet
- `communications/prompts/PACKET-GROK-cc79-harness-gemini_cli.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw-lineage harness packet
- `communications/prompts/PACKET-GROK-cc79-harness-openclaw.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw-lineage harness packet
- `communications/prompts/PACKET-GROK-cc79-harness-opencode.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw-lineage harness packet
- `communications/prompts/PACKET-GROK-cc79-harness-openhands.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw-lineage harness packet

### responses

- `communications/responses/RESPONSE-GROK-cc79-harness-aider-raw.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw response artifact
- `communications/responses/RESPONSE-GROK-cc79-harness-claude_code-raw.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw response artifact
- `communications/responses/RESPONSE-GROK-cc79-harness-openhands-raw.md`
  - note: `file lacks expected lane metadata markers`
  - rationale: preserved raw response artifact

## 3. Active Visibility Boundaries

This tolerance table does not cover the triaged remediation buckets from [COMMUNICATIONS-NAMING-TRIAGE-v1.md](/Users/system/syncrescendence/orchestration/state/COMMUNICATIONS-NAMING-TRIAGE-v1.md):

- `6` strict-ready metadata items
- `4` rename-required items
- `3` acceptable legacy-debt items

At the time of codification, the live validator report shows that the `6` strict-ready metadata findings are no longer present in the workspace. The tolerance mechanism did not suppress them; they appear to have been normalized elsewhere.

The current active report therefore preserves visibility for:

- `4` rename-required items
- `3` acceptable legacy-debt items

Those active findings remain visible in [COMMUNICATIONS-NAMING-REPORT.md](/Users/system/syncrescendence/orchestration/state/COMMUNICATIONS-NAMING-REPORT.md) and continue to participate in strict-mode failure if warnings are enabled.
