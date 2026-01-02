# François Chollet + Mike Knoop | ARC Prize Fireside Chat @ MIT

**Host:** Greg (MIT moderator)  
**Panelists:** François Chollet, Mike Knoop (ARC Prize Co-Founders)  
**Context:** University tour discussion of ARC Prize and ARC-AGI benchmarks for measuring intelligence  
**Date:** October 24, 2025

---

**Greg:** I want to invite François Chollet and Mike Knoop up to the stage now, who are going to be doing a fireside chat.

**Mike Knoop:** Thank you, Greg. Great kickoff, and thank you everyone for hosting us. François, it's been exactly one year since we were here promoting the ARC Prize and ARC-AGI on the university tour. One of our main goals was to inspire folks to work on new ideas toward AGI.

A big update since last year is that we created our own intelligent science lab called Indie, and we're using ARC as one of our north star metrics. We're trying to build the top program synthesis team in the industry right now. By the way, we're hiring—if you're a builder interested in program synthesis, come talk to us. We're starting to make real progress over the last few months, merging deep learning and program synthesis together toward ARC-1 and ARC-2. And hopefully soon we'll start looking at V3.

This question you asked earlier is a really common one we got with V1 and V2. I'm curious to get your take here with V3: you guys now have three versions of the benchmark, all with AGI in the name. If we can make progress and beat V1, V2, and V3, do we have AGI? Or if that's not binary, what does it mean exactly? Can you help us map out what it means to make progress against ARC 1, 2, and 3?

**François Chollet:** Right. First, with V3, just like with V1 and V2, we're not making the claim that this is a definitive test for whether we have AGI. Solving V1, V2, or V3 is not a sufficient condition to say we have AGI. That's not the purpose of the benchmark.

Now, what it would take to solve V3 compared to V1 and V2 involves adding a few really important abilities: the ability to discover your own goals from your experience, do temporal planning, and interactive learning. With V1 and V2, you're just doing passive model-fitting—looking at data and trying to come up with a model to explain it. With V3, you have to collect your own data by interacting with the environment.

Creating a system that could do these things at human-level information efficiency and human-level action efficiency—that's basically a micro version of AGI. These are the properties you'd want to see in an AGI system, but on a very small scale. Why very small scale? Because these games are simple and easy. Any of you could go play them and do well. They don't require super intelligence. In terms of complexity and bit count, these are tiny games with a very small environment, a small perceptual space, played on short time scales. You're learning across a few minutes.

But a human-level general intelligence learns throughout an entire life with an enormous perceptual space, learning incredibly complex tasks. There's a very long distance from these micro-environments to the real world. But the properties we're trying to measure are the same: Can you efficiently interact with the world, discover its underlying principles, understand it, and act on it? It's the same principles, just on a tiny scale.

The idea is that if you manage to crack ARC-3 the right way—with an efficient system, without shortcuts or brute force—ideally your solution can be scaled up to something more similar to real AGI. Though the solution itself might not be instantly at human level.

There's a big debate happening right now on Twitter inspired by Rich Sutton's recent interview about whether LLMs are sufficient as a substrate to produce human-like systems. I'm curious your take: are LLMs sufficient as a substrate for lifelong, continual learning in order to beat V3?

**Mike Knoop:** LLMs alone—definitely not. An LLM is basically a way to acquire and encode programs. It's a repository for reusable vector programs acquired via gradient descent on human data. That's not what AGI is. It could be a component of AGI—the memory component, the knowledge and skill representation component. But the defining characteristic of general intelligence is how efficiently you acquire skills and knowledge—how efficiently you extract information from the world, from your experience, and turn it into programs that generalize well.

That's not what LLMs do. In the LLM world, the algorithm playing that role is just gradient descent, which is four to five orders of magnitude less efficient than human intelligence at skill acquisition. This is not what we're looking for. LLMs could be part of the solution, but they're definitely not the solution on their own.

There was another really common point of critique when we launched the ARC Prize last year: the reason LLMs haven't made progress on ARC is because it's a visual benchmark—you need visual perception to make progress. I think there's pretty strong evidence now that's not the case, given the reasoning models from December. Curious how you look at V3 though. Do you think we need more advancements or breakthroughs in perception to beat V3, or is this fundamentally a program synthesis and reasoning benchmark?

**François Chollet:** It's fundamentally a reasoning benchmark. It's not a visual perception benchmark at all. In fact, it was deliberately designed this way, just like V1 and V2. We were trying to remove the need for vision as a confounding factor. If you can solve these tasks, you can solve them using any modality—you could convert the visual input to text or audio without changing the fundamental challenge.

What makes ARC hard is not the visual component. It's the reasoning, the need to infer the underlying rule or program that explains the relationship between the input and output. The visual format is somewhat arbitrary—it's just the representation we chose. You could represent it as text, as numbers, as anything, and the difficulty would remain the same.

---

**Greg:** All right, so we've got a couple of questions from the audience. Let me grab one from this side of the room.

**Audience Member 1:** I haven't looked at all the games, but they're all 2D with a state that can be frozen between turns. Would you expect the intelligence or learning skills to translate to a 3D environment or a game where you don't have discrete turns—something more fluid or continuous with a physics engine?

**François Chollet:** The fact that the game frame is a 2D grid of pixels isn't really important. You could treat it as a sequence. It could be 3D, 4D—it fundamentally doesn't matter. It's just a set of discrete symbols with discrete properties, organized as a 2D grid for convenience. It's fundamentally not important.

Now, you bring up something genuinely different: the fact that this is a step-by-step environment where you take an action to get to the next state. That's definitely different from a real-time continuous environment. If you make a really good V3 solver, you could put it on a robot in principle. It's not the only thing you'd need—you'd also need a perception system to convert continuous live data into high-level discrete concepts the ARC solver could process, and probably a longer-term planning engine to make use of the model produced by the ARC solver. But fundamentally, yes, you'd be making progress toward real-world applications.

**Mike Knoop:** This was a really intentional design choice for V3—not to stress-test perception but to challenge the reasoning aspect. We deliberately did not want games where timing was an element of gameplay, because there are many games challenging for humans not through understanding what's happening but through execution difficulty or timing difficulty. That's not intelligence, so we deliberately avoided that.

---

**Greg:** Cool. One more question.

**Audience Member 2:** This is great, I'm really glad you guys are doing this. I have a broad conceptual question: What is the distribution of skills over which you expect an intelligent agent to generalize?

**François Chollet:** Distribution of skills—in terms of abilities?

**Audience Member 2:** Yeah. You said skill acquisition efficiency is your definition of intelligence. You built some set of games and test games, and you want the intelligent agent to generalize to those test games. So what is the distribution implied by that test set you want to generalize over?

**François Chollet:** For ARC V1 and V2, what makes a valid ARC task is that humans can solve it—that's the only constraint. It should not leverage any acquired knowledge, only core knowledge. Anything you can build with only core knowledge that a human can do is in distribution. There's no other narrower definition of the distribution.

**Audience Member 2:** So the distribution is the set of tasks that humans can solve efficiently. Is that correct?

**François Chollet:** Yes, which is basically infinite.

**Audience Member 2:** But it's not a uniform distribution over all possible tasks. What do you mean exactly by general intelligence? Because it sounds like what you're defining is actually human intelligence, not general.

**François Chollet:** That's right. Human intelligence is the only proof of existence we have of AGI. But what is general about human intelligence? You could actually argue on the basis of the "no free lunch" theorem that there's no such thing as truly general intelligence. But general in the sense that when we show humans any of these games for the very first time, they can't figure some out, yet the space of games you could give them that they could figure out is infinite and extremely diverse. It's general in that sense.

It may not be universal—I'm sure there are many tasks you could show humans they couldn't figure out. But the space of tasks they can figure out is vastly larger than what current systems can do. We actually made tasks in V2 that were too hard for humans.

**Audience Member 2:** So we're not targeting universal intelligence?

**François Chollet:** We're not targeting universal intelligence, which would be any task whatsoever. We're targeting human-level general intelligence. That's right.

---

**Greg:** All right, let's wrap up there. Thank you, François. Let's hear it for Mike and François.

---

*Note: This transcript represents the core fireside chat discussion. All timestamps refer to the original video (0:08–19:57 duration). No preview content, commercial sponsorships, or promotional material were present in the original—this is the authentic panel conversation from start to finish.*

## Verification & Notes

[^1]: **Speaker Identification**: Speaker attribution determined by conversational context and topic knowledge. Mike Knoop opens with "Thank you, Greg" and directly addresses François, speaking about shared initiatives. François responds with technical elaboration on ARC benchmark design. This pattern continues throughout the discussion.

[^2]: **Transcription Correction**: "Cryonian descent" corrected to "gradient descent" (line ~278)—the standard optimization algorithm for training neural networks. Context confirms this interpretation.

[^3]: **Lab Name Uncertainty**: "Indie" lab referenced at 0:54. Original transcription unclear; this represents best interpretation of the panelist's pronunciation in context of their research initiative.

[^4]: **ARC Naming Convention**: V1, V2, V3 used interchangeably with ARC-1, ARC-2, ARC-AGI-3 throughout the discussion. All refer to successive versions of the benchmark suite.

[^5]: **"No Free Lunch" Theorem**: Reference at 19:10–12. François references the mathematical principle that no algorithm can outperform others across all possible problem distributions—relevant to his point about generalization and task distribution.

[^6]: **Rich Sutton Reference**: Citation at 4:11–14 to Rich Sutton's recent interview discussing substrate sufficiency for AGI development—published around the time of this October 2025 event.

---

