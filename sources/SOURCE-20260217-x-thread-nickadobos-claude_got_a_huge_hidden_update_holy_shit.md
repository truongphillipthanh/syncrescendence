---
url: https://x.com/NickADobos/status/2023861257757925469
author: "Nick Dobos (@nickadobos)"
captured_date: 2026-02-20
id: SOURCE-20260217-021
original_filename: "20260217-x_thread-claude_got_a_huge_hidden_update_holy_shit-@nickadobos.md"
status: triaged
platform: x
format: thread
creator: nickadobos
signal_tier: strategic
topics: [claude-code, ai-engineering, llm-architecture]
teleology: extract
notebooklm_category: ai-engineering
aliases: ["nickadobos - Claude hidden tool-use update"]
synopsis: "Identifies a significant hidden update to Claude's tool calling: instead of the old pattern (user -> Claude -> tool -> Claude), Claude now writes code that pre-plans how to react to tool results, handling conditional logic, multiple tool calls, and data parsing before returning to the LLM. This compresses agent loops by pre-baking potentially hundreds of decision paths."
key_insights:
  - "New pattern: Claude writes code that calls tools, parses results, adds conditional logic, and calls tools multiple times — all before returning to the LLM"
  - "This compresses LLM agent loops because the agent pre-bakes decision paths instead of deciding on the fly after each tool call"
  - "Potential 2x-100x improvements in agent loop and tool calling efficiency from this code-mediated tool use design"
---
Claude got a huge hidden update. Holy shit.

Before:
User prompt -> Claude -> uses tool -> Claude

After:
User prompt -> Claude -> writes code and logic -> that code uses a tool -> code logic can parse or format results, add conditional logic and use tool multiple times -> Claude

This unlocks crazy amounts of complex function calling. 

For example, say you are querying a database. Previously you would do one query, then Claude would read that result and then query again if needed. Now Claude writes code to call the tool, then that code can handle the result and do different things, like query again, strip or format data, and change what it's doing based on the tool call result, all before being sent back to Claude. The code, that Claude writes, pre plans how to react to the tool result. 

This compresses LLM agent loops, because the agent isn't deciding on the fly, and it doesn't need to keep asking the LLM to make decisions, instead the LLM pre-bakes potentially hundreds or thousands of decision paths.

I would not be surprised if we see eventually 2x-100x improvements or more on agent loop & tool calling efficiency scores from this design.