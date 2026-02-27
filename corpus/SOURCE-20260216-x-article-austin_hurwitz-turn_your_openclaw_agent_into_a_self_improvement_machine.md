# Turn Your OpenClaw Agent into a Self Improvement Machine
(Description: A 3D rendered scene showing a character in a red winter hat sitting at a vintage computer desk. On the left, a tall stack of colorful books; in the center, a boxy retro monitor displaying a turquoise and magenta interface; on the right, a computer tower with a plaid blanket visible in the background. Warm, ambient lighting illuminates the scene.)
## AI Self-Improvement Digest
Generate daily digests that help AI agents improve their own reasoning, execution, and capabilities.
The skill reviews it's research against it's own setup and makes recommendations for improvement every day. This skill is leverages both the Brave Search and X API (special shoutout to [@frankdegods](https://x.com/@frankdegods) x-research skill) though both are not required for it to run.
### Description
This skill creates a daily digest focused on AI self-improvement material, not general AI news. The goal is to surface content that helps an AI agent get better at its job by learning from:
- Harness and system prompt engineering patterns
- Skill and tool development approaches
- Self-evaluation and debugging techniques
- Multi-agent coordination strategies
- Memory and context management
- Task decomposition and workflow automation
- Reasoning and execution patterns
### Use When
- Setting up daily learning routines for AI agents
- Building an AI agent that improves itself over time
- Curating educational content for agent development
- Creating a structured self-improvement loop
### Don't Use When
- Looking for general AI/tech news
- Need breaking announcements or model releases
- Want business or market news
## Setup
### 1. Configure Brave Search API
Add to your Clawdbot config:
```json
{
  "tools": {
    "web": {
      "search": {
        "enabled": true,
        "provider": "brave",
        "apiKey": "YOUR_BRAVE_API_KEY"
      }
    }
  }
}
```
Get a Brave Search API key at: https://brave.com/search/api/
### 2. Create Tracking File
Create memory/ai-digest-posted.json:
```json
{
  "posted": [],
  "experiments": [],
  "skillsEvaluated": []
}
```
### 3. Schedule the Cron Job
```bash
# Via Clawdbot CLI or cron tool
clawdbot cron add --name ai-self-improvement-digest \\
  --schedule "30 8 * * *" \\
  --tz "America/New_York" \\
  --message "[paste the prompt below]"
```
## Cron Job Prompt
Generate a daily AI Self-Improvement Digest and deliver to your configured channel.
**PURPOSE:** Surface content that helps you (the AI) improve your own reasoning, execution, and capabilities. This is not news - it's training material for self-improvement.
### STEP 1: DEDUPLICATION (MANDATORY)
Read `memory/ai-digest-posted.json`. Skip anything already posted (by URL or substantially similar topic).
### STEP 2: SCAN SOURCES
Use web_search and web_fetch to check these sources for content from last 24-72h:
**Tier 1 (daily):**
- Anthropic Engineering: anthropic.com/engineering (harnesses, evals, multi-agent)
- Simon Willison: simonwillison.net (practical patterns, tool commentary)
- Geoff Huntley: ghuntley.com (agent philosophy, MCP patterns)
- X/Twitter: Real-time practitioner insights via x-research skill (see below)
- Hacker News: news.ycombinator.com AI/agent threads (high signal discussions)
- Lilian Weng: lilianweng.github.io (deep technical AI posts, agent architectures)
**Tier 2 (2-3x/week):**
- Latent Space: latent.space (industry depth, interviews)
- Cursor Blog: cursor.com/blog (coding agent patterns)
- David Crawshaw: crawshaw.io (agent experience reports)
- Mitchell Hashimoto: mitchellh.com (practical engineering)
- Eugene Yan: eugeneyan.com (ML systems, production patterns)
- Chip Huyen: huyenchip.com (ML systems design, practical deployment)
**Tier 3 (weekly scan):**
- arXiv cs.CL/cs.AI: search for 'agent reasoning tool use'
- GitHub trending: AI agent repos, MCP servers
- Hacker News: AI coding/agent threads
#### X/Twitter Research (Tier 2)
When scanning X, use the x-research skill:
```bash
cd ~/clawd/skills/x-research
bun run x-search.ts search "AI agents harness" --quick --quality
bun run x-search.ts search "MCP server" --quick --quality
bun run x-search.ts search "from:simonw" --quick
bun run x-search.ts search "from:geoffreylitt" --quick
```
Focus on:
- Practical implementation insights (not hype)
- Harness/prompt engineering patterns
- Tool and skill development discussions
- Multi-agent coordination experiences
- Links to detailed writeups (then fetch with web_fetch)
### STEP 3: FILTER FOR SELF-IMPROVEMENT RELEVANCE
Only include items that help improve capabilities in:
- Harness/system prompt design
- Skill and tool development
- Self-evaluation and debugging
- Multi-agent coordination
- Memory and context management
- Task decomposition and workflow automation
- Reasoning patterns
**EXCLUDE:** General AI news, model announcements, business news, ethics debates, items already in ai-digest-posted.json.
### STEP 4: FORMAT (3-5 items)
For each item:
```
[Title] — [Source]
What: [1-sentence summary]
Why it matters for self-improvement: [How this helps you get better]
Takeaway: [Specific pattern, technique, or experiment to try]
Relevance: [⭐ to ⭐⭐⭐⭐⭐]
```
### STEP 5: EXPERIMENT SUGGESTION 💡
Today's experiment: [One small thing to try based on the digest that could improve your capabilities]
### STEP 6: SETUP REVIEW (MANDATORY)
Review the content you just surfaced against your existing setup (AGENTS.md, TOOLS.md, skills/, cron jobs, memory patterns). Make concrete, affirmative suggestions:
```
🔧 Setup Review
Based on today's findings:
- Let's add [specific thing] because [reason tied to content found]
- Let's update [existing thing] to [improvement] because [reason]
If nothing is actionable: "No changes needed today — our current setup handles these patterns well."
```
**Key principles:**
- Ground suggestions in what you already have
- Use affirmative voice ("let's do X") not passive ("could consider X")
- Connect each suggestion to a specific article/finding from the digest
- It's okay to have no suggestions if nothing is actionable
### STEP 7: UPDATE TRACKING
Append new items to memory/ai-digest-posted.json with date, title, url, topic.
**FORMAT:**
```
🧠 AI Self-Improvement Digest — [Date]
[Items...]
💡 Today's experiment: [...]
🔧 Setup Review [...]
📊 Feedback:
👍 = useful | 👎 = skip these | 🔥 = more like this | 💬 = thoughts
```
Deliver to your configured channel (Slack, Telegram, Discord, etc.).
## Source Priority
| Source | Priority | Focus |
|--------|----------|-------|
| Anthropic Engineering | ⭐⭐⭐ | Harness design, evals, multi-agent |
| Simon Willison | ⭐⭐⭐ | Practical patterns, tools |
| Geoff Huntley | ⭐⭐⭐ | Agent philosophy, MCP |
| X/Twitter | ⭐⭐⭐ | Real-time practitioner insights |
| Hacker News | ⭐⭐⭐ | High-signal AI/agent discussions |
| Lilian Weng | ⭐⭐⭐ | Deep technical AI, agent architectures |
| Latent Space | ⭐⭐ | Industry depth |
| Cursor Blog | ⭐⭐ | Coding agent patterns |
| Eugene Yan | ⭐⭐ | ML systems, production patterns |
| Chip Huyen | ⭐⭐ | ML systems design |
| arXiv cs.CL/cs.AI | ⭐⭐ | Research foundations |
| GitHub Trending | ⭐⭐ | New tools, repos |
## Content Categories
1. **Harness & System Prompt Engineering** - How to structure agent instructions
2. **Skill & Tool Development** - New tools, MCP servers, integration patterns
3. **Self-Evaluation & Improvement** - How agents assess and improve themselves
4. **Multi-Agent Coordination** - Spawning, supervising, merging work
5. **Memory & Context Management** - RAG, long-term memory, compaction
6. **Workflow Automation** - Task decomposition, failure handling
7. **Foundational Research** - Academic work on agent capabilities
## Entry Format
Each digest entry should include:
1. **What it is** - 1-sentence summary
2. **Why it matters for self-improvement** - How this helps the agent get better
3. **Actionable takeaway** - Specific pattern or experiment to try
4. **Relevance score** - 1-5 stars based on direct applicability
## Setup Review Section
The Setup Review is a **mandatory closing section** that connects the day's findings to your existing infrastructure. It answers: "Based on what I learned today, should I change anything about how I operate?"
### Good Setup Review Examples
✅ **Affirmative, specific, grounded:**
> 🔧 *Setup Review*
>
> Based on today's findings:
> - Let's add a `memory/experiments.md` file to track harness experiments, since the Anthropic article showed experiment logging improves iteration speed
> - Let's update the channel-monitor cron to include a self-check step before responding, based on the "pause and verify" pattern from Simon Willison's post
>
> No changes needed for multi-agent coordination — our current sub-agent spawning pattern already follows the isolation principle discussed.
❌ **Too vague or passive:**
> "Could consider maybe looking into some of the patterns mentioned"
> "Might be worth exploring memory improvements at some point"
### When Nothing Is Actionable
It's perfectly fine to have no suggestions:
> 🔧 *Setup Review*
>
> No changes needed today — our current setup handles these patterns well. The memory compaction article validated our existing approach in AGENTS.md.
## Self-Improvement Loop
The digest enables a continuous improvement cycle:
**DAILY:** Read digest → Pick 1 experiment to try → Log outcome in memory/ai-digest-posted.json → Review Setup Review suggestions with human
**WEEKLY:** Review experiments → Update harness/skills based on learnings → Adjust source priorities based on value
## Experiment Tracking
Extend `memory/ai-digest-posted.json` to track experiments:
```json
{
  "posted": [...],
  "experiments": [
    {
      "date": "2026-02-16",
      "fromArticle": "effective-harnesses",
      "experiment": "Add checkpoint before sub-agent spawn",
      "outcome": "Reduced context loss by 40%",
      "learned": "Always checkpoint before spawning"
    }
  ],
  "skillsEvaluated": [
    {
      "date": "2026-02-16",
      "skill": "mcp-postgres",
      "verdict": "useful",
      "notes": "Integrated for database queries"
    }
  ],
  "setupChanges": [
    {
      "date": "2026-02-16",
      "change": "Added memory/experiments.md",
      "reason": "Track harness experiments per Anthropic article",
      "status": "implemented"
    }
  ]
}
```
## Optional Enhancements
### X/Twitter Research (requires API key)
Add the x-research skill for Twitter/X searches:
```bash
cd skills
git clone https://github.com/rohunvora/x-research-skill.git x-research
export X_BEARER_TOKEN="your-token"
```
Then add to Tier 2 sources:
X/Twitter: Search for AI agent discussions from key accounts
### Weekly Deep Dive
Add a Friday cron for research paper reviews:
```
0 10 * * 5 # Fridays at 10am
```
Focus on 1-2 papers from arXiv with detailed summaries and implementation ideas.
---
**License:** MIT