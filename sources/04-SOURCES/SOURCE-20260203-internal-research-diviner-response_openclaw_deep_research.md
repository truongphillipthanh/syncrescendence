---
id: SOURCE-20260203-004
original_filename: RESPONSE-DIVINER-20260203-openclaw_deep_research.md
status: triaged
platform: internal
format: research
creator: diviner
signal_tier: paradigm
topics:
  - ai-agents
  - openclaw
  - infrastructure
  - architecture
  - research
teleology: synthesize
notebooklm_category: ai-agents
aliases:
  - "Diviner response - OpenClaw technical architecture spec"
synopsis: "Deep technical architecture specification of OpenClaw v2026.2. Documents the Gateway as a persistent event-driven daemon, Agent/Node topology, multi-agent event routing, and the shift from ephemeral cloud chat to local-first persistent agent runtime."
url: internal
key_insights:
  - "OpenClaw's Gateway is a persistent event-driven daemon decoupling agent cognitive runtime from I/O, enabling persistence across UI restarts."
  - "The Agent/Node topology allows hardware mesh extension — mobile devices expose sensors back to the Gateway, extending agent actuation."
  - "Multi-agent routing through a single inbound transport represents a novel multiplexing pattern for agent platforms."
---
# **Technical Architecture Specification: OpenClaw Platform (v2026.2)**

## **1\. Architectural Topology and System Dynamics**

The OpenClaw platform represents a paradigm shift in autonomous agent runtime environments, moving away from ephemeral, cloud-hosted chat interfaces toward a persistent, local-first, event-driven architecture. Unlike traditional Request-Response models where an agent remains dormant until queried, OpenClaw operates as a continuous daemon—the Gateway—that maintains a persistent event loop.1 This architecture is designed to support long-running, multi-turn workflows, autonomous background processing, and complex multi-agent topologies on a single host.

At the core of this system lies the **Gateway**, an always-on process that functions as the central nervous system of the OpenClaw installation. It is responsible for protocol multiplexing, session state management, token accounting, and the orchestration of the agent loop.1 The Gateway binds to a local control plane (defaulting to WebSocket on 127.0.0.1:18789) and exposes a unified API surface for both local UIs (such as the macOS menu bar app) and remote control interfaces.1 This design allows the agent "brain"—the cognitive runtime executing the LLM inference—to be decoupled from the I/O layer, enabling it to persist across UI restarts and handle asynchronous events like cron jobs or webhooks.3

The system topology is further segmented into **Agents** and **Nodes**. Agents are the logical units of cognition, each possessing a distinct identity, workspace, session store, and configuration profile.2 They are not merely different system prompts but are architecturally isolated entities with their own memory banks and permission scopes. Nodes, conversely, form a distributed hardware mesh. These are paired devices—iOS or Android endpoints, or secondary desktop clients—that expose their hardware capabilities (cameras, screens, location sensors) back to the Gateway, effectively extending the agent's sensory and actuation range beyond the host server.4

The interaction model is fundamentally **Event-Driven**. The Gateway ingests signals from various sources—inbound messages from platforms like WhatsApp or Slack, temporal events from the internal cron scheduler, or hardware interrupts from connected nodes.2 These signals are normalized into a standard event format and routed deterministically to the appropriate Agent Runtime. This routing logic is critical for the platform's multi-agent capabilities, allowing a single inbound pipe (e.g., a WhatsApp phone number) to serve as the transport layer for multiple distinct agent personalities based on the sender's identity.2

## ---

**2\. Complete API Surface Extraction and Tooling Specification**

The primary interface between the OpenClaw agent and the external world is its Tool/API surface. OpenClaw abandons the legacy approach of unstructured shell-script "skills" in favor of typed, first-class tools that offer structured inputs, outputs, and validation.4 This transition enhances reliability and security, as the Gateway can enforce strict schema validation before any code executes.

### **2.1 Runtime and Execution Primitives**

The execution layer provides the agent with the ability to manipulate the host system or sandboxed environments. These tools form the backbone of any coding or DevOps-centric workflow.

#### **The exec Tool**

The exec tool is the foundational primitive for system interaction. It allows the agent to execute shell commands within the configured environment—whether that is the host operating system or a Dockerized sandbox.4

* **Capabilities:** It supports synchronous execution for immediate feedback or asynchronous execution for long-running tasks.  
* **Security Implications:** Access to exec is the primary vector for system modification. As such, it is heavily gated by the tool restriction chain (discussed in Section 7). The elevated parameter allows an agent to request host-level access even when running in a sandbox, provided the global and agent-specific policies permit it.1

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| command | String | Yes | The shell command string to be executed. |
| yieldMs | Number | No | Time in ms to wait for output before auto-backgrounding (Default: 10000).5 |
| background | Boolean | No | If true, forces immediate background execution without waiting for output.4 |
| timeout | Number | No | Execution hard limit in seconds (Default: 1800).5 |
| elevated | Boolean | No | Request execution on the host OS, bypassing sandbox constraints.4 |
| workdir | String | No | Specifies the working directory for the command execution.5 |
| env | Object | No | Key-value pairs defining environment variables for the process.5 |

#### **The process Tool**

While exec initiates commands, the process tool manages their lifecycle. This separation of concerns allows agents to fire off complex builds or servers and then monitor them asynchronously.4

* **Capabilities:** It maintains a registry of backgrounded processes (spawned via exec with background: true or exceeding yieldMs). Agents can attach to these processes to read logs, send input to stdin, or terminate them.  
* **Operational Nuance:** The log action supports pagination via offset and limit, preventing context window overflow when reading massive build logs.4

| Action | Description |
| :---- | :---- |
| list | Enumerate all active background processes managed by the agent. |
| poll | Check the current status (running/exit code) and output buffer of a PID. |
| log | Retrieve standard output/error logs. Supports specific line ranges. |
| write | Inject string data into the process's standard input stream (stdin). |
| kill | Send a termination signal (SIGTERM/SIGKILL) to the process. |
| clear | Flush the maintained output buffer for a specific process to free memory. |
| remove | Deregister a terminated process from the Gateway's tracking system. |

### **2.2 File System Manipulation (group:fs)**

File system access is granular, distinguishing between simple reading/writing and complex patching operations.

* **read / write / edit:** These standard tools provide basic I/O. edit is typically a simple replacement or append operation.  
* **apply\_patch:** This is a specialized, experimental tool designed to handle multi-hunk code modifications.4 It addresses a common failure mode in LLM coding agents where the model struggles to accurately locate and replace code blocks in large files. apply\_patch accepts a structured object representing the file paths and diff hunks, applying them atomically. It is currently restricted to OpenAI models and must be explicitly enabled via tools.exec.applyPatch.enabled.4

### **2.3 Network Intelligence and Browser Automation**

OpenClaw provides two distinct mechanisms for web interaction: a lightweight fetcher and a heavy-duty browser automation suite.

#### **web\_search and web\_fetch**

These tools constitute the "fast path" for information retrieval.

* **web\_search:** Utilizes the Brave Search API. It requires a query and accepts an optional count (1-10). To conserve API quotas and token usage, results are cached by the Gateway for 15 minutes.4  
* **web\_fetch:** Retrieves and parses a URL into LLM-friendly text or Markdown. It includes a maxChars parameter to prevent context flooding and features a Firecrawl anti-bot fallback mechanism to handle sites with aggressive scraping protections.4

#### **The browser Tool (group:ui)**

This tool controls a managed, headless (or headed) browser instance, allowing for complex interactions like filling forms, handling JavaScript-heavy SPAs, and capturing screenshots.

* **Architecture:** The browser runs as a managed child process of the Gateway (or within the sandbox). It supports profile management (create-profile, reset-profile) to handle session cookies and local storage persistence.4  
* **Visual Intelligence:** The browser tool integrates with the agent's multimodal capabilities. It can generate "AI snapshots" (semantic DOM representations optimized for LLM reading) or "Aria snapshots" (accessibility tree dumps).  
* **Action Set:** navigate, click, type, press (keys), hover, drag, fill (forms), screenshot, pdf, upload, dialog (handle alerts).4

### **2.4 Communication and Messaging (group:messaging)**

The message tool is the unified abstraction layer for all supported chat protocols (Discord, Slack, WhatsApp, Telegram, Signal, iMessage, MS Teams).4

* **Unified Interface:** Regardless of the underlying transport, the agent uses the same send action. The Gateway handles the protocol-specific translation.  
* **Platform Specifics:**  
  * **MS Teams:** Supports a card parameter for sending Adaptive Cards.  
  * **WhatsApp:** send and poll actions route via the Gateway's distinct WhatsApp integration, whereas Slack messages are routed directly.4  
  * **Discord/Slack:** Support rich interactions like react, pin, thread-create, and moderation actions (kick, ban).4  
* **Safety Mechanisms:** The Gateway enforces strict session binding. A message tool call is constrained to the target of the active session. This prevents an agent from accidentally (or maliciously) broadcasting a private response to a different channel or user.4

### **2.5 Session Orchestration (group:sessions)**

These tools allow the agent to introspect and manipulate its own state and the state of other agents.

#### **sessions\_spawn**

This is the primary primitive for **Agentic Concurrency**. It allows an agent to fork execution by spawning a sub-agent to perform a specific task in isolation.2

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| task | String | Yes | The natural language instruction for the sub-agent. |
| label | String | No | Human-readable tag for UI and logs. |
| agentId | String | No | Target specific agent configuration (requires permission). |
| model | String | No | Override the default model for this task. |
| runTimeoutSeconds | Number | No | Hard timeout for the sub-session execution. |
| cleanup | String | No | "keep" or "delete" (Default: "keep").2 |

**Operational Flow:** The tool returns immediately with a runId and childSessionKey. The sub-agent executes asynchronously. Upon completion, the result is injected back into the parent session via an "Announce" step.2

#### **sessions\_send / sessions\_list**

* **sessions\_send:** Enables inter-session communication. It supports a timeoutSeconds parameter: if \> 0, it acts as a synchronous RPC call waiting for a reply; if 0, it behaves as a fire-and-forget message.2  
* **sessions\_list:** Allows agents to discover active contexts, filtered by kind (main, group, cron) or recency.2

### **2.6 Automation and System Management (group:automation)**

* **cron:** Manages the scheduler. Agents can self-schedule tasks using add, update, or remove. This tool requires a full job schema (detailed in Section 4).  
* **gateway:** Provides administrative control. Includes config.get, config.patch (for hot updates), and restart. The restart action is powerful—it reboots the Gateway process—and thus requires explicit enablement in openclaw.json (commands.restart: true) to prevent accidental shutdowns.4

## ---

**3\. Deep-Dive: Session Architecture and State Management**

The Session is the fundamental unit of state in OpenClaw. It represents a continuous thread of conversation and context. Unlike cloud-based systems where sessions are database rows, OpenClaw sessions are file-system backed artifacts.2

### **3.1 Storage Topology and Identification**

Session data is strictly isolated per agent to prevent context contamination.

* **Location:** \~/.openclaw/agents/\<agentId\>/sessions/.  
* **The Store File (sessions.json):** A lightweight index mapping session keys to metadata (timestamps, labels, last message IDs). UI clients query this file (via the Gateway) to render session lists.2  
* **Transcripts (\<SessionId\>.jsonl):** The full history of the conversation is stored in JSON Lines format. This append-only structure ensures durability and allows for streaming reads.

**Keying Strategy:**

The system uses a deterministic key generation strategy to map external inputs to internal sessions:

* **Single-Agent Mode:** agent:main:\<mainKey\> (Defaults to "main").  
* **Multi-Agent Mode:** Direct chats collapse to agent:\<agentId\>:\<mainKey\>.  
* **Group Chats:** agent:\<agentId\>:\<channel\>:group:\<id\>.  
* **Sub-Agents:** agent:\<agentId\>:subagent:\<uuid\>.2

### **3.2 The sessions\_spawn Mechanism and Concurrency**

The sessions\_spawn tool is the engine of parallelism in OpenClaw. When invoked, it does not merely "call another model"; it instantiates a full Agent Runtime context.

1. **Forking:** The Gateway generates a unique session key for the sub-agent.  
2. **Context Construction:** A fresh context window is created. It acts as a "clean slate" execution, unburdened by the parent session's history unless explicitly passed.  
3. **Isolation:** The sub-agent runs with its own tool permissions. By default, sub-agents cannot spawn further sub-agents (preventing recursion loops), though this is configurable.2  
4. **The "Herbert Yang" Interaction:** Community discussions and bug reports (referenced as the "Herbert Yang" issue) highlighted a critical flaw in earlier versions where agentId and model overrides in sessions\_spawn failed to propagate routing context correctly. This resulted in "malformed tool calls" or 400 errors from providers like OpenRouter. The fix, implemented in release 2026.2.2 (attributed to @justinhuangcode), ensured that accountId and binding contexts are correctly inherited by the embedded run, allowing sub-agents to utilize the correct provider credentials and routing identities.6

### **3.3 Lifecycle Management and Context Hygiene**

To manage the finite context window of LLMs, OpenClaw implements aggressive hygiene protocols.

* **Session Expiration:**  
  * **Daily Reset:** By default, sessions "roll over" at 04:00 AM local time. A new Session ID is generated, effectively archiving the previous day's chat.  
  * **Idle Reset:** Configurable via idleMinutes. If a session is inactive for this duration, the next interaction starts a fresh session.2  
* **Pruning Strategy:**  
  * **Trigger:** Executed before every LLM call if mode: "cache-ttl" is active.  
  * **Logic:** The system removes toolResult messages (which are often verbose) that are older than the defined ttl (default: 5 minutes). Crucially, user and assistant messages are *never* pruned, ensuring the narrative thread remains intact.  
  * **Protection:** The last keepLastAssistants (default: 3\) tool results are preserved to maintain immediate context for follow-up actions.2  
* **Compaction:** Distinct from pruning, compaction summarizes older segments of the conversation history into persistent memory notes, freeing up tokens in the sliding window without losing semantic content.2

## ---

**4\. Temporal Architecture: Cron and Heartbeat**

The Cron system provides the temporal drive for OpenClaw, transforming it from a reactive bot into a proactive agent.

### **4.1 Cron Job Schema**

A cron job is defined by a structured object passed to the cron.add tool.

| Field | Type | Description |
| :---- | :---- | :---- |
| name | String | A human-readable identifier for the job. |
| schedule | Object | The timing definition (see below). |
| payload | Object | Defines the execution logic and target. |
| sessionTarget | String | **Crucial:** Determines the execution context (main or isolated).3 |

### **4.2 Schedule Types**

The schedule object supports three modes:

1. **at**: One-shot execution at a specific ISO timestamp (UTC). Supports delete-after-run for ephemeral reminders.3  
2. **every**: Recurring interval (e.g., "30m", "1h").  
3. **cron**: Standard 5-field unix cron syntax (e.g., 0 7 \* \* \*) for precise scheduling.3

### **4.3 Execution Payloads and Targets**

The sessionTarget field fundamentally changes how the job executes. This distinction is vital for architectural design.

* **Target: main (Payload: systemEvent)**  
  * **Behavior:** The job enqueues a systemEvent into the **primary** session loop.  
  * **Context:** It executes within the full context of the main chat history.  
  * **Use Case:** Reminders, daily briefings, or tasks that require awareness of recent user interactions (e.g., "Remind me to follow up on the email I mentioned yesterday").3  
  * **Mechanism:** Triggers a heartbeat wakeup of the main agent.  
* **Target: isolated (Payload: agentTurn)**  
  * **Behavior:** The job spawns a **dedicated, fresh session** (cron:\<jobId\>).  
  * **Context:** Zero-context execution. It starts with a clean slate.  
  * **Traceability:** The system prompt is prefixed with \[cron:\<jobId\> \<job name\>\].  
  * **Output:** If deliver: true, a summary is posted back to the main chat; otherwise, it runs silently.3  
  * **Use Case:** Heavy background processing, log scrubbing, or fetching external data where polluting the main context window with intermediate tool outputs is undesirable.3

**Heartbeat Interaction:** The Gateway maintains a heartbeat tick. When a systemEvent cron fires, it piggybacks on this heartbeat to wake the agent. For isolated jobs, the Gateway proactively spawns the new session immediately.3

## ---

**5\. Capability Extension: The Skills System**

OpenClaw adheres to the **AgentSkills** specification, a standardized format for portable agent capabilities. This allows capabilities to be shared, versioned, and gated.8

### **5.1 SKILL.md Schema**

A Skill is defined by a directory containing a SKILL.md file. This file combines metadata (Frontmatter) with natural language instructions.

**YAML Frontmatter Specification:**

YAML

name: unique-skill-identifier  
description: A concise summary of functionality.  
user-invocable: true            \# Is this exposed as a slash command?  
disable-model-invocation: false \# Hide from system prompt?  
command-dispatch: tool          \# Optional: Direct dispatch bypass  
command-tool: target\_tool\_name  \# The tool to invoke if dispatched  
metadata:  
  openclaw:  
    os: \["darwin", "linux"\]     \# OS gating  
    requires:  
      bins: \["ffmpeg"\]          \# Binary dependencies  
      env:          \# Environment variables  
      config: \["path.to.key"\]   \# OpenClaw config keys

**Instruction Body:** The Markdown body contains the prompt injection that teaches the model how to use the skill. It supports variable interpolation, most notably {baseDir}.9

### **5.2 Resolution and Precedence**

When multiple skills exist (potentially with conflicting names), OpenClaw resolves them using a strict hierarchy, from highest to lowest priority:

1. **Workspace Skills:** Located in \<workspace\>/skills. These are per-agent and user-owned.  
2. **Managed Skills:** Located in \~/.openclaw/skills. These are local overrides shared across agents.  
3. **Bundled Skills:** Shipped with the OpenClaw distribution.9

**{baseDir} Resolution:** The {baseDir} variable resolves dynamically based on the skill's location. For a workspace skill, it points to the agent's workspace; for a shared skill, it points to the global skills directory. This allows skills to reference local assets or scripts relative to their installation path reliably.9

### **5.3 Plugins vs. Standalone Skills**

* **Standalone Skills:** Purely declarative (Markdown). They can only instruct the agent on how to use *existing* tools (e.g., "Use exec to run this Python script"). They cannot introduce new TypeScript/Node.js runtime logic.  
* **Plugins:** Integrated modules that can register **new Tools** (via a register function in the plugin entry point) AND facilitate **Skills** (via openclaw.plugin.json). A plugin is required if you need to add a new fundamental capability (like a binary-level interface to a hardware device) rather than just orchestrating existing ones.8

## ---

**6\. Multi-Agent Topology and Configuration**

OpenClaw's configuration file (openclaw.json) supports complex multi-agent setups via the agents.list array.

### **6.1 agents.list Schema Breakdown**

JSON

{  
  "agents": {  
    "list":  
        },  
        "identity": { "theme": "blue", "emoji": "🔬" },  
        "sandbox": {  
          "mode": "all",       // "off" | "non-main" | "all"  
          "scope": "agent",    // "session" | "agent" | "shared"  
          "workspaceAccess": "rw",  
          "docker": {... }    // Docker specific config  
        },  
        "subagents": {  
          "allowAgents": \["\*"\] // Whitelist for spawning  
        },  
        "tools": {             // Tool Restriction Policy  
          "profile": "coding",  
          "allow": \["web\_search"\],  
          "deny": \["message"\]  
        }  
      }  
    \]  
  }  
}

.1

### **6.2 Binding and Routing Logic**

The Gateway uses a deterministic **Binding Resolution Order** to route inbound messages to the correct agent. The "Most Specific Match Wins" rule applies:

1. **Peer Match:** Exact User ID match (e.g., \+15551234567 or @user:discord).  
2. **Guild/Team Match:** Specific Discord Guild or Slack Team ID.  
3. **Account Match:** Specific Channel Account (accountId).  
4. **Channel Match:** Generic wildcard (accountId: "\*").  
5. **Fallback:** The agent marked default: true or the first in the list.2

**Shared Channel Accounts:**

This logic enables the "Shared Account" pattern. A single WhatsApp number can serve multiple users.

* **Config:** Bind peer: "+1234..." to Agent A and peer: "+5678..." to Agent B.  
* **Outcome:** Both users message the same number, but the Gateway routes their packets to completely isolated agent instances ("brains"), ensuring data privacy and context isolation on a shared transport.2

### **6.3 Agent-to-Agent Messaging**

Direct communication between agents is disabled by default to prevent loops. To enable it:

1. Configure the agentToAgent tool in the allowlist.  
2. Agents can then address each other using the message tool or sessions\_send, effectively treating other agents as chat peers.2

## ---

**7\. Security Architecture: Access Control and Sandboxing**

OpenClaw implements a defense-in-depth security model, critical for a system that allows LLMs to execute shell commands.

### **7.1 The Tool Restriction Chain (8 Levels)**

Permissions are calculated by filtering the requested tool usage through an 8-layer hierarchy. The logic is strictly **"Deny Wins"**—if any layer denies a tool, it is blocked, regardless of other allowances.

1. **Global Tool Profile** (tools.profile): Sets the baseline (e.g., "minimal", "coding", "messaging").  
2. **Global Provider Profile** (tools.byProvider): Restriction based on the LLM provider (e.g., restrict "exec" for untrusted local models).  
3. **Global Policy** (tools.allow / tools.deny): Explicit global overrides.  
4. **Provider Policy** (tools.byProvider.allow): Provider-specific overrides.  
5. **Agent Policy** (agents.list.tools.allow): **Primary user config layer.**  
6. **Agent Provider Policy**: Agent-specific provider restrictions.  
7. **Sandbox Policy** (tools.sandbox.tools): Defines what tools are available inside the Docker container.  
8. **Sub-agent Policy** (tools.subagents.tools): Restrictions applied to spawned sessions.10

### **7.2 Sandboxing Strategy**

Sandboxing is built on Docker.

* **Modes:**  
  * off: Tools run on the host (High Risk, High Power).  
  * non-main: Only "main" session runs on host; groups/cron runs in sandbox.  
  * **all**: Everything runs in the sandbox.  
* **Scopes:**  
  * session: Fresh container per session (most secure, slower).  
  * agent: Persistent container per agent.  
  * shared: Single container shared by multiple agents.1

## ---

**8\. Integration Strategy: Mapping to Syncrescendence**

The Syncrescendence constellation architecture (CAPTURE → DISPATCH → RETURN) maps cleanly onto OpenClaw's primitives.

### **8.1 Architectural Mapping**

| Syncrescendence Phase | OpenClaw Primitive | Implementation Strategy |
| :---- | :---- | :---- |
| **CAPTURE** (Ingestion) | **Gateway Event Loop** | Configure cron jobs with sessionTarget: "main" to periodically ingest state or listen for systemEvent webhooks. Inbound messages automatically trigger this phase. |
| **DISPATCH** (Routing) | **sessions\_spawn / Routing** | Use **Multi-Agent Routing** to define "Lanes." Create specialized agents (e.g., "ResearchLane", "CodingLane") in agents.list. Use sessions\_spawn(agentId="ResearchLane") to dispatch tasks to these lanes. Use cron with sessionTarget: "isolated" for scheduled dispatch tasks.3 |
| **RETURN** (Synthesis) | **Announce Step** | The sessions\_spawn lifecycle automatically handles the Return phase. When the sub-agent completes, the Gateway injects a structured result (Status \+ Result \+ Notes) back into the parent session, closing the loop.2 |

### **8.2 Memory Systems Comparison**

* **Syncrescendence (Repo-based):** Relies on a Git repository as the authoritative ground truth.  
* **OpenClaw (Hybrid):** Uses a dual approach.  
  * **Durable:** MEMORY.md (curated knowledge).  
  * **Ephemeral:** memory/YYYY-MM-DD.md (daily logs).  
  * **Search:** memory\_search uses a hybrid SQLite Vector Search (semantic) \+ FTS5 (lexical) index.11  
* **Integration:** OpenClaw is designed for "organic" conversation recall. To integrate Syncrescendence's repo-truth, you should bypass the vector store for authoritative data. Configure a skill that instructs the agent to use exec to grep or read the Syncrescendence repo directly, treating the file system as the source of truth rather than the vector index.

### **8.3 External Tool Triggers (Gemini/Claude)**

OpenClaw can easily act as the orchestrator for external CLIs like Gemini or Claude Code.

* **Mechanism:** The exec tool.  
* **Pattern:** Define a Skill (e.g., gemini-cli) that instructs the agent: "To query Gemini, run exec(command='gemini query "..."')".  
* **Automation:** A cron job with sessionTarget: "isolated" can run a script that invokes these CLIs, processes their output, and then uses the message tool (via a curl webhook or sessions\_send) to report back.  
* **Requirement:** Ensure the CLI binaries are in the $PATH visible to the Gateway process and that the tools.profile or sandbox policy permits exec access.1

This architecture allows OpenClaw to serve as the local "Hypervisor," managing specialized CLI agents (Claude Code for coding, Gemini for reasoning) as subservient tools within its broader autonomous loops.

#### **Works cited**

1. Configuration \- OpenClaw, accessed February 3, 2026, [https://docs.openclaw.ai/gateway/configuration](https://docs.openclaw.ai/gateway/configuration)  
2. Multi-Agent Routing \- OpenClaw, accessed February 3, 2026, [https://docs.openclaw.ai/concepts/multi-agent](https://docs.openclaw.ai/concepts/multi-agent)  
3. Cron Jobs \- OpenClaw, accessed February 3, 2026, [https://docs.openclaw.ai/cron-jobs](https://docs.openclaw.ai/cron-jobs)  
4. Tools \- OpenClaw, accessed February 3, 2026, [https://docs.openclaw.ai/tools](https://docs.openclaw.ai/tools)  
5. Background process \- OpenClaw, accessed February 3, 2026, [https://docs.openclaw.ai/background-process](https://docs.openclaw.ai/background-process)  
6. openclaw/CHANGELOG.md at main \- GitHub, accessed February 3, 2026, [https://github.com/openclaw/openclaw/blob/main/CHANGELOG.md](https://github.com/openclaw/openclaw/blob/main/CHANGELOG.md)  
7. openclaw/openclaw v2026.1.20 on GitHub \- NewReleases.io, accessed February 3, 2026, [https://newreleases.io/project/github/openclaw/openclaw/release/v2026.1.20](https://newreleases.io/project/github/openclaw/openclaw/release/v2026.1.20)  
8. Agent Skills: Overview, accessed February 3, 2026, [https://agentskills.io](https://agentskills.io)  
9. Skills \- OpenClaw, accessed February 3, 2026, [https://docs.openclaw.ai/tools/skills](https://docs.openclaw.ai/tools/skills)  
10. Multi-Agent Sandbox & Tools \- OpenClaw, accessed February 3, 2026, [https://docs.openclaw.ai/multi-agent-sandbox-tools](https://docs.openclaw.ai/multi-agent-sandbox-tools)  
11. Deep Dive: How OpenClaw's Memory System Works | Study Notes, accessed February 3, 2026, [https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive](https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive)