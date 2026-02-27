---
url: https://x.com/ArmanHezarkhani/status/2024499196993101927
author: "Arman Hezarkhani (@ArmanHezarkhani)"
captured_date: 2026-02-19
id: SOURCE-20260219-003
original_filename: "20260219-x_article-the_complete_guide_how_to_write_with_ai_slop_free-@armanhezarkhani.md"
status: triaged
platform: x
format: article
creator: armanhezarkhani
signal_tier: tactical
topics:
  - prompt-engineering
  - ai-workflow
  - prompting
  - extended-thinking
  - cursor
  - gpt
  - rag
teleology: implement
notebooklm_category: prompt-engineering
aliases:
  - "The Complete Guide How to Write with AI Slop Free"
synopsis: "The Complete Guide: How to Write with AI, Slop Free Introduction 90% of what I write is done with AI tools. That distinction matters, and its the unlock for efficiency. I use the same tools software engineers use to write code—Claude Code, Cursor, Wispr Flow—except I point them at prose instead of Python."
key_insights:
  - "They've learned how to direct AI precisely—spec the output, constrain the behavior, iterate on feedback, never ship what they can't explain."
  - "- **Iterate on feedback** — First draft is never final."
  - "The golden rule for AI-assisted writing is the same as Ad."
---
# The Complete Guide: How to Write with AI, Slop Free
(Description: Dark-themed banner image featuring a golden hand holding a pen against a circuit board pattern background with the text "No More Slop" in large white serif font, and subtitle "The Complete Guide: How to Write with AI, Slop Free")
## Introduction
90% of what I write is done with AI tools.
Not written BY AI.
Written WITH AI.
That distinction matters, and its the unlock for efficiency.
I use the same tools software engineers use to write code—Claude Code, Cursor, Wispr Flow—except I point them at prose instead of Python. The workflow is identical: define the spec, build iteratively, review every line, ship when it's ready.
The result is content that sounds like me, performs well on X, and takes a fraction of the time it used to.
Most people use AI for writing and get slop. Generic, lifeless paragraphs that read like a corporate FAQ. The kind of content you scroll past without registering.
Engineers don't have this problem with code. They've learned how to direct AI precisely—spec the output, constrain the behavior, iterate on feedback, never ship what they can't explain.
That same discipline applies to writing. Engineers are already using these tools to write code. You can use them to write viral and thoughtful content.
Here's everything I've learned.
## What Is Slop?
AI slop is content that technically answers a prompt but has no soul. You've seen it everywhere. You've probably written some.
The telltale signs:
- Opens with "In today's fast-paced world" or "In the ever-evolving landscape"
- Every paragraph is exactly 3-4 sentences
- Bullet points all start with gerunds ("Leveraging," "Streamlining," "Optimizing")
- Uses "delve," "crucial," "game-changer," "it's important to note," and "let's dive in"
- Hedges everything—"This can potentially help you perhaps improve your workflow"
- Sounds like it was written by a committee that's never had an original thought
- Has no specific details, no personal experience, no edge
Slop isn't a tool problem. It's a workflow problem.
People open ChatGPT, type "write me a blog post about X," get 800 words of beige prose, copy-paste it, and publish. That's not writing with AI. That's outsourcing your thinking to a machine that defaults to the most average version of everything.
The fix isn't "don't use AI." The fix is to use AI the way engineers use it—as a collaborator you direct, not an author you defer to.
## The Engineering Mindset
Software engineers don't type "build me an app" and ship whatever comes out. They:
- **Spec the requirements** — What does this need to do? What's the voice, the audience, the goal?
- **Build incrementally** — Get the structure right before adding detail. Skeleton first, polish last.
- **Review everything** — Read every line. If you can't explain why a sentence exists, cut it.
- **Test against criteria** — Does it accomplish the goal? Does it sound like a human wrote it?
- **Iterate on feedback** — First draft is never final. Refine based on what's actually working.
This is the exact workflow for writing with AI. The people who get slop skip steps 1, 3, and 5. The people who get great content follow all five.
The golden rule for AI-assisted writing is the same as Addy Osmani's rule for AI-assisted coding: never publish content you can't explain.
If you read your draft and can't articulate why every paragraph exists and what it's doing—you're not done editing.
## The Toolchain
Here's what I use and why.
### Claude Code: The Core
Claude Code is a terminal-based AI tool that software engineers use to write and edit code across entire projects. It reads your files, understands context, and makes changes directly.
I use it for writing because it does something no chatbot can: it works with your actual files.
Instead of copy-pasting between a chat window and Google Docs, Claude Code reads my drafts, my notes, my previous articles, my style guide—all at once. It has the full context of my writing project, not just the last message I sent.
Why this matters for writing:
- It can read 10 of your previous articles and learn your voice
- It edits your actual markdown files in place—no copy-pasting
- It can reference your notes, research, and outlines simultaneously
- You can say "make this section more like the opening of my MLE article" and it knows what you mean
- CLAUDE.md files let you define your style rules once and have them apply to everything
**Cost:** Requires Claude Pro ($20/mo) or Max ($100-200/mo)
### Cursor: The IDE for Prose
Cursor is an AI-powered code editor. But markdown is just text, and Cursor handles text beautifully.
Open your article as a .md file. Use Cmd+K to rewrite a paragraph. Use the Composer to restructure entire sections. Use Tab completion to finish your thoughts.
Why writers should care:
- Inline editing—highlight a paragraph, describe how to change it, see the diff
- Multi-file context—it can reference your outline, your research notes, and your draft simultaneously
- Composer mode for structural changes across the whole piece
- It shows you exactly what changed (like a code diff) so you can approve or reject each edit
**Cost:** Free tier → Pro $20/mo
### Wispr Flow: Voice to Draft
Wispr Flow is AI dictation that actually works. You talk, it writes clean text. No "um"s, no filler, proper punctuation.
I use it for first drafts. I know what I want to say—I just can't stare at a blank page. So I talk through my ideas while walking, and Wispr turns my rambling into coherent paragraphs.
What makes it different from Apple Dictation:
- It edits as you speak—"let's meet tomorrow, wait, no, Friday" becomes "let's meet Friday"
- Removes filler words automatically
- Adapts to context—casual in Slack, professional in email
- Command Mode lets you edit with your voice—highlight text, say "make this more direct"
- Whisper Mode works at low volume—planes, coffee shops, 2 AM
The workflow: Dictate a rough draft with Wispr → clean it up in Cursor or Claude Code → publish.
**Cost:** Free tier available → Pro starts at $9.99/mo
### The CLAUDE.md: Your Style Guide as Config
This is the most important piece.
In software engineering, a CLAUDE.md file tells Claude Code how to behave in your project—what conventions to follow, what patterns to use, what mistakes to avoid.
For writing, your CLAUDE.md is your voice. It's a config file that encodes your style so every piece of content sounds like you.
Here's what mine looks like:
```markdown
# Writing Style Guide
## Voice
- Conversational, direct, confident
- Short paragraphs (1-3 sentences max)
- Heavy use of em dashes
- Bold declarations, not hedging
- Write like you're explaining to a smart friend, not lecturing
## Structure
- Open with a personal anecdote or bold claim
- Use "That's not what this is" reframes
- Include actual prompts/examples in code blocks
- Label techniques as numbered patterns
- End with TL;DR (bolded key takeaways) and Quick Reference
## Rules
- Never use: "delve," "crucial," "game-changer," "it's important to note," "in today's," "landscape," "let's dive in," "embark," "realm"
- Never hedge. Say "this works" not "this can potentially work"
- No emoji unless explicitly requested
- Every paragraph must earn its existence—cut anything that doesn't add information
- Include specific details only I would know
- Reference real tools, real prices, real experiences
## Anti-Patterns
- No corporate speak
- No filler paragraphs that summarize what you're about to say
- No "In conclusion" or "To sum up"
- Don't start consecutive paragraphs the same way
- Don't explain what something "could" do—show what it does
```
When Claude Code reads this before editing any article, it matches my voice automatically. No more "make it sound more casual" back-and-forth. The rules are encoded once and applied every time.
This is the single biggest leverage point. A well-written CLAUDE.md eliminates 80% of the editing you'd normally do.
## The Workflow
Here's how I write an article from start to finish. This is the actual process, not a simplified version.
### Step 1: Research (30-60 minutes)
I use Claude Code to do deep research on the topic. Not "summarize this for me"—actual research.
```
Research [TOPIC] thoroughly. I'm writing a long-form guide. I need:
1. How the tool/concept actually works (technical detail)
2. What the current best practices are (2025-2026)
3. What most people get wrong
4. Specific examples and use cases
5. Pricing and practical details
6. Current limitations (honest)
Search the web. Read documentation. Find recent articles and discussions. Give me raw material, not a polished summary.
```
This gives me a pile of raw material—facts, quotes, technical details, pricing, limitations. Not a draft. Material.
### Step 2: Outline (15 minutes)
I outline by hand. This is the one step I don't delegate.
The outline is my spec. It defines the structure, the key points, the examples I'll use, and the flow from section to section. I decide what the article argues, what it teaches, and what makes it different from everything else on the topic.
If I can't outline it, I don't understand it well enough to write it.
### Step 3: First Draft (30-60 minutes)
Two options depending on the piece:
**Option A: Dictate with Wispr Flow.**
I talk through each section of my outline. Stream of consciousness. Wispr cleans up the audio into readable text. This works best for opinion pieces and personal stories.
**Option B: Section-by-section with Claude Code.**
I feed the outline and research, then work through each section:
```
Here's my outline and research for this article. Read my CLAUDE.md style guide. Write section 3: [SECTION TITLE]
Key points to cover:
- [point 1]
- [point 2]
- [point 3]
Reference material: [specific facts from research]
Write in my voice. Make it specific and practical— include actual prompts, prices, and examples. Do NOT write generic advice. Every sentence should teach something.
```
I do this section by section. Not the whole article at once. Each section gets written, reviewed, and approved before I move to the next one—just like building features incrementally.
### Step 4: Edit Pass (30-45 minutes)
This is where slop dies.
I read the entire draft out loud. Every sentence that makes me cringe gets rewritten. Every paragraph that doesn't earn its place gets cut.
Then I use Claude Code for targeted edits:
```
Read this draft. Find and fix:
1. Any sentence that sounds like it came from a corporate FAQ
2. Any hedging ("could potentially," "might help," "it's worth noting")
3. Any paragraph that doesn't add new information
4. Anywhere the energy drops
Be aggressive. Cut anything that doesn't need to exist.
```
### Step 5: The Slop Check
Before publishing, I run a final check:
```
Read this article against my CLAUDE.md style guide. Flag any violations.
Check for:
- Banned words and phrases
- Paragraphs longer than 4 sentences
- Sections that feel generic or could apply to any topic
- Missing specific examples or details
- Anywhere I'm telling instead of showing
```
This catches the 5% of slop that survives manual editing. It's like running a linter on your code before committing.
### Step 6: Publish
Ship it. Move the file from in_progress to posted. Done.
## The Anti-Slop Playbook
Here's the difference between content that reads as AI-generated and content that reads as human-written-with-AI-help.
### Pattern 1: Lead with What Only You Know
Slop is generic. The antidote is specificity.
**Slop:**
"AI tools are transforming how we work. Many professionals are finding new ways to be productive."
**Not slop:**
"Three months ago, I spent a weekend building my pregnant wife a 'Tinder for restaurants' app."
The second version can only come from one person. That's the test. If anyone could have written it, it's slop.
The rule: Every article needs at least 3-5 details that only you would know. A personal story. A specific number. A mistake you actually made. A tool you actually use with a price you actually pay.
### Pattern 2: Kill the Hedge
AI defaults to hedging because it's trained to be helpful and not wrong. That makes for terrible writing.
**Slop:**
"Using AI tools could potentially help streamline your writing workflow and may result in improved output quality."
**Not slop:**
"A well-written CLAUDE.md eliminates 80% of the editing you'd normally do."
The fix: After your draft is done, search for these words and kill them: "could," "potentially," "may," "might," "perhaps," "it's worth noting," "it's important to," "arguably." Replace with direct statements.
If you're not confident enough to state something directly, either do more research or cut the claim entirely.
### Pattern 3: Break the Rhythm
AI writes in a metronomic cadence. Every paragraph is 3-4 sentences. Every sentence is 15-20 words. The rhythm never changes.
Human writing breathes.
Sometimes a paragraph is one sentence.
Sometimes it's a longer exploration of an idea that takes multiple sentences to unpack because the concept genuinely requires more space to explain properly—and that's fine, because the previous two paragraphs were short enough to create contrast.
The fix: Vary your paragraph length intentionally. One-sentence paragraphs for emphasis. Longer paragraphs for complex ideas. Never let three consecutive paragraphs be the same length.
### Pattern 4: Use Your Vocabulary, Not AI's
Every AI model has a default vocabulary. You've seen these words a thousand times:
- "Delve" (nobody says this in conversation)
- "Crucial" (say "important" or "critical" like a human)
- "Landscape" (as in "the AI landscape")
- "Embark" (on a "journey," always)
- "Realm" (in the "realm" of)
- "Tapestry" (of ideas, experiences, life)
- "Game-changer" (everything is apparently a game-changer)
- "Leverage" (as a verb)
- "Robust" (solutions are always "robust")
- "Seamless" (integrations are always "seamless")
The fix: Ban these words in your CLAUDE.md. Replace them with how you actually talk. If you wouldn't say it to a friend at dinner, it shouldn't be in your writing.
### Pattern 5: Show, Don't Summarize
Slop loves to tell you what it's about to tell you, tell you, then tell you what it told you. Three layers of meta-commentary around one actual idea.
**Slop:**
"In this section, we'll explore how AI tools can help improve your writing process. Understanding these tools is key to getting better results. Let's look at some examples of how they work."
**Not slop:**
[Just shows the examples. No preamble. No summary. The content speaks for itself.]
The fix: Delete any sentence that describes what you're about to say. Delete any paragraph that summarizes what you just said. Trust your reader. Start with the substance.
### Pattern 6: Include Working Examples
The difference between generic AI advice and useful content is working examples.
**Generic:**
"You can use prompts to get better AI writing output."
**Useful:**
```
Read this draft. Find every instance of passive voice. Rewrite each one in active voice. Show me the before and after. Do not change any sentence that is already active voice.
```
Real prompts. Actual code blocks. Copy-paste-ready material. This is what engineers expect from documentation, and it's what readers expect from a good guide.
## Making AI Match Your Voice
The technical term for getting AI to write like you is "few-shot prompting"—showing it examples of your writing so it can match the pattern.
Here's how to do it systematically.
### Method 1: Feed It Your Best Work
```
Read these 5 articles I've written:
[article 1]
[article 2]
[article 3]
[article 4]
[article 5]
Analyze my writing style. Document:
- Average paragraph length
- Sentence structure patterns
- Vocabulary preferences
- How I open articles
- How I transition between sections
- Phrases I use repeatedly
- What I never do
Save this as a writing style profile.
```
This is the Voice DNA approach. Instead of telling the AI "write casually," you show it what casual looks like when you do it. Two good examples teach more about your voice than a paragraph of instructions.
### Method 2: Iterate Toward Your Voice
Sometimes the first draft is close but not quite right. Instead of rewriting manually, direct the edit:
```
This paragraph is too formal. Make it sound like I'm explaining this to my friend at a bar. Keep the same information, change the delivery.
```
```
Too many long sentences. Break this up. I want a mix of short punchy lines and longer explanations.
```
```
This sounds like ChatGPT wrote it. More edge. More opinions. I'm not hedging—I'm telling people what actually works.
```
### Method 3: The A/B Draft
For important pieces, I generate two versions and pick the better one:
```
Write this section two ways:
Version A: Direct and opinionated
Version B: More measured and analytical
I'll pick which approach works better for this audience.
```
This is how engineers evaluate approaches—build two, test both, keep the winner.
## What the X Algorithm Actually Rewards
Everything I've described so far makes your writing better. But if you're publishing on X, better writing alone isn't enough. You need to understand what the algorithm actually optimizes for.
I pulled X's open-source recommendation algorithm and analyzed the entire codebase. Here's what matters for writers:
### Shares Beat Everything
The algorithm tracks three distinct share types: general shares, DM shares, and link copies. DM shares—when someone sends your post directly to a friend—are likely the strongest positive signal.
**What this means for writers:**
Create content people want to share privately. "Insider knowledge" content. Specific, actionable guides that someone sends to a friend saying "you need to read this." That's exactly what performs.
### Replies Signal Depth
A post that generates genuine conversation scores higher than one that gets liked and scrolled past.
**What this means for writers:**
End sections with genuine questions. Make slightly contrarian takes. Share incomplete thoughts that invite completion. Don't write for passive consumption—write to start a conversation.
### Follows Are the Ultimate Signal
When someone reads your content and follows you, that's the strongest possible endorsement. The algorithm weights this heavily.
**What this means for writers:**
Include personality, not just information. Let your voice be distinctive enough that people think "who is this person?" and click your profile. Generic content doesn't earn follows—specific, opinionated, useful content does.
### Dwell Time Is Real
The algorithm measures how long people look at your post. Both a binary "did they pause?" and the actual seconds spent.
**What this means for writers:**
Information density matters more than word count. Write content that rewards close reading. Multi-image posts that require swiping. Threads with substance in every tweet.
### What Doesn't Matter
The algorithm has no signal for hashtags, post length, follower count, verification status, time of day, or keywords. It doesn't analyze your content—it predicts how people will respond to it.
**What this means for writers:**
Stop optimizing for things the algorithm doesn't track. No hashtag strategies. No "best time to post" hacks. Focus entirely on creating content that generates the engagement signals the algorithm actually measures.
### The Author Diversity Penalty
Post twice in quick succession and your second post gets roughly 55% of the first post's score. Third post drops to 32%. Space your posts 2-4 hours apart.
**What this means for writers:**
Quality over quantity. One great piece per day beats five mediocre posts. Each post competes against your other recent posts for limited feed slots.
## Common Mistakes
### Prompting for a "Blog Post"
Never say "write me a blog post." That phrase triggers every AI's corporate-FAQ mode. Instead, describe the specific output:
```
Write a 2,000 word guide about [TOPIC].
The audience is [WHO].
They already know [X] but don't know [Y].
The goal is to teach them [Z] with enough detail that they can actually do it today.
```
### Using AI for the Parts You Should Do
**AI is good at:** research synthesis, finding the right word, restructuring paragraphs, catching inconsistencies, generating examples.
**AI is bad at:** having original thoughts, knowing your audience, deciding what matters, making editorial judgment, being funny on purpose.
Do the thinking. Let AI do the typing.
### Publishing the First Draft
No engineer ships the first version of their code. Don't ship the first version of your content. The edit pass is where slop dies and personality emerges.
### Not Reading Your Own Work
If you haven't read your article out loud before publishing, you haven't edited it. AI-generated text has a cadence that sounds fine when reading silently but falls apart when spoken. Read it aloud. If it sounds weird, it is weird.
### Trying to Hide AI Usage
Don't write "AI-generated" disclaimers. Don't use tools to "humanize" AI text. Don't worry about AI detectors. Instead, write content so specific and opinionated that the question doesn't arise. The best defense against "did AI write this?" is content that obviously came from a real person with real experience.
## Current Limitations
**Voice drift on long pieces.**
AI can match your style for a section, but across a 3,000+ word article, the voice gradually drifts toward default. Break long pieces into sections and prompt each one individually.
**Humor is hard.**
AI can be witty on accident but struggles with intentional humor. Write your own jokes. Let AI set up the context around them.
**Cutting is harder than adding.**
AI is great at generating content but terrible at deciding what to cut. Editorial judgment—what doesn't belong—is still a human skill.
**Domain expertise gaps.**
AI doesn't know what it doesn't know. If you're writing about your specific domain, you'll catch errors AI can't. Always verify technical claims.
**The uncanny valley.**
Even with a great CLAUDE.md, AI sometimes produces paragraphs that are almost-but-not-quite right. You can feel the wrongness but can't immediately articulate it. This is normal. Rewrite those paragraphs by hand.
## Quick Reference
### The Workflow
- **Research** — Claude Code web search + synthesis (30-60 min)
- **Outline** — Do this yourself (15 min)
- **Draft** — Wispr Flow dictation or section-by-section with Claude Code (30-60 min)
- **Edit** — Read aloud, cut aggressively, targeted AI edits (30-45 min)
- **Slop Check** — Run against your CLAUDE.md rules (5 min)
- **Publish**
### The CLAUDE.md Essentials
- Ban slop words (delve, crucial, landscape, game-changer)
- Define your paragraph length range
- Specify your opening style
- List your structural patterns
- Include 2-3 examples of your best writing as reference
### The Anti-Slop Checklist
- Opens with something only I could write
- No hedging—every claim is direct
- Paragraph lengths vary (1 sentence to 5+)
- No banned words from my CLAUDE.md
- Includes 3+ specific personal details
- Has working examples and code blocks
- Read it out loud—sounds natural
- Every paragraph adds new information
- No preamble summarizing what I'm about to say
### Algorithm Optimization
- Optimize for shares (especially DMs) and follows, not likes
- Space posts 2-4 hours apart (author diversity penalty)
- Create content people want to send privately
- Include personality—follows come from distinctive voice
- Avoid triggering mutes/blocks (compound damage to reach)
### Prompt Templates
**Research:**
```
Research [TOPIC] thoroughly. Give me raw material:
- How it actually works (technical detail)
- What most people get wrong
- Specific examples and use cases
- Pricing and practical details
- Current limitations (honest)
```
**Section Draft:**
```
Read my CLAUDE.md. Write section [N]: [TITLE]
Key points:
[list]
Write in my voice. Be specific. Include examples. Every sentence teaches something. No filler.
```
**Edit Pass:**
```
Find and fix: corporate speak, hedging, filler paragraphs, energy drops, banned words.
Be aggressive—cut anything that doesn't need to exist.
```
**Voice Match:**
```
Read these 5 articles I've written. Analyze my style: paragraph length, sentence patterns, vocabulary, opening style, transitions, recurring phrases.
Save as a writing style profile.
```
## TL;DR
AI slop is a skill issue, not a tool problem. People type "write me a blog post" and get corporate FAQ output. The fix is using AI the way engineers use it—with specs, constraints, iteration, and review.
Your CLAUDE.md is your most important asset. A style guide that encodes your voice, bans slop words, and defines your patterns. Write it once, apply it to everything.
The workflow: research → outline (by hand) → draft → edit → slop check → publish. Never skip the outline. Never skip the edit pass. Never ship a first draft.
Show, don't generate. Lead with personal details only you know. Include working examples. Kill the hedge words. Vary your paragraph rhythm. If anyone could have written it, it's slop.
The X algorithm rewards shares and follows, not likes. Create content people send privately to friends. Include enough personality that readers follow you, not just consume you. Space your posts. Never trigger mutes or blocks.
The golden rule: never publish content you can't explain. If you read a sentence and can't articulate why it exists and what it's doing, cut it. The tool doesn't matter. The judgment does.
Engineers already know how to direct AI. The skill transfers directly to writing. Start treating your content like a codebase—spec it, build it, test it, iterate it—and the slop disappears.