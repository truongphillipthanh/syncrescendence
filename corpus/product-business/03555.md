# Extraction: SOURCE-20260205-009

**Source**: `SOURCE-20260205-x-article-jainarvind-how_do_you_build_a_context_graph.md`
**Atoms extracted**: 30
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (14)

### ATOM-SOURCE-20260205-009-0001
**Lines**: 3-4
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.20

> Context graphs are considered a "trillion-dollar opportunity" by investors like @JayaGup10 and @ashugarg in enterprise AI.

### ATOM-SOURCE-20260205-009-0002
**Lines**: 6-7
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.60

> AI models currently lack the process knowledge required to reliably automate work, despite being able to use tools.

### ATOM-SOURCE-20260205-009-0003
**Lines**: 7-8
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.60

> Systems of record capture decisions, but the actual work often occurs in less structured environments like meetings, chats, emails, and documents.

### ATOM-SOURCE-20260205-009-0004
**Lines**: 8-9
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.60

> Without a structured understanding of how work is performed, AI cannot reliably automate it.

### ATOM-SOURCE-20260205-009-0006
**Lines**: 30-32
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.60

> Current AI agents struggle with end-to-end processes or long-term tasks (spanning weeks or months) that necessitate synthesizing knowledge from multiple, disparate systems.

### ATOM-SOURCE-20260205-009-0007
**Lines**: 35-38
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.60

> Systems of record typically only display the current state and rarely capture execution variability or full historical context, leading to blind spots and suboptimal outcomes if relied upon solely.

### ATOM-SOURCE-20260205-009-0008
**Lines**: 40-42
**Context**: hypothesis / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.70

> An internal model of an organization's real processes, built from actual traces of actions (a context graph), serves as the best proxy for learning both the structure to follow and the intent behind the work.

### ATOM-SOURCE-20260205-009-0011
**Lines**: 59-61
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.60, actionability=0.50, epistemic_stability=0.60

> Modeling actions as first-class entities in a context graph allows for attaching predictive power to activity sequences, enabling suggestions for the next likely step without hard-coding flows.

### ATOM-SOURCE-20260205-009-0012
**Lines**: 64-66
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.30, actionability=0.50, epistemic_stability=0.60

> Layered on process paths, derived insights explain why one path differed from another, encoding a probable 'why' that can be fed to an agent at runtime.

### ATOM-SOURCE-20260205-009-0019
**Lines**: 101-102
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> Knowledge graphs are a key foundation for context graphs because activity signals alone are noisy and require the underlying knowledge graph to make them meaningful.

### ATOM-SOURCE-20260205-009-0023
**Lines**: 108-112
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> The system's context graph, which agents use as playbooks, is built by probabilistically viewing "what tends to happen," "in what order," and "why paths deviate," with timing used to determine process value (e.g., longer time for similar user groups suggests high value).

### ATOM-SOURCE-20260205-009-0026
**Lines**: 121-122
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The method of tagging incident transitions with IDs is not optimized for reasoning across thousands of incidents at once.

### ATOM-SOURCE-20260205-009-0027
**Lines**: 125-129
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> If agents run within the system, every agent run becomes a trace that the graph learns from, including tools called, order, inputs/outputs, success, efficiency, and user feedback.

### ATOM-SOURCE-20260205-009-0030
**Lines**: 137-139
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Successful agent runs reinforce desired patterns, becoming natural language playbooks, while runs needing intervention highlight anti-patterns requiring more context or better tool use.

## Concept (2)

### ATOM-SOURCE-20260205-009-0005
**Lines**: 19-21
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> A context graph is a model that connects enterprise entities (people, documents, tickets, systems) with the temporal traces of actions and events between them, surfacing actionable insights for AI to understand how work is done.

### ATOM-SOURCE-20260205-009-0009
**Lines**: 45-50
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> A context graph describes the flow of work by modeling 'how' change happens (behavior: who did what, in which apps, in what order, and with what effect) rather than just 'what' exists (traditional data and knowledge systems modeling things like customers, tickets, docs, people, systems).

## Framework (2)

### ATOM-SOURCE-20260205-009-0010
**Lines**: 52-57
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> In a context graph, 'actions' are first-class entities, represented as nodes (e.g., 'created,' 'viewed,' 'approved,' 'escalated,' 'commented on,' 'resolved' with timestamps and metadata) and edges representing causality and correlation (e.g., 'Message A' triggered 'Update B' at probability P).

### ATOM-SOURCE-20260205-009-0024
**Lines**: 114-116
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> A hybrid model for storing event data uses free-form text broken into smaller chunks with embedded entity IDs, rather than rigid pure graph structures or flexible but hard-to-navigate raw text.

## Praxis Hook (12)

### ATOM-SOURCE-20260205-009-0013
**Lines**: 68-70
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.40, actionability=0.70, epistemic_stability=0.60

> After an agent runs, its actions should become new traces for the context graph, allowing reinforcement learning to evaluate path optimality and identify future alternative paths.

### ATOM-SOURCE-20260205-009-0014
**Lines**: 74-78
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Building a context graph requires a foundation of deep connectors and observability, integrating at a document level with apps where work occurs (CRM, ticketing, chat, docs, email, calendars, code, dashboards, internal apps) and structured data.

### ATOM-SOURCE-20260205-009-0015
**Lines**: 85-87
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To build a context graph, capture all change events in an application, normalize them, and expose them as traces.

### ATOM-SOURCE-20260205-009-0016
**Lines**: 90-94
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> After crawling and indexing data, build a knowledge graph by running a machine learning pipeline to infer higher-level entities (projects, customers, products, teams, people) and their relationships (which docs, tickets, calls, dashboards belong to a given product or account).

### ATOM-SOURCE-20260205-009-0017
**Lines**: 90-99
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To analyze processes in aggregate, normalize personal graphs into sequences of anonymized steps, including action type, tool family, knowledge graph entities, derived process tags, and lightweight timing features/outcomes.

### ATOM-SOURCE-20260205-009-0018
**Lines**: 96-99
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Continuously feed activity signals (views, edits, comments) into the knowledge graph to understand information usage and collaboration patterns, enabling the system to recognize that entities like 'ACME Inc' in CRM and 'ACME' in support tickets refer to the same customer.

### ATOM-SOURCE-20260205-009-0020
**Lines**: 101-102
**Context**: method / limitation
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When abstracting process traces, exclude raw text (doc bodies, message text), user identifiers, or customer-specific secrets to preserve anonymity.

### ATOM-SOURCE-20260205-009-0021
**Lines**: 102-103
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Compute similarity between abstracted traces to identify processes that are likely the same.

### ATOM-SOURCE-20260205-009-0022
**Lines**: 105-106
**Context**: method / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Only consider a process pattern viable if it appears across at least 'k' distinct users and 'n' independent traces, dropping anything too rare to preserve anonymity.

### ATOM-SOURCE-20260205-009-0025
**Lines**: 118-121
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To enable agents to walk a process step-by-step, break down incidents into short segments marking transitions (e.g., "investigating" to "mitigating") by tagging them with IDs like incident_id=INC-123, channel_id=#p1-incidents, or action_type=escalated.

### ATOM-SOURCE-20260205-009-0028
**Lines**: 131-132
**Context**: method / limitation
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Agent learnings are scoped per enterprise and focus on how the agent uses tools, not on storing underlying content.

### ATOM-SOURCE-20260205-009-0029
**Lines**: 134-135
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Offline, replay agent traces and try alternative routes, scoring them on correctness, completeness, instruction following, and efficiency.
