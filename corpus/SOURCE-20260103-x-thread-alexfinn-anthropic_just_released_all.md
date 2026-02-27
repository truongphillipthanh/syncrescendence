# Anthropic Just Released ALL the Claude Code Secrets

**Anthropic just released ALL the Claude Code secrets**

Their Prompting best practices just went live in their docs and I spent hours reading it and testing out all the tips

**Here are the 10 that make Claude Code so much better:** 🧵

(Description: Promotional graphic showing "Welcome to Claude Code" terminal interface with orange "CLAUDE CODE" text and "Press Enter to continue" command)

---

## 1. 🔶 Use Github early and often

Once you connect CC to git, it gets access to your entire commit history

Meaning it will know about **EVERY change you've ever committed**, making it **SO much more powerful**

This will reduce hallucinations a ton. Connect CC to git right away

(Description: GitHub commits interface showing command history with multiple staged commits and file modifications listed in a code editor interface)

---

## 2. 🔶 Load up your context

CC's context management has gotten **MASSIVE improvements** the last few weeks

It now compacts intelligently, allowing you to keep context for a **LONG time**

Don't be afraid to load context by having CC review your architecture at the beginning of sessions

(Description: Code editor screenshot showing system prompts and architectural review instructions: "Take a look at the app and architecture. Understand deeply how it works inside and out. Ask me any questions if there are things you don't understand. This will be the basis for the rest of our conversation")

---

## 3. 🔶 Adjust eagerness

Claude Opus 4.5 is an incredibly eager model. It asks for forgiveness, not permission

The eagerness to make changes is why I love CC. But if you don't like this eagerness, Anthropic wrote a new **CLAUDE rule** you can put in your rules file:
```
do_not_act_before_instructions
Do not jump into implementation or changes files unless clearly instructed to make changes. When the user's intent is ambiguous, default to providing information, doing research, and providing recommendations rather than taking action. Only proceed with edits, modifications, or implementations when the user explicitly requests them.
</do_not_act_before_instructions>
```

---

## 4. 🔶 Be careful with the word 'think'

'**Think**' is the only word you can use with Claude Code that triggers extra token usage

If you are tight on budget or tokens, avoid using the word **'think'** '**think more**' or **'ultrathink'**

Instead use **'evaluate'** or **'consider'**

---

## 5. 🔶 Use vision

Claude Opus 4.5 is the **greatest vision model of all time**

Meaning, it can analyze and understand images better than any other model

Make sure to use as many images as you can. I like to use them for debugging and visual inspiration

Just paste directly into CC!

---

## 6. 🔶 Parallel tool calls

Claude Opus 4.5 is the **best model ever at tool usage**. It's incredibly agentic

With this new **CLAUDE rule** Anthropic created, you can have CC use tools in parallel, increasing efficiency

Just place this in CLAUDE .MD: (give image to claude to extract text)
```
use_parallel_tool_calls
If you intend to call multiple tools and there are no dependencies between the tool calls, make all of the independent tool calls in the same block, otherwise you MUST wait for previous calls to finish first to determine the dependent values (do NOT use placeholders or guess missing parameters). Prioritize calling tools simultaneously whenever the actions can be done in parallel rather than sequentially. Never use placeholders or guess missing parameters in tool calls.
</use_parallel_tool_calls>
```

---

## 7. 🔶 Reduce hallucinations

Claude's eagerness has some downsides

It will often make edits to files without truly understanding its purpose first

This new CLAUDE .md rule straight from Anthropic will fix that:
```
investigate_before_answering
Never speculate about code you have not opened. If the user references a specific file, you MUST read the file before answering. Make sure to investigate and read relevant files BEFORE answering questions about the codebase. Never make any claims about code before investigating unless you are certain of the correct answer - give grounded and hallucination-free answers.
</investigate_before_answering>
```

---

## Conclusion

**Implement these tips, and Claude Code will perform so much better for you!**

There's much more to their prompting guide, I'll link it in the next post.

**Make sure to hit like on the first post if you learned anything!**