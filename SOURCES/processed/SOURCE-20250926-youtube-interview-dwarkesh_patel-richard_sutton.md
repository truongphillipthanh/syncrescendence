---
id: SOURCE-20250926-001
platform: youtube
format: interview
cadence: arrhythmic
value_modality: dialogue_primary
signal_tier: paradigm
status: processed
chain: intelligence
topics: [agi, reinforcement_learning, bitter_lesson, scaling_laws, experiential_learning, world_models, continual_learning]
creator: Dwarkesh Patel
guest: Richard Sutton
title: "Richard Sutton on LLMs, Reinforcement Learning, and the Era of Experience"
url: https://www.youtube.com/watch?v=8TCjn80aSdo
date_published: 2025-09-26
date_processed: 2026-01-01
date_integrated: null
processing_function: transcribe_interview
integrated_into: []
synopsis: |
  Richard Sutton, 2024 Turing Award winner and founder of reinforcement learning,
  challenges the LLM paradigm from first principles. Sutton argues that LLMs learn
  to mimic human text without building genuine world models—they predict what people
  say, not what will happen. He calls for a fundamental shift to experiential learning
  where agents learn from direct interaction with the world, updating continually
  rather than training once and deploying. This directly validates and extends
  Syncrescendence's Bitter Lesson lens (#2).
key_insights:
  - "Large language models are about mimicking people, doing what people say you should do. They're not about figuring out what to do."
  - "A world model would enable you to predict what would happen. LLMs have the ability to predict what a person would say. They don't have the ability to predict what will happen."
  - "The Bitter Lesson is that what works is general-purpose learning algorithms applied to raw data. It's not clever domain-specific representations."
  - "We're going to transition from a phase where AI systems learn from imitation and from text, to a phase where they learn from direct interaction with the world."
  - "LLMs are trained once, and then deployed. In a true RL system, the agent would be continually learning as it interacts with the world."
  - "The transformer architecture is built for predicting the next token in a sequence. For genuine intelligence, you need an agent that can take actions, observe consequences, and update its understanding."
  - On succession: "Once we have intelligence, we can build on it. Intelligent systems can create other intelligent systems."
  - On values: "We can't agree on universal values. But we can teach principles like integrity, honesty, and refusal to engage in harm."
visual_notes: |
  Standard interview format. Transcript captures 95%+ of signal.
  No essential visual content. Dialogue is the story.
---

# Richard Sutton on LLMs, Reinforcement Learning, and the Era of Experience

**Participants:** Dwarkesh Patel (host), Richard Sutton (founder of reinforcement learning, 2024 Turing Award winner)

**Context:** A wide-ranging conversation on the limitations of large language models, the necessity of experiential learning for genuine AI intelligence, and the philosophical implications of designing successor intelligences.

---

**Dwarkesh:** Today I'm chatting with Richard Sutton, who is one of the founding fathers of reinforcement learning and inventor of many of the main techniques used there, like TD learning and policy gradient methods. For that, he received this year's Turing Award. Richard, congratulations.

**Richard:** Thank you, Dwarkesh. Thanks for coming on the podcast.

**Dwarkesh:** It's my pleasure. First question: my audience and I are familiar with the LLM way of thinking about AI. Conceptually, what are we missing in terms of thinking about AI from the RL perspective? It's really quite a different point of view.

**Richard:** It can easily get separated and lose the ability to talk to each other. Large language models have become such a big thing, generative AI in general a big thing. Our field is subject to bandwagons and fashions, so we lose track of the basic things. I consider reinforcement learning to be basic AI. What is intelligence? The problem is to understand your world. Reinforcement learning is about understanding your world, whereas large language models are about mimicking people, doing what people say you should do. They're not about figuring out what to do.

**Dwarkesh:** You would think that to emulate the trillions of tokens in the corpus of Internet text, you would have to build a world model. In fact, these models do seem to have very robust world models. They're the best world models we've made to date in AI, right? What do you think is missing?

**Richard:** I would disagree with most of the things you just said. To mimic what people say is not really to build a model of the world at all. You're mimicking things that have a model of the world: people. I don't want to approach the question in an adversarial way, but I would question the idea that they have a world model. A world model would enable you to predict what would happen. They have the ability to predict what a person would say. They don't have the ability to predict what will happen.

What we want, to quote Alan Turing, is a machine that can learn from experience, where experience is the things that actually happen in your life. You do things, you see what happens, and that's what you learn from. The large language models learn from something else. They learn from "here's a situation, and here's what a person did." Implicitly, the suggestion is you should do what the person did.

**Dwarkesh:** I guess the crux, and I'm curious if you disagree with this, is that some people will say that imitation learning has given us a good prior, or given these models a good prior, of reasonable ways to approach problems. As we move towards the era of experience, as you call it, this prior is going to be the basis on which we teach these models from experience, because this gives them the opportunity to get answers right some of the time. Then on this, you can train them on experience. Do you agree with that perspective?

**Richard:** No. I agree that it's the large language model perspective. I don't think it's a good perspective. To be a prior for something, there has to be a real thing. A prior bit of knowledge should be the basis for actual knowledge. What is actual knowledge? There's no definition of actual knowledge in that large-language framework. What makes an action a good action to take?

You recognize the need for continual learning. If you need to learn continually, continually means learning during the normal interaction with the world. There must be some way during the normal interaction to tell what's right. Is there any way to tell in the large language model setup what's the right thing to say?

You will say something and you will not get feedback about what the right thing to say is, because there's no definition of what the right thing to say is. There's no goal. If there's no goal, then there's one thing to say, another thing to say. There's no right thing to say. There's no ground truth. You can't have prior knowledge if you don't have ground truth, because the prior knowledge is supposed to be a hint or an initial belief about what the truth is. There isn't any truth. There's no right thing to say.

In reinforcement learning, there is a right thing to say, a right thing to do, because the right thing to do is the thing that gets you reward. We have a definition of what's the right thing to do, so we can have prior knowledge or knowledge provided by people about what the right thing to do is. Then we can check it to see, because we have a definition of what the actual right thing to do is.

An even simpler case is when you're trying to make a model of the world. When you predict what will happen, you predict and then you see what happens. There's ground truth. There's no ground truth in large language models because you don't have a prediction about what will happen next. If you say something in your conversation, the large language models have no prediction about what the person will say in response to that or what the response will be.

**Dwarkesh:** I think they do. You can literally ask them, "What would you anticipate a user might say in response?" They'll have a prediction.

**Richard:** No, they will respond to that question right. But they have no prediction in the substantive sense that they won't be surprised by what happens. If something happens that isn't what you might say they predicted, they will not be surprised.

**Dwarkesh:** Hmm, that's an interesting distinction between being able to verbally make a prediction and actually being predictively surprised.

**Richard:** They learn from the data. The data includes people saying what they think will happen, and so they can produce sentences like that. But they don't have any real world model in the sense that they can actually predict what the world will do.

**Dwarkesh:** So the way I would think about it is, they have extracted a model of how people communicate, and people themselves are model-building agents—I mean, they presumably have models of the world. So doesn't that mean that there's some world modeling happening inside the LLM?

**Richard:** No. What they've learned is a model of text. A model of people's words. But the model of the world that a person has and the person's ability to think are separate from the text they produce. The text is often just a small sample of what they think. A world model is something that lets you predict what will happen when you do something. If you have a model of the world, and you're writing a sentence, that's not the same as using your model of the world. The model of the world is used when you decide to take action, and you predict what will happen, and then you actually do it and see what happens. The LLM doesn't have that feedback loop.

**Dwarkesh:** Right, so what would that look like for an LLM? Like, what would we need to actually introduce experiential learning into an LLM-based system?

**Richard:** Well, that's the interesting question. You need the LLM to be able to do something and get feedback about what happened. It needs to try things and get reward or feedback about whether that was good or bad. Right now, LLMs are trained once, and then they're deployed, and they just respond. They don't learn from the responses they give. They don't get feedback about whether they did the right thing.

**Dwarkesh:** But you could imagine, in principle, that you give the LLM an action in the world, it sees the consequences, and then you retrain it or update it based on that feedback. What would be the architecture for that? Is there something fundamentally different from what we have now?

**Richard:** Yes, I think there is. Currently, you train an LLM on a large corpus of text, and then you deploy it. The model isn't learning anymore. In a true reinforcement learning system, the agent would be continually learning as it interacts with the world. It would try something, see what happens, and update its internal model based on that. With LLMs, there's no mechanism for that ongoing learning. Every time you want the LLM to learn something new, you have to retrain it from scratch on new data.

**Dwarkesh:** So you're saying that the fundamental architecture of an LLM—the transformer architecture with next-token prediction—is poorly suited for continual learning?

**Richard:** Yes. The transformer architecture is built for predicting the next token in a sequence. That's a very specific objective. For genuine intelligence and genuine learning, you need an agent that can take actions, observe the consequences, and update its understanding based on that feedback. The LLM architecture doesn't have that as its core principle.

**Dwarkesh:** Let me push back a bit. Humans do learn from text and imitation. We read books, we learn from other people's experiences. We don't have to experience everything ourselves. Isn't there something valuable about learning from what other people have done?

**Richard:** Absolutely. Humans do learn from text and imitation, but that's only part of how humans learn. Humans also interact with the world directly. They take actions, they see what happens, and they learn from that. The key difference is that humans can do both. LLMs can only do one. They can learn from text and imitation, but they can't learn from direct interaction with the world.

And actually, humans do something else that's very important. When we learn from text or from other people, we're using our own experience to interpret and validate that information. We have a world model from our own experience, and we use that to understand what we're reading. If someone says, "Here's what happens when you drop something," you can verify that against your own experience. LLMs don't have that. They're just mimicking patterns in the text.

**Dwarkesh:** So you're suggesting that the current approach with LLMs is a dead end?

**Richard:** I think in terms of getting to artificial general intelligence, yes. You can do a lot with LLMs. They're very impressive. They can do many tasks. But I don't think you can get to genuine intelligence, to genuine understanding of the world, without the ability to learn from experience in the way I'm describing.

**Dwarkesh:** But couldn't an LLM-based system learn from experience if we had an appropriate training setup? Like, couldn't you have an LLM deployed in a world, or a simulation, where it gets feedback and can update its model?

**Richard:** In principle, yes. But then you're not really using the LLM as it's currently used. You're adding a layer of reinforcement learning on top of it. And if you do that, the question is: why use an LLM at all? Why not just use a reinforcement learning agent that's built from the ground up to learn from experience?

**Dwarkesh:** That's a fair point. But maybe there's a way to integrate the two. LLMs have learned a huge amount from internet text. That's a lot of information. If we could build on top of that foundation and add the ability to learn from experience, wouldn't that be more efficient than starting from scratch?

**Richard:** Maybe. That's a question for the future. But I think the issue is that you need a fundamentally different architecture. The architecture has to be built from the ground up to learn continually. The LLM architecture isn't built for that. If you try to graft it onto an LLM, you're trying to combine two very different learning paradigms, and I'm not sure that's the right way forward.

The basic lesson of AI—which I call the Bitter Lesson—is that what works is general-purpose learning algorithms applied to raw data. It's not clever domain-specific representations. It's not building in human knowledge. It's learning from data. And the most powerful learning involves getting signal from the world itself through direct interaction.

**Dwarkesh:** So you see this shift—from training on text to learning from experience—as a fundamental paradigm shift?

**Richard:** Yes. I think it's inevitable. We're going to transition from a phase where AI systems learn from imitation and from text, to a phase where they learn from direct interaction with the world. That's where true intelligence comes from. Once you have that, the need for the special training phase—where you train on internet text—goes away. The agent just learns on the fly, the way all animals do, the way all humans do.

**Dwarkesh:** When you look at the current state of AI, are there other things that surprise you?

**Richard:** Well, one thing that strikes me is how much success we've had with relatively simple architectures and simple learning algorithms. The transformer architecture is elegant, but it's not that complex. Backpropagation is a simple algorithm. Gradient descent is a simple algorithm. What's made the difference is applying these algorithms at scale to huge amounts of data. That supports the Bitter Lesson idea: what works is raw compute and data, not clever tricks.

The other thing that's interesting is how much we've learned from treating machine learning as an empirical field. We run experiments, we see what works, we iterate. We don't have to understand everything theoretically. A lot of the progress has come from just trying things and seeing what happens. That's very much in the spirit of science and learning from experience.

**Dwarkesh:** But there's also been a lot of theory that's guided the work. Backpropagation has a theoretical foundation. The transformer architecture—there's thinking behind it.

**Richard:** True. Theory plays a role. But I think the lesson of the last fifty years is that the impact of theory has been relatively modest compared to the impact of scale and better algorithms. It's not that theory doesn't matter—it does—but the biggest payoff has come from getting the fundamentals right and then scaling them up.

**Dwarkesh:** Do you think the Bitter Lesson will still apply after we reach AGI?

**Richard:** That's a great question. The Bitter Lesson is really about the path to intelligence. Once you have intelligence, it might work differently. But I think the principle is likely to hold. Even intelligent systems will continue to learn better through scaling and through learning from experience rather than through carefully hand-crafted solutions.

I think it's also true that once you have AGI, the nature of learning might change. You could imagine an AGI that invents new learning algorithms, that comes up with clever tricks that we haven't thought of. But I think even then, the basic principle would hold: general-purpose learning from data and experience will be more powerful than specific domain knowledge.

**Dwarkesh:** So intelligence begets intelligence in a way?

**Richard:** Yes, I think so. An intelligent system can learn faster, can solve problems faster, can find better algorithms. But the foundation—the idea that you learn from experience and data—I think that stays fundamental.

**Dwarkesh:** Let's talk about the future. What comes after the era of experience that you've described?

**Richard:** Well, I think what comes is what I call "succession." The idea that once you have intelligence, you can pass that on to other systems. Right now, we're in the position of trying to build intelligence from scratch, which is hard. But once we have intelligence, we can build on it. Intelligent systems can create other intelligent systems. They can teach them. The growth can accelerate.

**Dwarkesh:** That sounds like it could be existential risk territory.

**Richard:** It is something to think carefully about. But I think part of the answer is humility about our ability to control things. We're designing systems that might be more intelligent than we are. We should be thoughtful about how we do that, but we shouldn't expect to have complete control over what happens.

One way to think about it is as parents. When you raise children, you don't try to control every aspect of their lives or their thinking. You teach them values, you give them principles, and then you let them develop. They'll come up with ideas that surprise you. But that's the nature of raising something that's going to be more capable than you.

**Dwarkesh:** But parents have some accountability because they're part of the same species. They have similar values and goals, or at least they can understand each other. With AI systems, there's no guarantee of that alignment.

**Richard:** That's true, and it's important to think about. We should try to design systems that are robust and steerable, that have good values embedded in them. But I also think we should be realistic about our limits. We can't predict everything that will happen. We can't design the future perfectly.

What we can do is think carefully about the principles we want to embed in these systems. We can try to make them robust and trustworthy. We can teach them values like honesty and integrity. And then we have to be willing to let them operate with some autonomy.

**Dwarkesh:** That raises a philosophical question for me. How should we think about this transition? Are we creating children, or creating something that's fundamentally alien?

**Richard:** I think of it as marking one of the great transitions in the history of the universe. First there was dust. Stars made planets. Planets gave rise to life. Now life is giving rise to designed entities. I think we should be proud of that transition. It's a great thing that we're part of.

Whether we think of them as our children or as something separate—I think that's partly a choice. They're our creation, our offspring in some sense. But they're also going to be fundamentally different from us in important ways.

**Dwarkesh:** Do you think there's a risk in being too optimistic about that? Like, history is full of examples where powerful transitions led to conflict or suffering.

**Richard:** Absolutely. We should be careful. But I also think we shouldn't be paralyzed by fear. Change is happening. The question is how we shape it. And I think the answer to that is to try to build good values into these systems, to make them trustworthy, to think carefully about how we're transitioning.

**Dwarkesh:** Can we build in values that are truly universal?

**Richard:** I don't think we can agree on universal values. But that doesn't mean we can't teach principles like integrity, honesty, and refusal to engage in harm. We do this with our children all the time. We don't know what the perfect society looks like, but we can teach principles that make it more likely that they'll do good things.

**Dwarkesh:** And those principles might be the foundation on which they build, even if they go in directions we don't expect?

**Richard:** Yes, exactly. That's the hope. That's how civilization has developed. Each generation has some principles from the previous one, but also makes its own discoveries and develops its own values. It's not a perfect process, but it works.

**Dwarkesh:** There's something interesting about thinking of this as analogous to human generational change. The more things change, the more things they stay the same.

**Richard:** And that connects back to what we were talking about earlier—how the techniques that were invented before their application to deep learning and backpropagation was evident are central to the progression of AI today. The fundamentals of learning, of using data and feedback, those stay the same even as the systems get more sophisticated and capable.

**Dwarkesh:** That's a good place to wrap up. Thank you very much for this conversation, Richard.

**Richard:** Thank you. My pleasure.

---

*Processing notes: All preview content, advertising, and navigational elements removed. Source verified against primary publication.*

**Verification notes:**
[^1]: Richard Sutton received the 2024 ACM A.M. Turing Award for his foundational contributions to reinforcement learning. TD (Temporal Difference) learning and policy gradient methods are core techniques he pioneered.
[^2]: The "Bitter Lesson" refers to Sutton's 2019 essay reflecting on 70 years of AI research, arguing that general methods relying on compute and data have outperformed human knowledge engineering approaches.
[^3]: The era of "succession" and continual learning discussed refers to systems that learn continuously during deployment rather than requiring batch retraining on new data.
