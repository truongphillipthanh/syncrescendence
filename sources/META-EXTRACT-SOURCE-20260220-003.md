# Extraction: SOURCE-20260220-003

**Source**: `SOURCE-20260220-x-article-misbahsy-youre_behind_if_youre_not_using_these_5_openclaw_skills.md`
**Atoms extracted**: 36
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (8)

### ATOM-SOURCE-20260220-003-0001
**Lines**: 4-12
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Most people use OpenClaw like a chat toy, asking questions and generating code, while those gaining significant leverage use it to hand off entire workflows.

### ATOM-SOURCE-20260220-003-0002
**Lines**: 13-14
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> The difference in leveraging AI agents for workflows versus simple queries is not the underlying model, but the specific skills installed.

### ATOM-SOURCE-20260220-003-0012
**Lines**: 93-97
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> Integrating image generation directly into an agent's workflow, rather than using separate tools like Midjourney, significantly streamlines the creative process.

### ATOM-SOURCE-20260220-003-0018
**Lines**: 123-124
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Integrating visual creation into the workflow prevents procrastination on visual tasks.

### ATOM-SOURCE-20260220-003-0022
**Lines**: 142-143
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Using Nano Pdf eliminates the time-consuming process of manually editing PDFs with traditional software like Adobe.

### ATOM-SOURCE-20260220-003-0033
**Lines**: 193-193
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Individually, skills like a Google CLI, summarizer, GitHub wrapper, image generator, or PDF editor are not complicated.

### ATOM-SOURCE-20260220-003-0034
**Lines**: 195-196
**Context**: hypothesis / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> Installing these skills together transforms an agent from a chatbot that writes code and answers questions into a coworker that operates within existing systems like inboxes, repositories, documents, and files.

### ATOM-SOURCE-20260220-003-0035
**Lines**: 198-198
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.60, actionability=0.50, epistemic_stability=0.70

> Many people fail to integrate these tools, thinking they will set them up later, leading to continued manual copy-pasting between AI tools and their work.

## Concept (4)

### ATOM-SOURCE-20260220-003-0004
**Lines**: 34-38
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> Gog is a Google Workspace CLI that allows an AI agent to interact with Gmail, Calendar, Drive, Contacts, Sheets, and Docs, enabling the agent to perform tasks directly within these applications after OAuth setup.

### ATOM-SOURCE-20260220-003-0008
**Lines**: 63-70
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> Summarize is an OpenClaw skill that provides concise summaries of web pages, PDFs, and YouTube videos using Gemini, and its power is amplified when an AI agent chains multiple summaries for comprehensive briefings.

### ATOM-SOURCE-20260220-003-0011
**Lines**: 90-92
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Nano Banana Pro is a tool that integrates Google's Gemini 3 Pro Image model for text-to-image and image-to-image editing, supporting 1K, 2K, and 4K resolutions.

### ATOM-SOURCE-20260220-003-0019
**Lines**: 132-133
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Nano Pdf is a tool that enables agents to edit PDFs using natural-language instructions, page by page.

## Framework (1)

### ATOM-SOURCE-20260220-003-0003
**Lines**: 15-29
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Five OpenClaw skills by Peter Steinberger (@steipete) are identified as transformative for agent capabilities: Gog (Google Workspace), Summarize (web pages, PDFs, YouTube), Github (issues, PRs, CI), Nano Banana Pro (image generation via Gemini 3 Pro), and Nano Pdf (PDF editing).

## Praxis Hook (23)

### ATOM-SOURCE-20260220-003-0005
**Lines**: 34-59
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To enable an AI agent to manage Google Workspace tasks, install Gog (e.g., `brew install steipete/tap/gogcli`) and configure OAuth, allowing the agent to access and manipulate data in Gmail, Calendar, Sheets, and Docs.

### ATOM-SOURCE-20260220-003-0006
**Lines**: 50-55
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Use Gog commands like `gog gmail search`, `gog calendar events`, `gog sheets get`, and `gog docs cat` to allow an AI agent to scan emails, pull schedules, read spreadsheets, and access Google Docs content.

### ATOM-SOURCE-20260220-003-0007
**Lines**: 56-58
**Context**: method / limitation
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When using an AI agent with Gog to send emails, implement a guardrail where the agent always asks for approval before sending, preventing unauthorized communications.

### ATOM-SOURCE-20260220-003-0009
**Lines**: 79-82
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To install Nano Banana Pro, ensure `gh` is installed and authenticated by running `gh auth login`.

### ATOM-SOURCE-20260220-003-0010
**Lines**: 80-84
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To summarize content, use the `summarize` command with a URL, file path, or YouTube link, optionally specifying `--length short` for key points, `--json` for programmatic output, or `FIRECRAWL_API_KEY` for paywalled sites.

### ATOM-SOURCE-20260220-003-0013
**Lines**: 99-105
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Nano Banana Pro can be used for generating blog post hero images (drafting in 1K, finalizing in 4K), quick product mockups, social media images matching specific aesthetics, and editing existing images (e.g., 'make the background darker and add more contrast').

### ATOM-SOURCE-20260220-003-0014
**Lines**: 108-110
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To generate an image using Nano Banana Pro, run `uv run ~/.openclaw/skills/nano-banana-pro/scripts/generate_image.py --prompt "..." --filename "output.png" --resolution 1K`.

### ATOM-SOURCE-20260220-003-0015
**Lines**: 111-114
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To edit an existing image with Nano Banana Pro, use `uv run ~/.openclaw/skills/nano-banana-pro/scripts/generate_image.py --prompt "make the sky more dramatic" --filename "output.png" --input-image "path/to/input.png"`.

### ATOM-SOURCE-20260220-003-0016
**Lines**: 115-119
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To save costs when using Nano Banana Pro, draft images at 1K resolution and iterate on the prompt until satisfied before generating the final 4K version, as 4K generations are more expensive.

### ATOM-SOURCE-20260220-003-0017
**Lines**: 120-122
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Nano Banana Pro requires a Gemini API key, which can be set as an environment variable `GEMINI_API_KEY` or passed via the `--api-key` argument.

### ATOM-SOURCE-20260220-003-0020
**Lines**: 134-136
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To edit a PDF with Nano Pdf, use a command like `nano-pdf edit deck.pdf 1 "Change the title to 'Q3 Results' and fix the typo in the subtitle"`.

### ATOM-SOURCE-20260220-003-0021
**Lines**: 139-141
**Context**: method / limitation
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When using Nano Pdf, always sanity-check page numbering (0-based or 1-based) and review the output before sharing.

### ATOM-SOURCE-20260220-003-0023
**Lines**: 145-147
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To install Nano Pdf, use the command `uv tool install nano-pdf`.

### ATOM-SOURCE-20260220-003-0024
**Lines**: 152-161
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up OpenClaw skills, first install the underlying CLI tools: `gogcli` via `brew install steipete/tap/gogcli`, `summarize` via `brew install steipete/tap/summarize`, `gh` (authenticated), `nano-pdf` via `uv tool install nano-pdf`, and ensure `uv` and a `GEMINI_API_KEY` are available for Nano Banana Pro.

### ATOM-SOURCE-20260220-003-0025
**Lines**: 163-166
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> After installing CLI tools, install the skills (`gog`, `summarize`, `github`, `nano-banana-pro`, `nano-pdf`) in OpenClaw and verify with `openclaw skills list` and `openclaw skills check`.

### ATOM-SOURCE-20260220-003-0026
**Lines**: 168-174
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Test each OpenClaw skill after installation: `gog gmail search 'newer_than:1d' --max 5` for Gog, summarize a public URL for Summarize, `gh run list --repo <your-repo> --limit 5` for Github, generate a 1K test image for Nano Banana Pro, and edit a throwaway PDF for Nano Pdf.

### ATOM-SOURCE-20260220-003-0027
**Lines**: 175-176
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> If an OpenClaw skill breaks during testing, `openclaw skills check` can help identify missing components.

### ATOM-SOURCE-20260220-003-0028
**Lines**: 179-190
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.70

> An OpenClaw agent can automate the installation and validation of skills by providing it with a detailed prompt outlining steps, non-negotiables (e.g., 'Do NOT send emails without my explicit approval'), and specific test commands for each skill.

### ATOM-SOURCE-20260220-003-0029
**Lines**: 184-184
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To install the @steipete summarize skill, install the CLI via: `brew install steipete/tap/summarize`.

### ATOM-SOURCE-20260220-003-0030
**Lines**: 186-186
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To install the @steipete github skill, ensure `gh` is installed and authenticated by running `gh auth status`.

### ATOM-SOURCE-20260220-003-0031
**Lines**: 188-188
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To install the @steipete nano-banana-pro skill, ensure `uv` is installed and check if `GEMINI_API_KEY` is set.

### ATOM-SOURCE-20260220-003-0032
**Lines**: 190-190
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To install the @steipete nano-pdf skill, install it via: `uv tool install nano-pdf`.

### ATOM-SOURCE-20260220-003-0036
**Lines**: 199-199
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.80

> Install these five skills, as it takes only 20 minutes, and it will improve your workflow.
