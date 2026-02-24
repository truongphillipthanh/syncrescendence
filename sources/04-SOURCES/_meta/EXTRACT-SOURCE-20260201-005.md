# Extraction: SOURCE-20260201-005

**Source**: `SOURCE-20260201-x-article-rohit4verse-what_makes_an_engineer_when_everyone_can_vibe_code.md`
**Atoms extracted**: 15
**Categories**: claim, concept, praxis_hook

---

## Claim (7)

### ATOM-SOURCE-20260201-005-0001
**Lines**: 19-20
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> As AI has lowered the entry barrier to coding, the demand for true engineering has never been higher.

### ATOM-SOURCE-20260201-005-0002
**Lines**: 20-21
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Companies and users prioritize accountability for the result over who writes the code.

### ATOM-SOURCE-20260201-005-0006
**Lines**: 56-58
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> An engineer's code doesn't fail less often, but they know how to fix issues, minimize loss, and quickly restore system functionality.

### ATOM-SOURCE-20260201-005-0007
**Lines**: 62-65
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.40, actionability=0.30, epistemic_stability=0.50

> LLMs tend to provide complex one-liners or obscure libraries, optimized for academic answers, which vibe coders may accept and ship without critical evaluation.

### ATOM-SOURCE-20260201-005-0009
**Lines**: 87-87
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> It is more important to keep code working forever than to get it done once.

### ATOM-SOURCE-20260201-005-0013
**Lines**: 130-130
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The best engineering work happens before a single line of code is even written.

### ATOM-SOURCE-20260201-005-0014
**Lines**: 150-151
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> AI lives in a utopia of infinite resources and zero latency, while reality has friction and budgets.

## Concept (5)

### ATOM-SOURCE-20260201-005-0003
**Lines**: 28-28
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Code is a liability, not an asset.

### ATOM-SOURCE-20260201-005-0004
**Lines**: 29-31
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> A 'vibe coder' generates features without considering future-proofing or potential issues like data breaches, prioritizing only the current problem statement.

### ATOM-SOURCE-20260201-005-0005
**Lines**: 41-51
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> An 'engineer' builds systems with guardrails for future-proofing, addressing edge cases like rate limiting, session management, logging, password resets, error handling that doesn't leak user existence, monitoring alerts, and documented runbooks for security incidents.

### ATOM-SOURCE-20260201-005-0010
**Lines**: 91-96
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> Vibe coders exhibit linear thinking, leading AI to generate simple, fast solutions that can result in spaghetti code, while engineers employ systems thinking to consider the broader ecosystem.

### ATOM-SOURCE-20260201-005-0012
**Lines**: 127-129
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> A 'vibe coder' acts as a waiter, taking orders and delivering solutions, while an 'engineer' acts as a consultant, questioning details, limitations, and premises to frame the problem correctly.

## Praxis Hook (3)

### ATOM-SOURCE-20260201-005-0008
**Lines**: 78-84
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> For date parsing, engineers should rely on boring, tested native `Intl.DateTimeFormat` or lightweight libraries like date-fns, write explicit parsing logic with clear error messages, and add unit tests for edge cases (leap years, timezone boundaries, February 29th, Daylight Saving Time transitions).

### ATOM-SOURCE-20260201-005-0011
**Lines**: 112-118
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> When exporting large datasets to CSV, an engineer should implement a paginated background job, generate CSVs server-side in chunks to save memory, email the user when the download is ready, store the file in S3 with an expiring security link, and add monitoring for job queue health.

### ATOM-SOURCE-20260201-005-0015
**Lines**: 156-160
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To manage costs for AI-powered image recognition, an engineer should implement client-side image validation, batch processing during off-peak hours, cache results for similar images, use smaller/cheaper models for initial triage, and only use expensive models for confusing edge cases.
