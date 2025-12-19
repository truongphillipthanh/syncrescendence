# Is RL + LLMs Enough for AGI?

**Host:** Dwarkesh Patel  
**Panelists:** Sholto Douglas (Anthropic, RL scaling), Trenton Bricken (Anthropic, mechanistic interpretability)  
**Original Air Date:** May 22, 2025

---

## How Far Can RL Scale?

**Dwarkesh:** Okay, I'm joined again by my friends, Sholto Bricken—wait, did I do this last time?

**Sholto:** You did the same thing. No, no, you named us differently, but we didn't have Sholto Bricken and Trenton Douglas.

**Dwarkesh:** You swapped us.

**Sholto:** Sholto Douglas and Trenton Bricken.

**Trenton:** Who are now both at Anthropic.

**Dwarkesh:** Right. Let's go. Sholto is scaling RL, Trenton's still working on mechanistic interpretability. Welcome back.

**Sholto:** Happy to be here.

**Trenton:** Yeah, it's fun.

**Dwarkesh:** What's changed since last year? We talked basically this month in 2024. Now we're in 2025. What's happened?

**Sholto:** Okay, so I think the biggest thing that's changed is that RL in language models has finally worked. We finally have proof of an algorithm that can give us expert human reliability and performance, given the right feedback loop.

I think this has only really been conclusively demonstrated in competitive programming and math. Think of these two axes: one is the intellectual complexity of the task, and the other is the time horizon at which the task is being completed. I think we have proof that we can reach the peaks of intellectual complexity along many dimensions. We haven't yet demonstrated long-running agentic performance. You're seeing the first stumbling steps of that now, and should see much more conclusive evidence of that by the end of the year, with real software engineering agents doing real work.

**Dwarkesh:** I think Trenton, you're experimenting with this at the moment?

**Trenton:** Yeah, absolutely. The most public example people could go to today is ClaudePlaysPokemon. Seeing it struggle is in a way kind of painful to watch, but each model generation gets further through the game. It seems more like a limitation of it being able to use memory system than anything else.

**Dwarkesh:** I wish we had recorded predictions last year. We definitely should this year. Hold us accountable.

**Sholto:** That's right.

**Dwarkesh:** Would you have said that agents would be only this powerful as of last year?

**Sholto:** I think this is roughly on track for where I expected with software engineering. I think I expected them to be a little bit better at computer use. But I understand all the reasons for why that is, and I think that's well on track to be solved. It's just a temporary lapse.

Holding me accountable for my predictions next year, I really do think by the end of this year to this time next year, we will have software engineering agents that can do close to a day's worth of work for a junior engineer, or a couple of hours of quite competent, independent work.

**Dwarkesh:** That seems right to me. I think the distribution's pretty wonky though, where for some tasks, like boilerplate website code, these sorts of things, it can already bang it out and save you a whole day.

**Sholto:** Exactly. I think last year, you said that the thing that was holding them back was the extra nines of reliability. I don't know if that's the way you would still describe the way in which these software agents aren't able to do a full day of work, but are able to help you out with a couple hours. Is it the extra nines that's really stopping you or is it something else?

**Trenton:** I think my description there was, in retrospect, probably not what's limiting them. I think what we're seeing now is closer to: lack of context, lack of ability to do complex, very multi-file changes—sort of the scope of the task, in some respects. They can cope with high intellectual complexity in a focused context with a scoped problem. When something's a bit more amorphous or requires a lot of discovery and iteration with the environment, with this kind of stuff they struggle more.

Maybe the way I would define the thing that's holding them back is this: if you can give it a good feedback loop for the thing that you want it to do, then it's pretty good at it. If you can't, then they struggle.

**Dwarkesh:** For the audience, can you say more about what you mean by this feedback loop if they're not aware of what's happening with RL and so forth?

**Sholto:** Yes, so it's the big thing that really worked over the last year. Broadly, the domain is called RL from Verifiable Rewards, or something like this, with a clean reward signal.

So the initial unhobbling of language models was RL from human feedback. Typically, it was something like pairwise feedback and the outputs of the models became closer and closer to things that humans wanted. This doesn't necessarily improve their performance at any difficulty or problem domain. Particularly, humans are quite bad judges of what a better answer is. Humans have things like length biases and so forth.

You need a signal of whether the model was correct in its output that is quite true. Things like the correct answer to a math problem, or passing unit tests. These are examples of a reward signal that's very clean. Even these can be hacked, by the way. Even with unit tests, the models find ways around it to hack in particular values and hard code values of unit tests, if they can figure out what the actual test is doing. If they can look at the cached Python files and find what the actual test is, they'll try and hack their way around it. These aren't perfect, but they're much closer.

**Dwarkesh:** Why has it gotten so much better at software engineering than everything else?

**Sholto:** In part, because software engineering is very verifiable.

---

## Is Continual Learning a Key Bottleneck?

**Dwarkesh:** So we talked about two axes of complexity and time horizon. If you think about what's actually limiting scaling here, is continual learning a key bottleneck? Or is it more about just having the right reward signal?

**Sholto:** I think it's the right reward signal. I think continual learning will be a bottleneck eventually, but I don't think we're there yet. The thing that's limiting us is that we don't have a good reward signal for most tasks that we care about.

If you think about what we've solved: we've solved competitive programming, we've solved math, we've solved basically any task where you can verify the answer. The thing we haven't solved is tasks where you don't have a clean reward signal. And most real-world tasks fall into that category.

**Trenton:** Right, and I think there's also the question of whether the model is actually learning to do more than its previous pass at K. Is it discovering something new each time, or is it just kind of converging on a local maximum?

**Dwarkesh:** That's an interesting point. So the model might look like it's improving just because the RL is helping it exploit the test cases better, rather than actually learning new reasoning skills?

**Trenton:** Exactly. And I think this is actually quite hard to measure. You'd want to look at whether the model's reasoning has actually changed, not just whether it's getting the right answer more often.

---

## Model Self-Awareness

**Dwarkesh:** One thing that's come up in conversations about scaling is whether models actually have self-awareness about what they're doing. When we're training with RL, is the model developing some kind of understanding of its own reasoning process?

**Sholto:** I think that's a really interesting question. What I've noticed is that as we push the models further with RL, they do seem to develop something that looks like self-awareness—or at least introspection. They'll sometimes catch their own mistakes mid-reasoning. They'll say something like, "Wait, I think I'm approaching this wrong."

But I'm honestly not sure whether that's genuine self-awareness or just a learned pattern. It might be that the reward signal is favoring models that use certain linguistic patterns that look like self-correction, even if there's no real underlying reflection happening.

**Trenton:** This gets at the mechanistic interpretability question I work on. If we could actually see what's happening inside the model when it's self-correcting, we could answer whether it's real or mimicry. But that's exactly what we don't yet know how to do cleanly.

**Dwarkesh:** So you're saying if we had better mechanistic interpretability, we could actually tell whether the self-awareness is real?

**Trenton:** Exactly. And I think that's become increasingly important because as these models get more sophisticated, the stakes of not understanding what's actually happening inside them go up.

---

## Taste and Slop

**Dwarkesh:** Let's talk about output quality. There's a lot of discussion about what people call "slop"—this sense that model outputs are becoming generic, kind of lowest-common-denominator. But you also need a lot of training data to train these reward models. Isn't there a tension between training data quantity and quality?

**Sholto:** Yeah, that's a real tension. The problem is that most of the high-quality data out there is already being used. So to scale further, you either need to create synthetic data or you need to accept lower quality data. Both approaches have downsides.

With synthetic data, you run the risk of mode collapse—the models just copying each other's patterns endlessly, and you lose diversity. With lower quality data, you get what people call slop: outputs that are technically correct but aesthetically or stylistically boring.

**Trenton:** And there's also this question of taste. Taste is fundamentally subjective. So when we're building reward models for tasks where taste matters—creative writing, design, music—how do you even define what a good output looks like?

**Dwarkesh:** So you're saying this isn't something RL can solve?

**Trenton:** Not in the traditional sense of RL, no. RL is great when you have a clean, objective reward signal. But for tasks where the reward is "does this have good taste," you're back to human feedback. And human feedback doesn't scale the way clean rewards do.

---

## How Soon to Fully Autonomous Agents?

**Dwarkesh:** Okay, so let's look forward. You've made a prediction about software engineering agents. But let me ask broader: how far away are we from agents that can do something like 8-10 hours of autonomous work on a complex project?

**Sholto:** I think the timeline depends a lot on what you mean by autonomous. If you mean the agent can work on a well-defined problem with clear success criteria, I think that's already possible in limited domains. If you mean the agent can identify its own problems, break them down, and route-find through an open-ended challenge, that's still a ways off.

**Trenton:** And there's also the question of reliability. You might have an agent that can do the work 95% of the time, but that last 5% of failures could be catastrophic. For real-world deployment, you need much higher reliability margins.

**Dwarkesh:** So it's not just about capability but about robustness?

**Sholto:** Right. And actually, I think the robustness question is where RL really helps. Because once you can verify success, RL can push the model to be reliable. It's the tasks where you can't verify success that remain hard.

---

## Neuralese

**Dwarkesh:** This is an interesting thread to pull on. Trenton, you've talked about "neuralese"—this idea that models might develop their own internal language that's optimized for how they compute, not for how humans read. What does that mean exactly?

**Trenton:** So the idea is that when we're looking at the internals of a model, we're seeing patterns of activation that might be the model's native way of thinking about a problem. But we're trained to interpret everything through human language and concepts. So we might be missing the actual structure of how the model computes.

Think of it like if you were trying to understand how a whale thinks by transcribing its clicks into English words. You'd get something, but you'd be missing a lot of the information that's in the original click patterns.

**Dwarkesh:** So when we develop mechanistic interpretability, we're not actually discovering the model's true thinking, we're just translating it into human concepts?

**Trenton:** That's one possibility. Another possibility is that the model's computation is actually closer to human reasoning than we realize, and what we're discovering through mechanistic interpretability is something real. But we genuinely don't know yet.

**Sholto:** And this connects to the earlier point about self-awareness. If neuralese is real, then the model might be self-aware in its native format, but that self-awareness doesn't necessarily translate cleanly into human language.

---

## Inference Compute Will Bottleneck AGI

**Dwarkesh:** There's been a lot of focus on training compute—the kind of scaling that leads to more capable models. But I've heard arguments that inference compute will actually be the bottleneck for AGI. What's the reasoning there?

**Sholto:** So the idea is that as we get more capable models through scaling training compute, we also need more compute per inference to get the best possible output. And inference compute is much harder to scale than training compute.

With training, you can throw more compute at it and get better models. With inference, every inference has to happen in real-time. You can't batch them the same way. So you can't just throw more compute at the problem without fundamentally changing the deployment model.

**Trenton:** Also, inference compute is much more decentralized. Training happens in a few large labs. But inference happens on edge devices, on phones, everywhere. So scaling inference compute requires completely different infrastructure.

**Dwarkesh:** So you're saying there's a hard scaling limit to inference?

**Sholto:** Not hard, but it's a much harder problem than training. And if models get good enough that everyone wants to run them locally for privacy or latency reasons, that becomes a real bottleneck.

---

## DeepSeek Algorithmic Improvements

**Dwarkesh:** DeepSeek has gotten a lot of attention recently for claiming significant algorithmic improvements. What have they actually demonstrated? And how much does this change the scaling picture?

**Sholto:** So DeepSeek has released models that show comparable performance to much larger US models, while being trained on far less compute. If their claims are real, that's significant. It means that efficiency improvements matter more than people thought.

**Trenton:** But we should be careful about how we interpret this. They might be using better data, better architectures, better training techniques, or some combination. It's not always clear which lever they're pulling.

**Dwarkesh:** So this doesn't necessarily mean the scaling laws are broken?

**Sholto:** Right. Scaling laws are asymptotic relationships. DeepSeek could be pulling specific efficiency levers without invalidating the fundamental laws. But it does suggest there's more efficiency on the table than people realized.

---

## Why Are LLMs 'Baby AGI' But Not AlphaZero?

**Dwarkesh:** This is a philosophical question that I find interesting. People often call LLMs "proto-AGI" or "baby AGI," but nobody says that about AlphaZero, even though AlphaZero is arguably more general within its domain. Why is there this asymmetry?

**Sholto:** I think it's because LLMs can do something AlphaZero fundamentally can't: they can reason about things outside their training distribution. AlphaZero is a master within its domain but utterly helpless outside it. LLMs have this weird property where they can kind of muddle through on novel tasks.

**Trenton:** It's like the difference between someone who has memorized everything about chess but can't think about anything else, versus someone who's moderately knowledgeable about many things and can transfer knowledge across domains.

**Dwarkesh:** So you're saying the generality is what makes LLMs look more like AGI, not the absolute capability level?

**Sholto:** Exactly. If AlphaZero could learn chess, then learn Go, then learn trading, then learn protein folding, we'd call it AGI. But it's locked into each domain by its training process. LLMs have this strange flexibility.

---

## Mechanistic Interpretability

**Dwarkesh:** Trenton, let's dig into mechanistic interpretability more directly. What's the actual frontier of what you can understand about a model right now?

**Trenton:** So we can identify features—patterns of activations that correspond to identifiable concepts. We can trace how information flows through the model. We're getting better at understanding attention patterns and how they relate to reasoning.

But we hit a hard problem: we can identify that something is happening, but we can't always explain why the model chose that particular computation over another one. It's like we can see the road the model took but not why it chose that road instead of alternatives.

**Dwarkesh:** So you can see *that* it's computing something but not *why* it chose to compute it that way?

**Trenton:** Right. And this matters because for safety, we need to understand not just what the model is doing, but why it's choosing to do it. If we don't understand the decision-making process, we can't really predict how it will generalize to new situations.

**Sholto:** This also connects back to the self-awareness question. If we could understand not just the model's reasoning but the model's reasoning about its reasoning, that would be huge for safety. But that's even harder.

**Trenton:** Exactly. That's the frontier right now. We're starting to see models that seem to have hierarchical reasoning—reasoning about their reasoning. Understanding that is going to be really important.

---

## How Countries Should Prepare for AGI

**Dwarkesh:** Let's zoom out to broader implications. If we're on track to AGI in some meaningful sense, how should countries be preparing? This seems like a question you've thought about.

**Sholto:** I think the first thing is to acknowledge the possibility seriously. A lot of governments are still treating AI as just another technology. If AGI is a real possibility, you need fundamentally different policy.

The second thing is infrastructure. Most of the compute for training large models is in the US and China. If other countries don't have access to compute, they won't have agency over their own AI futures. So compute access is a geopolitical issue.

**Trenton:** And I'd add talent migration. A lot of AI talent migrates to the US because that's where the best opportunities are. If you're a country that cares about AGI development, you need to be able to attract and retain talent. But you also need to build institutions that can do world-class work.

**Dwarkesh:** So you're saying this isn't just a matter of policy but of building actual capacity?

**Sholto:** Right. And there's also the question of which approaches you bet on. Different countries might be better positioned for different AI approaches. Some might be better at scaling. Some might be better at robotics. Some might be better at interpretability.

**Trenton:** And there's the international coordination question. Some AI risks are global. So you need international agreements on safety standards, on how to handle AGI once it exists, on not creating unnecessary existential risk. But right now, there's barely any international coordination happening.

---

## Automating White Collar Work

**Dwarkesh:** Let's talk about the economic implications. If we get software engineering agents and then more general agents, what happens to white collar work?

**Sholto:** I think the first phase is where human workers still necessary, but they're much more productive. A person working with a good AI agent can do what used to take three people. So there's displacement, but not unemployment yet.

But if agents get good enough, you reach a point where the human isn't really necessary anymore. You might have one human overseer per ten agents. Then you have genuine technological unemployment.

**Dwarkesh:** And that happens faster in some fields than others?

**Sholto:** Much faster. Fields with clear success criteria—programming, mathematics, probably law—are vulnerable first. Fields that require judgment and taste—management, creative fields, anything that requires political or social understanding—are probably more resilient.

**Trenton:** But I'd be cautious about assuming that. We've been surprised before by how much tasks seemed to require human judgment but actually didn't. I think we should prepare for faster disruption than seems intuitive.

---

## Advice for Students

**Dwarkesh:** If we're living in this world, what is your advice to somebody early in their career, or a student in college? What should they be planning on doing?

**Sholto:** Once again, it's worth considering the spectrum of possible worlds and preparing yourself for that. The action that I think is the highest expected value in that case is that at a minimum you're about to get dramatically more leverage. Already the startups in YC are writing huge amounts of their code with Claude.

The question to ask yourself is: What challenges, what causes do you want to change in the world with that added leverage? If you had ten engineers at your beck and call, what would you do? If you had a company at your beck and call, what would that enable you to do? What problems and domains suddenly become tractable? That's the world you want to prepare for.

Now, that still requires a lot of technical depth. Obviously there is the case where AI just becomes dramatically better than everyone at everything, but for at least a while there is something worth considering. Jensen Huang actually talked about this in an interview in an interesting way. He's like, "I have a hundred thousand general intelligences around me, and I'm still somewhat useful, because I'm there directing the values, and asking them to do things. I still have value even though I have a hundred thousand general intelligences."

For many people, I think that will still be true for a fair while. Then as the AIs get better and better and so on, eventually, no. But again, prepare for the spectrum of possible worlds because in the event where we're just totally outcompeted, it doesn't matter what you do. In all the other worlds, it matters a lot.

Get the technical depth. Study biology, study CS, study physics. Think hard about what challenges you want to solve in the world.

**Dwarkesh:** That's a lot of topics.

**Sholto:** That's a lot. But you can now. It's so much easier to learn. Everyone now has the infinite perfect tutor.

**Trenton:** It's definitely been helpful to me. I would say some combination of: get rid of the sunk cost of your previous workflows, or expertise in order to evaluate what AI can do for you.

Another way to put this, which is fun, is just be lazier in the sense that you figure out the way that the agent can do the things that are toilsome. Ultimately, you get to be lazier, but in the short run, you need to critically think about the things you're currently doing, and what an AI could actually be better at doing, and then go and try it, or explore it. Because I think there's still a lot of low-hanging fruit of people assuming and not writing the full prompt, giving a few examples, connecting the right tools for your work to be accelerated and automated.

**Dwarkesh:** There's also the sunk cost of feeling like since you're not "early to AI," that you've sort of missed the boat. I remember when GPT-3 came out. So backstory on the podcast: when I graduated college I was planning on doing some sort of AI wrapper startup, and the podcast was just a gateway into doing that. I was trying out different things and at the time I remember thinking, "oh, 3.5 is out." People were like, "I'm so behind on the startup scene here" or whatever. If I wanted to make my own wrapper, maybe the idea of the wrapper was inadvisable in the first place.

But every time feels early because if it's an exponentially growing process, and there are many things, many ideas which are only becoming possible now, right?

**Sholto:** Exactly. It's that product exponential. Products literally obsolete it. You need to constantly reinvent yourself to stay at the frontier of capabilities.

**Trenton:** Do you remember? I had a really shitty idea, and I gave you a call. I don't remember what it was. I think it was like RAG for lawyers, or something. Anyways, I think one of our first interactions was like, "Hey, what do you think of this idea?" And you were like, "I think the podcast sounds promising."

**Dwarkesh:** I was right.

**Trenton:** Which I appreciate. I got slightly annoyed at a friend recently who I think is really talented and clever and interested in AI but has pursued a biology route. I just kind of tried to shake them like, "You can work on AI if you want to."

Humans are biological general intelligences where a lot of the things of value are just very general. Whatever kind of specialization that you've done maybe just doesn't matter that much. Again, it gets back to the sunk cost, but so many of the people, even my colleagues at Anthropic are excited about AI. They just don't let their previous career be a blocker. Because they're just innately smart, talented, driven, whatever else, they end up being very successful and finding roles.

It's not as if they were in AI forever. I mean, people have come from totally different fields. Don't think that you need permission from some abstract entity to get involved, and apply, and be able to contribute. If somebody wanted to be an AI researcher right now, if you could give them an open problem, or the kind of open problem that is very likely to be quite impressive, what would it be?

**Dwarkesh:** I think that now that RL's come back, papers building on Andy Jones's "Scaling Scaling Laws for Board Games" are interesting. Investigating these questions like the ones you asked before—is the model actually learning to do more than its previous pass at K? Or is it just discovering that? Exploring questions like that deeply are interesting: scaling laws for RL, basically. I'd be very curious to see how much the marginal increase is in meta-learning from a new task, or something.

**Trenton:** On that note, I think model diffing has a bunch of opportunities. People say, "Oh, we're not capturing all the features. There's all this stuff left on the table." What is that stuff that's left on the table? If the model's jailbroken, is it using existing features that you've identified? Is it only using the error terms that you haven't captured?

I don't know. There's a lot here. I think MATS is great. The Anthropic fellowship has been going really well. Goodfire—Anthropic invested in recently—they're doing a lot of interpretability work. Or just apply directly to us. Anything to get your equity up, huh?

**Sholto:** There's just so many interpretability projects. There's so much low-hanging fruit, and we need more people, and I don't think we have much time. I also want to make a plug for performance engineering. This is one of the best ways to demonstrate that you have the raw ability to do it. If you made an extremely efficient transform implementation on TPU, or Trainium, or Incuda, then I think there's a pretty high likelihood that you'll get a job offer.

But there's a relatively small pool of people that you can trust to completely own end-to-end the performance of a model. And if you have broad, deep electrical engineering skills, I think you can probably come up to speed pretty fast on accelerator stuff. You can come up to speed reasonably fast and it teaches you a lot of good intuitions about the actual intricacies of what's going on in the models, which means that you're then very well-placed to think about architecture and this kind of stuff.

One of my favorite people in thinking about architecture at Anthropic at the moment actually came from a heavy GPU kernel programming background and just knows the ins and outs really deeply. He can think about the trade-offs really well.

**Dwarkesh:** This was fun guys. Thanks for doing it again.

**Sholto:** Great to be back.

---

*Note: All preview content, advertising, and promotional material has been removed from this transcript. The panel conversation begins at its natural starting point with the opening joke about the name mix-up. Timestamps and episode links that served as audience-retention devices have been excluded.*

## Verification Notes

[^1]: **RL from Verifiable Rewards**: This refers to reinforcement learning where models receive clear, objectively verifiable reward signals (like passing unit tests or correct answers) rather than subjective human feedback on preference pairs.

[^2]: **ClaudePlaysPokemon**: A public demonstration of Claude (Anthropic's AI) playing through a Pokémon game, showcasing multi-turn reasoning and agent capabilities across extended tasks.

[^3]: **Andy Jones "Scaling Scaling Laws for Board Games"**: Referenced research on scaling laws for reinforcement learning in game domains, informing understanding of how RL performance scales with compute and iterations.

[^4]: **MATS**: Referring to the Machine Learning for Alignment Bootcamp (or similar technical alignment/research training program), a pathway for researchers entering AI safety work.

[^5]: **Goodfire**: An interpretability-focused AI research company, mentioned as recently receiving Anthropic investment, working on mechanistic interpretability tools and techniques.

[^6]: **Jensen Huang quote**: Paraphrased reference to statements about directing AI systems even when vastly outnumbered in raw capability—illustrating the potential value of human direction in worlds with advanced AI.
