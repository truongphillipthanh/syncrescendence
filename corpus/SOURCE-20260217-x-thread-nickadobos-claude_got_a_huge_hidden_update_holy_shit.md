Claude got a huge hidden update. Holy shit.

Before:
User prompt -> Claude -> uses tool -> Claude

After:
User prompt -> Claude -> writes code and logic -> that code uses a tool -> code logic can parse or format results, add conditional logic and use tool multiple times -> Claude

This unlocks crazy amounts of complex function calling. 

For example, say you are querying a database. Previously you would do one query, then Claude would read that result and then query again if needed. Now Claude writes code to call the tool, then that code can handle the result and do different things, like query again, strip or format data, and change what it's doing based on the tool call result, all before being sent back to Claude. The code, that Claude writes, pre plans how to react to the tool result. 

This compresses LLM agent loops, because the agent isn't deciding on the fly, and it doesn't need to keep asking the LLM to make decisions, instead the LLM pre-bakes potentially hundreds or thousands of decision paths.

I would not be surprised if we see eventually 2x-100x improvements or more on agent loop & tool calling efficiency scores from this design.