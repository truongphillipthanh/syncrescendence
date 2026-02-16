---
url: https://x.com/EXM7777/status/2019433098795225325
author: Machina (@EXM7777)
captured_date: 2026-02-05
---

# X Thread: Model Benchmarking & AI Evaluation Strategy

stop trusting other people's takes for new models like Sonnet 5... everyone on X judges models based on coding evals... but your workflow is not their workflow

you might need it for copywriting, research, strategy, data analysis... and nobody is testing THAT

so build your own benchmarking station

here's how (using claude code):

use the prompt in the image to set up an environment where:
> you upload the exact prompts you use daily
> the new model runs all of them automatically
> you review every output yourself
> a competitor model scores each outputs

now you know exactly where the new model wins and where it doesn't

for YOUR tasks... not someone else's vibes on a timeline

---

(Description: Image showing a detailed task specification titled "# Task: Model Benchmarking Web App"

**# Task: Model Benchmarking Web App**

Build a React web app that tests how good an AI model is at different types of tasks. The user writes test prompts, the app sends them to a model, shows every response, and then asks a different AI model to score each response.

**# How Prompts Work**

Each prompt is a separate `.md` file inside a `/prompts` folder in the project. The file name is the prompt name. At the top of each file, a `category` field tells the app what type of task this is (coding, marketing, automation, content creation, etc.). Everything below is the actual prompt. Include a few example files so the user sees the format right away.

**# Picking Models**

The user picks two models: the one being tested, and a different one that acts as the judge. Both use the same API call format (OpenAI-compatible). Show a dropdown with these options already filled in:

- `=@openaiKey= `gpt-4.2`
- `=@anthropicKey= `sonnet-4`
- `=@geminitKey= `gemini-3-pro`
- `=@deepseekKey= `deepseek-v3.2`
- `=@xaiKey= `kini-k2.5`

Prompt the user to import more models if needed.

The tested model and the judge model cannot be the same. Block this in the interface.

**# How Judging Works**

The judge scores each output on five things: relevance, quality, creativity, practicality, and an overall score, each from 0 to 100. A 70 means "fine but nothing special." The judge also writes one sentence explaining the score.

The judging criteria change based on the category. Coding prompts get judged on correctness and edge cases. Marketing prompts get judged on persuasion and audience fit. If the category is not recognized, use general quality criteria.

The judge must return its scores as JSON. If the response is not valid JSON, try to pull out the numbers with a fallback method. If that also fails, show the raw response as the user can see what happened.

After every prompt has been scored, send one last request to the judge asking it to write a short summary (3-4 sentences) of what the tested model is good at and where it falls short. Show this summary at the top of the results.

**# What the User Sees**

1. `=@Setup area=` model selectors, API key fields, list of loaded prompts, a Run button and a Stop button
2. `=@Results area=` one card per prompt showing the benchmarked prompt, the full model response (with code highlighting where needed), the judge's scores and verdict. Cards appear one by one as each prompt finishes.
3. `=@Scorecard=` a bar chart showing average scores per category, color-coded from red (low) to green (high), the judge's summary, and a button to download all results as a JSON file.

Process prompts one at a time as the user can read each response as it comes in.

**# Important Rules**

- Dark mode, clean layout, plenty of space between cards – this is a reading tool
- If an API call fails, show the error on that card and move to the next prompt
- The Stop button pauses after the current prompt finishes and keeps all results so far
- Use React state only for storing data, no browser storage
- If no prompts are found, show a clear message explaining how to add them
- If an API key is missing, grey out the Run button and say why
)

---

i'll do that job for you, telling you exactly how to implement new releases each week here (launching end of the month):

[Link: weeklyaiops.com - The Real-Time AI Ops Community
Stop drowning in AI updates. Get one tested implementation guide every Monday. Real systems you can...]

---

each week there's a new release and it's the exact same pattern... people make you believe THIS thing is the real deal

but unless you try it in your own workflows, you can't tell

---

ik it sounds crazy