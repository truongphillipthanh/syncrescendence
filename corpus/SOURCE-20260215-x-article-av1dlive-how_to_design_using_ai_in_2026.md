# How to Design Using AI in 2026
(Description: Hero image featuring a serene landscape with a field of white and orange flowers at dusk, a bright golden-glowing architectural structure in the center, and dramatic swirling light trails in vibrant orange, pink, and blue tones across a clear blue sky)
Designing was hard. The era of vibe-coding, made the ability to build good designs super easy.
**What was hard always was TASTE.**
I built 5+ projects using AI before I figured this out. The answer never lied in better prompts. It was that AI amplified the one skill which I ignored: developing taste.
Here's the workflow that clicked for me:
## Execution Is Easy, Judgment Is Everything
You can ask Claude to "design a dashboard" and get something that works.
But does it look *good*? Does it even feel *right*?
AI excels at patterns it's seen. Your job is knowing which patterns are worth copying.
The designers who I see excelling in 2026 aren't the ones with the longest prompts or the newest tools.
They are more often the ones who've trained their eye by:
- studying hundreds of interfaces,
- deconstructing what works
- feeding that judgment back into their AI workflow.
Think about it: when you see a beautifully spaced landing page or a perfectly balanced color palette. You're not impressed by the technical execution.
You're impressed by the taste behind it.
AI can execute anything. You just need to know what's worth executing.
## Build Taste → Generate → Iterate
Here's the exact process I use now, broken into 5 steps that actually work together:
### Build Taste Through Visual References
Moodboarding is peak 2010s, but it works perfectly for vibe design in 2026.
Before I touch any AI tool, I spend 20-30 minutes gathering screenshots of interfaces which are not just "pretty" designs rather interfaces that solve the same problem I'm working on.
**Where to look:**
- **Awwwards** for cutting-edge web design
- **Pinterest AI search** (upload a screenshot, find similar designs)
- **Dribbble** for UI patterns
Pro tip: Don't just save random pretty images. Ask yourself: "What specifically works here?" Is it the hierarchy? The spacing? The color restraint? Try naming it as this builds your design vocabulary.
### Video → Code: The Kimi K2.5 Shortcut
You can literally record a video of any website you like and have AI recreate the code.
> Kimi Product @KimiProduct · Jan 27
> 
> One-shot "Video to code" result from Kimi K2.5 It not only clones a website, but also all the visual interactions and UX designs. No need to describe it in detail, all you need to do is take a screen recording and ask Kimi: "Clone this website with all the UX designs."
(Description: Split-screen image showing "Original Video (Cr. Jesko Jet)" on the left with a minimalist dark interface featuring a circular blue window design element and text "We are movement" and "We are distinction", and "Kimi's Output" on the right with a simplified version maintaining the same visual language and central blue circular element)
Here is the prompt i use to Reverse engineer screen recordings to landing pages:
(Description: Code block with monospace font displaying a structured prompt for analyzing website videos. The prompt header reads "Generate a ONE-PAGE LANDING PAGE prompt using a RANDOMLY SELECTED design style" followed by sections for "Dark Mode First, Gradient Modern, Typography First" and detailed instructions for layout & structure, typography, components, animations & interactions, and output specifications. Text is syntax-highlighted in blue and cyan)
**Key points:**
- Captures 80% of the aesthetic immediately
- Parses structure, components, and transitions frame-by-frame
### Learn the Language of Design
I struggled to make sense of anything till I understood the exact terms
You can't prompt what you can't name
Before generating anything, learn these terms so you can give AI precise instructions instead of garbage requests like "make this prettier fam" or the best one "please".
#### a) Typography basics:
- Hierarchy (H1→H6→body→captions)
- Kerning (space between two letters)
- Leading (vertical line spacing)
- Weight (thin/regular/bold/black)
#### b) Layout fundamentals:
- White space (breathing room around elements)
- Proximity (grouping related items)
- Contrast ratio (4.5:1 minimum for accessibility)
#### c) Color system:
- Primary (brand colors, max 2)
- Accent (CTAs and highlights)
- Semantic (error red, success green, warning yellow)
- Neutral (text grays)
Here is why this matters: When you say "reduce the leading on H2s to 1.4" AI executes perfectly.
**The difference is precision.** AI doesn't guess what "better" means. But it knows exactly what "increase white space between sections from 32px to 48px" means.
### Meta-Prompts + Skills: Build Once, Use Forever
Meta-prompts create range. Skills lock in quality. I prefer to use both.
#### Phase 1: Meta - Prompt
Use AI to write prompts to feed to AI
(Description: Terminal-style code block with dark background displaying an optimized prompt. Content includes "Generate a ONE-PAGE LANDING PAGE prompt using a RANDOMLY SELECTED design style: Neobrutalist, Swiss, Editorial, Glassomorphism, Bauhaus, Minimal, Japandi, Dark Mode First, Gradient Modern, Typography First" and additional instructions for output formatting covering paragraphs, design philosophies, and methodology)
I would suggest to take a look at the original prompt posted on Reddit by user JCodesMore on r/PromptEngineering
This would help to optimise the prompt for your use case
Then paste the style brief into Minimax-2.5 ( my current favourite model for front-end design). This is subjective for everyone :)
**Outcome:** you can produce dozens of distinct "vibe specs" quickly. Volume builds taste.
#### Phase 2- Skills.md
This is my new favourite to have all the required best practices and design philosophies at my disposal
**What "skills" are:** reusable, task-scoped rule packs (constraints + checks + workflows) that agents apply whenever the task matches
### My Current 3 favourite skills
#### 1) UI Skills (made by @Ibelick)
A library of reusable "fix packs" for agent-built UI: accessibility, motion performance, metadata hygiene, etc.
**Role:** prevent common mistakes by default.
> Ibelick @Ibelick · Jan 19
> 
> npx ui-skills init
(Description: Terminal window with code initialization command displayed. The window shows a command line interface with typical MacOS terminal appearance including red, yellow, and green window control buttons, displaying file paths and initialization output)
#### 2) UI/UX Pro Max - Design Intelligence
A searchable design playbook for web + mobile. You can literally pick up a stack and get recommendations for it
Install it using
(Description: Dashboard interface for "UI UX Pro Max" displaying color-coded badges and metadata. The design shows release version "V2.2.1", reasoning rules count "100", UI styles "67", along with Python "3.X" language indicator, MIT license badge, CLI tools, download metrics "$2k/month", star count "31k", PayPal and Development support buttons. Lower section shows a "Design Intelligence" heading with searchable database description and six numbered statistic boxes displaying numbers like 57, 95, 50, 8, 24, and 29)
#### 3) RAMS: final QA with line-level fixes
Automated review that flags UI issues and returns concrete fixes (often with line numbers).
**Role:** last-mile polish before you ship.
> Eli Rousso @elirousso · Feb 11
> 
> Rams Skill now has 29,198 installs
(Description: Dashboard interface for RAMS (Rams Automated Management System) tool. The interface shows a dark-themed layout with multiple columns and menu sections displaying installation metrics, feature lists, configuration options, and support information in a tabular format)
### Workflow I follow
1. **Meta-prompt → vibe spec** (style intent, hierarchy, interaction feel)
2. **Generate code** (Minimax-2.5)
3. **Apply skills** (baseline constraints: UI + motion + metadata)
4. **Run UI/UX Pro max review** (standardize production UI patterns)
5. **Final polish with RAMS** (fix flagged issues, ship)
**Why this compounds:** once your constraints live as skills, every future UI inherits them by default which mean less rework, fewer regressions and more consistent taste.
## The Zoom-In Method: 50% → 99% → 100%
This is the framework that changed everything for me. **Stop expecting AI to nail it in one shot.**
### First pass (50%): Full context dump
Give AI everything you know about the project:
- Goal and core features
- Target audience and vibe
- Color palette (specific hex codes)
- Every page and component needed
- Reference code from designs you like
(Description: Code block with monospace font showing a structured prompt template. The content reads "Create a [product type] for [target users]", followed by sections for "Core features/pages", "Color palette: [specific hex codes]", "Typography: [font choices if any]", "Style: [mood/vibe descriptors]", "Key components needed: [list all UI elements]", and "Technical constraints: [framework, accessibility needs, etc.]". Final line shows "Reference structure: [paste example code or link]")
### Second pass: Self-Review (99%)
Use this prompt for the AI to self-reflect
(Description: Terminal-style code block with dark background. The prompt reads "Review the [specific page/component] you created and improve it:" followed by numbered instructions: "1. Identify mistakes, inconsistencies, and visual issues 2. Apply modern UI/UX best practices: - Spacing and rhythm - Typography hierarchy - Color balance and contrast - Visual alignment - Accessibility (WCAG AA minimum) 3. Ensure layout feels balanced and professional 4. Fix awkward placements and improve consistency 5. Keep the same [color palette/design system]. Make it production-ready." The final line reads "Keep the same [color palette/design system]. Make it production-ready.")
AI catches 70% of its own mistakes when you make it review its work. Font sizes, padding inconsistencies, hierarchy issues ; it fixes them without you pointing them out.
Repeat this for each page.
You're now at 99%.
### Micro pass (100%): Pixel-perfect polish
This is the final nail in the coffin.
(Description: Terminal code block displaying precise UI adjustment instructions. Content shows "On [specific component/page], make these precise changes:" followed by five numbered items: "1. [Specific spacing adjustment with px values] 2. [Exact color/state change with hex codes] 3. [Precise alignment fix with measurements] 4. [Animation timing with ms/easing function] 5. [Any other micro-adjustments]". Text uses cyan and white color highlighting)
Being specific = better results. Screenshots help even more.
## The Philosophy: AI as Your Junior Designer
In this workflow, you stop treating AI like a "black box" and start treating it like a **junior designer**.
Professional design is a progression from low-fidelity wireframes to high-fidelity mockups, ending with polished micro-interactions.
The Zoom-In Method allows you to guide the tool through this proven process.
- **Old Way:** 6–8 hours of manual labor and "fighting" the software.
- **New Way:** 1–2 hours of strategic guidance and systematic refinement.
## The New Design Moat
Your **taste** and **process** are your true competitive advantages.
- **Precision:** Trade "make it look good" for professional terminology.
- **Curation:** Use real-world references to kill generic outputs.
- **Efficiency:** Let the **Zoom-In Method** handle the technical heavy lifting while you focus on cohesion and empathy.
## The Bottom Line:
You are no longer the bottleneck of your own creativity.
Stop overthinking and start shipping.
Before you generate anything, learn these terms. This is the difference between getting exactly what you want and getting random garbage.
### Typography basics:
- Hierarchy (H1→H6→body→captions)
- Kerning (space between two letters)
- Leading (vertical line spacing)
- Weight (thin/regular/bold/black)
### Layout fundamentals:
- White space (breathing room around elements)
- Proximity (grouping related items)
- Contrast ratio (4.5:1 minimum for accessibility)
### Color system:
- Primary (brand colors, max 2)
- Accent (CTAs and highlights)
- Semantic (error red, success green, warning yellow)
- Neutral (text grays)