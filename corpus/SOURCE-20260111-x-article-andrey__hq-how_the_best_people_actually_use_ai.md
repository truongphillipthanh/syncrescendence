# How the Best People Actually Use AI

(Description: Pixelated retro-style banner displaying "THE LEARNING GAP" in white block letters on a dark gray background with macOS-style window controls at top)

I'll start off by saying I'm no expert. I'm 20. I've worked at 4 companies in 3 years: two cybersecurity companies, an agent building company as a stable diffusion engineer, and now I'm head of marketing at another enterprise agent startup. I've been lucky enough to be in rooms with people way smarter than me.

This isn't advice from someone who's figured it all out, but rather my observations from being around some of the smartest minds.

## The One Thing They All Have in Common

As counterintuitive as it might seem, it's not intelligence, or decades of experience, but curiosity.

The best engineers, operators, builders all have relentless curiosity. They ask questions nobody else thinks to ask, and they question everything. They dig into tools most people dismiss, and they try things that seem pointless (until they're not).

An engineer I worked with would spend the first hour of every day just reading release notes and documentation for tools she already used. Mind you, these weren't new tools. These were tools she'd been using for the last 2 years, but she found features nobody else on the team knew existed. This is what Claude skills and MCP servers feel like in today's world, so take advantage of those.

The pattern was consistent: the best people treated learning as non-negotiable. Not as something they'd get to when they had time, but like actual work, and they would go about it very very humbly.

## Why Claude Became the Default

This isn't surprising now, but it was back in 2023. I watched engineers try everything. GPT-3.5, Gemini, local models, Mixtral, Claude, Grok. But despite the vast availability of all of these models, 9/10 engineers still went with Claude for their core work. When I asked why they unanimously mentioned that it was because of how it thinks.

Claude processes architectural decisions differently than other models. When you give it a complex system design problem, it doesn't spit back the most common pattern from its training data, but it reasons through tradeoffs. The biggest turning point for me was when a senior engineer gave the same prompt to four different models (he built a workflow that enabled him to have 4 terminal screens, where he would only have to write a prompt once and every model would have the same prompt instantly.) 3 of the AI models gave borderline identical answers without any clarifying questions, but Claude. It then gave an answer that addressed edge cases none of the other models even mentioned.

Opus 4.5 specifically became the standard for anything requiring judgment.

When you need to think through a system design, take into consideration some options or need something that will push back on ideas. That's when Claude pulls ahead (it doesn't agree with you by default, and you can get it to truly resist with a skill).

For execution tasks where the path is already clear, people would switch to faster models. But for the thinking work, for the stuff that actually determines whether a project succeeds (or fails), Claude became the default.

The best people I watched treated model selection as a skill worth developing in of itself.

## The Specificity Problem

The singular pattern that I noticed across every person who got consistently good AI output is that they never asked generic questions. The input matters a whole lot more than you think.

If you don't know how it works, AI processes what's known as markdown files and structured files extremely well. The more specific you can get about your problem, the better output you'll get. This works in every use case that you can think of.

**Example:** bad - "Write me a script to process these CSV files."

Better: "Write a Python script that reads sales.csv and orders.csv from the current directory, joins them on customer_id, calculates total revenue per customer, and outputs to revenue.csv. Don't log and don't configure, just write the script"

The first version gives Claude creative freedom it will use poorly. Don't get me wrong, it will build something that works, but probably not to the standard that you want it to. The second version gives Claude a concrete target, so it knows what success looks like and you told it how to get there. Claude just fills in the blank. The thought process still remains on you.

The best engineers in the world give air-tight prompts because they'd actually thought through what they wanted before they started typing. This skill alone is what separates 99% of engineers from the top 1%.

## The Copy-Paste Reset

The most tactical approach I've seen engineers use in the more recent days is what's known as the copy-paste reset method. The problem is that context windows get bloated, context accumulates and the model starts spitting garbage at you. This is actually a very common problem and it's very easily solvable.

The fix: copy everything important from your current session, clear the context entirely, and paste back only what matters. The last part is crucial for success, as otherwise this is pointless. The best engineers end up turning this into a custom bash command that they run with claude as well. You can do the same by just creating .claude/commands/ in your directory → write a markdown file → write your prompt inside that file and you're done.

Fresh context with critical information preserved, and the model starts being unrecognizably good. I know this sounds obvious, but I watched people struggle through degraded context for hours instead of just clearing and starting fresh. I was also guilty of this many many times.

The mental model that works for the top engineers: treat AI as stateless. Every conversation starts from nothing except what you explicitly give it. Plan accordingly.

## The Rate of Learning Problem

The thing that most people can't seem to get yet is that information is not the moat, but also the moat simultaneously. Access to information is everywhere now. Everyone has Claude, GPT, everyone can generate code and analyze content, etc. But what separates you from the best is access to the right information.

The gap between people who use AI well and people who struggle isn't tool access, but knowing what to ask for. Knowing what to ask for comes from being curious and actually trying things that seem pointless to learn. Yes, AI has knowledge on pretty much every question that you could possibly have, but it's your life, not AI's. So be curious.

The best people I worked with treated AI like a skill that compounds. It's like exploring a new area in a video game, because there's always something you can learn, every day. Every other week the top engineers would optimize for the seconds they could save by building a custom skill or workflow for something extremely niche. This is why they're the top engineers.

The people who struggled though used AI the same way in month six as they did in month one. I'm not saying you need to spend hours every day studying AI tool, even though that wouldn't necessarily hurt. I'm saying you need to be curious enough to notice when something isn't working and try something different, and increase your rate of trial.

The best engineer I worked with would occasionally use AI to do something completely outside his job, just to see how it handled different types of problems. He'd ask it to plan a vacation, write a speech, or do something completely irrelevant. He might not have even needed it, but he was doing it to test his own intuition on AI (as he later revealed to me).

That intuition translated directly to his actual work. He knew when to trust AI output and when to push back. He had a very good instinct of when AI was giving good outputs, or when he needed to involve his expertise and human judgement.

## The Uncomfortable Truth

Unfortunately, most people will read this and not change anything. They'll think "I already know this" or "this doesn't apply to me" or "I'll try this later.", and that's fine. Most people don't actually want to learn, but feel like they're learning by reading articles and watching videos and feel productive without actually changing behavior.

The people who actually get ahead with AI do something different. They read something, and they immediately try it. So go back up in the article and try creating your own command in claude code. Before it becomes one more thing you'll "get to eventually."

## Summary

The best people I've watched all share the same trait: relentless curiosity. They treat learning as non-negotiable, not something they'll get to when they have time.

Claude became the default for thinking work because it reasons through tradeoffs instead of regurgitating training data. Faster models handle execution, while Claude handles judgement.

Specificity is the whole game. Vague prompts == vague outputs. The engineers who get consistently good results aren't better at prompting. They're better at thinking through what they want before they type.

Context degrades. When output quality drops, clear everything and paste back only what matters. Treat AI as stateless. Every conversation starts from nothing except what you explicitly give it.

Access to information is everywhere now. Access to the right information is what separates you from everyone else.

Everything else is details.

Hope you found something useful.