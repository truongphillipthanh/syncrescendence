---
id: [[CANON-30450-PRODUCTION_FRAMEWORKS-asteroid-INTELLIGENCE]]
name: Production Frameworks
identity: PRODUCTION_FRAMEWORKS
tier: CANON
type: asteroid
chain: INTELLIGENCE
parent: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]
version: 2.0.0
status: canonical
created: 2025-12-30
updated: 2025-12-30
synopsis: Production agent frameworks, SDK comparisons, MCP/A2A protocols, tool integration, and deployment patterns.
---

# CANON-30450-PRODUCTION_FRAMEWORKS-asteroid-INTELLIGENCE (SN Format)

**Note**: This is a Semantic Notation compressed version.
**Original**: 2,003 words, 17,116 characters

---

TERM IntelligenceChainAsteroid:
    sutra: "Parent: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] (Agentic Architecture)  ---"
    gloss:
        **Parent**: [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] (Agentic Architecture)

---
end


TERM PURPOSE:
    sutra: "This asteroid provides detailed specifications for production agent frameworks and deployment inf..."
    gloss:
        This asteroid provides detailed specifications for production agent frameworks and deployment infrastructure. Where [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]] surveys the framework landscape, this document provides implementation depth for SDK selection, protocol implementation, and production deployment patterns.

---
end


TERM 11TheEndofExperimentalToolkits:
    sutra: "March through October 2025 witnessed dramatic framework consolidation, ending the era of experime..."
    gloss:
        March through October 2025 witnessed dramatic framework consolidation, ending the era of experimental agent toolkits. Production-ready frameworks with stability commitments replaced research-oriented prototypes.
end


TERM 12MajorFrameworkReleases:
    sutra: "``yaml Framework_Timeline:   March_2025:     OpenAI_Agents_SDK:       - Replaced experimental Swa..."
    gloss:
        ```yaml
Framework_Timeline:
  March_2025:
    OpenAI_Agents_SDK:
      - Replaced experimental Swarm
      - Four minimal abstractions: Agents, Handoffs, Guardrails, Sessions
      - Provider-agnostic: 100+ LLMs supported
      - Built-in tracing, automatic conversation history
      - Pydantic-vali...
end


TERM 21ArchitecturalApproaches:
    sutra: "| Framework | Philosophy | Core Pattern | |-----------|------------|--------------| | LangGraph |..."
    gloss:
        | Framework | Philosophy | Core Pattern |
|-----------|------------|--------------|
| **LangGraph** | Graph-based stateful DAG | Explicit control, deterministic paths |
| **OpenAI SDK** | Minimal abstractions | Provider-agnostic simplicity |
| **Google ADK** | Hierarchical composition | Multi-agent...
end


TERM 22LangGraph:
    sutra: "``yaml LangGraph:   philosophy: Model agent interactions as stateful, directed graph    character..."
    gloss:
        ```yaml
LangGraph:
  philosophy: Model agent interactions as stateful, directed graph

  characteristics:
    - State persists between nodes by design
    - Human-in-the-loop at any node
    - Explicit control and observability
    - Complex branching and loops supported
    - Steeper learning curve...
end


TERM 23OpenAIAgentsSDK:
    sutra: "``yaml OpenAI_SDK:   philosophy: Minimal abstractions, broad compatibility    abstractions:     -..."
    gloss:
        ```yaml
OpenAI_SDK:
  philosophy: Minimal abstractions, broad compatibility

  abstractions:
    - Agents: Core autonomous units
    - Handoffs: Control transfer between agents
    - Guardrails: Safety constraints
    - Sessions: Context management

  characteristics:
    - Provider-agnostic (100+ L...
end


TERM 24GoogleADK:
    sutra: "``yaml Google_ADK:   philosophy: Multi-agent from inception, interoperability leader    compositi..."
    gloss:
        ```yaml
Google_ADK:
  philosophy: Multi-agent from inception, interoperability leader

  composition:
    - LLM agents: Foundation model powered
    - Workflow agents: Sequential, parallel, loop patterns
    - Custom agents: User-defined behavior

  capabilities:
    - Bidirectional audio-video stre...
end


TERM 25MicrosoftAgentFramework:
    sutra: "``yaml Microsoft_AF:   philosophy: Unified enterprise solution    unification:     - AutoGen: Res..."
    gloss:
        ```yaml
Microsoft_AF:
  philosophy: Unified enterprise solution

  unification:
    - AutoGen: Research-oriented dynamic orchestration
    - Semantic Kernel: Enterprise SDK
    - Combined: Single production path

  architecture:
    - Microsoft Orleans: Event-driven distributed
    - Azure AI Foundr...
end


TERM 26CrewAI:
    sutra: "``yaml CrewAI:   philosophy: Role-based teamwork simulating human teams    model:     - Agents ha..."
    gloss:
        ```yaml
CrewAI:
  philosophy: Role-based teamwork simulating human teams

  model:
    - Agents have roles, goals, backstories
    - Sequential or hierarchical orchestration
    - State passed as task outputs
    - Human-in-the-loop supported (less granular)

  characteristics:
    - Intuitive and e...
end


TERM 31ModelContextProtocolMCP:
    sutra: "``yaml MCP:   purpose: Universal translation layer between agents and external systems   standard..."
    gloss:
        ```yaml
MCP:
  purpose: Universal translation layer between agents and external systems
  standard: JSON-RPC 2.0-based
  open_sourced: November 2024 by Anthropic

  mechanism:
    - Tools and agents implement common interface independently
    - Eliminates N×M integration problem
    - Standardized...
end


TERM 32AgenttoAgentProtocolA2A:
    sutra: "``yaml A2A:   purpose: Peer agent communication and collaboration   launched: April 2025 by Googl..."
    gloss:
        ```yaml
A2A:
  purpose: Peer agent communication and collaboration
  launched: April 2025 by Google

  backers: 150+ organizations
    major:
      - Microsoft, Salesforce, Atlassian, PayPal
      - Accenture, BCG, Deloitte, McKinsey, PwC

  components:
    AgentCards: Self-description documents for...
end


TERM 33AdditionalProtocols:
    sutra: "| Protocol | Use Case | Characteristics | |----------|----------|-----------------| | ACP | Manuf..."
    gloss:
        | Protocol | Use Case | Characteristics |
|----------|----------|-----------------|
| **ACP** | Manufacturing, autonomous vehicles | Low-latency, high-reliability sessions |
| **ANP** | Decentralized networks | W3C DIDs, JSON-LD graphs |

---
end


TERM 41AnthropicClaudeAPIUpdatesMay2025:
    sutra: "``yaml Claude_API_Updates:   code_execution_tools:     - Python sandbox for data analysis     - V..."
    gloss:
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

  ex...
end


TERM 42ClaudeCodeOctober2025:
    sutra: "``yaml Claude_Code_Updates:   - Remote MCP server support   - Plugin system packaging:     - Slas..."
    gloss:
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
end


TERM 43ToolIntegrationArchitecture:
    sutra: "``yaml Tool_Integration:   discovery:     - Capability registry with operations and specs     - S..."
    gloss:
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

  re...
end


TERM 51CLASSicFrameworkICLR2025:
    sutra: "``yaml CLASSic:   source: Aisera   innovation: Beyond accuracy to five critical dimensions    dim..."
    gloss:
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
      - End-to-end response time...
end


TERM 52TrajectoryEvaluationVertexAI:
    sutra: "``yaml Trajectory_Evaluation:   source: Google Cloud (January 2025)   focus: Reasoning quality ov..."
    gloss:
        ```yaml
Trajectory_Evaluation:
  source: Google Cloud (January 2025)
  focus: Reasoning quality over final answers

  metrics:
    exact_match: Perfect action sequence
    in_order_match: Correct sequence with possible extra steps
    tool_correctness: Appropriate tool selection
    tool_efficiency:...
end


TERM 53BenchmarkEcosystem:
    sutra: "| Benchmark | Focus | Scope | |-----------|-------|-------| | AgentBench | LLM-as-Agent reasoning..."
    gloss:
        | Benchmark | Focus | Scope |
|-----------|-------|-------|
| **AgentBench** | LLM-as-Agent reasoning | 8 environments, 5-50 turns |
| **WebArena** | Web tasks | 812 templated tasks |
| **GAIA** | General AI assistants | 466 human-annotated tasks |
| **BrowseComp** | Information retrieval | Complex...
end


TERM 61EnterpriseAdoptionStackOverflow2025:
    sutra: "``yaml Adoption_Patterns:   orchestration_tools:     Ollama: 51%     LangChain: 33%    memory_dat..."
    gloss:
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

  impac...
end


TERM 62DeploymentInfrastructure:
    sutra: "``yaml Deployment_Stack:   observability:     - OpenTelemetry traces     - Prompt logging     - T..."
    gloss:
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
    - Latency breakdowns...
end


TERM 63FailurePatternsandMitigations:
    sutra: "| Pattern | Cause | Mitigation | |---------|-------|------------| | Over-engineering | 18-month b..."
    gloss:
        | Pattern | Cause | Mitigation |
|---------|-------|------------|
| Over-engineering | 18-month builds launching obsolete | Iterative deployment |
| State mismanagement | Duplicate processing, data loss | Explicit state architecture |
| Poor handoff design | Customer confusion, abandonment | Clear t...
end


TERM 71DecisionMatrix:
    sutra: "``yaml Selection_Guide:   raw_performance:     choose: LangGraph     reason: Lowest latency, lowe..."
    gloss:
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
    reason: Native integration, enterprise...
end


TERM 72MigrationConsiderations:
    sutra: "``yaml Migration_Notes:   from_AutoGen:     path: Microsoft Agent Framework     timeline: AutoGen..."
    gloss:
        ```yaml
Migration_Notes:
  from_AutoGen:
    path: Microsoft Agent Framework
    timeline: AutoGen enters maintenance mode
    action: Plan migration before features freeze

  from_Semantic_Kernel:
    path: Microsoft Agent Framework
    timeline: Semantic Kernel enters maintenance mode
    action:...
end


TERM 81FinancialServices:
    sutra: "``yaml Financial_Deployments:   JPMorgan_COIN:     scope: 50,000+ commercial agreements annually ..."
    gloss:
        ```yaml
Financial_Deployments:
  JPMorgan_COIN:
    scope: 50,000+ commercial agreements annually
    achievement: 360,000 human hours → seconds
    features: Quantum-resistant security

  Algorithmic_Trading:
    adoption: 75% of equity trades
    capabilities: ESG compliance, crypto arbitrage

  C...
end


TERM 82Healthcare:
    sutra: "``yaml Healthcare_Deployments:   Seattle_Children:     function: Process clinical notes, literatu..."
    gloss:
        ```yaml
Healthcare_Deployments:
  Seattle_Children:
    function: Process clinical notes, literature, images
    output: Evidence-based clinical information

  eClinicalWorks:
    function: Patient data extraction from documents

  Microsoft_Cancer_Care:
    challenge: <1% of patients access multidi...
end


TERM 83Technology:
    sutra: "``yaml Technology_Deployments:   Netlify_Agent_Runners (October 2025):     - Claude Code, Codex, ..."
    gloss:
        ```yaml
Technology_Deployments:
  Netlify_Agent_Runners (October 2025):
    - Claude Code, Codex, Gemini integration
    - Live production applications

  Azure_AI_Foundry (September 2025):
    - Enterprise-ready deployment
    - Deep Research integration

  Salesforce_Agentforce:
    - 70% tier-1 s...
end


TERM 91TheProblem:
    sutra: "> 78% of companies deploy agents"
    gloss:
        > **78% of companies deploy agents. 80% report no material earnings impact.**
end


TERM 92TheResolution:
    sutra: "``yaml Paradox_Resolution:   horizontal_copilots:     - Easily deployed     - Task assistance acr..."
    gloss:
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
    -...
end


TERM 101UpcomingReleases:
    sutra: "``yaml Upcoming:   November_2025:     MCP_Specification:       - Enhanced async operation support..."
    gloss:
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
      - End of breaking changes era...
end


TERM 102TrajectorySummary:
    sutra: "``yaml Trajectory:   protocols:     - MCP + A2A as dual interoperability standards     - Linux Fo..."
    gloss:
        ```yaml
Trajectory:
  protocols:
    - MCP + A2A as dual interoperability standards
    - Linux Foundation and AWS institutional backing
    - Network effects increasing value with adoption

  architectures:
    - Multi-agent as default (not single-agent)
    - Specialists over generalists
    - Hyb...
end


TERM SATELLITES:
    sutra: "None"
    gloss:
        None. This is a leaf asteroid.

---
end


TERM VERSIONHISTORY:
    sutra: "Version 1.0.0 (December 2025): Genesis establishment - Canonized from Technology Lunar - Agents.m..."
    gloss:
        **Version 1.0.0** (December 2025): Genesis establishment
- Canonized from Technology Lunar - Agents.md
- Production frameworks documented
- Protocol specifications detailed
end
