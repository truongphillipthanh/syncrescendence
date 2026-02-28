# Extraction: SOURCE-20260204-013

**Source**: `SOURCE-20260204-x-article-zain_hoda-the_agent_will_eat_your_system_of_record.md`
**Atoms extracted**: 13
**Categories**: claim, concept, prediction

---

## Claim (10)

### ATOM-SOURCE-20260204-013-0002
**Lines**: 9-14
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.10, epistemic_stability=0.80

> Being the system of record is the most defensible position in enterprise software because it ensures all integrations and workflows route through it, making it the literal source of truth, regardless of UI or feature parity.

### ATOM-SOURCE-20260204-013-0004
**Lines**: 20-27
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Systems of record typically do not contain large amounts of data; for example, an entire Salesforce instance or Jira history might only be a few megabytes to a few gigabytes, often smaller than a single video file.

### ATOM-SOURCE-20260204-013-0005
**Lines**: 29-32
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.80

> Historically, the small size of data in systems of record didn't matter because the data was trapped within the application's interface, fusing the application and data together.

### ATOM-SOURCE-20260204-013-0006
**Lines**: 34-34
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.70, actionability=0.40, epistemic_stability=0.40

> AI agents break the assumption that data is trapped within an application's interface.

### ATOM-SOURCE-20260204-013-0007
**Lines**: 39-42
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> To be useful, an AI agent requires access to enterprise systems like CRM, project management tools, and documentation via API credentials to look up data, update records, and take actions.

### ATOM-SOURCE-20260204-013-0009
**Lines**: 53-59
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.30, epistemic_stability=0.30

> Once an AI agent has a complete, synchronized copy of the data and becomes the primary interaction layer, the original system of record primarily functions as a write endpoint where data is created before being pulled into the agent's context.

### ATOM-SOURCE-20260204-013-0010
**Lines**: 61-64
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.30, epistemic_stability=0.30

> Implementing aggressive rate limits or restricting API access to keep data trapped within a system of record is a losing strategy against AI agents.

### ATOM-SOURCE-20260204-013-0011
**Lines**: 69-71
**Context**: speculation / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.40, epistemic_stability=0.30

> If an AI agent faces rate limits, it will build a caching layer, pulling data, storing it locally, and syncing periodically, effectively delaying the inevitable data replication.

### ATOM-SOURCE-20260204-013-0012
**Lines**: 73-77
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.40, epistemic_stability=0.30

> Once an AI agent has a cache, that cache becomes the de facto system of record because it is more current, faster to query, and where the agent (the primary interface) does its work.

### ATOM-SOURCE-20260204-013-0013
**Lines**: 79-79
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.30, epistemic_stability=0.30

> Systems of record that try to protect themselves with rate limits risk becoming irrelevant.

## Concept (1)

### ATOM-SOURCE-20260204-013-0001
**Lines**: 4-7
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.10, epistemic_stability=0.90

> A "system of record" in enterprise software refers to the authoritative source for a particular type of data, such as Salesforce for customer data or Workday for employee data.

## Prediction (2)

### ATOM-SOURCE-20260204-013-0003
**Lines**: 16-16
**Context**: speculation / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.20, epistemic_stability=0.30

> The defensible position of being the system of record is about to collapse.

### ATOM-SOURCE-20260204-013-0008
**Lines**: 46-49
**Context**: speculation / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.40, epistemic_stability=0.30

> Due to the small size of data in systems of record and permissive APIs, an AI agent can quickly pull a complete copy of all data within minutes or seconds.
