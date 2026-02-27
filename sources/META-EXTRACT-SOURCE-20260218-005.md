# Extraction: SOURCE-20260218-005

**Source**: `SOURCE-20260218-x-article-dabit3-how_to_build_a_custom_agent_framework_with_pi_the_agent_stack_powering_openclaw.md`
**Atoms extracted**: 71
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (9)

### ATOM-SOURCE-20260218-005-0002
**Lines**: 11-11
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> The PI packages are the same ones that power OpenClaw.

### ATOM-SOURCE-20260218-005-0016
**Lines**: 152-154
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> `pi-ai` uses official provider SDKs (e.g., OpenAI SDK, Anthropic SDK) under the hood, and the `api` field determines which SDK handles the request, allowing compatibility with OpenAI-compatible endpoints like Ollama or vLLM.

### ATOM-SOURCE-20260218-005-0029
**Lines**: 378-380
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> OpenClaw uses `steer` for real-time user messages (e.g., typing while the agent works) and `followUp` for programmatic chaining of tasks.

### ATOM-SOURCE-20260218-005-0032
**Lines**: 397-399
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Most users should start with `pi-coding-agent` and only use `pi-agent-core` directly if they require a custom agent without the built-in coding tools or session system.

### ATOM-SOURCE-20260218-005-0047
**Lines**: 490-492
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> OpenClaw uses one session file per channel thread, stored as `~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl`, ensuring each conversation is independent and crash-safe because JSONL is append-only.

### ATOM-SOURCE-20260218-005-0050
**Lines**: 525-528
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> OpenClaw uses tool factories to create workspace-scoped tools for each agent, then wraps them with middleware for permission checks, image normalization, and Claude Code parameter compatibility aliases.

### ATOM-SOURCE-20260218-005-0052
**Lines**: 562-563
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The `pi-coding-agent` handles long conversations exceeding the model's context window through compaction, which summarizes old messages while retaining recent ones.

### ATOM-SOURCE-20260218-005-0062
**Lines**: 609-611
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.60, epistemic_stability=0.70

> OpenClaw utilizes extensions for context pruning (trimming oversized tool results to save tokens) and compaction safeguards (replacing default summarization with a multi-stage pipeline that preserves file operation history and tool failure data).

### ATOM-SOURCE-20260218-005-0067
**Lines**: 757-761
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> A persistent coding assistant can be built in approximately 120 lines of code, capable of reading files, running commands, editing code, searching the web, and remembering conversations across restarts, with full history preserved through compaction in a JSONL session tree.

## Concept (20)

### ATOM-SOURCE-20260218-005-0004
**Lines**: 29-31
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> `pi-ai` is a PI package that provides a unified interface for communicating with various LLMs (Anthropic, OpenAI, Google, etc.), handling streaming, completions, tool definitions, and cost tracking.

### ATOM-SOURCE-20260218-005-0005
**Lines**: 33-35
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> `pi-agent-core` is a PI package that wraps `pi-ai` to implement an agent loop, allowing agents to define tools, call LLMs, execute tools, and feed results back until a task is complete.

### ATOM-SOURCE-20260218-005-0006
**Lines**: 37-39
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> `pi-coding-agent` is a PI package that provides a full agent runtime with built-in file tools (read, write, edit, bash), JSONL session persistence, context compaction, skills, and an extension system.

### ATOM-SOURCE-20260218-005-0007
**Lines**: 41-43
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> `pi-tui` is a PI package that offers a terminal UI library with features like differential rendering, Markdown display, multi-line editor with autocomplete, loading spinners, and flicker-free screen updates.

### ATOM-SOURCE-20260218-005-0010
**Lines**: 86-90
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `completeSimple` function in `pi-ai` returns an `AssistantMessage` object, which contains a `.content` array of typed blocks (text, thinking, toolCall), `.usage` for token counts, and `.stopReason` (e.g., "stop", "toolUse", "length", "error", "aborted").

### ATOM-SOURCE-20260218-005-0012
**Lines**: 120-123
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> `streamSimple` in `pi-ai` normalizes different provider streaming formats into a single set of events, including `start`, `text_start`, `text_delta`, `text_end`, `thinking_start/delta/end`, `toolcall_start/delta/end`, `done`, and `error`.

### ATOM-SOURCE-20260218-005-0015
**Lines**: 150-154
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The `api` field in `pi-ai` models determines which official provider SDK (e.g., OpenAI SDK, Anthropic SDK) handles the request, allowing compatibility with any endpoint supporting that SDK's API (e.g., Ollama, vLLM, Mistral for OpenAI-compatible endpoints).

### ATOM-SOURCE-20260218-005-0019
**Lines**: 176-178
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> `pi-agent-core`'s `Agent` class implements the standard agent loop, managing communication with an LLM, executing tool calls made by the LLM, and feeding results back until the model stops.

### ATOM-SOURCE-20260218-005-0028
**Lines**: 376-378
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> `steer` interrupts an agent's current work, skipping remaining tools and injecting a new message, while `followUp` queues a message to be processed after the agent completes its current tasks naturally.

### ATOM-SOURCE-20260218-005-0031
**Lines**: 394-396
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> `pi-coding-agent` is a production-ready agent built on `pi-agent-core` that includes built-in tools, session persistence, and extensibility.

### ATOM-SOURCE-20260218-005-0034
**Lines**: 409-410
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The `read` tool reads file contents and images, truncating text output to 2000 lines or 50KB, and supports `offset`/`limit` for pagination.

### ATOM-SOURCE-20260218-005-0035
**Lines**: 411-412
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The `bash` tool executes a shell command in the working directory, returning stdout and stderr truncated to the last 2000 lines or 50KB, with an optional `timeout`.

### ATOM-SOURCE-20260218-005-0036
**Lines**: 413-414
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The `edit` tool replaces exact text in a file, requiring `oldText` to match precisely for surgical edits.

### ATOM-SOURCE-20260218-005-0037
**Lines**: 415-416
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The `write` tool writes content to a file, creating it if it doesn't exist, overwriting if it does, and automatically creating parent directories.

### ATOM-SOURCE-20260218-005-0038
**Lines**: 420-421
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The `grep` tool searches file contents for a regex or literal pattern, returning matching lines with file paths and line numbers, respecting `.gitignore` and using ripgrep.

### ATOM-SOURCE-20260218-005-0039
**Lines**: 422-423
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The `find` tool searches for files by glob pattern, returning matching paths relative to the search directory and respecting `.gitignore`.

### ATOM-SOURCE-20260218-005-0040
**Lines**: 424-425
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The `ls` tool lists directory contents, sorting entries alphabetically with a `/` suffix for directories and including dotfiles.

### ATOM-SOURCE-20260218-005-0044
**Lines**: 450-451
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> `SessionManager.inMemory()` creates an ephemeral session that disappears when the process exits.

### ATOM-SOURCE-20260218-005-0054
**Lines**: 566-567
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.00, epistemic_stability=0.00

> An extension in the `@mariozechner/pi-coding-agent` framework is a TypeScript module that exports a function receiving an `ExtensionAPI`.

### ATOM-SOURCE-20260218-005-0057
**Lines**: 574-580
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> Extensions are mechanisms that modify how an agent behaves without the LLM's awareness, by hooking into lifecycle events (e.g., before LLM calls, before compaction, on tool calls, on session start) to implement logic like trimming tool results, custom summarization, permission gating, or injecting context.

## Framework (5)

### ATOM-SOURCE-20260218-005-0001
**Lines**: 4-10
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> PI is a toolkit for building AI agents, structured as a monorepo of layered packages: `pi-ai` for LLM communication, `pi-agent-core` for the agent loop and tool calling, `pi-coding-agent` for a full coding agent with built-in tools and persistence, and `pi-tui` for a terminal UI.

### ATOM-SOURCE-20260218-005-0021
**Lines**: 197-202
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> An `AgentTool` in `pi-agent-core` is defined by a `name` (LLM identifier), `label` (human-readable), `description` (LLM usage instructions), `parameters` (TypeBox schema for type-safe validation), and an `execute` function that runs the tool and returns `content` (for LLM) and `details` (for UI).

### ATOM-SOURCE-20260218-005-0033
**Lines**: 402-404
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> `pi-coding-agent` includes 7 built-in tools: `read`, `bash`, `edit`, `write` (active by default as `codingTools`), and `grep`, `find`, `ls` (available but off by default).

### ATOM-SOURCE-20260218-005-0041
**Lines**: 427-430
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Built-in tools in `pi-coding-agent` are organized into presets: `codingTools` includes `read`, `bash`, `edit`, `write` (default), and `readOnlyTools` includes `read`, `grep`, `find`, `ls` for exploration without modification.

### ATOM-SOURCE-20260218-005-0061
**Lines**: 606-608
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.80

> Key extension events include `context` (rewrite messages), `session_before_compact` (customize summarization), `tool_call` (intercept tool invocations), `before_agent_start` (inject context/modify prompt), and `session_start`/`session_switch` (react to session changes).

## Praxis Hook (37)

### ATOM-SOURCE-20260218-005-0003
**Lines**: 14-15
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To build production-grade agentic software without vendor lock-in, understand how to compose the layered PI packages.

### ATOM-SOURCE-20260218-005-0008
**Lines**: 47-58
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up a PI agent project, create a directory, initialize npm, install `@mariozechner/pi-ai`, `@mariozechner/pi-agent-core`, `@mariozechner/pi-coding-agent`, `@mariozechner/pi-tui`, `chalk`, `typescript`, `@types/node`, and `tsx`, then set your API key as an environment variable (e.g., `ANTHROPIC_API_KEY`).

### ATOM-SOURCE-20260218-005-0009
**Lines**: 63-84
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To make a basic LLM call using `pi-ai`, import `getModel` and `completeSimple`, get a model instance (e.g., `getModel("anthropic", "claude-opus-4-5")`), and then call `completeSimple` with a system prompt and user messages.

### ATOM-SOURCE-20260218-005-0011
**Lines**: 93-119
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To stream LLM responses with `pi-ai`, use `streamSimple` instead of `completeSimple`, then iterate over the `stream` events, handling `text_delta` for text chunks and `done` for the final message.

### ATOM-SOURCE-20260218-005-0013
**Lines**: 128-135
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To switch LLM providers in `pi-ai`, only change the `getModel` call (e.g., `getModel("openai", "gpt-4o")`), ensuring the corresponding API key is set as an environment variable.

### ATOM-SOURCE-20260218-005-0014
**Lines**: 137-151
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Custom models for self-hosted endpoints can be defined in `pi-ai` by creating a `Model` object with `id`, `name`, `api` (e.g., "openai-completions"), `provider`, `baseUrl`, and other configuration details.

### ATOM-SOURCE-20260218-005-0017
**Lines**: 155-162
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> API keys for `pi-ai` are automatically resolved from environment variables based on provider name (e.g., `OPENAI_API_KEY`) or can be passed directly as an `apiKey` option in the `streamSimple` function.

### ATOM-SOURCE-20260218-005-0018
**Lines**: 165-170
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To enable extended thinking levels (e.g., "minimal", "low", "medium", "high", "xhigh") for models that support it (e.g., Claude, o3, Gemini 2.5) in `pi-ai`, set the `reasoning` option when calling `streamSimple`.

### ATOM-SOURCE-20260218-005-0020
**Lines**: 194-196
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When defining an `AgentTool` in `pi-agent-core`, pass the TypeBox schema as a generic parameter to `AgentTool<typeof schema>` to enable TypeScript to infer parameter types correctly within the `execute` function.

### ATOM-SOURCE-20260218-005-0022
**Lines**: 203-204
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> The `onUpdate` callback within an `AgentTool`'s `execute` function allows streaming partial results during tool execution, which is useful for long-running operations.

### ATOM-SOURCE-20260218-005-0023
**Lines**: 207-220
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To create an `Agent` in `pi-agent-core`, instantiate it with an `initialState` object containing a `systemPrompt`, `model`, an array of `tools`, and a `thinkingLevel`, along with a `streamFn` (e.g., `streamSimple` from `pi-ai`) to connect to the LLM provider.

### ATOM-SOURCE-20260218-005-0024
**Lines**: 223-242
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To monitor an `Agent`'s activity in `pi-agent-core`, subscribe to its event stream and handle various event types such as `agent_start`, `message_update` (for streaming text), `tool_execution_start`, `tool_execution_end`, and `agent_end`.

### ATOM-SOURCE-20260218-005-0025
**Lines**: 245-254
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.70

> Initiate an `Agent`'s operation by calling its `prompt` method with a user message; the agent will then autonomously manage the LLM interaction, tool execution, and result feedback loop.

### ATOM-SOURCE-20260218-005-0026
**Lines**: 361-367
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To interrupt an agent's current task and redirect it, use `agent.steer()` which delivers the message after the current tool finishes and skips remaining pending tools.

### ATOM-SOURCE-20260218-005-0027
**Lines**: 370-374
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To queue a message for an agent to process after it naturally finishes its current work without interruption, use `agent.followUp()`.

### ATOM-SOURCE-20260218-005-0030
**Lines**: 383-390
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> An agent's configuration can be changed at any time using methods like `agent.setModel()`, `agent.setThinkingLevel()`, `agent.setSystemPrompt()`, `agent.setTools()`, and `agent.replaceMessages()`, with changes taking effect on the next turn.

### ATOM-SOURCE-20260218-005-0042
**Lines**: 434-454
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To create an agent session, pick a `SessionManager` factory method based on your use case (in-memory, new persistent, open specific, or continue recent) and pass the resulting manager to `createAgentSession` along with the model.

### ATOM-SOURCE-20260218-005-0043
**Lines**: 440-441
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> `createAgentSession` is used to configure an agent with a model, tools, session persistence, and settings.

### ATOM-SOURCE-20260218-005-0045
**Lines**: 456-458
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> You can list existing sessions for a directory using `SessionManager.list(process.cwd())`.

### ATOM-SOURCE-20260218-005-0046
**Lines**: 461-489
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> For custom session logic, `SessionManager` provides methods like `buildSessionContext()` to reconstruct conversation, `getLeafEntry()` to get the last entry, `branch(entryId)` to fork conversation, `appendMessage(message)` to manually add messages, and `getTree()` to get the full session tree structure.

### ATOM-SOURCE-20260218-005-0048
**Lines**: 496-506
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To create tools that operate on a specific directory, use factory functions like `createCodingTools("/path/to/workspace")` or `createReadOnlyTools("/path/to/workspace")` instead of the singleton pre-built tool arrays.

### ATOM-SOURCE-20260218-005-0049
**Lines**: 508-524
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Tool factory functions accept an optional `operations` object to override underlying I/O, allowing tools to run in different environments like Docker containers, over SSH, or against virtual filesystems by providing custom `readFile`, `access`, or `exec` implementations.

### ATOM-SOURCE-20260218-005-0051
**Lines**: 531-559
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.70

> To add custom functionality beyond file operations and shell commands, define your own tools (e.g., `deployTool`) and pass them via the `customTools` array to `createAgentSession`; they will be available alongside built-in tools.

### ATOM-SOURCE-20260218-005-0053
**Lines**: 564-572
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> You can manually trigger compaction by calling `session.compact("Preserve all file paths and code changes.")` and provide an optional string to guide what the summary should preserve; `createAgentSession` enables auto-compaction by default when the context approaches the model's window limit.

### ATOM-SOURCE-20260218-005-0055
**Lines**: 566-570
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.00, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.60

> To create an extension, define a default export function that takes an `ExtensionAPI` object as an argument, allowing you to register event handlers and commands.

### ATOM-SOURCE-20260218-005-0056
**Lines**: 571-582
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.70

> Use `api.on("context", ...)` to rewrite the message array before every LLM call, for example, to prune large tool results older than 10 messages and exceeding 5000 characters.

### ATOM-SOURCE-20260218-005-0058
**Lines**: 581-583
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> An extension is a TypeScript module that exports a function receiving an `ExtensionAPI`, which allows it to register event handlers like `api.on("context", ...)` to rewrite message arrays before LLM calls or `api.on("session_before_compact", ...)` to replace default compaction logic.

### ATOM-SOURCE-20260218-005-0059
**Lines**: 584-594
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.70

> Implement `api.on("session_before_compact", ...)` to replace the default context compaction logic with custom summarization, returning a summary, `firstKeptEntryId`, and `tokensBefore`.

### ATOM-SOURCE-20260218-005-0060
**Lines**: 596-604
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.70

> Register user-facing commands (not LLM tools) using `api.registerCommand("commandName", { description: "...", handler: async (...) => { ... } })` to provide functionality like showing session statistics.

### ATOM-SOURCE-20260218-005-0063
**Lines**: 612-654
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.70

> To build a codebase assistant, use `@mariozechner/pi-coding-agent` to create an `AgentSession` with a specified model, `thinkingLevel`, `sessionManager` for persistence, and `customTools` like a web search tool.

### ATOM-SOURCE-20260218-005-0064
**Lines**: 645-649
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.70

> Implement session persistence by creating a `SessionManager` that opens a `.jsonl` file in a dedicated session directory, ensuring conversation history is remembered across restarts.

### ATOM-SOURCE-20260218-005-0065
**Lines**: 664-685
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.70

> Attach event handlers to the agent session using `session.subscribe()` to react to events like `message_update` (for streaming assistant responses), `tool_execution_start`/`end`, `auto_compaction_start`, and `agent_end`.

### ATOM-SOURCE-20260218-005-0066
**Lines**: 707-747
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.70

> Create a Read-Eval-Print Loop (REPL) for user interaction by using `readline` to prompt for input, handling commands like 'exit' and 'new' (to reset the session), and passing user prompts to `session.prompt()`.

### ATOM-SOURCE-20260218-005-0068
**Lines**: 759-761
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To manage credentials across multiple providers and support OAuth flows in a production environment, use `AuthStorage` and `ModelRegistry` classes, as demonstrated by OpenClaw.

### ATOM-SOURCE-20260218-005-0069
**Lines**: 762-763
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Initialize `AuthStorage` by creating an instance with a path to an `auth.json` file, and then create a `ModelRegistry` instance using this `authStorage` and a `modelsConfigPath`.

### ATOM-SOURCE-20260218-005-0070
**Lines**: 764-767
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Create an agent session using `createAgentSession` by passing the initialized `authStorage`, `modelRegistry`, and a specific model found via `modelRegistry.find("ollama", "llama3.1:8b")`.

### ATOM-SOURCE-20260218-005-0071
**Lines**: 765-766
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.70

> For production use, replace a single API key with `AuthStorage` and `ModelRegistry` to manage credentials across multiple providers and support OAuth flows.
