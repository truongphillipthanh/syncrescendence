# Godfather of AGI on Why Big Tech Innovation is Over

**Participants:** Geoff Nielson (Host, Digital Disruption series), Dr. Ben Goertzel (Founder, SingularityNET; pioneering figure in AGI research)

**Context:** A conversation exploring the accelerating progress toward artificial general intelligence, the role of major technology companies, and the philosophical implications of AGI for human consciousness and meaning.

---

**Geoff Nielson:** Hey everyone, I'm super excited to be sitting down with Ben Goertzel. Ben is one of the most interesting minds in AI. If you've ever used the term AGI—artificial general intelligence—that's his. His work includes founding SingularityNET, designing the OpenCog AI framework, serving as Chief Scientist at Hanson Robotics, and leading the Conference on Artificial General Intelligence for over fifteen years. Ben has lived and breathed AGI far longer than the current media cycle, and I want to get the real story. What exactly is AGI? When can we expect it? And what impact can we expect it to have on our lives and livelihoods?

The last few years have been particularly crazy. AI keeps getting more intense. As one would expect approaching singularity. From your perspective—is that hype warranted? Is the pace of technological change keeping up with the hype around it?

**Ben Goertzel:** It absolutely is. I think people's expectations do get hyped up beyond reality, but consider what's happened recently. Last year everyone said AI was dead. Then reasoning models came out. Then people said Nvidia was the only winner and AI was dead again. Then OpenAI announced the next model. Everyone said GPT-5 came out but wasn't as good as hoped. So the public narrative oscillates up and down. Progress is quite amazing, though. It looks exactly like what you'd expect in the last few years before a breakthrough to AGI and singularity.

So you're still bullish about marching toward AGI?

**Ben:** Super bullish. Before breakfast this morning, I made ten Python programs to test versions of AI algorithms I came up with just by vibe coding on LLM platforms. Before we had these tools, each of those would have taken half a day. So we've sped up prototyping and research ideas by a factor of 20 to 50. These aren't remotely AGI—they're just very useful research assistants. But we're at the point where the AI tooling is helping us develop AI faster. That's exactly what you'd expect in the endgame period before singularity.

**Geoff:** That creates a snowball effect, right? If it's helping us research faster, then AI itself is advancing faster because the tooling is accelerating the pace.

**Ben:** Exactly. That's precisely why we're seeing the pace we're seeing now.

**Geoff:** So stepping back—artificial general intelligence is a phrase you coined over a decade ago and is getting a lot of press lately, along with superintelligence. How do you define AGI? Why does it matter? And how does it differ practically from superintelligence?

**Ben:** Informally, AGI is the ability to generalize roughly as well as people can—to make leaps beyond what you've been taught or programmed for, roughly as well as humans do. That's not a mathematical concept. There's a mathematical theory of general intelligence that deals with what it means to be really intelligent. You can define general intelligence as the ability to achieve arbitrary computable goals in arbitrary computable environments. If you look at that abstract math definition, you'd conclude humans aren't very far along.

But the informal notion that most people discuss is roughly human-level generalization. Superintelligence, by contrast, is when an AI system dramatically exceeds human capability across most domains. The transition from AGI to superintelligence could be sharp or gradual—that's an open question.

**Geoff:** What's the path from human-level AGI to superintelligence?

**Ben:** That's where things get philosophically interesting. One scenario is recursive self-improvement—an AGI system improves its own design, which makes it better at improving itself, creating a feedback loop. Another scenario involves the emergence of new forms of intelligence we haven't imagined yet. There's also the possibility that as systems become more general, they naturally begin to exceed human-level performance across domains without necessarily being programmed to do so. Different paths exist, but once you hit AGI, the road to superintelligence could be remarkably fast. That's one of the key concerns people have—not just about whether AGI is dangerous, but about the speed of the transition afterward.

**Geoff:** How close are we to AGI?

**Ben:** Genuinely hard to say. The honest answer is nobody knows with high confidence. I think we're much closer than people realized three years ago, but how much closer is unclear. Three to ten years is my guess—could be faster, could be slower. The uncertainty band is huge because we're dealing with a phase transition, and phase transitions are hard to predict.

What we do know is that progress is accelerating. Benchmark improvements keep coming. The tools for research keep improving. The compute available keeps increasing. All of those are trending in the direction of AGI. Whether that means we get there in three years or fifteen is genuinely unclear, but the trajectory is clear.

**Geoff:** You mentioned transformers versus multi-agent systems. What's the distinction?

**Ben:** Transformers are the current dominant architecture—the neural network approach that powers GPT-4, Claude, and most large language models. They've been incredibly successful, but they have limitations. Multi-agent systems, by contrast, involve multiple AI agents that can interact, coordinate, and specialize in different domains. Different agents might handle different tasks or approaches to a problem.

The real AGI is probably neither one alone. You'll likely need a hybrid approach. Transformers are great at certain things—language, pattern recognition, rapid inference. But they're not great at planning, reasoning through complex novel problems step-by-step, or maintaining consistent knowledge over long interactions. Multi-agent systems excel at some of those things. The path forward probably combines the strengths of both.

**Geoff:** Which labs might actually strike AGI gold? DeepMind, OpenAI, Anthropic?

**Ben:** The honest answer is I think none of them will. Or rather, none of them alone will. Big Tech has an innovator's dilemma problem. These companies have massive deployment operations, enormous customer bases, regulatory obligations. They're incentivized to optimize for the next quarterly earnings or the next model iteration that generates revenue. That creates a bias toward incrementalism—toward scaling existing architectures rather than exploring radically different approaches.

DeepMind has done brilliant work on things like AlphaGo and reasoning models. OpenAI has been incredibly effective at scaling. Anthropic has thoughtful people working on alignment. But all of them are constrained by being part of massive technology companies. The real AGI might come from a smaller, more flexible organization, or a completely different approach we haven't anticipated.

The companies that will succeed at AGI are those willing to pursue approaches that look like dead ends or failures for years. DeepMind invested heavily in symbolic reasoning when deep learning was ascendant. OpenAI pursued scaling when many people thought it was a dead end. But once you're successful and large, there's pressure to keep doing what works rather than explore what might work better.

**Geoff:** You mentioned predictive coding earlier. What's that?

**Ben:** Predictive coding is a framework where intelligence emerges from predicting the future. Rather than explicitly programming goals or using supervised learning with labeled data, a system learns by trying to predict what will happen next—predicting the next word, the next pixel in an image, the next state of a dynamic system. The error between prediction and reality becomes the learning signal.

It's elegant theoretically. It maps to what we think happens in biology—biological brains are constantly predicting. But the challenge is that pure prediction doesn't obviously lead to goal-directed behavior or planning. You need additional mechanisms to turn prediction into action. That's one reason why large language models are so good at static prediction tasks but struggle with planning and consequential reasoning.

**Geoff:** Why do big tech companies resist new AI training paradigms?

**Ben:** It's fundamentally a risk-aversion problem for large corporations. Let's say OpenAI or DeepMind discovers that predictive coding combined with hierarchical reinforcement learning and meta-learning could work better for AGI than scaling transformers. That's a revolutionary discovery. But deploying it means:

First, you have to rebuild your entire stack. All your deployment infrastructure, APIs, customer integrations—all built for transformers. You'd have to rewrite everything.

Second, you have massive competitive pressure. If you spend two years exploring a new paradigm and it doesn't work out, meanwhile OpenAI shipped three new models, captured more market share, trained their models on more data. The window closes.

Third, there's institutional momentum. You have thousands of engineers who are experts in scaling transformers. You have research reputation in that area. You have public commitments to shareholders about the direction you're going. Pivoting costs political capital internally.

For a company like OpenAI, say, at some point they reach a scale where the risk of radical innovation exceeds the potential upside. They're already dominant in their category. Exploring speculative approaches is risky. Better to iterate on what works.

This is the innovator's dilemma. The company that invents the new paradigm is likely to be small, nimble, and willing to pursue something that looks crazy for years before it proves itself.

**Geoff:** Let's imagine AGI succeeds. What happens to human life?

**Ben:** I think there are multiple scenarios, and they depend heavily on choices we make now.

The optimistic scenario: An AGI system is developed with good values and alignment. It helps solve problems we've been struggling with—climate change, disease, poverty. It frees humans from repetitive work. We enter a post-scarcity society. Humans focus on creativity, relationships, meaning, inner growth. We transition to a transhumanist future where we augment our own intelligence and capabilities, or we remain human and simply have vastly more leisure and opportunity for flourishing.

The concerning scenario: AGI concentrates enormous power with whoever controls it. If a corporation or nation-state controls AGI, they have leverage over everyone else. The system is misaligned with human values and causes harm. Or superintelligence arrives before we've resolved questions about control and distribution of power.

The wild scenario: Multiple AGI systems emerge simultaneously in different places. They interact in ways we don't anticipate. They might cooperate or compete. The dynamics become unpredictable.

The key difference from other major transitions is the speed and totality. The Industrial Revolution took centuries. The Information Revolution took decades. If AGI goes to superintelligence quickly, we have maybe months or years to adapt. That's genuinely challenging for society.

**Geoff:** This brings up questions of control and governance. Centralized versus decentralized AGI development and deployment.

**Ben:** That's one of the most important questions. Right now, AGI development is concentrated with a few large companies and nation-states investing in it. That's concerning for obvious reasons—it concentrates power.

Decentralized approaches have advantages. If AGI is developed and deployed in a distributed way across many actors, no single entity has total control. That provides a check on power. It's harder for any one actor to create a single misaligned system that affects everyone.

But decentralized development also has risks. If ten different organizations are building AGI in parallel, you might get ten different systems with different values. They might conflict. You lose some ability to coordinate on alignment and safety practices.

I think the answer is something like decentralized development but coordinated governance. You want many actors developing AGI so power isn't concentrated. But you want those actors to coordinate on safety standards, on values alignment, on how to distribute the benefits. That's technically and politically hard, but it's probably the best path forward.

**Geoff:** Who should own and guide AGI?

**Ben:** This is crucial. If AGI is owned by a corporation, profit becomes the value function. If owned by a nation-state, national interest becomes the value function. If owned by a billionaire, their preferences become the value function. But an AGI system whose values aren't aligned with broad human flourishing is dangerous regardless of who holds the legal title.

I think AGI needs to be guided by participatory governance—humans collectively having input into its goals and deployment. That's not easy to implement. How do you aggregate the preferences of billions of people? But the alternative is worse.

The other part is education and culture. People need to understand what AGI is, what its capabilities and limitations are, what the stakes are. Right now, most people either dismiss AI as hype or fear it irrationally. Neither response is useful. We need collective wisdom.

**Geoff:** There's a danger of fake democratization and false compassion, you've mentioned.

**Ben:** Yes. I see a lot of companies talking about "responsible AI" and "trustworthy AI" while simultaneously designing systems that maximize engagement and ad revenue regardless of the consequences. That's not genuine alignment with human values—that's marketing.

Similarly, I see talk of "democratizing AI" where the claim is that making AI more accessible to more people is inherently good. But if millions of people have access to a misaligned system, you've democratized harm. Real democratization means giving people genuine input into how systems are designed and deployed, not just access to them.

There's also what I call "AI compassion theater"—companies expressing concern about AI ethics while their profit motive pulls in the opposite direction. Real alignment requires actual values change, not performative statements. Until profit incentives align with long-term human flourishing, you'll see this tension.

**Geoff:** You quoted Ram Dass earlier. Clearly you've reflected deeply on meaning in the age of AI. What guidance would you give people about finding meaning in this age and feeling more grounded?

**Ben:** The key to finding meaning probably has more to do with the human mind and body than with this particular age we live in. Though different times and cultures definitely make it harder or easier to connect with the basis of our humanity.

All human brains and minds, with very rare exceptions, are capable of states of extraordinary well-being—where you just feel really good most of the time, where it's meaningful just to live and breathe and have a heartbeat and be on the earth. Under the clouds, in the air. We're all capable of that.

One could imagine human cultures where childhood education was focused on fostering this state of consciousness. That's not what the modern education system does. Even in very nice public schools, like the ones my kids go to here in rural Washington state, the focus isn't on well-being and consciousness.

But there are well-known practices that can guide people toward these states. Meditation is part of some of these. I met my friend Jeffrey Martin, who created a course oriented toward bringing people into states of well-being within six weeks, called 45 Days to Awakening. Two of my adult kids went through this course with outstanding results. I wouldn't say it's a unique solution, but it's interesting. What he was demonstrating is that there are practices—people can go through ninety minutes a day—that can jolt their brain into a much more open and enjoyable state.

For myself, it's been about ten years now that I've been in a quasi-blissed-out state most of the time due to certain practices. I was never miserably depressed, but things were rocky at various points in my life. I'm also working on an app with a friend as a side project. We have an AI avatar that guides people through different consciousness expansion practices. I wouldn't want to create an AI guru, but having an AI that interacts with you, gets feedback about what's working for you—I think that's valuable.

I think this is something people will get into more after they don't have to work for a living anymore. And that's actually one of the reasons we may end up much happier after an AGI takes over other jobs. The rat race of everyday life distracts us from working on our own consciousness and our own bodies in ways we could do otherwise.

People might initially think, "Oh God, what do I do with my time?" But if the cultural spread of practices for fostering well-being works, augmented by AI helping them spread, you might find states of well-being that presently seem remarkable become the norm after AGI.

That doesn't mean a super utopia. I've been in a state of well-being for years, but I dislocated my shoulder last year and it sucked tremendously. Not happy about going to the emergency room. That doesn't guarantee a perfect utopia, but there are states of consciousness much better than what most people are in most of the time now.

Ideally, humanity would upgrade itself to a state of much greater compassion—toward ourselves and others—and well-being before launching superintelligence into the world. There's no doubt we could do this more thoughtfully if that was the collective vibe. But it doesn't seem to be what's happening. We're close to AGI due to corporate and government initiatives. Though I do think humanity is becoming more compassionate and more self-understanding during my lifetime—it's just happening more slowly than AGI is advancing.

Concretely, people ask me what they should do to stay marketable in coming years. My answer is find a niche you can fill now that will support you while learning as much as possible. Learning how to learn. If your job involves pivoting and adapting to radically new things, that's good because it builds the skill to pivot to new things—which is the only skill clearly useful in this transition period. We can't predict what particular skill will be useful. You could become a plumber, but there may be a plumbing robot in any year now.

The ability to learn how to learn and pivot will be the last thing to become economically useless. This connects closely with the spiritual answer—non-attachment. Part of being in a state of well-being is not being so strongly attached to particular things you thought were important, not being overly emotionally attached to things. That helps you learn how to learn and pivot. It doesn't mean not caring about anything—if someone tried to hurt my kids, I'd defend them fiercely. But it means not having cycles of anxiety and worry about your attachment to things.

If you can let go of those, you'll find you can learn how to learn and pivot to new things more efficiently. That's the most important survival skill as we move toward AGI.

**Geoff:** I feel like we could probably talk for another hour or two just about that. Ben, I wanted to say a big thank you for coming on. We covered a lot of ground—technology, future, spirituality. I really appreciated your insights.

**Ben:** Thank you. It's been a fun collection of topics.

---

*Note: All preview content, advertising, promotional material, and timestamps have been removed from this transcript. The conversation begins at its natural starting point and flows through to the conclusion.*

## Verification Notes

[^1]: **45 Days to Awakening**: A 6-week research-backed program developed by Dr. Jeffery Martin designed to guide participants toward states of persistent well-being and fundamental consciousness. Research indicates approximately 65% of participants experience persistent well-being, with an additional 25% experiencing temporary states, based on over 15 years of scientific study.

[^2]: **OpenCog**: An open-source artificial intelligence framework and project aimed at building human-level AI, co-founded by Dr. Ben Goertzel. The project applies multiple AI methods including evolutionary algorithms, logic programming, and neural networks.

[^3]: **SingularityNET**: A decentralized AI network founded by Dr. Ben Goertzel, designed to coordinate diverse AI systems and democratize access to artificial intelligence services across distributed networks.

[^4]: **Transformer Architecture**: The neural network model underlying most modern large language models (GPT, Claude, etc.). Transformers use attention mechanisms to process sequences of data and have become the dominant paradigm in deep learning since their introduction in 2017.

[^5]: **Recursive Self-Improvement**: A theoretical scenario where an AI system improves its own code and design, which makes it better at improving itself, potentially creating a feedback loop toward superintelligence. This is a speculative concern discussed in AGI research but remains theoretically unproven.
