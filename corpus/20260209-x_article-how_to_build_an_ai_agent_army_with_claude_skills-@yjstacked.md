# How to Build an AI Agent Army with Claude Skills

(Description: Hero image showing two hands reaching toward each other in a classic "creation of Adam" pose. One hand appears robotic/digital with blue circuitry patterns, the other is human. A MacBook with an Apple logo is visible in the background on a marble surface, suggesting collaboration between human and AI.)

Every time you paste the same instructions into Claude, you're burning tokens and degrading output quality. Most teams don't realize their AI is underperforming because they're doing the equivalent of re-training an employee from scratch every single day.

Claude Skills solve this. They're not templates. They're not saved prompts. They're **modular capabilities** that Claude loads automatically when needed, turning it from a general assistant into a specialized expert that remembers how to do your specific workflows.

Before we start, if you want to work with us and automate jarring business operations, head over to https://tally.so/r/mZbV0a

Here's how to stop wasting context and start building a digital workforce that actually gets better over time.

## What Claude Skills Actually Are

Skills are **folders containing instructions, scripts, and resources** that Claude loads dynamically when relevant to your task.

Think of Skills like specialized training modules for an employee:

- **Without Skills:** You explain your brand guidelines every single time you need a document. Claude starts from zero, burns 2,000+ tokens on setup, and still gets details wrong.
- **With Skills:** You package those guidelines once. Claude sees "create brand document," loads the skill automatically, and applies your standards without being asked.

### The Core Innovation: Progressive Disclosure

Traditional approaches load everything upfront. Your project context, custom instructions, example files — all consuming tokens whether Claude needs them or not.

Skills use **progressive disclosure**:

- **Startup:** Claude loads only skill names and descriptions (metadata)
- **Relevance check:** User asks for something → Claude checks if a skill matches
- **Dynamic load:** Claude reads only the specific skill files needed for this task
- **Execution:** Skill guides Claude through the workflow with zero wasted context

The difference: Your 50KB brand guidelines document doesn't consume any tokens until Claude actually needs to create a branded document.

## Skills vs Everything Else

Claude has multiple ways to extend its capabilities. Here's when to use each:

| Feature | Purpose | Context Loading | Best For |
|---------|---------|-----------------|----------|
| Projects | Persistent workspaces with shared context | Context available within project conversations | Team collaboration, shared background knowledge |
| Custom Instructions | Global behavioral preferences | Always loaded | Tone, style, general preferences |
| MCP (Model Context Protocol) | Connects to external tools/data | Provides access to resources | Slack, databases, APIs, real-time data |
| Skills | Specialized task workflows | Loaded selectively when Claude determines relevance | Repeatable tasks, domain expertise, workflows |

The pattern most teams should use: **MCP provides the tools, Skills teach Claude how to use them.**

Example: Sentry's MCP server gives Claude access to error data. Sentry's **sentry-code-review skill** teaches Claude their specific bug analysis workflow and how to format GitHub PR comments with fixes.

## How Skills Work: The Technical Reality

### File Structure

Every skill is a folder with a `SKILL.md` file. That's it. The rest is optional.
```
my-skill/
├── SKILL.md                    # Required: Instructions and metadata
├── references/                 # Optional: Context files
│   ├── examples.md
│   └── glossary.md
├── scripts/                    # Optional: Executable code
│   └── analyzer.py
└── templates/                  # Optional: Document templates
    └── report.docx
```

### The SKILL.md Format
```yaml
---
name: brand-document-creator
description: Creates documents following Acme Corp brand guidelines
---

# Brand Document Creator

## Instructions

When creating any document:
1. Load `references/brand-guidelines.md` for styling rules
2. Use templates from `templates/` directory
3. Apply color palette: Primary #0066CC, Secondary #FF6B35
4. Include logo placement per section 3 of guidelines
5. Run `scripts/validate-brand.py` to check compliance

## Reference Files

- `brand-guidelines.md`: Complete style guide
- `approved-templates.md`: Pre-approved layouts
- `tone-examples.md`: Voice and messaging samples
```

**YAML frontmatter** (the section between --- markers) is required and must include:

- `name:` Unique identifier
- `description:` When Claude should use this skill

The body contains instructions Claude follows when the skill is invoked.

### How Claude Decides to Use a Skill

1. **At startup:** Claude loads all skill names and descriptions into its system prompt (this is lightweight metadata, not full content)
2. **User makes request:** "Create a marketing one-pager for our new product"
3. **Skill matching:** Claude scans skill descriptions, finds brand-document-creator matches
4. **Progressive load:** Claude reads `SKILL.md` body, then loads only referenced files it actually needs
5. **Execution:** Claude follows the instructions, runs scripts if needed, delivers result

**Key insight:** A skill with 100MB of reference PDFs consumes zero tokens until Claude decides it's relevant and opens specific files.

## Built-in Skills You Can Use

Anthropic provides document creation skills that work across Claude.ai, Claude Code, and the API. These Skills require Code Execution to be enabled.

**Plan availability:** Skills are included in Max, Pro, Team, and Enterprise plans at no additional cost. API usage follows standard API pricing.

### Document Creation Skills

Available on paid plans when Code Execution is enabled:

- **pptx:** Create and edit PowerPoint presentations
- **xlsx:** Create Excel spreadsheets with formulas and formatting
- **docx:** Create and edit Word documents
- **pdf:** Extract text/tables, fill forms, merge PDFs

Example:

> User: "Create a PowerPoint about Q3 sales results with our revenue by region"
> 
> Claude: [Automatically invokes pptx skill] [Creates professional deck with charts] [Returns downloadable .pptx file]

You don't invoke these manually. Claude detects when you need document creation and uses the appropriate skill automatically.

### Example Skills You Can Enable

Anthropic's [public skills repository](https://github.com/anthropics/skills) contains dozens of examples you can customize:

**Creative & Design:**
- AI image generation workflows
- Music composition
- Brand design systems

**Development & Technical:**
- Web app testing
- MCP server generation
- Code review workflows

**Enterprise & Communication:**
- Meeting notes formatting
- Email template generation
- Project documentation

To use these:
1. Browse the [anthropics/skills repository](https://github.com/anthropics/skills)
2. Download the skill folder
3. Upload via Settings > Capabilities in Claude.ai

## Creating Your First Custom Skill

### Use the Skill Creator (The Fast Way)

Claude includes a **skill-creator** skill that guides you through the process interactively.

**Step 1: Enable skill-creator**

Go to Settings > Capabilities, enable the skill-creator skill.

**Step 2: Describe what you need**

Prompt: "I just enabled skill-creator. Help me build a skill that converts my tweets into newsletter content."

What happens: Claude asks clarifying questions:
- What format should the newsletter follow?
- Do you have example tweets?
- Should it match a specific voice/tone?
- Any structural requirements?

**Step 3: Provide examples**

Upload:
- Sample tweets showing your writing style
- Example newsletter format you like
- Any specific guidelines

**Step 4: Generate and download**

Claude creates:
- Properly formatted `SKILL.md` file
- Organized folder structure
- Reference files from your examples

Downloads as a ZIP file.

**Step 5: Upload to Claude**

Settings > Capabilities > Upload a skill > Select your ZIP

**Step 6: Test it**

Prompt: "I just added the tweet-to-newsletter skill. Convert this tweet into newsletter format: [paste tweet]"

Claude automatically detects the skill, loads it, and applies your specific formatting and voice.

## Real-World Skill Examples

### 1. Marketing Analytics Skill

**Problem:** Analysts paste the same data interpretation instructions every time they upload a CSV.

**Solution:** Create a skill with:
```yaml
---
name: marketing-analytics
description: Analyzes marketing campaign data using company-specific metrics and formulas
---

# Marketing Analytics

## Instructions

When analyzing marketing data:
1. Load `scripts/calculate-metrics.py` for accurate calculations
2. Reference `references/metrics-glossary.md` for definitions
3. Calculate these KPIs (in order):
   - CPC: Total Spend / Total Clicks
   - Conversion Rate: (Conversions / Visitors) × 100
   - ROI: ((Revenue - Spend) / Spend) × 100
   - CAC: Spend / New Customers
4. Compare against targets in `references/performance-benchmarks.md`
5. Generate insights following `references/report-template.md`

## Reference Files

- `metrics-glossary.md`: Definitions of all marketing terms
- `performance-benchmarks.md`: Target ranges for each KPI
- `report-template.md`: Standard output format

## Scripts

- `calculate-metrics.py`: Deterministic calculations (not LLM-interpreted)
```

**Why scripts matter:** LLMs can misinterpret formulas. A Python script ensures CPC is always spend / clicks, not an approximation.

### 2. Brand Compliance Skill

**Problem:** Team creates documents that don't match brand standards.

**Solution:**
```yaml
---
name: acme-brand-standards
description: Applies Acme Corp brand guidelines to all documents and presentations
---

# Acme Brand Standards

## Instructions

Apply these standards to ALL documents:

### Color Palette
- Primary: #0066CC (Acme Blue)
- Secondary: #FF6B35 (Acme Orange)
- Text: #333333 (Dark Gray)
- Background: #FFFFFF or #F5F5F5

### Typography
- Headings: Montserrat Bold
- Body: Open Sans Regular
- Captions: Open Sans Light

### Logo Usage
- Minimum size: 1 inch width
- Clear space: 0.25 inches on all sides
- Never modify colors or proportions
- Reference `templates/logo-placement-examples.pdf`

### Document Templates

Use pre-approved templates from `templates/` directory:
- `one-pager.pptx` for product sheets
- `presentation.pptx` for decks
- `report.docx` for written documents

Run `scripts/brand-check.py` before finalizing any document.
```

**Result:** Every document Claude creates follows your exact standards without you specifying colors, fonts, or layouts each time.

### 3. AB Test Generator Skill

**Problem:** Product managers manually brainstorm test ideas without a systematic framework.

**Solution:** Skill that uses MCP to scrape your website, then applies structured AB testing methodology.
```yaml
---
name: ab-test-generator
description: Generates prioritized AB test ideas for websites using ICE framework
---

# AB Test Generator

## Instructions

When asked for AB test ideas:
1. Use Firecrawl MCP to scrape the target URL
2. Analyze current page structure, copy, and layout
3. Apply ICE framework (Impact × Confidence × Ease)
4. Generate 5-10 experiment ideas
5. For each idea provide:
   - Hypothesis
   - Test variation description
   - Impact score (1-10)
   - Confidence score (1-10)
   - Ease score (1-10)
   - ICE score (product of above)
   - Success metrics
6. Sort by ICE score descending

## Reference
- `references/ice-framework.md`: Scoring guidelines
- `references/test-best-practices.md`: What makes good tests
```

Usage:

> User: "Generate AB test ideas for acmecorp.com/pricing"
> 
> Claude: [Loads ab-test-generator skill] [Uses Firecrawl MCP to scrape page] [Analyzes layout] [Generates prioritized experiments]

Output includes things like:
- "Move social proof above pricing table (ICE: 8.5)"
- "Test value-based vs feature-based headlines (ICE: 7.2)"
- "Add money-back guarantee badge (ICE: 6.8)"

## Advanced Skill Patterns

### Pattern 1: Skill + MCP Integration

MCP gives Claude access to tools. Skills teach Claude how to use them effectively.

**Example: Linear Task Creation**
```yaml
---
name: linear-task-creator
description: Creates Linear tasks following team conventions and project structure
---

# Linear Task Creator

## Instructions

When creating Linear tasks:
1. Use Linear MCP to access projects and teams
2. Follow team conventions:
   - Engineering tasks: Include tech spec link
   - Design tasks: Include Figma link
   - Product tasks: Include PRD link
3. Set priority based on `references/priority-matrix.md`
4. Auto-assign based on `references/team-ownership.md`
5. Apply labels per `references/label-taxonomy.md`
6. Set sprint based on current planning cycle

## Reference Files

- `priority-matrix.md`: P0/P1/P2 definitions
- `team-ownership.md`: Who owns what areas
- `label-taxonomy.md`: Standardized label usage
```

**Result:** "Create a task to fix the login bug" becomes a properly structured Linear issue with correct priority, owner, labels, and links — automatically.

### Pattern 2: Multi-Skill Workflows

Claude can load multiple skills simultaneously for complex tasks.

**Example: Financial Model Creation**

> User: "Build a DCF valuation model for a SaaS company"
> 
> Claude: [Loads custom dcf-analysis skill] [Loads built-in xlsx skill] [Creates Excel file with formulas] [Applies DCF methodology from skill] [Returns downloadable model]

The dcf-analysis skill provides the financial modeling methodology. The xlsx skill handles actual spreadsheet creation. They work together.

### Pattern 3: Scripts for Determinism

When to use scripts:
- Mathematical calculations that must be exact
- Data transformations requiring consistency
- Analysis following specific algorithms
- Validation checks with binary pass/fail

**Example: Data Quality Checker**
```python
# scripts/validate-data.py
import pandas as pd

def validate_marketing_data(df):
    """Validates marketing data against known rules."""
    errors = []
    
    # Check required columns
    required = ['campaign', 'spend', 'clicks', 'conversions']
    missing = [col for col in required if col not in df.columns]
    if missing:
        errors.append(f"Missing columns: {missing}")
    
    # Check for negative spend
    if (df['spend'] < 0).any():
        errors.append("Negative spend values detected")
    
    # Check conversion rate sanity
    df['conv_rate'] = df['conversions'] / df['clicks']
    if (df['conv_rate'] > 1.0).any():
        errors.append("Conversion rate exceeds 100%")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'summary': df.describe()
    }
```

Claude runs this script and gets deterministic validation results, not LLM-interpreted guesses about data quality.

## Skills for Teams and Organizations

### Organization-Wide Provisioning

For Team and Enterprise plans:

Organization Owners can provision skills for all users:
1. Go to Admin settings > Capabilities
2. Upload a skill
3. Choose whether to enable it by default for all users

What happens:
- Skill appears automatically in every team member's skill list
- Users see a team indicator badge
- Individual users can toggle it on/off
- No manual upload required by each person

Use cases:
- Company brand guidelines
- Standard report formats
- Compliance checklists
- Internal workflow automation
- Domain-specific analysis frameworks

### Skill Discovery for Teams

Currently, individual peer-to-peer skill sharing is not available. Options:
- **Organization provisioning** (Team/Enterprise plans)
- **Version control:** Share skill folders via GitHub/GitLab
- **Documentation:** Maintain internal skill library docs
- **API deployment:** Use the /v1/skills endpoint to programmatically manage skills

## Using Skills via the API

Skills work identically across Claude.ai, Claude Code, and the Claude API.

### Basic API Usage

**Prerequisites:**

Skills run in Claude's code execution environment. To use Skills via the API, you need:
- The skills-2025-10-02 beta header
- The code-execution-2025-08-25 beta header
- The code execution tool enabled

**Note:** Skills require Code Execution in Claude environments that use them (claude.ai, Claude Code, API).
```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Create a presentation about renewable energy"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

**Key components:**
- `betas:` Both beta headers are required
- `container.skills:` Array of skills to make available
- `tools:` Code execution tool must be included
- You can include multiple skills per request (check current API limits)

### Using Custom Skills via API

**Step 1: Upload your skill**
```python
from anthropic.lib import files_from_dir

# Create custom skill by uploading skill directory
dcf_skill = client.beta.skills.create(
    display_title="DCF Analysis",
    files=files_from_dir("/path/to/dcf_skill"),
    betas=["skills-2025-10-02"]
)
```

The skill directory should contain a `SKILL.md` file and any reference files or scripts.

**Step 2: Use it in requests**
```python
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"}
        ]
    },
    messages=[{
        "role": "user",
        "content": "Build a DCF model for this SaaS company"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

**Combining skills:** You can include multiple skills per request, mixing Anthropic-managed skills (pptx, xlsx, docx, pdf) with your custom skills.

### Retrieving Created Files

When skills create documents, they return files through the code execution tool. Extract the file ID from the tool result and download using the Files API:
```python
# Extract file ID from response
file_id = None
for block in response.content:
    if block.type == 'tool_use' and block.name == 'code_execution':
        for result_block in block.content:
            if hasattr(result_block, 'file_id'):
                file_id = result_block.file_id
                break

if file_id:
    # Download the file
    file_content = client.beta.files.download(
        file_id=file_id,
        betas=["files-api-2025-04-14"]
    )
    
    # Save to disk
    with open("output.xlsx", "wb") as f:
        file_content.write_to_file(f.name)
```

**Note:** File download requires the files-api-2025-04-14 beta header. See the [code execution tool documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files) for complete details.

## Best Practices

### 1. Write from Claude's Perspective

**Bad:**
```
This skill helps users analyze marketing data by providing a framework for calculating ROI and other metrics.
```

**Good:**
```
When the user asks to analyze marketing data:
1. Load the CSV file
2. Calculate ROI: (Revenue - Spend) / Spend
3. Identify top 3 campaigns by ROI
4. Generate recommendations
```

Write instructions as if you're training Claude to do the job, not describing the skill to users.

### 2. Use Progressive Disclosure

**Bad: Loading everything upfront**
```
Here's everything about our company: [10,000 words of context]
Use this information when relevant.
```

**Good: Reference files loaded as needed**
```
When creating a product brief:
- Load `references/product-catalog.md` for current offerings
- Load `references/pricing-tiers.md` if pricing is mentioned
- Load `references/competitor-analysis.md` if doing competitive research
```

Only load what's needed for each specific task.

### 3. Make Names and Descriptions Specific

**Bad:**
```yaml
---
name: helper
description: Helps with various tasks
---
```

**Good:**
```yaml
---
name: customer-support-email-generator
description: Generates customer support email responses following company tone guidelines and including relevant knowledge base links
---
```

Claude uses the description to decide when to invoke your skill. Be specific about triggers.

### 4. Iterate Based on Real Usage

1. Deploy initial version
2. Monitor what Claude does with it
3. Identify where it goes off-track
4. Add constraints or examples
5. Update and redeploy

**Example iteration:**
```
# Version 1
Generate a meeting summary.

# Version 2 (after seeing Claude miss action items)
Generate a meeting summary including:
- Key decisions
- Action items with owners
- Follow-up dates

# Version 3 (after seeing inconsistent formatting)
Generate a meeting summary using this exact format:

## Decisions
- [List decisions here]

## Action Items
- [ ] Task description (@owner, due: YYYY-MM-DD)

## Follow-up
- [Next steps]
```

### 5. Use Scripts for Precision

**When scripts are worth it:**
- Financial calculations
- Data validation
- Statistical analysis
- Compliance checks
- File transformations

**When instructions are enough:**
- Creative writing
- Document formatting
- Workflow orchestration
- Conversational responses

## Common Issues and Solutions

### Problem: Skill not being invoked

**Causes:**
- Description doesn't match the task
- Skill name is too generic
- Other skills are masking it

**Solutions:**
- Make the description more specific
- Test with explicit phrases: "Using the [skill-name] skill, do X"
- Check for conflicting skills with similar descriptions

### Problem: Claude uses wrong reference files

**Causes:**
- Instructions aren't clear about when to load each file
- File organization is confusing

**Solutions:**
- Add explicit "Load X when doing Y" instructions
- Use clear file names: `brand-colors.md` not `guidelines-v2-final.md`
- Group related files in subdirectories

### Problem: Inconsistent outputs

**Causes:**
- LLM interpreting instead of executing
- Missing constraints
- No validation step

**Solutions:**
- Add scripts for deterministic parts
- Provide explicit output templates
- Include validation scripts
- Add examples of correct outputs

### Problem: Skills greyed out

**Causes:**
- Code execution disabled
- Organization admin hasn't enabled Skills

**Solutions:**
- Check Settings > Capabilities > Code execution is ON
- For Team/Enterprise: Ask organization Owner to enable in Admin settings

## Agent Skills as an Open Standard

Anthropic has moved Agent Skills toward an open standard with a specification available at [agentskills.io](https://agentskills.io/).

What this means:
- Skills use a simple, portable format (folders with `SKILL.md` files)
- The format is documented and reproducible
- Other AI platforms can adopt the same structure
- Reference SDK available for implementations

**Growing ecosystem:**

The Skills format is being adopted across popular development tools and AI platforms, enabling portability and shared workflows.

**Platform compatibility:**

Skills work identically across Claude.ai, Claude Code, and the Claude API. Some skills may use platform-specific features; authors can note this in the compatibility field of `SKILL.md` frontmatter.

## Partner Skills

### Skills from Partners

Anthropic has collaborated with partners to create specialized Skills that combine workflow expertise with tool access:

**Examples of partner integrations:**
- Project management platforms for issue tracking and backlog generation
- Design tools for design-to-code workflows
- Documentation systems for knowledge management
- Payment infrastructure and subscription workflows
- Cross-platform automation

**How partner skills work:** These skills are designed to work with their respective MCP connectors, combining tool access with workflow expertise.

Example: A project management skill might teach Claude best practices for turning specifications into properly structured backlogs, while the MCP connector provides the actual tool access.

## Getting Started: Your First Week

### Day 1: Understand What You Have

1. Enable Code Execution in Settings > Capabilities
2. Test Anthropic's built-in skills: "Create an Excel sheet tracking my project tasks" "Make a PowerPoint about our Q1 results"
3. Notice how Claude automatically invokes the right skill

### Day 2: Identify Your Repetitive Tasks

Answer these questions:
- What instructions do you paste into Claude repeatedly?
- What workflows require the same setup every time?
- What domain knowledge does your team reuse constantly?

Pick your top 3 candidates.

### Day 3: Build Your First Skill

Use skill-creator:

"I enabled skill-creator. Help me build a skill that [describes your workflow]."

Provide examples when Claude asks. Download the ZIP.

### Day 4: Test and Iterate

1. Upload your skill (Settings > Capabilities)
2. Test with multiple variations of requests
3. Note where Claude goes off-track
4. Update `SKILL.md` instructions
5. Re-upload and test again

### Day 5: Add Reference Files

Enhance your skill with:
- Examples of good outputs
- Glossary of terms
- Templates to follow
- Company-specific guidelines

### Day 6-7: Build Skill Library

Create 2-3 more skills for your common workflows:
- Email templates
- Report formats
- Data analysis frameworks
- Meeting notes
- Code review checklists

## The Bottom Line

**The problem most teams have with AI:** Every conversation starts from zero. You burn tokens on setup. You get inconsistent results. You can't build institutional knowledge.

**What Skills solve:** Package expertise once, apply it automatically forever.

Instead of explaining your brand guidelines 50 times, you create one skill. Instead of pasting analysis instructions into every data request, you build one skill. Instead of hoping Claude remembers your workflow, you encode it.

**The shift:** From "AI assistant that needs constant direction" to "AI employee that knows the job."

Start with the built-in document skills. Test them. Then create one custom skill for your most repeated workflow. Watch how much faster Claude becomes when it stops asking the same questions and starts delivering exactly what you need.

**The teams winning with AI aren't using more powerful models. They're using Skills to make Claude an expert in their specific domain.**

Your skill library is your competitive advantage. Start building it today. If you want this set up (DFY) — https://tally.so/r/mZbV0a

## Resources

### Official Documentation

- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills API Quickstart](https://platform.claude.com/docs/en/build-with-claude/skills-guide)
- [Claude Code Skills Guide](https://code.claude.com/docs/en/skills)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Agent Skills Open Standard](https://agentskills.io/)

### Blog Posts

- [Introducing Agent Skills](https://www.anthropic.com/news/skills)
- [Equipping Agents for the Real World](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### Support

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

---

**Published:** 12:57 AM · Feb 9, 2026  
**Engagement:** 316 Replies, 185 Likes, 397 Bookmarks, 14.2K Views