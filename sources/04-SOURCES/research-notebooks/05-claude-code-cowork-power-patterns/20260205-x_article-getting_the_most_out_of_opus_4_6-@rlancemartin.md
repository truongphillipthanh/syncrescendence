---
url: https://x.com/RLanceMartin/status/2019482019324219477
author: Lance Martin (@RLanceMartin)
captured_date: 2026-02-05
---

# Getting the Most Out of Opus 4.6

Claude Opus 4.6 adds a new adaptive thinking mode and several API improvements to help with context management for long-running tasks. Here's an overview of Opus 4.6 with links to some useful API docs.

## Adaptive Thinking

Several papers have explored how Claude thinks. Sonnet 3.7 introduced extended thinking, which gave Claude space to plan **before** taking action.

Further research showed that Claude benefits from thinking **between** actions in multi-step agentic tasks. Claude 4 added this as interleaved thinking.

Thinking has been controlled with the `budget_tokens` parameter in the API and with thinking-mode or keywords (e.g., ultrathink) in Claude Code.

> A little counter-intuitive, but I recommend using Opus with thinking for everything if you can. Because it's more intelligent, it reduces both cost and latency vs. not using thinking or not using Opus
>
> — Boris Cherny (@bcherny), Jan 1

(Description: Bar chart showing "Multidisciplinary reasoning" performance on "Humanity's Last Exam" comparing Opus 4.6 vs Opus 4.5 vs Sonnet 4.5 vs Gemini 3.7 vs Gemini Deep Research vs GPT-3.2 vs GPT-5.2 Pro, with and without tools. Opus 4.6 shows 53.1% accuracy without tools and 40.0% with tools, demonstrating significant improvements in reasoning capabilities.)

Opus 4.6 extends the frontier of expert-level reasoning.

Opus 4.6 also introduces **adaptive thinking**, which takes out the guesswork of thinking budget. Claude dynamically decides when and how much to think based upon the task complexity. Here's how to enable it:
```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    thinking={
        "type": "adaptive"
    },
    messages=[{
        "role": "user",
        "content": < your message >
    }]
)
```

The effort parameter acts as soft guidance for Claude's thinking allocation. Effort is a behavioral signal, not a strict token budget.

At lower effort, Claude will still think on sufficiently difficult problems. It will just think less than it would at higher effort levels for the same problem. You can learn more about general guidance on prompting Opus 4.6.

## Context Management

Opus 4.6 improves on its predecessor's coding skills and sustains agentic tasks for longer. Context management is a central problem in long-horizon tasks and Opus 4.6 has a few features to help.

### Context Window

Opus 4.6 has an **expanded context window with 1M tokens**. A larger context window offers more space for long-horizon tasks.
```python
from anthropic import Anthropic

client = Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": < your message >}
    ],
    betas=["context-1m-2025-08-07"]
)
```

### Context Awareness

Opus 4.6 also has **context awareness**, enabling Claude to track its remaining context and understand how much space it has left.

### Context Pruning

Opus 4.6 will **automatically strip old thinking blocks** when using adaptive thinking, preserving token capacity for conversation content. There's also fine controls for context editing to clear old tool results, which is a common source of context bloat.

(Description: Diagram showing context editing impact. "Before context editing" shows a sequence of tool uses and results stacked horizontally (Tool Use 1, Tool Result 1, ..., Tool Use N, Tool Result N, etc.). "After context editing" shows the same sequence but with old tool results removed, leaving only Tool Use 1, Tool Result 1, Tool Use N, Tool Result N+1, and "Available Context" highlighted in green at the end.)

### Context Compaction

Claude Code uses compaction to summarize the conversation and preserve important context (e.g., decisions or errors). Opus 4.6 brings compaction to the API and will handle this for you.
```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112"
            }
        ]
    }
)
```

Here is the flow for context compaction:

(Description: Flow diagram with "Server" label showing sequence: "Input tokens exceed trigger threshold" → "Conversation is summarized" → "Compaction block created with summary" → "Response continues with compacted context". Below is "Client" section showing "Append response to messages" with note "Messages before the compaction block are dropped on next request".)

### Context Isolation with Sub-agents

Many agent harnesses use sub-agents for context isolation. Opus 4.6 has improved subagent orchestration, recognizing when tasks would benefit from delegating work to specialized subagents. Prompting best practices provides some useful guidance:

**Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams. For simple tasks, sequential operations, or single-file edits, work directly rather than delegating.**