---
url: https://x.com/rjs/status/2020184079350563263
author: "Ryan Singer (@rjs)"
captured_date: 2026-02-13
id: SOURCE-20260207-013
original_filename: "20260207-x_article-shaping_0_1_with_claude_code-@rjs.md"
status: triaged
platform: x
format: article
creator: rjs
signal_tier: strategic
topics: [claude-code, vibe-coding, best-practices, tutorial, case-study]
teleology: implement
notebooklm_category: claude-code
aliases: ["Ryan Singer - Shaping 0-1 with Claude Code"]
synopsis: "Step-by-step walkthrough of shaping and building a small project from zero to working product in Claude Code, using Ryan Singer's shaping skills from GitHub. Shows the complete process with no steps skipped, from initial prompt to finished product."
key_insights: ["Shaping (defining the problem before building) is even more important when working with AI — the first prompt sets the trajectory", "The complete 0-to-1 process in Claude Code can be demonstrated without skipping steps, showing the real workflow", "Shaping skills from product management translate directly into effective AI-assisted development"]
---
# Shaping 0-1 with Claude Code

Here's what it looks like to shape and build a small project from 0-1 in Claude Code. This example uses my shaping skills on GitHub. I am not skipping any steps here. You're seeing the whole thing from scratch to working product.

## 1. The first prompt

I have something in my head. I open Claude Code in a new blank directory. I describe what I'm envisioning:

> I want to create a simple TUI app here. it should talk to the internet to get a reliable source of what the current time zone is in a specified locale. eg Detroit. or Brasil. or Poland. Then it should show a table of every hour for each of the locales that i ask. each locale is a column in the table, and the rows are hours in the day, and the local time then is in each cell. i should be able to specify a few default time zones that are always loaded. it's important that it fetches the data freshly every time it loads (so it is accurate), and it should default to a list of the hours in the current day. (eg the next 12 hrs). There should be an input field at the bottom where I can make requests to a very simple local LLM to instruct the app to add/remove locales and or change the "time window" which is the day that we are looking at. via tool calls. so i could be able to say "today" or "feb 12" etc. "show me times feb 12 in brasil." and the screen will reload to show me the table with brasil included and the time window changed to feb 12 (of the current year).

Before I hit enter ... I added one specific thing to invoke the shaping skill:

> use your shaping skill to capture the requirements and tease apart the key parts of the solution A that i have specified here

I'm asking it to use the skill to **separate problem and solution**. That way we can start to iterate on both. When I say "solution A" I am using terminology from the skill. I'm assuming we might have different solution options A, B, C ... and we'll choose from them as we learn what is possible and desirable.

Claude Code answers:

- I'll start by capturing the requirements and shape you've described. Let me first check what's already in the project directory.
- Empty project. Let me create the shaping doc to capture everything.

It creates a first draft of `shaping.md`. The doc has a nice first draft of problem/outcome, the requirements, and the initial shape. I've got a Markdown previewer running that hot reloads the file. Here's what that doc looks like.

First, Claude started the doc with a frame in the form of problem/outcome:

(Description: Screenshot of a markdown document showing a "Frame" section with "Problem" and "Outcome" subsections detailing the time zone coordination challenge and desired user experience)

Below that, it extracted the requirements. The skill calls these "R" for reference (we'll see why later).

(Description: Table showing requirements R0-R10, including showing time zone tables, fetching data from internet, accepting locale names, supporting default time zones, time window defaults, LLM input field, adding/removing locales via tool calls, changing time window via tool calls, screen refresh capability, TUI implementation, and using a local LLM)

Note it's not perfect. R0-R5 are nicely general. They would apply to any solution we come up with (eg a web app). R6-10 probably belong in the solution, not the requirements. But this is fine for a first draft.

The last thing in the first draft of the doc is the first Shape A:

(Description: Shape A section titled "Single-shape TUI with internet tz lookup + local LLM input" containing a table with 6 parts (A1-A6): TUI shell, Time zone resolver, Hour table builder, Default config, LLM input handler, and Tool executor, with yellow warning flags on unknowns A2 and A5)

Those parts A1..A6 are its first whack at "finding the elements" at a high level. They're the moving parts / mechanics of the solution. Notice the unknowns that are flagged (⚠️). It means those parts are sketchy or fuzzy -- it doesn't know how to unpack them into detail yet if asked. Okay so that's what's in shaping.md. But for a simple project like this, I'm not even looking at that yet. I'm just relying on the markdown file to have a record of the context we're building up.

## 2. Checking the fit

Without looking at the markdown file, the first thing I asked to understand what it did was this:

> show me R x A

This is shorthand for "show me the fit between the requirements (R) and the shape A." In shaping terminology this is called a fit check.

This is the output:

(Description: Fit Check table showing requirements R0-R10 mapped against solution parts A1-A6, with green checkmarks (✓) and red X marks (✗) indicating which parts satisfy which requirements, plus a legend explaining flagged parts)

This is what's actually in my head whenever I'm working on a problem. Whether it's on the whiteboard, on paper, or here in the terminal. I want to see what's solved and unsolved, what's known and unknown, what's a constraint vs what's a potential solution.

The reason I reached for this first is it gives me a jumping in point. I'm getting a read on which parts of the problem it thinks are answered. I can see what it thinks is solved and what isn't. If I like how it's going, I can just let it roll. But if I start to get new ideas about a different approach ("should this really be a TUI? maybe it's a web app") I can just ask for that as a new shape B without losing R to test against and without losing A to fall back to.

Right now, I want to understand A better. (Remember I haven't looked at the markdown file yet.) So I asked it to rotate the fit check. Instead of showing R with A flattened into pass/fail values, show me all of A against all R.

> can you show me A x R ... that is, rotate the fit check

The output:

(Description: Rotated Fit Check table showing parts A1-A6 mapped across all requirements, with checkmarks and X marks rotated 90 degrees, plus a summary noting that A2 and A5 need resolution and suggesting two unknowns would fill all five green indicators)

I love that commentary at the bottom. It's telling me the next steps are (1) to pick a tz API (A2), and (2) pick an LLM runtime. That tracks what I'm thinking. First we can get this thing to just render time zone tables, and then after that we can figure out how to interactively change which time zones and dates are showing up. Probably there are things we're missing along the way, but pursuing the tz API will uncover those. As we discover missing requirements, we can populate R. Or if the solution just starts to unfold, we can populate A. Eventually the design will be clear enough to say "go build that."

## 3. Spiking the first unknown

So let's make more progress by spiking the tz API part.

> Please spike A2

("Spike" is a term I learned from engineer colleagues over the years. It means dig into a question in more concreteness to come back with information about what is possible and/or how it could work.)

I'm trusting that the Rs and context of the rest of A is going to help it know what to ask for. The first output is this:

- Write (`spike-a2.md`)

It knows from the shaping skill to write the spike as a separate markdown file, so all the findings are saved for reference and inspection. It summarizes the output into the chat, describing two different approaches and a suggestion to improve R (!):

(Description: Screenshot of spike-a2.md markdown file showing context, approaches, and findings related to timezone API options for the solution)

This is exactly like what happens on the whiteboard in a live shaping session. "Oh, what if we did THIS instead..." It's telling me that it doesn't need to go to the internet to look up the timezones (that was just a random unchecked assumption in my original idea for this little app.) And further -- I love this -- it's suggesting we revise R. It doesn't make sense for our requirements to say "fetch from the internet." In Claude's words...

- **R1 says "fetch tz data from the internet on every load." But if the tz library is local and handles DST rules correctly, there's nothing to fetch — the data is accurate by design. The "freshness" concern is really about keeping the OS tz database updated, which happens through normal system updates. Should we reword R1, or is there a real reason you want a network call on every load?**

> Let's update A with Approach 1

- Now I'll update the shape, R1, and the fit check to reflect Approach 1.

## 4. Spiking the local LLM

> Can you spike the local LLM piece?

This time let me show you the full output of a spike. Using the shaping skill, it wrote another spike document. The structure is like this... (I'm taking screenshot from the Markdown previewer.)

The spike doc opens up with some **context** explaining what we're trying to answer. (In my experience, the #1 rule of spiking is to never make it a yes-or-no question. A spike should mean we are gaining objective information in order to make a decision.)

Then after the context, there is a table of **questions** asked. In this case, because it generated the document and performed the spike in one go, it's already filling in the answers besides the questions as well. (When defining a spike for humans, there are no answers in this section of course.)

(Description: Screenshot of spike-a5.md showing context, goal, and questions table with answers regarding LLM runtime options, models, tool calling protocols, latency, and language/library choices)

I think it went a little overboard with the number scheme (relating each Q to part A5). Simply numbering the questions is enough. But okay.

Below that are the details findings:

(Description: Continued spike findings showing recommended stack with Ollama runtime, Qwen model options, native tool calling protocol, Python ollama package, and example code for tool calling)

That's what's in the doc. Back to the console, here's what I'm seeing after it wrote the file:

(Description: Console output showing A5 Spike Results with recommended stack, findings about regex parsing options, and confirmation of tool calling approach)

"But for V1, LLM-only is simpler" — I appreciate that. I tell it to put this into A. And here's where we stand:

(Description: Updated Fit Check table now showing all green checkmarks for all requirements, indicating all unknowns have been resolved)

Green!

## 5. Adding missing detail with a sketch

Now that the approach seems good, I ask it to spell out A in more detail:

(Description: Markdown detail showing the concrete shape A with six parts: A1 TUI shell, A2 Mechanism using zoneinfo, A3 Hour table builder, A4 Default config, A5 LLM input handler with tool definitions, A6 Tool executor with validation)

Now, I'm looking at these six parts... and I'm comparing them to what's in my head. I've had a fat marker sketch in my head for his the whole time ... and I think there's something missing. So I open up TLDraw and I make the sketch:

(Description: Hand-drawn sketch showing the UI layout: a header with "Feb 7, 2026" and date label, three columns labeled "Portugal", "Detroit", "Pacific" with wavy lines representing time data, and at the bottom an input field with placeholder text "Feb 12 in Brazil?")

Should I have done this first? I don't know. It was easier just to describe it in words this time. But now ... I'm concerned that I don't see the date window mentioned as an explicit UI affordance in the parts list. All of the UI has been packed into A1 "TUI shell", which is a smell to me. So I literally drop this screenshot into the TUI and ask it to consider this.

> We're missing something. We should make sure that there's an explicit affordance for the date, so it's always clear what the state is and how it's changing as we interact with natural language in the field. See this sketch. [Image #1]

Charming! 😂

(Description: Updated A1 TUI shell showing three distinct regions: date label section (A1), column headers section, hour rows section (A3), and input field section (A5))

Last thing ... I realized when drawing the input field in the sketch that I might want to just tell it to change the time, or the locale, or both. It might not be necessary, but I'll feel more confident if we express that in the requirements.

> Add R that we should be able to change the time window and add/remove locales via the input field, either independently or together.

Here's our back and forth on that:

(Description: Console conversation showing Claude's response about single commands combining actions (e.g., "feb 12 in brasil" or "add Detroit") and confirmation that R6 and R7 already cover independent cases, with R11 added for combined actions)

## 6. Breadboarding

At this point, for how simple this app is, I might be able to just say "make an implementation plan and go build." But I'd like to use this opportunity to show how I've been handling larger projects that are too hard to explain in an article like this.

In a larger / harder project, it's important to create vertical slices (what the book calls "scopes"). A vertical slice is a subset of the overall project that has both backend and frontend in such a way that you can actually demo something. The reason I need this in a big project is I want to verify that this is heading in the right direction by trying part of it. I don't want it to one shot a giant thing, and then have to churn throwing big pieces away or get tangled into a bunch of interdependent decisions that I don't like.

I've learned that the best way to slice vertically is to first draw a breadboard. A breadboard is a technical diagram that combines UI and code into one circuit. The mental picture is an electrical circuit with switches and LED lights (UI affordances) and components making it work (resistors, ICs, capacitors, etc).

When we have a wiring digram that shows all of it in one circuit, that's good primitive for slicing into specific parts to build out. Anyway that's spelled out in the skills. I'm just going to ask Claude Code to breadboard now.

> let's breadboard A

Claude says:

- Done. Breadboard is in the shaping doc. The system has 5 UI affordances, 11 code affordances, and 3 data stores across 3 places (TUI, Ollama, Open-Meteo). Ready to slice when you are.

This means there will be a Mermaid diagram in the shaping doc now. I hacked a little CLI tool called `beam` that finds any Mermaid code in a Markdown file and projects it to a local TLDraw instance. I use the TLDraw to zoom in and out, and it hot reloads as any changes are made by the LLM.
```
rjs@Mac tick % beam shaping.md
Watching: /Users/rjs/apps/tick/shaping.md
HTTP server: http://localhost:3456
WebSocket server: ws://localhost:3457
Watching: /Users/rjs/apps/tick/shaping.md
File detected, rendering...
Found 1 Mermaid block(s)
Opened browser: http://localhost:3456
[0] Mermaid
Client connected
Found 1 Mermaid block(s)
 Mermaid
```

(Description: TLDraw application window showing a breadboard diagram with nodes and connections representing the system architecture including UI affordances (pink boxes) and code components (tan/beige boxes) across three layers)

Sometimes I'll see things in this view that lead to iteration. In this case, I'm happy to move on to slicing so we can see something working.

## 7. Slicing vertically (into demoable scopes)

Under the hood, each element on the breadboard is an affordance located in a place. Affordances are UI or code affordances (something you can do as a user or with the system) and they each have IDs. The wiring is defined as a table of "wire" relationships between the IDs. This gives us a tidy little formalism for the LLM to slice with. It can define a slice as a subset of the affordances, keeping the wiring intact.

> let's slice it

- The system is compact — I see two natural slices:

(Description: Slice Summary table showing V1 (Table with defaults) and V2 (LLM commands work) with their respective parts, affordances, and demo descriptions)

Note that each slice includes a description of what to demo. This is what makes them vertical. TLDraw hot reloads with the sliced breadboard:

(Description: TLDraw showing the breadboard split into two colored regions (green for V1, blue for V2) with pink UI affordances and tan code components distributed across the slices)

I want to see the first slice working! Let's do it.

## 8. Building the first slice

> Please make an implementation plan for the first slice. include how you will test it yourself to ensure it's working.

Claude Code put itself into plan mode, then started working. Here's the output:

(Description: Console output showing V1 implementation plan with project structure, files to be created (project.toml, UV lock, src/tick/, tests/), and verification steps)

I ran it .. and it works!

(Description: Terminal screenshot showing the working time zone table application with columns for Detroit, London, and Tokyo with hour-by-hour times listed)

Time for the next slice.

## 9. Building the second slice

I gave it to the same prompt to build the second slice. After whirring and finishing, it was ready to test. On first run, the app crashed. To save myself from going in circles with who knows how many errors ... I gave it the following instruction:

> Please run the app yourself and interact with it in order to verify that it works. Cover all cases like "add brazil" or "feb 12" or "paris feb 18"

And it worked!

(Description: Terminal recording/GIF showing the interactive time zone app with user typing commands like "add brazil" and "feb 12" with the app responding dynamically to update the display)

## Conclusions and next steps

Everything I pictured in my head when we started is working. And we got there with very little of the painful back-and-forth: "No that's not what I meant ... no that doesn't work." And the back-and-forth we did have felt meaningful: "Ah, we that's a better solution. Ah that requirement should be like this.."

Maybe Claude could have one-shot such a simple app. But going through this process means I have a view of how it works. I understand the system. And I can ask questions about all of the documents that explain how and why it's put together the way it is when I want to make improvements and changes.

If you want to dig deeper into this, here are some suggestions:

- Check out the repo for this project with all the markdown docs that Claude generated here: https://github.com/rjs/tick
- Try out the shaping and breadboarding skills on your own project: https://github.com/rjs/shaping-skills
- See what the human version of this workflow looks like: YouTube: End-to-End with Shape Up: A Real-World Case Study

---

**Metadata**
- Posted: 9:13 AM · Feb 7, 2026
- Views: 244.1K
- Replies: 36
- Reposts: 62
- Likes: 860
- Bookmarks: 2.6K