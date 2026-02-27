[[00:00](http://www.youtube.com/watch?v=P60LqQg1RH8&t=0)]

**LEON VAN ZYL**: In this video, we are looking at sub-agents and background agents. Understanding how sub-agents work and knowing how to run specialized agents in the background is a critical skill to have, whether you are vibe coding or using agentic coding as an experienced developer. By the end of this video, you will know exactly what sub-agents are and how to create your own specialized agents. I will also demonstrate my workflow for implementing complex solutions.

To begin, let's look at Claude Code. I am going to switch over to planning mode and ask the agent to list all the sub-agents it has access to. Claude Code already has several built-in sub-agents. It has a bash agent, which is a specialist for running bash commands like git operations and terminal tasks. There is a general-purpose agent for researching complex questions and executing multi-step tasks, which is ideal for searches where you aren't confident in finding the right match quickly. There is also a status line setup agent used for the dashboard, an explore agent that uses the fast and cheap Haiku model for searching code patterns, a planning agent for investigating requirements, and a Claude Code guide agent for feature-related questions.

You can call an agent directly by entering the `@` symbol followed by the agent name, such as `@claude-code-guide`. You can also run any of these agents in the background by pressing `Ctrl+B`. This frees up the main agent, allowing you to continue the conversation while waiting for the background agent to complete its task.

[[03:07](http://www.youtube.com/watch?v=P60LqQg1RH8&t=187)]

**LEON VAN ZYL**: We can also get the main agent to call sub-agents for us without using the `@` symbol. To demonstrate, I've set up a basic Next.js boilerplate project. We can get the explore agent to analyze the codebase and provide a summary of features and the tech stack. While the main agent could do this work, it is a bad idea because we want to keep the main conversation clean and clutter-free.

If I ask the main agent to summarize the tech stack without sub-agents, all tool responses and the final response contribute to the context usage, which might sit around 15%. However, if I prompt it to use two explore agents in parallel, the main agent launches them to investigate the stack and features simultaneously. You can monitor these background tasks by pressing the down arrow and Enter.

Multitasking allows one agent to investigate the tech stack while another focuses on core features. Usually, a single agent would have to go through everything sequentially, which takes longer. Furthermore, the more specific the scope for an agent, the better the results. In a complex project, the quality difference between a single agent and specialized sub-agents is night and day.

[[06:35](http://www.youtube.com/watch?v=P60LqQg1RH8&t=395)]

**LEON VAN ZYL**: Creating your own agents is straightforward. Simply run the `/agents` command. You can create agents at the project level or personal level; personal agents are available across all your projects. To create one, you describe the agent—for example, a UI/UX expert with 20 years of experience who ensures the application uses a "neo-brutalism" design with bright colors and hard shadows.

After describing the agent, Claude writes the system prompt. You then select the tools the agent can access and the model it should use, such as Opus, Sonnet, or Haiku. After naming the agent—for instance, "UI Expert"—it appears in the `.claude` folder. To ensure the agent is recognized, you may need to exit and restart Claude Code. Once active, you can ask the main agent to invoke the UI expert to review the application and make changes.

The primary benefit here is protecting the context window. Large language models have a maximum context window size, and when you exceed it, the quality of responses decreases as earlier parts of the conversation are dropped. By offloading work to sub-agents, each runs in its own thread with its own conversation context. This means 50,000 tokens used by a sub-agent do not affect the 200,000-token limit of the main agent. Sub-agents return a short summary to the main thread, greatly reducing token bloat.

[[14:31](http://www.youtube.com/watch?v=P60LqQg1RH8&t=871)]

**LEON VAN ZYL**: To further optimize a workflow, we can create a "Coder" agent and a "Code Reviewer" agent. The Coder agent should be an experienced developer focused on performant, secure, and well-commented code. The Code Reviewer agent checks completeness against requirements and ensures modularity. For code reviews, even the Haiku model does a surprisingly good job at identifying glaring issues.

Before implementing a complex feature, enter planning mode. Instead of letting the main agent plan everything, you can ask it to use three planning agents in parallel to investigate different aspects of the application. For a complex project—like a Kanban to-do list app with local storage, Postgres, Drizzle ORM, and "Better Auth" authentication—doing everything in a single conversation would hit the context limit almost immediately.

By using sub-agents for the planning phase, the main thread stays clean. In one example, sub-agents consumed 80,000 tokens, but the main thread usage only increased slightly to 26%. If the main agent had done the work, usage would have been closer to 60%. Once a plan is generated, I recommend storing it in a `spec` folder within the project root. This plan can then be handed over to a team of sub-agents for execution.

[[24:00](http://www.youtube.com/watch?v=P60LqQg1RH8&t=1440)]

**LEON VAN ZYL**: The most advanced way to use these agents is to have the main agent act as a coordinator. You can instruct the main agent to look at the implementation plan, identify tasks that can be done in parallel, and create different "tracks." For each track, the main agent kicks off a Coder sub-agent. Once the work is done, it hands the code to a Code Reviewer agent for feedback. This cycle continues until the feature is complete.

This orchestration allows you to build a fully functional application—including authentication and database integration—while only using a fraction of the context window. In my demonstration, the entire project was implemented using background agents, and we only used 58% of the main context window.

After the initial build, you can use the review agents to identify security or accessibility issues. You can then task Coder sub-agents to fix these critical issues in parallel. This methodology ensures that even deep into a build, you still have plenty of context available for bug fixes and refinements. Using sub-agents isn't just about saving tokens; it's about maintaining the "intelligence" of the main agent by preventing the fragmentation that occurs when a conversation becomes too long.

---