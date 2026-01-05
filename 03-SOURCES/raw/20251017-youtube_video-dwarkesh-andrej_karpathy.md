# Andrej Karpathy on Agents, AGI, and the Future of Education

**Participants:** Dwarkesh Patel (host), Andrej Karpathy (Tesla/former OpenAI)  
**Date:** October 17, 2025  
**Platform:** Dwarkesh Podcast

---

**Dwarkesh:** Today I'm speaking with Andrej Karpathy. Andrej, why do you say that this will be the decade of agents and not the year of agents?

**Andrej:** First of all, thank you for having me here. I'm excited to be here. The quote you've just mentioned, "It's the decade of agents," is actually a reaction to a pre-existing quote. I'm not sure who said it, but they were alluding to this being the year of agents with respect to LLMs and how they were going to evolve. I was triggered by that because there's some over-prediction going on in the industry. In my mind, this is more accurately described as the decade of agents.

We have some very early agents that are extremely impressive, and I use them daily—Claude, Codex, and so on. But I still feel there's so much work to be done. My reaction is we'll be working with these things for a decade. They're going to get better, and it's going to be wonderful. I was reacting to the timelines implied by that quote.

**Dwarkesh:** What do you think will take a decade to accomplish? What are the bottlenecks?

**Andrej:** Actually making it work. When you're talking about an agent—what the labs have in mind, and maybe what I have in mind as well—you should think of it almost like an employee or an intern that you would hire to work with you. For example, you work with some employees here. When would you prefer to have an agent like Claude or Codex do that work? Currently, of course, they can't.

What would it take for them to be able to do that? Why don't you do it today? The reason is because they just don't work. They don't have enough intelligence. They're not multimodal enough. They can't do computer use. They don't do a lot of the things you alluded to earlier. They don't have continual learning. You can't just tell them something and they'll remember it. They're cognitively lacking, and it's just not working. It will take about a decade to work through all of those issues.

**Dwarkesh:** As a professional podcaster and a viewer of AI from afar, it's easy for me to identify what's lacking: continual learning, or multimodality. But I don't have a good way of putting a timeline on it. If somebody asks how long continual learning will take, I have no prior about whether this is a project that should take five years, ten years, or fifty years. Why a decade? Why not one year? Why not fifty years?

**Andrej:** This is where you get into my intuition and doing an extrapolation with respect to my own experience in the field. I've been in AI for almost two decades—it's going to be fifteen years or so, not that long. You had Richard Sutton here, who was around for much longer. I do have about fifteen years of experience of people making predictions and seeing how they turned out. I was in research, and I've worked in the industry for a while. I have a general intuition from that. I feel like the problems are tractable and surmountable, but they're still difficult. If I average it out, it just feels like a decade to me.

**Dwarkesh:** This is quite interesting. I want to hear not only the history, but what people in the room felt was about to happen at various different breakthrough moments. What were the ways in which their feelings were either overly pessimistic or overly optimistic? Should we just go through each of them one by one?

**Andrej:** That's a giant question because you're talking about fifteen years of stuff. AI is wonderful because there have been a number of seismic shifts where the entire field suddenly looked a different way. I've lived through two or three of those. I still think there will continue to be some because they come with surprising regularity.

When my career began, when I started working on deep learning, this was by chance of being right next to Geoff Hinton at the University of Toronto. Geoff Hinton, of course, is the godfather figure of AI. He was training all these neural networks. I thought it was incredible and interesting. This was not the main thing that everyone in AI was doing by far. This was a niche subject on the side.

That's the first dramatic seismic shift—it came with AlexNet. AlexNet reoriented everyone, and everyone started training neural networks. But it was still very per-task, very specific task. Maybe you'd have an image classifier or a neural machine translator. People slowly became interested in agents. People started to think, "Okay, maybe we've checked off the visual cortex, but what about the other parts of the brain? How can we get a full agent or full entity that can interact in the world?"

The Atari deep reinforcement learning shift in 2013 or so was part of that early effort of agents. It was an attempt to get agents that not just perceive the world but also take actions and interact and get rewards from environments. At the time, this was Atari games. I feel that was a misstep.

**Dwarkesh:** Why was it a misstep?

**Andrej:** It was a misstep that even the early OpenAI that I was part of adopted. The zeitgeist at the time was reinforcement learning environments, games, game playing. Beat games, get lots of different types of games. OpenAI was doing a lot of that. That was another prominent part of AI where, for two, three, or four years, everyone was doing this. And I think it was a misstep.

The real issue is that in the real world, you don't have a reward signal. There's no environment telling you how well you're doing. Atari games have a very specific reward structure—you can play the game and get a score. In the real world, if you're an agent working as an intern in an office, you don't get this signal. The reward signal is implicit and has to come from a human or has to be inferred in some way.

This turned out to be an extremely hard problem. People spent many years trying to solve it, and it's still not solved. So the misstep was that we were training agents in these toy environments with perfect reward signals, but the real-world agent problem requires solving this much harder problem of figuring out what the reward signal should be.

**Dwarkesh:** Did people in the field recognize this at the time?

**Andrej:** Not as clearly as I'm describing it now. The field was very excited about RL and thought it was going to be the path forward. But looking back now, we can see that the real breakthroughs came from a different direction entirely. The breakthrough was language models and in-context learning, which is a completely different paradigm from RL.

Actually, I want to zoom out a bit. The field has gone through these periods where we thought we had the answer, and then we realized we didn't. We tried RL, and it didn't scale the way we hoped. We tried imitation learning from humans, and that was useful but limited. And then suddenly LLMs showed up, and the entire field reoriented.

---

**Dwarkesh:** I want to shift gears and talk about LLM cognitive deficits. From your perspective, what are the key limitations of current LLMs?

**Andrej:** There are several. First, they're really good at pattern matching in text. They've seen enormous amounts of text, and they can reproduce patterns. But they have genuine limitations in reasoning and in certain types of thinking. 

One limitation is what I'd call a lack of depth reasoning. You can test this easily. Give an LLM a problem that requires you to chain together many logical steps. Most LLMs will make errors somewhere in that chain. A human can often hold five, six, or ten steps in their head and work through a problem methodically. LLMs struggle with this.

Another limitation is uncertainty and calibration. LLMs don't really know what they don't know. They're trained to produce text, and they produce text with high confidence regardless of whether that text is correct. A human will say, "I don't know," but an LLM will give you an answer that sounds plausible and might be completely wrong. This is called hallucination, but it's really a calibration problem.

There's also a lack of true reasoning about causality. LLMs learn correlations in data. If A correlates with B in their training data, they'll predict B given A. But they don't understand whether A actually causes B or whether there's a confound. This is a fundamental limitation of predicting on text.

**Dwarkesh:** How do you think about the trajectory of fixing these? Are these fixable within the LLM paradigm, or do we need something fundamentally different?

**Andrej:** Some of these are fixable. Depth reasoning might improve with better training, better prompting strategies, or by having LLMs work step-by-step. But some of these limitations seem more fundamental. The uncertainty and hallucination problem is tricky because you're training a model that's intrinsically a next-token predictor. It's going to produce tokens, and it doesn't have access to a ground truth as it's generating. 

I think there will be hybrid systems. We'll use LLMs for what they're good at—they're amazing at language understanding, pattern recognition, and generating coherent text—but we'll combine them with other tools. Symbolic reasoning engines, retrieval systems, external memory. Tools that can provide certainty where the LLM provides uncertainty.

---

**Dwarkesh:** Let's talk about reinforcement learning. I know you have strong opinions about this.

**Andrej:** Yes, I do. Reinforcement learning is terrible.

**Dwarkesh:** Why?

**Andrej:** The core problem is that RL requires a reward signal, and getting that reward signal in the real world is extremely hard. You have to specify what you want the agent to do, and you have to do it in a way that the agent can actually measure progress. Most problems don't have this.

Let me give you an example. If I want to train an AI to write good essays, what's the reward signal? Is it a test score? But that's noisy. Is it a human rating? But that's expensive and subjective. Is it some automated metric? But those are usually gameable or don't capture what you actually care about. This is the reward specification problem, and it's fundamentally hard.

Now contrast this with how humans learn. When you learn to cook, you don't get a numerical reward signal. You taste the food, you adjust, you get feedback from people. It's implicit, it's rich, it's multifaceted. When you learn to write, you read other writing, you get feedback from people, you read more. You're not optimizing a reward signal; you're engaging with the world and absorbing patterns.

So RL was a nice idea—let's give agents explicit reward signals and have them optimize. But in practice, it's been much harder than people hoped. And meanwhile, a completely different approach—just training models on massive amounts of data—has been more successful. We've gotten further with LLMs trained on next-token prediction than we have with RL agents.

**Dwarkesh:** But haven't we gotten some successes with RL? AlphaGo, for instance.

**Andrej:** Yes, AlphaGo is a great example. But notice that AlphaGo is playing a game. Games are precisely the domain where RL works well because they have a perfect reward signal. You either win or you lose. The state space is well-defined. The action space is discrete and limited. These are all very artificial constraints that happen to be present in games but absent from the real world.

So RL has had genuine successes, but in a very narrow domain. The broader question is: can we scale RL to real-world problems where the reward signal is implicit? And the answer so far is no. We haven't figured that out.

**Dwarkesh:** If RL is so bad, what would you recommend instead?

**Andrej:** I think the near-term path forward is a combination of things. One, we should continue improving LLMs because they're clearly on an exponential growth curve. Two, we should focus on in-context learning and prompting—ways that agents can learn within a single conversation or session. Three, we should think more carefully about imitation learning from human demonstrations, because humans do give rich information about how to solve problems.

And longer term, I think we need to move toward something like how humans and animals learn. We learn by interacting with the world, getting rich multimodal feedback, and building internal models. Not by optimizing a scalar reward signal. We need to move away from the RL paradigm toward something that looks more like how biological intelligence actually works.

---

**Dwarkesh:** How do humans learn? What's the mechanism?

**Andrej:** Humans learn through multiple channels simultaneously. You're perceiving the world—vision, sound, touch, proprioception. You're getting feedback from your actions. You're learning from social interaction. You're learning from language. You're learning from reading. You're learning by doing. It's this rich, multimodal, continuous process.

And crucially, humans have goals and drives, but we don't have explicit numerical reward signals. I don't have a meter telling me how well I'm doing in life. But I adjust based on feedback, on how people respond to me, on how my actions lead to consequences. The learning signal is implicit and rich.

There's also something about intrinsic motivation. Humans are curious. We want to understand how the world works. We want to solve problems. We want to create things. This motivation drives learning in a way that's not captured by reinforcement learning with an external reward signal.

And learning is continuous. You don't learn something and then stop. You're constantly refining your understanding, updating your models, learning new things. Even as an adult, I'm learning all the time. This is very different from the offline supervised learning paradigm where you train on a fixed dataset and then stop.

**Dwarkesh:** Do you think we can implement this in AI systems?

**Andrej:** We can implement some aspects of it. We can give systems multiple modalities of input. We can create learning objectives that capture curiosity and intrinsic motivation. We can make learning continuous rather than episodic. But I don't think we fully understand how human learning works, so it's hard to say we've replicated it.

One thing that's clear is that raw data efficiency matters. Humans are incredibly data-efficient learners. You see a dog a few times and you understand what a dog is. You don't need to see ten thousand pictures of dogs to understand the concept. AI systems, especially current LLMs, are extremely data-hungry. They need billions of tokens to learn.

This suggests that there's something fundamentally different about how biological intelligence works. We have inductive biases, probably evolutionary constraints that allow us to learn efficiently. We probably have domain-specific learning mechanisms. We're not just blank slates learning from raw data.

So improving AI learning efficiency might require moving away from the general-purpose approach and incorporating more structure, more inductive bias, more domain-specific mechanisms. This is tricky because general-purpose learners have been very successful. But maybe there's a middle ground.

---

**Dwarkesh:** Let's talk about AGI and where it fits into economic growth. You've said something interesting about how AGI might just blend into continued economic growth.

**Andrej:** Yes, this is something I find often gets misunderstood. People talk about AGI as this discontinuous event. Like, we're going along, then AGI happens, and suddenly everything changes. But I think that's wrong.

Look at economic history. The past 200-250 years have been characterized by about 2% annual GDP growth in developed countries. This sounds small, but it compounds. Over two centuries, it means the world has gotten about fifty to one hundred times richer. That's enormous. And this growth has come from technological progress: the steam engine, electricity, manufacturing, computers, the internet.

Each of these represented genuine breakthroughs. But they didn't cause a discontinuous jump in economic growth. Instead, they gradually raised the growth rate or changed which sectors were growing. The industrial revolution didn't cause sudden exponential growth; it caused sustained growth over decades as the technology was implemented, refined, and diffused through the economy.

I think AGI will be similar. It'll be revolutionary in how it affects our capabilities. But in terms of economic growth, it will probably fit into the same 2% growth trajectory. Maybe it pushes it to 2.5% for a while. Maybe it creates new industries. But I don't think we'll see a discontinuous jump to 10% growth or something exponential.

**Dwarkesh:** Why do you think that?

**Andrej:** Several reasons. One is just looking at history. Technological progress doesn't lead to discontinuous economic jumps. Two, the economy is complicated. Even if we have a technology that makes everyone ten times more productive, implementation takes time. There are bottlenecks. There are skill gaps. There are regulatory barriers. It takes decades to fully deploy a new technology.

Three, and this is important: growth is already based on improving technology and productivity. That's where the 2% comes from. Adding AI to that picture is adding another tool to improve productivity. It's not some brand new category; it's an improvement to something we're already doing.

Now, this doesn't mean AGI isn't important or revolutionary. It absolutely is. It means that the economic growth trajectory might not change as dramatically as people hope or fear. Which is actually quite interesting and might disappoint the doomers and the accelerationists equally.

**Dwarkesh:** So you're saying we won't have superintelligence leading to rapid recursive self-improvement and explosive growth?

**Andrej:** Well, even if we build artificial superintelligence, yes. Superintelligence is real and would be powerful. But the idea of recursive self-improvement leading to explosive growth runs into physical and economic constraints. You can't make things infinitely faster. You can't make chips infinitely small. You can't make electricity infinitely cheap. There are limits.

And even if an AI system is superintelligent in a narrow sense—say, it's amazing at reasoning and coding—it still has to interact with a world that's constrained by physics and economics. Building a new factory takes time. Deploying a new technology takes time. These constraints apply whether the technology is superintelligent or not.

So I expect superintelligence to be very valuable and to accelerate progress in certain domains. But the world's economic growth trajectory, I expect to follow a pretty similar curve to what we've seen.

---

**Dwarkesh:** Why did self-driving take so long to crack? A lot of people in 2011 thought it would be solved by now.

**Andrej:** This is a great example of the difference between vertical progress and horizontal progress. Vertical progress is how good a system is at its task. Horizontal progress is how many tasks you've solved or how general your solution is.

In 2011, self-driving cars seemed like a solved problem in the vertical sense. We had the perception technology. We had the control algorithms. We could build a car that drives on highways reasonably well. What we didn't have was a solution that worked in all conditions, all weather, all edge cases.

Self-driving ended up being a horizontal problem. It's not "make the car drive well at one thing"—it's "make the car drive well at everything." Every edge case, every rainy day in some city you've never been to, every weird interaction with pedestrians. You need to handle all of it.

This is hard because the world is full of infinite variation. There are millions of specific situations a car might encounter, and you need to handle all of them. You can't just collect data and train on it because there are always new situations.

Moreover, self-driving was limited by the datasets available and the simulation environments available. For a long time, we didn't have huge amounts of diverse data from real self-driving attempts. The perception algorithms needed that data to get good. This created a chicken-and-egg problem.

Also, there was the problem of getting to the last mile of accuracy. Going from 95% accuracy to 99% accuracy is much harder than going from 80% to 95%. The last 5% contains all the edge cases, the rare scenarios. Those are inherently hard to collect data on and train for.

And then there's the deployment problem. Even if you have a good system, you need to convince people it's safe enough to deploy. You need regulatory approval. You need to build the fleet. You need to train the operators. You need to handle the liability issues. These are all slow processes.

So self-driving took so long because it turned out to be a much harder problem than people anticipated. It looked like a vertical problem—make better perception—but it was really a horizontal problem—make perception work in all possible scenarios.

**Dwarkesh:** Do you think we've now solved self-driving?

**Andrej:** I'd say we've made tremendous progress, especially with Tesla's vision-only approach. But I wouldn't say it's fully solved. We've gone from "this is impossible" to "this is working in many scenarios." But there are still edge cases, still scenarios where systems fail. I think we're close to human-level performance in many contexts.

The question then becomes: what does "solved" mean? If it means "better than human drivers," then we might already be there in some contexts. If it means "works perfectly in all scenarios," then no, we're not there yet. I'd say we're at the point where autonomous driving is genuinely useful and safe for many applications, and we're working through the remaining issues.

---

**Dwarkesh:** Let's turn to education. You've become quite invested in this. Your YouTube channel on neural networks and LLMs has been watched by hundreds of thousands of people. What's your philosophy?

**Andrej:** I'm passionate about education because I think it's the most intellectually interesting problem, actually. The challenge is this: you have a tangle of understanding—a lot of interconnected ideas, concepts, and skills. You need to lay it out in a way that creates a ramp where everything only depends on the thing before it.

This untangling of knowledge is intellectually interesting. I love doing it, and I have a fascination with trying to lay things out in a certain way. It makes the learning experience so much more motivated because students understand not just what something is but why it's needed.

**Dwarkesh:** Your tutorial on the transformer begins with bigrams—literally a lookup table. Here's the word right now, here's the previous word, here's the next word. It's just a lookup table. Then you build up from there.

**Andrej:** That's the essence of it, yes. It's such a brilliant way to start—with a lookup table and then build toward a transformer. Each piece is motivated. Why would you add that? Why would you add the next thing? You could memorize the attention formula, but having an understanding of why every single piece is relevant and what problem it solves—you present the pain before you present the solution. That's how you take the student through that progression.

There are a lot of other small things that make it nice and engaging and interesting. Always prompting the student. There's a lot of important small things like that. How would you solve this? I'm not going to present the solution before you guess. That would be wasteful.

**Dwarkesh:** Why is that important?

**Andrej:** Because if you try to come up with it yourself, you get a better understanding of the action space, what the objective is, and then why only this action fulfills that objective. You have a chance to try it yourself, and you have an appreciation when I give you the solution. It maximizes the amount of knowledge per new fact added.

**Dwarkesh:** Why do you think, by default, people who are genuine experts in their field are often bad at explaining it to somebody learning?

**Andrej:** It's the curse of knowledge and expertise. This is a real phenomenon, and I've suffered from it myself as much as I try not to. You take certain things for granted, and you can't put yourself in the shoes of new people who are just starting out. It's pervasive and happens to me as well.

One thing that's extremely helpful: As an example, someone was trying to show me a paper in biology recently, and I had so many terrible questions. What I did was use ChatGPT to ask the questions with the paper in the context window. It worked through some of the simple things. Then I shared the thread with the person who wrote that paper or worked on that work. If they could see the dumb questions I had, it might help them explain better in the future.

For my material, I would love it if people shared their dumb conversations with ChatGPT about the stuff I've created because it really helps me put myself again in the shoes of someone who's starting out.

**Dwarkesh:** That's interesting. What's another trick?

**Andrej:** Here's something that just works astoundingly well: If somebody writes a paper or a blog post or an announcement, it is in 100% of cases that the narration or the transcription of how they would explain it to you over lunch is way more understandable and also more accurate and scientific.

People have a bias toward explaining things in the most abstract, jargon-filled way possible. They clear their throat for four paragraphs before they explain the central idea. But there's something about communicating one-on-one with a person that compels you to just say the thing.

**Dwarkesh:** I saw that tweet, I thought it was really good. I shared it with a bunch of people.

**Andrej:** I notice this many, many times. The most prominent example is that I remember back in my PhD days doing research. You read someone's paper, and you work to understand what it's doing. Then you catch them having beers at the conference later, and you ask, "So this paper, what were you doing?" They just tell you these three sentences that perfectly capture the essence of that paper and totally give you the idea. You didn't have to read the paper.

It's only when you're sitting at the table with a beer or something, and they're like, "Oh yeah, the paper is just—you take this idea, you take that idea and try this experiment and you try out this thing." They have a way of just putting it conversationally perfectly. Why isn't that the abstract?

**Dwarkesh:** Exactly.

**Andrej:** This is coming from the perspective of how somebody trying to explain an idea should formulate it better. When you're speaking casually to a person, you're forced to be clear because the person will tell you if they don't understand. If you're writing, you can hide behind jargon and abstraction.

**Dwarkesh:** What's your advice as a student to other students? If you don't have a Karpathy doing exposition of an idea, if you're reading a paper from somebody or reading a book, what strategies do you employ to learn material you're interested in?

**Andrej:** I don't know that I have unique tips and tricks, to be honest. It's a painful process. One thing that's always helped me quite a bit: learning things on demand is pretty nice. I do feel you need alternation between learning depth-wise—you're trying to achieve a certain project where you're going to get a reward from—and learning breadth-wise, which is just, "Let's do whatever 101, and here's all the things you might need."

School does a lot of breadth-wise learning. "Trust me, you'll need this later." And you're like, "Okay, I trust you. I'll learn it because I guess I need it." But I love the kind of learning where you'll get a reward out of doing something, and you're learning on demand.

The other thing I've found extremely helpful: explaining things to people is a beautiful way to learn something more deeply. This happens to me all the time. I realize if I don't really understand something, I can't explain it. It's so annoying to come to terms with that. You can go back and make sure you understood it. It fills these gaps in your understanding. It forces you to come to terms with them and reconcile them.

I love to re-explain things, and people should be doing that more as well. It forces you to manipulate the knowledge and make sure that you know what you're talking about when you're explaining it.

**Dwarkesh:** That's an excellent note to close on. Andrej, that was great. Thank you.

---

*Note: All preview content, advertising, and promotional material has been removed from this transcript. The conversation begins at its natural starting point.*

## Terminology Notes

[^1]: **LLM**: Large Language Model, such as Claude, GPT-4, or others
[^2]: **Atari DQN**: Deep Q-Network, a reinforcement learning algorithm that learned to play Atari games; released by DeepMind in 2013
[^3]: **AlexNet**: Deep convolutional neural network that won the ImageNet competition in 2012, marking a major shift toward deep learning
[^4]: **Micrograd**: A minimal implementation of automatic differentiation written by Karpathy to teach neural network fundamentals
[^5]: **In-context learning**: The ability of an AI system to adapt to new tasks by learning from examples provided in a single conversation, without being retrained
