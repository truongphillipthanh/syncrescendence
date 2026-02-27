---
url: https://x.com/aidenybai/status/2018812643369488747
author: "Aiden Bai (@aidenybai)"
captured_date: 2026-02-13
id: SOURCE-20260203-011
original_filename: "20260203-x_article-how_i_made_claude_code_3x_faster-@aidenybai.md"
status: triaged
platform: x
format: article
creator: aidenybai
signal_tier: strategic
topics:
  - ai-engineering
  - developer-tools
  - vibe-coding
  - performance
teleology: implement
notebooklm_category: ai-engineering
aliases:
  - "Aiden Bai - Claude Code 3x faster for frontend"
synopsis: "Analysis of why coding agents struggle with frontend work — the intent translation pipeline (UI vision to prompt to code to UI) is lossy. Presents a solution that achieves 3x faster edits on average by reducing this translation loss, with benchmark data showing distribution improvements."
key_insights:
  - "The core bottleneck for AI coding agents on frontend is the lossy intent translation pipeline: mental image to prompt to code to rendered UI."
  - "Reducing translation loss between intent and output produces 3x speed improvements, suggesting the prompt-to-code step is the primary bottleneck, not model speed."
  - "Benchmark-driven optimization of agent workflows (measuring time per edit with distribution analysis) is emerging as a rigorous approach to agent performance engineering."
---
# How I made Claude Code 3x faster

(Description: A dark-themed benchmark visualization showing a magenta and gray distribution curve with the title "3x faster on average" displayed below. The x-axis represents "Time per Edit (seconds)" ranging from 0 to 30, with two overlapping probability distributions illustrating the performance comparison between control and treatment groups.)

## The Problem: Translating Intent is Lossy

Coding agents suck at frontend because **translating intent** (from UI → prompt → code → UI) is lossy.

For example, if you want to make a UI change:

1. Create a visual representation in your brain
2. Write a prompt (e.g. "make this button bigger")

How the coding agent processes this:

1. Turns your prompt into a trajectory (e.g. "let me grep/search for where this code might be")
2. Tries to guess what you're referencing and edits the code

Search is a pretty random process since language models have non-deterministic outputs. Depending on the search strategy, these trajectories range from instant (if lucky) to very long. Unfortunately, this means added latency, cost, and performance.

## Two Current Solutions

Today, there are two solutions to this problem:

- **Prompt better:** Use @ to add additional context, write longer and more specific prompts (this is something YOU control)
- **Make the agent better at codebase search** (this is something model/agent PROVIDERS control)

Improving the agent is a **lot** of unsolved research problems. It involves training better models (see [Instant Grep](https://cursor.com/changelog/2-1), [SWE-grep](https://cognition.ai/blog/swe-grep)).

Ultimately, reducing the amount of translation steps required makes the process faster and more accurate (this scales with codebase size).

But what if there was a different way?

## Digging through React internals

In my ad-hoc tests, I noticed that referencing the file path (e.g. path/to/component.tsx) or something to grep (e.g. className="flex flex-col gap-5 text-shimmer") made the coding agent **much** faster at finding what I was referencing. In short - there are shortcuts to reduce the number of steps needed to search!

Turns out, React.js exposes the source location for elements on the page. React Grab walks up the component tree from the element you clicked, collects each component's component name and source location (file path + line number), and formats that into a readable stack.

It looks something like this:
```javascript
<span>React Grab</span> in StreamDemo at components/stream-demo.tsx:42:11
```

When I passed this to Claude Code, it **instantly** found the file and made the change in a couple seconds. Trying on a couple other cases got the same result.

## Benchmarking for speed

I used the [shadcn/ui dashboard](https://github.com/shadcn-ui/ui) as the test codebase. This is a Next.js application with auth, data tables, charts, and form components.

The benchmark consists of [20 test cases](https://github.com/aidenybai/react-grab/blob/main/packages/benchmarks/test-cases.json) designed to cover a wide range of UI element retrieval scenarios. Each test represents a real-world task that developers commonly perform when working with coding agents.

Each test ran twice: once with React Grab enabled (treatment), once without (control). Both conditions used identical codebases and Claude 4.5 Sonnet (in Claude Code).

(Description: A side-by-side comparison showing two code search processes. Left side labeled "Without React Grab" shows multiple file reads and grep operations for a task like "Find the forgot password link in the login form". Right side labeled "With React Grab" shows the same task with a direct reference to the exact component file path with line numbers.)

Without React Grab, the agent must search through the codebase to find the right component. Since language models predict tokens non-deterministically, this search process varies dramatically - sometimes finding the target instantly, other times requiring multiple attempts. This unpredictability adds latency, increases token consumption, and degrades overall performance.

With React Grab, the search phase is eliminated entirely. The component stack with exact file paths and line numbers is embedded directly in the DOM. The agent can jump straight to the correct file and locate what it needs in O(1) time complexity.

…and turns out, Claude Code becomes ~**3× faster with React Grab!**

(Description: A dual-axis probability distribution chart showing normalized comparison. The magenta curve (With React Grab - 5.8s) is significantly compressed and shifted left compared to the gray curve (Without React Grab - 16.8s), visually demonstrating the 3x performance improvement. The chart indicates "3x faster on average" with time measurements on the x-axis and density on the y-axis.)

Distribution of edit times across 20 UI tasks. React Grab eliminates the search phase by providing exact file paths and line numbers, letting the agent jump straight to the code.

(Description: A comparative bar chart showing three key metrics: Avg Duration (16.82s vs 5.77s), Total Cost ($0.72 vs $0.29), and Avg Tool Calls (5.3 vs 0.3). Each metric displays gray bars for Control and magenta bars for React Grab, with percentage improvements shown (65.7%, 60.1%, and 93.4% respectively).)

Below are the latest measurement results from all 20 test cases. The table below shows a detailed breakdown comparing performance metrics (time, tool calls, tokens) between the control and treatment groups, with speedup percentages indicating how much faster React Grab made the agent for each task.

(Description: A comprehensive data table with 20 rows of test cases including Calendar Data Cell, Drag Handle, Dropdown Actions, and others. Columns include TEST NAME, INPUT TOKENS, OUTPUT TOKENS, COST, DURATION, and REACT GRAB performance metrics, with green highlighting indicating improvements in the treatment group. Speedup percentages range from approximately 50% to 97%.)

To run the benchmark yourself, check out the benchmarks directory on GitHub.

## How it impacts you

The best use case I've seen for React Grab is for low-entropy adjustments like: spacing, layout tweaks, or minor visual changes.

If you iterate on UI frequently, this can make everyday changes feel smoother. Instead of describing where the code is, you can select an element and give the agent an exact starting point.

React Grab works with **any** IDE or coding tool: Cursor, Claude Code, Copilot, Codex, Zed, Windsurf, you name it. At its core, it just adds extra context to your prompt that helps the agent locate the right code faster.

We're finally moves things a bit closer to narrowing the intent to output gap (see [Inventing on Principle](https://youtube.com/watch?v=PUv66718DII&t=390)).

## What's next

There are a lot of improvements that can be made to this benchmark:

- Different codebases (this benchmark used shadcn dashboard) - what happens with different frameworks/sizes/patterns? Need to run it on more repos.
- Different agents/model providers
- Multiple trials and sampling - decrease variance, since agents are non-deterministic

On the React Grab side - there's also a bunch of stuff that could make this even better. For example, grabbing error stack traces when things break, or building a Chrome extension so you don't need to modify your app at all. Maybe add screenshots of the element you're grabbing, or capture runtime state/props.

If you want to help out or have ideas, dm me [@aidenybai](https://x.com/@aidenybai) or open an issue on GitHub.

React Grab is free and open source. [Go try it out!](https://www.react-grab.com/)