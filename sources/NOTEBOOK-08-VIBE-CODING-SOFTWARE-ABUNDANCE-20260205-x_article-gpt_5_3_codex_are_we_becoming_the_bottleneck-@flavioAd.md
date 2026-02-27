---
url: https://x.com/flavioAd/status/2019474660866290061
author: Flavio Adamo (@flavioAd)
captured_date: 2026-02-05
---

# GPT 5.3-Codex: Are we becoming the bottleneck?

(Description: Large gradient banner with blue-to-purple transition containing white text reading "GPT-5.3-Codex")

I started using GPT-5.3-Codex as my main model about two weeks ago, fully expecting it to be "just another iteration," but day after day it just made the work feel smoother in ways that were hard to quantify at first.

Beyond the usual benchmarks, I thought it would be more useful to share what will actually change in your day-to-day work.

## Visual understanding

I asked both (see below) models to recreate the Codex website starting from a single image; a pixel-perfect 1:1 reproduction. Here's the original reference image I gave both models:

(Description: Codex official website screenshot showing OpenAI branding, centered Codex logo with blue gradient background, navigation menu on left sidebar with options including "New thread," "Automations," and "Skills," center panel showing "Create a compelling launch hero for the new Codex app on openai.com," and right panel with code snippets and configuration options)

I ran this against **GPT 5.2 xHigh** and the new **GPT 5.3 xHigh**. Both took roughly 10 minutes to process, but the results were drastically different, and kinda… unexpected?

### GPT-5.2-Codex xHigh

(Description: Rendered website output showing Codex interface with similar layout to reference but with slightly different styling and positioning; sidebar navigation visible with menu items listed, center content area with text and interface elements)

### GPT-5.3-Codex xHigh

(Description: Rendered website output showing improved Codex interface with closer fidelity to original, better color matching with blue-purple gradient, improved button styling, corrected spacing and alignment, more polished visual presentation)

Yes, the GPT-5.3-Codex output is **closer to the original**. But that's not the interesting part.

## What I didn't expect

GPT-5.3-Codex finished generating the site and then... **it didn't stop**.

At a certain point, it installed a rendering library via npx, rendered the page it had just built, and compared it to the reference image I gave as context.

### Then it started correcting itself

- It noticed the primary button color didn't match the screenshot and fixed it.
- It noticed the app preview in the reference image was positioned lower and moved it.
- It adjusted spacing and alignment in multiple places.
- And it even provided a live preview of the rendering so I didn't have to open it locally to check the progress.

## Okay, Now the Serious Stuff (Production Bugs)

There's a layout bug in production on [avely.me](https://avely.me) that's been causing us pain for a while. Title handling is subtly broken, and every attempted fix so far had introduced new formatting issues.

I had already tried solving it with:

- Claude Code (Opus 4.5)
- GPT-5.2 Codex

Neither managed to fully fix it. So I gave the same exact problem to both GPT-5.2 Codex (again) and GPT-5.3 Codex.

### The first thing I noticed

**With GPT-5.2 Codex:** After about 2 minutes, this is what you see. Just a loader and eventual output

(Description: Screenshot showing dark interface with text "Exploring 6 files, 7 searches, 4 lists" followed by status lines: "Listed files," "Searched for handle in app," "Listed files in app," "Listed files in [handle]" (repeated), "Searched for Title in components")

**With GPT-5.3 Codex:** The result is much more verbose

(Description: Screenshot of verbose reasoning process showing detailed breakdown in dark box with text: "I'm going to trace the /handle page title component and reproduce the line-break/padding behavior in code, then patch the input/textarea logic so new lines render immediately and spacing is reduced." Below: "Explored 1 file, 1 search, 1 list" and additional reasoning steps about UI fixes)

It walked through what it believed the problem was, what it planned to change, and why, before touching the code.

Is this just a UX trick to make the wait feel shorter? Maybe. But I can see exactly what is happening behind the scenes without waiting for the final result. It makes me feel involved in the process, instead of just staring at a loading screen.

### So, what happened?

As mentioned, GPT 5.2-Codex (like Claude before it) failed to solve the issue "completely." In fact, while trying to fix the logic, it actually broke the title formatting.

- **GPT 5.2:** Took **11 minutes and 06 seconds**. Failed to solve the bug
- **GPT 5.3:** Took **7 minutes and 30 seconds**. Correctly solved the problem

## SO, Is it faster?

Yes. On paper, the difference might look small: a minute here, 30 seconds there. But if you are a power user like me, you understand the math: by the end of the day, that saved time compounds into hours.

## My Final Thoughts

I could have shown you 1,000 other examples, but I wanted to focus on the concrete differences that actually impact your daily workflow. I am confident that if you try it, you will feel the difference immediately.

We are living in an era where AI tools are finally fast enough that **we are the ones slowing things down**. This trend is only going to accelerate.

So, I'll leave you with one question: **Are we becoming the bottleneck?**

---

**Post Details:**
- Posted: 10:14 AM · Feb 5, 2026
- Views: 192.3K
- Replies: 14
- Reposts: 57
- Likes: 552
- Bookmarks: 403