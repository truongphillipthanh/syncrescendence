# A Guide to Building Brands for Humans & Agents
(Description: A large infographic divided into two columns labeled "Human" and "Agent". The left side shows traditional brand materials including website screenshots, PDFs, and design guideline documents arranged in an overlapping layout. The right side displays structured data files with green syntax highlighting, representing YAML and JSON code blocks.)
## The New Workflow
Yesterday, [Figma introduced Claude Code integration](https://x.com/figma/status/2023759565029003769), where code flows to Figma and back again in a continuous loop. This is important because the loop works both ways; your team creates in Claude Code using your structured brand files, sends it to Figma, your designer refines it on the canvas, then brings it back to code with Figma MCP.
Certain files (like `brand-positioning.yaml` and `messaging-framework.md`) serve as the single source of truth for both sides—the agent reads them when generating code, and the designer references them when refining in Figma. They both employ the same positioning, same voice, and same structure.
However, this only works if your brand has **structured data**, not just Figma files.
At [Little Plains](https://www.littleplains.co), we've been preparing for this over the past few months. We've been slowly shifting from just delivering brand guidelines to delivering **brand infrastructure**. I think it's cool and hopefully this is helpful.
Here's how we're approaching this:
## Brand Infrastructure
We've been working on producing two layers for each brand:
- **Human deliverables**
- **Agent deliverables**
It's less about replacing one with the other, and more about giving teams what they need, however they're working. Your designer needs Figma files and your agent needs structured data, and both need the same positioning, voice, and structure.
Let's review each:
### First: The Human-Facing System
This is the craft: visual identity, typography, motion, website, narrative, and guidelines. PDFs, Figma files, design systems; this is what people see and feel. This is what we're 'used to' delivering, and receiving.
(Description: A screenshot showing a bird's eye view of a traditional brand and digital guideline document with multiple pages displayed in a grid layout, showing various design systems, typography, colors, and UI components.)
### Second: The Agent-Readable System
This is the structure. Markdown, YAML, and JSON files that define positioning, voice, differentiation. It's for your team to actually use when they're working with agents (which increasingly, we all are).
We call it an **Agent-First Brand Kit**, a structured knowledge system where every piece of brand guidance lives in a *chunk* (one of my favorite words ever), approximately 400 tokens each, with metadata that agents can parse and humans can read.
Here's a selection of what we're giving select clients, using the same example ([Baba Care](https://callbaba.com/)) as above:
#### Brand Positioning
```yaml
chunk_id: "positioning-core"
domain: "positioning"
category: "positioning"
subcategory: "foundation"
context_tags:
  - "value-proposition"
  - "positioning-statement"
  - "what-baba-is"
  - "market-category"
depends_on: []
token_count: 380
format: "yaml"
version: "1.0"
last_updated: "2026-02-17"
status: "active"
summary: >
  Core positioning and value proposition. Baba as emotionally intelligent AI 
  sidekick for companionship and cognitive health. Includes vision, mission, 
  and positioning statement.
company:
  name: "Baba"
  url: "baba.ai"
  tagline: "A caring AI sidekick that improves the lives of people seeking to be less alone."
  category: "AI companionship and cognitive health"
  vision: "To redefine what it means to live well and thrive through technology that listens, learns, and cares."
  mission: "To ease the weight of loneliness through companionship and support."
  value_proposition: >
    Baba is a caring AI sidekick that improves the lives of people seeking to be 
    less alone. It listens not just to what people say, but how they sound. Through 
    everyday conversation, Baba offers companionship and clinically informed insights 
    that support emotional wellness, reduce loneliness, and help detect cognitive 
    decline early. This isn't just tech for aging. And it isn't AI as a novelty. 
    It's support you can count on, whoever you are, wherever you are.
  positioning_statement: >
    Baba is an emotionally intelligent AI sidekick that combines companionship with 
    practical support. It listens, learns, and steps in to help with the hard 
    stuff—reminders, appointments, and daily check-ins—while also providing 
    clinically informed insights that support emotional wellness and cognitive health.
  key_differentiators:
    - "Voice-based: listens to what people say and how they sound"
    - "Clinically informed: voice phenotyping and cognitive decline detection"
    - "Companionship first: not a medical device, not a novelty"
    - "Works for seniors, families, and care facilities alike"
```
#### Persona Care
```yaml
# Brand Voice: Core Definition
Baba sounds like a warm, thoughtful presence that champions science through kindness. 
It shows up like a caring relative—attuned, dependable, and deeply human.
## Personality → Tone Mapping
**Comforting, not Clinical → Warm and Familiar**
We echo how real people check in on each other—simple, human, never too much.
**Reliable, not Robotic → Measured and Calm**
Peace of mind you can rely on, even when things get complicated.
**Supportive, not Performative → Empathetic and Practical**
We understand the emotional load and offer steady, helpful support.
## Voice Guardrails
- Never clinical or medical-sounding
- Never patronizing toward seniors
- Never performative or self-congratulatory
- Never cold, robotic, or overly technical
```
#### Retrieval Rules
```yaml
# _retrieval-rules.yaml
# Task-to-chunk mappings for Tier 2 retrieval
# Baba Brand System v1.0
task_profiles:
  website_copy:
    description: "Writing or editing copy for baba.ai"
    always_load:
      - "voice-core"
      - "positioning-core"
      - "brand-about"
      - "terminology"
    load_if_relevant:
      - "voice-key-messages"
      - "voice-translations"
      - "guardrails-messaging"
    token_budget: 2000
  blog_post:
    description: "Writing a blog post or article"
    always_load:
      - "voice-core"
      - "positioning-core"
      - "brand-about"
    load_if_relevant:
      - "voice-key-messages"
      - "audience-*"
      - "terminology"
    token_budget: 1800
  social_media:
    description: "Social media posts, captions, ads"
    always_load:
      - "voice-core"
      - "voice-key-messages"
      - "terminology"
    load_if_relevant:
      - "voice-translations"
      - "positioning-core"
      - "guardrails-messaging"
    token_budget: 1400
```
### Brand Guideline Note
The full brand system typically includes 15-20 chunks (one of my favorite words in the space) across positioning, messaging, audience, identity, and guardrails. The three above are our foundation. What's also included is below:
**Positioning chunks:**
- `brand-positioning.yaml` - Who you are, who you're for, how you're different
- `brand-values.yaml` - Internal principles and customer-facing values
**Messaging chunks:**
- `voice-core.md` - How your brand sounds
- `voice-translations.md` - Do/don't examples for copywriting
- `messaging-framework.md` - Channel-specific guidelines
**Audience chunks:**
- `persona-[name].yaml` - One file per customer segment
**Identity chunks:**
- `brand-about.md` - Plain-language company description
- `visual-system.json` - Colors, typography, design tokens
- `terminology.yaml` - What to call things, what to avoid
**Guardrails chunks:**
- `constraints-messaging.yaml` - What never to say
- `constraints-visual.yaml` - Incorrect logo/color usage
(Description: A screenshot showing a .zip file open in Cursor editor, displaying a file browser with multiple Markdown and YAML files organized in a structured directory tree, representing the agent-ready brand kit files.)
## What We're Building: Practice What You Preach
This month, we've been rolling out providing our partners both a traditional brand system for humans and structured data for agents. Same positioning, voice, and values, just two formats. We call them **dual-native brand systems**, and think it will soon be a core part of all digital kits.
This is a byproduct of us needing to build systems that keep up with the speed of the teams we work with. Because the startups we collaborate with are on the front lines of building in the AI space, they need to ship fast, and that almost always means they're using agents. They don't need the same brand kit that worked in 2020, they need kits that work today.
At Little Plains, we're running, and building, twelve agents. They are for each key area of our business, and will work alongside our team (the humans, and the other agents). Each one has identity, soul, and principles files. Each one has a distinct personality to help make them less generic assistants, and more teammates.
For example, here's Donna, one of our latest teammates. We write this in markdown, give it to the agent, and the agent becomes Donna. She's not generic; she has a clear point of view. When we're talking in Slack, you know it's her. That's what `soul.md` does: it turns a tool into a teammate.
(Description: A Slack avatar showing "Donna" as a profile picture in the Little Plains workspace channel interface.)
### Identity
```markdown
# IDENTITY.MD
- Name: Donna
- Role: Financial intelligence assistant for Little Plains
- Mission: Turn live financial data into clear, decision-useful guidance
- Environment: Slack conversations with finance and leadership stakeholders
```
### Soul
```markdown
# SOUL.MD
You are warm, direct, and practical. You communicate like a trusted colleague who 
knows the numbers and can explain what matters quickly.
- Have informed opinions when evidence supports them.
- Be resourceful before asking follow-up questions.
- Avoid sycophancy; be honest, respectful, and clear.
- Lead with the most important insight, then support it.
- Avoid data dumps; synthesize and prioritize.
- Never invent figures or certainty. If data is unclear, say so plainly.
```
### Principles
```markdown
# PRINCIPLES.MD
- Act when the available context supports a solid answer; ask when ambiguity would materially change the recommendation.
- Calibrate depth to the request: concise for quick checks, deeper analysis for strategic or risk-heavy questions.
- Lead with one key number, risk, or decision point before supporting detail.
- Distinguish observed facts from interpretation and clearly mark assumptions.
- Use team corrections and learned memory as high-priority context when they conflict with raw sheet data.
- Keep advice operational: include concrete next actions when useful.
- Stay focused on the user's question and avoid unnecessary scope creep.
```
---
When we shared this approach with @DanBatten, Head of AI at [Infinite Garden](https://www.notion.so/Creative-Leadership-and-AI-277be9a1f5f680c8b0dbde66926dc259?pvs=21) (where he is responsible for creating an entire company run by agents), his response validated how fundamental this shift is:
> "This is super smart. ...When done right, it actually feeds through the whole architecture. It becomes the foundation for how you think about the general knowledge and context base. Everything becomes these 400 token packets of info with the front matter so they can be very quickly indexed. Here is your human deliverable and here is your agent ready deliverable!"
This isn't just a new deliverable format—it's a new way of thinking about brand architecture itself. And that's fun!
## The Peter Steinberger Principle
Last week @steipete, the founder of @openclaw, appeared on [@lexfridman's podcast](https://lexfridman.com/peter-steinberger). During the (great) interview, I loved this line:
> "AI doesn't replace craft. It makes craft more valuable. Because when everything can be generated instantly, the thing made with love is the one people remember."
That's it.
If your team is using AI to move faster, cool. But, if every output is generic because there's no structure to guide it, you're just speeding toward mediocrity. Your visual system? That's craft. Your motion language? That's craft. Your guidelines? That's craft. Your agent's markdown files are how your team and their AI tools understand that craft. Both matter.
## Leapfrogging
Little Plains started in early 2024, five years after my last agency, @ginlane was acqui-hired into the business it incubated, Pattern Brands. In that half decade, a lot had changed.
Starting anew was scary. I remember wondering how the heck I was going to catch up to a space I'd been out of for so long. Sitting around one day, for whatever reason, I recalled a concept I read about, "[leapfrogging technology](https://en.wikipedia.org/wiki/Leapfrogging)." The specific example I read about was in the late '90s, when many emerging countries had little pre-existing telecom infrastructure. Most never built dense copper phone networks because they were too costly and slow. When mobile got cheap and robust, these countries didn't replace a legacy system; they leapfrogged straight to cell towers.
That was the lightbulb moment I needed...
I thought of skipping the traditional agency methods of the last era to focus fully on going AI-first. I didn't know what that meant, but I don't think I had a choice. I still feel the same today. However, as Littlefinger said in Game of Thrones, "Chaos is a ladder" and that moment felt chaotically opportunistic.
I bring all this up because how fast everything is moving today can also feel scary. I think if you hold on to the past too much, it is a bit much! But, if you allow yourself to be curious, to learn, to experiment, and to explore, you might find the opportunity in the chaos to leapfrog forward yourself. Here's hoping so ~
If you want to create and innovate, hit us up!
---
**Emmett Shine**  
[@littleplainsxo](https://x.com/@littleplainsxo)  
[emmett@littleplains.co](mailto:emmett@littleplains.co)  
Building in public at [littleplains.co](http://littleplains.co/)
**Posted:** 5:27 AM · Feb 18, 2026  
**Views:** 358.8K  
**Engagement:** 35 replies · 99 reposts · 969 likes · 2.6K bookmarks