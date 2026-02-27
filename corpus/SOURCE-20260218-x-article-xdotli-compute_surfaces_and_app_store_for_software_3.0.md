# Compute Surfaces and App Store for Software 3.0
## Introduction
There are maybe 20 skills registries, marketplaces, or app stores out there right now. Everyone wants to be the single source of truth for distribution. But what actually builds the moat for a skills registry?
**tldr** - Skills are the apps in Software 3.0, and skills stores will be the new App Stores. Skills registries don't win without owning or connecting to a local desktop application that users use daily. Switching between desktop applications will be easy; potential moats can potentially be better multimodal memories and a tighter ecosystem.
## The App Store Lesson
The lesson from the App Store is instructive. Apple didn't win distribution by building a better catalog — they won by controlling the **end-user compute surface**. Once you own the surface for compute, you dominate the distribution of software. npm and PyPI are also examples: they're determined and made default by the runtime. Interestingly, when Deno launched, it was the existing npm ecosystem that preserved Node's dominance. Bun only gained traction because it accommodated npm. Back to Skills, even if you become the GitHub of skills, there's still a long road to App Store profitability.
(Description: Split-screen image showing the App Store logo on the left with text "Reach every iPhone user" and on the right, a green card with text "The story of why Marc Benioff gifted the AppStore.com domain to Steve Jobs" dated June 2, 2020. Steve Jobs is visible in the bottom left of the image. Caption: "One of the monumental moments of App Store")
## The Agent Landscape Analogy
The analogy maps cleanly onto the current agent landscape:
- **Apps** = Skills. The reusable bundles of instructions and scripts that agents execute.
- **Hardware** = The user-facing application that controls distribution. The desktop client, the terminal UI, the chat interface — whatever surface the user opens every day.
- **OS** = The agent harness. Claude Code, Codex CLI, OpenClaw's gateway — the runtime that actually executes skills and mediates between the user and the model.
(Description: Technical diagram showing the abstraction framework with nested circles labeled "Skills," "Agent Harness," and "Operating System" inside, with a bar chart on the right showing "Agent architecture stack and resolution rates across 7 agent-model configurations on 84 tasks." The chart displays multiple colored bars (red, blue, green) across different test categories. Caption: "The abstraction framework and findings we have from SkillsBench.ai")
What makes this moment strange is that one piece of "hardware" can run multiple "operating systems." I can open the Codex Desktop app and run Codex's agent harness, but I could also, in principle, route tasks through a different agent runtime on the same machine. This is unlike phones, where the hardware and OS are tightly coupled. It's more like the PC era, where the same box could run Windows or Linux — and that looseness made it harder for any single player to lock in users.
## How I Learned Local-First Won
I used to think the right form factor for agents was remote-first. Last August, we built Instaline, which is a product that let any agent live on iMessage, WhatsApp, SMS, and phone calls, starting with Claude Code. We made the agents run on Daytona persistent sandboxes. Before we even launched, two friends heard about what we were doing and reached out. One was building a startup and wanted to keep working from his phone while stepping away from his laptop. The other wanted root access to his laptops as well as all the VMs he owned, like a master agent that could orchestrate work on every device he owned.
(Description: Screenshot of iMessage interface showing a conversation with Claude Code AI. The screen displays a chat with messages in blue (user) and gray (Claude responses), with text discussing code review. The background shows a sunset mountain landscape. On the right side is a headshot of a smiling person wearing glasses. Below reads "send texts to any agents you want." Posted Sep 3, 2025, 61.5K Views. Caption: "Our first launch of Claude Code on iMessage")
Neither was quite the fit we'd designed for. Our model was PR-based: a remote session picks up a pull request and continues the work. We explored secrets vaults, persistent file systems as agent memory, fault tolerance for stuck agents. But we couldn't find enough users who wanted a remote-first product. After the first few weeks of launching, we pivoted and shelved the idea, the same idea that OpenClaw later was based on, made mainstream, and gained massive traction when it launched in this year.
**In hindsight, the market was telling us something. Local-first has won the race for most workflows.** Codex now ships a desktop app that's local-first and doesn't even require a git repo. I migrated from another very well-designed app @conductor_build because they require everything to be a git repo a few months ago. Claude Cowork targets white-collar knowledge work by executing directly on local files. Eigent does the same with multi-agent orchestration on your desktop. The remote-first bet was premature.
## The Hardware Race is On, and Switching Costs Are Low
Which brings me back to skills stores. What's interesting is that Codex Desktop launched with a Skills tab in the sidebar, and it's actively growing. What's also interesting is that if you look close, its upper left corner is almost identical to that of HappyCapy. The experience is genuinely good: vertical terminal bars where you can trigger up to eight parallel workflows without losing context. It's almost like the Arc Browser for terminal coding agents. Between that and Claude Code's lack of a comparable UI, I find myself reaching for Codex Desktop more often than Ghostty. Also from a lot of repeated experiments and local benchmarking (my focus and job is to make and run benchmarks), I can hardly distinguish the results of Codex and Claude Code with each's SOTA models.
(Description: Architectural diagram titled "LLM OS" showing a systems architecture layout. On the left are Software 1.0 tools including Calculator, Python Interpreter, Terminal, and File system with embeddings. In the center is the LLM with RAM and context window. On the right are peripherals including video, audio, CPU, Ethernet, Browser, and Other LLMs. Labeled "Initial diagram by @karpathy in his YC AI Startup School keynote")
But here's the problem for anyone trying to be the "hardware" layer: switching costs between desktop apps are extremely low. Codex Desktop or Claude Desktop, I can move between them in seconds. There's no vendor lock-in, no iCloud Photos and Families, no data on critical platform-only apps. This is fundamentally different from where switching from iPhone to Android.
So if switching costs are low, what builds the moat? I don't have the answer. I guess the frontier labs are elbowing each other to find out. Here're a few things that I find potentially relevant:
### Personal Memory
The agent that remembers my codebase conventions, my writing style, my communication preferences, my project history. Basically an agent that's harder to leave. This is the equivalent of iCloud Photos: not the reason you bought the phone, but a major reason you stay. However, users still need to be able to export their data. Memory that feels like a trap will get rejected; memory that feels like an asset will compound loyalty. For text modalities I feel it might be simpler going on, but as AI embeds more and more into lifes, it will consume exponentially more multimodal data as well. Effectively filtering, labeling, and retrieving those data in an agent and store them in a memory system remains unsolved.
### Proprietary Skills Built on Your Platform
Generic skills that run on any harness are commodities. But if a platform develops high-quality, deeply-integrated skills that take advantage of its specific runtime capabilities, like Codex's Figma or its automation scheduling, or someone made an astoundingly good Excel Skills, those become reasons to stay. The App Store's moat isn't just that it has apps; it's that developers build for iOS first because of the specific capabilities and economics of that ecosystem.
### Ecosystem Gravity
When your skills, your memory, your automations, and your connected services all live in one place, the switching cost isn't any single feature, it's the sum of all of them. This is how Apple actually locks you in: not with any one product, but with the interplay between iCloud, AirDrop, Handoff, iMessage, and the App Store. One scenario I see happening is Codex Desktop or Claude Code Cowork ships with a markdown editor, a macOS and Windows compatible launcher (Raycast), linear, a screenshot taker, a meeting notetaker, a light weight editor for editing code snippets (I use ChatGPT web editor after getting the markdown from Claude.ai because I can't edit markdowns on Claude.md), and 1Password etc. The Agent will get all our context automatically and on the fly.
## What's New
It seems to me we are in a very weird time where Apps (Skills) are popping out and are landing on and being indexed on all kinds of websites without a dominant hardware (desktop app) that knits them together. No one has locked in enough users through a combination of daily-driver UX, personal memory, and proprietary skills to own the distribution layer the way Apple owns mobile. I believe there's a huge opportunity here. It's unclear who will build it, whether it's big labs, big tech, or emerging startups. You might argue that big labs have all the resources and distribution, but on another note, it's been really early in the new paradigm shift, thus no one knows much more than others. And usually in times like this is a great equalizer and opportunity for startups.
Fun fact: This article is initially written on X post editor, polished by GPT-5.2 (on chatgpt.com), Opus 4.6 (on claude.ai), Gemini 3 Flash (gemini.google.com), moderately edited in ChatGPT's web editor (I copy pasted the output from claude.ai to the editor on ChatGPT.com), and finalized on Notion.so's code block.
## References
- @HanchungLee, The Model is the Product, https://aicouncil.com/talks25/the-model-is-the-product
- @karpathy, Software Is Changing (Again), https://www.youtube.com/watch?v=LCEmiRjPEtQ
- SkillsBench team, SkillsBench: Benchmarking How Well Skills Work Across Diverse Tasks, https://arxiv.org/abs/2602.12670
## Appendix
(please comment for any interesting products and companies that I didn't include here)
### List of Compute Surface Products / Companies
- Codex Desktop
- Claude Cowork
- @conductor_build
- @Eigent_AI by @guohao_li
- @emdashsh
- sculptor by @imbue_ai
### List of Agent Harnesses Products / Companies
- @openclaw
- @FactoryAI
- Claude Code
- Codex
- Gemini CLi
- @opencode and oh-my-opencode
- pi.dev
### List of Skills Registries
- skillsmp.com
- skills.sh
- sundialhub.com
- https://skillsdirectory.com/
- orthogonal.com
- https://skills.re/