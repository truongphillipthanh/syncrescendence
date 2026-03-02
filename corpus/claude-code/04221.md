# Extraction: SOURCE-20260217-009

**Source**: `SOURCE-20260217-x-article-meer_aiit-the_complete_guide_to_building_skills_for_claude.md`
**Atoms extracted**: 41
**Categories**: analogy, claim, concept, framework, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260217-009-0007
**Lines**: 62-64
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> MCP is like giving a contractor access to a workshop, while skills are the blueprints and process, illustrating that tools alone are insufficient without instructions on how to use them effectively.

## Claim (5)

### ATOM-SOURCE-20260217-009-0004
**Lines**: 40-41
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Multiple Claude skills can be loaded simultaneously, requiring individual skills to be designed for interoperability.

### ATOM-SOURCE-20260217-009-0005
**Lines**: 43-45
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> A single Claude skill can be used across Claude.ai, Claude Code, and via API without modifications.

### ATOM-SOURCE-20260217-009-0008
**Lines**: 66-70
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.60, epistemic_stability=0.80

> Without skills, users will frequently ask for setup instructions and guidance, and each session will effectively start from scratch.

### ATOM-SOURCE-20260217-009-0009
**Lines**: 72-75
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> With skills, Claude automatically understands workflows, embeds best practices, and enables users to achieve results without constant hand-holding.

### ATOM-SOURCE-20260217-009-0021
**Lines**: 204-206
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Anthropic made Skills an open standard, similar to MCP, with the goal of portability across platforms, allowing a skill built once to work in any AI tool supporting the standard.

## Concept (2)

### ATOM-SOURCE-20260217-009-0001
**Lines**: 10-12
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> A 'skill' in Claude is a folder containing instructions and optional files that teach Claude how to perform a specific task, allowing it to remember and reuse workflows without repeated explanations.

### ATOM-SOURCE-20260217-009-0006
**Lines**: 47-60
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> MCP (The Tools) provides Claude with capabilities like connections, data access, and tool calls, representing 'What Claude CAN do,' while SKILLS (The Process) teach Claude 'How Claude SHOULD do' things through workflows and best practices, combining to form a complete solution with tool access, a knowledge layer, and reliable results.

## Framework (9)

### ATOM-SOURCE-20260217-009-0002
**Lines**: 14-22
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> A Claude skill folder typically includes a mandatory `SKILL.md` for instructions, and optional subdirectories for `scripts/` (Python, Bash), `references/` (documentation, API guides), and `assets/` (templates, images).

### ATOM-SOURCE-20260217-009-0003
**Lines**: 25-37
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Claude skills load in three levels: Level 1 (the hook) is YAML frontmatter in `SKILL.md` always loaded in the system prompt; Level 2 (instructions) is the main body of `SKILL.md` loaded when relevant; Level 3 (deep stuff) includes additional files discovered only when needed.

### ATOM-SOURCE-20260217-009-0012
**Lines**: 96-100
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Anthropic identifies three types of Claude skills: 'Making Stuff' (creating output like marketing copy), 'Running Processes' (automating multi-step workflows), and 'Making MCP Better' (turning raw tool access into structured workflows).

### ATOM-SOURCE-20260217-009-0018
**Lines**: 156-174
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Three areas to test for skills are: 1) Does it trigger correctly? (Test obvious requests, variations, and unrelated queries), 2) Does it work? (Run full workflow, check outputs, verify API calls, test edge cases), and 3) Is it better than nothing? (Compare performance with and without the skill, measuring messages, tokens, and failed API calls).

### ATOM-SOURCE-20260217-009-0022
**Lines**: 210-214
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Different contexts for using skills include: Claude.ai or Claude Code for direct user interaction, Claude.ai or Claude Code for testing and iteration, API for building applications, and API for production at scale.

### ATOM-SOURCE-20260217-009-0025
**Lines**: 243-254
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> Skills can be approached in two ways: 'Problem-first,' where the user has a goal and the skill orchestrates tools to achieve it, or 'Tool-first,' where the user has connected tools and the skill teaches best practices for using them.

### ATOM-SOURCE-20260217-009-0026
**Lines**: 255-272
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The 'Sequential Workflows' pattern is used when steps must happen in order, such as processing refund requests, which involves verifying transactions, checking eligibility, calculating amounts, processing the refund, and sending confirmation, with explicit dependencies and validation.

### ATOM-SOURCE-20260217-009-0027
**Lines**: 273-292
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The 'Multi-Tool Coordination' pattern is for tasks requiring multiple services, like publishing blog content, which involves phases for content creation, asset generation (e.g., Midjourney), publication (e.g., WordPress), social scheduling (e.g., Buffer), and team notification (e.g., Slack), with clear handoffs and data passing between tools.

### ATOM-SOURCE-20260217-009-0028
**Lines**: 293-308
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The 'Iterative Improvement' pattern is used when output gets better with refinement, such as creating data visualizations, involving initial drafting, quality checks, and refinement steps repeated until quality criteria are met, with programmatic validation where possible.

## Praxis Hook (24)

### ATOM-SOURCE-20260217-009-0010
**Lines**: 78-80
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When designing a Claude skill, start by defining the desired outcome and identify a specific recurring problem it solves, rather than building a skill simply because it's possible.

### ATOM-SOURCE-20260217-009-0011
**Lines**: 90-93
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To plan a Claude skill, ask: What is the end goal? What tools are needed? What common mistakes do users make? What domain knowledge improves the workflow?

### ATOM-SOURCE-20260217-009-0013
**Lines**: 120-128
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> To ensure a Claude skill works, track benchmarks such as: skill loading automatically 90% of the time, task completion in fewer steps, and successful API calls without retries. Observe if users avoid asking 'what do I do next?', if results are consistent, and if new users succeed on the first try.

### ATOM-SOURCE-20260217-009-0014
**Lines**: 130-139
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> A Claude skill folder must have `SKILL.md` spelled exactly, use dashes for folder names (e.g., `email-campaign-builder`), and should not contain a `README.md` inside the skill folder.

### ATOM-SOURCE-20260217-009-0015
**Lines**: 141-150
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> The YAML frontmatter in `SKILL.md` determines if Claude loads a skill, requiring a `name` (lowercase, dashed, matching folder name) and a `description` (under 1024 characters, stating what the skill does and when to use it, including trigger phrases).

### ATOM-SOURCE-20260217-009-0016
**Lines**: 143-149
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To test skills, you can use manual testing (fast, no setup, good for early iteration), scripted testing (write test cases in Claude Code for repeated runs), or API testing (build full evaluation suites for systematic tests against benchmarks).

### ATOM-SOURCE-20260217-009-0017
**Lines**: 152-154
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When developing a skill, focus on getting Claude to succeed on one hard task first, then extract what worked into the skill, as this is faster than trying to handle everything at once.

### ATOM-SOURCE-20260217-009-0019
**Lines**: 176-183
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The built-in `skill-creator` skill can generate `SKILL.md` structures for new skills and review existing skills for issues like vague descriptions, missing error handling, or structural problems.

### ATOM-SOURCE-20260217-009-0020
**Lines**: 187-196
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To troubleshoot skill loading issues: if a skill doesn't load when it should, add specific keywords to the description; if it loads for everything, add negative triggers like 'Do NOT use for general Y queries'; if it loads but fails, add more specifics, error handling, and break down complex steps.

### ATOM-SOURCE-20260217-009-0023
**Lines**: 216-219
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To share a skill, put it on GitHub in a public repo with a README explaining its function, include screenshots, and link to it from any related MCP documentation.

### ATOM-SOURCE-20260217-009-0024
**Lines**: 232-238
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When positioning a skill, talk about outcomes rather than features; for example, instead of listing SQL templates, describe how the skill turns '2 hours of manual SQL work into 30 seconds' by allowing natural language queries.

### ATOM-SOURCE-20260217-009-0029
**Lines**: 300-302
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> When troubleshooting a skill that won't upload due to a "Could not find SKILL.md" error, rename the file to exactly `SKILL.md` (case matters).

### ATOM-SOURCE-20260217-009-0030
**Lines**: 303-313
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> When troubleshooting a skill that won't upload due to an "Invalid frontmatter" error, check the YAML syntax for issues like missing dashes or unclosed quotes.

### ATOM-SOURCE-20260217-009-0031
**Lines**: 315-319
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.80

> If a skill never loads, add specific trigger phrases to its description that users would actually say, and test by asking Claude "When would you use the [skill name] skill?" to see if Claude understands its purpose.

### ATOM-SOURCE-20260217-009-0032
**Lines**: 321-325
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.80

> If a skill loads for everything, add boundaries to its description, specifying what it is for and what it is NOT for (e.g., "Use for X. Do NOT use for general Y questions.").

### ATOM-SOURCE-20260217-009-0033
**Lines**: 327-332
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.80

> If a skill loads but doesn't follow instructions, move detailed documentation to a `references/` folder, keep `SKILL.md` under 5,000 words focused on the core workflow, put critical instructions at the top with clear headers, and use a script for validation that must work every time.

### ATOM-SOURCE-20260217-009-0034
**Lines**: 334-338
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> If MCP calls keep failing, verify that the MCP server is connected via Claude.ai Settings > Extensions, and test the MCP independently by asking Claude to use the service to fetch data.

### ATOM-SOURCE-20260217-009-0035
**Lines**: 340-344
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.80, epistemic_stability=0.80

> To improve slow skill performance, move documentation to `references/` and link to it, keeping only essential instructions in `SKILL.md`, and check if more than 50 skills are enabled, as this can slow things down.

### ATOM-SOURCE-20260217-009-0036
**Lines**: 355-358
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Before building a skill, identify 2-3 main use cases, understand necessary tools, and review similar example skills.

### ATOM-SOURCE-20260217-009-0037
**Lines**: 359-364
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> During skill building, ensure the folder is named with dashes, `SKILL.md` is spelled exactly right, YAML frontmatter has proper `---` delimiters, and the description includes both what the skill does and when to use it, with specific and actionable instructions.

### ATOM-SOURCE-20260217-009-0038
**Lines**: 365-370
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> Before sharing a skill, test it with obvious trigger phrases and paraphrased requests, verify it doesn't trigger on random topics, run through the full workflow, and check error handling.

### ATOM-SOURCE-20260217-009-0039
**Lines**: 371-375
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> After deploying a skill, monitor actual usage, collect feedback, iterate on the description and instructions, and update the version number.

### ATOM-SOURCE-20260217-009-0040
**Lines**: 378-379
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> When defining YAML for a skill, `name` and `description` are required, while `license`, `allowed-tools`, and `custom metadata` are optional.

### ATOM-SOURCE-20260217-009-0041
**Lines**: 385-385
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> For skill security, avoid XML brackets (`<>`) and do not use "claude" or "anthropic" in skill names.
