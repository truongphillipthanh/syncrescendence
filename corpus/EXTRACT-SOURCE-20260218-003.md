# Extraction: SOURCE-20260218-003

**Source**: `SOURCE-20260218-x-article-boringmarketer-i_stopped_writing_better_skills_and_started_building_skill_architecture.md`
**Atoms extracted**: 6
**Categories**: claim, praxis_hook

---

## Claim (2)

### ATOM-SOURCE-20260218-003-0001
**Lines**: 4-7
**Context**: rebuttal / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Most people believe an AI skill is primarily a well-written instruction file, but the architecture surrounding these skills is where significant gains are made.

### ATOM-SOURCE-20260218-003-0003
**Lines**: 27-31
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Dumping all available brand memory into every AI skill does not improve output quality; instead, it leads to 'muddy' results because attention is finite.

## Praxis Hook (4)

### ATOM-SOURCE-20260218-003-0002
**Lines**: 15-23
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Implement persistent memory for AI skills by using a shared brand directory where specific profile files have single owners for overwriting (with diff and confirmation) and append files only grow without truncation.

### ATOM-SOURCE-20260218-003-0004
**Lines**: 33-43
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Employ a context matrix to score and selectively load context for AI skills, providing only what sharpens the skill and withholding everything else, along with using Time-To-Live (TTL) rules for context freshness (e.g., <7 days pass as-is, 7-30 days flag age, 30-90 days summary only, >90 days don't load).

### ATOM-SOURCE-20260218-003-0005
**Lines**: 48-53
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Establish schema contracts between AI skills using typed interfaces, so skills output structured artifacts (e.g., JSON Schema) that other skills can directly consume as input, enabling data flow and pipeline creation.

### ATOM-SOURCE-20260218-003-0006
**Lines**: 58-63
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Integrate learning loops into AI systems by asking for performance feedback after major deliverables (e.g., 'shipped as-is', 'minor edits', 'rewrote significantly'), logging answers, and having skills read these learnings to adapt and improve future outputs.
