---
url: https://x.com/MengTo/status/2019789723590697257
author: Meng To (@MengTo)
captured_date: 2026-02-06
---

# How OpenClaw + Codex are changing the way I work as a designer

(Description: Hero image showing multiple design application interfaces and outputs including chat windows with AI-generated content, design mockups with green accent colors, and "VISION BEYOND DESIGN" branded material displayed on a landscape background)

As someone who hadn't warmed up to Claude Code yet (terminal isn't my favorite tool), it took me a few days to see the actual benefits. OpenClaw requires some real setup and thinking outside the box, especially for visual people.

So let's start with how OpenClaw is changing my workflow, then I'll cover where Codex fits below.

## The tools I'm replacing (and why)

A lot of "AI tooling" is actually just glue:

- copy/paste between apps
- context switching between chats, docs, terminals
- remembering where things live

OpenClaw replaces the glue with something simpler: **one assistant that can reach your real tools** (files, shell, browser, messaging) with a deliberate security model.

## Notion → local Markdown files + Obsidian

(Description: Screenshot showing OpenClaw interface with multiple panel windows displaying chat commands, markdown file preview, and design workflow visualization against a landscape background)

I still like Notion, but I don't like using it as the *source of truth*.

With OpenClaw, I can write everything in **Markdown** (in chat), commit it, and export it to:

- HTML
- a preview site
- a real site

I use Obsidian to preview and do quick edits when I want a fast visual pass before publishing.

The writing loop I trust is hybrid:

- AI edits local Markdown files
- I manually tweak in Obsidian when needed
- preview stays fast, so quality control is easy

The big win: local Markdown files live with the project. Versioned. Searchable. Scriptable.

## Midjourney / Krea → Nano Banana Pro local ops (APIs via Codex + Telegram)

(Description: Telegram messaging interface showing 4 bot avatars (Shiori, Komori, Sakura, Shimo) with conversation threads, alongside a grid of AI-generated lifestyle and product photography showcasing various poses, professional portraits, and everyday scenes)

Doing ops with my 4 agents in Telegram

I replaced Midjourney and Krea with Nano Banana Pro, and run those image APIs via Codex + Telegram.

This changed everything for image generation in my workflow.

I used Midjourney a lot before (had a $200/m sub), but the error rate was still high. I hit similar issues with FLUX, Ideogram, and OpenAI Image 1: either too many mistakes, or iteration that felt too slow for production work.

Nano Banana Pro is far better for hands, small details, and realistic down-to-earth images.

The aesthetic also matches what modern product and marketing sites already use: more grounded, less synthetic, fewer obvious artifacts like broken fingers. In practice, my hit rate is very high, so I waste less time re-rolling outputs.

For the kind of work I do, the killer feature isn't "a pretty image generator." It's the pipeline:

- generate new images from any reference image on my machine
- lock to specific aspect ratios / resolutions
- organize outputs locally
- generate variations in batches at 50% discount while I sleep
- run image APIs through Codex and Telegram workflows
- send image results back to Telegram as attachments for visual review (easy zoom, quick approve/reject)
- then spin up a little browseable gallery when I need to review

The key is still prompt quality. Strong prompts plus a strong reference library are what make the workflow consistently good.

That replaces a lot of what I used Midjourney/Krea for.

**Prompt:**

"Generate 5 images inspired by this reference. No UI, no text, no logos. No collage. Don't copy, only use as a reference, be creative, change names, text, numbers but maintain the same visual style. Use varied aspect ratios across the set: 16:9, 4:3, 1:1, 3:4, 9:16. Make details ultra-sharp."

## Cursor / Lovable / v0 / Aura → one workflow that actually ships

(Description: Code editor interface showing multiple windows with syntax-highlighted code, file tree navigation on the left, and code diff comparisons displaying changes across repository files)

I still use Cursor for code review when changes get large. Codex is strong for surgical task execution, but its UI is still minimal, so Cursor is better when I need to inspect complex diffs and catch issues across a large codebase.

Lovable, v0, and Aura are in the same bucket for me: prototype fast, build full websites, and publish.

Disclosure: I build Aura, so I am biased here.

Here are the pieces that matter for loop-closing:

- strong templates, visual design explorations with variant.ai
- ready-made assets and @ references
- a more advanced manual design layer (Figma-like editing)
- publishing and custom domain workflows
- CMS, Collaboration

The goal is not just generation. The goal is solving the hard parts creators should not rebuild from scratch every time, and create their greatest work. If tools stop chasing the best workflow, it becomes obsolete fast to AI. Taste and manual edits still matter.

OpenClaw + Codex are strongest for starting projects, organizing work, and gluing systems together.

## Figma and Nano Banana Pro in practice

Figma is still excellent for precise manual edits, and I still keep an active subscription.

In day-to-day execution, I use it less for first-pass generation:

- website creation, slides, prototyping, animations moves more into Codex, v0, lovable, Aura.
- image and marketing material work moves more into Nano Banana Pro

Nano Banana Pro keeps improving fast. Typography is already strong, UI quality is decent, and it is clearly getting better over time.

The real multiplier is prompt quality plus reference quality. With strong prompts and a strong reference library of past work and inspirations, Nano Banana Pro becomes extremely potent.

(Description: Four-panel grid of AI-generated design assets showing: top-left a gradient tech interface mockup with purple accent, top-right a mobile app interface with Step 2 instructions, bottom-left a portrait of a person in olive jacket with "EXPLORE VARIATIONS" text and mountain landscape, bottom-right a dark blue interface displaying "AI ships fast. But it also ships... generic." with control interface elements)

Made with Nano Banana using Telegram while waiting for my order at the restaurant

## Why Codex matters in this setup

OpenClaw gives me the **agent on my machine**. Codex gives that agent **real coding leverage**.

The combo matters because I'm not just asking for ideas — I'm asking for:

- fast, surgical edits across real files
- code that compiles and matches the existing style
- refactors that don't break the product
- paired work where I can stay in design mode and still ship

Codex makes the workflow feel like a real teammate, not a chat toy.

## Codex vs OpenClaw (how I think about it)

Codex is the **coding specialist**. It's smarter at code, works repo by repo, and stays focused on shipping clean changes.

OpenClaw is the **agency layer**. It reaches more apps, more messaging, and more day‑to‑day workflow. It also feels more self‑improving across the stuff I actually do.

If I'm on the go, OpenClaw wins because it's already where I am. Codex doesn't have a phone app right now.

Codex has skills, but they're more limited. Building new ones is real work compared to OpenClaw's "just do it" vibe.

One big Codex advantage: **visibility**. You can follow the commands it runs, see the code it changes, and review diffs in the UI. It's good at hiding that complexity, but it's still there when you want it.

OpenClaw is the opposite: you can dig into logs, but you don't see the full picture — especially on the go. That's fine for a lot of work, but for real code changes it matters.

Maybe in a future where AI is a perfect coder, that won't matter. Right now, if you're serious about shipping, **code review is still a habit**, especially as projects get more complex.

## What I'm actually shipping with it

For context, before AI I depended on a team of about 5 to 10 people. A single product of similar caliber often took around 3 months with normal PR cycles and handoffs. Now we can ship that same level in about a week, and this workflow keeps compressing that timeline.

Design speed changed even more. We used to spend around 3 weeks on one design or even a small UI component set just at the Figma layer. Now we ship full templates that are publishable, live, and tied directly to content and distribution.

As a creator, this is not one output stream. I regularly ship **20-50 templates a month**, large features across multiple apps with codebases well over **500k lines**, plus the full content and marketing layer around those products.

That means I am shipping in parallel: features, assets, prompts, video edits, YouTube content, social posts, and long-form writing. This workflow matters because it made me at least **2x faster** again, on top of already being roughly **5-10x** faster than I was two years ago.

- Code and product features across ~**$95k MRR** worth of projects
- Templates, landing pages, and design explorations at high volume
- Marketing assets, video content, social posts, and written content (planned and versioned in Markdown)

(Description: Four-panel gallery showing AI-generated website templates and designs: top-left a dark theme interface with "Funding manifesto" and minimal sidebar, top-middle a centered design with header text and sidebar navigation, bottom-left a colorful card-based layout with blue and orange accents showing "Skills page detail", bottom-right a dark interface with purple gradient and large hero text)

Templates I'm shipping on Aura

## Shipping real features

I'm shipping code and features that are getting harder and more complex.

Recent examples:

- **CMS**: AI‑generated collections/items, plus imports from Notion and Google Sheets
- **Custom domain names**: I had no idea how to do this before; now it ships
- **Skills**: skills page + skill detail, referencing skills in prompts, and an admin UI to add/edit skills
- **Playwright screenshots**: I used html-to-canvas & image-to-html and they were... bad. Lots of rendering issues. Codex helped me ship a Playwright script that creates near-perfect screenshots of sites.

Even updates to old projects are trivial now: tell it the app + repo + feature, and it fixes, runs commands, and deploys with very little intervention.

The autonomy is real: if you ask it to be more autonomous, it **will** be.

All of that shipped in **under a week** while I was still doing ops — generating images, handling other tasks, and shipping across multiple sites. This is the new reality.

(Description: Four-panel grid showing lifestyle and workspace photography: top-left wooden shelf with white objects and desk setup, top-right papers on desk with golden hour sunlight creating dramatic shadows, bottom-left camera lens with phone showing portrait image and notebook, bottom-right laptop on wooden desk with blurred window view of outdoor scenery)

Assets exploration while riding the taxi

## Cool stuff I can do (because it lives on your machine)

Rule of thumb: **start with OpenClaw for general life stuff**. As you specialize, layer in **Codex** for deep code work.

- **Print flows:** "Print this doc" (kids homework, forms, PDFs) → find files, generate a quick quiz, export to PDF, print
- **Start & publish projects:** spin up a site or interactive demo from one prompt (folders, README, scripts, basic UI). Can even push the github project.
- **Admin + accounting:** rename and file receipts, prep docs, summarize PDFs, move files where they belong
- **Image ops:** batch variations from *any* local image (ratios, crops, iterations). I increasingly use Nano Banana Pro for graphic design.
- **Web Design ops:** research prompts, create skills for web design, create quick designs in html.
- **Content ops:** speak your ideas, turn them into plan.md + content.md, keep everything versioned

The core difference is **access**. OpenClaw isn't just a browser or a single app — it can reach **everything on my computer**. If it exists locally, it's addressable.

At the end of the day, this is about **reducing friction**. If I can talk, it can capture the idea, structure it, and ship it — that turns daily life into real output.

(Description: Landscape background with OpenClaw file system interface showing file browser sidebar with dropdown menus for accessing local documents, folders, and file organization options)

## From Cursor/Terminal to Codex

I used to split time across Claude Code and Cursor. Between subscriptions and API keys, it was easy to blow past **$200+/month per tool** — and if you forget to cancel, those costs stack up fast.

Codex is now my **default coding tool**. It's strong at multi‑project, multi‑task work, and feels more agentic — like it's borrowing from the OpenClaw playbook — which matters when the codebase is big.

Multitasking is a big reason why. I can queue tasks back to back while the agent is still running: submit, submit again, keep going.

In my workflow, OpenClaw is solid for a few queued tasks, but around 3+ it can start to blur context. Codex handles bigger queues better (5-10 tasks) because each thread stays more surgical and scoped.

So my current rule:

- **Codex** when I'm coding and shipping.
- **OpenClaw** when I'm on the go or need cross‑app agency.

## Telegram becomes my control room (and why I split into 4 bots)

(Description: Telegram desktop application showing conversation threads with 4 distinct bot profiles (Shiori, Komori, Sakura, Shimo) with different avatar colors and icons, alongside a right panel showing content including "Write blogs locally with AI" message and design mockup)

Keeping track of conversations is the real problem, especially in Telegram where tasks can get very general very quickly. I also need to track multiple projects at once, so splitting into multiple bots helps keep related tasks and context together instead of mixing everything in one thread.

It is also a mobile reality issue. In Singapore, I still do not have practical mobile access to tools like Codex or Claude Code in the same way I can use Telegram, and that is true for many creators outside a few core markets. OpenClaw + Telegram is the best next option for staying productive on the go.

Image ops is a big win here. I can run requests and review visual outputs while traveling or waiting in line, instead of blocking all work until I am back at a desktop.

Splitting into multiple bots is really about **separating responsibilities** so the context stays clean.

- **Shiori** → writing + narrative structure
- **Komori** → image pipelines + asset generation
- **Sakura** → design critique + calm iterations
- **Shimo** → ops + system hygiene

It sounds like overhead, but it reduces the real tax: the agent guessing what mode it should be in.

## The system: SOUL + projects + files

This model is becoming standard in the new generation of AI tools: memory, personality, workflow rules, and skills all living in files. Codex and Claude Code workflows are converging on the same idea because it works.

One detail that matters once you split bots: **each bot should have its own SOUL.md, IDENTITY.md, and MEMORY.md**.

It's not roleplay. It's containment.

- Less cross-contamination between tasks
- Less "who am I right now?" confusion
- Clearer security boundaries (what each bot should/shouldn't do)

(Description: Desktop file system interface showing file browser window with sidebar containing folders like "Users", "Configurations", and "Data", displaying organized file structure on a landscape background)

OpenClaw effortlessly viewed/read all my designs, pdf, invoices and renamed/organized them based on my prompt

## Drawbacks (the annoying parts)

OpenClaw isn't magic. It's a workflow trade.

- **No response streaming (yet).** You don't see the model "typing" or a live trace of what it's thinking.
- **You'll still get permission prompts.** For anything that can be destructive or sensitive, I've found it's safer to have the assistant **ask you to run commands** (or explicitly confirm) instead of auto-executing.
- **One task at a time.** There's no real concurrency: you can't have it run 5 separate projects in parallel without spinning up separate agents and managing the overhead.
- **Security is your responsibility.** If you set it up wrong, you can create a very hackable surface area. You need to regularly revisit your security posture.

Because of that one-task-at-a-time limit, I usually multitask across Codex, Claude Code, and other tools in parallel threads. Oh and don't forget to set your security.
```
openclaw security audit --fix
```

## Conclusion: where this is heading

I believe the next generation of AI tools will keep moving toward this model: persistent memory, reusable skills, clear personality, and workflow files that define how each agent works.

Those agents will increasingly communicate with each other and connect across all layers of work and life: email, design, coding, content, video, and operations.

I do not agree with the idea that AI replaces UI. We are actually creating more UI than ever, because the cost of building apps, websites, and tools is now much lower. The big shift is the coding layer: you can speak intent, review diffs, and supervise assistants instead of writing every line manually.

That changes the human role. I spend more time on quality control, product testing, research, marketing, and taste, and less time on repetitive execution.

The result is practical, not theoretical: I get more done, with better quality, and still have more time for life outside work. For me, this is the most exciting part of where AI tooling is going.

(Description: Four-panel collage of design mockups and slides: "Codex makes it real shipping" in serif typography, "OpenClaw is the agency layer - It reaches real tools files shell browser", "Write blogs locally with AI - Markdown as source of truth Versioned and searchable", and additional design presentation mockups with blue and orange gradients)

Creating my slides for this article with Telegram