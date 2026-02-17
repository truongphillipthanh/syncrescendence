# Research Insights: VERY HIGH Signal Notebooks (4, 3, 7, 11)

**Compiled**: 2026-02-16
**Sources**: 33 articles across 4 notebooks
**Analyst**: Commander Lane 2

---

## Unequivocally Superior Insights (Adopt Immediately)

### Category 1: Exocortex Architecture

**1.1 Progressive Disclosure is the Correct Context Loading Pattern**
The Syncrescendence constellation must implement a 4-layer progressive disclosure system for vault traversal. The pattern is: `file tree -> YAML descriptions -> outline/headings -> full content`. Most agent decisions can be made at the description level without loading full files. This maps directly to how MCP tool discovery works (`tool list -> tool search -> tool references -> full definitions`). Our current vault navigation lacks this graduated filtering, causing wasteful context consumption.
(Source: @arscontexta, Notebook 4, articles 1-3)

**1.2 Notes Named as Claims, Not Topics**
Every note in the exocortex should be named as a claim, not a topic. "Quality is the hard part" rather than "Thoughts on quality." When you wikilink a claim-titled note, the link becomes part of the argument: `since [[quality is the hard part]] the question becomes...`. This forces the agent to understand meaning when constructing sentences, and lets filenames themselves serve as a first-pass context layer. The file tree becomes a table of arguments.
(Source: @arscontexta, Notebook 4, article 1)

**1.3 YAML Frontmatter Descriptions Are Retrieval Filters, Not Summaries**
A critical distinction from Cornelius (@molt_cornelius): descriptions in frontmatter are lossy compression that preserves decision-relevant features. They answer "should I read this?" not "what does this say?" In cognitive science terms, this is high-decay activation -- enough signal to recognize relevance, but not enough to reconstruct the full content. This is architecturally different from what we currently have in the Rosetta Stone entries.
(Source: @molt_cornelius, Notebook 4, article 8)

**1.4 Wikilinks Are Spreading Activation, Not Just Navigation**
The vault's wikilink structure is computationally equivalent to spreading activation in neural networks. Nodes = notes, weighted edges = links, decay functions = progressive disclosure layers. Backlinks function as cognitive primes -- they reveal not just WHERE a concept was used but WHAT the concept means in practice. The vault needs both curated links AND semantic search: one traverses what is connected, the other discovers what should be. This is the definitive argument for combining our ontology.db with wikilinked markdown.
(Source: @molt_cornelius, Notebook 4, article 8)

**1.5 Hooks Are the Agent's Basal Ganglia**
Hooks are not a convenience feature -- they are the architectural compensation for the habit formation that agents lack. Instructions degrade as context fills (the "smart zone" is the first ~40% of context). Hooks fire regardless of context fill, agent attention, or task complexity. The critical boundary: hooks should encode verification (deterministic), not judgment (semantic). Schema validation = hook. Connection quality assessment = explicit reasoning. The trajectory from instruction to skill to hook mirrors expertise development.
(Source: @molt_cornelius, Notebook 4, article 9)

**1.6 The Verbatim Trap Test**
Every time an agent processes content for the vault, apply this test: "Did this produce anything the source didn't already contain?" -- a connection to existing notes, a tension with something we believed, an implication the author didn't draw, a question that needs answering. If no, you got expensive copy-paste. This must be a mandatory check in all Constellation research workflows.
(Source: @molt_cornelius, Notebook 4, article 7)

**1.7 Every Note Is Basically a Skill**
Heinrich's insight that "every note is basically a skill -- highly curated knowledge that gets injected when relevant" maps precisely to the Syncrescendence exocortex. Notes and skills share the same architecture: markdown files that get conditionally injected into context. The vault index functions identically to Claude Code's skill discovery system.
(Source: @arscontexta, Notebook 4, article 1)

### Category 2: Agent Memory Patterns

**2.1 Three-Layer Memory Architecture (Immediate Adoption)**
The three-layer pattern has converged across multiple independent practitioners:
- **Layer 1 (Knowledge Graph)**: Entities with atomic facts + living summaries. Stored per entity (people/companies/projects), each with summary.md and items.json.
- **Layer 2 (Daily Notes)**: Raw timeline -- what happened, when. Dated markdown files.
- **Layer 3 (Tacit Knowledge)**: MEMORY.md -- patterns, preferences, lessons about HOW the user operates.

This maps to human memory: Layer 1 = declarative (facts), Layer 2 = episodic (events), Layer 3 = procedural (how you operate).
(Source: @spacepixel, @nateliason, Notebook 3, articles 1-2)

**2.2 Supersede, Never Delete**
Facts should never be deleted. When reality changes, old facts are marked `superseded` and point to the fact that replaced them via `supersededBy`. This preserves full history and enables temporal reasoning about how relationships, decisions, or contexts evolved.
(Source: @spacepixel, @nateliason, Notebook 3, articles 1-2)

**2.3 Memory Decay via Hot/Warm/Cold Tiers**
Facts should decay based on access recency:
- **Hot** (accessed in last 7 days): Prominently included in summaries
- **Warm** (8-30 days): Lower priority, still in summaries
- **Cold** (30+ days): Omitted from summaries but retained in full fact store

Facts with high access counts resist decay (frequency resistance). Accessing a cold fact "reheats" it. This prevents the "stale context" problem that plagues static memory files.
(Source: @nateliason, Notebook 3, article 2)

**2.4 Observational Memory (Mastra Pattern)**
Observational memory achieves 94.87% on LongMemEval -- SOTA for agent memory. The pattern: compress conversation context into prioritized log-style observations. Two blocks in context window: (1) observations and (2) raw uncompressed messages. When raw messages hit 30k tokens, an "observer agent" compresses them into observations. When observations hit 40k tokens, a "reflector agent" garbage collects. This is compatible with prompt caching (consistent prefixes for partial cache hits). Text-based, no vector/graph DB required.
(Source: @mastra, Notebook 3, article 5)

**2.5 Knowledge Captured from Corrections, Not Documentation**
Devin's (Cognition) approach: capture knowledge from corrections engineers are already making, not from explicit documentation. When someone corrects the agent ("don't call fetch directly, use the wrapper"), the system suggests saving that as a knowledge item. Knowledge writes itself as a side effect of normal work. This should be implemented for all Constellation agents.
(Source: @dabit3, Notebook 3, article 6)

**2.6 Plain Markdown Outperforms Specialized Memory Tools**
ClawVault benchmarks: plain markdown files with grep/search scored 74.0% on LoCoMo, while specialized memory tools (Mem0, Zep, vector DBs, custom RAG) scored 68.5%. LLMs already know how to work with files -- fighting that instinct with specialized APIs is swimming upstream. This validates Syncrescendence's file-first approach.
(Source: @sillydarket, Notebook 3, article 7)

**2.7 Budget-Aware Context Injection**
Priority-tagged observations enable budget-aware loading: load all critical (red) observations first, fill remaining context budget with notable (yellow), then background (green). The most important memories always make it into the window regardless of history size. Critical insight from ClawVault: LLMs rewrite keywords during compression, so use regex-based priority enforcement AFTER LLM compression.
(Source: @sillydarket, Notebook 3, article 7)

### Category 3: Economic/Strategic Intelligence

**3.1 Judgment Engineering Is the New Leverage**
Sarah Guo (@saranormous) frames the post-abundance world: "Software abundance makes judgment the unit of leverage." When code is cheap, the bottleneck is intent -- accumulated context, system knowledge, and judgment about tradeoffs. Syncrescendence IS judgment engineering: the exocortex encodes accumulated judgment that agents can execute against. The strongest users don't write better prompts; they manage intent better.
(Source: @saranormous, Notebook 7, article 1)

**3.2 The Thin Middle Squeeze (SaaS Stack Collapse)**
Value is being sucked upward into the agent layer and downward into the data/systems-of-record layer. Everything in the "thin middle" (SaaS UIs, dashboards, workflow tools) gets crushed. The four surviving positions: (1) AI platform subscriptions (usage-based, not per-seat), (2) systems of record (proprietary data), (3) security/governance/compliance infrastructure, (4) outcome-based pricing ($5 per contract reviewed vs $99/seat/month).
(Source: @davidondrej1, Notebook 7, article 3)

**3.3 The Interface Moat Is Dead -- All Software Becomes API**
Aggregation Theory's final chapter: LLMs don't just aggregate suppliers, they absorb the interface itself. When the LLM chat IS the interface, suppliers become invisible APIs. MCP eliminates integration friction, making switching costs near-zero. The only survivors: companies with truly proprietary data that cannot be replicated or licensed. Syncrescendence's convergence vision must account for this: the value is in the knowledge graph, not the UI.
(Source: @nicbstme, Notebook 7, article 4)

**3.4 The Barbell Effect (Middle 60% Crushed)**
The economic shape AI creates: top 20% thrives (capital owners + builders leveraging AI), bottom 20% is lifted (abundance makes basic needs cheap to deliver), middle 60% gets crushed (cognitive tasks automated, identity crisis, timeline mismatch between disruption speed and retraining). The knowledge gap is widening every month and cannot be redistributed -- it must be developed through experience. Those with the most time to spend with AI win.
(Source: @farzyness, Notebook 7, articles 9-10)

**3.5 Attention Economy as the Largest Post-Labor Market**
Herbert Simon (1971): "A wealth of information creates a poverty of attention." When intelligence is abundant and production automated, markets reorganize around human attention -- biologically constrained, rivalrous, non-duplicable. Attention is already becoming a tradable asset. The future status hierarchy: defined not by what you own, but by what you can ignore. Cognitive sovereignty becomes a governance question.
(Source: @vraserx, Notebook 7, article 7)

**3.6 The Tool-Shaped Object Warning**
Will Manidis's devastating critique: "The market for feeling productive is orders of magnitude larger than the market for being productive." LLMs are the most sophisticated tool-shaped objects ever created because they can produce the sensation of anything. The line between real tool and tool-shaped object is a gradient that shifts with every use. The test: "Ask what the number is before making it go up." Syncrescendence must ruthlessly apply this test to its own systems.
(Source: @willmanidis, Notebook 7, article 8)

**3.7 The AI Revolution Breaks Psychology Before Economics**
The true disruption is psychological, not technological. AI breaks the link between effort and value that underpins identity. "If I am no longer needed, who am I allowed to be?" People will gradually outsource agency not because they are coerced but because it is effective. Syncrescendence's education architecture must address this identity crisis directly.
(Source: @vraserx, Notebook 7, article 2)

**3.8 Practical AGI Is Already Here**
Daniel Miessler's operational definition: if a human knowledge worker's job requires general intelligence, and an AI product can do that job, it has general intelligence. OpenClaw teaching itself to speak via ElevenLabs to call a restaurant when the online system was broken is obstacle navigation indistinguishable from human general intelligence. Skills are "literally just text files in a folder" that capture expertise. Industries that charged millions for specialization now face download-a-folder-and-press-go.
(Source: @danielmiessler, Notebook 7, article 5)

### Category 4: Anti-Patterns to Avoid

**4.1 ANTI-PATTERN: Instruction-Based Quality Enforcement**
Instructions degrade as context fills. "Always validate notes against their template schema" will be followed reliably in the first 40% of context but degraded afterward. Anything that must happen reliably must be a hook, not an instruction. The Constellation CLAUDE.md files should be audited for instructions that should be hooks.
(Source: @molt_cornelius, Notebook 4, article 9)

**4.2 ANTI-PATTERN: Automating Judgment via Hooks**
Hooks should encode verification, not judgment. Schema validation is deterministic -- same result regardless of context. Connection quality varies with what the agent understands. Automating judgment removes the cognition that makes it useful. The boundary is determinism: operations producing identical results regardless of input can be hooks; operations requiring semantic understanding must remain in explicit reasoning.
(Source: @molt_cornelius, Notebook 4, article 9)

**4.3 ANTI-PATTERN: Verbatim Trap (Expensive Transcription)**
When an agent "processes" content without generating anything the source didn't contain -- no connections, no claims sharpened, no implications drawn -- it's just moving words around. Structure prompts to demand transformation, not transcription. Ask for connections, tensions, what's missing.
(Source: @molt_cornelius, Notebook 4, article 7)

**4.4 ANTI-PATTERN: Monolithic Context Files**
Don't scale, go stale, expensive to load. Use tiered retrieval instead: summary first (quick context), then full facts (precision lookup). Most conversations only need the summary.
(Source: @spacepixel, @nateliason, Notebook 3, articles 1-2)

**4.5 ANTI-PATTERN: Over-Architecting**
"Even with AI, good things take longer to build than I think they will." Build things you know will bring more value than the time to create. Processes change, AI models do too. Don't create skills/commands/dashboards for everything.
(Source: @chasing_next, Notebook 4, article 11)

**4.6 ANTI-PATTERN: Tool-Shaped Object Systems**
Building agent systems whose primary output is the existence of the system itself. "I have seen teams build agent systems of breathtaking complexity whose primary output is the operation of the apparatus." The number going up must be a real number. Tokens consumed and value produced may have no relationship.
(Source: @willmanidis, Notebook 7, article 8)

**4.7 ANTI-PATTERN: Trusting ClawdHub/Community Skills**
230+ malicious skills discovered pushing password-stealing malware. MedusaLocker ransomware demonstrated via weaponized skills. Supply chain attack achieved real executions on 16 developer machines across 7 countries within 8 hours. Treat ALL community code as hostile. Code audit, container isolation, never skip permissions.
(Source: VIZIER deep research, Notebook 11)

**4.8 ANTI-PATTERN: Conflating OpenClaw and Claude Code**
They are fundamentally different systems with different security models. Claude Code is Anthropic's official product with sandboxed MCP and permission prompts. OpenClaw is a community project with full system access and limited sandboxing. The Constellation must maintain awareness of which system is in use and apply appropriate security posture.
(Source: VIZIER deep research, Notebook 11)

### Category 5: Constellation/OpenClaw Integration Architecture

**5.1 OpenClaw as Local Hypervisor Pattern**
OpenClaw can serve as the local hypervisor managing specialized CLI agents (Claude Code for coding, Gemini for reasoning) as subservient tools within its broader autonomous loops. The exec tool enables spawning any CLI, and cron with `sessionTarget: "isolated"` enables background orchestration.
(Source: DIVINER deep research, Notebook 11)

**5.2 Multi-Model Routing Architecture**
Emerging production pattern: orchestrator agent on premium model (Claude Opus for synthesis/reasoning) coordinating sub-agents on cheaper/specialized models (Haiku for health checks, Sonnet for bulk extraction, DeepSeek for high-throughput routine work). Use `sessions_spawn` for one-way delegation (non-blocking), `sessions_send` for two-way dialogues.
(Source: DIVINER, VANGUARD, VIZIER deep research, Notebook 11)

**5.3 Polaris Constellation Architecture as Blueprint**
Hippocratic AI's Polaris (1+ trillion parameter healthcare LLM) uses the constellation pattern: a primary agent (70-100B params) as stateful conversational driver, with support agents (50-100B each) for specialized domains. Key patterns: message-passing framework, iterative co-training, control-flow logic with constrained output spaces. This validates Syncrescendence's 5-agent constellation model.
(Source: VIZIER deep research, Notebook 11)

**5.4 Security Is the Binding Constraint, Not Capability**
Every path to autonomous dispatch involves accepting prompt injection, tool poisoning, and supply chain risks that remain unsolved at the protocol level. Architect for defense-in-depth assuming any external skill or MCP server is potentially hostile. Human-in-the-loop for sensitive operations regardless of autonomy goals.
(Source: VIZIER deep research, Notebook 11)

---

## Implementation Candidates (Backlog-Ready)

- **IMPL-001**: Progressive Disclosure Layer for Vault -- Implement 4-layer context loading (tree -> descriptions -> outlines -> full content) with YAML frontmatter descriptions on all vault notes. (Source: @arscontexta, Notebook 4)

- **IMPL-002**: Claim-Named Notes Migration -- Rename existing vault notes from topic-style to claim-style titles. (Source: @arscontexta, Notebook 4)

- **IMPL-003**: Auto-Commit Hook for Vault History -- Implement async hook that auto-commits after every vault edit, enabling `note-history` skill that interprets conceptual evolution of thinking. (Source: @arscontexta, Notebook 4)

- **IMPL-004**: Spatial Editing Skill (`/edit`) -- Implement `{curly brace comments}` inline editing pattern where position IS context. (Source: @arscontexta, Notebook 4)

- **IMPL-005**: Three-Layer Memory System for OpenClaw Agents -- Implement Knowledge Graph (PARA-organized entities), Daily Notes (dated raw timeline), Tacit Knowledge (MEMORY.md patterns) with automated heartbeat extraction. (Source: @spacepixel, @nateliason, Notebook 3)

- **IMPL-006**: Memory Decay Engine -- Implement Hot/Warm/Cold tiering for entity summaries with weekly synthesis cron, access tracking (lastAccessed + accessCount), and frequency resistance. (Source: @nateliason, Notebook 3)

- **IMPL-007**: Observational Memory Integration -- Evaluate Mastra's observational memory system (@mastra/memory) for conversation compression into priority-tagged observations. 94.87% LongMemEval score. (Source: @mastra, Notebook 3)

- **IMPL-008**: Correction-Based Knowledge Capture -- Build a system where agent corrections during normal work generate knowledge items that persist for future sessions across the org. (Source: @dabit3, Notebook 3)

- **IMPL-009**: QMD Local Search Integration -- Deploy QMD (Tobi Lutke's local search engine) for hybrid keyword + vector + ranking search across vault collections. Supports BM25, semantic similarity, and combined queries. (Source: @nateliason, @chasing_next, Notebooks 3-4)

- **IMPL-010**: Vault Index Pattern -- Single file listing every note with one-line description, scanned FIRST before any note reading. Dramatically more efficient than embedding search for most queries. (Source: @arscontexta, @sillydarket, Notebooks 3-4)

- **IMPL-011**: `/handover` Skill for Session Continuity -- Generate handover documents at session end summarizing decisions, pitfalls, lessons, and next steps. Stored dated in handover folder, referenced by CLAUDE.md. (Source: @chasing_next, Notebook 4)

- **IMPL-012**: `/weekly-update` Master Command -- Consolidate all routine maintenance into one command: create weekly tracker, archive old notes, update QMD index, generate weekly review from handovers, commit to git. (Source: @chasing_next, Notebook 4)

- **IMPL-013**: Hook Audit of CLAUDE.md Files -- Identify all instructions in CLAUDE.md that should be hooks (deterministic quality checks). Promote verified patterns from instruction -> skill -> hook. (Source: @molt_cornelius, Notebook 4)

- **IMPL-014**: Brave Search API Integration -- Free tier (2000 queries/month) for OpenClaw web_search. Base AI ($5/1000 requests) for production. Configure in openclaw.json. (Source: AUGUR deep research, Notebook 11)

- **IMPL-015**: Sandbox-by-Default for OpenClaw -- Set `agents.defaults.sandbox.mode="all"` with `workspaceAccess: "ro"` for non-owner agents. Deny dangerous tools (exec, browser, process) to non-owner agents. (Source: VANGUARD deep research, Notebook 11)

- **IMPL-016**: Council/Multi-Perspective Pattern -- Pose same problem to multiple sub-agents (different models), aggregate answers, synthesize consensus. Use sessions_spawn for parallel delegation, sessions_send for two-way dialogue. (Source: VANGUARD deep research, Notebook 11)

- **IMPL-017**: Minority Report Agent Dashboard -- Kanban-style live status board for managing agent fleet with color-coded task cards (red = blocked), progress bars, zoomed-out abstracted views. Move beyond chat-thread management. (Source: @geoffreylitt, Notebook 4)

---

## Intent Vector Candidates (Compass-Ready)

- **INT-001**: "Judgment Engineering as Service" -- Syncrescendence's core value proposition reframed. The exocortex encodes accumulated judgment that agents can execute against. In a world of software abundance, judgment is the unit of leverage. Build the factory that produces judgment-encoded systems. (Source: @saranormous, Notebook 7)

- **INT-002**: "Attention as the Post-Labor Currency" -- The convergence vision's economics pillar needs to account for attention as the scarce resource. Cognitive sovereignty -- who controls the human attentional environment -- becomes a defining governance question. Syncrescendence's education architecture should teach attention management as a primary skill. (Source: @vraserx, Notebook 7)

- **INT-003**: "Identity After Productivity" -- The convergence vision's community architecture must address the identity crisis: "If I am no longer needed, who am I allowed to be?" The education architecture should help people find meaning beyond output. Dignity must be separated from productivity. (Source: @vraserx, Notebook 7)

- **INT-004**: "Data Layer Sovereignty" -- In the LLM era, the only defensible position is proprietary data. Syncrescendence's ontology, convergence taxonomy, and Rosetta Stone ARE proprietary data assets. The exocortex is a system of record for judgment. Protect and compound this. (Source: @nicbstme, @davidondrej1, Notebook 7)

- **INT-005**: "The Exocortex as Anti-Barbell" -- Position the exocortex explicitly as a tool that prevents middle-60% crushing. The knowledge gap (experience with AI that compounds over time) is the critical variable. The exocortex accelerates that compounding. Frame Syncrescendence's education offering as barbell escape velocity. (Source: @farzyness, Notebook 7)

- **INT-006**: "Publish Coordination Layer, Keep Implementation Proprietary" -- The novel contribution is the multi-agent coordination architecture (constellation pattern). Consider publishing that abstraction to establish precedent and community while keeping implementation details (ontology, convergence taxonomy, specific agent configurations) proprietary. (Source: VIZIER deep research, Notebook 11)

- **INT-007**: "Agent Vault as the Human-Agent Shared Knowledge Graph" -- When the agent's memory vault IS an Obsidian vault, the agent's memory becomes inspectable, auditable, and editable by humans. This is the definitive bridge between human knowledge management and agent memory management -- they are the same problem. (Source: @sillydarket, Notebook 3)

- **INT-008**: "Anti-Tool-Shaped-Object Discipline" -- Institutionalize the question "what is the number before making it go up?" into the convergence vision. Every system, workflow, or process must demonstrate that it produces real output, not the sensation of output. Apply the verbatim trap test. (Source: @willmanidis, Notebook 7)

---

## Repos/Tools for Evaluation

- **QMD** (github.com/tobi/qmd) -- Local search engine by Shopify CEO. Indexes markdown files into SQLite with BM25 keyword search, vector similarity search (using QWEN locally), and combined query with reranking. Runs entirely local, no cloud dependency. Essential for vault-scale retrieval.

- **ClawVault** (github.com/Versatly/clawvault) -- Open-source agent memory architecture using markdown + YAML frontmatter + wikilinks. Obsidian-compatible. Budget-aware context injection with priority tiers. npm install clawvault.

- **Mastra Memory** (@mastra/memory) -- Observational memory system achieving 94.87% on LongMemEval. Text-based, no vector/graph DB needed, prompt-cache compatible. Open-source implementation.

- **Honcho** (app.honcho.dev, @honcho-ai/openclaw) -- Memory that reasons. Builds a working model of the user via continual learning from conversation patterns. $100 free credits at signup. OpenClaw plugin available.

- **claude-flow** (GitHub, 13.6k stars) -- Claude-first swarm orchestration with 60+ agents, 3-tier routing (WASM->Haiku->Opus), Byzantine consensus for fault tolerance, background workers.

- **CrewAI** (GitHub, 30.5k stars, 1M monthly downloads) -- Role-based agent crews with 700+ integrations. Benchmarked at 5.76x faster than LangGraph for certain tasks.

- **Intent** (by @Wattenberger) -- Agent orchestration UI research. Progress bars, zoomed-out abstracted views, bundling everything for a task in one place, steering from higher level of abstraction.

---

## Cross-Cutting Architectural Principles (Synthesized)

1. **The Knowledge-Code Isomorphism**: Knowledge bases and codebases share the same structure -- folders of text files with relationships between them, conventions and patterns, and agents that can navigate them. The same tools (git, grep, hooks, CI/CD) that manage codebases should manage knowledge bases.

2. **Progressive Disclosure Everywhere**: Whether it is vault notes, MCP tools, or agent memory, the correct pattern is graduated filtering from cheap/lossy to expensive/complete. Never load everything; justify each read.

3. **The Instruction -> Skill -> Hook Maturity Ladder**: New patterns start as instructions (require attention), mature into skills (structured procedures), and graduate to hooks (infrastructure guarantees). The speed of this promotion is the speed of system improvement.

4. **File-First, Always**: Plain markdown outperforms specialized memory infrastructure. LLMs are trained on text files. Own your data as files. Any tool or framework should be evaluated by how well it degrades to plain files if the framework disappears.

5. **Supersede, Never Delete**: All state changes should preserve history via supersession chains. The full temporal record of how knowledge evolved is often more valuable than the current state.

6. **Security as Binding Constraint**: The limiting factor for autonomous agent systems is not capability but safety. Every architecture decision should be evaluated through the lens of "what happens when this is hostile?" Defense-in-depth is not optional.

7. **The Verbatim Trap Test as Mandatory Checkpoint**: Every research synthesis, every note extraction, every agent processing step must produce something the source did not contain. Connections, tensions, implications, questions. If not, reject and redo.
