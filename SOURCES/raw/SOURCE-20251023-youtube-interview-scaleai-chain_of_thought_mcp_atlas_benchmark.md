# Chain of Thought | Leaderboard Deep Dive - Scale's MCP Atlas Benchmark

**Host:** Brad Kenstler (Head of Agent Capabilities and Environments, Scale AI)  
**Panelists:**  
- Chaitanya Bandi (ML Research Scientist, Scale AI)
- Sami Hassaan (AI Product Manager, Scale AI)
- Chetan Rane (Head of Product, Agents, Scale AI)

**Context:** Discussion of Scale AI's new MCP Atlas benchmark, which evaluates how well language models handle real-world tool use through the Model Context Protocol.

---

**Brad:** Welcome to Chain of Thought. On this week's episode, we're going to be talking about Scale's latest research in benchmarks, specifically for MCP evaluations and MCP agents. My name is Brad Kenstler. I'm the head of agent capabilities and environments research here at Scale.

**Chaitanya:** I've been working on the MCP for a while, so excited to share what we have.

**Sami:** I work as a product manager owning all things tool use.

**Chetan:** I lead the product team for agents and environments. We have lots of exciting updates to share on this new benchmark, which is one of the first to test out MCP capabilities. We'd love to dive into the research behind this, but do you mind giving us an overview of what MCP actually is?

**Chaitanya:** MCP stands for model context protocol. It's roughly in the name—it's a way for standardizing how you provide context to models. Other communication protocols exist, but this is the one that is the most widely adopted in terms of standardizing it. A brief context on that: LLMs are the brains of the system. We need, in order to make agents that are reliable, that are actually able to do things that we do on a day-to-day basis, they need access to information that they can retrieve externally and also be able to make changes in the state outside of their own internal memory.

**Sami:** And to do that, we need ways to connect LLMs with a lot of different tools. Now, MCP is the most widely adopted standardization of that. Previously we had many that weren't as widely adopted in terms of standardization, and this is a standard that has been really embraced by developers. It's gone viral, and AI is all a developer play—whatever developers embrace is what's going to be there for a while. MCP is something that developers really like.

**Brad:** I'm curious—what came before MCP? If I was building an agent application in 2022, how did I do that? And how does MCP sort of change the game for the space today?

**Chetan:** Typically back in 2022, the conversation was most around RAG systems. That's complementary to MCP, but it's having external information that you get and then plug into your LLM, so it's more grounded. But the communication between different servers, different external services and models—that wasn't standardized. OpenAI came up with their function calling API. That's one framework they provide. Other companies like LangChain, they have their own systems for how to standardize communication between models and external services. But MCP came out last year and it provided a way for both ends of it—the model builders to adopt it and also the third party services to come up with abstractions that anybody can then use.

**Chaitanya:** End of 2023 to be exact. But it's been amazing since they came out, led by Anthropic. And it's been great after that.

**Sami:** One of the exciting things about MCP is how the standardization around this protocol has made it easier for both sides of the ecosystem to build something that's compatible. If you're thinking about, hey, I'm a SaaS provider and I want to make my service readily available to MCP clients, or agents, I now have a protocol that I can design for. I can release an MCP server. And now anyone that's actually building an agent, it's dead simple for them to just use that MCP server, integrate it into their MCP client. This sort of decoupling of having to build fit-for-purpose connectors is what's really turbocharging a lot of this and making it exciting.

**Chaitanya:** Absolutely. There's three parts: there's the developer, and then there's all the model builders and LLMs here on the left, and then there's the developer and all the third party services here on the right. Each one of them can have its own line and how it's integrated. Developers had to write their own adapters, and MCP makes it such that you don't have to. Each one of those lines can be abstracted away and it's very simple to plug any third party service with any model builder as long as they adopt it, which recently we've seen a lot of companies adopt it.

**Brad:** What specifically about MCP makes it different from traditional APIs?

**Chetan:** It's more of a standard. Think of REST API for web development. Before that there used to be a lot of protocols for web development. REST API just made it easier for folks to educate themselves on how to build applications, and that's the standardization that's bringing out the power of MCP. It's more of—hey, is it the only way? It's not, but it's a standard way so that people can now take away that mental effort to build a new one.

**Sami:** That standardization definitely increases overall adoption, and MCP is obviously emerging as the de facto solution now for how we think models are going to interact with different services, different systems, and access data across them. I think to maybe contextualize this for the audience, can you give us a few examples of MCP servers that are maybe popular or that we think a lot of model developers are going to want to figure out how to integrate with and improve their capabilities on?

**Chetan:** This really depends on the use case that somebody targets, but you can have MCP servers for your ERP system or your CRM system or your communications channels or your productivity systems, note-taking, even your social media channels, depending on the use case. Let's take an example of Notion. A lot of folks take notes in Notion. They have an MCP server now, which means that now, regardless of which frontier model you are using—for example, Claude Desktop or some other application—if you hook up your Notion MCP server with it, now your model can interact with your notes. It can fetch notes based on queries that you have. It can create new notes. It can update them. And all of that through this standardized interface, which is your MCP server, which is hosted by Notion.

**Chaitanya:** Brave has an MCP server as well, so you can search the web. Google Drive has one, so you can access your documents, interact with them. GitHub, GitLab—these are all popular places where folks store their information. And if you're building any agent workflows, chances are you're going to use one or the other or sometimes all of them for your particular use case.

**Brad:** I'd also say that—not only are there MCP servers for different services and systems, but there are also MCP servers that provide different types of capabilities. We mentioned search, we mentioned CRM, document management. There are also MCP servers for things like data analytics. You can connect to databases. There are memory servers that allow you to persist information across different sessions. So the type of capabilities that MCP servers can expose is quite broad.

**Chetan:** One interesting thing also on the MCP server adoption is, there's the registry that Anthropic keeps track of, and I believe they are past a thousand MCP servers. That's like—

**Sami:** It's a lot.

**Chetan:** —such rapid growth. It's been under a year now. The rate at which people are developing it—that shows you how much energy is behind this whole MCP push. And I think it's going to stay for a while. It's definitely more powerful than you'd think initially, and it's something that has the potential to be—in my opinion—one of the most important pieces of infrastructure going into the age of AI agents, of AIs that are going to do stuff.

**Brad:** I think there's also—maybe it's worth discussing—who's actually building these MCP servers? Is it third party developers, open source community? Is it the companies themselves?

**Chetan:** That's a great question. The MCP servers are actually being built by all types of folks. The companies themselves build some—Anthropic has a few that are by Claude. Notion has an MCP server that's maintained by Notion. But a lot of them are the open source community and independent developers. The fact that this has gone viral has made it such that there are MCP servers for almost anything you want to interact with. And being able to use them is as simple as just connecting them to your MCP client. That standardization is really powerful. We ourselves, at Scale, have MCP servers for our products. We have one for Donovan, we have one for SEAL. We have what, four or five MCP servers ourselves.

**Brad:** For the different products that we have at Scale. And I think that gets at something important, which is—if you're a SaaS provider or if you're building a product and you want to make sure that it's accessible in the age of agents, having an MCP server is almost table stakes now for discoverability and integration into these agent workflows.

**Sami:** Absolutely.

**Brad:** All of this leads us naturally into—okay, we understand what MCP is, we understand the ecosystem, but how do we evaluate MCP capabilities? How does Scale think about measuring how good models are at actually using these MCP servers?

**Chaitanya:** The way we think about it is—ultimately agents need to execute tasks, and tasks are usually multi-step. They require you to break down a high-level objective into smaller steps, and each step might involve calling different tools, parsing the information, and then deciding what to do next. The challenge with evaluating this is that it's not just about whether the model can call a function. It's about whether it can discover the right tools, use them in the right sequence, handle errors, and synthesize all of that information into a coherent answer.

**Sami:** What we built with MCP Atlas is an evaluation framework that tests exactly that. We created realistic tasks that span multiple domains—things like customer support scenarios, data analysis workflows, research tasks. Each task requires the model to work with actual MCP servers, not simulated APIs or mock functions. The model needs to understand what tools are available, figure out which ones to use, call them correctly with the right parameters, interpret the results, and then continue the workflow until it completes the task.

**Chetan:** And I think what's important here is that we're testing in live environments. The MCP servers are actually running. The models are making real API calls. This isn't a synthetic benchmark where we've pre-computed all the possible paths. The environment is dynamic, which means the model has to actually reason about what it's doing at each step.

**Brad:** Can you walk us through what an actual evaluation looks like? Like what does the model see, what does it have to do?

**Chaitanya:** Sure. Let's say we have a task where the model needs to analyze a company's recent GitHub activity and create a summary report in Google Docs. The model first needs to discover that there's a GitHub MCP server available. It needs to authenticate, query for the right repository, pull recent commits and pull requests, maybe analyze code changes. Then it needs to switch to the Google Drive MCP server, create a new document, format it properly, and populate it with the analysis. Throughout this, it needs to handle things like rate limits, missing data, and errors in tool calls.

**Sami:** And we evaluate this on multiple dimensions. We're not just looking at whether the task was completed successfully. We look at intermediate steps—did the model call the right tools? Were the parameters correct? Did it handle errors gracefully? Did it discover the necessary tools without being told explicitly what to use? We have rubrics for each of these dimensions, and we score models accordingly.

**Brad:** This gets at something really important about the benchmark design. We wanted to move beyond just function calling accuracy. A lot of existing benchmarks test whether a model can predict the right function given a description. But that's not what agents do in the real world. In the real world, agents need to explore their environment, discover what's possible, and execute complex workflows.

**Chetan:** Exactly. And I think that's what differentiates MCP Atlas from other tool use benchmarks out there. We're testing end-to-end agent capabilities, not just narrow function calling skills.

**Sami:** Maybe we should talk about the actual benchmark itself—what's in it, how we designed it, what we're releasing?

**Chaitanya:** MCP Atlas consists of several hundred tasks spanning different domains and difficulty levels. We have simple tasks that might require one or two tool calls, and we have complex tasks that require 10, 15, 20 tool calls with sophisticated reasoning between them. The tasks are designed to test different aspects of tool use: discovery, planning, execution, error handling, multi-tool coordination.

**Sami:** And we're open-sourcing the entire thing. The task definitions, the MCP servers, the evaluation harness—everything is available on GitHub. We want the community to be able to use this, extend it, add their own tasks, build on top of it.

**Brad:** Why did you decide to open-source it?

**Chetan:** I think for a few reasons. One, we want to accelerate progress in this space. If everyone is evaluating on different benchmarks with different methodologies, it's hard to compare progress. By open-sourcing MCP Atlas, we're creating a shared standard that the community can rally around. Two, we want feedback. This is version one. There are probably edge cases we haven't thought of, tasks we should add, ways to improve the evaluation methodology. The best way to discover that is to get it into people's hands. And three, we think this is important for the ecosystem. If we want agents to actually work well with MCP servers, we need good benchmarks to drive that progress.

**Sami:** We're also hosting the results on our public leaderboard, so people can see how different models perform. We've evaluated all the major frontier models—Claude, GPT-4, Gemini, and others. The leaderboard gives you a transparent view of where each model stands.

**Brad:** How does MCP Atlas compare to other tool use benchmarks that are out there?

**Chaitanya:** There are a few notable benchmarks in this space. Berkeley has the function calling leaderboard, which focuses on whether models can correctly predict function calls given descriptions. Gorilla has APIBench, which tests API calling capabilities. ToolBench from Tsinghua tests tool use on simulated APIs. AgentBench has some multi-step scenarios.

**Sami:** What makes MCP Atlas different is really the focus on real environments and the MCP protocol specifically. Most other benchmarks either use simulated tools or test a narrower slice of capabilities. We wanted to test the full stack—from discovery to execution to error handling—in environments that actually matter to developers building with MCP.

**Chetan:** And I think the other thing is that MCP Atlas is designed to grow. The benchmark isn't static. We can add new MCP servers, new tasks, new evaluation criteria as the ecosystem evolves. It's a living benchmark in that sense.

**Brad:** Can you give us some specific examples of tasks in the benchmark? What does a typical task look like? What makes a task difficult?

**Sami:** Sure. Let me give you a few examples at different difficulty levels. On the simpler end, we have tasks like: "Search for recent papers on transformer architectures and save the top three results to a text file." This requires discovery of a search MCP server, making a search query, parsing results, and using a file system MCP server to save the information. It's a few steps, but the logic is fairly straightforward.

**Chaitanya:** In the middle range, we have tasks like: "Analyze the last week of GitHub commits in the main repository, identify any breaking changes, and post a summary to the team Slack channel." This requires authenticating with GitHub, querying commit history, analyzing diffs, understanding what constitutes a breaking change, formatting a message, and posting to Slack. The model needs to coordinate between multiple tools and apply domain knowledge.

**Sami:** On the harder end, we have tasks like: "A customer reported a bug in version 2.3.1. Find the relevant GitHub issue, trace the code changes in that version, determine the root cause, draft a technical explanation for the customer, and update the issue with your findings." This is complex because it requires multi-step reasoning, navigating uncertainty, synthesizing information from multiple sources, and producing a coherent output at the end.

**Brad:** And how do you evaluate these? What do the rubrics look like?

**Chaitanya:** Each task has a rubric that breaks down evaluation into several dimensions. We look at task completion—did the model ultimately accomplish the goal? We look at tool discovery—did it find the necessary MCP servers without being told? We look at tool execution—were the API calls correct with proper parameters? We look at error handling—when something went wrong, did the model recover gracefully? We look at reasoning—did the intermediate steps make sense and follow a logical plan? And for the final output, we evaluate correctness and quality.

**Sami:** These rubrics are designed to give us fine-grained signal about where models are succeeding and where they're failing. It's not just a binary pass/fail. We can see, for example, that a model is good at discovering tools but poor at error handling, or that it can execute simple workflows but struggles with complex multi-step reasoning.

**Brad:** So what did you actually find when you ran the benchmark? What are the results telling us?

**Chetan:** The results are really interesting. First, there's still a lot of room for improvement across the board. Even the best models are only achieving around 40-50% success rates on the hardest tasks. This tells us that we're testing capabilities that are genuinely challenging for current systems.

**Chaitanya:** Second, we see meaningful differences between models. The frontier models—Claude Sonnet, GPT-4, Gemini—perform substantially better than smaller models. But even among the frontier models, there are differences in what they're good at. Claude tends to be strong at reasoning and planning. GPT-4 is very good at tool execution. Gemini shows interesting strengths in error recovery.

**Sami:** Third, and this was surprising to us, the correlations between performance on different task types is actually quite low. What that means is that being good at one kind of tool use doesn't necessarily predict being good at another. A model might excel at data analysis tasks but struggle with communication tasks. This suggests that tool use is not a monolithic capability—it's a collection of different skills that need to be developed independently.

**Brad:** What about the relationship between model size and performance?

**Chaitanya:** We saw the expected trend that larger models generally perform better, but it's not purely a function of scale. A well-trained smaller model with good tool use data can outperform a larger model that hasn't been specifically trained for this. This suggests that there's signal in the training process that matters a lot.

**Chetan:** We also found that models struggle most with discovery and error handling. Many models can execute tool calls correctly when they know what to use, but figuring out which tools are available and recovering from failures—those are still weak points. This gives us clear direction on where training should focus.

**Sami:** And I think one of the most important findings is just how much models are failing on what seem like straightforward tasks. When you have to coordinate three or four tools in sequence, even simple errors compound quickly. A model might make a mistake in step two, and by step five it's completely off track. Building robustness into these multi-step workflows is a major challenge.

**Brad:** It sounds like there's a lot of low-hanging fruit for improvement.

**Chaitanya:** Absolutely. The error modes are often quite fixable—it's things like not parsing responses correctly, or not checking for errors before proceeding, or giving up too early when something fails. These are capabilities that can be trained.

**Chetan:** But there are also some harder problems. The planning challenges—when a model needs to break down a complex goal into the right sequence of steps—that's still really difficult. And the contextual reasoning—understanding not just what a tool does, but when it's appropriate to use it—that requires deeper semantic understanding.

**Brad:** Looking forward, where do you see this going? How do you think about the future of MCP and tool use benchmarks?

**Sami:** Tool use has been around for a while, and we're starting to see more investment on the post-training side in RL for tool use in general. We're also seeing more investment in tool use data in pre-training and mid-training, and base models are getting a firmer understanding of just agentic behavior and stateful actions in general. I think that will ultimately cascade downstream into gains during post-training. I also think that environments for training are going to get better—and I know that because we're going to play a big part in that.

**Brad:** But what I think is going to be true is that the environments that we evaluate are going to continue to get more complex. We're really excited about this benchmark, but this is just a starting point for us. We know that we want to continue to expand the horizon of complexities within our benchmarks. This captures a lot, but it's only step one. I'm pretty bullish that models are going to improve here, but there's going to be another one right around the corner that they need to climb as well. And I think we're going to continue to be a driving force for that.

**Chaitanya:** I agree. That makes a lot of sense. I'm also very excited about—with MCP, the thing that's most exciting is everybody, anybody can create an abstraction over any API and then contribute to this shared registry which can plug into any model. The more we do that, each additional MCP server increases the surface area for how useful of an application you can build. And I think that then means there's more adoption on the user side. With that compounding, I think we will see some very solid improvements. Also very excited about the environment part and looking forward to how people use it, extend it, add more MCP servers, poke holes in it too. That's very cool as well. We love feedback. But super excited about this, and I would say the ask to our users is that this is, in some sense, a live benchmark in the sense that the environment is there so they can use parts of the MCP servers there, create their own tasks, create their own ways to evaluate. It's not a static benchmark in that sense. So I ask all our colleagues in other companies, universities, to really download it, use it, let us know what they think of it.

**Brad:** Maybe we can end on one final question, which is—in one to two years from now, how do you think this plays a role in the broader agent ecosystem? Are we just going to see thousands or millions of MCP servers? Are there any big gaps or bottlenecks that are preventing more widespread adoption right now? Paint a picture of where the world is going from here.

**Chetan:** Eventually, going back to the beginning of how we started this—a model needs to be really good at ingesting information and manipulating the environment outside of it for it to do any meaningful work. And eventually, if we extend it and if MCP is the standard by which all communication happens between each of these parties, it plays a central role. It becomes a critical part of that infrastructure. Now the part that I'm excited about most is how this then plays with computer use, because MCP is just the standardization of tool use, which is programmatic ways of calling APIs, but then there's also other ways where we can manipulate information using computers, browser use, et cetera. MCP combined with other mechanisms—the mechanisms that we have for direct computer use—I'm very excited for that to come together, and that might be—eventually we can look into creating benchmarks there as well.

**Chaitanya:** For me, I think this is the first step towards using static tools. You can think of MCP servers as deterministic type of tools, but then what if the other entity that you are interacting with is also another agent? This is a natural step towards agent-to-agent communication systems. Is an LLM or an LLM-based agent able to leverage the right agent, not just an MCP tool but the right agent? I think that's where things are going. And then once these agents start talking to each other, then it's an explosion—an intelligence explosion.

**Brad:** I think the saying used to be that software is going to eat everything, and I'm pretty bullish that agents are going to steal software's lunch and they're going to be eating everything. And really the way they're going to do that is through MCP. I think in a year, two years' time, basically our entire digital infrastructure is going to have integration entry points for agents, and that's going to be driven by MCP.

**Sami:** How would agents talk to each other? Are you going to wrap an agent into an MCP server?

**Chaitanya:** Yeah, and there are already versions of MCP for that.

**Chetan:** There are protocols like A2A.[^1]

**Sami:** Okay, that's very interesting.

**Brad:** One last thing. What's next on MCP benchmarks?

**Chetan:** I have the same answer. I'm really excited to combine MCP—we have this benchmark. If it needs to be more difficult, we'll continue progressing there. But what I want to do is combine it with other modalities, and that's computer use. If we can create a benchmark which tests both tool use and then computer use—I have a problem with my VPN right now. If it could uninstall my VPN using computer use, then pull the docs via MCP server, do all of that—that would be capabilities that I would love to test.

**Chaitanya:** For me it's the multi-turn continual learning aspect. Can we actually check for LLMs if they are able to do multi-turn, remember the interactions they're having, and then keep improving on that? I think this, and then the agent-to-agent—I think these are the two aspects that I'm really excited by.

**Brad:** Cool. Well thanks guys. I think that wraps up this episode of Chain of Thought. Thanks a lot.

**Chetan:** Thank you.

**Sami:** For viewers, if you have any questions please feel free to drop them in the comments and we'll get to them next time. Thanks.

---

*Note: All preview content, advertising, and promotional material has been removed from this transcript. The conversation is presented in its natural flow with systematic removal of filler words while preserving each speaker's distinctive voice and the collaborative panel dynamics.*

[^1]: **Protocol reference**: A2A likely refers to "Agent-to-Agent" communication protocols that extend MCP's capabilities to enable direct agent-to-agent interaction, though this is an emerging area of standardization.