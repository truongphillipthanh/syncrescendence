# Extraction: SOURCE-20260208-008

**Source**: `SOURCE-20260208-x-article-nickspiska_-the_only_ai_agent_architecture_guide_youll_ever_need.md`
**Atoms extracted**: 97
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (24)

### ATOM-SOURCE-20260208-008-0001
**Lines**: 40-41
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Every custom AI agent, regardless of complexity, can be broken down into six distinct layers.

### ATOM-SOURCE-20260208-008-0004
**Lines**: 70-71
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The data layer is the foundational component for AI agents, influencing all subsequent architectural decisions.

### ATOM-SOURCE-20260208-008-0012
**Lines**: 117-118
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The data privacy decision (where data lives and who can see it) is the primary determinant for half of an AI agent's architecture.

### ATOM-SOURCE-20260208-008-0015
**Lines**: 131-132
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The Single Responsibility Principle is non-negotiable for agent tools; a tool that performs two functions should be separated into two distinct tools.

### ATOM-SOURCE-20260208-008-0017
**Lines**: 138-139
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Vague parameter descriptions in tools lead agents to make incorrect choices, while strong typing and clear documentation are crucial for reliable agent performance.

### ATOM-SOURCE-20260208-008-0019
**Lines**: 157-157
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> UV is designed for agent skill distribution, allowing scripts to be written once and run identically everywhere, with `uv lock` providing deterministic reproducibility.

### ATOM-SOURCE-20260208-008-0024
**Lines**: 193-195
**Context**: consensus / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Skills represent a paradigm shift, adopted by major platforms like Microsoft, OpenAI, Google, Cursor, and Goose, and are crucial for how agents perform.

### ATOM-SOURCE-20260208-008-0026
**Lines**: 203-204
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> A tool is a command to 'call this API,' whereas a skill is guidance on 'how an expert approaches this entire domain,' including tool usage, order, and potential issues.

### ATOM-SOURCE-20260208-008-0027
**Lines**: 208-209
**Context**: consensus / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Skills offer significantly more efficient context loading and lower token costs compared to tools, being 500x more efficient than MCP for large libraries.

### ATOM-SOURCE-20260208-008-0028
**Lines**: 215-216
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Enterprises require both tools for action capability and skills for reasoning strategy, as an agent with only tools lacks domain expertise, and one with only skills cannot execute.

### ATOM-SOURCE-20260208-008-0030
**Lines**: 227-229
**Context**: consensus / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> The `SKILL.md` file's YAML frontmatter (name, description, compatibility) loads as metadata (~100 bytes) at startup, and the full `SKILL.md` loads only when the agent determines the skill is relevant, with referenced resources loading on-demand.

### ATOM-SOURCE-20260208-008-0032
**Lines**: 242-244
**Context**: consensus / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Progressive disclosure allows an agent to access thousands of skills without context window bloat, achieving 500x more efficiency than traditional MCP servers that consume 50,000+ tokens of JSON schema upfront.

### ATOM-SOURCE-20260208-008-0036
**Lines**: 262-263
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Memory is the distinguishing factor between a helpful tool and a genuinely useful agent, as the session layer persists context and the memory layer enables recall, learning, and evolution.

### ATOM-SOURCE-20260208-008-0037
**Lines**: 265-265
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Without memory, every conversation an agent has starts from scratch, but with memory, the agent becomes smarter over time.

### ATOM-SOURCE-20260208-008-0047
**Lines**: 346-348
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> The choice of LLM and its orchestration significantly impacts an agent's cost and performance, with proper routing being crucial for efficiency.

### ATOM-SOURCE-20260208-008-0071
**Lines**: 479-481
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Multi-Agent with Subagents architecture, where a primary agent delegates to specialized subagents each with its own context window and tools, can significantly outperform single-agent systems; Anthropic research showed multi-agent Claude Opus 4 + Sonnet subagents outperformed single-agent Opus 4 by 90.2%.

### ATOM-SOURCE-20260208-008-0078
**Lines**: 506-506
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> An 'Early-stage company' AI agent stack can operate with a monthly cost of $50-200, primarily for LLM API costs.

### ATOM-SOURCE-20260208-008-0081
**Lines**: 541-541
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> An 'Enterprise Knowledge Worker' AI agent stack can cost between $2,000-10,000 monthly, covering infrastructure and API costs.

### ATOM-SOURCE-20260208-008-0084
**Lines**: 583-583
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> A 'Privacy-First Autonomous Agent' AI stack can cost $5,000-20,000 monthly, primarily due to GPU infrastructure and engineering time.

### ATOM-SOURCE-20260208-008-0087
**Lines**: 623-623
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> A 'No-Code Business Automator' AI stack can cost $100-500 monthly, covering platform subscription and per-use API costs.

### ATOM-SOURCE-20260208-008-0093
**Lines**: 652-652
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> A 'Multi-Channel Personal Assistant' AI stack can cost $10-70 monthly, covering API costs and running on existing hardware.

### ATOM-SOURCE-20260208-008-0095
**Lines**: 662-663
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Claude Opus 4.6 and Codex 5.3 AGENTS.md files provide persistent project knowledge without retrieval overhead.

### ATOM-SOURCE-20260208-008-0096
**Lines**: 662-663
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> pgvector leverages existing Postgres infrastructure.

### ATOM-SOURCE-20260208-008-0097
**Lines**: 662-663
**Context**: consensus / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Multi-model routing uses Claude for complex refactoring and Gemini Flash for quick completions.

## Concept (25)

### ATOM-SOURCE-20260208-008-0006
**Lines**: 78-80
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> Vector Databases store embeddings (mathematical representations of content) and retrieve them based on semantic meaning, enabling Retrieval Augmented Generation (RAG) for AI agents.

### ATOM-SOURCE-20260208-008-0009
**Lines**: 104-105
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> Graph Databases capture relationships between entities, useful for agents needing to answer 'how are these two things connected?' or traverse complex information webs.

### ATOM-SOURCE-20260208-008-0014
**Lines**: 129-129
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.60, epistemic_stability=0.70

> Tools are how agents interact with the outside world, each performing exactly one function, taking defined inputs, and producing predictable outputs.

### ATOM-SOURCE-20260208-008-0016
**Lines**: 136-136
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.80

> A well-designed tool is atomic (one operation), deterministic (predictable output), typed (JSON schema inputs/outputs), and least-privileged (minimum necessary permissions).

### ATOM-SOURCE-20260208-008-0021
**Lines**: 163-165
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> MCP (Model Context Protocol) is an open standard for connecting LLM clients to external tools and data sources, where an MCP server exposes tools via `tools/list` (discovery) and `tools/call` (execution) endpoints with JSON Schema contracts.

### ATOM-SOURCE-20260208-008-0025
**Lines**: 200-201
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Tools execute operations and return results, while skills inject domain expertise and behavioral guidance into an agent's reasoning.

### ATOM-SOURCE-20260208-008-0031
**Lines**: 236-240
**Context**: consensus / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Progressive disclosure in skills involves a three-tier loading model: metadata (name + description, ~100 bytes) always in context, full instructions (SKILL.md body) loaded when activated, and resources (scripts, templates, references) loaded on-demand.

### ATOM-SOURCE-20260208-008-0034
**Lines**: 250-252
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Memory is the distinguishing factor between a "helpful tool" and a "genuinely useful agent," enabling the agent to recall, learn, and evolve across interactions.

### ATOM-SOURCE-20260208-008-0040
**Lines**: 284-286
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Vector Search (Semantic Recovery) stores conversation turns and facts as embeddings, retrieving them by semantic similarity, making it suitable for broad recall queries like "find me something related to X."

### ATOM-SOURCE-20260208-008-0041
**Lines**: 288-290
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Knowledge Graphs (Structured Recovery) store entities and relationships with temporal metadata, excelling at queries about connections between entities (e.g., "how are X and Y connected?") and changes over time.

### ATOM-SOURCE-20260208-008-0055
**Lines**: 382-384
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> OpenRouter is a fully managed, zero-infrastructure solution for LLM routing that monitors provider health and automatically routes away from degraded providers, suitable for teams that prefer not to manage routing.

### ATOM-SOURCE-20260208-008-0056
**Lines**: 386-388
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> LiteLLM is an open-source, self-hostable proxy for LLM routing with Redis-based usage tracking and multiple routing strategies, ideal for teams desiring more control, and can use OpenRouter as a backend.

### ATOM-SOURCE-20260208-008-0057
**Lines**: 390-392
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Helicone is an observability layer for multi-model LLM deployments, offering an 8ms P50 latency overhead, native cost tracking, and Redis caching (up to 95% cost reduction on repeated queries), making it essential for production environments.

### ATOM-SOURCE-20260208-008-0061
**Lines**: 418-420
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The agent harness is the orchestration layer that manages the agent loop (prompt → reason → act → observe → repeat), coordinates tools and skills, and handles state management, binding all underlying components into a functioning system.

### ATOM-SOURCE-20260208-008-0062
**Lines**: 424-433
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Pi-Mono is a minimal, opinionated, open-source coding agent toolkit with four core tools (read, write, edit, bash), a system prompt under 1,000 tokens, and support for 20+ LLM providers, best for developers seeking minimal foundations to extend.

### ATOM-SOURCE-20260208-008-0063
**Lines**: 435-443
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The Claude Agent SDK is Anthropic's official SDK, featuring the same agent loop and tools system as Claude Code, available in Python and TypeScript, with automatic context management, message summarization, and native MCP support, best for production Claude deployments with security requirements.

### ATOM-SOURCE-20260208-008-0064
**Lines**: 445-453
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> MindStudio is a visual, no-code agent builder offering access to 200+ models and 1,000+ pre-built integrations, with an average build time of 15 minutes to 1 hour, making it suitable for business users, rapid prototyping, and non-technical teams.

### ATOM-SOURCE-20260208-008-0065
**Lines**: 455-463
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> OpenClaw is a free, open-source (MIT), self-hosted agent that connects to messaging platforms (WhatsApp, Telegram, Discord, Slack), offers 100+ pre-configured skills, and uses Semantic Snapshots for web automation with 100x fewer tokens than screenshots, ideal for multi-channel agents and self-hosting.

### ATOM-SOURCE-20260208-008-0066
**Lines**: 467-467
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> CrewAI is an agent orchestration framework supporting multi-agent, role-based teams with over 100 built-in tools, performing 5.76x faster than LangGraph for certain tasks.

### ATOM-SOURCE-20260208-008-0067
**Lines**: 469-470
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> LangGraph is a low-level, DAG-based orchestration framework from LangChain, providing durable execution with failure recovery and human-in-the-loop capabilities with state inspection.

### ATOM-SOURCE-20260208-008-0068
**Lines**: 472-472
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Dify is an open-source platform that integrates a visual workflow builder, RAG engine, agent capabilities, and model management.

### ATOM-SOURCE-20260208-008-0070
**Lines**: 476-477
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> A Single Agent architecture involves one agent handling all tools, effective for up to 10-15 tools and well-bounded tasks due to its simplicity in building and debugging.

### ATOM-SOURCE-20260208-008-0072
**Lines**: 483-485
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The Router Pattern in agent architecture uses a lightweight agent to classify incoming requests and dispatch them to specialist agents, each handling a specific domain, ensuring clean separation of concerns.

### ATOM-SOURCE-20260208-008-0074
**Lines**: 487-488
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The Pipeline Pattern involves sequential agents, where each agent performs one step and the output of one becomes the input to the next, suitable for workflows with clear stages.

### ATOM-SOURCE-20260208-008-0076
**Lines**: 490-492
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> Human-in-the-Loop is an agent architecture pattern where the agent proposes actions at critical checkpoints, and a human approves, modifies, or rejects them, which is essential for high-stakes decisions (e.g., money, legal, customer-facing communication).

## Framework (20)

### ATOM-SOURCE-20260208-008-0002
**Lines**: 40-60
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> The Six-Layer Agent Stack for AI agents consists of: AGENT HARNESS (orchestration), LLM (reasoning), SKILLS (domain expertise), SESSION & MEMORY (context persistence), TOOLS (integrations), and DATA (personalized foundation). Each layer depends on the one beneath it.

### ATOM-SOURCE-20260208-008-0007
**Lines**: 82-94
**Context**: method / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Key vector databases include Pinecone (managed cloud, enterprise RAG), Qdrant (self-hosted/cloud, privacy-first), Weaviate (self-hosted/cloud, hybrid search), ChromaDB (local/embedded, prototyping), pgvector (PostgreSQL extension), and Milvus (distributed, billions of vectors).

### ATOM-SOURCE-20260208-008-0008
**Lines**: 96-102
**Context**: method / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Document Stores, such as MongoDB, Elasticsearch, and PostgreSQL, hold raw source material and structured metadata, often with native vector search capabilities.

### ATOM-SOURCE-20260208-008-0010
**Lines**: 107-113
**Context**: method / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Graph databases include Neo4j (knowledge graphs, Cypher), Amazon Neptune (AWS-native, Gremlin/SPARQL), and FalkorDB (lightweight, Cypher-compatible).

### ATOM-SOURCE-20260208-008-0013
**Lines**: 120-123
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Data residency and sensitivity dictate architectural choices: Public/Non-Sensitive data allows cloud-managed services; Proprietary but Non-Regulated data suggests self-hosting vector DBs with managed LLMs; Regulated data (HIPAA, SOC 2, GDPR) requires full self-hosting or private cloud with specific compliance implementations; Air-Gapped/Government data demands entirely on-premise, self-hosted open-source solutions.

### ATOM-SOURCE-20260208-008-0029
**Lines**: 220-225
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Skills are structured with a `SKILL.md` file (YAML frontmatter + markdown instructions), `scripts/` for executable code, `references/` for supporting documentation, `assets/` for templates/fonts/images, and `templates/` for structured prompts/forms.

### ATOM-SOURCE-20260208-008-0035
**Lines**: 259-270
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Agent memory can be categorized into five types: Working Memory (active context, single turn), Short-Term/Episodic (full conversation history, one session), Medium-Term (compressed summaries, days to weeks), Long-Term/Semantic (user preferences, persistent), and Procedural (agent behavior rules, permanent).

### ATOM-SOURCE-20260208-008-0043
**Lines**: 314-317
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Mem0 is a universal memory layer that offers self-improvement through priority scoring, resulting in a 26% improvement over OpenAI baseline, 91% lower p95 latency, and 90% token cost savings, making it an easy on-ramp for memory implementation.

### ATOM-SOURCE-20260208-008-0044
**Lines**: 319-322
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> Letta (formerly MemGPT) is an OS-inspired memory management system where agents actively edit their own memory, featuring Core Memory (always visible) and Archival Memory (unlimited, search-on-demand), enabling personality evolution and user learning.

### ATOM-SOURCE-20260208-008-0045
**Lines**: 324-326
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Zep / Graphiti is a temporal knowledge graph platform that provides real-time graph updates without batch recomputation and outperforms MemGPT by 18.5% accuracy in LongMemEval benchmarks.

### ATOM-SOURCE-20260208-008-0049
**Lines**: 358-358
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Three effective routing patterns for multi-model LLM orchestration are Task-Type Routing, Cascade Routing, and Fallback Routing.

### ATOM-SOURCE-20260208-008-0069
**Lines**: 474-474
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Key agent architecture patterns include Single Agent, Multi-Agent with Subagents, Router Pattern, Pipeline Pattern, and Human-in-the-Loop.

### ATOM-SOURCE-20260208-008-0073
**Lines**: 486-486
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> There are six distinct patterns for AI agent stacks, each tailored to different organizational needs and constraints: Early-stage company, Enterprise Knowledge Worker, Privacy-First Autonomous Agent, No-Code Business Automator, Multi-Channel Personal Assistant, and High-Performance Code Agent.

### ATOM-SOURCE-20260208-008-0075
**Lines**: 488-500
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The 'Early-stage company' AI agent stack is characterized by minimal infrastructure, fast iteration, and low cost, utilizing ChromaDB (embedded) + PostgreSQL for data, UV Python scripts + MCP servers for tools, community skills + custom SKILL.md files, JSON file sessions + ChromaDB for memory, a single vendor LLM (Claude or GPT-5.3), and Pi-Mono or Claude Agent SDK for the harness.

### ATOM-SOURCE-20260208-008-0080
**Lines**: 523-535
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> The 'Enterprise Knowledge Worker' AI agent stack is designed for mid-to-large companies with proprietary data and compliance requirements, featuring Qdrant (self-hosted) + MongoDB + Neo4j for data, Go CLI binaries + MCP servers + internal REST APIs for tools, custom and curated community skills, Mem0 (SOC 2 compliant) + Graphiti + PostgreSQL sessions for memory, multi-model LLM via LiteLLM, and LangGraph or CrewAI for the harness.

### ATOM-SOURCE-20260208-008-0083
**Lines**: 565-577
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.70

> The 'Privacy-First Autonomous Agent' AI stack is for regulated industries requiring strict data residency and autonomous operation, using self-hosted Qdrant + PostgreSQL + Neo4j for data, Go CLI binaries + local MCP servers for tools, fully custom skills, Letta (MemGPT) + local Graphiti + SQLite sessions for memory, self-hosted LLMs (Llama 4 Maverick or DeepSeek-V3 via vLLM), and OpenClaw or Pi-Mono for the harness.

### ATOM-SOURCE-20260208-008-0086
**Lines**: 607-617
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> The 'No-Code Business Automator' AI stack is for non-technical teams needing workflow automation, prioritizing speed-to-value, using managed cloud data (Pinecone or Weaviate), pre-built integrations (MindStudio or Dify), template-based skills, platform-managed sessions for memory, multi-model LLM via platform, and MindStudio or Dify as the harness.

### ATOM-SOURCE-20260208-008-0090
**Lines**: 640-650
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The 'Multi-Channel Personal Assistant' AI stack is for power users or small teams needing a personal AI assistant across messaging platforms with local control and privacy, using SQLite + local ChromaDB for data, OpenClaw's pre-configured skills + custom SKILL.md files, OpenClaw persistent memory + local ChromaDB for memory, any API LLM (Claude, GPT, or local Ollama), and OpenClaw as the harness.

### ATOM-SOURCE-20260208-008-0091
**Lines**: 647-649
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> A high-performance code agent for engineering teams integrates with development workflows, handles large codebases, and operates with minimal latency.

### ATOM-SOURCE-20260208-008-0092
**Lines**: 651-660
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> The stack for a high-performance code agent includes: pgvector and Git repositories for data; UV Python scripts, Go CLI tools, and MCP servers (GitHub, Jira, CI/CD) for tools; code-specific skills (refactoring, review, testing, documentation); JSON sessions, vector search over codebase, and AGENTS.md for project context for memory; Claude Sonnet (primary, highest SWE-bench) and Gemini Flash (fast iteration) for LLMs; and Claude Agent SDK or Pi-Mono for the harness.

## Praxis Hook (28)

### ATOM-SOURCE-20260208-008-0003
**Lines**: 62-64
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> When building an AI agent, start with the Data layer and work upwards through the stack, rather than starting with the LLM layer.

### ATOM-SOURCE-20260208-008-0005
**Lines**: 73-74
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Avoid rushing or skipping the data layer in AI agent development, as it often leads to costly re-architecting later.

### ATOM-SOURCE-20260208-008-0011
**Lines**: 112-125
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up a data layer, audit client data sources (types, volume, sensitivity), determine data residency requirements, select a compliance framework (SOC 2, HIPAA, GDPR, or none), choose a vector database based on scale and deployment, choose a document store for raw content and metadata, evaluate the need for a knowledge graph, design a chunking strategy (semantic preferred, with overlap), set up an embedding pipeline (model selection: OpenAI ada-002, Cohere, or self-hosted), implement encryption at rest (AES-256) and in transit (TLS 1.2+), define data retention and deletion policies, and set up an incremental update pipeline for ongoing ingestion.

### ATOM-SOURCE-20260208-008-0018
**Lines**: 143-146
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Python Tools via Astral UV allow for rapid development of self-contained Python scripts using PEP 723 inline metadata, where dependencies are declared within the script and `uv run` installs them in an ephemeral virtual environment, eliminating virtualenv management, requirements.txt, and dependency conflicts.

### ATOM-SOURCE-20260208-008-0020
**Lines**: 159-161
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Go CLI Tools compile to a single binary with zero runtime dependencies, and the Cobra framework can be used for CLI scaffolding, making them suitable for performance-critical applications and tight agent feedback loops at scale.

### ATOM-SOURCE-20260208-008-0022
**Lines**: 171-174
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Use UV Python scripts for rapid development, data processing, and API integrations, Go CLI binaries for performance-critical and cross-platform distribution, MCP servers for standardized integrations and multi-agent ecosystems, and HTTP callables for existing REST APIs and microservices.

### ATOM-SOURCE-20260208-008-0023
**Lines**: 179-189
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up the tools layer, inventory required integrations, classify each as a single-purpose tool, choose an implementation language per tool (UV Python for speed, Go for performance), define JSON schemas for all tool inputs and outputs, implement least-privilege credentials, set up an MCP server for tools needing standardized discovery, write clear tool documentation, create structured error handling patterns, test each tool in isolation, and set up a tool versioning strategy.

### ATOM-SOURCE-20260208-008-0033
**Lines**: 249-258
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up the skills layer, identify required domain expertise, audit existing community skills, write custom `SKILL.md` files for client-specific domains (keeping body under 500 lines), structure skills with `scripts/`, `references/`, and `templates/` subdirectories, implement progressive disclosure in the agent framework, test skill activation triggers, set up cross-platform distribution if needed, create a skill evaluation pipeline, and version control all skills alongside the codebase.

### ATOM-SOURCE-20260208-008-0038
**Lines**: 273-276
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For prototyping agent sessions, use JSON file-based persistence, where each session is a directory containing metadata, turn files, and accumulated agent state, offering simplicity, Git-friendliness, and easy debugging.

### ATOM-SOURCE-20260208-008-0039
**Lines**: 278-281
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For production agent sessions, use database-backed persistence, with options like SQLite for development, PostgreSQL for production ACID, Redis for sub-1ms latency, MongoDB for flexible schemas, or DynamoDB for AWS serverless environments.

### ATOM-SOURCE-20260208-008-0042
**Lines**: 293-295
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For production, combine vector search for broad semantic recall with knowledge graphs for structured relationship queries and session files for conversation continuity to achieve hybrid memory.

### ATOM-SOURCE-20260208-008-0046
**Lines**: 331-341
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up agent memory, define requirements, choose session persistence (JSON for dev, DB for prod), select a vector database for semantic memory, evaluate the need for a knowledge graph, choose a memory framework (Mem0, Zep, Letta), implement hierarchical summarization, set up consolidation, define cleanup policies, implement multi-agent sharing, and test recovery accuracy.

### ATOM-SOURCE-20260208-008-0048
**Lines**: 354-356
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> To optimize costs and availability in LLM deployments, route requests to the best model for each task, which can lead to up to 85% cost savings and higher availability through fallback mechanisms.

### ATOM-SOURCE-20260208-008-0050
**Lines**: 360-366
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Implement Task-Type Routing by assigning specific LLMs to different agent activities: Classification/summarization to Gemini Flash, Code generation to OpenAI Codex, Complex reasoning to Claude Opus, Multimodal tasks to Gemini Pro, and Real-time chat to the fastest available model (e.g., xAI for socials).

### ATOM-SOURCE-20260208-008-0051
**Lines**: 366-368
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When starting out, choose a single vendor LLM (e.g., Claude-only via Claude Agent SDK) for simpler implementation, deterministic performance, and easier compliance, accepting the risk of vendor lock-in.

### ATOM-SOURCE-20260208-008-0052
**Lines**: 368-374
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Utilize Cascade Routing to reduce costs while maintaining quality: start with a small, cheap model with a confidence threshold (e.g., 0.7), escalate to a mid-tier model if uncertain, and finally to a frontier model if still uncertain. This can achieve 85% cost reduction with 95% quality maintenance.

### ATOM-SOURCE-20260208-008-0053
**Lines**: 370-370
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For production, implement multi-model orchestration to route requests to the best model for each task, which can lead to up to 85% cost savings and higher availability through fallback.

### ATOM-SOURCE-20260208-008-0054
**Lines**: 376-378
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Implement Fallback Routing by defining a primary, secondary, and tertiary model, monitoring provider health every 30 seconds, and using automatic circuit breaking on failures to ensure agent uptime.

### ATOM-SOURCE-20260208-008-0058
**Lines**: 395-397
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Self-host LLM infrastructure when processing millions of tokens/day (where cost savings outweigh hardware costs), data cannot leave your infrastructure, or operating in regulated industries.

### ATOM-SOURCE-20260208-008-0059
**Lines**: 399-400
**Context**: method / limitation
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Avoid self-hosting LLM infrastructure for prototyping, low volume (under 100K tokens/day), limited MLOps expertise, or when proprietary model capabilities are required.

### ATOM-SOURCE-20260208-008-0060
**Lines**: 403-414
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up an LLM layer, profile workload types, decide on single-vendor vs. multi-model, set up routing infrastructure (OpenRouter or LiteLLM) if multi-model, define model assignments per task, implement cascade routing with confidence thresholds (if cost-sensitive), set up fallback chains with health monitoring, implement rate limiting per provider, set up observability (Helicone or equivalent), provision GPU infrastructure and set up vLLM if self-hosting, and benchmark the routing strategy on held-out traffic before production.

### ATOM-SOURCE-20260208-008-0077
**Lines**: 495-505
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up an agent harness, assess team technical capability, evaluate single-agent vs. multi-agent requirements, select a framework based on LLM strategy, implement the agent loop with error handling and retry logic, configure tool and skill discovery, set up session management and memory integration, implement human-in-the-loop checkpoints for high-stakes actions, set up logging and observability, define agent permission boundaries, test end-to-end, and set up CI/CD for deployment and skill updates.

### ATOM-SOURCE-20260208-008-0079
**Lines**: 508-518
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To set up an 'Early-stage company' AI agent stack, one should: set up PostgreSQL, initialize embedded ChromaDB, create UV Python tools, write 2-3 custom SKILL.md files, configure Pi-Mono or Claude Agent SDK with a single model, implement JSON session files, deploy to a single server/container, set up basic logging, test end-to-end, and monitor API costs weekly.

### ATOM-SOURCE-20260208-008-0082
**Lines**: 543-560
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To set up an 'Enterprise Knowledge Worker' AI agent stack, one should: deploy Qdrant, MongoDB, and Neo4j, build a data ingestion pipeline, develop Go CLI tools, set up MCP servers, write enterprise SKILL.md files, deploy SOC 2 compliant Mem0 and Graphiti, configure LiteLLM, implement role-based access controls, set up Helicone, deploy a multi-agent system, implement human-in-the-loop, set up audit logging, run security reviews, and create disaster recovery procedures.

### ATOM-SOURCE-20260208-008-0085
**Lines**: 585-602
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To set up a 'Privacy-First Autonomous Agent' AI stack, one should: provision GPU infrastructure, deploy vLLM, set up encrypted Qdrant and PostgreSQL with row-level security, deploy Neo4j Community Edition, build all tools as Go CLI binaries, write comprehensive custom skills, deploy Letta and local Graphiti, configure OpenClaw or Pi-Mono with local model endpoints, implement network isolation, set up comprehensive audit logging, conduct security and compliance reviews, create operational runbooks, set up monitoring and alerting, and document data flow diagrams.

### ATOM-SOURCE-20260208-008-0088
**Lines**: 625-635
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To set up a 'No-Code Business Automator' AI stack, one should: sign up for MindStudio or Dify Cloud, identify top automation workflows, connect existing business tools, select LLM models per workflow, build the first agent using a template, test with scenarios, set up webhook triggers, train the team, set up usage alerts and cost monitoring, and iterate based on feedback.

### ATOM-SOURCE-20260208-008-0089
**Lines**: 633-643
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To set up a high-performance code agent, deploy OpenClaw, configure messaging channels, set up LLM API keys (or local Ollama), enable pre-built skills, write custom SKILL.md files for personal workflows, set up scheduled automations, test cross-channel conversations, and set up automatic updates and backups.

### ATOM-SOURCE-20260208-008-0094
**Lines**: 654-655
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To set up a 'Multi-Channel Personal Assistant' AI stack, one should: set up a server or repurpose existing hardware, deploy OpenClaw, configure messaging channels, set up LLM API keys (or local Ollama), enable desired pre-built skills, write custom SKILL.md files, set up scheduled automations, test cross-channel conversations, and set up automatic updates and backups.
