---
url: https://x.com/froessell/status/2018621691006439603
author: ✌︎ frederik ✌︎ (@froessell)
captured_date: 2026-02-03
---

# My AI Design Toolkit: What Actually Works For Me in 2026

(Description: Screenshot showing six tool icons arranged horizontally: a dotted grid pattern (v0), a hand holding a pen (Superdesign), Figma logo, a 3D box (Aura.build), a sun-like icon (Jitter), and the Jitter text logo on black background.)

I've been obsessing over AI design tools for the past year. Testing everything, discarding most, building real workflows with the few that stuck.

Here's my honest breakdown of what actually works and how I use them together.

## But first, a caveat.

I work in two very different contexts. On one hand, I'm a senior product designer at a large ecommerce company. Established design systems, multiple platforms and brands, token pipelines connected to GitLab, stakeholders to align with. You can't just wing it.

On the other hand, I have side projects. Greenfield work where I can experiment freely, move fast, and break things without consequences.

My AI workflows look completely different depending on which hat I'm wearing.

This article covers both. I'll start with my side project workflow (because that's the most fun and this is where AI tooling really shines), then talk about how I adapt for enterprise work.

If you're working in a big company with established systems, don't worry. I'll get to you. But the side project workflow is worth understanding first, because that's where you'll see what's possible before figuring out what's practical.

## It's Not About the "Best" Tool

My workflow isn't about finding a single perfect tool. It's about the right tool at the right stage.

**Ideation → Iteration → Build → Polish → Content**

Each phase has different needs. Trying to use one tool for everything is like editing video in Photoshop. You can, but why would you?

(Description: Screenshot of Superdesign.dev interface showing multiple design mockup variations for a product concept laid out in an infinite canvas style interface, with sidebar navigation and tool options visible.)

## Phase 1: Quick Concepts

**Tools:** v0.app, Superdesign.dev, Variant.ai, aura.build

This is where AI shines brightest. I'm not precious here. I want volume and speed.

- Prompt-based exploration
- Adding inspiration images for context
- Generating copy alongside visuals

The goal isn't perfection. It's finding a direction worth pursuing.

**v0 and Aura** are my go-to for rapid UI concepts. Describe what you want, get something tangible in seconds.

**Superdesign** has a web interface that makes quick exploration easy and uses an infinite canvas similar to Figma. It's neat and feels creative to use.

**Variant.ai** for when I need multiple directions fast.

I'm not looking for final designs here. I'm looking for sparks.

## Phase 2: Iteration

**Tool:** Figma

(Description: Screenshot of Figma design interface showing multiple mobile app screens and design variations with component library on the right side, displaying dark-themed UI designs.)

Once I've found a concept worth pursuing, I bring it into Figma.

AI got me 60% there. The last 40% (the taste, the details, the "why does this feel right") is still me and Figma. No AI substitute for this part (yet).

This is where design thinking happens. The AI gave me raw material. Now I shape it.

(Description: Screenshot of Vibecodeapp interface showing a mobile phone template with a "Pick template" selection screen displaying various template options including device mockups.)

## Phase 3: Build

**Tools:** Claude Code, Vibecodeapp, Cursor

This is where designers become dangerous.

**Claude Code** is my number one. It thinks with me, understands full codebases, and lets me ship frontend polish without waiting on dev. I spend as much time here as I do in Figma now. Skills are an absolute game changer for me. I'm still on the regular Claude plan, but it's enough for my use for now.

**Vibecodeapp and Cursor** fill gaps depending on the project. I build prototypes in Vibecode app - adding AI apis, database and Revenuecat is just a few clicks. Afterwards I bring it into Cursor.

Cursor is my workhorse when I've spent my daily credits on Claude Code. The designer who can prototype their own ideas has an unfair advantage. You're not waiting for dev resources. You're not explaining micro-interactions in Loom videos. You're just... building.

Claude Code made this accessible. You don't need to be a "real" developer. You need to be curious enough to try.

## Phase 4: Back to Figma

(Description: Screenshot of Lummi.ai interface displaying a grid of high-quality lifestyle product photography with various items including sunglasses, beverages, and lifestyle shots with modern aesthetic.)

Sometimes the prototype reveals what the static designs couldn't.

I'll go back to Figma, iterate on main screens based on how the build *feels*, then return to code.

**Design → Code → Design → Code**

The loop is the process now. Anyone still treating design and development as separate phases with a hard handoff is working with an outdated model.

## Phase 5: Visual Content

**Tools:** Midjourney, Lummi.ai

Midjourney for custom visuals. Still unmatched for creative image generation.

Lummi.ai for quick, high-quality alternatives when I need something faster or more grounded. Often times I just prefer the style of images on Lummi over midjourney - it varies.

Hot tip: Midjourney's image-to-video feature is surprisingly good for quick attention-grabbing content. Social posts, hero sections, whatever needs movement. It's not replacing proper video production, but for quick wins, it's excellent.

## Phase 6: Motion

(Description: Screenshot of Jitter.video animation editor interface showing a composition with the text "BOLD" and "motion" overlaid on an image with a man in sunglasses, complete with timeline and animation controls at the bottom.)

**Tools:** Claude Code + Remotion

For spec work and motion design, I've started to use Claude Code with Remotion skills.

Programmatic video that I can iterate on like code. Change timing, swap assets, adjust easing. All without reopening After Effects.

Motion designers, seriously look into this. The mental model shift from timeline-based editing to code-based composition takes adjustment, but the iteration speed is worth it.

If I need something quick for social media or a pitch, I default to Jitter.video - it's one of the best online animation tools I've used in a long time.

## What I'm Adding Next

Two things I'm actively experimenting with:

### Claude Code + Framer MCP

The goal: let AI handle the "boring" Framer work.

- Accessibility content
- Responsiveness setup
- Figma to Framer cleanup

The creative decisions stay mine. The tedious implementation? Automated. This is the unsexy automation that actually saves hours.

### Claude Code + Figma MCP

Our design system at work is a mess. Multiple designers contributing, documentation slipping, organization deteriorating over time. The usual entropy.

I'm planning to use this for:

- Adding descriptions to components
- Organizing and cleaning up the design system
- Optimizing token structure

AI as design system janitor. It's not glamorous work, but it's the kind of maintenance that makes everything else faster.

## The Full Workflow

**Concepts:** v0, Superdesign, Variant.ai
↓
**Iterate:** Figma
↓
**Build:** Claude Code, Vibecodeapp, Cursor
↓
**Iterate again:** Figma
↓
**Images:** Midjourney, Lummi.ai
↓
**Motion:** Claude Code + Remotion

## What I've Learned

**AI for speed and volume, humans for taste and decisions.** The tools are getting better at generating options. They're not getting better at knowing which option is right.

**The design-code loop is the new process.** Treating them as separate disciplines with a handoff moment feels increasingly outdated.

**"Boring" work is the best place to automate first.** Don't start with the creative stuff. Start with the tedious stuff you've been avoiding.

**Your workflow will look different than mine.** That's fine. The point isn't to copy someone else's setup. It's to find what fits how you think.

## Tools Mentioned

**Ideation:** @v0, @SuperDesignDev, @variantui

**Design:** @figma

**Build:** @claudeai, @vibecodeapp, @cursor_ai

**Images:** @midjourney, @lummipics

**Motion:** @claudeai + @Remotion

**Coming soon:** Framer MCP, Figma MCP

The landscape keeps shifting. What works today might be obsolete in six months. But the principle stays the same: use AI where it's strong, stay human where it matters.

**What's in your stack?**