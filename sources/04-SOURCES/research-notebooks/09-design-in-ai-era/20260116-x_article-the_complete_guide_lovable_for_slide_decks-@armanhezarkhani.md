---
url: https://x.com/ArmanHezarkhani/status/2012224841374486998
author: Arman Hezarkhaki (@ArmanHezarkhani)
captured_date: 2026-02-13
---

# The Complete Guide: Lovable for Slide Decks

*Build slide decks that actually impress clients.*

(Description: Gradient logo featuring orange-to-purple heart shape with "The Complete Lovable Presentation Guide" heading and subtitle "Build slide decks that actually impress clients.")

---

## Opening Statement

I actually believe that Google Slides and Powerpoint still have a place.

Finance and consulting firms aren't going to immediately change their ways.

But, the rest of us can.

At Tenex, we use every AI tool we can get our hands on. Lovable has become our go-to for one unexpected use case: building slide decks that actually impress clients.

Here's everything I've learned after creating dozens of presentations in Lovable -- from sales pitches to conference talks to internal training materials.

---

## What Is Lovable?

Lovable is an AI-powered full-stack app builder. You describe what you want in plain English, and it generates a working React application with real code.

The tech stack: React 18 + TypeScript + Tailwind CSS + shadcn/ui + Vite. This matters because your "slides" get smooth animations, modern design, and responsive layouts out of the box.

To get started, go to lovable.dev, sign up, and start prompting. The free tier gives you 5 daily credits (up to 30/month). Pro starts at $21/month (billed annually) for 100 credits, scaling up based on your needs.

### Key 2025 Updates

- Agent Mode is now the default -- it thinks, plans, and acts autonomously
- Credits are usage-based: simple edits cost less than 1 credit, complex ones cost more
- Visual Edits let you tweak UI without burning credits
- Dev Mode lets paid users edit code directly in Lovable
- Chat Mode Agent can reason across multiple steps and debug intelligently

---

## The Mental Shift

The biggest mistake people make with Lovable for slides is thinking in PowerPoint terms. They try to create "a presentation with 10 slides" and get frustrated when the AI doesn't understand their vision.

That's not what this is.

A slide deck in Lovable is an app. It's a single-page React application where each "slide" is a full-screen view, and navigation is handled by state changes. Think of it like a website where you can only see one section at a time.

Once you understand this, everything clicks.

---

## Write Better Prompts

The quality of your deck is directly proportional to your initial prompt. People who get terrible results type "make me a pitch deck" and expect magic.

Before you prompt anything, answer these questions:

### What does "done" look like?

If you can't picture the finished state, neither can Lovable. "Create a presentation" is vague. "Create a full-screen slide deck with keyboard navigation, animated transitions, and 8 slides covering our Q4 results" is actionable.

### What design system?

Dark or light theme? What colors? What font style? Lovable defaults to its own choices if you don't specify -- and they're often not what you want.

### What navigation method?

Arrow keys? Click buttons? Swipe gestures? All three? Specify upfront or you'll burn credits fixing it later.

### The Prompting Golden Rule

From Lovable's official documentation: Take your time with prompts. Re-check everything. Break work into small, testable blocks. The more precise your inputs, the better your outputs.

---

## Set Up a Knowledge File First

The Knowledge File is your project's brain. It gets sent with every prompt and helps Lovable understand the full context. For complex decks (10+ slides, specific branding), create one before you start building.

Use Chat Mode to generate it:
```
Generate a knowledge file for my presentation project:

PROJECT: Q4 Investor Update Deck
AUDIENCE: Board members, existing investors
TONE: Professional, confident, data-driven

BRAND:
- Primary: #1e3a5f
- Accent: #f59e0b
- Background: Dark theme, #0f172a
- Typography: Inter font family

SLIDE STRUCTURE:
- Max 3 key points per slide
- Icons from Lucide React
- Subtle animations on content reveal
- 16:9 aspect ratio optimized

TECHNICAL:
- Must work on projector (high contrast)
- Keyboard navigation required
- No external dependencies beyond what's already installed
```

Save this as a file in your project. Reference it when prompting: "Following the knowledge file, create slide 5: Market Size"

---

## The Foundation Prompt

This is the prompt I use to start every slide deck. Copy it, modify the specifics, and use it as your base:
```
Create a presentation slide deck app with these specifications:

STRUCTURE:
- Full-screen slides (100vh x 100vw)
- Keyboard navigation: Arrow keys, Space, Enter to advance; Escape for overview
- On-screen navigation: Subtle prev/next buttons at screen edges
- Progress indicator: Dots at bottom showing current position
- Total slides: [NUMBER]

DESIGN:
- Theme: [Dark with navy #0f172a background / Light with white background]
- Accent color: [YOUR BRAND COLOR]
- Typography: Clean sans-serif, large headings (48-72px), readable body (20-24px)
- Spacing: Generous whitespace, content centered, 64px padding from edges

ANIMATIONS:
- Use Framer Motion for all transitions
- Slides: Fade + horizontal slide (0.4s ease-out)
- Content: Staggered entrance within each slide
- Keep all animations under 0.5s

SLIDE CONTENT:
1. Title slide: "[TITLE]" with subtitle "[SUBTITLE]"
2. [Describe slide 2]
3. [Describe slide 3]
...

Build navigation first. Confirm it works before adding detailed content.
```

---

## Prompting Patterns That Actually Work

### Pattern 1: Build Navigation First

Never try to build everything at once. The navigation system is the skeleton -- get it working before you dress it up.

**Prompt 1:** "Create a slide deck skeleton with 5 placeholder slides. Each slide should just say 'Slide 1', 'Slide 2', etc. Implement keyboard navigation (arrow keys) and bottom progress dots. Test that navigation works before doing anything else."

**Prompt 2:** "Navigation works. Now design slide 1 as a title slide with..."

**Prompt 3:** "Slide 1 looks good. Now design slide 2 with..."

This approach saves credits and prevents the AI from breaking things.

### Pattern 2: Use Chat Mode for Planning

Chat Mode Agent is your AI co-pilot. It helps you debug, brainstorm, and plan implementations -- without editing your code until you're ready.

Before building anything complex:
```
"I'm building a 12-slide investor pitch deck. Help me plan the optimal structure.
What slides should I include? Which ones need animations vs. static content?
What's the best order for narrative flow?"
```

**Pro tip:** Many experienced Lovable users spend 60-70% of their time in Chat Mode. Only click "Implement the plan" when you're fully satisfied.

### Pattern 3: Be Explicit About What NOT to Touch

The AI sometimes "fixes" things you didn't ask it to fix, breaking working code. Add guardrails:
```
On slide 4 only, add a three-column feature comparison.

Do NOT modify:
- The navigation system
- Any other slides
- The color scheme
- The animation timing

Please don't touch component A, layout B, or shared logic unless necessary.
Follow best practices from Tailwind.
```

### Pattern 4: Reference Known Styles

Instead of describing aesthetics from scratch, reference things Lovable has seen:
```
"Design this slide like an Apple keynote presentation:
- Single bold statement centered on screen
- Dramatic fade-in animation
- Minimal supporting text
- Lots of negative space"
```
```
"Make this look like a Stripe landing page:
- Clean gradient background
- Floating cards with subtle shadows
- Modern, technical aesthetic"
```

---

## Slide Templates You Can Steal

### Title Slide

Create the title slide:
- Company logo placeholder at top (200px width, centered)
- Main title: "[YOUR TITLE]" in 72px bold white text
- Subtitle: "[YOUR SUBTITLE]" in 24px text at 60% opacity
- Animated entrance: Logo fades in first (0.3s), then title slides up (0.3s), then subtitle fades in (0.2s)
- Gradient background from #0f172a to #1e293b

### Statistics/Metrics Slide

Create a metrics slide with 4 key statistics in a 2x2 grid:
- Each stat: Large number with count-up animation on first view
- Small label below each number
- Lucide icon above each stat
- Cards have subtle border and lift on hover
- Stats to show: "150+" Enterprise Clients, "99.9%" Uptime SLA, "$2.4M" Annual Revenue, "4.8/5" Customer Rating
- Stagger the card entrance animations (0.1s delay each)

### Feature Comparison Slide

Create a three-column pricing comparison:
- Headers: "Starter", "Pro", "Enterprise"
- 6 feature rows with checkmarks (green) or X marks (gray)
- Middle column highlighted with accent border and "Most Popular" badge
- Columns animate in with stagger effect from left to right
- On hover, columns lift slightly with shadow

### Quote/Testimonial Slide

Create a testimonial slide:
- Large decorative quotation mark (low opacity, top-left)
- Quote text in 28px italic, max 2 lines
- Customer name in bold, title and company below
- Small company logo (if available)
- Elegant fade-in animation for the entire block
- Dark background with subtle gradient

### Team Slide

Create a team slide with 4 team members:
- Circular placeholder images (150px diameter)
- Name in 20px bold, title in 16px below each
- Arranged in centered row with equal spacing
- On hover: subtle scale up (1.05) and shadow
- Staggered entrance animation left to right

### Call-to-Action Slide

Create closing CTA slide:
- Bold headline: "Ready to Get Started?"
- Two buttons side by side: "Schedule Demo" (primary, filled) "Learn More" (secondary, outlined)
- Contact email below buttons
- Subtle animated gradient background
- Everything centers vertically and horizontally

---

## Visual Edits: Your Credit-Saving Weapon

Visual Edits is a Figma-like editor that doesn't cost credits. Use it for small tweaks instead of burning messages on "make the button bigger."

### How to use it:

1. Click "Edit" in the prompt box
2. Click the element you want to change
3. Modify text, fonts, colors, or spacing directly
4. Click Save

Changes show up immediately through Vite-powered Hot Module Reloading.

### What Visual Edits can do:

- Change text content
- Adjust font sizes, weights, and alignment
- Modify colors
- Tweak padding and margins
- Resize images
- Apply Tailwind classes directly
- Jump to selected elements in code

### When to use it:

- Fixing typos
- Adjusting font sizes
- Changing colors
- Fine-tuning spacing
- Quick UI polish

### When NOT to use it:

- Adding new components
- Changing layouts fundamentally
- Implementing animations
- Anything structural

This is how you make a deck look polished without burning your monthly credits.

---

## Chat Mode Agent: Your Debug Partner

When things break (and they will), Chat Mode Agent is how you fix them without making things worse. It can reason across multiple steps, search files, inspect logs, and query databases.

### The Debug Pattern:
```
"The slide transitions stopped working after the last change. Please investigate:
1. What changed in the AnimatePresence wrapper?
2. Why are slides no longer animating?
3. What's the fix?

Do not implement anything yet -- just explain."
```

Read the explanation. If it makes sense, then:
```
"Implement the fix you described. Do not change anything else."
```

### The "I'm Frustrated" Pattern:

This is an official Lovable best practice. When the AI keeps making the same mistake:
```
"I am frustrated. The navigation keeps breaking every time you edit a slide.
Walk me through exactly what's happening and suggest a different approach."
```

This actually works. The AI responds differently when you signal that normal approaches aren't working.

---

## Version Control Strategy

Every edit in Lovable is a commit. Use this to your advantage.

### Pin working versions.

After every major milestone -- navigation working, design system applied, all content added -- pin that version. Name it descriptively: "v3-navigation-and-animations-complete"

### Compare when debugging.

When something breaks:
```
"Compare the current version to the version from 30 minutes ago.
What changed that might have broken the keyboard navigation?"
```

### Use GitHub sync.

Connect your project to GitHub. This gives you:
- Automatic backup of all changes
- Ability to roll back to any commit
- Option to export and continue in VS Code or Cursor
- Full code ownership

### Use Dev Mode for precision.

If you're comfortable with code, Dev Mode lets you edit directly in Lovable. Sometimes a 2-line fix in code is faster than explaining what you want to the AI.

---

## Animations That Don't Suck

Lovable can use Framer Motion, but you have to ask for it right.

### Slide Transitions:
```
"Implement slide transitions with Framer Motion and AnimatePresence:
- Entering slides: Fade in (opacity 0→1) + slide from right (x: 50→0)
- Exiting slides: Fade out + slide to left (x: 0→-50)
- Duration: 0.4 seconds
- Easing: ease-out
- Use AnimatePresence with mode='wait' to prevent overlap"
```

### Staggered Content:
```
"When slide 3 enters, animate its content sequentially:
- Heading appears first (fade up, 0.3s)
- Subheading next (fade up, 0.2s delay)
- Each bullet point staggers in (0.1s between each)
- Use Framer Motion variants for orchestration
- Animation should only trigger once, on first view"
```

### Micro-interactions:
```
"Add subtle hover effects to all interactive elements:
- Buttons: scale to 1.02 on hover, 0.95 on press
- Cards: translateY -4px with shadow on hover
- Navigation dots: scale to 1.3 when hovered
- All transitions under 0.2 seconds
- Use Tailwind transition classes where possible"
```

### Performance tips:

- Use only transform and opacity (GPU-accelerated)
- Reduce duration to 0.3s maximum for snappy feel
- Use ease-out easing, not spring physics (simpler to control)
- Add `will-change: transform` to animated elements

---

## 15 Use Cases That Actually Work

### Pitch Decks

- Investor pitch with animated metrics and team slides
- Sales deck with interactive product demos embedded
- Partnership proposal with comparison matrices
- Startup pitch with live data from your API

### Internal Presentations

- Quarterly business review with real-time dashboard
- Team all-hands with embedded video placeholders
- Training deck with interactive quiz components
- Project kickoff with clickable timeline

### External Presentations

- Conference talk with syntax-highlighted code slides
- Webinar deck with live poll integration
- Product launch with animated feature reveals
- Customer case study with before/after sliders

### Creative Uses

- Portfolio showcase with project galleries
- Interactive resume/CV presentation
- Event recap with photo carousel slides

---

## When Things Go Wrong

### Navigation Stops Working

**Problem:** Arrow keys don't change slides anymore.

**Fix prompt:**
```
"The keyboard navigation broke. Please:
1. Check that useEffect has the keydown event listener
2. Ensure listener is on window/document, not a specific element
3. Verify the cleanup function removes the listener on unmount
4. Confirm currentSlide state updates correctly

Do not touch any slide content."
```

### Animations Are Choppy

**Problem:** Slide transitions feel janky.

**Fix prompt:**
```
"Animations are stuttering. Optimize for performance:
1. Use only transform and opacity (GPU-accelerated properties)
2. Remove any width/height/layout animations
3. Add will-change: transform to animated elements
4. Reduce duration to 0.3s maximum
5. Use ease-out easing, not spring physics"
```

### Content Overflows

**Problem:** Slide content extends past the viewport.

**Fix prompt:**
```
"Content is overflowing slides. Fix this:
1. Set max-height: 100vh and overflow: hidden on slide container
2. Use clamp() for responsive fonts: clamp(16px, 3vw, 24px)
3. Reduce content density -- fewer items per slide
4. Add proper padding that accounts for navigation elements"
```

### The AI Keeps Breaking Other Slides

**Problem:** Every change seems to break something else.

**Fix approach:** First use Chat Mode to plan:
```
"I need to add content to slide 5, but every time I make changes, other slides break.
Suggest an approach that isolates changes."
```

Then implement with guardrails:
```
"Create slide 5 content as a completely separate component.
Import it into the main slide array.
Do not modify any existing slide components or the navigation system."
```

### The "Try to Fix" Button Loops

**Problem:** Lovable says it fixed the issue, but it didn't.

**Fix approach:**

1. Copy the actual error message
2. Switch to Chat Mode
3. Paste: "This is the actual error: [error]. Analyze what's really happening."
4. Ask it to insert debug code if needed
5. Screenshot console output and paste it back
6. Only then implement the fix

---

## Mobile and Responsive

By default, your deck will look weird on phones. If you need mobile support:
```
"Make the slide deck responsive:

DESKTOP (1200px+):
- Full presentation mode
- Large typography (72px titles, 24px body)
- Keyboard hints visible

TABLET (768px-1199px):
- Slightly reduced font sizes
- Touch-friendly navigation buttons (44px minimum)
- Swipe gestures enabled

MOBILE (below 768px):
- Swipe navigation primary
- Stack any columns vertically
- Reduce title to 36px, body to 18px
- Hide keyboard hints
- Larger navigation dots (easier to tap)"
```

For mobile-first development, use this prompt (from Lovable's official guidance):
```
"Always make things responsive on all breakpoints, with a focus on mobile first.
Use modern UI/UX best practices for determining how breakpoints should change the components.
Use shadcn and Tailwind built-in breakpoints instead of anything custom.
Optimize the app for mobile without changing its design or functionality."
```

---

## Publishing and Sharing

Once your deck is done:

### One-click deploy:

1. Click "Share" → "Publish" in Lovable
2. Get your unique URL: your-project.lovable.app
3. Share directly -- viewers don't need to download anything

### Custom domain:

1. Buying and connecting domains is now built into Lovable
2. Go to Settings → Domain
3. Add your custom domain
4. Now it's presentations.yourcompany.com

### Presenter mode additions:
```
"Add presenter utilities:
- Press 'F' to toggle fullscreen
- Press 'B' for black screen (presentation breaks)
- Press 'T' to show elapsed time in corner
- Press 'O' for slide overview/grid view

Position controls in bottom-right, semi-transparent until hovered"
```

---

## Current Limitations

Lovable is powerful but not perfect. What doesn't work well:

**Complex animations:** Anything beyond basic fade/slide/scale gets unreliable. If you need particles, 3D transforms, or complex choreography, you'll fight the AI.

**Pixel-perfect design:** If your brand guidelines specify exact pixel values for everything, you'll spend more time fixing than building. Lovable works best when you give it creative latitude.

**Large decks (20+ slides):** The AI's context window struggles with very long presentations. Break them into sections or expect some inconsistency.

**Real-time collaboration:** Unlike Google Slides, you can't have multiple people editing simultaneously with cursors visible. Lovable has workspaces and multiplayer, but it's async.

**Offline use:** These are web apps. No internet, no presentation. Export to PDF if you need offline backup.

**Export to PowerPoint:** There's no "download as .pptx" option. You're either presenting from the web URL or screen-sharing the Lovable preview.

---

## Quick Reference

**Access:** lovable.dev

**Pricing:**
- Free Plan: $0, includes 5 daily credits (30/month)
- Pro Plan: Starting from $21/mo (when billed annually), includes 100+ monthly credits
- Business Plan: Starting from $42/mo (when billed annually), includes Team features and SSO (Single Sign-On)

Credits are usage-based: simple edits < 1 credit, complex ones > 1 credit.

**Best for:** Pitch decks, product demos, conference talks, any presentation that benefits from modern web design and animations

**Not for:** Presentations that must be PowerPoint files, offline-only scenarios, decks with 20+ slides

**Tech stack:** React 18, TypeScript, Tailwind CSS, shadcn/ui, Framer Motion (on request)

**Key features:**
- Agent Mode (default): thinks, plans, acts autonomously
- Visual Edits (no credits): Figma-like UI tweaking
- Chat Mode Agent: planning and debugging
- Dev Mode: direct code editing
- Version pinning for checkpoints
- GitHub sync for backup
- One-click publish to shareable URL
- Security Scan before publishing

**Keyboard shortcuts to implement:**
- ← / →: Previous / Next slide
- Space / Enter: Next slide
- Home: First slide
- End: Last slide
- 1-9: Jump to slide
- F: Toggle fullscreen
- B: Black screen
- O: Overview mode

---

## TL;DR

**Lovable builds slide decks as React apps.** Understand this and you'll unlock its power.

**Set up a Knowledge File first.** It's your project's brain and gets sent with every prompt.

**Write better prompts.** Define what "done" looks like. Specify design, navigation, and constraints upfront.

**Build navigation first.** Get the skeleton working before adding content. Test keyboard and click navigation.

**Use Visual Edits for tweaks.** It's free. Don't burn credits on "make the text bigger."

**Use Chat Mode Agent for debugging.** Investigate before implementing. Avoid the fix-break-fix loop.

**Pin working versions.** After every milestone, create a checkpoint. Name it descriptively.

**Request Framer Motion explicitly.** Lovable can do beautiful animations, but you have to ask.

**Guardrail your prompts.** Tell the AI what NOT to touch. It prevents collateral damage.

**Try "I am frustrated" when stuck.** It's an official pattern that actually helps.

**Know the limits.** Complex animations, huge decks, and offline use are weak spots.

**One-click publish.** When it's done, share a URL. No downloads, no installations, no friction.

**The tool is maturing fast.** Start learning now while everyone else is still making boring PowerPoints.