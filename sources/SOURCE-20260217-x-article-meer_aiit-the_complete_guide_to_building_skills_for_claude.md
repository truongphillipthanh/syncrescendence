---
url: https://x.com/Meer_AIIT/status/2023763364502008002
author: "@Meer_AIIT"
captured_date: 2026-02-17
title: The Complete Guide to Building Skills for Claude
id: SOURCE-20260217-009
original_filename: "20260217-x_article-the_complete_guide_to_building_skills_for_claude-@meer_aiit.md"
status: triaged
platform: x
format: article
creator: meer_aiit
signal_tier: strategic
topics: [claude-code, developer-tools, ai-engineering, best-practices]
teleology: implement
notebooklm_category: claude-code
aliases: ["meer_aiit - complete guide to building Claude skills"]
synopsis: "Comprehensive breakdown of Anthropic's 33-page Skills guide. Covers skill folder structure (SKILL.md, scripts, references, assets), three-level loading (hook/instructions/deep), YAML frontmatter design, three skill categories (making stuff, running processes, making MCP better), testing approaches, distribution via Claude.ai/Code/API, and four implementation patterns (sequential workflows, multi-tool coordination, iterative improvement, smart tool selection)."
key_insights:
  - "Skills have three loading levels: hook (always in system prompt), instructions (loaded when relevant), deep files (discovered on demand) — keeps context small until needed"
  - "MCP gives Claude the tools, Skills teach Claude how to use them — without skills, users connect MCP and ask 'now what?' and every session starts from zero"
  - "Four skill patterns: sequential workflows (ordered steps with validation), multi-tool coordination (phase handoffs), iterative improvement (quality-gated refinement), and smart tool selection (context-dependent routing)"
---
# The Complete Guide to Building Skills for Claude
*Anthropic just dropped a 33-page guide on building Skills for Claude. I broke it down so you don't have to read the whole thing.*
By the end of this article, you'll know what Skills are, how they work, and how to build one from scratch. No fluff, just what you need:
## Chapter 1: Fundamentals
A skill is a folder that teaches Claude how to do something specific. Instead of explaining your workflow every single time, you package it once. Claude learns it, remembers it, uses it.
### What goes in the folder
```
your-skill-name/
├── SKILL.md (Instructions) — Required
├── scripts/ (Optional)
│   └── Python files, Bash scripts
├── references/ (Optional)
│   └── Documentation, API guides
└── assets/ (Optional)
    └── Templates, Images
```
### Three Levels of Loading
**Level 1: The hook**
YAML frontmatter sits at the top of SKILL.md. This is always loaded in Claude's system prompt. It tells Claude "here's what this skill does, here's when to use it." Minimal context, maximum clarity.
**Level 2: The instructions**
The main body of SKILL.md loads when Claude thinks it's relevant. This is where your full workflow lives. Step-by-step processes, error handling, examples.
**Level 3: The deep stuff**
Additional files Claude discovers only when needed. API documentation, reference guides, template libraries. This keeps context small until Claude actually needs the details.
### Why This Matters
You can load multiple skills at once. Your skill needs to play well with others, not assume it's the only one running.
And here's the best part: build once, use everywhere. Same skill works in Claude.ai, Claude Code, and via API. No modifications needed.
### Skills + MCP: The Full Picture
```
MCP (The Tools)          SKILLS (The Process)
- Connections           • How to use
- Data access          + • Workflows
- Tool calls             • Best practices
- Real-time              • Domain knowledge
         ↓                    ↓
    "What Claude    +    "How Claude
     CAN do"              SHOULD do"
         └──────────┬─────────┘
                    ↓
         Complete Solution
         - Tool Access
         - Knowledge Layer
         - Reliable Results
```
MCP gives Claude the tools. Skills teach Claude how to use them.
Think of it like this: You hire a contractor and give them access to your entire workshop. That's MCP. But they still need the blueprints and the process. That's the skill.
**Without skills:**
- Users connect your MCP integration and ask "now what?"
- They send you messages: "How do I set this up?"
- Every session starts from zero.
**With skills:**
- Claude knows the workflow automatically.
- Best practices are embedded.
- Users get results without hand-holding.
## Chapter 2: Planning and Design
Start with the outcome you want. Don't build a skill because you can. Build it because there's a specific problem that keeps coming up.
### Use Case: Customer Support Ticket Analysis
**Trigger:** User says "analyze my support tickets" or "show me customer pain points"
**Steps:**
1. Pull last 30 days of tickets from Zendesk
2. Group by category and severity
3. Identify patterns in complaints
4. Generate summary with action items
5. Create presentation with findings
**Result:** Complete analysis deck ready to share with the team
**Ask these questions:**
- What's the end goal?
- What tools does this workflow need?
- What mistakes do people make without guidance?
- What domain knowledge makes this work better?
### Three Types of Skills
Anthropic noticed three patterns in how people build skills.
**Category 1: Making Stuff**
These skills create output. Marketing copy, slide decks, data visualizations, code modules.
Example: A skill that generates investor update emails. It knows your metrics, your tone, your format. Claude pulls the data, structures the narrative, writes the email. No templates needed, uses Claude's native abilities.
**Category 2: Running Processes**
These skills automate workflows. Multi-step processes where order matters.
Example: A skill that runs your weekly content planning. It checks what performed well last week, suggests topics for this week, creates a content calendar, assigns tasks to team members. All in sequence, all validated at each step.
**Category 3: Making MCP Better**
These skills turn raw tool access into actual workflows. You built an MCP connector to your database. Now build a skill that knows how to query it correctly.
Example: A skill for your internal analytics database. It knows which tables matter, how to join them, what metrics to calculate, how to format results. Users ask questions in plain English. Claude runs the right queries every time.
### What Success Looks Like
You need to know if your skill actually works. Here are rough benchmarks, not hard rules.
**Numbers to track:**
- Skill loads automatically 9 out of 10 times
- Completes tasks in fewer steps than without the skill
- API calls succeed without retries
**Things to observe:**
- Users don't ask "what do I do next?"
- Results are consistent across different sessions
- New users get it right on the first try
### The Technical Setup
Your folder needs this structure:
```
email-campaign-builder/
├── SKILL.md
├── scripts/
│   └── validate_links.py
├── references/
│   └── brand-voice-guide.md
└── assets/
    └── email-templates/
```
**Rules that matter:**
- SKILL.md must be spelled exactly like that.
- Folder names use dashes: `email-campaign-builder` ✅ (not spaces, underscores, or capitals)
- Don't put a README.md inside the skill folder.
### The YAML Frontmatter
This is how Claude decides whether to load your skill.
**Minimum version:**
```yaml
---
name: email-campaign-builder
description: Creates email campaigns for product launches. Use when user wants to draft launch emails, announcement sequences, or promotional campaigns.
---
```
**What goes in name:** Lowercase words with dashes. Should match your folder name exactly.
**What goes in description:** Two parts, both required.
- Part 1: What does this skill do?
- Part 2: When should Claude use it?
Include phrases users would actually say. Keep it under 1024 characters.
### Writing Descriptions That Work
The description determines whether Claude loads your skill. Get this wrong and your skill never triggers.
**Good description:**
> Generates SQL queries for the customer analytics database. Use when user asks about customer behavior, purchase patterns, retention metrics, or churn analysis. Include queries for monthly cohorts, revenue breakdowns, and user segmentation.
This works because:
- Says what it does clearly
- Lists specific trigger phrases
- Mentions the domain (customer analytics)
**Bad description:**
> Helps with database stuff.
Too vague. Claude has no idea when to use this.
### Writing the Instructions
After the frontmatter comes the actual workflow. Structure it like this: Clear steps (numbered or bulleted). Examples of what success looks like. Common errors and how to fix them.
**Write instructions like you're training someone:**
Instead of: "Ensure data integrity"
Write: "Run `python scripts/check_data.py` and verify these three outputs: no missing fields, dates in YYYY-MM-DD format, no duplicate IDs"
Be that specific. Include what to do when things go wrong.
"If the API returns a 429 error, wait 60 seconds and retry. If it happens again, check rate limits in the dashboard."
Move detailed reference docs to the references/ folder. Keep SKILL.md focused on the core workflow.
## Chapter 3: Testing and Iteration
You can test skills three ways.
**Manual testing:** Open Claude.ai, try your skill, see what happens. Fast, no setup, good for early iteration.
**Scripted testing:** Write test cases in Claude Code. Run them repeatedly as you make changes.
**API testing:** Build full evaluation suites. Run systematic tests against defined benchmarks.
Pick based on who uses your skill. Personal use? Manual is fine. Deploying to 1000 users? Go deeper.
**Pro tip from Anthropic:** Focus on one hard task first. Get Claude to succeed on that single task. Then extract what worked into the skill. This is faster than trying to handle everything at once.
### Three Areas to Test
**1. Does it trigger correctly?**
- Test obvious requests: "Help me analyze these support tickets"
- Test variations: "Can you look at my customer complaints from last month?"
- Test unrelated stuff: "What's the weather?" (should NOT trigger)
**2. Does it work?**
- Run the full workflow.
- Check that outputs are correct.
- Verify API calls succeed.
- Test edge cases like empty data or malformed inputs.
**3. Is it better than nothing?**
Compare with and without the skill enabled. Count how many messages it takes to complete the task. Measure tokens used. Track failed API calls.
Without skill: 12 messages, 3 failed calls, user has to explain the process.
With skill: 3 messages, 0 failed calls, Claude knows the process.
### Using skill-creator
There's a built-in skill called skill-creator. It helps you build other skills. Tell it what you want, it generates the SKILL.md structure. You can build a working skill in 15-30 minutes.
It also reviews skills you've written. "Review this skill and tell me what's wrong with it"
It'll flag vague descriptions, missing error handling, structural issues.
Note: It helps you write skills, but doesn't run automated tests.
### Iteration Loop
Skills aren't done on the first try. Plan to iterate based on what you see.
**Skill doesn't load when it should:**
Your description is too generic. Add specific keywords and phrases to the description field.
**Skill loads for everything:**
Your description is too broad. Add negative triggers: "Use for X. Do NOT use for general Y queries."
**Skill loads but fails:**
Your instructions are unclear. Add more specifics, include error handling, break down complex steps.
## Chapter 4: Distribution and Sharing
Right now, distribution works like this: Users download your skill folder. Zip it. Upload to Claude.ai via Settings > Capabilities > Skills. Or drop it in the Claude Code skills directory.
**For teams:** Admins can deploy skills across the entire workspace. Everyone gets them automatically. No individual setup needed. This shipped in December 2025.
### The Open Standard
Anthropic made Skills an open standard. Same concept as MCP. The goal is portability across platforms. Build a skill once, it should work in any AI tool that supports the standard.
### Using Skills via API
If you're building an application or automated workflow, use the API. The `/v1/skills` endpoint lets you manage skills programmatically. Add skills to API requests with the `container.skills` parameter.
**When to use what:**
- Direct user interaction: Claude.ai or Claude Code
- Testing and iteration: Claude.ai or Claude Code
- Building apps: API
- Production at scale: API
### How to Share Your Skill
Put it on GitHub with a public repo. Include a README that explains what it does (this README is for humans browsing GitHub, not inside the skill folder). Add screenshots showing it in action. Then link to it from your MCP documentation if you have one.
**Simple installation guide:**
1. Download
   - Clone: `git clone github.com/yourcompany/your-skill`
   - Or download ZIP
2. Install
   - Open Claude.ai > Settings > Skills
   - Click Upload
   - Select the zipped folder
3. Enable
   - Toggle your skill on
   - Make sure related MCP server is connected if needed
4. Test
   - Ask Claude: "Help me [task your skill handles]"
### How to Position It
Talk about outcomes, not features.
**Good:** "This skill turns 2 hours of manual SQL work into 30 seconds. Ask Claude a question in plain English, get the exact query you need."
**Bad:** "This skill contains 47 pre-written SQL templates in a structured format with YAML metadata."
If you have an MCP connector, explain the combination: "Our MCP gives Claude access to your data. Our skill teaches Claude how to query it correctly. Together, you ask questions and get answers."
## Chapter 5: Patterns and Troubleshooting
These patterns come from real skills built by early users. They're starting points, not rigid templates.
### Two Ways to Think About Skills
**Problem-first:** User has a goal, skill figures out the tools.
"I need to send a product announcement email to customers who bought in the last 90 days."
The skill orchestrates: query database, filter by date, format email list, draft message, schedule send.
**Tool-first:** User has tools connected, skill teaches best practices.
"I have Stripe MCP connected, now what?"
The skill knows: how to pull transaction data, calculate metrics, handle edge cases, format reports.
Most skills lean one way or the other.
### Pattern 1: Sequential Workflows
Use this when steps must happen in order.
Example: Processing refund requests.
**Step 1: Verify transaction exists**
- Call: `get_transaction(transaction_id)`
- Check: `transaction.status == "completed"`
**Step 2: Check refund eligibility**
- Rule: Refund allowed if < 30 days
- Rule: Product not marked as final sale
**Step 3: Calculate refund amount**
- If partial return: calculate prorated amount
- If full return: use original transaction amount
**Step 4: Process refund**
- Call: `create_refund(transaction_id, amount)`
- Verify: `refund.status == "succeeded"`
**Step 5: Send confirmation**
- Template: `refund_confirmation_email`
- Include: original order details, refund amount, timeline
**Key techniques:**
- Explicit dependencies between steps
- Validation before proceeding
- Rollback instructions if something fails
### Pattern 2: Multi-Tool Coordination
Use this when you need multiple services.
Example: Publishing blog content.
**Phase 1: Content Creation (Internal)**
- Draft blog post based on outline
- Generate 3 social media versions
- Create meta descriptions and tags
**Phase 2: Asset Generation (MCP: Midjourney)**
- Generate header image based on topic
- Create 3 social media graphics
- Save to asset library
**Phase 3: Publication (MCP: WordPress)**
- Upload blog post with formatting
- Attach header image
- Set publication date and categories
**Phase 4: Social Scheduling (MCP: Buffer)**
- Queue social posts
- Attach generated graphics
- Stagger timing across platforms
**Phase 5: Team Notification (MCP: Slack)**
- Post to #marketing channel
- Include preview link
- Tag relevant team members
**Key techniques:**
- Clear handoff between phases
- Data passes from one tool to the next
- Validation before moving forward
### Pattern 3: Iterative Improvement
Use this when output gets better with refinement.
Example: Creating data visualizations.
**Initial Draft:**
1. Analyze data structure
2. Choose appropriate chart type
3. Generate first version
**Quality Check:**
1. Run validation script
2. Check for: missing labels, unclear axes, color accessibility issues
3. List improvements needed
**Refinement:**
1. Address each issue
2. Regenerate affected sections
3. Re-validate
**Repeat until:**
- All labels clear
- Data accurately represented
- Visual hierarchy works
- Accessible color scheme used
**Finalize:**
- Export in multiple formats
- Generate embed code
- Save to library
**Key techniques:**
- Define quality criteria upfront
- Validate programmatically when possible
- Know when to stop iterating
### Pattern 4: Smart Tool Selection
Use this when the same task needs different tools depending on context.
Example: Saving project files.
**Decision Logic:**
If file is collaboration doc (Google Doc, Notion): Keep in cloud workspace, set sharing permissions.
**Key techniques:**
- Domain rules embedded in logic
- Validate before taking action
- Comprehensive documentation of decisions
### Troubleshooting
**Skill won't upload**
Error: "Could not find SKILL.md"
Fix: Rename your file to exactly SKILL.md (case matters).
Error: "Invalid frontmatter"
Fix: Check your YAML syntax.
```yaml
# Wrong - missing dashes
name: my-skill
description: Does things
# Wrong - quotes not closed
description: "Does things
# Right
---
name: my-skill
description: Does things
---
```
**Skill never loads**
Your description is too vague. Add specific trigger phrases users would actually say.
Test by asking Claude: "When would you use the [skill name] skill?"
Claude will quote your description back. If it's unclear to Claude, it's unclear to users.
**Skill loads for everything**
Your description is too broad. Add boundaries: "Use for X. Do NOT use for general Y questions."
Example: "Use for SQL queries on the analytics database. Do NOT use for general data questions without database context."
**Skill loads but doesn't follow instructions**
Instructions are probably too long or buried. Move detailed docs to references/ folder. Keep SKILL.md under 5,000 words focused on core workflow. Put critical instructions at the top with clear headers. For validation that must work every time, use a script instead of text instructions.
**MCP calls keep failing**
Check that your MCP server is actually connected. Claude.ai: Settings > Extensions > verify status.
Test the MCP independently: "Use [Service] to fetch my data"
If that fails, the problem is MCP setup, not your skill.
**Performance is slow**
Your skill might be too large. Move documentation to references/ and link to it. Keep only essential instructions in SKILL.md.
Also check how many skills you have enabled. More than 50 skills loaded at once can slow things down.
## Chapter 6: Resources and References
**Official Documentation:**
Anthropic's Best Practices Guide and API Reference have everything technical. Their blog has deep dives on how skills work under the hood.
**Example Skills:**
GitHub repo at anthropics/skills has real working examples. You can clone them and modify for your needs. Partner skills from companies like Asana, Figma, Sentry show different approaches.
### Quick Validation Checklist
**Before building:**
- Know your 2-3 main use cases
- Understand which tools you need
- Review example skills similar to yours
**During building:**
- Folder named with dashes
- SKILL.md spelled exactly right
- YAML frontmatter has proper --- delimiters
- Description includes what AND when
- Instructions are specific and actionable
**Before sharing:**
- Test on obvious trigger phrases
- Test on paraphrased requests
- Verify it doesn't trigger on random topics
- Run through the full workflow
- Check error handling
**After deploying:**
- Monitor actual usage
- Collect feedback
- Iterate on description and instructions
- Update version number
### YAML Reference
**Required:** name and description
**Optional:** license, allowed-tools, custom metadata
**Custom metadata example:**
```yaml
metadata:
  author: Your Name
  version: 1.0.0
  category: productivity
```
**Security:** No XML brackets (<>), no "claude" or "anthropic" in skill names.
## What You Should Do Now
1. Pick one workflow you keep explaining to Claude over and over.
2. Use skill-creator to generate the first draft in 20 minutes.
3. Test it manually, fix what breaks, test again.
4. If it works, share it on GitHub.
Skills turn repetitive explanations into permanent knowledge. Build your first one this week.
## Additional Resources
**Official Guide:**
[The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en)
**Newsletter:**
[The AI Night](https://www.theainight.com/)
---
*Published: February 17, 2026 | 415K views | 225 reposts | 1.3K likes*