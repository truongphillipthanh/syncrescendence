This is a comprehensive **Deep Research Prompt** designed to be fed into a capable research agent (such as Claude with tool use, OpenAI Deep Research, or a Perplexity-style engine).

It is structured to first rigorously validate the architectural foundations established in our thread, then aggressively push into "superintelligent" optimization territories by exploring emergent, undocumented, and theoretical capabilities of the Claude Code runtime.

***

# Deep Research Prompt: The "God-Mode" Claude Code Architecture

**Objective:** Conduct a recursive, multi-stage investigation into Anthropic’s "Claude Code" (CLI) to transition from "expert usage" to "superintelligent orchestration." The goal is to produce the empirical data necessary to architect a self-improving, autonomous software development engine.

**Context:** We have established a "Fleet Commander" architecture involving parallel execution, hierarchical memory (`CLAUDE.md`), and plan-execute separation. We now seek to validate recent undocumented features (Task systems, merged Skills/Commands) and theoretical agent topologies.

---

### Phase 1: Architectural Validation & Ground Truth (The Physics of the Engine)
*Validate the precise mechanics of the runtime environment using first-party documentation and technical analysis.*

1.  **The "Task" Primitive & Dependency Graphs:**
    *   **Query:** Investigate the specific JSON schema and state management of the newly released "Task" system.
    *   **Research Target:** How does `TaskUpdate` handle dependencies (`addBlockedBy`) across sessions? Specifically, verify if the `CLAUDE_CODE_TASK_LIST_ID` environment variable allows disparate CLI instances (e.g., in different terminal tabs or `git worktrees`) to atomically read/write to the same task graph without race conditions.
    *   **Goal:** Determine if "Tasks" can replace our ad-hoc `plan.md` as the unified bus for multi-agent coordination.

2.  **Context Compaction Mechanics:**
    *   **Query:** Analyze the exact trigger conditions for auto-compaction (e.g., is it strictly token-count based or heuristic?).
    *   **Research Target:** Does the new v2.1.x update persist "Tasks" and "Plans" *through* compaction as claimed by community reports? If so, does this obsolete the need for the "Ralph" wipe-context loop, or does "context rot" (degradation of recall) still necessitate hard resets?
    *   **Goal:** Define the mathematical optimal "Time-to-Live" (TTL) for a session before a hard reset is required.

3.  **The Skill/Command Merge & Subagent Scoping:**
    *   **Query:** Investigate the unification of Slash Commands and Skills.
    *   **Research Target:** Specifically, analyze the `agent` field in `SKILL.md` frontmatter. Can a Skill spawn a *recursive* subagent that spawns *another* subagent (nesting), or is it flat? Validate how `context: fork` behaves—does it copy the *entire* current history, or just the system prompt and `CLAUDE.md`?
    *   **Goal:** Determine if we can architect a "Fractal Agent" topology where skills dynamically spin up disposable workers.

---

### Phase 2: Frontier Pattern Analysis (The "Dark Matter" of Usage)
*Identify emergent behaviors and "superintelligent" anomalies in the developer community that contradict or surpass official guidance.*

4.  **The "Recursive Self-Improvement" Loop:**
    *   **Query:** Find examples of "Compounding Engineering" where the agent modifies its own `CLAUDE.md` or `SKILL.md` files *without* explicit human prompting.
    *   **Research Target:** Look for "Auto-Linter" patterns where `PostToolUse` hooks feed error logs back into the `CLAUDE.md` "Anti-Patterns" section. Is there a known feedback loop where the agent creates a new Skill to solve a recurring error it detected in itself?
    *   **Goal:** Design a "Self-Healing Constitution" protocol.

5.  **Headless Orchestration & CI/CD Integration:**
    *   **Query:** Investigate the limits of the `-p` (print/headless) flag and GitHub Actions integration.
    *   **Research Target:** Can we daisy-chain headless instances? (e.g., Agent A runs `claude -p "Design spec" > spec.md`, which triggers Agent B `claude -p "Implement spec.md"`). Look for "Swarm" implementations using `claude-flow` or similar tools that use the file system as a message bus between headless agents.
    *   **Goal:** Blueprint a "Serverless Agency" where Claude Code runs entirely in the background via git triggers.

6.  **The "Context Injection" vs. "RAG" Debate:**
    *   **Query:** Analyze the effectiveness of "custom indexing scripts" (like `fd` or `ripgrep` optimization) vs. MCP-based RAG.
    *   **Research Target:** Is it more effective to force Claude to "explore" the file system (active agentic retrieval) or to inject a map via `CLAUDE.md`? Look for benchmarks on retrieval latency vs. hallucination rates in large (>100k LoC) repos.

---

### Phase 3: Superintelligent Hypothesis Testing (The Novelty Search)
*Propose and simulate theoretical architectures that do not yet exist in the wild.*

7.  **Hypothesis: The "Git-Based Neural Bus"**
    *   **Proposition:** If multiple Claude instances run in parallel `worktrees`, can they use `git commit` messages as a communication protocol?
    *   **Research Task:** Investigate if an "Oracle" agent can watch the `git log` of "Worker" agents to monitor progress, effectively treating the Git graph as a distributed ledger of thought.
    *   **Goal:** Validate a "Zero-API" multi-agent swarm protocol using only Git primitives.

8.  **Hypothesis: The "MCP-as-OS" Layer**
    *   **Proposition:** Can we replace the OS shell entirely with high-level MCP tools?
    *   **Research Task:** Look for MCP servers that abstract "DevOps" (Kubernetes, AWS, Docker) into natural language tools. Can Claude Code effectively become the Operating System, managing infrastructure via MCP without ever seeing a raw bash terminal?
    *   **Goal:** Define the "Semantic Operating System" architecture.

9.  **Hypothesis: The "Hyper-Compacted" Memory Crystal**
    *   **Proposition:** Instead of simple summarization, can we use a specialized "Librarian" agent to compress session state into a rigorous `STATE.json` or `MEMORY.md` that is perfectly optimized for the *next* context window?
    *   **Research Task:** Investigate prompts or schemas (like "The 70/80 Rule" for docs) that maximize information density for model ingestion.
    *   **Goal:** Create a lossless "Save State" protocol for infinite-session continuity.

---

### Phase 4: Synthesis & Output Generation
*Compile the findings into the next-generation Definitive Guide.*

**Requirement:** Based on the findings above, generate:
1.  **The "God-Config":** A finalized, highly opinionated `settings.json`, `CLAUDE.md`, and `.mcp.json` suite that enables the "Task-Based" + "Git-Worktree" swarm architecture.
2.  **The "Oracle Protocol":** A step-by-step Standard Operating Procedure (SOP) for acting as the human fleet commander, specifically detailing how to use the new `Task` system to delegate to sub-agents.
3.  **The "Recursion Hook":** A specific `PostToolUse` hook script that forces Claude to update its own instructions upon failure.

**Execute deep research now.**