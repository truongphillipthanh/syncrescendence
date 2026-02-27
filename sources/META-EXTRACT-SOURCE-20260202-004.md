# Extraction: SOURCE-20260202-004

**Source**: `SOURCE-20260202-x-article-manthanguptaa-ai_engineering_roadmap_2026.md`
**Atoms extracted**: 16
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (6)

### ATOM-SOURCE-20260202-004-0005
**Lines**: 23-26
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Prompt engineering, using techniques like few-shot learning, chain-of-thought, and structured outputs, can significantly improve AI application results without model training.

### ATOM-SOURCE-20260202-004-0007
**Lines**: 34-37
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Retrieval Augmented Generation (RAG) is a common pattern for production AI applications that grounds LLMs in specific data, addressing knowledge cutoffs and hallucinations, and requires understanding chunking strategies, embedding models, vector databases, and retrieval metrics.

### ATOM-SOURCE-20260202-004-0009
**Lines**: 45-48
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Systematic evaluation and testing, including building eval datasets, choosing metrics (accuracy, helpfulness, safety), running A/B tests, and detecting regressions, are crucial for measuring and improving AI applications.

### ATOM-SOURCE-20260202-004-0011
**Lines**: 56-59
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.80

> Agents extend LLMs to perform actions like browsing the web, executing code, and querying databases, requiring an understanding of agent architectures (ReAct, function calling, planning), tool design, and failure modes.

### ATOM-SOURCE-20260202-004-0013
**Lines**: 67-70
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Structured outputs and data extraction, using techniques like JSON mode, function calling, and constrained generation, are essential for integrating LLM outputs with downstream systems and bridging conversational AI with software engineering.

### ATOM-SOURCE-20260202-004-0015
**Lines**: 78-81
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Implementing input/output guardrails, PII detection, content filtering, and adversarial testing is crucial for production AI deployment to prevent jailbreaking, harmful content, or sensitive information leaks.

## Concept (2)

### ATOM-SOURCE-20260202-004-0001
**Lines**: 6-8
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> AI Engineering is a distinct discipline from traditional Machine Learning Engineering, primarily focused on building applications atop foundation models rather than training models from scratch.

### ATOM-SOURCE-20260202-004-0003
**Lines**: 12-15
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Foundation models (e.g., GPT-5.2, Claude, Gemini, Llama) are pre-trained models that serve as the building blocks for modern AI applications, differing from traditional ML where models are trained from scratch.

## Framework (1)

### ATOM-SOURCE-20260202-004-0002
**Lines**: 10-79
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The AI Engineering Roadmap 2026 outlines nine key areas: Understanding Foundation Models, Prompt Engineering, Retrieval Augmented Generation (RAG), Evaluation and Testing, Agents and Tool Use, Structured Outputs and Data Extraction, Guardrails and Safety, Observability and Monitoring, and AI System Architecture.

## Praxis Hook (7)

### ATOM-SOURCE-20260202-004-0004
**Lines**: 17-20
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To understand foundation models, create a Python notebook to send the same 10 prompts to different models (e.g., Gemini API, Groq for Llama, OpenAI playground) and compare their responses for quality, speed, and style.

### ATOM-SOURCE-20260202-004-0006
**Lines**: 28-31
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To practice prompt engineering, pick a task (e.g., summarizing an article), write five different prompts (zero-shot, few-shot, chain-of-thought, persona-based, structured output), test each on 10 examples, and score results in a spreadsheet.

### ATOM-SOURCE-20260202-004-0008
**Lines**: 39-42
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Build a simple RAG app over 5-10 markdown notes or text files using an agentic framework with ChromaDB to split documents, embed them, and query with natural language.

### ATOM-SOURCE-20260202-004-0010
**Lines**: 50-53
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Create a simple evaluation script by making a JSON file with 20 question-answer pairs, then write a Python script to run a prompt against each question, compare outputs to expected answers (or use an LLM-as-judge), and print a score.

### ATOM-SOURCE-20260202-004-0012
**Lines**: 61-64
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Build a calculator agent using OpenAI function calling or an agentic framework, giving the LLM access to basic arithmetic functions to answer math questions.

### ATOM-SOURCE-20260202-004-0014
**Lines**: 72-75
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Create a recipe extractor that takes a recipe from a website and outputs structured JSON (ingredients, quantities, steps, times) using OpenAI's structured output feature.

### ATOM-SOURCE-20260202-004-0016
**Lines**: 83-85
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Wrap a chatbot with simple guards: check input for prompt injection attempts using keyword matching or a classifier, and check output for blocklisted words, logging flagged messages.
