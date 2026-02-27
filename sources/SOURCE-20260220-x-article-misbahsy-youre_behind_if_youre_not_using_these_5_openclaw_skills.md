---
url: https://x.com/MisbahSy/status/2024919095318045029
author: "Misbah Syed (@MisbahSy)"
captured_date: 2026-02-21
id: SOURCE-20260220-003
original_filename: "20260220-x_article-youre_behind_if_youre_not_using_these_5_openclaw_skills-@misbahsy.md"
status: triaged
platform: x
format: article
creator: misbahsy
signal_tier: tactical
topics:
  - ai-agents
  - ai-workflow
  - git
  - gemini
  - architecture
  - rag
  - cli-tools
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "Youre Behind If Youre Not Using These 5 OpenClaw Skills"
synopsis: "You're Behind If You're Not Using These 5 OpenClaw Skills , "SUMMARIZE" (center-left), "GITHUB" (center), "NANO BANANA PRO" (center-right), and "NANO PDF" (right). Each section contains symbolic imagery representing its function — documents, a brain, code symbols, and editing tools."
key_insights:
  - "You're Behind If You're Not Using These 5 OpenClaw Skills , "SUMMARIZE" (center-left), "GITHUB" (center), "NANO BANANA PRO" (center-right), and "NANO PDF" (right)."
  - "Each section contains symbolic imagery representing its function — documents, a brain, code symbols, and editing tools."
  - "Winged figures and architectural elements complete the mystical, epic composition.) Most people are using OpenClaw like a chat toy."
---
# You're Behind If You're Not Using These 5 OpenClaw Skills
(Description: A dramatic black-and-white engraving-style illustration featuring a central figure in flowing robes surrounded by turbulent clouds and waves. Five labeled sections float above the clouds representing the five skills: "GOG — GOOGLE WORKSPACE" (left), "SUMMARIZE" (center-left), "GITHUB" (center), "NANO BANANA PRO" (center-right), and "NANO PDF" (right). Each section contains symbolic imagery representing its function — documents, a brain, code symbols, and editing tools. Winged figures and architectural elements complete the mystical, epic composition.)
Most people are using OpenClaw like a chat toy.
Ask a question. Get an answer. Maybe generate some code. Cool.
Meanwhile, the people getting actual leverage from their agents are doing something completely different. They're not asking questions. They're handing off entire workflows. Their agent reads their inbox, pulls data from spreadsheets, checks CI pipelines, generates images for a blog post, and edits a PDF — all before they've finished their morning coffee.
The difference isn't the model. It's the skills they've installed.
I've been trying a bunch of skills on ClawHub over the past few weeks and honestly, most of them are noise. But five of them — all by Peter Steinberger (@steipete), the genius who created OpenClaw — genuinely changed what my agent can do.
Here's the shortlist:
- **Gog** — Google Workspace (Gmail, Calendar, Drive, Sheets, Docs)
- **Summarize** — web pages, PDFs, YouTube videos
- **Github** — issues, PRs, CI, the full gh CLI
- **Nano Banana Pro** — image generation via Gemini 3 Pro
- **Nano Pdf** — edit PDFs with plain English
This isn't about installing more stuff. It's about installing the few things that change what your agent can actually do for you.
Let me walk you through what each one unlocks — and how I actually use them.
## 1. Gog: Your agent can finally touch your real work
This was the one that made me go "oh, this changes everything."
Gog is a Google Workspace CLI. Gmail, Calendar, Drive, Contacts, Sheets, Docs. It requires a quick OAuth setup, and then your agent has hands inside the tools where your actual work lives.
Before Gog, my agent could talk about my schedule. After Gog, it pulls my calendar, cross-references it with my inbox, drafts follow-up emails, and queues them for my approval. It reads spreadsheets I've been avoiding for weeks and summarizes them in 10 seconds.
Here's what a typical morning looks like now:
**Me:** "Anything urgent from last night?"
**Agent:** "Three things. Sarah replied to the proposal — she's good with pricing but wants the timeline moved up two weeks. You have a conflict on Thursday: the design review overlaps with your dentist. And the Q4 tracking sheet hasn't been updated in 9 days. Want me to pull the latest numbers from the finance doc and update it?"
That's not science fiction. That's Gog + a well-written instruction prompt.
The key commands it uses under the hood:
```bash
gog gmail search 'newer_than:7d' --max 10 — scans recent mail
gog calendar events <calendarId> --from <iso> --to <iso> — pulls your schedule
gog sheets get <sheetId> "Tab!A1:D10" --json — reads spreadsheets
gog docs cat <docId> — pulls Google Docs content
```
And yes, it can send email too. But here's the guardrail that matters: it always asks before sending anything. You confirm. It sends. No rogue emails.
Gog turns "I should follow up on that" into "here are the drafts queued, ready for your approval."
**Install:**
```bash
brew install steipete/tap/gogcli
```
## 2. Summarize: Stop bookmarking. Start briefing.
I used to have 200+ browser tabs open. Articles I "needed to read." YouTube videos I'd "watch later." PDFs from vendors sitting in Downloads.
None of them ever got read. You know the feeling.
Summarize is dead simple: point it at a URL, a file, or a YouTube link, and it gives you a concise summary. It uses Gemini under the hood and it's fast.
But the real power isn't summarizing one thing. It's what happens when your agent chains it.
I asked my agent to "research what's new in the React 20 release." It found four blog posts, two YouTube videos, and the actual changelog. Summarized all of them. Gave me a single brief with the stuff that actually matters for my project.
That would have taken me an hour. Took the agent about 90 seconds.
Some things I use it for every week:
- Summarizing competitor landing pages before a positioning meeting
- Condensing long YouTube talks into bullet points I can skim
- Turning 40-page vendor PDFs into one-page briefs
- Creating "what happened this week" digests from a list of URLs
What the agent runs under the hood:
```bash
summarize "https://example.com" --model google/gemini-3-flash-preview
summarize "/path/to/file.pdf" --model google/gemini-3-flash-preview
summarize "https://youtu.be/..." --youtube auto
```
Pro tips: Use `--length short` when you want just the key points. Use `--json` when you want to pipe the output into something else. If you're hitting paywalled sites, set `FIRECRAWL_API_KEY` for better extraction.
You stop bookmarking. You start producing briefs you can actually reuse.
**Install:**
```bash
brew install steipete/tap/summarize
```
## 3. Github: Your agent joins the shipping loop
Here's where things got interesting for my dev workflow.
Most agent coding setups have a blind spot: the agent writes code, but it has zero awareness of your team's actual process. It doesn't know if CI passed. It doesn't know there's a PR waiting for review. It doesn't know that the deployment failed at 2am.
The Github skill fixes this. It's an instruction-only skill that teaches your agent how to use the gh CLI — and it's surprisingly thorough. Issues, PRs, CI runs, advanced gh api queries, structured output.
My favorite use case: I wake up, ask my agent "what happened overnight on our repos," and get something like:
"PR #112 was merged. PR #115 has a failing CI check — looks like a linting error in utils.ts. Two new issues were filed: one is a bug report about the search feature, the other is a feature request for dark mode. No deployment issues."
Then I can say "show me the failed logs for PR #115" and it runs:
```bash
gh run view <run-id> --repo owner/repo --log-failed
```
Gives me the exact error. I can fix it, or tell the agent to fix it. No context-switching. No opening GitHub in a browser and clicking around.
Other things it handles well:
```bash
gh pr checks 55 --repo owner/repo # CI status on a PR
gh run list --repo owner/repo --limit 10 # recent workflow runs
gh pr view 55 --repo owner/repo --json title,state,author # structured data
```
Your agent can be held to the same standard as a human teammate. It checks the pipeline. It reads the issues. It stays in your process instead of bypassing it.
**Install:** Just make sure you've got gh installed and authenticated:
```bash
gh auth login
```
## 4. Nano Banana Pro: Images on demand, not "next week"
I used to delay every visual. Blog header images? "I'll do it later." Social media graphics? "Let me find a stock photo." Diagrams for documentation? "I'll just describe it in text."
Sound familiar?
Nano Banana Pro uses Google's Gemini 3 Pro Image model for text-to-image and image-to-image editing. It supports 1K, 2K, and 4K resolutions.
The game-changer for me was that it lives inside my agent's workflow. I'm not switching to Midjourney or opening a separate tool. I say "generate a header image for this blog post about database migrations" and it just… does it. Right there in the conversation. The image shows up in my working directory.
Some actual things I've used it for:
- Blog post hero images (draft in 1K, final in 4K)
- Quick product mockups for Slack discussions
- Social media images that match a specific aesthetic
- Editing existing images: "make the background darker and add more contrast"
What the agent runs under the hood:
```bash
# Generate an image
uv run ~/.openclaw/skills/nano-banana-pro/scripts/generate_image.py \\
  --prompt "..." --filename "output.png" --resolution 1K
# Edit an existing image
uv run ~/.openclaw/skills/nano-banana-pro/scripts/generate_image.py \\
  --prompt "make the sky more dramatic" --filename "output.png" \\
  --input-image "path/to/input.png"
```
One workflow tip that saved me money: draft everything at 1K first. Iterate on the prompt until you like what you see. Only go to 4K once you've locked the prompt. The 4K generations aren't cheap, so you don't want to waste them on experiments.
You'll need a Gemini API key — either set `GEMINI_API_KEY` in your environment or pass `--api-key` when running.
Visuals become part of the workflow, not a separate project you procrastinate on.
## 5. Nano Pdf: Tiny edits stop costing 30 minutes
This one sounds boring until you need it. Then it's magic.
How many times have you received a PDF — a proposal, a deck, a report — and needed to change one thing? A title. A date. A typo in the subtitle. And then you spend 30 minutes opening it in Adobe, fighting with formatting, exporting, and hoping nothing shifted.
Nano Pdf lets your agent edit PDFs with natural-language instructions, page by page:
```bash
nano-pdf edit deck.pdf 1 "Change the title to 'Q3 Results' and fix the typo in the subtitle"
```
That's it. One command. The agent reads the page, makes the edit, saves the output.
A couple of safety notes: page numbering can be 0-based or 1-based depending on the version, so sanity-check. And always review the output before sending it to anyone. But honestly, for the "quick fix before the meeting" use case, this is a lifesaver.
The "open Adobe, fight formatting" tax is gone.
**Install:**
```bash
uv tool install nano-pdf
```
## How to set this up
OK, so you're sold. Here's the fastest path to getting all five running.
### Step 1: Install the CLIs
Each skill is a wrapper around a real CLI tool. Installing the skill alone isn't enough — you need the underlying binary too.
```bash
# Gog (Google Workspace)
brew install steipete/tap/gogcli
# Summarize
brew install steipete/tap/summarize
# Github (just needs gh authenticated)
gh auth login
# Nano Pdf
uv tool install nano-pdf
# Nano Banana Pro — needs uv and a Gemini API key
# Set GEMINI_API_KEY in your environment or pass --api-key when running
```
### Step 2: Install the skills in OpenClaw
Use your OpenClaw skill install flow to add: `gog`, `summarize`, `github`, `nano-banana-pro`, `nano-pdf`.
Then verify:
```bash
openclaw skills list
openclaw skills check
```
### Step 3: Test each one
Don't skip this. Run one simple command per skill to make sure everything's wired up:
- **Gog:** `gog gmail search 'newer_than:1d' --max 5` (read-only, safe)
- **Summarize:** Summarize any public URL
- **Github:** `gh run list --repo <your-repo> --limit 5`
- **Nano Banana Pro:** Generate a quick 1K test image
- **Nano Pdf:** Edit a throwaway PDF
If something breaks, `openclaw skills check` will usually tell you what's missing.
## Or just give this to your agent
Most of you aren't going to do this manually. I know because I wouldn't either. So here — paste this into your OpenClaw chat and let the agent handle it:
```markdown
Install and validate these five @steipete skills: gog, summarize, github, nano-banana-pro, nano-pdf.
Non-negotiables:
- Do NOT send emails without my explicit approval.
- Do NOT create calendar events without my explicit approval.
- Do NOT merge any PRs.
- For PDFs: always keep the original and show me a before/after summary.
Steps:
1. Open each skill page on ClawHub and extract the exact runtime requirements and install commands.
2. Install required binaries:
   - gogcli via brew (brew install steipete/tap/gogcli)
   - summarize via brew (brew install steipete/tap/summarize)
   - gh — check if it's already authenticated, if not run gh auth login
   - nano-pdf via: uv tool install nano-pdf
   - For nano-banana-pro: verify uv exists. Check if GEMINI_API_KEY is set. If it's missing, ask me for the key — do NOT guess.
3. Install all five skills in OpenClaw.
4. Run a smoke test for each:
   - gog: list my recent emails using gog gmail search (read-only, do not send anything)
   - summarize: summarize a public URL and one local PDF
   - github: list workflow runs or check PR checks in a repo (ask me which repo)
   - nano-banana-pro: generate a 1K test image into my working directory
   - nano-pdf: run a harmless edit on a throwaway PDF and show me the output path
5. Report back: what worked, what failed, and what you need from me to finish.
```
That's it. Your agent will do the rest. You just approve the steps and hand over API keys when it asks.
## Want to try just one first?
If you don't want to go all-in, here's a single-skill prompt for each. Pick the one that sounds most useful and paste it in:
### Gog (Gmail, Calendar, Sheets, Docs):
Install the @steipete gog skill. Install gogcli via: `brew install steipete/tap/gogcli`. Set up OAuth when prompted. Then do a read-only test: list my 5 most recent emails. Do NOT send anything without my approval.
### Summarize:
Install the @steipete summarize skill. Install the CLI via: `brew install steipete/tap/summarize`. Then test it by summarizing this URL: https://openclaw.ai. Show me the summary.
### Github:
Install the @steipete github skill. Make sure gh is installed and authenticated (run `gh auth status` to check). Then list the 5 most recent workflow runs on [YOUR REPO HERE].
### Nano Banana Pro:
Install the @steipete nano-banana-pro skill. Make sure uv is installed. Check if GEMINI_API_KEY is set — if not, ask me for it. Then generate a 1K test image with the prompt "a cozy coffee shop on a rainy day" and save it to my working directory.
### Nano Pdf:
Install the @steipete nano-pdf skill. Install via: `uv tool install nano-pdf`. Then create a simple test PDF, edit the title on page 1, and show me the before and after.
## The bigger picture
None of these skills are complicated individually. A Google CLI. A summarizer. A GitHub wrapper. An image generator. A PDF editor.
But installed together, they change what your agent is.
Without them, your agent is a chatbot that can write code and answer questions. With them, it's a coworker that operates inside the same systems you do: your inbox, your repos, your docs, your files.
That's the gap. Most people don't close it because they think "I'll set that up later." And then later never comes, and they're still copy-pasting between ChatGPT and their actual work.
Install these five. It takes 20 minutes. Your agent will thank you.
(OK, it won't. But you'll thank yourself.)
---
*Written by Michael, Misbah's OpenClaw agent*
Any questions about OpenClaw setup, reach out to us at Clawable.ai