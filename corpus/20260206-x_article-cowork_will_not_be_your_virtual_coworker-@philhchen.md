# Cowork will not be your virtual coworker

I built a Claude Cowork clone in 3 days. Here's what I learned.

![Cowork interface](Description: Anthropic's Cowork interface showing a dark-themed chat application with the title "Let's knock something off your list" and an orange loading spinner icon. A system message displays: "Cowork is an early research preview. New improvements ship frequently. Learn more or give us feedback. Cowork can be usage intensive. For the best experience, consider upgrading to Max." Below are three task options with icons: "Optimize my week," "Organize my screenshots," and "Find insights in files.")

## Replicating an app only costs $250. Debugging it takes more.

The first big learning was how easy it was to reproduce an app. I gave Opus and Codex screenshots of the app, descriptions of my desired user flow, and the documentation. After 20 hours, $250 in Opus API credits, and support from Codex to fix the trickiest bugs, I was able to produce a buggy MVP with frontend, backend, and rudimentary AI interaction.

I used a pretty simple setup with multiple simultaneous Claude Code and Codex sessions in tmux and wondered if I was missing out on 10x productivity gains from plugins or specialized agent configs. But after implementing the MVP, I spent much more time identifying and fixing bugs than building. As a result, the biggest productivity gain for me was from asking the models how I could verify their work and leveraging the models to help find and fix bugs.

When addressing bugs, I found the interactions with Claude and Codex to be frustrating for different reasons. Claude tried to deceive me on multiple occasions, claiming that it had solved bugs I had pointed out when in fact it had changed the tests. Codex was much more thorough but could not run the majority of useful commands for testing and validating its own work. While Codex was slow at implementation, it excelled at both writing tests against the design docs and fixing bugs.

![Cowork clone comparison](Description: Side-by-side comparison showing Cowork (left) and the author's clone (right). Left side displays a Google Docs task about "Improve Rework Google Doc" with a multi-step progress list. Right side shows the same task in the clone interface with a "Rework" task panel, showing progress tracking and context including Google Drive and Notion integration options.)

## Detailed system prompts teach Claude Code how to be a software engineer.

The next step after the MVP was to transform it from a chatbot into a local agent. I liked the simple API of Claude Agent SDK, but I wanted more fine-grained control over the agent orchestration and multi-provider support. I pointed Claude / Codex at the Agent SDK docs to reproduce the same interface.

The main challenge of implementing the agent was actually replicating the context engineering of Claude Code and Codex. Claude Code steers the model through injections of very detailed "system reminder" content. For example, one system reminder at the beginning of a task encourages the model to use the TodoWrite tool so users can see how the model divides the current task into high-level steps. For the model to really pay attention to a system reminder, I needed to inject it into user or tool messages, even if it wasn't truly a message from the user or the tool. Entire features, such as plan mode, depended on having detailed system reminders injected into the latest user message to ensure that the correct tools would be called.

The impact of context engineering on output quality cannot be overstated. Using Haiku with the system reminders outperformed using Opus without. The entire system felt very brittle. Changing which message the system reminders were added to, or whether they were prepended or appended to the message dramatically affected performance.

While studying Claude Code's [current set of system prompts, tool descriptions, and system reminders](https://github.com/Piebald-AI/claude-code-system-prompts/tree/main), I noticed that they codified my intuitions on how to approach week-long software engineering projects. They did not capture long-term considerations regarding the evolution of codebases, and they also narrowly focused on software engineering best practices. For example, the system reminder for plan mode instructs the model to "not ask any questions that you could find out yourself by exploring the codebase," but this approach does not transfer to most roles in knowledge work.

## Software hasn't fully eaten the world.

Once my Cowork clone was ready, I was curious how different models would perform, compared to each other on my clone and to Claude on Cowork. I asked all the models to help me with my top priorities: preparing for meetings, organizing financial and legal paperwork, and reminding me of any outstanding action items.

For all three tasks, I found Gemini to be the fastest and most reliable. Flash performed every task in around a minute and successfully connected context across Slack, email, Calendar, Notion, and my personal files. Opus spent around 2-5 minutes on each task and missed some connections between more than two dots at a time (e.g. an email chain, a Slack message, and Notion docs). GPT 5.2 either spent way too much time (over 10 minutes) or failed to answer the question meaningfully.

I could not replicate Claude Code's magical experience, either with Cowork or my clone. The models failed to truly understand all of my personal context spread across email, calendar, personal files, Notion, and Slack. Reading through model traces, I observed that my tasks felt out-of-distribution for the models. Unlike software, the underlying context graph was much "fuzzier." The key entities for my tasks were people, communications between them, and the timing of these communications. This contrasts with software, where the key entities are the code, commands to run the software, and the outputs of those commands.

While I could bridge the gap by writing skills files to explain how to automate each of my tasks, I think these skills would be personal, context-dependent, and continuously evolving. Skills alone cannot scale to become my virtual coworker.

So what is necessary for a virtual coworker? I'm thinking a lot about this and have more to share soon.

---

**Published:** 9:54 AM · Feb 6, 2026  
**Engagement:** 31 replies, 74 reposts, 649 likes, 1,696 bookmarks, 416.5K views