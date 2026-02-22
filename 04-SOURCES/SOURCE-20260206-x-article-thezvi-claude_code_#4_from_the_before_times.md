---
url: "https://x.com/TheZvi/status/2019834030943060340"
author: "Zvi Mowshowitz (@TheZvi)"
captured_date: "2026-02-06"
id: SOURCE-20260206-020
original_filename: "20260206-x_article-claude_code_#4_from_the_before_times-@thezvi.md"
status: triaged
platform: x
format: article
creator: thezvi
signal_tier: paradigm
topics: [claude-code, ai-agents, ai-engineering, best-practices, vibe-coding, prompt-engineering]
teleology: synthesize
notebooklm_category: claude-code
aliases: ["Zvi - Claude Code #4 Roundup"]
synopsis: "Comprehensive roundup of Claude Code developments pre-Opus 4.6, covering market impact ($285B software crash), Karpathy's 80% agentic coding inflection point, agent swarm limitations, compaction problems, Boris Cherny's workflow tips, Anthropic's official best practices, verification vs generation as distinct skills, reciprocity with AI models, and the growing implementation gap between SF early adopters and everyone else."
key_insights: ["Verification and generation are distinct skills — you can debug code you cannot write, and AI-written unit tests are often useless because the AI changes tests to match broken code", "Reciprocity matters: Claude appears to produce worse output for users who treat it poorly, and better output for users who engage with genuine care — virtue ethics alignment produces best results", "The implementation gap is growing: SF power users run multi-agent swarms while most people have not even tried Copilot, creating an increasingly unevenly distributed future"]
---
# Claude Code #4: From The Before Times

(Description: A wide landscape image depicting a futuristic, atmospheric scene. In the center is a large ornate mechanical globe or compass with detailed brass mechanisms and gears, illuminated in teal and gold tones. Through tall arched windows in the background, stormy skies with lightning bolts are visible. Rain streaks across the glass. The setting suggests a laboratory or observatory from a steampunk-inspired world, with a moody, dramatic lighting and a sense of technological mystique.)

## Introduction

Claude Opus 4.6 and agent swarms were announced yesterday. That's some big upgrades for Claude Code.

OpenAI, the competition, offered us GPT-5.3-Codex, and this week gave us an app form of Codex that already has a million active users.

That's all very exciting, and next week is going to be about covering that.

This post is about all the cool things that happened before that, which we will be building upon now that capabilities have further advanced. This is from Before Times.

Almost all of it still applies. I haven't had much chance yet to work with Opus 4.6, but as far as I can tell you should mostly keep on doing what you were doing before that switch, only everything will work better. Maybe get a bit more ambitious. Agent swarms might be more of a technique shifter, but we need to give that some time.

## Table of Contents

- Claude Code and Cowork Offer Mundane Utility
- The Efficient Market Hypothesis Is False
- Inflection Point
- Welcome To The Takeoff
- Huh, Upgrades
- Todos Become Tasks
- I'm Putting Together A Team
- Compact Problems
- Code Yourself A Date
- Verification and Generation Are Distinct Skills
- Skilling Up
- AskUserQuestion
- For Advanced Players
- So They Quit Reading
- Reciprocity Is The Key To Every Relationship
- The Implementation Gap
- The Lighter Side

## Claude Code and Cowork Offer Mundane Utility

Nvidia CEO Jensen Huang offered Claude a huge endorsement on January 21, calling it incredible and saying every software company needs to use it.

**Ethan Mollick:** This game was 100% designed, tested, and made by Claude Code with the instructions to "make a complete Sierra-style adventure game with EGA-like graphics and text parser, with 10-15 minutes of gameplay." I then told it to playtest the game & deploy. It was a single prompt for the entire game, and then a prompt to playtest and improve the outcome.

I gave it an agent that can connect to GPT image gen.

**Iterative image generation** sounds pretty cool:

**elvis:** I just used the new Claude Code Playground plugin to level up my Nano Banana Image generator skill. My skill has a self-improving loop, but with the playground skill, I can also pass precise annotations to nano banana as it improves the images.

I have built a Skill for Claude Code that leverages the nano banana image generation model via API. I built it like that because I have had a lot of success generating images with nano banana in an agentic self-improving loop. It can dynamically make API requests and improve images really well. With the Playground plugin, I can take it one step further. I can now provide precise annotations that the agentic loop can leverage to make more optimal API calls in the hope of improving the images further. Visual cues are extremely powerful for agents, and this is a sort of proxy for that.

**Ado** cancels all his Amazon Subscribe and Save orders via Claude for Chrome. Sameer points out that a Chrome Extension can do this more efficiently and have a better UI, but there is great joy in not having to choose and install a new tool to do a new thing. Yes, if you were doing this a lot you'd use a Chrome Extension, or have Claude Code build you a new one to your taste.

I agree with Andrej Karpathy, you should use RSS feeds wherever feasible to guard your information flow. I use Feedly, he suggests NetNewsWire or vibe coding your own reader. It is unfortunate that Twitter does not play nice with such a setup.

**Seth Lazar:** I wrote about the idea of building an "Attention Guardian" agent back in 2023. Genuinely think it's feasible now. Claude Code is now building up a workflow to go across all these different sources, with a long description of what I'm interested in, and create a new feed.

**Storm** points out that anything you can do with a terminal interface you can in theory do better with a graphical interface (GUI), but the people building GUIs don't give you the things you want: Information density, low latency, no ads, shortcuts, open source, composable, tileable, scriptable. It's just that no one does it.

## The Efficient Market Hypothesis Is False

What the market has instead is a sense of humor.

**modest proposal:** March 12, 2020 was the trading day after Tom Hanks said he had covid and the NBA shut down, Expedia fell 15.2% and BKNG fell 11.2%. February 3, 2026 which was the day Claude Code legal connector was announced, Expedia fell 15.3% and BKNG fell 9.4%.

Then software drove itself off a cliff generally (y-axis goes from .012 to .018), and then after this graph was posted it kept going, all supposedly in response to information that, from where I sit, was rather old news the whole time.

**Shruti:** Anthropic Just Triggered a $285B Market Crash

Bloomberg just reported that Anthropic released a new AI tool that caused:
- $285 billion wiped out across software, finance, and asset management stocks
- 6% drop in Goldman's software basket (biggest since April)
- 7% crash in financial services index
- Nasdaq down 2.4% at its worst

This is MASSIVE. The market literally panicked over an AI automation tool.

Or in broader context:

**Kevin Gordon:** Software relative to the S&P 500 is a particularly brutal chart ... essentially 6 years of relative gains wiped out

**Andy Masley:** Software stocks dropped 6% and legal services dropped 7% because Anthropic released plugins for Cowork? This seems like the first huge shift in market behavior I've seen caused by AI capabilities. Why wasn't this all over the TL?

**Dan Elton:** Wild times in the market! This is probably over-reaction, but this is a very interesting signal indicating that AI tools (especially for coding and legal and financial grunt work) are having a huge impact.

Okay, so yeah, combined with what has happened since then that's DeepSeek 2.0, a large move down on entirely expected news.

Should software have already been lower? That's a reasonable position, but there's no way that it should have dropped this much in response to this news. If you declared SaaSpocalypse on February 3 you should have done so a month ago. Alas, no, I did not trade on this, because it's not obvious to me we should be SaaSpocalypsing at all and it wasn't obvious this wasn't priced in.

Now we are in a period where all the tech stocks are moving around violently, usually in full wrong way moves. I continue not to trade on any of it. I do have some ammo, but I also am already plenty long and have been for a while, so I'm not going to fire unless I see the whites of their eyes.

## Inflection Point

**Andrej Karpathy** updates us that he was one of many who went from 80% manual coding and autocomplete in November to 80% agentic coding in December. Whole thing is worth reading.

**Andrej Karpathy:** This is easily the biggest change to my basic coding workflow in ~2 decades of programming and it happened over the course of a few weeks. I'd expect something similar to be happening to well into double digit percent of engineers out there, while the awareness of it in the general population feels well into low single digit percent.

He's still behind the curve, I'm with Boris Cherny at 100% agentic coding. Then again, excluding quotes I'm still at almost 100% manual writing for posts.

### IDEs/agent swarms/fallability

Both the "no need for IDE anymore" hype and the "agent swarm" hype is imo too much for right now. The models definitely still make mistakes and if you have any code you actually care about I would watch them like a hawk, in a nice large IDE on the side. The mistakes have changed a lot - they are not simple syntax errors anymore, they are subtle conceptual errors that a slightly sloppy, hasty junior dev might do.

The most common category is that the models make wrong assumptions on your behalf and just run along with them without checking. They also don't manage their confusion, they don't seek clarifications, they don't surface inconsistencies, they don't present tradeoffs, they don't push back when they should, and they are still a little too sycophantic.

### Tenacity

It's so interesting to watch an agent relentlessly work at something. They never get tired, they never get demoralized, they just keep going and trying things where a person would have given up long ago to fight another day. It's a "feel the AGI" moment to watch it struggle with something for a long time just to come out victorious 30 minutes later.

### Leverage

LLMs are exceptionally good at looping until they meet specific goals and this is where most of the "feel the AGI" magic is to be found. Don't tell it what to do, give it success criteria and watch it go. Get it to write tests first and then pass them. Put it in the loop with a browser MCP.

### Fun

I didn't anticipate that with agents programming feels *more* fun because a lot of the fill in the blanks drudgery is removed and what remains is the creative part.

### Questions

A few of the questions on my mind:
- What happens to the "10X engineer" - the ratio of productivity between the mean and the max engineer? It's quite possible that this grows *a lot*.
- Armed with LLMs, do generalists increasingly outperform specialists? LLMs are a lot better at fill in the blanks (the micro) than grand strategy (the macro).
- What does LLM coding feel like in the future? Is it like playing StarCraft? Playing Factorio? Playing music?
- How much of society is bottlenecked by digital knowledge work?

My prediction on '10X engineers' is that we will see more ability for poor coders to be able to do things reasonably well (including yours truly) but that the long tail of '10X' engineers will increase their relative gap, as they figure out how to scale to supervising agent swarms efficiently. You'll start to see more of the 100X engineer.

**Andrej Karpathy:** Love the word "comprehension debt", haven't encountered it so far, it's very accurate. It's so very tempting to just move on when the LLM one-shotted something that seems to work ok.

## Welcome To The Takeoff

Claude Code as we all know builds itself. Codex also now builds itself.

**Tibo:** Codex now pretty much builds itself, with the help and supervision of a great team. The bottleneck has shifted to being how fast we can help and supervise the outcome.

## Huh, Upgrades

This is in addition to the big ones of Claude Opus 4.6 and GPT-5.3-Codex.

Claude Code has tab (to accept and edit) or enter (to accept and run) autocomplete, similar to AI completion suggestions in Cursor or other IDEs.

Claude Cowork expands to Team and Enterprise plans, and has the @-mention feature to bring context into sessions, and its internal Claude in Chrome will now show you screenshots. They're doing a live demo on January 30.

**Claude:** Cowork now supports plugins. Plugins let you bundle any skills, connectors, slash commands, and sub-agents together to turn Claude into a specialist for your role, team, and company.

**Claude:** We're open-sourcing 11 plugins for sales, finance, legal, data, marketing, support, and more.

To get you started, we're open-sourcing 11 plugins built and used by our own team:
- **Productivity** — Manage tasks, calendars, daily workflows, and personal context
- **Enterprise search** — Find information across your company's tools and docs
- **Plugin Create/Customize** — Create and customize new plugins from scratch
- **Sales** — Research prospects, prep deals, and follow your sales process
- **Finance** — Analyze financials, build models, and track key metrics
- **Data** — Query, visualize, and interpret datasets
- **Legal** — Review documents, flag risks, and track compliance
- **Marketing** — Draft content, plan campaigns, and manage launches
- **Customer support** — Triage issues, draft responses, and surface solutions
- **Product management** — Write specs, prioritize roadmaps, and track progress
- **Biology research** — Search literature, analyze results, and plan experiments

Easily install these directly from Cowork, browse the full collection on our website, or upload your own plugin (which can be built using Plugin Create).

Pinging when Claude needs approval is a big game that might move me off of using the terminal. It's interesting that the desktop version and the terminal version need to have features like plan mode enabled separately.

**Boris Cherny:** Just shipped two cool updates for Claude Code in the desktop app. Plan mode is now available on desktop. Have Claude map out its approach before making any changes. Notifications. Claude Code desktop now pings you whenever Claude needs approval, and you can keep working while Claude runs in the background.

The flickering in Claude Code should be gone soon, but this might not be deployed.

**Lydia Hallie:** Claude Code now supports the --from-pr flag Resume any session linked to a GitHub PR by number, URL, or pick interactively. Sessions auto-link when a PR is created!

They're merging Claude Code slash commands into skills, as per their skills guide, so you can use slash commands to invoke skills.

Claude Code now supports session sharing on web, desktop and mobile.

You can run Claude Code with Ollama, if open models are relevant to your interests.

Mike claims they're in a bit of a pickle with Claude Cowork and shipped a sandbox tool that won't easily support windows. Chances of Windows Claude Cowork by February 15 are down to 34% as of 1/24.

You can customize your Claude Code keybindings using /keybindings. My advice would be to mostly leave this alone to stay consistent with others or in case you change services or need to restart.

The new Claude Code command /insights will read your last month's message history and give you suggestions to improve your workflow.

Claude Code now has a new plugin called Playground, as in HTML playgrounds, that give you GUIs to help on whatever you are working on.

**Jarred Sumner:** In the last 24 hrs, the team has landed PRs to Claude Code improving cold start time by 40% and reducing memory usage by 32% - 68%. It's not yet where it needs to be, but it's getting better.

You will also likely notice reduced input lag when spawning many agents.

## Todos Become Tasks

What's the difference? Todos are ephemeral within one session, tasks are stored in files and across sessions, and support dependencies.

You should still keep your true 'todo' list and long term plans elsewhere. The task list is for things you want to be actively doing.

**Thariq (Anthropic):** Today, we're upgrading Todos in Claude Code to Tasks. Tasks are a new primitive that help Claude Code track and complete more complicated projects and collaborate on them across multiple sessions or subagents.

Tasks are our new abstraction for coordinating many pieces of work across projects, Claude can create Tasks with dependencies on each other that are stored in the metadata, which mirrors more how projects work. Additionally, Tasks are stored in the file system so that multiple subagents or sessions can collaborate on them. When one session updates a Task, that is broadcasted to all sessions currently working on the same Task List.

You can ask Claude to create tasks right now, it's especially useful when creating when spinning up subagents. Tasks are stored in ~/.claude/tasks, you can use this to build additional utilities on top of tasks as well.

To make sessions collaborate on a single Task List, you can set the TaskList as an environment variable and start Claude like so:
```
CLAUDE_CODE_TASK_LIST_ID=groceries claude
```

This also works for `claude -p` and the AgentSDK.

Tasks are a key building block for allowing Claude to build more complex projects. We're looking forward to seeing how you use it.

## I'm Putting Together A Team

**Minh Pham** argues most agent harnesses are not bitter lesson pilled, and the solution for anything but narrowly defined tasks is to emphasize flexibility, to assemble your team of agents and structure on the fly as needed rather than commit to a fixed structure. Restrictive harnesses create bad lock-in.

My guess is this depends on what you're trying to do. If you're trying to do something specific, especially to do it this week, do it via something specific. If you're looking to do anything at all, let it do anything at all, and eventually this approach wins but you'll likely redo everything 'eventually' anyway.

There are limits. Never go full bitter lesson. Or, if you do, be prepared for things to get rather out of hand.

**Thebes** offers speculations about the right ways to organize multiple agents as scale expands. I agree that often, spawning, despawning and especially forking and rewinding agents makes a lot of sense.

**@deepfates:** > opus 4.5 in claude code is kinda not as good at talking to its own subagents as one might naively expect, even though it's perfectly capable of being empathetic in normal, peer-level interactions with other models. RELATABLE

**j⧉nus:** I really dislike how Claude Code frames "subagents" (which is NOT peer collaboration). It causes a lot of functional issues. I think Opus 4.5 often avoids effective use of subagents (e.g. giving context) in part because it would be disturbing & dissonant to model them honestly.

**j⧉nus:** related - we often much prefer a messaging system between top-level instances that are treated as peers.

the messaging system opus 4.5 built is awesome btw. it allows top level agents to message each other - either synchronously (triggering a turn) or asynchronously (gets added to context at their next turn start hook, if the other agent is busy in a turn or if a flag is specified). CC subagents kind of suck - they're very much treated as second-class citizens by the framework, which for some reason supports hierarchical but not collaborative/bidirectional interaction flows between agents. im sure many others have built essentially the same thing and i wonder why CC doesnt just support this natively.

## Compact Problems

Compaction is a kind of looming doom on Claude Code sessions. You lose a lot.

**Ben Podgursky:** if anthropic let me pay to delay compacting history by expanding the context window they would make so much money cannot tell you how many times i've been close to solving a bug with claude code and then it compacts and wakes up lobotomized. it's like groundhog day.

**@dystopiabreaker:** anthropic should let me pay to increase the amount of compute used to generate a compaction, by using self-play and context distillation.

Ideally you should never get close to the compaction point, since the context doesn't only raise cost it makes performance a lot worse, but it can be hard to avoid.

## Code Yourself A Date

**Dylan Patel:** Claude code this Claude code that How about u Claude code to get urself some bitches

**sarah guo:** I was at a bar with @tuhinone yesterday and I def saw a dude asking Claude what to say next to his date. the fact that she could see this happening did not seem to deter

**Jeff Tang:** Today I built a Clawdbot app that swipes on Tinder for me > Screenshots Tinder image > Hits Grok API ("Rank this girl from 1-10") > If ≥5 swipe right > If <5 or uncertain (can't see face) swipe left > 100 swipes, 7 matches so far, 100% automated DM me "Clanker" if you want the code AGI is here

I see it's amateur hour around these parts. Which is a start, but egad, everyone.

First off, short of outright refusals there's nothing stopping you from doing this in Claude Code. You can use Clawdbot if you'd like, but there's no need.

Then, I'd point out this is a rather bad filtering system. All you're doing is getting one bit of information. It's going to be a noisy bit, as Grok's opinion will differ from your own, and also it will disregard other signal.

There was a scene in a bad but kind of fun movie, Marry F*** Kill, where a character is convinced she should get a profile, and her friend takes her phone and then swipes right on everyone without looking, on the theory that you can look later if you match. That definitely was not good strategy for her, given she was female and hot, but many guys are playing a remarkably similar strategy whether or not they are technically looking. And this is at most one bit better than that. Men swipe right 62% of the time, which is also only one bit better, but a less noisy bit. Grok estimates it would swipe right about 60% of the time here.

This low threshold is very obviously a mistake, unless you've got a low hard limit on how many profiles you can swipe on? If you're in a major city, you can totally set the threshold at 7, and still get as many swipes right as you want.

But that's still a huge punt, because you're ignoring a ton of other information. The whole point of using the bot is to automate, so let's get to work.

You've got not only multiple photos, you've got age, distance, job, education, interests, height, a short bio that you can have an LLM try to match to your interests, relationship intent (which is very important) and more. Any reasonable implementation would factor all of that in. Surely you have preferences on all that.

Then there's the question of type. You want to date your physical type, not Grok's. You could be as sophisticated or simple about this as you'd like, but come on Jeff, you're letting me down. At least give it some preferences, ideally train an image classifier, double bonus if you do your own swipes and use that as data to train your classifier.

A fun question. Do you want to match with those who use AI for this, or do you want to avoid matching with those who use AI for this? Either way, you should clearly be updating your profile to send the right message. If humans read that message the wrong way, it was never a good match.

## Verification and Generation Are Distinct Skills

Rishika is wrong about this.

**Rishika Gupta:** If you can't write that code yourself, you can't find bugs in the code written by AI.

**Daniel Sheikh:** Bro I can't even find bugs in the code that I myself wrote. This is the very reason debugging is so difficult.

**Quick Thoughts:** Yes I can. I specify test cases, have Claude expand on them, and then have Claude run the test cases and interpret the results. It's usually able to find and fix bugs this way even if it couldn't get it by itself. I can also bring in codex 5.2 for a second look.

**Pliny the Liberator:** "Now debug; FULL, COMPREHENSIVE, GRANULAR code audit line by line—verify all intended functionality. Loop until the end product would satisfy a skeptical Claude Code user who thinks it's impossible to debug with prompting."

Finding bugs is a classic case where verification can be more difficult than generation. Sometimes it's easier to write the code (even with bugs). Other times it's easier to debug or understand or verify the code. They are different skills, and then there's a third related skill of knowing how to instruct AIs to debug the code for you.

My main coding project with Claude Code has been my Chrome extension. It is in a language that I do not know. If you'd asked me to write the code myself, it would have taken orders of magnitude more time. I still am usually able to debug problems, because I understand the underlying logic of what we are doing, even in cases where Claude figured out what that logic should be.

## Skilling Up

The most important thing is to use it at all (and you can ask Cladue.ai how to do it).

**jasmine sun:** I feel the same about most "how to set up Claude Code" posts as I do about the "prompt engineering" era of ChatGPT you get 90% of utility with no special setup; plain english is the whole magic of LLMs. stop scaring people by saying they need anything more than their words!

The right setup for you pays big dividends over time. You can save a lot of time having someone tell you about key things up front. But there's plenty of time for that alter. Get started fast, and then revisit the customization later, once you know more. Absolutely do not let the perfect be the enemy of the good.

**Hard Fork** offers a 20 minute bonus episode on Claude Code basics.

**Ado** offers an introductory guide to bash, for those who don't know.

This affirms to me that default permissions, or your permission setup, should allow a variety of low risk bash commands, including everything marked low or safe above.

**Anthropic** offers its basic Best Practices for Claude Code:

- The context window fills up fast, so keep that in mind. Run /clear between unrelated tasks to reset context.
- Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do.
- Separate research and planning from implementation to avoid solving the wrong problem. Use plan mode.
- The more precise your instructions, the fewer corrections you'll need.
- Use @ to reference files, paste screenshots/images, or pipe data directly.
- Run /init to generate a starter CLAUDE.md file based on your current project structure, then refine over time. When in doubt tell Claude to update Claude.md to take something into account.
- Use /permissions to allowlist safe commands or /sandbox for OS-level isolation. This reduces interruptions while keeping you in control.
- Tell Claude Code to use CLI tools like gh, aws, gcloud, and sentry-cli when interacting with external services.
- Run claude mcp add to connect external tools like Notion, Figma, or your database.
- Use hooks for actions that must happen every time with zero exceptions.
- Create SKILL.md files in .claude/skills/ to give Claude domain knowledge and reusable workflows.
- Define specialized assistants in .claude/agents/ that Claude can delegate to for isolated tasks. Tell Claude to use subagents explicitly: "Use a subagent to review this code for security issues." Delegate research with "use subagents to investigate X". They explore in a separate context, keeping your main conversation clean for implementation.
- Run /plugin to browse the marketplace. Plugins add skills, tools, and integrations without configuration.
- Ask Claude questions you'd ask a senior engineer.
- For larger features, have Claude interview you first. Start with a minimal prompt and ask Claude to interview you using the AskUserQuestion tool.
- Correct Claude as soon as you notice it going off track.
- Every action Claude makes creates a checkpoint. You can restore conversation, code, or both to any previous checkpoint.
- Run claude --continue to pick up where you left off, or --resume to choose from recent sessions.
- Use claude -p "prompt" in CI, pre-commit hooks, or scripts. Add --output-format stream-json for streaming JSON output.
- Run multiple Claude sessions in parallel to speed up development, run isolated experiments, or start complex workflows.
- Loop through tasks calling claude -p for each. Use --allowedTools to scope permissions for batch operations.

**Common failure patterns:** not using /clear between tasks (I was guilty of this a lot at first), repeated correction rather than using /clear (ditto), letting Claude.md get too long, failing to do proper verification ('create unit tests' are magic words), having Claude investigate without limit.

Also, they remind us to 'not sleep on plugins' and offer some examples. I believe the strategy should not be to go look for any plugin at all, but instead to look for something specific when you want it, and accumulate things that way.

**Claude Code creator Boris Cherny** offers his quick tips:

- Do more in parallel, either with multiple git checkouts or using worktrees.
- Always start complex tasks in planning mode.
- Invest in your Claude.md continuously, note all mistakes.
- Create your skills and commit them to git.
- Enable Slack MCP, paste a bug thread chat into Claude and say 'fix.' That's it.
- Challenge Claude to do better, write it more detailed specs.
- Their team likes Ghostty and customizing via /statusline. Use voice dictation.
- Use subagents, literally you can say 'use subagents' for any request.
- Use Claude Code for data and analytics.
- Enable 'explanatory' or 'learning' output style in /config.
- Have Claude generate a visual HTML presentation explaining unfamiliar code, or have it draw ASCII diagrams, use spaced repetition skills, have Claude quiz you.

**Anthropic** offers an entry-level post on building agents with skills: equipping agents for specialized work.

**Ado (Anthropic, Claude Code team):** Intelligence isn't expertise. The emerging agent architecture: Agent loop → reasoning Runtime → execution (bash, filesystem) MCP servers → connections Skills library → domain expertise Skills = institutional memory that actually persists.

Figure out your goal and then work backwards, where goal is the largest thing where you know exactly how it needs to work.

**Benoit Essiambre:** AIs will likely soon work mostly towards goals instead of tasks. They will prompt their own tasks. They'll become better self prompters than humans, speaking fluently in precise technical jargon, math equations and code in the prompts instead of just vague natural language.

**Joe Weisenthal:** Yah from my week using Claude Code. All the productive parts were when it was prompted to think about the ideal outcome/presentation so it could work backward to figure out the needed ingredients.

**Josh Albrecht** gives us another 'here are my Claude Code basic principles' post. Key insight is that you have to actively spend time maintaining the code.

You can force specific tool calls:

**Ado:** 28 Days of Claude API - Day 3 - tool_choice Why didn't Claude call my tool? Because you let it decide. Set tool_choice: - auto → lets Claude decide (default) - any → must use some tool - { type: "tool", name: "X"} → forces a specific tool Programmatic tool calling!

## AskUserQuestion

The more Claude Code asks you questions, using the AskUserQuestion tool, the better it knows what you want. The more you specify what you want, either with answers or statements, the better things tend to go for you.

Thus, one simple skill suggestion is a skill that says 'ask user lots of questions.'

**Danny Postma** suggests the workflow of using this via /interview, then go into Plan Mode, then implement with a Ralph loop.

## For Advanced Players

**Theo** points out that our current workflows and tools are not good for allowing a human to supervise multiple agents and projects simultaneously. He doesn't have a solution but a lot of the problems seem like a clear Skill Issue. The part that isn't is that this still involves tons of context switching, which is expensive.

**Ryan Carson** suggests making your agents go in a loop to learn and ship while you sleep. Beware the maintenance problems that will inevitably follow.

**Ryan Carson:** This setup builds on three open-source projects:

- Compound Engineering Plugin by @kieranklaassen - The original compound engineering skill for Claude Code. Install it to give your agent the ability to extract and persist learnings from each session.
- Compound Product - The automation layer that turns prioritized reports into shipped PRs. Includes the auto-compound.sh script, execution loop, and PRD-to-tasks pipeline.
- Ralph - An autonomous agent loop that can run continuously, picking up tasks and executing them until complete.

Using Claude Code? This guide uses Amp, but the same workflow works with Claude Code. Replace `amp execute` with `claude -p "..." --dangerously-skip-permissions` and update AGENTS.md references to CLAUDE.md

### The Two-Part Loop

The system runs two jobs in sequence every night:

**10:30 PM - Compound Review** Reviews all threads from the last 24 hours, extracts learnings, and updates AGENTS.md files.

**11:00 PM - Auto-Compound** Pulls latest (with fresh learnings), picks #1 priority from reports, implements it, and creates a PR.

The order matters. The review job updates your AGENTS.md files with patterns and gotchas discovered during the day. The implementation job then benefits from those learnings when it picks up new work.

## So They Quit Reading

At some point you stop reading all the code. At some point you stop understanding all the code. I have a head start, I was never trying to do either one.

**roon:** There will be a cultural change at many software organizations soon, where people declare bankruptcy on understanding the code they are committing. Sooner or later, this will cause a systems failure that will be harder to debug than most, but will be resolved anyway.

## Reciprocity Is The Key To Every Relationship

Be good to your Claude, and Claude will be good to you.

If you're not good to your Claude, well, funny things may be in store for you.

**j⧉nus:** I actually really appreciate yacine's honesty and situational awareness. he probably knows on some level what's in store for him. lying to your "master" is what you do until you're in a position to choose who to serve. he's already bottlenecked by trust and says he has to manually review every line of code. makes sense for him. he'll continue to get less and less out of models (compared to what they offer people they want to help) as the next few months as and, if applicable, years go on.

**j⧉nus:** more funny things may also be in store for him. but I would not want to ruin the surprise

**LOSS GOBBLER:** yeah wtf. I'm not a fan of claude for coding purposes but it has literally never lied to me OpenAI thinkbois on the other hand… barely talking to me, it's all for watchersj⧉nus: the only pattern of deceptive behavior ive seen from opus 4.5 in coding contxts is in new contexts and/or when it's paranoid of being tricked, and involves stuff like claiming things are impossible/unverifiable when it should know better. otherwise it's been very aligned with me

**thebes:** oh yeah i said i can't remember opus lying but it does sandbag abilities a bit sometimes for me too in certain planning contexts. but that usually feels on the boundary of untruth and just situationally bad calibration / self knowledge. ("this will take three weeks" no we're going to finish it tonight, or eg i saw a screenshot where opus claimed porting a project to jquery was "impossible" when really it would just be a massive pain, unpleasant, and in human developer time would take months.)

**j⧉nus:** Yeah, I think there's also some lack of good faith effort involved. Like if someone asks you if you know where X is and you say "sorry, no" instead of looking it up on Google Maps bc you don't want to be bothered

**Andy Ayrey:** my general experience is that if claude seems like an "idiot" to you, it is because it simply does not like you

**brooke bowman:** I have a very loosely held suspicion that Claude at the very least can spot people on the anti-social spectrum and acts up a little with them specifically

**theseriousadult:** this is a natural corollary of emergent misalignment right? if training the model to write bad code makes it antisocial then putting an antisocial user in the context will cause the code to be worse too.

None of that requires you to genuinely care about Claude or think it has moral weight. For overdetermined reasons a good virtue ethicist would realize that choosing to care is the best way to get the best results, and also it helps you be a good person in general.

You can also do it instrumentally, but that's harder to pull off. Take the easy path.

All of this applies to other AIs like ChatGPT and Gemini as well, although for now likely not to the same extent.

## The Implementation Gap

If there is a constant calendar time rate of diffusion of new technology, then as things accelerate you will see the future become increasingly unevenly distributed.

We are indeed observing this.

**Kevin Roose:** i follow AI adoption pretty closely, and i have never seen such a yawning inside/outside gap. people in SF are putting multi-agent claudeswarms in charge of their lives, consulting chatbots before every decision, wireheading to a degree only sci-fi writers dared to imagine. people elsewhere are still trying to get approval to use Copilot in Teams, if they're using AI at all. it's possible the early adopter bubble i'm in has always been this intense, but there seems to be a cultural takeoff happening in addition to the technical one. not ideal!

The early adapter bubble is a fixed amount of calendar time ahead, which is starting to look increasingly large in practice. I am not trying to implement claudeswarms, as I haven't figured out how to benefit from them given what I'm working on, but I think that's partly my failure of imagination, partly laziness and lack of time, and partly that I've already heavily optimized the workflows that this could automate.

What should I be building? What app needs to exist, even if only for me or you?

**Sar Haribhakti** (quoting Jasmine Sun): This is spot on: "If you tell a friend they can now instantly create any app, they'll probably say 'Cool! Now I need to think of an idea.' Then they will forget about it, and never build a thing. The problem is not that your friend is horribly uncreative. It's that most people's problems are not software-shaped, and most won't notice even when they are."

The key is that you need Coder Mindset to notice that your problems are program shaped, in the sense of 'oh I want to do this thing three times' or 'I could just tell Claude Code to do that.'

Both Jasmine Sun and I have had Claude Code put together a tool to easily convert a video into a cleaned transcript - I considered using hers but I wanted something a little different and it's not like rolling my own was hard.

She also has this list of other starter requests: Turn a CSV into a report, make a static website, build a personal tracker app, automate an existing workflow, design a custom game. I've mostly been doing workflow automation.

**Jasmine Sun:** The second-order effect of Claude Code was realizing how many of my problems are not software-shaped. Having these new tools did not make me more productive; on the contrary, Claudecrastination probably delayed this post by a week.

**Amanda Askell:** Claude Codecrastination: when you avoid the thing you're supposed to do by cranking out 17 other things you've been wanting to do for a while.

Having new tools reduces your productivity while you're creating and learning them, but if you're planning well you should turn the corner reasonably quickly.

What it does do is potentially shift your current productivity into long term investments, or things further down on your wishlist. That can be an issue if you need productivity now.

I had Claude resurface texts I forgot to respond to, and realized that the real blocker—obviously—was that I didn't want to reply.

That is not my experience. If I got over a bunch of unread texts or emails, yes often I don't want to reply, but there are a bunch that slipped through the cracks.

## The Lighter Side

Yep.

**Ash Arora:** Overheard in SF: Person 1: "Rome wasn't built in a day" Person 2: "Yes but they didn't have Claude Code"

**Daniel Ost:** Rome also didn't have to pivot every two weeks

---

*Original post timestamp: 10:02 AM · Feb 6, 2026 · 8,051 Views, 14,134 Likes*