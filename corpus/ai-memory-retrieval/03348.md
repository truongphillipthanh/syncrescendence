# Extraction: SOURCE-20260201-002

**Source**: `SOURCE-20260201-x-article-ashpreetbedi-dash_open_sourcing_openais_in_house_data_agent.md`
**Atoms extracted**: 15
**Categories**: claim, concept, framework, praxis_hook, prediction

---

## Claim (6)

### ATOM-SOURCE-20260201-002-0001
**Lines**: 7-8
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> OpenAI recently published details on how they built their internal data agent, which includes 6 layers of context, a self-learning memory system, and production lessons.

### ATOM-SOURCE-20260201-002-0002
**Lines**: 9-9
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.60

> The OpenAI data agent is one of the best enterprise use-cases for agents.

### ATOM-SOURCE-20260201-002-0003
**Lines**: 12-12
**Context**: consensus / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> OpenAI's architecture for their data agent validates the 'gpu-poor continuous learning' approach.

### ATOM-SOURCE-20260201-002-0005
**Lines**: 20-20
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Without sufficient context, even strong models hallucinate column names, miss type quirks, and ignore tribal knowledge.

### ATOM-SOURCE-20260201-002-0006
**Lines**: 21-22
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> Most Text-to-SQL agents are stateless, leading to repeated mistakes because each session starts fresh.

### ATOM-SOURCE-20260201-002-0014
**Lines**: 87-87
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> Data agents are currently one of the best enterprise use cases for AI.

## Concept (2)

### ATOM-SOURCE-20260201-002-0004
**Lines**: 16-16
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> Dash is a self-learning data agent that grounds its answers in 6 layers of context and improves with every run.

### ATOM-SOURCE-20260201-002-0010
**Lines**: 53-60
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.40, actionability=0.70, epistemic_stability=0.50

> Gpu-poor continuous learning is a method where a system learns through trial and error without requiring GPUs, exemplified by Dash's learning machine configuration.

## Framework (2)

### ATOM-SOURCE-20260201-002-0007
**Lines**: 24-32
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Dash implements 6 layers of context to address issues of hallucination and statelessness in Text-to-SQL agents: Table Usage, Human Annotations, Query Patterns, Institutional Knowledge, Memory, and Runtime Context.

### ATOM-SOURCE-20260201-002-0009
**Lines**: 39-51
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> Dash learns through two complementary systems: Static Knowledge (curated by teams, including validated queries, business context, schemas, data quality notes, metric definitions, tribal knowledge, and gotchas) and Continuous Learning (patterns discovered through trial and error, improving with usage).

## Praxis Hook (4)

### ATOM-SOURCE-20260201-002-0008
**Lines**: 34-35
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> A data agent can retrieve relevant context at runtime via hybrid search, use this to generate grounded SQL, and then use the results to deliver insights.

### ATOM-SOURCE-20260201-002-0011
**Lines**: 64-70
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up Dash, clone the repository, copy `example.env` to `.env` and add your `OPENAI_API_KEY`, then use `docker compose up -d --build` to start services, and `docker exec` commands to load sample data and knowledge.

### ATOM-SOURCE-20260201-002-0012
**Lines**: 74-77
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To connect to the Dash UI, open os.agno.com, add a local OS connection to http://localhost:8000, and then connect.

### ATOM-SOURCE-20260201-002-0013
**Lines**: 81-84
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Dash includes an evaluation suite supporting string matching, LLM grading, and golden SQL comparison, which can be run via `docker exec -it dash-api python -m dash.evals.run_evals` with optional flags for grading and golden SQL.

## Prediction (1)

### ATOM-SOURCE-20260201-002-0015
**Lines**: 88-88
**Context**: speculation / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.60, actionability=0.50, epistemic_stability=0.60

> Every company over a certain size should have a data agent.
