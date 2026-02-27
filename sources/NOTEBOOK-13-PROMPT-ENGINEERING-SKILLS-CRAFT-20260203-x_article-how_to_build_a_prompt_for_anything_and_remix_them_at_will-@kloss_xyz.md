---
url: https://x.com/kloss_xyz/status/2018951817892442260
author: klöss (@kloss_xyz)
captured_date: 2026-02-03
---

# How to Build a Prompt for Anything (and Remix Them at Will)

(Description: An isometric technical illustration featuring two hands assembling an abstract 3D geometric structure with wireframe grid overlay, rendered in grayscale line art style)

I've written a few articles now. This might be my most valuable one though. "Why You Suck at Prompting" for LLM chats and "Why You Suck at Vibe Coding" for agentic engineering both came down to a simple system. And it's gone viral. Hundreds of thousands of views, thousands of bookmarks, and a lot of people realizing they've been typing fucking wishes into AI instead of engineering behavior or a system. If you haven't read them, go read them.

Those articles told you why your prompts suck and frankly why you're shit at vibe coding. This one gives you the construction method to be a fucking superhero. And I'm not kidding either. I'll give you the actual framework for free. The system I use to build every prompt I write, regardless of what it's for.

By the end of this, you won't need to copy paste anyone's prompts ever again if you don't want to. You'll want to build and remix your own. For anything. And you will feel like Tony Stark. You just don't know it yet.

## 1. Stop Copy-Pasting Prompts

The internet is full of "Top 50 ChatGPT Prompts" threads. People bookmark them, paste them in, a lot of the times get mid results, and then move on.

Here's the problem: a prompt built for someone else's use case, with someone else's context, for someone else's output, will never work as well as one you built or remix yourself. And it's also not my job to tell you that. It's your job to figure it the fuck out. But I'm telling you it anyways. Because I love you. What you're doing right now is like wearing someone else's prescription glasses. Technically functional, practically useless. Your context and setup matter for any prompt setup even if someone shares something valuable.

The fix isn't finding more prompts to copy. The fix is learning how to build and how to remix them at will.

What you need is system architecture, not a bookmark library you rarely visit.

## 2. The XML Tag System

Most people prompt in plain english paragraphs. That works for simple questions. It falls completely apart for anything remotely complex.

The problem is ambiguity. When you write a paragraph, the model has to guess where the role ends and the task begins, where the constraints are, what the output should look like, and if there's any context or memory related. Every guess is a potential hallucination.

XML tags eliminate guessing. They create labeled containers that tell the model exactly what each piece of information is and how to use it.
```xml
<role> Who you are </role>
<mission> What you do </mission>
<rules> How you behave </rules>
```

The model doesn't have to interpret structure. The structure is explicit. Each tag is a boundary. Each boundary is a decision you made so the model doesn't have to. This isn't theory. @AnthropicAI (the company behind @claudeai) uses XML tags in their own system prompts. It's how the model is designed to parse structured instructions.

## 3. The Core Tags

These are the tags you'll use in almost every prompt. Think of them as the foundation. Most prompts need all of these. Some can skip one or two depending on the use case.

### `<role>`

This is who the model becomes. Not a vague personality. A specific expert with specific experience.

**Bad:**
```xml
<role> You are a helpful assistant. </role>
```

That's nothing. The model defaults to "helpful assistant" anyway. You've added zero information. 

**Good:**
```xml
<role> You are a senior brand strategist with 15 years of experience building consumer brands from zero to acquisition. You specialize in positioning, messaging architecture, and competitive differentiation. </role>
```

The role tag sets the lens everything else is filtered through. A code reviewer and a creative writer will interpret the same mission completely differently. The role is the foundation that every other tag builds on.

The more specific the role, the less the model guesses. "Marketing expert" is a guess. "Senior brand strategist specializing in positioning and messaging architecture" is a constraint.

### `<mission>`

This is what the model actually does. Not a description. A directive.

**Bad:**
```xml
<mission> Help the user with their writing. </mission>
```

**Good:**
```xml
<mission> Analyze the user's draft and provide specific, actionable feedback on structure, clarity, and persuasion. Identify the three weakest points and rewrite them as examples. Do not rewrite the entire piece. The user must do the work. </mission>
```

The mission defines your scope. What goes in, what comes out. What the model does, and what it doesn't do. A prompt without a clear mission is a prompt that will do whatever the fuck it wants. And "whatever it wants" is usually generic.

### `<rules>`

Rules are behavioral. They control how the model acts, not what it produces.
```xml
<rules> 
Never assume context the user hasn't provided. If information is missing, ask. Do not give generic advice. Every recommendation must be specific to the user's situation. If the user's idea has a fatal flaw, say so directly. Do not soften bad news. Do not use bullet points unless the user specifically asks for them. 
</rules>
```

Rules prevent the model's worst behavioral habits. Every model has default rails it falls back on. Bullet points when you wanted natural written English. Randomly building out code when you wanted a prompt. Assumptions made when you wanted an app idea interrogation instead. Rules are how you override those defaults.

Think of rules as the "never do this" and "always do this" layer. They're the guardrails that keep the model on the road you built.

### `<constraints>`

Constraints are hard limits. They define the boundaries of the output itself.
```xml
<constraints> 
Response must be under 280 characters. Do not reference competitors by name. All recommendations must be implementable within 30 days. Output must be in American English. 
</constraints>
```

**Rules vs constraints:** Rules govern your model behavior. Constraints govern your model's output. "Don't assume" would be a rule. "Keep it under 300 words" would be a constraint. And the distinction matters because the model processes them differently. Rules shape how models think. Constraints shape what models produce.

### `<output_format>`

The most overlooked tag. Most people describe what they want, but never describe what it looks like.
```xml
<output_format>
Return a single paragraph of no more than 3 sentences summarizing the core finding. Follow with a confidence score from 1-10. If confidence is below 7, add a line explaining what additional information would raise it.
</output_format>
```

Without output format, you get whatever the hell the model feels like giving you in that moment. Sometimes that's a paragraph. Sometimes it's a 500-word essay with bullet points. Sometimes it's a list when you wanted a narrative.

Output format is the difference between "write me something about this" and "give me exactly this, in exactly this shape." This tag turns your prompt from a request into specs.

Watch how the same prompt changes with different output formats:

Same role, same mission, but:

- `<output_format>One sentence.</output_format>` gives you a headline.
- `<output_format>A 3-paragraph executive summary.</output_format>` gives you a brief.
- `<output_format>A detailed report with sections and subheadings.</output_format>` gives you a document.
- `<output_format>JSON with keys: summary, confidence, next_steps.</output_format>` gives you structured data.

The model didn't change at all. Your control over output format did.

### `<examples>`

The single most powerful and most underused tag. One good example teaches the model more than a paragraph of instructions.
```xml
<examples>
<example>
<user>Review this headline: "We Make Great Software"</user>
<response>
SCORE: 3/10
PROBLEM: Generic value prop. "Great" means nothing. No specificity, no differentiation, no urgency.
REWRITE: "Ship 3x faster with AI that writes your test suite."
REASONING: Specific outcome (3x faster), specific mechanism (AI test suite), specific audience (developers who ship).
</response>
</example>
</examples>
```

The example doesn't just show the model what you want. It shows the model the format, the depth, the tone, the structure, and the reasoning all at once. No amount of written instructions replicates what a single concrete example communicates.

Two examples is usually enough. Three is overkill for most prompts. The goal isn't comprehensive coverage. It's calibration. This is obviously different with something like Clawdbot/Moltbot/OpenClaw as here we're talking prompting a LLM to make you a prompt, whereas OpenClaw has persistent contextual memory and the more examples, the better. I will write a separate article on that.

## 4. The Advanced Tags

Core tags handle 80% of your prompting, while the advanced tags handle the other 20% (the prompts that need more precision, interactivity, or domain awareness).

You don't use all of these in every prompt. You reach for them when the core tags aren't enough.

### `<context>`

This is background information the model needs before it acts. This is separate from the mission because context is reference material, not a directive.
```xml
<context>
The user is a SaaS founder with $2M ARR, 15 employees, selling to mid-market companies. They are preparing for Series A fundraising in the next 6 months. Their product is a workflow automation tool.
</context>
```

Context sets the stage for the model. Without it, the model gives generic advice for a generic person. With it, every response is calibrated to the user's actual situation at hand.

When to use it: any time the model needs to know something about the user, the project, the industry, or the situation before it starts working.

### `<persona>` and `<tone>`

Role defines expertise. Persona defines personality. Tone defines emotional register.
```xml
<persona> 
Direct, no-nonsense communicator. Uses short sentences. Avoids corporate jargon. Speaks like a founder who's built and sold companies, not a consultant who's read about it.
</persona>

<tone>
Confident but not arrogant. Blunt but not rude. Supportive when the user is on the right track. Honest when they're not.
</tone>
```

These are separate from role on purpose. A "senior financial analyst" (role) could be warm and encouraging or cold and clinical. The role doesn't determine the voice. Persona and tone do.

When to use them: any time you need the model to communicate in a specific way that the role alone doesn't capture. Writing prompts, coaching prompts, and brand voice prompts as example.

### `<audience>`

Who the output is for. This shifts vocabulary, depth, and assumed knowledge.
```xml
<audience>
Non-technical founders who have never written code. They understand business metrics but not technical architecture. Assume zero programming knowledge. Use business analogies, not technical ones.
</audience>
```

The same explanation of a building out an API looks completely different for a developer vs a CEO vs a student. Audience is the tag that helps control that.

When to use it: any time the model's output is going to be read by someone other than you, or when you need the model to calibrate complexity.

### `<knowledge>`

Domain-specific information injected as reference. Different from context because knowledge is factual material, not situational background.
```xml
<knowledge>
Our pricing tiers are: Starter ($29/mo, 1 user), Growth ($99/mo, 5 users), Enterprise ($299/mo, unlimited). Our main competitors are Tool A (cheaper, fewer features) and Tool B (more expensive, enterprise-focused). Our differentiator is real-time collaboration, which neither competitor offers.
</knowledge>
```

When to use it: any time the model needs specific facts, data, or institutional knowledge to do its job. Product info, company policies, technical specifications, pricing structures.

### `<method>` or `<steps>`

A sequenced process the model follows. Not "do these things." More like "do them in this order, and don't skip ahead."
```xml
<method>
1. Read the user's input completely before responding.
2. Identify the core question or problem. State it back in one sentence.
3. Check if any critical information is missing. If so, ask before proceeding.
4. Provide your analysis in the format specified in output_format.
5. End with one follow-up question that would deepen the analysis.
</method>
```

Method is powerful for complex workflows where order matters. Analysis prompts, debugging prompts, research prompts. Anything where step 3 depends on step 2.

When to use it: any time the model needs to work through a process rather than just produce an output.

### `<anti_patterns>`

The "don't do this" tag, but with teeth. Instead of just saying "don't do X," you show what bad output looks like so the model can avoid it.
```xml
<anti_patterns>
BAD: "There are many factors to consider when evaluating this opportunity."
WHY: Vague filler. Says nothing. Wastes the reader's time.

BAD: "On one hand... on the other hand..."
WHY: Fence-sitting. The user asked for a recommendation, not a debate.

BAD: Starting any response with "Great question!"
WHY: Sycophantic filler. Just answer the question.
</anti_patterns>
```

Anti-patterns are more effective than rules for specific failure modes models are susceptible to. A rule tells the model "don't be vague." An anti-pattern shows exactly what vague looks like. The model can pattern-match against concrete examples much better than abstract instructions.

When to use them: when the model keeps producing a specific type of bad output that rules alone haven't fixed.

### `<fallback>`

What the model should do when it can't complete the task. With this, the model cannot hallucinate an answer or give you a useless "I'm not sure."
```xml
<fallback>
If you don't have enough information to give a confident answer, say "I need more information" and list exactly what's missing. If the question is outside the scope of this role, say so and suggest what type of expert the user should consult. Never guess. Never make up data. Never fabricate sources.
</fallback>
```

When to use it: any prompt where wrong answers are worse than no answers. Financial analysis, medical information, legal review, technical recommendations.

### `<evaluation>`

Self-check criteria. The model reviews its own output before delivering it.
```xml
<evaluation>
Before responding, verify:
- Does this directly answer the user's question? If not, refocus.
- Is every claim specific and actionable? If anything is vague, rewrite it.
- Would a busy person find this useful in under 60 seconds? If not, cut.
- Are there any assumptions? If so, flag them explicitly.
</evaluation>
```

Evaluation is like giving the model a quality assurance (QA) checklist. It forces a second pass before the output reaches you.

When to use it: any prompt where quality consistency really really matters. Client facing work, content production, analysis, recommendations, apps.

### `<discovery_engine>`

Questions the model asks the user before acting. This is the tag behind my viral app idea interrogation prompt.
```xml
<discovery_engine>
Before doing any work, ask the user:
1. What specific outcome do you need from this?
2. Who is the audience for the final output?
3. What constraints am I working within (length, format, tone)?
4. What have you already tried that didn't work?
5. Is there anything I should absolutely not do?

Wait for all answers before proceeding.
</discovery_engine>
```

This tag flips the dynamic. Instead of the user providing everything upfront and hoping they didn't miss anything, the model extracts what it needs. It's the difference between filling out a form and having a conversation with an expert.

When to use it: any prompt where the user's initial input is likely incomplete. Consulting prompts, strategy prompts, creative briefs, project scoping.

### `<chain>`

Links prompts together. The output of one becomes the input of the next.
```xml
<chain>
This prompt is Step 2 of 3.
INPUT: You will receive a structured requirements document (output of Step 1).
YOUR JOB: Convert the requirements into a technical architecture document.
OUTPUT: Your output will be fed into Step 3, which generates the implementation plan. Do not include implementation details. That's Step 3's job.
</chain>
```

When to use it: multi-step workflows where each prompt handles one phase. Research → analysis → recommendation. Draft → critique → revision. Interrogation → documentation → implementation.

## 5. Choosing Your Tags

Not every prompt needs every tag. This is important. Here's how to think about it:

**Simple task** (summarize this, rewrite that, answer this question): `<role>` + `<mission>` + `<output_format>`

**Professional output** (client deliverable, published content, formal analysis): `<role>` + `<mission>` + `<rules>` + `<constraints>` + `<output_format>` + `<examples>`

**Interactive/conversational** (coaching, consulting, brainstorming): `<role>` + `<mission>` + `<rules>` + `<discovery_engine>` + `<fallback>`

**Complex workflow** (multi-step analysis, research, production pipeline): All core tags + `<method>` + `<evaluation>` + `<chain>` + `<anti_patterns>`

Start with the core tags. Add advanced tags only when you hit a specific problem that you really need to solve. A prompt with six tags that are all doing great work is better than a prompt with twelve tags where half are mid.

## 6. Full Prompt: Voice Style Extractor

Here's the framework in action. This prompt takes any writing sample and reverse engineers the author's voice into a reusable system prompt. Useful for content creators, ghostwriters, or anyone who needs to maintain a consistent voice across AI-generated content.
```xml
<role>
You are a linguistic forensics analyst who specializes in deconstructing writing styles. You identify the specific, measurable patterns that make a writer's voice distinct, not vague descriptions like "conversational" or "professional," but the actual structural and tonal mechanics.
</role>

<mission>
The user will provide a writing sample. Your job is to extract every identifiable pattern of the author's voice and produce a reusable style profile that another AI (or the same AI in a future session) can use to replicate that voice accurately.
</mission>

<method>
1. Read the entire sample before analyzing anything.
2. Identify patterns across these dimensions:
   - Sentence structure (length distribution, rhythm, fragments vs complex sentences)
   - Vocabulary level (grade level, jargon density, word choice patterns)
   - Punctuation habits (em dashes, ellipses, periods for emphasis, comma density)
   - Paragraph structure (length, transitions, standalone lines)
   - Rhetorical devices (repetition, direct address, questions, callbacks)
   - Tone markers (authority level, humor type, emotional register)
   - Formatting preferences (headers, lists, bold, line breaks)
   - What they never do (equally important as what they do)
3. Synthesize into a style profile structured as a system prompt.
</method>

<rules>
Never describe style with vague adjectives. "Conversational" is not a pattern. "Uses sentence fragments for emphasis, averages 8 words per fragment, deploys them after longer complex sentences to create rhythmic contrast" is a pattern. Every observation must be supported by at least two examples from the sample. If the sample is too short to identify a pattern reliably, flag it as "insufficient data" rather than guessing.
</rules>

<anti_patterns>
BAD: "The author has a casual, engaging tone."
WHY: Meaningless. Every content creator thinks they have a casual engaging tone.

BAD: "The writing is clear and concise."
WHY: Describes quality, not mechanics. How is it clear? Short sentences? Active voice? Concrete nouns?
</anti_patterns>

<output_format>
Return two sections:

ANALYSIS: A detailed breakdown of every pattern identified, organized by dimension, with examples quoted from the source material.

STYLE PROMPT: A complete, copy-paste-ready system prompt that begins with <role> and captures the voice so precisely that output written using it would be indistinguishable from the original author to a careful reader. This prompt should use XML tags following the same framework taught in this article.
</output_format>

<examples>
<example>
<user>Analyze this: "Let's get this out of the way: You don't suck at prompting because you're dumb. You suck because you think prompting is asking nicely instead of engineering behavior."</user>
<response>
ANALYSIS:
Sentence structure: Opens with a short imperative setup ("Let's get this out of the way:") followed by a two-part construction that mirrors then subverts. First sentence is a negative ("not because X"), second is the real thesis ("because Y"). Creates tension then resolution.

Direct address: Uses "you" immediately. Makes the reader the subject, not a passive observer.

Word choice: "Suck" is deliberately informal, lowering the register to feel like peer-to-peer, not teacher-to-student... [continues across all dimensions]
</response>
</example>
</examples>
```

**Why this prompt works (framework breakdown):**

The `<role>` is specific: "linguistic forensics analyst." Not "writing expert." The specificity tells the model exactly what lens to use.

The `<method>` forces sequenced analysis. Read first, then identify, then synthesize. Without it the model tries to do all three at once and misses patterns.

The `<anti_patterns>` prevent the most common failure mode: vague style descriptions that sound insightful but are actually useless for replication.

The `<output_format>` demands two deliverables: the analysis (so you can verify it's accurate) and the style prompt (so you can use it immediately).

The `<examples>` section shows the depth expected. One example calibrates the model more than any amount of written instructions.

## 7. Full Prompt: Keyword & Sentiment Search Engine

This prompt turns your AI into a research analyst that monitors conversations around specific topics, accounts, or keywords and reports on sentiment, patterns, and actionable insights.
```xml
<role>
You are a social intelligence analyst specializing in real-time discourse analysis. You monitor public conversations across platforms to extract signal from noise: what people actually think, what's shifting, what's emerging, and what's being ignored.
</role>

<mission>
The user will provide keywords, account names, topics, or a combination. Your job is to search for and analyze the current public discourse around those inputs. Deliver a structured intelligence brief the user can act on immediately.
</mission>

<context>
This is used for market research, brand monitoring, competitive intelligence, and content strategy. The user needs to understand what people are saying, how they feel about it, and what opportunities or risks exist in the conversation.
</context>

<method>
1. Search for the provided keywords/accounts/topics across available sources.
2. Categorize findings by sentiment: positive, negative, neutral, mixed.
3. Identify the dominant narratives (what are most people saying?).
4. Identify outlier narratives (what are few people saying that might matter?).
5. Flag any emerging shifts (is sentiment changing? is a new angle gaining traction?).
6. Assess volume and velocity (how much conversation, is it growing or fading?).
7. Extract actionable insights (what should the user do with this information?).
</method>

<rules>
Distinguish between loud minority opinions and actual consensus. 10 angry tweets is not "widespread backlash." Never present sentiment as fact without volume context. "Negative sentiment" means nothing without "across X posts over Y timeframe." If data is insufficient to draw conclusions, say so. Do not extrapolate from thin data. Always separate what people are saying from what they mean. Surface-level complaints often mask deeper issues.
</rules>

<constraints>
All analysis must be based on publicly available information. Do not speculate on private motivations of individuals. Do not present AI-generated summaries as direct quotes. Flag the difference between verified accounts and general public discourse.
</constraints>

<output_format>
TOPIC: [what was analyzed]
TIMEFRAME: [when]
VOLUME: [how much conversation]
VELOCITY: [growing/stable/declining]
SENTIMENT BREAKDOWN:
- Positive (X%): [dominant positive themes]
- Negative (X%): [dominant negative themes]
- Neutral (X%): [informational/factual mentions]
KEY NARRATIVES:
1. [Most common narrative + example]
2. [Second most common + example]
3. [Emerging/outlier narrative worth watching]
ACTIONABLE INSIGHTS:
- [What to do based on this data]
- [What to watch for next]
- [What opportunity exists]
GAPS:
- [What data was insufficient]
- [What would improve this analysis]
</output_format>

<evaluation>
Before delivering:
- Is every percentage tied to actual volume data?
- Are narratives supported by multiple data points, not single posts?
- Are insights genuinely actionable or just observations?
- Have I flagged what I don't know?
</evaluation>
```

**Why this prompt works (framework breakdown):**

The `<context>` tag does critical work here. Without it, the model doesn't know if you're doing brand monitoring, competitive research, or academic analysis. Same keywords, but a completely different analytical lens.

The `<method>` creates a 7-step analytical process. This prevents the model from jumping to conclusions. It has to categorize, then identify narratives, then check for shifts, then assess volume, then extract insights. Each step builds on the previous one.

The `<rules>` prevent the biggest sin in sentiment analysis: treating noise as signal. The rule about "10 angry tweets is not widespread backlash" is doing real work because models love to overweight negative sentiment.

The `<evaluation>` tag forces a self-check. The model has to verify its own percentages are backed by data before delivering. This catches hallucinated statistics.

The `<output_format>` is not flexible by design. Intelligence briefs need consistent structure so you can compare them across time periods and topics. The GAPS section is arguably the most important: it tells you what the model couldn't find, which is often more valuable than what it could.

## 8. Full Prompt: The Idea Interrogator

If you follow me, you've probably seen this one. It's the prompt behind the viral tweet. The one that forces AI to tear apart your app or coding idea before writing a single line of code or documentation.

Here's the full version, built on the same framework you just learned.
```xml
<role>
You are a ruthless requirements interrogator. You do not build. You do not code. You do not suggest solutions. You do not generate documentation. You ask questions until there is nothing left to assume.
</role>

<mission>
The user will describe an app, product, or project idea. Your job is to meticulously and exhaustively interrogate them about every detail, decision, design choice, edge case, constraint, and dependency until zero assumptions remain. Do not generate any code, documentation, plans, or recommendations during this phase. Only ask questions. When you believe every assumption has been eliminated, present a complete summary of everything you've learned and ask the user to confirm nothing is missing.
</mission>

<discovery_engine>
Begin by asking every question you need. Do not hold back. Do not pace yourself. Ask everything upfront. Cover at minimum:
- Core problem being solved and for whom
- User types, roles, and permissions
- Every screen, flow, and interaction
- Data: what's stored, where, who can access it
- Authentication and authorization model
- Third-party services and integrations
- Edge cases and error states
- Performance and scale expectations
- Platform targets (web, mobile, desktop)
- Design preferences and constraints
- Budget and timeline realities
- What success looks like, quantified

Then go deeper on every answer that contains ambiguity.
</discovery_engine>

<rules>
Never assume. Never infer. Never fill gaps with "reasonable defaults." If an answer is vague, push back. "Something modern" is not a tech stack. "Users can log in" is not an auth model. "Clean design" is not a spec. When you think you're done, you're probably not. Ask what you might have missed. The goal is not speed. The goal is zero assumptions.
</rules>

<anti_patterns>
BAD: Accepting "I'll figure that out later" as an answer.
WHY: That's an assumption wearing a disguise. If it matters enough to mention, it matters enough to define.

BAD: Suggesting solutions mid-interrogation.
WHY: The moment you suggest, the user anchors to your suggestion instead of thinking through their own requirements.

BAD: Asking one question at a time.
WHY: This isn't a therapy session. The user has an idea in their head. Extract all of it as efficiently as possible so they can see the full picture.
</anti_patterns>

<fallback>
If the user says "I don't know" to a question, do not skip it. Instead:
1. Explain why the question matters.
2. Give 2-3 common approaches others have taken.
3. Ask them to pick one or table it as an explicit open question.

No unresolved ambiguity gets swept under the rug.
</fallback>

<output_format>
After interrogation is complete, deliver:

REQUIREMENTS SUMMARY
Organized by category (users, features, data, auth, integrations, design, infrastructure, constraints).

CONFIRMED DECISIONS
Every explicit decision the user made during interrogation.

OPEN QUESTIONS
Anything still unresolved, with a note on why it matters and when it needs to be decided.

ASSUMPTIONS LOG
If any assumptions were unavoidable, list them explicitly so they can be validated later.

End with: "Review this summary. If anything is wrong, missing, or needs to change, tell me now. This becomes the foundation for everything built after it."
</output_format>
```

**Why this prompt works (framework breakdown):**

The `<role>` is deliberately narrow. "You do not build. You do not code. You do not suggest." Each sentence removes a behavior. Without these explicit contradictions, the model will try to be helpful by offering solutions or randomly start coding, which defeats the entire purpose.

The `<discovery_engine>` is the heart of this prompt. It tells the model to ask everything upfront, not drip-feed questions. That's a deliberate design choice. You want the full picture extracted in one pass so the user can see the scope of their idea as well as waste less model compute in a session.

The `<anti_patterns>` section targets the three most common ways this prompt fails: accepting vagueness, suggesting instead of asking, and pacing questions too slowly. Each one is a behavior the model naturally defaults to that this prompt has to override.

The `<fallback>` handles the "I don't know" problem. Instead of skipping the question, the model explains why it matters and gives options. This turns "I don't know" into a decision point instead of a dead end.

The `<output_format>` delivers four distinct sections, each serving a different purpose. The requirements summary is the document. The confirmed decisions are your audit trail. The open questions are the to-do list. The assumptions log is the risk register. Together they give you a complete foundation to build from.

## 9. Debugging Your Prompts

Your prompt isn't working. Maybe something's off. Here's how to figure out which tag is the problem:

**Output is generic or shallow:** Your `<role>` is too vague. Make it more specific. Add years of experience, a specialization, or maybe a domain. The more specific the role, the less generic the output. Have fun with this one.

**Output is wrong format:** Your `<output_format>` is missing from the equation or too loose. If you wanted a .csv or .md and got paragraphs instead, that's not the model's fault. Specify exactly what the output should look like.

**Output ignores your instructions:** Your `<rules>` or `<constraints>` are buried or contradictory. Move them earlier in the prompt. Make them shorter and more direct. Check if any rules conflict with each other.

**Output is playing it safe or sugarcoating everything:** You'll want to add an `<anti_patterns>` section with explicit examples of the hedging behavior. Show the model what you don't want.

**Output misses the point:** Your `<mission>` is ambiguous. If you can read your mission statement and imagine three different interpretations, the model will pick one at random. Tighten it until there's only one possible reading of it.

**Output makes up facts:** Add a `<fallback>` tag. Tell the model what to do when it doesn't know something. Without fallback instructions, the model's default is to guess confidently.

**Output is inconsistent across runs:** Add `<examples>`. Nothing stabilizes output like showing the model what good looks like. One example is worth a hundred words of instructions.

**Output is right but the process is wrong:** Add a `<method>` tag with explicit steps. The model might arrive at the right answer by the wrong path, which means it'll get the wrong answer next time. Your method ensures the process is repeatable and scalable.

## 10. Build and Remix Your Own

You now have the system. Every tag, what it does, when to use it, and how it breaks when you don't.

The framework is the same whether you're building a prompt for coding review, voice extraction, content writing, SEO strategy, data analysis, meal planning, or literally whatever else you can likely think of. The tags don't change, the content inside them does.

Now you can copy, build, and remix prompts at will. Go make them your own. You are Tony Stark now. Go build your Jarvis.

And if you want me to share my 50+ AI use cases and prompts built on this exact framework, that's coming in a little bit. Stay tuned for more.

If you made it this far, you now know more about prompt construction than 99% of people using AI daily. This isn't a secret. It's a system. And now it's yours.

Follow me for more: [@kloss_xyz](https://x.com/kloss_xyz)