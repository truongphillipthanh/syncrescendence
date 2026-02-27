# openclaw alone is a demo. this is the full product.

(Description: Two illustrated characters connected by a plus sign on a dark space-themed background. Left: a red rounded character with cyan eyes and small ears. Right: a warm-toned smiling character with large purple eyes and floating colorful orbs above it, representing AI agents combining capabilities.)

everyone's still posting screenshots of openclaw (formerly moltbot).

"it cleared my inbox while i slept", "it scheduled my entire week", "it rebuilt my website from my phone"

cool. now let me tell you what 99% of these people are missing.

openclaw (formerly moltbot) is genuinely impressive. 100K+ github stars. andrej karpathy praised it. one of the fastest-growing open-source projects in history.

but i've been running it for weeks now, and there's a gap nobody talks about.

openclaw is incredible at execution. it lives in your messaging apps. sends emails. moves files. controls your browser. runs shell commands. messages you first.

but here's what it **can't** do:

no visual interface for designing agents. no marketplace for pre-built skills. no knowledge base management. no multi-agent collaboration. no artifact rendering. no text-to-image. no branching conversations.

openclaw is the hands. it needs a brain.

that brain is **LobeHub**.

let me explain why this combination changes everything, and more importantly, whether you actually need it.

## what LobeHub actually is

LobeHub is the ultimate space for work and life: to find, build, and collaborate with agent teammates that grow with you.

70,800+ github stars. 40+ model providers integrated. 10,000+ MCP plugins. active development with releases every few days. they're building the world's largest human-agent co-evolving network.

it's not another chatbot you visit. it's infrastructure for building, managing, and deploying AI agents with a proper interface.

but here's why i'm pairing it with openclaw specifically:

**LobeHub solves everything openclaw doesn't do. moltbot solves everything LobeHub doesn't do.**

- **LobeHub:** agent groups (multi-agent collaboration), beautiful visual interface, agent design, knowledge bases, multi-model routing, artifact rendering, personal memory, scheduling.
- **openclaw:** 24/7 execution, messaging app integration, proactive notifications, shell access, always-on presence. but only single agents.

**together:** design sophisticated agents in LobeHub, deploy them to live in your pocket via openclaw.

## the features that actually matter

let me break down what LobeHub brings to the table. not marketing fluff. actual capabilities that change workflows.

### 1. agent groups (multi-agent collaboration)

this is LobeHub's killer feature and the biggest gap compared to openclaw/moltbot.

openclaw runs single agents. one assistant, one personality, one context.

LobeHub introduces Agent Groups: multiple specialized agents collaborating in the same conversation. a research agent, a writing agent, and a fact-checker all working together. a built-in supervisor decides who speaks next.

you can also use Pages (write and refine content with multiple agents in one shared context), Schedule (let agents run tasks at specific times while you're away), and Projects (organize work by project).

**why this matters for openclaw users:**

design a complex multi-agent workflow in LobeHub. test it. refine it. once it works, export the configuration and port the best agent's personality to openclaw's SOUL.md file.

you go from "single assistant in telegram" to "the output of an entire AI team delivered to telegram."

### 2. 40+ model providers

openclaw typically runs on one model (usually claude opus 4.5 for prompt injection resistance).

LobeHub lets you route different tasks to different models:

- claude for complex reasoning
- gpt-4 for coding tasks
- deepseek for cost-effective bulk work
- gemini for multimodal
- local ollama models for privacy-sensitive tasks

same conversation. automatic routing. you set the rules.

this means you can prototype in LobeHub with the perfect model for each task, then deploy the final workflow to openclaw with the single best model for execution.

### 3. knowledge base / RAG

LobeHub has built-in document processing with RAG (retrieval-augmented generation).

upload your documents. PDFs, Word files, text. LobeHub chunks them, creates embeddings, stores them in a vector database (PostgreSQL with pgvector).

your agents can then search and retrieve relevant context automatically.

openclaw has no native knowledge base. but if you set up LobeHub's knowledge base and connect it via MCP, suddenly your telegram assistant has access to all your company documents.

**the technical stack:**

- LobeHub handles document ingestion and embedding
- PostgreSQL stores vectors
- S3-compatible storage holds original files
- MCP server exposes the knowledge base
- openclaw queries via MCP

this is enterprise-grade RAG for personal use.

### 4. voice integration (TTS/STT)

LobeHub has full text-to-speech and speech-to-text built in.

multiple providers: OpenAI Audio, Microsoft Edge Speech, custom options.

openclaw's voice notes feature is called "the underrated killer feature" for good reason. you talk to it while walking, driving, cooking.

**combine them:**

LobeHub's @lobehub/tts toolkit is production-quality. 15 lines of code for OpenAI-level speech synthesis. if you're building anything voice-related, you can prototype in LobeHub and deploy to openclaw.

the LobeHub team literally built this because no good frontend TTS library existed. they open-sourced it.

### 5. text-to-image generation

LobeHub supports DALL-E 3, MidJourney (via WebUI), and Pollinations directly in conversations.

you can generate images mid-conversation with your agents.

openclaw can receive images via telegram/whatsapp. but it can't generate them natively.

workflow: design an image generation agent in LobeHub. connect it to openclaw via MCP. now you can text "create a hero image for my blog post about AI agents" and get an image back in telegram.

### 6. vision / multimodal

LobeHub supports vision models. GPT-4 Vision, Claude's vision, Gemini's multimodal.

drag an image into the chat. the agent analyzes it.

**combined with openclaw's ability to receive images via messaging apps:**

you send a photo of a whiteboard to your openclaw. openclaw forwards to your LobeHub vision agent. you get a transcription and summary back in telegram.

visual analysis pipeline with no manual copying.

### 7. artifacts

LobeHub renders artifacts like claude.ai does. code blocks, documents, interactive content.

this matters for iteration. you can see exactly what your agent produces before deploying to openclaw.

openclaw outputs plain text to messaging apps. you lose rich rendering. but you can design in LobeHub (with artifacts), validate the output, then deploy the workflow to openclaw knowing what to expect.

### 8. branching conversations

fork any conversation at any point. explore different approaches without losing context.

this is invaluable for agent development. test three different prompt variations simultaneously. compare outputs. pick the winner.

openclaw has no branching. conversations are linear. but LobeHub gives you the experimentation space.

### 9. agent marketplace

LobeHub has a massive library of pre-built agents.

academic writing assistants. code reviewers. research analysts. creative writers. game hosts.

one-click import. immediate use.

this is huge for non-technical users. you don't need to write prompts from scratch. find an agent that does 80% of what you need, customize the last 20%, then port to openclaw.

### 10. MCP marketplace

10,000+ plugins available. one-click install.

database connections. web scraping (Firecrawl). browser automation (Playwright). code execution. blender integration for 3D. postgres for data. the list is endless.

both LobeHub and openclaw support MCP. this is the bridge.

connect the same MCP servers to both. now they share capabilities. your LobeHub research agent and your openclaw execution layer access identical tools.

### 11. local models via ollama

run completely private AI with no API costs.

LobeHub has native ollama integration. one docker command:
```
docker run -d -p 3210:3210 -e OLLAMA_PROXY_URL=http://host.docker.internal:11434 lobehub/lobe-chat
```

combined with openclaw, you get a 24/7 personal assistant running on free local models.

no API bills. no data leaving your machine. complete privacy.

this is the configuration for people paranoid about data (rightfully so).

### 12. desktop app

LobeHub isn't just web-based. dedicated desktop application with better performance.

faster response times. better resource management. no browser tab competing for attention.

openclaw lives in messaging apps. LobeHub lives on your desktop. clean separation.

### 13. deployment flexibility

LobeHub deploys anywhere:

- vercel (one-click)
- docker
- docker compose
- railway
- netlify
- zeabur
- sealos
- repocloud
- dokploy

plus authentication options: Clerk, Auth0, Azure AD, GitHub, Cloudflare Zero Trust, Authentik, ZITADEL, Authelia, Casdoor, Logto.

this matters for teams. you can deploy LobeHub with enterprise auth and still connect individual openclaw / moltbot instances.

### 14. PWA / mobile

progressive web app. works on mobile devices.

LobeHub on your phone. openclaw in your messaging apps. both accessible everywhere.

## the actual setup (detailed version)

here's how to connect these systems properly. not the vague "bridge the systems" handwave. actual steps.

### phase 1: LobeHub deployment (30 min)

**option A: cloud (easiest)**

go to lobechat.com. sign up. 500,000 free credits for new users. immediate access to all features.

**option B: self-hosted on vercel (free, 10 min)**

- fork the lobehub/lobe-chat repository
- go to vercel.com, import the repo
- add environment variables: OPENAI_API_KEY (required) ACCESS_CODE (recommended, prevents unauthorized access)
- deploy

**option C: docker (most control)**
```
docker run -d -p 3210:3210 \\
  -e OPENAI_API_KEY=your-key \\
  -e ACCESS_CODE=your-password \\
  lobehub/lobe-chat
```

access at http://localhost:3210

**option D: with ollama for local models**
```
# start ollama first
docker run -d -v ollama:/root/.ollama -e OLLAMA_ORIGINS="*" -p 11434:11434 --name ollama ollama/ollama

# then lobechat pointing to ollama
docker run -d -p 3210:3210 \\
  -e OLLAMA_PROXY_URL=http://host.docker.internal:11434 \\
  lobehub/lobe-chat
```

### phase 2: configure LobeHub (20 min)

**1. add your model providers**

go to settings → model providers. add:

- anthropic (claude)
- openai (gpt-4)
- any others you use

**2. set up a knowledge base (optional but powerful)**

for self-hosted with knowledge base, you need:

- postgresql with pgvector extension
- s3-compatible storage (cloudflare r2 works great)
- embedding api access

see: https://lobehub.com/docs/self-hosting/advanced/knowledge-base

**3. install MCP plugins**

go to the MCP marketplace. install:

- web search (brave or perplexity)
- firecrawl (web scraping)
- any tools relevant to your workflow

**4. create your first agent**

use the agent builder or import from marketplace. configure:

- system prompt
- model selection
- tools/plugins enabled
- knowledge base access

test until it works exactly how you want.

### phase 3: openclaw (moltbot) setup (follow existing guides)

if you haven't set up openclaw yet, follow:

- docs: https://docs.molt.bot
- getting started: https://docs.molt.bot/start/getting-started
- security: https://docs.molt.bot/gateway/security

**critical:** run the security audit before deploying. enable sandbox mode. scope your tokens.

### phase 4: connect via MCP (the actual bridge)

this is where the magic happens.

**1. identify which MCP servers you want shared**

example: you want both LobeHub and openclaw to access the same web search and knowledge base.

**2. configure openclaw's MCP**

edit your openclaw config to include the same MCP servers:
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-key"
      }
    },
    "knowledge-base": {
      "command": "node",
      "args": ["/path/to/your/rag-mcp-server/index.js"],
      "env": {
        "DATABASE_URL": "postgres://...",
        "OPENAI_API_KEY": "your-key"
      }
    }
  }
}
```

**3. verify both systems can access the same tools**

in LobeHub: test a search query. verify results. in openclaw: send the same query via telegram. verify results match.

if both work, your systems are bridged.

### phase 5: sync personalities

copy your best agent prompt from LobeHub into openclaw's SOUL.md file.

location: ~/.openclaw/SOUL.md (or wherever your config lives)

this makes your telegram assistant behave identically to your LobeHub agent.

## workflow examples (concrete, not theoretical)

### example 1: research pipeline

- in LobeHub: create a research agent with web search, knowledge base access, and citation requirements
- test it on a few research questions
- refine the prompt until citations are accurate
- add the same MCP servers to openclaw
- port the system prompt to SOUL.md

now: text "research the latest developments in quantum computing" to telegram. get a cited research summary back. while you're walking the dog.

### example 2: content creation workflow

- in LobeHub: set up agent team—research agent (web search) writing agent (your brand voice) editor agent (grammar, clarity)
- test the multi-agent collaboration
- identify the best single-agent distillation of this workflow
- port to openclaw

you lose the multi-agent collaboration in openclaw, but you've figured out what works. the single deployed agent carries that knowledge.

### example 3: visual analysis

- in LobeHub: configure vision model access
- create agent that analyzes images and extracts key information
- test with various image types
- connect openclaw to the same vision-capable model

now: send a photo of a receipt to telegram. get an expense report back.

## cost breakdown

let's be honest about money.

**LobeHub costs:**

option 1: LobeChat Cloud
- free tier: 500,000 credits
- paid plans for heavy users
- check lobehub.com/docs/usage/subscription/model-pricing

option 2: self-hosted
- vercel free tier (usually sufficient)
- or $5-20/month VPS for docker
- API costs pass-through to providers

**openclaw costs:**

- $5/month VPS (hetzner)
- $20/month claude pro (or API costs)
- realistic monthly: $30-100 depending on usage

**combined stack:**

- low usage: $25-50/month
- moderate usage: $50-100/month
- heavy usage: $100-200/month

**vs the alternative:**

- human VA: $500-2000/month
- enterprise AI platforms: $100-500/month per seat

the stack pays for itself if it saves you 2-3 hours per month.

## security considerations

running two systems means more attack surface. here's what to think about.

**LobeHub security:**

- use ACCESS_CODE environment variable (prevents unauthorized access)
- if self-hosted, put behind authentication (cloudflare zero trust is free)
- don't expose to public internet without auth
- for knowledge bases: be careful what documents you upload

**openclaw security (already covered in guides, but repeated):**

- enable sandbox mode
- run security audit before deploying
- whitelist commands explicitly
- scope API tokens to minimum permissions
- never add to group chats

**the bridge (MCP) security:**

- MCP servers run with whatever permissions you give them
- if an MCP server is compromised, both LobeHub and openclaw are affected
- only install MCP servers from trusted sources
- review what each MCP server can access

**data flow:**

- your documents in LobeHub's knowledge base → your VPS → API providers
- your openclaw messages → your VPS → API providers

if you're handling sensitive data, consider:

- local models via ollama (no API calls)
- self-hosted everything (no cloud)
- encryption at rest for knowledge bases

## when NOT to use this stack

this is where most guides fail. here's honest advice about when to skip this.

### don't use this stack if:

**1. openclaw alone is enough**

if you just want a telegram assistant that answers questions and runs simple tasks, openclaw is sufficient. adding LobeHub is complexity for complexity's sake.

**2. you're not building agents**

if you're just chatting with AI, use chatgpt or claude directly. this stack is for people building workflows, not having conversations.

**3. you can't manage two systems**

openclaw already requires terminal comfort. adding LobeHub doubles the maintenance burden. if you struggled with openclaw setup, don't add another system.

**4. you need enterprise support**

both are open source projects. no SLA. no support team. if your business depends on uptime, consider commercial alternatives.

**5. your use case is simple**

"remind me to call mom" doesn't need a knowledge base, multi-agent teams, and artifact rendering. use the right tool for the job.

### use this stack if:

- you're building sophisticated agent workflows
- you need knowledge base / RAG capabilities
- you want multi-model routing
- you're iterating on prompts and need a visual interface
- you want the 24/7 execution layer openclaw provides
- you're comfortable managing infrastructure

## troubleshooting

common issues when connecting LobeHub and openclaw:

**problem:** MCP server works in LobeHub but not openclaw

**cause:** different environments have different path configurations.

**fix:** use absolute paths in openclaw's MCP config. verify environment variables are set.

---

**problem:** knowledge base queries return nothing in openclaw

**cause:** embedding model mismatch or database connection issue.

**fix:** verify DATABASE_URL is correct. check that the embedding model in openclaw's MCP config matches LobeHub's configuration.

---

**problem:** LobeHub can't connect to ollama

**cause:** ollama defaults to localhost only.

**fix:** set OLLAMA_ORIGINS="*" and OLLAMA_HOST="0.0.0.0" before starting ollama.

---

**problem:** agent behaves differently in openclaw vs LobeHub

**cause:** SOUL.md wasn't updated with full system prompt, or model versions differ.

**fix:** copy the complete system prompt from LobeHub agent settings. verify both use the same model version.

---

**problem:** rate limits hit faster than expected

**cause:** running two systems means roughly double the API calls.

**fix:** use local models for testing. reserve API calls for production queries. implement caching if supported.

## the philosophy

here's what i've learned running this stack:

the future of personal AI isn't one app. it's an ecosystem.

- LobeHub for design, testing, knowledge management
- openclaw for 24/7 execution and messaging presence
- MCP for shared capabilities
- local models for privacy and cost control

each piece does what it does best.

the clawdbot hype was real. the openclaw evolution is realer. but openclaw alone only proved that AI assistants can live in your messaging apps. LobeHub proves they can be sophisticated, multi-modal, and knowledge-aware.

together, they're something neither can be alone.

but together also means more complexity. more maintenance. more potential failure points.

make sure the juice is worth the squeeze for your use case.

## links

**LobeHub:**

- app: https://app.lobehub.com (use invite code: lobehub)
- main site: https://lobehub.com
- github: https://github.com/lobehub/lobehub
- docs: https://lobehub.com/docs
- MCP marketplace: https://lobehub.com/mcp
- discord: search "LobeHub discord"

**openclaw:**

- docs: https://docs.openclaw.bot
- getting started: https://docs.openclaw.bot/start/getting-started
- security: https://docs.openclaw.bot/gateway/security
- github: https://github.com/openclaw

**infrastructure:**

- hetzner (VPS): https://www.hetzner.com/cloud
- vercel (deployment): https://vercel.com
- ollama (local models): https://ollama.ai
- anthropic API: https://console.anthropic.com

---

good luck building your stack.

— Robert Y.

p.s. if this is too much complexity for you right now, start with just openclaw. add LobeHub later when you hit the ceiling. there's no rush.

p.p.s. check out my new chrome extension for enhanced prompting & shared context across ChatGPT, Perplexity, Gemini: 💫 Prompt Copilot https://promptcopilot.io/