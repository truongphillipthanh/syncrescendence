# Extraction: SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills

**Source**: `SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills.md`
**Atoms extracted**: 15
**Categories**: analogy, claim, concept, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0005
**Lines**: 46-48
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> MCP is like a toolbox (hammer, screwdriver, wrench), while a Skill is like the instruction manual (when to use which tool, how to build things).

## Claim (5)

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0001
**Lines**: 4-6
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> MCP servers are not merely REST API wrappers; they require a different approach focused on agentic flow.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0003
**Lines**: 22-30
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> In an MCP setup, the LLM performs agentic navigation by parsing ambiguous requests, discovering available tools, deciding tool order, chaining calls, and synthesizing coherent answers, unlike traditional REST APIs where an application layer makes deterministic calls.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0006
**Lines**: 52-89
**Context**: anecdote / evidence
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.70

> Before Skills, tool docstrings in MCP servers became excessively long, attempting to cram both technical definitions and usage intelligence, leading to high token usage when loaded into the LLM's context.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0014
**Lines**: 227-235
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Proper separation of responsibilities in AI agent design leads to token efficiency (smaller docstrings reduce context window bloat), improved maintainability (workflow changes don't affect MCP code), increased reusability (one MCP can serve many Skills), greater clarity (technical definitions and business logic are distinct), and progressive disclosure (LLM loads full instructions only when needed).

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0015
**Lines**: 237-238
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Separating technical definitions (MCP) from usage intelligence (Skills) creates a scalable, maintainable, and efficient system for LLM tool use.

## Concept (4)

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0002
**Lines**: 8-12
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Agentic flow describes how an LLM navigates through tools, discovering what's available, understanding when to use each, and chaining them to accomplish complex tasks, similar to a developer exploring a codebase.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0004
**Lines**: 40-48
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Skills act as a guide for the LLM, sitting between the user and the MCP server, filtering and guiding input to help the LLM make better decisions about tool usage.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0007
**Lines**: 91-94
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The 'docstring problem' in MCP development arose from mixing two distinct concerns: the technical definition of what a function does and the usage intelligence of when/how/why to use it.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0013
**Lines**: 221-221
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> MCP (Multi-Component Pipeline) servers act as navigation frameworks for LLM agents, while Skills serve as user manuals guiding this navigation.

## Praxis Hook (5)

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0008
**Lines**: 99-110
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> MCP tools should be lean and focused solely on their technical contract (what the function does, its arguments, and returns), with usage intelligence delegated to Skill files.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0009
**Lines**: 112-220
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Skill files should handle all usage intelligence, guiding the LLM on workflows, patterns, when to use specific tools, and how tools relate to each other, providing rich context and business logic.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0010
**Lines**: 194-199
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When designing AI agent interactions, always validate city names (expanding abbreviations), consider time zones, provide context beyond raw numbers, and be proactive in mentioning extreme weather.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0011
**Lines**: 201-205
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.80

> Avoid redundant tool calls by using synthesis tools (e.g., `compare_weather` instead of multiple `get_current_weather` calls), clarify units (Celsius vs Fahrenheit), and use forecast tools for future-oriented questions.

### ATOM-SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills-0012
**Lines**: 209-215
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.70

> For troubleshooting 'City not found' in AI agents, try alternative spellings, nearby major cities, or ask the user for clarification. If 'Forecast unavailable', fall back to current weather and explain the limitation to the user.
