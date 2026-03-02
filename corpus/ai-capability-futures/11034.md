# ARC-AGI-3 UPDATE
(Description: The article header shows "ARC PRIZE" text with colored squares (red, yellow) on a dark grid background, representing the ARC-AGI challenge branding)
## Summary
**TLDR:** Opus 4.6 demonstrates better reasoning and use of memory than Gemini 3.1 Pro and solves more levels. I'm now much more confident that current and future models will be able to solve ARC-AGI-3, given that they have access to harness with simple memory.
I suspect that memory scaffolds might be enough for pseudo-continual learning to push us over some self-improvement or research-agent threshold within the next 2 years.
---
## First of all, my harness:
The system prompt tells the agent that it is in an abstract 2D graphics game environment, and that it has to solve puzzles to get to the next level within an allowed action budget.
Furthermore, it explains that on each turn it will see its own memory that it can modify, the previous state, previous action, the current state and all the available actions. It also explains the JSON response format the agent has to follow.
It is quite simple, the agents don't get any images as input and don't get any diff-files to immediately see what changed in the environments, but they still get hints about how to use the memory and what to do with the previous state and actions.
The harness I used in the previous test was bad, which I only noticed after vibe-coding myself a nice little platform to track everything. It shows all the games runs I have started, the 3 different games, with before an after pic for each action, cost, token usage, the action, reasoning and the whole input and output for the model for debugging purposes.
(Description: A white-background interface showing a table with game run logs and debug information, including two side-by-side screenshots of an abstract 2D puzzle game with gray backgrounds, colored elements (blue, orange, yellow), and action descriptions)
---
Ultimately I think the models shouldn't need a memory or the previous state and action (that should be simply in context and in the weights, but I'm poor and models still have small context windows and no continual learning, which is why we use these harnesses).
---
## Gemini 3.1 Pro
What I can say is that it's better than Gemini 3.0 Pro. It identifies what the problem is. In this case it has to make 4 clicks in the bottom right square, but fumbles it, tries a few solutions and runs out of moves.
(Description: A 3x3 grid puzzle showing blue squares, red squares, and a white square with a small red dot in the center. Two identical grids shown side by side for comparison)
The same thing happens for the second game. It's a good start, but after reaching the white cross it starts thinking that the white cross shows the direction it has to move in. It also doesn't realize that the blue element in the GUI has rotated by 90 degrees and is now the same as the smaller blue element at the top. So it just stumbles through the level not really knowing what to do next. Again, it runs out of moves.
(Description: Gameplay animation showing a 2D puzzle environment with gray walls, a white cross symbol in the center, blue rotated elements, orange squares, and yellow blocks. Progress bar shown at bottom with yellow bar and red indicators)
Here on the last game it tries for a while to find the correct action, then finds it and quickly finishes the first level. It gets stuck on the second level.
(Description: Gameplay animation showing a top-down 2D maze-like environment with gray stone-textured walls, a cyan/blue rotated element at top, white cross marker, dark rectangular obstacles, and a blue element with orange and yellow indicators at the bottom)
Another thing I noticed is that it wasn't really using its memory to the fullest extent. Opus 4.6 did a much better job as you will see shortly. Gemini 3.1 Pro mostly just writes 1 or two sentences in the memory without any structure:
(Description: A text screenshot showing Gemini's memory output: "xs block of 12s/9s. Arrow points LEFT. Moving shifted the block left by 5 units. Continuing to move left until we hit the wall.")
Gemini 3.0 Pro performed better when vision was enabled in the previous harness. I think the same could be true for 3.1 Pro too, but I have already spent $120 on testing. I leave that up to someone else and want a fair comparison to Opus 4.6.
---
## Claude 4.6 Opus (Thinking)
Opus is a smart little bugger. It just one-shots the first level, then moves to the second level. I thought it was solving the 2nd level too first try, but it got the colors inverted. Then it deleted everything and tried the same solution again, hinting at a failure to make good use of memory. The memory should ideally be divided into long term and short term goals and observations. Basically some kind of hierarchical memory or context management that operates on different time-scales. (obligatory hint to the Nested Learning paper: https://abehrouz.github.io/files/NL.pdf )
(Description: A 3x3 grid puzzle with blue, red, and white squares with a centered red dot, followed by the same grid with inverted colors showing blue, red, and blue squares. Play button overlay indicates video content)
The second game was again a joy to watch.
(Description: Gameplay animation showing a maze-like environment with gray walls, blue rotated elements, white cross marker, and orange/blue colored objects. Progress bar at bottom with yellow and blue indicators)
It ran straight to the blue element, but realized something was missing. So it goes to the white cross, realizes in the reasoning that the blue element rotated by 90 degrees and that the borders of the blue elements are now active. Then continue to use the long way towards the final blue element lol.
In the second level it moves directly to the white cross. It beautifully plans ahead here, but the execution stops because I ran into the 50 move limit.
Also take a look at the memory. It has much more structure than the memory of Gemini 3.1 Pro!
(Description: A game state visualization showing a maze environment on the left with blue elements, and on the right a detailed memory structure text output describing observations, goals, memory states, and reasoning steps with much more organization and hierarchy than Gemini's output)
In the last game Opus finishes the first level with ease, but gets completely stuck on the second level. However in the memory you can see that it actually knows what the solution is. It just couldn't find the correct location to click :(
Again much better use of the memory compared to Gemini. More detailed and more structured!
(Description: Another game state visualization showing gameplay environment on the left with blue elements and obstacle layouts, and on the right an expanded memory structure with detailed observations, goals, hypothesis about block rotations, movement strategies, and execution notes)
(Description: Gameplay animation showing a split-screen view with a partially completed maze environment on left and a clear white section on right with blue elements and yellow/blue goal markers. Demonstrates solution path planning)
---
## Overall Assessment
Overall, Opus 4.6 demonstrates better reasoning and use of memory and solved more levels. I expect similarly good results from GPT-5.3.
This means Google still has some catching up to do.
---
## What's missing to solve ARC-AGI-3?
- I think ARC-AGI-3 is entirely solvable with simple memory like demonstrated here
- To improve performance it would help having memory for different timescales and having even more structured and detailed memory. The best solution of course would be to let the models learn that themselves. But if you just wanted to brute-force ARC-AGI-3, then I would add a short-, medium- and long-term memory each with defined fields like observations, goals, hypotheses, world model, and more.
- **Models really just need a way to compress their context and learn from it**
---
*Posted: 4:23 PM · Feb 19, 2026 · 225.8K Views*
*Engagement: 16 replies, 32 reposts, 444 likes, 309 bookmarks*