# I spent $10,000 to automate my research at OpenAI with Codex

I use **billions** of codex tokens. Here is my setup and is what I learned.

Many people drastically underestimate what codex can do. Even some of my colleagues still underutilize codex, but they are eager to experiment once you show them some ambitious use-cases. Thus, I wanted to write something down and share it more broadly, in the hopes it inspires more people.

In this post, I'll share my simple setup and discuss some killer use-cases, where I routinely allocate hundreds of millions of tokens. In total, I spent $10,000 on API costs this month, which makes me one of the most prolific users in my team. Totally worth it.

Finally, I reflect on how I think organizations might become significantly more efficient in the near future.

## Continual Note Taking

My personal setup is incredibly simple: git worktrees, many shell windows, and one VSCode instance per worktree so I can browse code changes. You basically get this setup out of the box in the new codex app. Don't get baited by overly fancy tooling.

The big unlock was getting codex to continually document and improve its own workflows. This is something I fully hacked together for my personal setup. Codex consistently gets better and faster at tasks I use it for, just because I have the habit of asking it to take notes and improve. While working, codex commits notes and helpers to my personal folder in our monorepo. After a few interactions with a new part of the codebase, these helpers tend to stabilize. I've never actually read these notes, their utility to me is purely the effect on codex's performance.

With my setup now able to compound knowledge across sessions, I got comfortable scaling up the tasks I used it for. Let's dive into two tasks I recently spent hundreds of millions of tokens on.

## Scaling Research

Research moves fast. Experiments are expensive and easy to misconfigure, so staying on top of the most recent findings and gotchas is crucial. Luckily, codex is an amazing search engine.

When I want to quickly implement a one-off experiment in a part of the codebase I am unfamiliar with, I get codex to do extensive due diligence. Codex explores relevant slack channels, reads related discussions, fetches experimental branches from those discussions, and cherry picks useful changes for my experiment. All of this gets summarized in an extensive set of notes, with links back to where each piece of information was found. Using these notes, codex wires the experiment and makes a bunch of hyperparameter decisions I couldn't possibly make without much more effort.

Asking for a second opinion greatly increases my confidence in what I'm shipping. In settings where mistakes are costly, you want an incredibly diligent, high-recall search agent. Codex routinely scratches that itch for me.

Coding agents are also great at data analysis, and have made it very easy to quickly get insights from data. Currently, the real bottleneck is figuring out **what** to analyze.

Recently, I aggressively scaled some of our model behavior efforts using codex. I realized that our internal slack is filled with discussions, reports, and data all relating to different types of model behavior which we might want to test for more rigorously. I used codex to locate and extensively crawl the appropriate channels and generate descriptions of testable hypotheses. Beyond reading slack, it looked at screenshots people shared, pulled documents related to model behavior, and navigated spreadsheets. Over the course of several hours, this resulted in over 700 new hypotheses which are currently improving our understanding of model behavior and user preferences.

Most of this work was done with GPT-5.2, but I've been testing the new GPT-5.3-codex model for a few days now. My tokens-used per day are going up, which I think loosely correlates with my productivity.

I find GPT-5.3-codex to be particularly good at managing multiple subagents concurrently. Additionally, the recent speed-ups to the codex stack make the whole subagent experience feel a lot more snappy.

My workflow is currently shifting towards only talking to one agent, which in turn orchestrates a battalion of agents to do slack research, code research, code writing, and data science. This drastically reduces the amount of context-switching I need to do in order to parallelize my work through agents. However, when I need to do a crucial task, I still opt to directly talking to that specific subagent.

## Implications for Society

These workflows reveal something fundamental about how organizations can operate. In both of my use-cases, I achieved comprehensive cross-organizational knowledge transfer without manual coordination. No meetings, no emails, no asking around. I simply pointed codex at the problem and it aggregated knowledge from dozens of people, who didn't even know they were contributing to my cause.

I can't help but wonder how this will impact society. Traditionally, organizations pay some headcount-tax: add more people and total output increases, but each additional person contributes less because coordination overhead grows. This is a huge issue. Modern organizations use tools like unstructured communication channels (Slack, Teams), shared codebases, and centralized documentation to mitigate this, but there's still massive friction. Surfacing the right context for any given decision still requires significant human effort.

With the technology available today, we can now traverse an organization's entire information landscape and synthesize relevant context on demand. We can make a real dent into inefficiencies every organization on the planet suffers from.

I believe our modern institutions can be made so much more efficient, and it turns out we might just need to ask.

---

**Published:** 10:24 AM · Feb 5, 2026  
**Engagement:** 132 replies · 366 reposts · 3.7K likes · 6.9K bookmarks · 1.1M views