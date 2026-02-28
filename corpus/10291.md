# LLMs Eat Scaffolding for Breakfast

(Description: Three colorful abstract icons representing AI concepts: a black spiral/DNA-like shape, an orange sunburst pattern, and a rainbow gradient 4-pointed star)

It's Monday morning, 6:30 AM in San Francisco. I already know what's gonna happen this week. We're gonna delete our code. A lot of it. Because models are eating our code. I will show up to our Mission office and delete thousands of lines of code. Again.

Each time a new LLM model comes out, that's the same story.

LLMs have limitations so we build scaffolding around to make them work. Each models introduce new capabilities so that old scaffoldings must be deleted and new ones be added.

But as we move closer to super intelligence, less scaffoldings are needed. This post is about what it takes to build successfully in AI today.

## Why We Build Scaffolding?

Every line of scaffolding is a confession: the model wasn't good enough.

- LLMs can't read PDF? Let's build a complex system to convert PDF to markdown
- LLMs can't do math? Let's build compute engine to return accurate numbers
- LLMs can't handle structured output? Let's build complex JSON validators and regex parsers
- LLMs can't read images? Let's use a specialized image to text model to describe the image to the LLM
- LLMs can't read more than 3 pages? Let's build a complex retrieval pipeline with a search engine to feed the best content to the LLM
- LLMs can't reason? Let's build chain-of-thought logic with forced step-by-step breakdowns, verification loops, and self-consistency checks

etc, etc... millions of lines of code to add external capabilities to the model.

But look at models today: GPT-5.2 is solving frontier mathematics, Grok-4 Fast can read 3000+ pages with its 2M context window, Claude 4.5 can ingest images or PDFs, all models have native reasoning capabilities and support structured outputs.

The once essential scaffolding are now obsolete. Those tools are backed in the model capabilities.

## Why it's so hard to build in AI?

It's nearly impossible to predict what scaffolding will become obsolete and when. What appears to be essential infrastructure and industry best practice today can transform into legacy technical debt within months.

The best way to grasp how fast LLMs are eating scaffolding is to look at their system prompt (the top-level instruction that tells the AI how to behave).

Looking at the prompt used in Codex, OpenAI coding agent from GPT-o3 model to GPT-5 is mind-blowing.

GPT-o3 prompt: 310 lines
GPT-5 prompt: 104 lines

The new prompt removed 206 lines. A 66% reduction.

GPT-5 needs way less handholding. The old prompt had complex instructions on how to behave as a coding agent (personality, preambles, when to plan, how to validate). The new prompt assumes GPT-5 already knows this and only specifies the Codex-specific technical requirements (sandboxing, tool usage, output formatting).

The new prompt removed all the detailed guidance about autonomously resolving queries, coding guidelines, git usage. It's also less prescriptive. Instead of "do this and this" it says "here are the tools at your disposal."

As we move closer to super intelligence, the models require more freedom and leeway (scary, lol!).

Advanced models require simple instructions and tooling. Claude Code, the most sophisticated agent today, relies on a simple filesystem instead of a complex index and use bash commands (find, read, grep, glob) instead of complex tools.

It moves so fast. Each model introduces a new paradigm shift. If you miss a paradigm shift, you're dead.

Having an edge in building AI applications require deep technical understanding, insatiable curiosity, and low ego. But because everything changes, it's good to focus on what won't change

## The Four LLM Constants

### 1. Context Windows: The Great Expansion

Context window is how much text you can feed the model in a single conversation. Early model could only handle a couple of pages. Now it's thousands of pages and it's growing fast.

Dario Amodei the founder of Anthropic expects 100M+ context windows while Sam Altman hinted at billions of context tokens. It means the LLMs can see more context so you need less scaffolding like retrieval augmented generation.

- November 2022: GPT-3.5 could handle 4K context
- November 2023: GPT-4 Turbo with 128K context
- June 2024: Claude 3.5 Sonnet with 200K context
- June 2025: Gemini 2.5 Pro with 1M context
- September 2025: Grok-4 Fast with 2M context

### 2. Generation Speed: From Seconds to Instant

Models used to stream at 30-40 tokens per second. Today's fastest models like Gemini 2.5 Flash and Grok-4 Fast hit 300+ tokens per second. A 5x improvement.

On specialized AI chips (LPUs), providers like Cerebras push open-source models to 2,000 tokens per second. It is rumored that GPT Codex will use Cerebras' inference speed.

We're approaching real-time LLM: full responses on complex task in under a second.

### 3. Intelligence: There is no Wall

LLMs are becoming exponentially smarter. With every new model, benchmarks get saturated. On the path to AGI, every benchmark will get saturated. Every job can be done and will be done by AI.

As with humans, a key factor in intelligence is the ability to use tools to accomplish an objective. That is the current frontier: how well a model can use tools such as reading, writing, and searching to accomplish a task over a long period of time.

This is important to grasp. Models will not improve their language translation skills (they are already at 100%), but they will improve how they chain translation tasks over time to accomplish a goal. For example, you can say, "Translate this blog post into every language on Earth," and the model will work for a an hour or more on its own to make it happen.

Tool use and long-horizon tasks are the new frontier.

### 4. Cost: The Cost of Intelligence is Going to Zero

The cost of intelligence is going to zero. As Sam Altman noted:

> "The cost to use a given level of AI falls about 10× every 12 months, and lower prices lead to much more use."

Today's smartest model costs what the smartest model cost 3 years ago. This exponential decline in pricing means AI capabilities that were once prohibitively expensive are becoming accessible to everyone.

## What Nobody Tells You About Scaffolding

The uncomfortable truth: most engineers are maintaining infrastructure that shouldn't exist but they don't know it yet.

Models will make it obsolete and the survival of AI apps depends on how fast you can adapt to the new paradigm. That's what startups have an edge over big companies. Bigcorp are late by at least two paradigms.

Some examples of scaffolding that are on the decline:

- **Vector databases**: Companies paying thousands/month for when they could now just put docs in the prompt or use agentic-search instead of RAG
- **LLM frameworks**: These frameworks solved real problems in 2023. In 2025? They're abstraction layers that slow you down. The best practice is now to use the model API directly.
- **Prompt engineering teams**: Companies hiring "prompt engineers" to craft perfect prompts when now current models just need clear instructions with open tools
- **Model fine-tuning**: Teams spending months fine-tuning models only for the next generation of out of the box models to outperform their fine-tune
- **Custom caching layers**: Building Redis-backed semantic caches that add latency and complexity when prompt caching is built into the API.

This cycle accelerates with every model release. The best AI teams master have critical skills:

- **Deep model awareness**: They understand exactly what today's models can and cannot do, building only the minimal scaffolding needed to bridge capability gaps.
- **Strategic foresight**: They distinguish between infrastructure that solves today's problems versus infrastructure that will survive the next model generation.
- **Frontier vigilance**: They treat model releases like breaking news. Missing a single capability announcement from OpenAI, Anthropic, or Google can render months of work obsolete.
- **Ruthless iteration**: They celebrate deleting code. When a new model makes their infrastructure redundant, they pivot in days, not months.

It's not easy. Teams are fighting powerful forces:

- **Lack of awareness**: Teams don't realize models have improved enough to eliminate scaffolding (this is massive btw)
- **Sunk cost fallacy**: "We spent 3 years building this RAG pipeline!" (lol)
- **Fear of regression**: "What if the new approach is simple but doesn't work as well on certain edge cases?"
- **Organizational inertia**: Getting approval to delete infrastructure is harder than building it
- **Resume-driven development**: "RAG pipeline with vector DB and reranking" looks better on a resume than "put files in prompt" right?

In AI the best team builds for fast obsolescence and stay at the edge.

## The counter intuitive truth

Software engineering sits on top of a complex stack. More layers, more abstractions, more frameworks. Complexity was a sophistication. A simple web form in 2024? React for UI, Redux for state, TypeScript for types, Webpack for bundling, Jest for testing, ESLint for linting, Prettier for formatting, Docker for deployment….

AI is inverting this. The best AI code is simple and close to the model.

Experienced engineers look at modern AI codebases and think: "This can't be right. Where's the architecture? Where's the abstraction? Where's the framework?"

The answer: The model ate it bro, get over it. The worst AI codebases are the ones that were best practices 12 months ago.

As models improve, the scaffolding becomes technical debt. The sophisticated architecture becomes the liability. The framework becomes the bottleneck.

LLMs eat scaffolding for breakfast and the trend is accelerating.