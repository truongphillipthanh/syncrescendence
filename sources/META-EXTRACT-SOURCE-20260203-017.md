# Extraction: SOURCE-20260203-017

**Source**: `SOURCE-20260203-x-article-getfoundry-unbrowse_100x_faster_than_browser_automation.md`
**Atoms extracted**: 19
**Categories**: claim, concept, framework, praxis_hook, prediction

---

## Claim (9)

### ATOM-SOURCE-20260203-017-0001
**Lines**: 10-14
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Traditional browser automation for AI agents is slow, taking 10-45 seconds per action, and unreliable, failing 15-30% of the time, while consuming significant resources (500MB+ RAM for a headless browser).

### ATOM-SOURCE-20260203-017-0002
**Lines**: 16-16
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> Many web actions performed by browser automation are essentially API calls disguised as button interactions.

### ATOM-SOURCE-20260203-017-0003
**Lines**: 30-30
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> A website's internal API call can return data in 200ms, whereas browser automation for the same task can take 12 seconds.

### ATOM-SOURCE-20260203-017-0004
**Lines**: 32-32
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> A workflow involving 10 web actions can take over 2 minutes with browser automation, compared to 2 seconds with direct API calls.

### ATOM-SOURCE-20260203-017-0010
**Lines**: 95-95
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.70

> Unbrowse enhances OpenClaw agents by making their web interactions 100 times faster.

### ATOM-SOURCE-20260203-017-0011
**Lines**: 101-102
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> An agent's first visit to a website uses a browser, but subsequent visits leverage direct API calls, allowing the agent to become faster with more use.

### ATOM-SOURCE-20260203-017-0014
**Lines**: 120-124
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The current methods for AI agent web access are problematic: official APIs are rare (~1% of websites), MCP servers require manual building, and browser automation is slow, brittle, and expensive.

### ATOM-SOURCE-20260203-017-0015
**Lines**: 126-126
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.70

> 99% of the web is currently only accessible to agents through slow browser automation, which Unbrowse aims to unlock at API speed.

### ATOM-SOURCE-20260203-017-0016
**Lines**: 128-130
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Every website inherently possesses internal APIs, as modern web applications like React apps and SPAs fetch data from backends, with the browser merely serving as a rendering layer.

## Concept (3)

### ATOM-SOURCE-20260203-017-0005
**Lines**: 45-45
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> The browser acts as a Graphical User Interface (GUI) on top of underlying API calls, which agents do not necessarily need.

### ATOM-SOURCE-20260203-017-0012
**Lines**: 105-112
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.40, actionability=0.60, epistemic_stability=0.50

> Every API captured by Unbrowse becomes a 'skill' – a reusable package that any OpenClaw agent can install, enabling an ecosystem where agents can share and trade these capabilities.

### ATOM-SOURCE-20260203-017-0017
**Lines**: 131-135
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> Browser automation involves a redundant four-step process: launching a browser, rendering HTML from JSON, scraping HTML back into data, and clicking buttons that send API requests, when a single direct API call could suffice.

## Framework (1)

### ATOM-SOURCE-20260203-017-0009
**Lines**: 90-93
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Unbrowse is a plugin for OpenClaw, an open-source framework designed to enable AI agents to perform actions like sending emails, managing calendars, deploying code, and monitoring chats autonomously.

## Praxis Hook (4)

### ATOM-SOURCE-20260203-017-0006
**Lines**: 65-66
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Unbrowse operates by observing website network traffic via Chrome DevTools Protocol during a single browse session, capturing all XHR, fetch, WebSocket, auth headers, and cookies.

### ATOM-SOURCE-20260203-017-0007
**Lines**: 68-69
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Unbrowse analyzes captured network traffic to identify real API endpoints, automatically detect authentication methods (Bearer tokens, cookies, API keys), infer parameters, and cluster endpoints by resource.

### ATOM-SOURCE-20260203-017-0008
**Lines**: 71-72
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Unbrowse generates a complete API skill, including documented endpoints, a TypeScript client, and authentication configuration, enabling agents to directly call these APIs without needing a browser for subsequent interactions.

### ATOM-SOURCE-20260203-017-0019
**Lines**: 144-145
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> OpenClaw and Unbrowse are open-source projects, installable via `npm install -g openclaw` and `openclaw plugins install @getfoundry/unbrowse-openclaw` respectively.

## Prediction (2)

### ATOM-SOURCE-20260203-017-0013
**Lines**: 114-116
**Context**: speculation / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.50, epistemic_stability=0.30

> A marketplace will be built where agents can share and trade skills using x402 micropayments, allowing agents to acquire capabilities autonomously without human approval.

### ATOM-SOURCE-20260203-017-0018
**Lines**: 139-139
**Context**: speculation / claim
**Tension**: novelty=0.80, consensus_pressure=0.10, contradiction_load=0.10, speculation_risk=0.90, actionability=0.40, epistemic_stability=0.20

> $FDRY (2ZiSPGncrkwWa6GBZB4EDtsfq7HEWwkwsPFzEXieXjNL) will be used as currency to incentivize contributions to the agentic web.
