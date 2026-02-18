---
url: https://x.com/pablostanley/status/2019813770336620560
author: Pablo Stanley (@pablostanley)
captured_date: 2026-02-13
---

# How I Stopped Worrying and Learned to Love the Terminal

I'm a designer. For years, my world has been Figma, Sketch, Adobe. Nice GUIs with buttons and panels and things I could click. The terminal? That was a black rectangle where the dev team did hacker things. No buttons. No UI. Just a blinking cursor judging you for not knowing what `ls -la` meant.

And now? My design tool of choice is the terminal.

I know. For a designer, this sounds ridiculous. But now the alternative, tools like figma, now even feel old-school…

## here's how it happened

This is a comic from a few years ago… u can see I revered the terminal with respect (and fear)

(Description: A four-panel comic strip showing interactions between an engineer and a designer. Panel 1: Engineer says "NO PROBLEM, WE CAN FIX THIS ON THE TERMINAL" and Designer responds "WHOA, YOU'RE A HACKER!" with "NO, IT'S JUST THE TERMINAL". Panel 2: Designer asks "WHERE ARE ALL THE BUTTONS, ICONS, AND DROPDOWN MENUS?" and engineer responds "IS THIS... THE MATRIX?" with "YES." The comic is titled "AN ENGINEER HELPING A DESIGNER" and signed with "PABLO STANLEY")

## The Shift

Last year I started using Claude Code, as u may already know, a CLI tool... meaning, I would have to use that scary terminal thing.

But... while it took me a bit to get used to it, it wasn't so bad because instead of having to learn a ton of commands, I just... talked to it. I described what I wanted, and it figured out the rest.

Suddenly, the terminal wasn't about memorizing commands. It was about having a conversation.

I started building things. Real things. Prototypes that actually worked, not just pretty pictures of what an app could be. Recently, efecto.app and remoto.sh are stuff I actually shipped. And I've been able to iterate faster than I ever could in a traditional design tool because the code was real from the start.

I should say: I've had a lot of help. I work with a team of devs and designers at Vercel who gave me access to the v0 repo, answered my dumb questions, and pulled me out of holes when I got stuck. A lot of what I know comes from watching how they work and asking "wait, what did you just do?" If you don't have that, the community around these tools is pretty active. People share tips, help troubleshoot, and generally don't make you feel dumb for not knowing things (well… on reddit they might).

So… anyway… let me do a braindump of some stuff I've learned and might help u stop worrying and learn to love the terminal.

## You Don't Need to Memorize Anything

Let me save you some anxiety: I still don't know most terminal commands. And it doesn't matter.

You really only need a couple of commands that u will use a lot... `cd`, which is change directory. You want this so you can work on the correct folder on your computer. I usually put `cd` then drag-and-drop the folder I want to work on from the finder to the terminal, this will put the full folder destination.

Also, `npm run dev` so you can test what you've built locally (u will start visiting `http://localhost:3000/` a lot)

Did something work last week but can't remember? Hit `ctrl+r`, type a few letters, and it finds it.

And obviously, `claude`, so you can run claude code. After that, once it's open... then u can actually just ask it to do the things you want and it will run the necessary commands in the terminal for you (but, asking for permissions... which can be annoying… a dangerous tip about it at the end of this article.)

But, the thing is... you don't need to be a command-line wizard. You just need to know how to navigate and let the tool do the work.

I've been using the Ghostty terminal. It's fast, looks native, doesn't require an account. I've also run Claude Code inside Cursor's integrated terminal, which is nice when you want to browse files in the IDE while Claude does its thing. Cursor's autocomplete is annoying most of the time but occasionally useful. Honestly though, I haven't optimized any of this. The default terminal works for me. And I think I'm not alone, I've seen others also use Claude Code inside Cursor and kind of ignore its chat interface lol

(Description: A simple line-drawn illustration of a person with a confused expression sitting at a computer)

## What Actually Works

After months of using this setup, here's what I've learned, both from my own experience and from watching how the people who built these tools use them.

**Start with a plan.** Before building anything, I use plan mode constantly (shift+tab twice in Claude Code). Go back and forth until the approach makes sense. A good plan means Claude can usually get things right on the first try instead of going in circles.

**The most important thing is giving Claude a way to verify its work.** If Claude can test what it built, the quality goes way up. For UI work, that means actually opening the browser and checking if it looks right. I use Agent Browser for this. It's a headless browser that Claude can control directly. Claude opens the page, takes screenshots, clicks around, verifies things work. It can even test responsive design by resizing the viewport to different sizes and screenshot each one. This catches so many issues: buttons that don't align, text that overflows, hover states that look wrong.

**Don't trust unit tests blindly** though. AI-written tests often just confirm that the code does what the code says it does. Which is useless if the code is wrong. The tests will all be green while everything is broken because the AI will happily change the test to match the broken code.

**If you're building something complex**, accept that the first version probably won't be the final thing. You'll end up with duplicate implementations, bypassed abstractions, seven nearly-identical types... dude, it's insane how bad it can get if u let it loose and unguided lol... but that's okay. The rewrite will be more solid because now you know what you actually need. Just don't refactor forever. Sometimes good enough is good enough... (that's why plan mode is important, so you don't end up in these loops)

**Before adding features**, make sure the basics work. Login. File saving. Undo/redo. Getting these right early prevents a lot of weird workarounds later.

(Description: A cartoon illustration showing a character with a round head wearing a hat, surrounded by floating boxes and electronic components, appearing to juggle multiple tasks with dynamic motion lines)

## Design Stuff

As a designer, here are specific things I've learned to tell Claude when working on UI.

For **typography**, I ask claude code to use `text-balance` for headings and `text-pretty` for body text. As a type snob, I ask it to use `tabular-nums` for data and numbers. To avoid awkward lines hanging or just unbalanced cards and stuff, I ask it to use `truncate` or `line-clamp` for dense UI. And ask it to never touch `letter-spacing` unless it reaaaally needs to.

For **visual design**, no gradients unless specifically requested (especially not purple or multicolor ones since omg, that will be a clear sign that your app is AI slop lol). No glow effects as primary affordances. Stick to the default shadow scale. Limit accent colors to one per view and use existing theme tokens before adding new colors. Every empty state needs one clear next action (it loves leaving empty states as just informational which is a ux no-no).

For **components**, use accessible primitives like shadcn/ui or radix. These are really easy to edit with tailwindcss and customize to make them your own... but honestly, shadcn, out of the box, is already great for most stuff.

Add `aria-labels` to icon-only buttons. For animation, never animate layout properties like width, height, or margins and just stick to `transform` and `opacity`. Also, ask it to use `ease-out` on entrance transitions.

I'll go deeper on the design stuff in another post. There's a lot more to say about working with AI to make our AI slop not look so sloppy.

## Running in Parallel

One thing that changed how I work: running multiple Claude sessions at once. I usually have 3-5 terminal tabs going, plus a few web sessions on `claude.ai/code`. I start tasks from my phone sometimes and check in on them later.

It sounds chaotic, but it works. While one Claude is building a component, another can be writing tests, and a third can be researching how to approach a tricky problem.

The trick to making this work without everything colliding: **git worktrees**. When I want multiple Claudes working on the same project simultaneously, I tell each one to create its own worktree and branch. That way they're not stepping on each other's files. Each session does its work in isolation, runs tests, verifies locally, and opens its own PR. I just tell Claude something like "create a new branch off main, do the work in its own git worktree so it doesn't interfere with other agents, run the tests, check it in the browser, then open a PR." Claude handles the rest.

(Description: A line-drawn illustration showing four simple computer/robot characters arranged in a circle with arrows connecting them, suggesting communication or workflow between multiple processes)

## Images and Media

Here's something I didn't expect: the terminal is now where I do a lot of my image work too.

I use **Sharp** for generating images programmatically. Need a grid of avatars? A set of placeholder images at specific sizes? Social cards for blog posts? Claude writes a Sharp script, runs it, done. No opening Figma, no exporting, no fiddling with settings. For videos and GIFs, **ffmpeg** handles trimming, compressing, converting formats, extracting frames.

Claude creates these scripts once, and then I reuse them. Need to batch-compress a folder of PNGs? There's a script for that. Need to convert a screen recording to a GIF under 5MB? Script. Over time, you build up a library of these little utilities. Claude remembers they exist and reaches for them when relevant.

(Description: A cartoon illustration showing a child-like figure climbing up a large pyramid or triangle structure. At the top is a small computer/monitor. At the base are various scattered boxes and tools. The figure appears to be working to reach the top.)

## Skills and Shortcuts

Claude Code has this concept of "skills" which are custom commands you define that Claude can invoke when needed. I have skills for things I do repeatedly: optimizing images, generating social cards, creating responsive screenshot sets, compressing videos for web.

The cool part is Claude picks the right skill dynamically. I might say "make this ready for Twitter" and Claude knows that means: resize to 1200x675, compress under 5MB, convert to the right format. I didn't have to specify the skill. Claude figured out which one applied. You define these in `.claude/commands/` and they become part of your toolkit.

Also, Vercel recently launched **skills.sh**, an open directory where devs share reusable skills. There are skills for react best practices, front end stuff, even companies like Stripe jumped in with their own best-practice guides.

(Description: A humorous illustration of a character holding what appears to be a large wrench or tool, with a mischievous expression, suggesting capability or problem-solving)

## Connecting Your Tools

Through something called **MCP**, you can connect Claude Code to other tools. For example, Figma, Notion, Slack, Google Drive and even Blender (seen some crazy stuff done with that, omg!). So instead of copy-pasting specs or describing what you designed, you can pull that context directly into the conversation.

For **GitHub**, there's a GitHub Action you can install with `/install-github-app`. Once it's set up, you can mention `@claude` in PR comments or issues and it'll respond. Implementing features, fixing bugs, doing code reviews. It follows your CLAUDE.md guidelines so the code stays consistent with your project's patterns.

For **deployment**, there's a Vercel plugin you install with `/plugin install vercel@claude-plugins-official`. After that, you can just say "deploy this" and Claude runs `/deploy` to push to Vercel. It also adds `/vercel-logs` for checking what went wrong when something breaks.

There's also the **CLAUDE.md** file which is a markdown file in your project where you document your design patterns, preferences, and rules. Claude reads it at the start of every session. So instead of repeating yourself, "yo, use our spacing scale!" "stick to these colors!" "we use shadcn for components!!!" you write it once and Claude remembers. Every time Claude does something wrong, I ask Claude to add it to the file (oh, yeah, claude can update its own claude.md haha).

Over time, Claude gets better at matching how you work and know more about your project.

(Description: A line-drawn illustration showing a figure at a command-line interface (v0 vibes display visible on screen), surrounded by scattered tools and components, working at a retro-style computer setup)

## If You're Not Ready for the Terminal

If all this still feels like too much, there's a stepping stone: **v0** from Vercel. (disclaimer, I work there). It's a visual interface for generating UI. You describe what you want, or even paste a screenshot, and it generates the code. No terminal required, you preview what you get right there, and it has all the pro benefits from claude code (connects to github, to vercel projects, to databases, etc).

U can also start with v0, put your project on github, then open that project with claude from the github repo, push the changes, and later go back to working on v0 again... vercel and github become your source of truth.

## The Weird Part

The weird part is how natural this feels now. I used to think the terminal was for a certain type of person... not me. Someone who thinks in code and prefers typing to clicking.

But it turns out the terminal becomes just another interface. And with the right guidance, it can be surprisingly good for design work. Honestly, I haven't used Figma for UI/UX work in a long time now... I only use it for marketing assets now... but even that, I can do with the terminal, Sharp, and Skills.

I just describe what I want in plain language, get something real back, and iterate by having a conversation. It's not that different from working with a great developer, except it's available at 2am when I have a dumb idea.

If you're a designer and you've been avoiding the terminal, I get it. I was you. But maybe give Claude Code a try. Start with something small.

I'm still figuring this out too. If you know better ways to do any of this, or if I'm doing something obviously wrong, I'd like to know. I'm `@pablostanley` on Twitter.

(Description: A cartoon illustration showing three figures with chaotic hair/expressions, each sitting at laptops surrounded by floating documents and scattered papers, suggesting busy multitasking or collaboration)

## Further Reading

If you want to dig deeper: the **Claude Code docs** are the best place to start, along with the **Chrome extension** for browser-based testing. **Boris's thread** on how he uses Claude Code and **this one** about how the Claude Code team uses their own tool.

For image work, check out **Sharp** and **ffmpeg**. For connecting your design tools, look into **MCP**. And if you want to start more gradually, **v0** is a good visual-first option with all the superpowers of the terminal (github, repos, branching, virtual machines, omg)

also, try a tool I've been working on: **https://efecto.app/**

oh, and the last tip… if u know what u want, and you're sure claude can handle it without hand holding, then… before boot claude with this:
```plaintext
claude --dangerously-skip-permissions
```

like it says, it will stop **dangerously** asking for permissions.

---

This post was originally posted on my substack... that's where I post stuff first, if u wanna subscribe :)

https://pablostanley.substack.com/

**Engagement:** 11 replies, 41 reposts, 445 likes, 804 bookmarks, 79.3K views | Posted 8:41 AM · Feb 6, 2026