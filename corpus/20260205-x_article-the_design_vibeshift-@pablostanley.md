# The Design Vibeshift

(Description: Illustration of two people collaborating at a round table. One person in a turquoise shirt sits on the left with a laptop displaying design tools. The other person in a black shirt sits on the right with another laptop. Between them are various sketched design elements, UI components, and prototyping tools floating in the air, rendered in a friendly, hand-drawn style with muted colors including teal and pink accents.)

A change is happening... for a lot of designers, code is becoming our new canvas

I've been watching my feed on X and the vibe has changed. More and more, I see designers sharing finished experiments or prototypes they coded themselves, rather than static Figma files. Moving from working on a canvas to talking to an LLM. The conversation isn't "here's a design I made" anymore... it's "here's something I shipped this afternoon."

Figma is a great tool, real-time collab, no local file drama, browser-based so u could work from anywhere, focused on ux/ui, an infinite canvas, components… etc etc. But heading into 2026, the conversation has changed. Designers are increasingly calling it slow or less central compared to AI tools like [Claude Code](https://claude.ai/code), [Cursor](https://cursor.com/), and [v0](https://v0.dev/).

It's not about tools like Figma or Webflow disappearing. It's about code becoming the primary playground for creative workflows.

(disclaimer, I work at v0, but these are my personal opinions)

## What Designers Are Saying

(Description: Hand-drawn cartoon illustration of a person with a large expressive face surrounded by multiple computer screens and digital interfaces, rendered in black ink with energetic linework, depicting creative overwhelm or active multitasking in design work.)

A general sentiment I keep seeing is designers describing a hybrid loop: Idea → Code → Shipped. Code feels quicker for complex screens, or interactions that would require a ton of work in a static design tool. You can quickly see if the animation feels right. You can pull real data and see your idea come alive more faithfully. You can find all those edge cases you'd miss in a design tool (or that you're too lazy, like me, to even design).

I've seen a ton of people prototyping in Cursor, v0, and Claude Code and seeing Figma as supplementary... like a snapshot in time, not the source of truth anymore.

Code is the source of truth.

[Hardik Pandya](https://x.com/hvpandya), Head of Design at Atlassian, [posted about](https://x.com/hvpandya/status/1977779726308807066) why Cursor beats Figma for him after months of use:

> "I absolutely love Figma and have used it for years. But ever since I picked up Cursor over the last 6 months, I find it hard to go back to designing on canvas."

He lists the advantages of working in code: real-time behavior, responsiveness, live data, micro-interactions, and no manual duplication for states. He also [shares](https://x.com/hvpandya/status/2013240464879894786):

> Figma is very quickly becoming a huge bottleneck in building products.

Atlassian's design team published ["Handoffs into Handshakes"](https://atlassian.design/articles/ai-design-tools/handoffs-into-handshakes) about their shift to AI-assisted design. The framing is telling... it's not about replacing tools, it's about collapsing the gap between designing and building.

The sentiment I keep seeing: building out a design system in Figma feels archaic after using Claude Code to create stuff

[Adam Whitcroft](https://x.com/AdamWhitcroft/status/2009317293327892837)

> "It feels like the days of Figma as the source of truth for design are numbered. I think there's still a use case for initial direction setting / mood exploration, but I just don't see a strong case for keeping those monolithic files of an entire product area up to date anymore."

[Darrin Henein](https://x.com/darrinhenein)

> "…my conviction is that we move our design systems from Figma into github, from an abstraction layer into our product — our source of truth becomes codified, version-controlled, branchable and machine-consumable. Our canonical definitions move from the design tool to the product itself."

## Not Everyone's All-In

(Description: Minimalist black ink illustration of a cartoonish figure with a frustrated expression standing next to a small mechanical robot with antenna and control panel details, symbolizing the interaction between human designers and AI tools.)

Not everyone has fully switched though.

Some keep Figma for exploration, alignment, or detail work like components and consistency. [Rogie](https://x.com/rogie), a product designer at Figma, [put it well](https://x.com/rogie/status/2001684053259620387):

> "Vibe coding is incredible, and it's enabled me to communicate designs faster, easier, in fractions of the time it took. So far, nothing is replacing iterating by duplicating and riffing and exploring the solution space... I guess I'm saying: Do both."

Mobile-focused folks mention vibe-coding from scratch works better than forcing Figma fidelity into tools like React Native. And there's a valid counterpoint too... if everyone's shipping directly to code, who's keeping track of the bigger picture? Consistency across screens? The design system?

The pragmatists are somewhere in the middle: Figma for core screens, code for the rest… I'm a bit like this at work, tbh

[Greg Huntoon replied](https://x.com/GregHuntoon/status/2001713813192843565):

> "My new default seems to be: Figma Design → Make → Copy Designs back to Design → Make roundtripping, with lots of GPT-cleaned prompts, Cursor/VSC CoPilot, etc."

## My Own Experience

(Description: Vintage-style illustration of a cartoon character working at a retro CRT computer monitor labeled "VIBES" displaying code. The character is surrounded by scattered building blocks, papers, and design elements, rendered in black and white line art with an 80s aesthetic.)

I've felt this pull myself over the last couple years.

Less Figma for product work, more jumping to [CodePen](https://codepen.io/) with ChatGPT in the early days, then using [v0](http://v0.app/) for a tool where you can actually preview what you're doing, and lately Claude Code for complex stuff where I need access to the CLI. Animations and interactions just land better with real code ([Framer Motion](https://motion.dev/), Tailwind, etc.). Even basic notes or screenshots? CLI these days.

I wrote about this shift in [my terminal article](https://pabs-writings.vercel.app/posts/how-i-stopped-worrying-and-learned-to-love-the-terminal). Honestly, while I still use Figma at work, I use it mostly as a wireframe, a starting point I can feed to an LLM so I don't have to describe everything. The Figma wireframe (using actual components from our system) becomes part of my initial prompt. But I haven't used Figma for more finalized UI/UX work in a long time now.

Weirdly, I've been using it a ton for marketing assets. But even that, can feel repetitive, and I have used the terminal with stuff like [Sharp](https://sharp.pixelplumbing.com/) and [Remotion](https://www.remotion.dev/)

## What's Actually Happening

The mix makes sense right now. Tools like Figma for broad ideation and team sync, AI/code for fast iteration and shipping. Figma itself isn't standing still... [Figma Make](https://www.figma.com/make/) is their answer to this shift, turning designs directly into working prototypes with AI.

But here's the thing... the tools that let you go from idea to shipped product in the same conversation? Those are winning attention. Not because they're perfect, but because the feedback loop is immediate

When I describe something to v0 or Claude Code and see it running in my browser thirty seconds later, that's different from pushing pixels and then waiting for a developer to interpret my intent. The design IS the code. There's no translation layer.

That pushes design toward strategy. Which is what the best designers have always wanted anyway. You can't craft a good experience if the business itself is confused about what it offers. So we've always pushed for a seat at the table where the real decisions happen

If you're deep in Figma, try vibe-coding one screen. Prompt Claude or Cursor, tweak live, feel the difference. You don't have to abandon your tools... just see what the conversation is about.

I'm still figuring this out too. What's your current setup?

---

This was originally posted on my Substack last week, if u wanna follow https://pablostanley.substack.com/p/the-design-vibeshift

Also, I invite u to try two tools I'm involved with: [v0](http://v0.app/) (where I work!) and [Efecto](https://efecto.app/) (a personal project)