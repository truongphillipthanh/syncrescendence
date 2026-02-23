---
url: https://x.com/deepfates/status/2019912654173651131
author: "@deepfates"
captured_date: 2026-02-06
id: SOURCE-20260206-029
original_filename: "20260206-x_thread-in_my_quest_to_understand_the_true_nature_of_an_agent-@deepfates.md"
status: triaged
platform: x
format: thread
creator: deepfates
signal_tier: paradigm
topics: [ai-agents, llm-architecture, ai-engineering, research, framework]
teleology: synthesize
notebooklm_category: ai-agents
aliases: ["deepfates - Recursive Language Model"]
synopsis: "Proposes that agents are not chatbots but programming languages come alive. Introduces the Recursive Language Model (RLM) architecture where the LLM is hooked directly to a REPL, context is a variable, and both users and sub-LLMs become functions inside the computational environment. Reports processing 6M tokens without context degradation by spawning sub-agents that pass variables without reading their contents."
key_insights: ["The RLM architecture puts the agent inside the computer rather than having a chat as the 'main world' — users and sub-LLMs become tools within the environment", "Context rot is solved by offloading long-term memory to variables that sub-agents can operate over without reading into the main context window, making it effectively infinite", "Future agents will feel like councils, senates, and hive minds rather than single chat-thread instance minds — post-training must find patterns for multi-agent, multi-channel worlds"]
---
# Agents as Programming Languages Come Alive

In my quest to understand the true nature of an Agent I have been thinking a lot about the loop and the actions and the environment. And I think i see where we're headed next.

**Agents are not going to be like chatbots. They are going to be like programming languages come alive.**

---

Right now most people's working definition of an agent is "a language model in a loop with some tools", right? This is the ReAct paradigm we've been using for 3 years at least. The models are trained around it, from data formatting to inference stack. Tool calling, function calling, MCPs all rely on this turn-by-turn structure. But context is still the bottleneck, and all the tool call inputs and outputs still have to go through the input.

In the meantime we had things like CodeAct, and Code Mode, and Claude Code, that give the model access to some kind of REPL (Read Eval Print Loop, an interactive computational environment, like a terminal or a programming language notebook). And we've seen models simulate computer environments as well, like in worldsim and Infinite Backrooms.

People realized the model didn't have to simulate just a chatbot. It could simulate a computer. Or a computer user.

And once you get RL with verifiable rewards, computer environments suddenly became the thing for models to learn. You can tell whether your model did things right by how well the code runs!

So post-training baked in computer use, shell environments, bash tool, and suddenly you have models that are good at predicting what a computer will do in response to complicated programs and commands. Computers that can use themselves.

The user is still in a privileged position. The outer conversation loop with the model is still "the main world". But it can do stuff in its computational environment and that stuff persists. The squishy human is no longer the whole environment. There is an ontologically hard reality and it's the computer world, the files and folders and programs within.

---

The Recursive Language Model (RLM) pushes this a step further: **What if we don't have a "chat" at all? What if we make the user just a function inside the computer? In fact, what if we put the agent inside the computer too?**

So the RLM hooks up the language model directly to the REPL and puts the context in as a variable. The LLM can operate over large documents or its own memories or whatever is in that context variable. And it can call the human user with a final answer, or call a sub-LLM with its own {prompt, context} input.

This week I built a recursive language model in typescript, and watched it process over 6M tokens without degrading from context rot. It feels… different.

You ask it to do something and it writes code that spawns more of itself and then merges back just knowing the answers. The context window hasn't grown almost at all, no matter how much work the sub-agents did, because they can send variables around without reading what's inside them. You can have an ongoing conversation where the long-term memory is offloaded to a variable, and the agent can operate over its own memories, so the "context window" is effectively infinite.

These new agents will feel less like coworkers, or slowly dying houseplants, than what we have now. They will feel like councils, senates, hive minds. They will be composed of many minds working and communicating. Right now, the models only know "user" and "assistant" and "tool". Future post-training will have to find patterns for a multi-agent, multi-channel world.

In a way, the user and the sub-llms become tools within the environment. We are no longer building single chat-thread instance minds. We are building an intelligent System of software, hardware, and wetware, a program that writes programs, where each of us is a moving part.

**Haven't you always wanted to be part of something?**

---

## RLM Architecture Diagram

(Description: A detailed flowchart diagram showing the Recursive Language Model architecture at multiple depths. At the root level (depth=0), a "query" box (purple) connects to a "Language Model" box (green), with "context" flowing in from a yellow box on the left, and "final response" (pink box) flowing out on the right. Below this is a central red box labeled "the agent lives here!" pointing to an "Environment E (e.g. REPL)" box (salmon/coral colored) in a light blue container.

The diagram branches into two RLM (depth=1) sections at the bottom:
- Left side shows sub-query 1 and sub-context 1 feeding into a Language Model, with sub-response 1 output
- Right side shows sub-query 2, sub-context 2, and sub-query 3 feeding into a Language Model, with sub-response 2 output

The right side's Environment E box further branches into three parallel execution paths (indicated by ellipses), representing recursive depth expansion.)

---

*Posted 3:14 PM · Feb 6, 2026 · 49.1K Views*