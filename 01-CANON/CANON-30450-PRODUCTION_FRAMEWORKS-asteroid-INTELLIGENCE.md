---
id: CANON-30450
name: Production Frameworks
identity: PRODUCTION_FRAMEWORKS
tier: CANON
type: asteroid
chain: INTELLIGENCE
parent: CANON-30400
version: 2.0.0
status: canonical
created: 2025-12-30
updated: 2025-12-30
synopsis: Production agent frameworks, SDK comparisons, MCP/A2A protocols, tool integration, and deployment patterns.
---

# CANON-30450: PRODUCTION FRAMEWORKS
## Intelligence Chain Asteroid

**Parent**: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] (Agentic Architecture)

---

## PURPOSE

This asteroid provides detailed specifications for production agent frameworks and deployment infrastructure. Where [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] surveys the framework landscape, this document provides implementation depth for SDK selection, protocol implementation, and production deployment patterns.

---

## PART I: FRAMEWORK CONSOLIDATION (2025)

### 1.1 The End of Experimental Toolkits

March through October 2025 witnessed dramatic framework consolidation, ending the era of experimental agent toolkits. Production-ready frameworks with stability commitments replaced research-oriented prototypes.

### 1.2 Major Framework Releases

```yaml
Framework_Timeline:
  March_2025:
    OpenAI_Agents_SDK:
      - Replaced experimental Swarm
      - Four minimal abstractions: Agents, Handoffs, Guardrails, Sessions
      - Provider-agnostic: 100+ LLMs supported
      - Built-in tracing, automatic conversation history
      - Pydantic-validated function tools
      - Deployments: Coinbase, Klarna (2/3 of support), Clay (10x growth)

  April_2025:
    Google_ADK:
      - Multi-agent from inception
      - Hierarchical composition: LLM agents + workflow agents + custom agents
      - Bidirectional audio-video streaming (v0.2.0)
      - Native Vertex AI integration
      - 200+ models via LiteLLM
      - Native MCP + A2A support
      - Powers: Agentspace, Customer Engagement Suite

  October_2025:
    Microsoft_Agent_Framework:
      - Unified AutoGen + Semantic Kernel
      - Ends years of fragmentation
      - Functional agents in <20 lines of code
      - Microsoft Orleans for event-driven distributed architecture
      - Azure AI Foundry integration
      - Python and .NET support
      - AutoGen and Semantic Kernel enter maintenance mode

  Throughout_2025:
    LangGraph:
      - Python v0.6.10 stable
      - 1.0.0 alpha September 2025
      - Lowest latency and token usage in benchmarks
      - February: Supervisor pattern for hierarchical systems
      - June: Node-level caching, deferred execution
      - August: Dynamic tool calling, LangSmith trace mode
```

---

## PART II: FRAMEWORK COMPARISON

### 2.1 Architectural Approaches

| Framework | Philosophy | Core Pattern |
|-----------|------------|--------------|
| **LangGraph** | Graph-based stateful DAG | Explicit control, deterministic paths |
| **OpenAI SDK** | Minimal abstractions | Provider-agnostic simplicity |
| **Google ADK** | Hierarchical composition | Multi-agent from inception |
| **Microsoft AF** | Unified enterprise | Azure ecosystem integration |
| **CrewAI** | Role-based teamwork | Human team simulation |

### 2.2 LangGraph

```yaml
LangGraph:
  philosophy: Model agent interactions as stateful, directed graph

  characteristics:
    - State persists between nodes by design
    - Human-in-the-loop at any node
    - Explicit control and observability
    - Complex branching and loops supported
    - Steeper learning curve
    - More verbose syntax

  best_for:
    - Production-grade enterprise workflows
    - Tasks requiring loops, branching, approval
    - Lowest latency requirements
    - Complex conditional branching

  performance:
    - Lowest latency in benchmarks
    - Lowest token usage
    - Predefined deterministic paths minimize LLM invocations
```

### 2.3 OpenAI Agents SDK

```yaml
OpenAI_SDK:
  philosophy: Minimal abstractions, broad compatibility

  abstractions:
    - Agents: Core autonomous units
    - Handoffs: Control transfer between agents
    - Guardrails: Safety constraints
    - Sessions: Context management

  characteristics:
    - Provider-agnostic (100+ LLMs)
    - Built-in tracing
    - Automatic conversation history
    - Pydantic validation

  best_for:
    - Simplicity priority
    - Broad model support
    - Minimal abstractions preferred
```

### 2.4 Google ADK

```yaml
Google_ADK:
  philosophy: Multi-agent from inception, interoperability leader

  composition:
    - LLM agents: Foundation model powered
    - Workflow agents: Sequential, parallel, loop patterns
    - Custom agents: User-defined behavior

  capabilities:
    - Bidirectional audio-video streaming
    - Native Vertex AI integration
    - 200+ models via LiteLLM
    - Native MCP + A2A support

  best_for:
    - Multi-model deployments
    - Interoperability priority
    - Google Cloud ecosystem
    - Audio/video agent interactions
```

### 2.5 Microsoft Agent Framework

```yaml
Microsoft_AF:
  philosophy: Unified enterprise solution

  unification:
    - AutoGen: Research-oriented dynamic orchestration
    - Semantic Kernel: Enterprise SDK
    - Combined: Single production path

  architecture:
    - Microsoft Orleans: Event-driven distributed
    - Azure AI Foundry: Native integration
    - Cross-platform: Python + .NET

  best_for:
    - Azure ecosystem
    - Enterprise governance requirements
    - .NET integration
    - Existing Microsoft stack
```

### 2.6 CrewAI

```yaml
CrewAI:
  philosophy: Role-based teamwork simulating human teams

  model:
    - Agents have roles, goals, backstories
    - Sequential or hierarchical orchestration
    - State passed as task outputs
    - Human-in-the-loop supported (less granular)

  characteristics:
    - Intuitive and easy to learn
    - Rapid development for business workflows
    - Less flexible for cyclical/dynamic tasks
    - Less explicit orchestration

  best_for:
    - Business process automation
    - Marketing, sales, research workflows
    - Clearly defined roles
    - Rapid prototyping
```

---

## PART III: PROTOCOL SPECIFICATIONS

### 3.1 Model Context Protocol (MCP)

```yaml
MCP:
  purpose: Universal translation layer between agents and external systems
  standard: JSON-RPC 2.0-based
  open_sourced: November 2024 by Anthropic

  mechanism:
    - Tools and agents implement common interface independently
    - Eliminates N×M integration problem
    - Standardized schemas for capability discovery
    - Automatic invocation without hard-coded integration

  june_2025_specification:
    - OAuth Resource Server classification
    - RFC 8707 Resource Indicators for token protection
    - Async operation support

  adoption_timeline:
    March_2025: OpenAI
    April_2025: Google DeepMind
    May_2025: Microsoft Copilot Studio (GA)
    2025: AWS steering committee
    IDE: Zed, VS Code, JetBrains

  analogy: "USB-C for AI applications"
  servers: Thousands available
```

### 3.2 Agent-to-Agent Protocol (A2A)

```yaml
A2A:
  purpose: Peer agent communication and collaboration
  launched: April 2025 by Google

  backers: 150+ organizations
    major:
      - Microsoft, Salesforce, Atlassian, PayPal
      - Accenture, BCG, Deloitte, McKinsey, PwC

  components:
    AgentCards: Self-description documents for discovery
    Task_Lifecycle:
      states: submitted → working → completed
    Modality_Negotiation: text, forms, audio, video

  version_0.3 (July 2025):
    - gRPC support
    - Security card signatures

  governance: Linux Foundation (June 2025)

  framework_support:
    - LangGraph
    - ADK
    - CrewAI

  relationship: Complements MCP
    MCP: Agent-to-tool interactions
    A2A: Agent-to-agent collaboration
```

### 3.3 Additional Protocols

| Protocol | Use Case | Characteristics |
|----------|----------|-----------------|
| **ACP** | Manufacturing, autonomous vehicles | Low-latency, high-reliability sessions |
| **ANP** | Decentralized networks | W3C DIDs, JSON-LD graphs |

---

## PART IV: TOOL INTEGRATION

### 4.1 Anthropic Claude API Updates (May 2025)

```yaml
Claude_API_Updates:
  code_execution_tools:
    - Python sandbox for data analysis
    - Visualization capabilities

  MCP_connectors:
    - Direct API integration to remote servers
    - No client code required

  Files_API:
    - Upload once
    - Reference repeatedly across sessions

  extended_prompt_caching:
    - 1-hour TTL (12x improvement)
    - 90% cost reduction
    - 85% latency reduction
```

### 4.2 Claude Code (October 2025)

```yaml
Claude_Code_Updates:
  - Remote MCP server support
  - Plugin system packaging:
    - Slash commands
    - Subagents
    - MCP servers
    - Safety hooks

  growth: 160% active user base (post Claude 4 launch)
```

### 4.3 Tool Integration Architecture

```yaml
Tool_Integration:
  discovery:
    - Capability registry with operations and specs
    - Semantic search by description
    - Dynamic addition/removal of tools

  invocation:
    - Standardized request-response pattern
    - JSON or function-call format
    - Normalized result handling

  reliability:
    - Automatic retries on failure
    - Circuit breakers for flaky dependencies
    - Schema validation for inputs/outputs

  benefit: |
    Standard integration layer means developers don't
    reinvent error handling for every tool call.
```

---

## PART V: EVALUATION FRAMEWORKS

### 5.1 CLASSic Framework (ICLR 2025)

```yaml
CLASSic:
  source: Aisera
  innovation: Beyond accuracy to five critical dimensions

  dimensions:
    Cost:
      - API usage
      - Token consumption
      - Infrastructure overhead
      finding: Domain-specific agents dramatically cheaper

    Latency:
      - End-to-end response time
      finding: Specialized agents 2.1s vs longer for general

    Accuracy:
      - Workflow execution correctness
      finding: Domain-specific 82.7% on IT ops

    Stability:
      - Consistency across diverse inputs
      finding: Specialized agents 72% stability

    Security:
      - Resilience to adversarial inputs
      status: Increasingly critical

  validation: Specialized agents outperform across all five dimensions
```

### 5.2 Trajectory Evaluation (Vertex AI)

```yaml
Trajectory_Evaluation:
  source: Google Cloud (January 2025)
  focus: Reasoning quality over final answers

  metrics:
    exact_match: Perfect action sequence
    in_order_match: Correct sequence with possible extra steps
    tool_correctness: Appropriate tool selection
    tool_efficiency: Minimize unnecessary calls
    reasoning_quality: Step-by-step logic
    error_recovery: Adaptation to feedback

  benefit: Identify where agents succeed or fail in multi-step processes
```

### 5.3 Benchmark Ecosystem

| Benchmark | Focus | Scope |
|-----------|-------|-------|
| **AgentBench** | LLM-as-Agent reasoning | 8 environments, 5-50 turns |
| **WebArena** | Web tasks | 812 templated tasks |
| **GAIA** | General AI assistants | 466 human-annotated tasks |
| **BrowseComp** | Information retrieval | Complex multi-site research |
| **SWE-bench** | GitHub issue resolution | Real software engineering |
| **OSWorld** | OS-level tasks | Extremely challenging (5% best) |

---

## PART VI: PRODUCTION DEPLOYMENT PATTERNS

### 6.1 Enterprise Adoption (Stack Overflow 2025)

```yaml
Adoption_Patterns:
  orchestration_tools:
    Ollama: 51%
    LangChain: 33%

  memory_data:
    Redis: 43%
    ChromaDB: 20%
    pgvector: 18%

  observability:
    Grafana_Prometheus: 43%
    Sentry: 32%

  concerns:
    accuracy: 87%
    security_privacy: 81%

  active_users: 48%

  impact:
    reduced_time: 70%
    productivity: 69%
    collaboration: 17% (lowest)
```

### 6.2 Deployment Infrastructure

```yaml
Deployment_Stack:
  observability:
    - OpenTelemetry traces
    - Prompt logging
    - Tool invocation tracking
    - Token usage monitoring
    - Orchestration step visibility

  tracing:
    - Correlation IDs across subagents
    - End-to-end request tracking
    - Latency breakdowns

  monitoring:
    - Real-time dashboards (Phoenix, GALILEO)
    - Anomaly detection
    - Automated rollbacks

  deployment:
    - Feature flags for gradual rollout
    - Stage environments
    - A/B testing capability
```

### 6.3 Failure Patterns and Mitigations

| Pattern | Cause | Mitigation |
|---------|-------|------------|
| Over-engineering | 18-month builds launching obsolete | Iterative deployment |
| State mismanagement | Duplicate processing, data loss | Explicit state architecture |
| Poor handoff design | Customer confusion, abandonment | Clear transition protocols |
| Distribution shift | Benchmark ≠ production | Realistic test environments |

---

## PART VII: FRAMEWORK SELECTION GUIDE

### 7.1 Decision Matrix

```yaml
Selection_Guide:
  raw_performance:
    choose: LangGraph
    reason: Lowest latency, lowest token usage

  rapid_development:
    choose: CrewAI
    reason: Intuitive role-based abstractions

  azure_ecosystem:
    choose: Microsoft Agent Framework
    reason: Native integration, enterprise governance

  multi_model_interop:
    choose: Google ADK
    reason: MCP + A2A native, 200+ models

  simplicity_first:
    choose: OpenAI SDK
    reason: Minimal abstractions, broad support

  complex_branching:
    choose: LangGraph
    reason: Explicit control, hierarchical structures
```

### 7.2 Migration Considerations

```yaml
Migration_Notes:
  from_AutoGen:
    path: Microsoft Agent Framework
    timeline: AutoGen enters maintenance mode
    action: Plan migration before features freeze

  from_Semantic_Kernel:
    path: Microsoft Agent Framework
    timeline: Semantic Kernel enters maintenance mode
    action: Evaluate new Agent Framework API surface

  from_experimental_tools:
    path: Any production framework
    action: Assess stability commitments before selection
```

---

## PART VIII: INDUSTRY DEPLOYMENTS

### 8.1 Financial Services

```yaml
Financial_Deployments:
  JPMorgan_COIN:
    scope: 50,000+ commercial agreements annually
    achievement: 360,000 human hours → seconds
    features: Quantum-resistant security

  Algorithmic_Trading:
    adoption: 75% of equity trades
    capabilities: ESG compliance, crypto arbitrage

  Cybersecurity:
    Darktrace_Antigena: Autonomous threat detection/neutralization (milliseconds)
```

### 8.2 Healthcare

```yaml
Healthcare_Deployments:
  Seattle_Children:
    function: Process clinical notes, literature, images
    output: Evidence-based clinical information

  eClinicalWorks:
    function: Patient data extraction from documents

  Microsoft_Cancer_Care:
    challenge: <1% of patients access multidisciplinary care
    solution: Multi-agent coordination
    result: Hours of prep → minutes of automation
```

### 8.3 Technology

```yaml
Technology_Deployments:
  Netlify_Agent_Runners (October 2025):
    - Claude Code, Codex, Gemini integration
    - Live production applications

  Azure_AI_Foundry (September 2025):
    - Enterprise-ready deployment
    - Deep Research integration

  Salesforce_Agentforce:
    - 70% tier-1 support automation
    - 2025 launch
```

---

## PART IX: THE GEN AI PARADOX

### 9.1 The Problem

> **78% of companies deploy agents. 80% report no material earnings impact.**

### 9.2 The Resolution

```yaml
Paradox_Resolution:
  horizontal_copilots:
    - Easily deployed
    - Task assistance across roles
    - Proliferate widely
    - Low organizational impact

  vertical_transformation:
    - Function-specific process transformation
    - High organizational impact
    - Stuck in pilots
    - Requires CEO-led initiatives

  successful_examples:
    Northwestern_Mutual: Insurance underwriting automation
    Teladoc_Health: Virtual care coordination
    AXA: Claims processing reinvention

  success_requirements:
    - CEO-led strategic programs
    - Cross-functional transformation squads
    - Process reinvention (not task automation)
    - Industrialized delivery
```

---

## PART X: FORWARD TRAJECTORY

### 10.1 Upcoming Releases

```yaml
Upcoming:
  November_2025:
    MCP_Specification:
      - Enhanced async operation support
      - Improved scalability features
      - Refined authorization schemes

  Q1_2026:
    Microsoft_Agent_Framework_GA:
      - Production stability commitments
      - End of breaking changes era

  Q2_2025:
    Semantic_Kernel_Process_Framework_GA:
      - Long-running business processes
      - Dapr and Orleans integration
```

### 10.2 Trajectory Summary

```yaml
Trajectory:
  protocols:
    - MCP + A2A as dual interoperability standards
    - Linux Foundation and AWS institutional backing
    - Network effects increasing value with adoption

  architectures:
    - Multi-agent as default (not single-agent)
    - Specialists over generalists
    - Hybrid hub-spoke with mesh

  operational:
    - Observability, security, cost efficiency differentiate
    - Feature proliferation → operational excellence
    - Test-first, continuous monitoring
```

---

## SATELLITES

None. This is a leaf asteroid.

---

## VERSION HISTORY

**Version 1.0.0** (December 2025): Genesis establishment
- Canonized from Technology Lunar - Agents.md
- Production frameworks documented
- Protocol specifications detailed
