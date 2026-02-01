# **OPENAI ECOSYSTEM — FORENSIC CATALOG \+ ARCHITECTURE MAP (ANTI-OMISSION EDITION)**

## **0\. AS-OF SNAPSHOT: THE STATE OF THE INFRASTRUCTURE (JANUARY 12, 2026\)**

### **0.1 The Strategic Pivot: From Chatbot to "Compute Utility"**

As of January 12, 2026, the operational reality of OpenAI has shifted fundamentally from a consumer-facing chatbot company to a provider of heavy-compute "reasoning" and "agentic" infrastructure. While the public still perceives "ChatGPT" as a text interface, the forensic reality reveals a platform that has bifurcated into two distinct operational modes: the low-latency conversational layer (GPT-5.1/Instant) and the high-latency, high-compute agentic layer (o3-pro, Deep Research, Computer Use).

This shift is not merely marketing; it is architectural. The deprecation of the stateless **Assistants API** in favor of the stateful **Responses API** signals that OpenAI intends to own the "execution loop" of AI agents.1 In a modern AI constellation, particularly one orchestrated by Anthropic's Claude, OpenAI is no longer the primary "brain" for nuance or architectural planning—a role Claude 4.5/Opus retains due to superior codebase context retention—but rather the "muscle." OpenAI has positioned itself as the high-capability **Action Utility Layer**, providing the raw infrastructure for web browsing, sandboxed computer interaction, and massive-scale reasoning verification.

### **0.2 The "Pro" Divergence and Compute Inequality**

A critical forensic finding in the last 90 days is the hardening of the "Pro" tier wall. Access to the most capable models—specifically **o3-pro** and **GPT-5.2 Pro**—is now strictly gated behind the $200/month subscription or high-tier API spend (Tier 4/5).3 This has created a functional "compute inequality" where standard developers (Tier 1-3) and consumers (Plus) are accessing a fundamentally different class of intelligence than enterprise or high-spend users. The "Pro" models are priced at a premium that suggests they utilize massive chain-of-thought ensembles, with output costs reaching $168.00 per million tokens for GPT-5.2 Pro, compared to just $14.00 for the standard flagship.3

### **0.3 The "Sunset" Crisis**

The ecosystem is currently in a state of aggressive consolidation. The most urgent signal is the impending sunset of **GPT-4o** API access on **February 17, 2026**.6 This is an unusually aggressive timeline for a model that was the flagship less than 18 months ago, indicating a concerted effort to force migration to the GPT-5.x architecture. Furthermore, the fragmentation of "Operator" as a standalone brand—now folded into "ChatGPT Agent" or "Agent Mode"—demonstrates OpenAI's strategy to productize agents as features rather than standalone services.8

## ---

**1\. ECOSYSTEM TAXONOMY**

To integrate OpenAI into a Claude-centric constellation, one must navigate a complex taxonomy of access tiers, model classes, and user personas. The "one size fits all" era of GPT-4 is over; the current ecosystem requires precise selection of the correct "node" for the specific task.

### **1.1 The User Plane: Access Gating & Segmentation**

The "User Plane" dictates what capabilities are available to human operators and how those capabilities are capped.

#### **1.1.1 The "Plus" Tier ($20/mo): The Sampler**

The standard Plus subscription has been effectively downgraded to a "Sampler" tier for agentic features. While it offers access to the flagship **GPT-5.2** model, usage is dynamically throttled (observed around 160 messages per 3 hours).9 Crucially, the new high-value agentic features are severely capped:

* **Deep Research:** Limited to **10 queries per month**.10 This renders it useless for professional workflows.  
* **Agent Mode:** Limited to **40 messages per month**.11  
* **Role in Constellation:** Useful only for personal, low-intensity testing or as a backup interface.

#### **1.1.2 The "Pro" Tier ($200/mo): The Compute Station**

The Pro tier is now the baseline requirement for any serious agentic workflow. It unlocks the "High-Compute" assets that are otherwise inaccessible or prohibitively expensive via API.

* **Exclusive Access:** Only Pro users can access **o3-pro** and **GPT-5.2 Pro** in the chat interface.9  
* **Volume:** Deep Research caps increase to **120 queries per month** 10, and Agent Mode to **400 messages per month**.11  
* **Role in Constellation:** This is the recommended "human-in-the-loop" interface for supervising autonomous agents or conducting deep manual research.

#### **1.1.3 Team & Enterprise: The Governance Layer**

* **Team ($25-$30/user):** Functionally similar to Plus but adds data privacy (no training on data) and shared workspaces. It does *not* inherently include the high-compute access of Pro unless specific upgrades are applied.12  
* **Enterprise:** Custom pricing. Offers unlimited high-speed access, extended context windows (128k+ output), and critical governance features like Single Sign-On (SSO), SCIM provisioning, and data residency enforcement.12

### **1.2 The Developer Plane: Trust Tiers & API Access**

OpenAI gates access to its most dangerous and powerful API models based on cumulative spend, creating "Trust Tiers."

* **Tier 1 ($5+ paid):** "Sandbox" access. Low rate limits (500 RPM).  
* **Tier 2 ($50+ paid):** Standard access.  
* **Tier 3 ($100+ paid):** **The Agentic Threshold.** This is often the minimum requirement to access sensitive models like computer-use-preview or high-rate-limit o3. Users below this tier frequently report "Model Not Found" errors for preview endpoints.13  
* **Tier 4 ($250+ paid) & Tier 5 ($1,000+ paid):** Enterprise scale. Access to **GPT-5.2 Pro** endpoints and massive batch processing queues.14

### **1.3 The Model Taxonomy**

Models are no longer generic; they are specialized functional nodes.

| Functional Node | Primary Models | Description & Constellation Role |
| :---- | :---- | :---- |
| **Flagship Node** | **GPT-5.2** | The generalist. High intelligence, moderate cost. Use as a fallback for general NLP tasks where Claude is busy or rate-limited. |
| **Precision Node** | **GPT-5.2 Pro** | The expensive expert ($21/1M Input). Use strictly for final verification of critical data where cost is secondary to accuracy. |
| **Reasoning Node** | **o3**, **o3-pro** | The logic engine. "Thinking" models that perform chain-of-thought verification. Use for math, complex logic puzzles, or verifying Claude's architectural plans. |
| **Research Node** | **o3-deep-research**, **o4-mini-deep-research** | The librarian. Autonomous systems that browse, read, and synthesize. Use to gather raw intel for Claude to analyze. |
| **Action Node** | **computer-use-preview**, **Codex** | The hands. Models trained to control GUIs or write CLI commands. Use for execution of tasks defined by Claude. |
| **Media Node** | **gpt-realtime**, **Sora** | The senses. Low-latency voice I/O and video generation. Use for end-user interfaces. |

## ---

**2\. SERVICE CATALOG MATRIX (THE "TAX CODE")**

This section provides the definitive pricing and specification ledger. Forensic scanning of the pricing pages reveals a complex economy of input, output, and hidden "tool" costs. All prices are per 1 Million Tokens unless otherwise noted.

### **2.1 Text & Reasoning Models (API)**

The pricing structure reveals a massive premium for "Pro" models, indicating the immense computational cost of their underlying reinforcement learning / chain-of-thought processes. Note the "Cached Input" price, which utilizes prompt caching to reduce costs by up to 90% for repetitive contexts.

| Model ID | Context Window | Knowledge Cutoff | Input Cost ($) | Cached Input ($) | Output Cost ($) | Notes / Role |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **gpt-5.2** | 400,000 | Aug 2025 | $1.75 | $0.175 | $14.00 | **Flagship.** The standard for high-quality tasks. 3 |
| **gpt-5.2-pro** | 400,000 | Aug 2025 | $21.00 | N/A | $168.00 | **Precision.** 12x output cost vs standard. 3 |
| **gpt-5.1** | 200,000 | Aug 2025 | $1.25 | $0.125 | $10.00 | **Legacy Flagship.** Good balance. 15 |
| **gpt-5-mini** | 128,000 | Aug 2025 | $0.25 | $0.025 | $2.00 | **Economy.** High speed, low cost. 3 |
| **o3** | 200,000 | Oct 2023 | $2.00 | $0.50 | $8.00 | **Reasoning.** High logic. 4 |
| **o3-pro** | 200,000 | Oct 2023 | $20.00 | N/A | $80.00 | **Max Reasoning.** Tier 4+ only. 4 |
| **o4-mini** | 128,000 | Jun 2024 | $1.10 | $0.275 | $4.40 | **Fast Reasoning.** Efficient logic. 15 |
| **gpt-4o** | 128,000 | Oct 2023 | $2.50 | $1.25 | $10.00 | **Legacy.** Sunset Feb 17, 2026\. 6 |

**Forensic Insight:** The pricing of gpt-5.2-pro ($168 output) suggests that for every token it generates, it is performing roughly 12 times the internal computation of the standard model. This makes it economically unviable for high-volume orchestration but indispensable for "zero-fail" verifications.

### **2.2 Agentic & Tool Models (Responses API)**

These models are accessible only via the v1/responses API and often incur additional per-call fees for the tools they invoke.

| Model ID | Primary Function | Input Cost ($) | Output Cost ($) | Tool Fees | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **o3-deep-research** | Web Research | $10.00 | $40.00 | \+ Search Costs | The "Deep Research" engine. 18 |
| **o4-mini-deep-research** | Web Research | $2.00 | $8.00 | \+ Search Costs | Faster, cheaper research variant. 19 |
| **computer-use-preview** | GUI Automation | $3.00 | $12.00 | N/A | Requires CUA loop / Docker. 20 |
| **codex-mini-latest** | CLI Coding | $1.50 | $6.00 | N/A | **Sunset Jan 16, 2026\.** 21 |
| **gpt-realtime** | Audio/Voice | $4.00 (Txt) $32.00 (Aud) | $16.00 (Txt) $64.00 (Aud) | N/A | Low latency WebRTC. 3 |

### **2.3 The "Hidden Tax" of Tooling**

Architects must account for the peripheral costs associated with agentic workflows. A single "Deep Research" run does not just cost token money; it incurs tool usage fees.

* **Web Search:** $10.00 per 1,000 calls \+ content tokens.3  
* **Code Interpreter:** $0.03 per session.3  
* **File Search Storage:** $0.10 / GB / day (First GB free).3  
* **File Search Tool Call:** $2.50 / 1,000 tool calls (Responses API only).3  
* **Video (Sora):** $0.10 \- $0.50 per second of generated video, dependent on resolution.3

**Cost Simulation:** A single complex "Deep Research" task using o3-deep-research might involve reading 20 web pages (50k input tokens), performing 15 searches, and writing a 2k token report.

* Input Tokens: 0.05 \* $10 \= $0.50  
* Output Tokens: 0.002 \* $40 \= $0.08  
* Search Calls: 15 \* ($10/1000) \= $0.15  
* **Total:** \~$0.73 per run.  
* *Note:* Reports from heavy users indicate this can spike to over **$10.00 per query** if the agent enters a recursive rabbit hole of reading massive documents found via search.22

## ---

**3\. LIMITS & QUOTAS: OFFICIAL VS OBSERVED**

OpenAI employs "Smart Rate Limits" which are opaque and dynamic. However, forensic analysis of documentation and user reports provides a clearer picture of the actual boundaries.

### **3.1 Consumer Limits (ChatGPT)**

| Plan | Feature | Official Limit | Observed Behavior & Nuance |
| :---- | :---- | :---- | :---- |
| **Free** | GPT-5.2 | 10 msgs / 5 hrs | **Hard Cap.** Users are aggressively downgraded to gpt-5-mini or gpt-4o-mini once hit. No access to agentic tools. 9 |
| **Plus** | GPT-5.2 | \~160 msgs / 3 hrs | **Dynamic.** During peak US hours, this limit often tightens. 9 |
| **Plus** | Deep Research | 10 queries / month | **Hard Cap.** This limit effectively renders the Plus tier a "demo" for Deep Research. 10 |
| **Plus** | Agent Mode | 40 msgs / month | **Hard Cap.** Barely sufficient for testing a single workflow. 11 |
| **Pro** | GPT-5.2 | "Unlimited" | **Soft Cap.** Subject to "fair use," but reports suggest power users rarely hit walls unless automating via the UI. 23 |
| **Pro** | Deep Research | 120 queries / month | **Significant Capacity.** Allows for roughly 4 deep research tasks per day. 10 |
| **Pro** | Agent Mode | 400 msgs / month | **Production Ready.** Sufficient for daily delegation of routine tasks. 11 |

### **3.2 Developer Limits (API Trust Tiers)**

* **Tier 1:** 500 RPM (Requests Per Minute). Suitable only for prototyping.  
* **Tier 3 ($100+ lifetime spend):** 5,000 RPM. This is the **Minimum Viable Tier** for production applications. Crucially, access to limited models like computer-use-preview is often restricted to Tier 3 and above.13  
* **Tier 5 ($1,000+ lifetime spend):** 15,000 RPM. Unlocks higher concurrency and massive batch processing limits.

## ---

**4\. DEPRECATION / MIGRATION / ROADMAP SIGNALS**

The ecosystem is in a volatile state of transition. Several key assets are scheduled for termination in 2026\. This "Death Row" list is critical for integration planning.

### **4.1 The "Death Row" List (2026)**

| Asset | Sunset Date | Status | Required Action |
| :---- | :---- | :---- | :---- |
| **Voice on macOS App** | **Jan 15, 2026** | **CRITICAL** | Functionality retires in 3 days. Users must migrate to the main app or web interface. 24 |
| **codex-mini-latest** | **Jan 16, 2026** | **CRITICAL** | Model deletion in 4 days. Update CLI configurations to gpt-5-codex-mini. 7 |
| **chatgpt-4o-latest** | **Feb 17, 2026** | **HIGH** | Model deletion in \~5 weeks. Applications using this specific snapshot must migrate to gpt-5.1-chat-latest. 6 |
| **DALL-E 3 (API)** | May 12, 2026 | Medium | Model deletion. Migrate to gpt-image-1 or gpt-image-1-mini. 7 |
| **Assistants API** | Aug 26, 2026 | Strategic | **Major Architecture Shift.** The Assistants API is deprecated. All stateful agent implementations must migrate to the **Responses API**. 1 |

### **4.2 The "Responses API" Mandate**

The most significant architectural shift is the deprecation of the **Assistants API** in favor of the **Responses API** (v1/responses).

* **Mechanism:** The Responses API is a stateful interface where the *server* manages the "Thought \-\> Tool Call \-\> Observation \-\> Thought" loop.  
* **Exclusivity:** New capabilities such as **Computer Use** and **Deep Research** are available *only* via the Responses API. They cannot be accessed via the standard Chat Completions endpoint. This forces developers to adopt the stateful paradigm if they wish to use OpenAI's latest tools.2  
* **Timeline:** While the Assistants API technically functions until August 2026, it is effectively feature-frozen. All new development should target v1/responses.

## ---

**5\. CODEX & "DEVELOPER-AGENT" DEEP DIVE**

In the context of a Claude-centric constellation, the role of "Coder" is contested between Anthropic's **Claude Code** and OpenAI's **Codex**. A forensic comparison reveals they serve different architectural purposes.

### **5.1 Codex CLI: The "Worker"**

* **Architecture:** OpenAI's terminal agent. It can run in two modes: "Local" (executing on the user's machine) or "Cloud" (executing in a sandboxed environment managed by OpenAI).26  
* **Model:** Powered by gpt-5.1-codex or gpt-5-codex-mini.  
* **Strengths:**  
  * **Asynchronous:** Codex excels at "fire and forget" tasks. You can assign it to "write unit tests for this module" and it will execute in the background.  
  * **Cost:** Access is often bundled with ChatGPT Plus/Pro subscriptions or billed at lower rates via API.  
  * **Integration:** Native integration with OpenAI's "Responses" loop allows it to efficiently retry failed tests without user intervention.  
* **Weaknesses:** Reasoning capability is generally inferior to Claude. It tends to "patch" code rather than "architect" it.

### **5.2 Claude Code: The "Architect"**

* **Architecture:** A local terminal client that indexes the file system deeply.  
* **Strengths:**  
  * **Context:** Claude's massive context window and superior retrieval allow it to understand the *entire* codebase structure better than Codex.  
  * **Quality:** Consistently scores higher on "Pass@1" benchmarks like SWE-bench.28  
  * **Refactoring:** Capable of complex architectural refactors that require holding multiple file dependencies in memory simultaneously.  
* **Weaknesses:** Synchronous, expensive (high token burn), and high latency.

### **5.3 Integration Strategy**

In a Constellation architecture, **Claude Code** acts as the "Head" and **Codex** as the "Hands."

* **Scenario:** A massive refactor.  
* **Claude:** Analyzes the architecture, defines the interface changes, and creates a plan.  
* **Codex:** Is triggered via CLI to implement the boilerplate changes, write the new unit tests, and fix linting errors in the background.

## ---

**6\. BROWSER / COMPUTER AGENTS (UI \+ API)**

These capabilities represent the "Action Layer" of the ecosystem—where the AI leaves the text box and interacts with the digital world.

### **6.1 Agent Mode (Consumer)**

* **Identity:** Formerly known as "Operator." Now branded as "ChatGPT Agent" or "Agent Mode".8  
* **Function:** A consumer-facing integration that allows ChatGPT to perform browser-based tasks like booking flights, filling forms, or shopping.  
* **Availability:** Integrated into the ChatGPT UI. Not available as a standalone app. Strictly gated by the 40/400 message limits discussed in Section 3.1.

### **6.2 Computer Use (API)**

* **Identity:** computer-use-preview.20  
* **Mechanism:** This is a vision-reasoning model optimized for GUI interaction. It does not "know" the OS API; it "looks" at screenshots and "acts" via coordinate clicks and keystrokes.  
* **Architecture:** Implementation requires a **Dockerized Sandbox**. OpenAI provides a reference container (Ubuntu \+ VNC). The application loop is:  
  1. Client captures screenshot of Docker container.  
  2. Client sends screenshot to v1/responses API.  
  3. Model returns action (e.g., click(200, 300)).  
  4. Client executes action in container.  
  5. Repeat.  
* **Security Risk:** **HIGH.** This model should *never* be connected to a host machine or sensitive production environment without strict isolation. The risk of prompt injection via visual elements (e.g., a website displaying text that tricks the model into executing a malicious command) is non-zero.25

### **6.3 Deep Research (API)**

* **Identity:** o3-deep-research (High Quality) and o4-mini-deep-research (High Speed).18  
* **Mechanism:** An autonomous loop that breaks a user query into sub-questions, performs web searches, reads content, identifies gaps, and iterates until a report can be synthesized.  
* **Performance:** Can take 5 to 30 minutes to complete a run. Requires background=true in the API call to handle the long timeout.31  
* **Value:** This is arguably the most valuable node for a Claude-centric system, offloading the massive context overhead of "reading the web" to OpenAI's infrastructure.

## ---

**7\. UNIQUE CAPABILITIES VS CLAUDE**

Why include OpenAI in a Constellation if Claude is the orchestrator? The answer lies in specialized infrastructure that Anthropic lacks or exposes less efficiently.

1. **Deep Research Loop:** While Claude can browse the web, it typically does so in a single-turn "search and read" fashion. OpenAI's o3-deep-research is a dedicated *agentic loop* that is far more robust for generating comprehensive "analyst-grade" reports without consuming Claude's context window or requiring complex client-side orchestration.  
2. **Computer Use Infrastructure:** OpenAI has standardized the computer-use-preview model and API interactions specifically for GUI control. While Anthropic has "Computer Use" capabilities, OpenAI's integration via the **Responses API** offers a potentially more streamlined "turn-key" solution for developers already in the Azure/OpenAI stack.  
3. **Realtime Voice:** The gpt-realtime API offers WebRTC connectivity for low-latency (\<500ms) speech-to-speech interaction. This is superior to chaining transcription \-\> LLM \-\> TTS, creating a much more natural conversational interface.  
4. **Cost Efficiency (Mini Models):** The o4-mini and gpt-5-mini models offer an extremely competitive price-to-performance ratio for low-stakes tasks, often undercutting Claude Haiku in specific reasoning/speed benchmarks.32

## ---

**8\. INTEGRATION ARCHITECTURE FOR A CLAUDE-CENTRIC CONSTELLATION**

This section outlines the blueprint for wiring OpenAI's "Utility Cloud" into a system orchestrated by **Claude 3.5/4.5 Sonnet**.

### **8.1 The "Constellation" Pattern**

The architecture defines **Claude** as the "Central Brain" and OpenAI as the "Peripheral Nervous System."

Code snippet

graph TD  
    User\[User Input\] \--\> Claude\[Orchestrator: Claude 4.5\]  
      
    subgraph "Claude Core"  
        Claude \--\> Logic  
        Claude \--\> CodeArch\[Code Architect\]  
    end  
      
    subgraph "OpenAI Utility Cloud"  
        Claude \-- "Tool Call: Research" \--\> O\_Research\[OpenAI o3-deep-research\]  
        Claude \-- "Tool Call: Action" \--\> O\_Computer\[OpenAI Computer Use\]  
        Claude \-- "Tool Call: Voice" \--\> O\_Voice  
        Claude \-- "Tool Call: Bulk Code" \--\> O\_Codex\[OpenAI Codex CLI\]  
    end  
      
    O\_Research \-- "Report Artifact" \--\> Claude  
    O\_Computer \-- "Action Result" \--\> Claude  
    O\_Voice \-- "Transcript" \--\> Claude  
    O\_Codex \-- "PR/Diff" \--\> Claude  
      
    Claude \--\> Final

### **8.2 Operational Protocols**

#### **8.2.1 The Research Protocol**

1. **Trigger:** Claude identifies a user request requiring broad, up-to-date market data (e.g., "Analyze 2026 lithium pricing trends").  
2. **Delegation:** Claude constructs a structured prompt for o3-deep-research.  
3. **Execution:** The system calls the OpenAI v1/responses API with background=true.  
4. **Wait:** The system polls for completion (approx. 10-20 mins).  
5. **Ingestion:** OpenAI returns a structured Markdown report.  
6. **Synthesis:** Claude reads the report (as context) and answers the user's specific question, citing the OpenAI report as source material.

#### **8.2.2 The Coding Protocol**

1. **Trigger:** A requirement for massive but low-complexity code changes (e.g., "Add docstrings to all 50 Python files").  
2. **Delegation:** Claude defines the docstring standard.  
3. **Execution:** The system triggers **Codex CLI** (or API) to iterate through the files and apply the changes.  
4. **Review:** Claude reviews the resulting git diff for quality assurance before committing.

#### **8.2.3 The Voice Protocol**

1. **Interface:** The user interacts with a frontend powered by **OpenAI Realtime API**.  
2. **Handoff:** The Realtime API handles the immediate conversational turn-taking (filling silence, acknowledging input).  
3. **Escalation:** If the user asks a complex reasoning question, the Realtime agent summarizes the query and passes it to **Claude**.  
4. **Response:** Claude generates the thoughtful answer, which is passed back to the Realtime API to be spoken to the user.

## ---

**9\. COST / VALUE MODEL**

### **9.1 The "Pro" Subsidy: Arbitraging the Subscription**

For individual power users, the **ChatGPT Pro ($200/mo)** plan represents a massive economic subsidy compared to API costs.

* **The Math:** o3-pro costs $20 (Input) / $80 (Output) per 1M tokens via API.  
* **The Scenario:** If a user generates just **2.5 Million output tokens** (roughly 50 detailed reports or 10 extensive coding sessions) in a month, the API cost would be **$200**.  
* **The Reality:** Pro users often exceed this volume significantly. Therefore, for *personal* agentic workflows, it is far more economical to use the Pro interface (or reverse-engineer the "ChatGPT Agent" web access) than to run the same workload via API.

### **9.2 Research Cost Modeling**

Deep Research is expensive. Architects must choose the right model.

* **Option A (o3-deep-research):** $10 (in) / $40 (out). High quality. A single run can cost **$1.00 to $5.00** depending on the depth of the rabbit hole.  
* **Option B (o4-mini-deep-research):** $2 (in) / $8 (out). Medium quality. A run typically costs **$0.20 to $1.00**.  
* **Strategy:** Use o4-mini for initial scoping or low-stakes queries. Reserve o3 for final client deliverables or high-stakes analysis.32

### **9.3 API Optimization**

* **Batch API:** Offers a **50% discount** on token costs. Use this for all asynchronous background tasks (e.g., nightly research summaries).  
* **Prompt Caching:** OpenAI's cached input ($0.175 for GPT-5.2) is extremely cheap. Ensure that static context (e.g., codebase documentation, rulebooks) is sent first to trigger caching.3

## ---

**10\. APPENDICES**

### **10.1 Evidence Ledger (Selected)**

| ID | Source | Date | Fact / Claim |
| :---- | :---- | :---- | :---- |
| 3 | OpenAI Pricing Page | Jan 2026 | Pricing for GPT-5.2 ($1.75/$14) and GPT-5.2 Pro ($21/$168). |
| 34 | News / Wikipedia | Feb 2025 | Deep Research launched Feb 3, 2025\. |
| 24 | Release Notes | Jan 2026 | macOS Voice feature retiring Jan 15, 2026\. |
| 20 | Model Docs | Jan 2026 | computer-use-preview pricing ($3/$12). |
| 9 | Help Center | Jan 2026 | Pro tier exclusive access to GPT-5.2 Pro and o3-pro. |
| 6 | Tech News | Nov 2025 | GPT-4o API sunset confirmed for Feb 17, 2026\. |
| 7 | OpenAI Deprecations | Jan 2026 | Official deprecation list including codex-mini-latest. |
| 1 | Migration Guide | Jan 2026 | Assistants API sunset date set for Aug 26, 2026\. |
| 32 | DataCamp | Jan 2026 | o4-mini-deep-research pricing ($2/$8). |

### **10.2 Known Unknowns**

* **Tier 5 Gating:** The exact cumulative spend required to unlock gpt-5.2-pro via API is not explicitly public, though widely estimated at \>$1,000/mo.  
* **Computer Use Whitelist:** It remains unclear if computer-use-preview is fully open to all Tier 3 users or if manual approval is still required for some regions/accounts.  
* **Pro Fair Use Caps:** The exact numerical cap for "Unlimited" messages on the Pro plan is unpublished, creating a risk for heavy automation users.

### **10.3 Re-Run Playbook**

To update this forensic report, the analyst should:

1. **Verify Timestamps:** Check if the **Jan 15, 2026** macOS Voice retirement occurred as scheduled.  
2. **Monitor Deprecations:** Watch the platform.openai.com/docs/deprecations page for the **Feb 17, 2026** GPT-4o removal.  
3. **Price Watch:** Scan openai.com/api/pricing weekly for o3 price drops, as competition from open-source reasoning models often forces adjustments.  
4. **API Status:** Check the status of the **Responses API** migration guides for new mandatory flags or breaking changes.

#### **Works cited**

1. From Assistants API to Responses API: Migration Guide & Best Practices \- CoSupport AI, accessed January 12, 2026, [https://cosupport.ai/articles/assistants-api-responses-api-migration-guide-best-practices](https://cosupport.ai/articles/assistants-api-responses-api-migration-guide-best-practices)  
2. Migrate to the Responses API \- OpenAI Platform, accessed January 12, 2026, [https://platform.openai.com/docs/guides/migrate-to-responses](https://platform.openai.com/docs/guides/migrate-to-responses)  
3. API Pricing \- OpenAI, accessed January 12, 2026, [https://openai.com/api/pricing/](https://openai.com/api/pricing/)  
4. How is OpenAI o3-pro Different from o3? \- Data Studios, accessed January 12, 2026, [https://www.datastudios.org/post/how-is-openai-o3-pro-different-from-o3](https://www.datastudios.org/post/how-is-openai-o3-pro-different-from-o3)  
5. O3 vs O3 Pro Pricing: Which OpenAI Model Should You Use? \- Creole Studios, accessed January 12, 2026, [https://www.creolestudios.com/openai-o3-vs-o3-pro-pricing-performance-comparison/](https://www.creolestudios.com/openai-o3-vs-o3-pro-pricing-performance-comparison/)  
6. OpenAI will stop API access to the GPT-4o model in February 2026 \- AI NEWS \- AIBase, accessed January 12, 2026, [https://news.aibase.com/news/23009](https://news.aibase.com/news/23009)  
7. Deprecations | OpenAI API, accessed January 12, 2026, [https://platform.openai.com/docs/deprecations](https://platform.openai.com/docs/deprecations)  
8. Introducing Operator \- OpenAI, accessed January 12, 2026, [https://openai.com/index/introducing-operator/](https://openai.com/index/introducing-operator/)  
9. GPT-5.2 in ChatGPT | OpenAI Help Center, accessed January 12, 2026, [https://help.openai.com/en/articles/11909943-gpt-5-in-chatgpt](https://help.openai.com/en/articles/11909943-gpt-5-in-chatgpt)  
10. What Is OpenAI's New Deep Research Feature? How to Use It & More \- Tech.co, accessed January 12, 2026, [https://tech.co/news/openai-new-deep-research-feature](https://tech.co/news/openai-new-deep-research-feature)  
11. ChatGPT Agent Mode: What's New, and Why It Matters for Entrepreneurs & Creators, accessed January 12, 2026, [https://danielbensonpoe.medium.com/chatgpt-agent-mode-a5f385bac3ac](https://danielbensonpoe.medium.com/chatgpt-agent-mode-a5f385bac3ac)  
12. ChatGPT Plans: Comparing Free, Plus, Pro, Business & Enterprise \- IntuitionLabs, accessed January 12, 2026, [https://intuitionlabs.ai/articles/chatgpt-plans-comparison](https://intuitionlabs.ai/articles/chatgpt-plans-comparison)  
13. Computer-use-preview not working even after getting tier 3 \- OpenAI Developer Community, accessed January 12, 2026, [https://community.openai.com/t/computer-use-preview-not-working-even-after-getting-tier-3/1144255](https://community.openai.com/t/computer-use-preview-not-working-even-after-getting-tier-3/1144255)  
14. GPT-5.2 Model | OpenAI API, accessed January 12, 2026, [https://platform.openai.com/docs/models/gpt-5.2](https://platform.openai.com/docs/models/gpt-5.2)  
15. Pricing | OpenAI API, accessed January 12, 2026, [https://platform.openai.com/docs/pricing](https://platform.openai.com/docs/pricing)  
16. Compare models | OpenAI API, accessed January 12, 2026, [https://platform.openai.com/docs/models/compare](https://platform.openai.com/docs/models/compare)  
17. ChatGPT-4o Model \- OpenAI Platform, accessed January 12, 2026, [https://platform.openai.com/docs/models/chatgpt-4o-latest](https://platform.openai.com/docs/models/chatgpt-4o-latest)  
18. Azure OpenAI Service \- Pricing, accessed January 12, 2026, [https://azure.microsoft.com/en-au/pricing/details/cognitive-services/openai-service/](https://azure.microsoft.com/en-au/pricing/details/cognitive-services/openai-service/)  
19. Exploring OpenAI's deep research API model o4-mini-deep-research \- Simon Willison: TIL, accessed January 12, 2026, [https://til.simonwillison.net/llms/o4-mini-deep-research](https://til.simonwillison.net/llms/o4-mini-deep-research)  
20. computer-use-preview Model | OpenAI API, accessed January 12, 2026, [https://platform.openai.com/docs/models/computer-use-preview](https://platform.openai.com/docs/models/computer-use-preview)  
21. codex-mini-latest Model | OpenAI API, accessed January 12, 2026, [https://platform.openai.com/docs/models/codex-mini-latest](https://platform.openai.com/docs/models/codex-mini-latest)  
22. OpenAI Deep Research API explained: features, use cases, and pricing | by Rysysth Insights, accessed January 12, 2026, [https://medium.com/@rysysth-insights/openai-deep-research-api-explained-features-use-cases-and-pricing-162c87bba8a8](https://medium.com/@rysysth-insights/openai-deep-research-api-explained-features-use-cases-and-pricing-162c87bba8a8)  
23. Is ChatGPT Pro Worth It in 2025? What $200 Actually Gets You \- Global GPT, accessed January 12, 2026, [https://www.glbgpt.com/hub/is-chatgpt-pro-worth-it/](https://www.glbgpt.com/hub/is-chatgpt-pro-worth-it/)  
24. ChatGPT — Release Notes \- OpenAI Help Center, accessed January 12, 2026, [https://help.openai.com/en/articles/6825453-chatgpt-release-notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)  
25. Computer use | OpenAI API, accessed January 12, 2026, [https://platform.openai.com/docs/guides/tools-computer-use](https://platform.openai.com/docs/guides/tools-computer-use)  
26. Claude Code vs OpenAI Codex: which is better in 2026? | Blog \- Northflank, accessed January 12, 2026, [https://northflank.com/blog/claude-code-vs-openai-codex](https://northflank.com/blog/claude-code-vs-openai-codex)  
27. Codex CLI \- OpenAI for developers, accessed January 12, 2026, [https://developers.openai.com/codex/cli/](https://developers.openai.com/codex/cli/)  
28. Claude vs Codex: Anthropic vs OpenAI in the AI Coding Agent Battle of 2026 | WaveSpeedAI Blog, accessed January 12, 2026, [https://wavespeed.ai/blog/posts/claude-vs-codex-comparison-2026/](https://wavespeed.ai/blog/posts/claude-vs-codex-comparison-2026/)  
29. Claude Opus 4.5 vs GPT-5.2 Codex: Best AI for Coding 2026 \- Vertu, accessed January 12, 2026, [https://vertu.com/lifestyle/claude-opus-4-5-vs-gpt-5-2-codex-head-to-head-coding-benchmark-comparison/](https://vertu.com/lifestyle/claude-opus-4-5-vs-gpt-5-2-codex-head-to-head-coding-benchmark-comparison/)  
30. Building Computer Use Agents with OpenAI's API \- RIIS LLC, accessed January 12, 2026, [https://www.riis.com/blog/building-computer-use-agents-with-openai-api](https://www.riis.com/blog/building-computer-use-agents-with-openai-api)  
31. Gemini Deep Research Agent | Gemini API \- Google AI for Developers, accessed January 12, 2026, [https://ai.google.dev/gemini-api/docs/deep-research](https://ai.google.dev/gemini-api/docs/deep-research)  
32. O4-Mini: Tests, Features, O3 Comparison, Benchmarks & More | DataCamp, accessed January 12, 2026, [https://www.datacamp.com/blog/o4-mini](https://www.datacamp.com/blog/o4-mini)  
33. LLM-Powered Search: o4-mini-high vs o3 vs Deep Research | alexop.dev, accessed January 12, 2026, [https://alexop.dev/posts/llm-powered-search-comparison-o4-mini-high-o3-deep-research/](https://alexop.dev/posts/llm-powered-search-comparison-o4-mini-high-o3-deep-research/)  
34. ChatGPT Deep Research \- Wikipedia, accessed January 12, 2026, [https://en.wikipedia.org/wiki/ChatGPT\_Deep\_Research](https://en.wikipedia.org/wiki/ChatGPT_Deep_Research)