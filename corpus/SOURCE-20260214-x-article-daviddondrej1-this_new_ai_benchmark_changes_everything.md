# This New AI Benchmark Changes Everything
(Description: A horizontal bar chart showing AI model performance rankings on SWE-rebench. Models are listed on the x-axis with corresponding percentage scores on the y-axis, ranging from approximately 30% to 52.9%. Claude Code with Opus 4.6 leads at 52.9% (red bar), followed by Claude Opus 4.6 at 51.7%. Western AI labs (Anthropic, OpenAI, Google) dominate the top positions shown in red, light gray, and other colors. Chinese models including Kimi, GLM, Qwen, and MiniMax appear in the lower rankings, shown in green, cyan, and purple bars, with MiniMax M2.5 at 39.6%.)
Everyone thinks the AI race is close.
It's not.
A new benchmark called **SWE-rebench** just came out. And it basically proved that a lot of these Chinese AI companies have been optimizing their models on popular evals & benchmarks.
And now we have the numbers to prove it.
## I. The Benchmark Scam
Here's how AI benchmarks are supposed to work.
You create a standardized test. You give it to every model. The best model wins.
Simple.
Except there's a massive flaw. The questions are public.
Which means if you're a lab with fewer resources, less talent, and less GPUs — you don't have to build a better model. You just train your model on the test answers. You design your training data to overfit on those specific questions.
That's it. That's the trick.
You'll score really well. But your model didn't actually get smarter. It just memorized the answers.
This is exactly what's been happening in AI for the past 12 months.
## II. What SWE-rebench Is and Why It Matters
SWE-bench has been one of the most popular coding benchmarks in AI.
Every lab uses it. Every model announcement references it. It became the standard for measuring whether an AI can actually write code and solve real engineering problems.
The problem? It's been completely saturated.
The questions have been public for so long that labs — especially Chinese labs — have been designing their training data to overfit on these exact problems. Not to build better models. To score higher on this one test.
SWE-rebench fixes this.
It pulls fresh GitHub tasks from recent repos. New problems. Problems that no model has ever seen in training. Same difficulty. Same format. Same type of challenges.
The only difference is you can't cheat.
And the results are brutal.
## III. The Numbers
Here's what happened.
Claude Code with Opus 4.6 came in first at 52.9%. Claude Opus 4.6 on its own hit 51.7%. GPT-5.2 variants landed around 51%. Sonnet 4.5 at 47.1%. Gemini 3 Pro Preview at 46.7%. Codex at 44.0%.
The entire top 10 is Anthropic, OpenAI, and Google.
Now the Chinese models.
Kimi K2 Thinking: 43.8%. GLM-5: 42.1%. Qwen3-Coder-Next: 40.0%. MiniMax M2.5: 39.6%. Kimi K2.5: 37.9%.
Here's why this matters.
MiniMax M2.5 reported 80.2% on the original SWE-bench. Opus 4.6 scored 80.8%. On paper, they were basically the same model. The narrative everywhere was that Chinese open-source had caught up.
But on SWE-rebench? With fresh problems no model has seen before?
MiniMax dropped to 39.6%. Opus 4.6 hit 51.7%.
That's a 12-point gap. Completely invisible on the old benchmark.
These models were never comparable. MiniMax was just trained to ace that specific test.
## IV. They're Copying, Not Competing
This isn't an accident.
China has always been really good at copying technology. Not inventing it. Copying it. They did it with smartphones. Social media. EVs. And now they're doing it with AI.
But with AI you can't just copy the architecture and call it a day. You need compute. You need talent. You need data infrastructure. You need a research culture that can build frontier models from scratch.
Chinese labs have less of all of that compared to Anthropic and OpenAI. Less funding. Fewer GPUs. Less research talent.
So they cheat.
They pick the most popular benchmarks. They get the questions — because they're public. They design their training data to overfit on those benchmarks specifically.
The result is a model that looks world-class on a leaderboard. But the moment you give it a problem it hasn't been trained to solve, it falls apart.
That's not innovation. That's memorization.
SWE-rebench exposed the difference.
## V. Training Data Is Everything
This is the real takeaway.
You can train any neural net to ace any specific benchmark. Just feed it the right data. Overfit on those questions. You'll get impressive numbers.
But that doesn't make it a powerful model.
The reason people love Opus 4.6 — the reason it's #1 and #2 on SWE-rebench — is because you can put it in any situation and it performs. Coding. Writing. Analysis. Reasoning. Doesn't matter. It works.
It's a genuinely powerful general model.
That cannot be said for models that are hyper-trained on one benchmark.
The moment you remove the public questions and replace them with fresh ones — same difficulty, just new — the Chinese models collapse. MiniMax goes from "matching Opus" to 17th place.
That's not underperformance. That's what happens when you take the answer key away.
## VI. Stop Reading Benchmarks, Start Using Models
Here's what anybody who actually builds with AI already knows.
If you've spent a few hours on Opus 4.6 and then switched to MiniMax or GLM, you know the difference immediately. It's obvious. Even when the old benchmarks said they should be comparable, they never were in practice.
SWE-rebench just proved what power users already knew.
Anthropic and OpenAI are at least 6 to 12 months ahead. The gap is real. It's significant. And it was being hidden by corrupted benchmarks.
This is why we need to keep building new benchmarks. Discard the old ones that are saturated and contaminated. Pay attention to decontaminated benchmarks like SWE-rebench that actually test what matters — can this model solve problems it has never seen before?
That's the only question that matters if you're building real products with AI.
## VII. What You Should Actually Be Using Right Now
If you're building software with AI there are two tools you should be using. That's it.
**Claude Code powered by Opus 4.6.** Ranked #1 on SWE-rebench at 52.9%. Pass@5 of 70.8%. Best coding AI in the world right now.
**OpenAI's native Codex app with GPT-5.3 Codex.** The GPT-5.2 variants already hit 51% on SWE-rebench. The newer Codex model is even better.
Everything else is a distraction.
Yeah, MiniMax costs $0.09 per problem compared to $3.50 for Claude Code. It's cheaper. It's also ranked 17th instead of 1st.
Use the models that perform when the problems are real and fresh. Not the ones that only perform when they've already seen the test.
---
**P.S.:** If you already have $1,000 MRR or more, and want to scale to $30k and beyond, consider joining my Accelerator. I sold my AI startup, Vectal, for $1.8 million just 14 months after founding. And inside of the Accelerator, I help other founders do the same. Apply here → https://www.scalesoftware.ai/start