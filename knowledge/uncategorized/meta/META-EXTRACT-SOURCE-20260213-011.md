# Extraction: SOURCE-20260213-011

**Source**: `SOURCE-20260213-x-article-legendaryy-your_agent_is_only_as_good_as_its_search.md`
**Atoms extracted**: 35
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (26)

### ATOM-SOURCE-20260213-011-0001
**Lines**: 15-16
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The quality of search context feeding LLMs is a more fundamental bottleneck for AI agents than the choice of LLM itself.

### ATOM-SOURCE-20260213-011-0002
**Lines**: 18-21
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> An agent with poor search capabilities cannot reason effectively, regardless of the underlying LLM's power, leading to hallucinations, looping, and poor user outcomes.

### ATOM-SOURCE-20260213-011-0003
**Lines**: 30-33
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> Brave's research indicates that a weaker open-weight model (Qwen3) combined with high-quality search context can outperform stronger models like ChatGPT, Perplexity, and Google AI Mode.

### ATOM-SOURCE-20260213-011-0004
**Lines**: 35-36
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> In a 1,500-query evaluation, Ask Brave (Qwen3 + LLM Context API) scored 4.66/5, surpassing ChatGPT (4.32), Google AI Mode (4.39), and Perplexity (4.01), with only Grok (4.71) scoring higher.

### ATOM-SOURCE-20260213-011-0005
**Lines**: 37-37
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Context quality is a more significant differentiator than model capability for AI agents.

### ATOM-SOURCE-20260213-011-0008
**Lines**: 53-53
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Brave's LLM Context API has a p90 latency under 600ms for the full pipeline (search + extraction + ranking) with less than 130ms overhead on top of normal search.

### ATOM-SOURCE-20260213-011-0010
**Lines**: 70-72
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Perplexity's citation tokens are now free on standard Sonar and Sonar Pro, which reduces per-query costs.

### ATOM-SOURCE-20260213-011-0011
**Lines**: 72-74
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.20, epistemic_stability=0.70

> Perplexity's total cost per query is difficult to predict due to its dependence on model choice, context size, and token volume, unlike flat-rate APIs.

### ATOM-SOURCE-20260213-011-0013
**Lines**: 79-80
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Exa 2.0 offers three tiers: Exa Fast (sub-350ms p50), Exa Auto (balances latency and quality), and Exa Deep (agentic multi-search, ~3.5s p50, highest quality), with Exa Instant pushing latency below 200ms for real-time applications.

### ATOM-SOURCE-20260213-011-0014
**Lines**: 84-88
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Firecrawl specializes in extraction, starting with a URL to retrieve all content from a page, including handling JavaScript rendering, pagination, authentication, CAPTCHAs, and multi-page workflows automatically.

### ATOM-SOURCE-20260213-011-0015
**Lines**: 88-88
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Firecrawl is open source and self-hostable.

### ATOM-SOURCE-20260213-011-0016
**Lines**: 88-91
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.20, epistemic_stability=0.60

> Firecrawl reported 77.2% coverage and 0.638 F1 quality in its own comparison testing, compared to Exa's 69.2% coverage and 0.508 F1.

### ATOM-SOURCE-20260213-011-0017
**Lines**: 91-92
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> Firecrawl's reported benchmarks are vendor-published and not independently audited.

### ATOM-SOURCE-20260213-011-0019
**Lines**: 95-97
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.60, actionability=0.30, epistemic_stability=0.90

> Firecrawl's pricing is flat and predictable at one credit per page, without depth multipliers or variable consumption.

### ATOM-SOURCE-20260213-011-0020
**Lines**: 97-98
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> At 100K pages monthly, Firecrawl costs $83, which is significantly less than Tavily's $500-800 for equivalent extraction.

### ATOM-SOURCE-20260213-011-0023
**Lines**: 139-141
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.80

> Brave's blog argues that scrapers are legally risky (citing Google v. SerpAPI), can be arbitrarily shut off, and cannot offer true Zero Data Retention because queries pass through a third party.

### ATOM-SOURCE-20260213-011-0024
**Lines**: 141-142
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.80

> Brave is positioning itself as the safe infrastructure choice for enterprise AI due to being the only western independent search index at scale outside Big Tech.

### ATOM-SOURCE-20260213-011-0025
**Lines**: 144-148
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Brave's LLM Context API is a purpose-built pipeline that searches an independent 35B-page index, extracts smart chunks from results, ranks them for relevance, and delivers them in a token-budget-controlled format for any LLM, all under 600ms.

### ATOM-SOURCE-20260213-011-0026
**Lines**: 147-150
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.20, epistemic_stability=0.70

> The search layer is becoming the primary differentiator for agent builders because LLMs are commoditizing and their performance is converging.

### ATOM-SOURCE-20260213-011-0027
**Lines**: 148-149
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.60

> An open-weight model with good search context outperformed frontier models with worse context in Brave's evaluation.

### ATOM-SOURCE-20260213-011-0028
**Lines**: 150-151
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.20, epistemic_stability=0.70

> The search API choice is now a product decision, not just an infrastructure one, due to its impact on LLM performance differentiation.

### ATOM-SOURCE-20260213-011-0029
**Lines**: 154-155
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.70

> The most effective agent stacks utilize a hybrid approach, routing different query types to different APIs.

### ATOM-SOURCE-20260213-011-0030
**Lines**: 158-159
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.70

> Using a multi-API approach can reduce costs by 40-60% compared to using a single provider for all agent search needs.

### ATOM-SOURCE-20260213-011-0031
**Lines**: 162-164
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.80

> Privacy and independence are now critical factors for enterprise AI teams, especially in regulated industries with sensitive query content.

### ATOM-SOURCE-20260213-011-0032
**Lines**: 164-165
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.80

> Brave's ZDR policy and SOC 2 attestation are competitive advantages for enterprise AI in regulated industries.

### ATOM-SOURCE-20260213-011-0033
**Lines**: 165-166
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> Firecrawl's open-source self-hosting option provides full data sovereignty for teams requiring it.

## Concept (5)

### ATOM-SOURCE-20260213-011-0007
**Lines**: 47-51
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> Brave's LLM Context API performs a full search on its independent index of 35+ billion pages, then extracts 'smart chunks' (clean text, structured data, JSON-LD, tables, code, forum discussions, YouTube captions) from pages in real-time, ranking them by relevance and compiling them into a token-efficient format for LLM consumption.

### ATOM-SOURCE-20260213-011-0009
**Lines**: 65-67
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> Tavily is a search API purpose-built for AI agents, offering four endpoints: Search (web discovery), Extract (content from URLs), Map (site structure), and Crawl (navigate and extract from entire sites).

### ATOM-SOURCE-20260213-011-0012
**Lines**: 77-78
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> Exa (formerly Metaphor) uses neural embeddings trained on its own index of tens of billions of pages to enable semantic search by meaning rather than keywords.

### ATOM-SOURCE-20260213-011-0018
**Lines**: 94-95
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Firecrawl is an extraction tool used after a search engine finds relevant URLs, rather than a search engine itself.

### ATOM-SOURCE-20260213-011-0022
**Lines**: 139-142
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Brave's LLM Context API is not a wrapper around other search engines, not bundled with a forced LLM, and not just a search endpoint.

## Framework (1)

### ATOM-SOURCE-20260213-011-0006
**Lines**: 41-43
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Five search APIs (Brave, Tavily, Exa, Perplexity, Firecrawl) offer different philosophies for integrating web content into LLMs: Brave (own index, LLM-optimized chunks, privacy-first), Tavily (agent-native, search + extract + crawl), Exa (neural semantic search), Perplexity (Sonar API, answers with citations), Firecrawl (extract-first, scrape anything, structured).

## Praxis Hook (3)

### ATOM-SOURCE-20260213-011-0021
**Lines**: 119-121
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> The optimal strategy for agent builders is to route different query types to different APIs based on their strengths, rather than picking a single API.

### ATOM-SOURCE-20260213-011-0034
**Lines**: 169-171
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> For agents running on OpenClaw, the Brave LLM Context API is the easiest path to high-quality web grounding, especially since Brave Search MCP server is already integrated.

### ATOM-SOURCE-20260213-011-0035
**Lines**: 171-171
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.70

> Combine Brave LLM Context API with Exa for research tasks and Firecrawl for deep extraction to create a more powerful agent stack.
