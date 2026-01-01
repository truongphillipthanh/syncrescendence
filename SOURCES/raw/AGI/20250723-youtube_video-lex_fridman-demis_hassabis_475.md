# Demis Hassabis: Future of AI, Simulating Reality, Physics and Video Games
## Lex Fridman Podcast #475

**Participants:**  
**Lex Fridman** — Interviewer, host of the Lex Fridman Podcast  
**Demis Hassabis** — CEO of Google DeepMind, Nobel Prize winner for protein structure prediction

---

**Lex:** In your Nobel Prize lecture, you propose a really interesting conjecture: "Any pattern that can be generated or found in nature can be efficiently discovered and modeled by a classical learning algorithm." What kind of patterns or systems are we talking about—biology, chemistry, physics, cosmology, neuroscience?

**Demis:** It's sort of a tradition in Nobel Prize lectures to be a little provocative, and I wanted to follow that. When you look back at all our work—the Alpha projects, AlphaGo, AlphaFold—what they really are is models of very high-dimensional, combinatorially complex spaces. If you tried to brute force a solution, find the best move in Go or the exact shape of a protein, you'd enumerate possibilities that far exceed the atoms in the universe. You have to do something much smarter.

What we did in both cases was build models of those environments that guided the search in an intelligent way, making it tractable. With protein folding, a natural system, proteins fold in milliseconds in our bodies. Somehow physics solves this problem, and we've now solved it computationally too. I think that's possible because natural systems have structure—they were shaped by evolutionary processes. If that's true, then you can learn what that structure is.

**Lex:** There's something really interesting here. You're saying, roughly: anything that can be evolved can be efficiently modeled. Is there truth to that?

**Demis:** I sometimes call it "survival of the stablest." There's evolution for living things, but also—if you think about geological timescales—the shape of mountains shaped by weathering over thousands of years, the orbits of planets, shapes of asteroids. These have all survived selection processes many times over. So there should be some pattern, some manifold that helps you search toward the right solution and predict things efficiently. Because it's not random.

Now, it may not work for manmade things or abstract problems like factorizing large numbers. Unless there's pattern in the number space, if it's uniform, there's no structure to learn—you'd need brute force, maybe a quantum computer. But in natural systems we care about, they have structure that evolved for a reason and survived over time. That's learnable by neural networks.

**Lex:** It's like nature's doing a search process, and in that process it's creating systems that could be efficiently modeled.

**Demis:** That's right.

**Lex:** So they can be efficiently rediscovered because nature's not random. Everything we see around us—elements that are stable, all of it—is subject to selection pressure.

**Demis:** Exactly.

**Lex:** Do you think, given your interest in theoretical computer science and complexity theory, we could formulate a new complexity class—something like learnable natural systems, LNS? Systems that are actually learnable by classical systems?

**Demis:** I've always been fascinated by P equals NP and what's modelable by classical systems, by Turing machines. In my spare time with colleagues, I'm thinking about whether there should be a new complexity class—solvable by these neural network processes, mapped onto natural systems with structure. It could be a very interesting framework.

It fits with how I think about physics generally: information is primary, the most fundamental unit of the universe, more fundamental than energy and matter. Everything converts between them. The universe is fundamentally an informational system.

**Lex:** So if the universe is informational, then P equals NP is a physics question.

**Demis:** That's right.

**Lex:** And one that could help us solve the entirety of what's happening.

**Demis:** Yeah. I think P equals NP is one of the most fundamental questions if you see physics as informational. The answer will be enlightening.

**Lex:** Some of what we're saying sounds crazy now—but like Christian Anfinsen's Nobel Prize speech, which was controversial and sounded crazy, and then you went on to win a Nobel Prize for solving that problem with John Jumper. Let me focus on P versus NP specifically. If you can do polynomial-time or constant-time computation upfront, construct a massive model, could you then solve extremely difficult problems efficiently from a theoretical computer science perspective?

**Demis:** There's a huge class of problems you can couch this way—like AlphaGo and AlphaFold. You model the dynamics of the system, its properties, the environment you're trying to understand. That makes the search for the solution, the prediction of the next step, efficient—polynomial time, tractable by classical systems, neural networks running on normal computers, Turing machines essentially.

How far can that paradigm go? The AI community has shown that classical systems can go much further than we thought. They model protein structures and play Go at superhuman level. People thought decades ago this was decades away, maybe requiring quantum machines for protein folding. But we're just scratching the surface of what classical systems could do. AGI built on neural networks on top of classical computers would be the ultimate expression of that. The question of what bounds that system, directly speaks to P equals NP.

**Lex:** What might be outside this? Emergent phenomena? Like cellular automata—extremely simple systems where complexity emerges?

**Demis:** Those systems would be right on the boundary. Most emergent systems, cellular automata, could be modelable by classical systems—just do forward simulation, probably efficient enough. Chaotic systems are different—where initial conditions matter, leading to uncorrelated end states. Those could be difficult to model. These are open questions.

But when you look at what we've done—the problems we've solved—and then look at Veo 3, video generation rendering physics and lighting, these are really core fundamental things in physics. It tells us something fundamental about how the universe is structured. In a way, that's why I want to build AGI—to help us as scientists answer these questions like P equals NP.

**Lex:** We might be continuously surprised about what's modelable by classical computers. AlphaFold 3 on the interaction side is surprising—you can make progress there. AlphaGenome is surprising—you can map the genetic code to function. There are so many combinatorial options, and yet you find the kernel that's efficiently modeled.

**Demis:** There's structure, some landscape—an energy landscape or whatever—that you can follow. Neural networks are good at following gradients. If there's one to follow and you specify the objective function correctly, you don't have to deal with all the complexity. We've naively thought about these problems for decades—if you enumerate all possibilities, it looks totally intractable. There are 10 to the 300 possible protein structures, 10 to the 170 possible Go positions. Way more than atoms in the universe. How could you possibly find the right solution?

But it turns out you can. Reality does it—proteins fold. That gives confidence that if we understood how physics solves this, we could mimic that process on classical systems. That's the conjecture.

**Lex:** And there's nonlinear dynamical systems, highly nonlinear systems, everything involving fluid dynamics.

**Demis:** Exactly. Fluid dynamics, Navier-Stokes equations—traditionally thought of as very difficult, intractable on classical systems. Weather prediction systems involve enormous compute for fluid dynamics calculations. But look at Veo 3, our video generation model. It models liquids surprisingly well, materials, specular lighting. I've seen videos of clear liquids going through hydraulic presses being squeezed out. I used to write physics engines and graphics engines in my early days in gaming. I know how painstakingly hard it is to build programs that do that. Yet somehow these systems reverse engineer from just watching YouTube videos.

Presumably they're extracting underlying structure around how materials behave. Perhaps there's a lower-dimensional manifold that can be learned. That might be true of most of reality.

**Lex:** I've been fascinated by Veo 3. People highlight the comedic aspects, the memes, the ultrarealistic ability to capture humans, the native audio integration. All marvelous. But what you're mentioning—the physics—isn't perfect, but it's pretty good. And the scientific question is: what does Veo 3 understand about our world to generate videos like that?

The cynical take is diffusion models don't understand anything. But you can't generate that kind of video without understanding something. And then our philosophical notion of understanding surfaces. To what degree does Veo 3 understand our world?

**Demis:** To the extent it can predict the next frames coherently, that's understanding—not anthropomorphic or philosophical understanding of what's happening. These systems haven't modeled that. But they've modeled enough dynamics to generate eight seconds of consistent video that's hard to distinguish from reality. And imagine where this will be in two or three more years, given the trajectory. The rate of progress is incredible.

**Lex:** Video games seem like a natural testing ground for understanding reality. Why have you focused on video games?

**Demis:** Well, I grew up programming in Lisp as a kid, playing lots of games, writing games. Video games are interesting because they're microcosms of physics, with rules that can be relatively simple but produce complex behaviors. Go, for instance, is the simplest conceivable physics—pieces on a board, binary outcome. Yet it's immensely complex. Chess similarly. Video games scale that up with richer physics, visual elements, harder exploration problems.

I think they're great environments for testing AI. There's immediate feedback on whether you're making progress. They're measurable. And they represent a spectrum from simple, deterministic worlds to rich, complex 3D worlds where you need visual understanding. I've been interested in that progression.

**Lex:** AlphaGo was a beautiful achievement, but it was a closed domain. With video games, you're dealing with higher-dimensional observation spaces—pixel inputs, more open-ended problems.

**Demis:** Right. Video games offer something in between. Not as open-ended as the real world, but more complex than board games. You have continuous control, visual scenes, partial observability, stochasticity. And there's a nice range of difficulty. Some games are relatively simple, others incredibly hard. It's a good testing ground.

**Lex:** Have you been surprised by what the systems can do?

**Demis:** Continuously surprised, honestly. When I was younger, I wrote physics engines myself. To build something that handles even simple fluid simulation is phenomenally complex. The fact that systems trained on video can capture that behavior is remarkable. It suggests these systems are learning fundamental principles about how the world works.

**Lex:** Let me ask about AlphaEvolve. This seems like a big leap—recursively improving code. Tell me about it.

**Demis:** AlphaEvolve is enabling something interesting on the programming side—potentially recursive self-improvement. If you imagine what an AGI system might do, maybe not the first version, but a few versions beyond, recursive self-improvement becomes possible. AlphaEvolve has humans in the loop, deciding on various things. Separate hybrid systems that interact. You could imagine eventually doing that end-to-end.

Right now, systems aren't good enough to come up with code architecture on their own. They're good when you give very specific instructions. If you say "make the code faster" for matrix multiplication, they're very good at incrementally improving that. But if you say "invent a game as good as Go," that's underspecified. The current systems don't know what to do with that level of vagueness. Similarly, "make a better version of yourself"—too unconstrained.

**Lex:** But as you do more and more improvements iteratively, at what point does it transition from incremental improvement to something larger?

**Demis:** That's the question. These systems do incremental hill climbing. They're good at it. But could they produce a leap like the Transformer architecture? We don't know if something like AlphaEvolve would have invented Transformers in 2017. These systems might only be capable of incremental improvement. You might need one or two more big breakthroughs on top of that.

**Lex:** But maybe the path to AGI isn't like a hard takeoff. Maybe it's just incremental improvements recursively, like matrix multiplication, and as you do more improvements, things slow down. The path to AGI is gradual.

**Demis:** If it's just incremental improvements, it would look gradual. The question is whether we can achieve further breakthroughs with these systems, or if we need completely new approaches.

**Lex:** What about the possibility of these systems providing both incremental and breakthrough improvements? S-curves—where you have incremental improvement within a curve, but then periodically a leap to a new curve.

**Demis:** No one's shown unequivocally that systems can deliver those big leaps. We have systems good at hill climbing on the current S-curve. The move 37 moment in AlphaGo—that would be the kind of leap we're talking about. Whether current systems can produce that at scale, we don't know.

**Lex:** Do you think scaling laws are holding strong—pre-training, post-training, test time compute?

**Demis:** There's a lot of room in scaling. Actually, three different scalings happen concurrently: pre-training, post-training, and inference time. How innovative you can be matters. We have the broadest, deepest research bench. Incredible researchers like Noam Shazeer, who came up with Transformers, Dave Silver, who led AlphaGo. That research base means if a new breakthrough is needed—like AlphaGo or Transformers was—I'd back us to be the place that does it.

When terrain gets harder, that's when it becomes more research than engineering. That's our sweet spot. It's harder to invent things than to fast follow. We're probably 50/50 on whether new things are needed or existing scaling is enough. We're pushing both—new blue sky ideas with about half our resources, scaling current capabilities maximally. We're seeing fantastic progress with each new version of Gemini.

**Lex:** So if progress toward AGI requires breakthroughs, not just engineering, you feel well-positioned at DeepMind and Google.

**Demis:** Looking at the last decade or 15 years, 80-90% of modern AI breakthroughs came from Google Brain, Google Research, and DeepMind originally. So yeah, I'd back that to continue.

**Lex:** Are you concerned about running out of high-quality data, especially high-quality human data?

**Demis:** Not very worried. There's enough data to get systems pretty good. And this goes back to simulations. If you have enough data to create simulations, you can create synthetic data from the right distribution. That's the key—you need enough real-world data to build data generators. We're at that step now.

**Lex:** You've done incredible work on the science and biology side with limited data relative to what you might expect.

**Demis:** Exactly. Limited in the sense that it's not billions of examples, but you can still achieve significant takeoff. We're doing that now.

**Lex:** How much compute do we need to get to AGI? What's your sense?

**Demis:** That depends on breakthrough definitions. If we just scale what we have, enormous compute. If we get clever about it, maybe not as much. Energy is becoming the constraint. It's not just about compute, but electricity to power it.

**Lex:** How much electricity are we talking? Is this sustainable?

**Demis:** We're talking terawatts potentially. There's a finite amount of power available on Earth. You could argue AI will spur energy innovation—better solar, better fusion. But there are physical limits. We'll hit constraints around electricity before compute.

**Lex:** What's your sense of human nature? This seems relevant to where we are right now.

**Demis:** That's a big question. I think humans are adaptable, curious, compassionate. We have infinite capacity for learning. We're tribal, competitive, but also capable of cooperation at scale. We have this unique ability to model other minds, to have theory of mind. I think that's been key to human success. We're capable of both tremendous compassion and terrible cruelty. We seem to be in the middle—not angels or demons.

**Lex:** Google and the race to AGI—what's your view on how Google should approach this?

**Demis:** DeepMind is part of Google, and I think Google is well-positioned. The company has massive resources, incredible talent, long-term thinking. But I think the race element itself might not be the best framing. This is arguably the most important thing humanity will do. Getting it right matters more than getting it first. I worry about the safety aspect. I wanted to build AGI to benefit humanity. If we're in a race dynamic where people cut corners on safety, that concerns me.

**Lex:** There's competition and talent acquisition. How do you think about that?

**Demis:** Competition drives innovation, and talent is key. But I worry when it becomes adversarial rather than collaborative. AI safety research especially needs collaboration. We shouldn't be racing to build unsafe systems faster. That's a bad outcome. I think the field is maturing on this. People recognize it's not about who gets there first, but about getting it right.

**Lex:** What does the future of programming look like?

**Demis:** I think programming will be increasingly collaborative between humans and AI. Humans will set high-level goals, reasoning about what matters. AI will handle implementation details. Gradually, AI might handle more of the architectural decisions too. But I don't think programming disappears. Humans will still need to think about big-picture design.

**Lex:** What about John von Neumann and his work interests you?

**Demis:** Von Neumann was a genius across so many domains—mathematics, physics, computation, game theory. He invented a lot of foundational concepts. He died young, but left this incredible legacy. His work on self-replicating machines is particularly relevant now. He was thinking about how systems organize themselves, how information propagates. These ideas feel relevant to understanding AGI development.

**Lex:** What's your current thinking on p(doom)—the probability of existential catastrophe from AI?

**Demis:** I worry about it, but I'm not in the extremely high doom camp. There are serious challenges to getting AGI right. The alignment problem is real. How do you align a superintelligent system with human values? That's genuinely hard. But I'm somewhat optimistic that we can figure it out. The field is taking it seriously. There are talented people thinking hard about it. I don't think doom is inevitable.

**Lex:** How do you think about humanity's future?

**Demis:** I'm fundamentally optimistic, maybe naively so. Humans are resilient, creative, capable of great cooperation. We have problems—climate change, inequality, conflict—but humans have overcome existential challenges before. I think the key is to maintain our humility. We don't have all the answers. We need to stay open to new ideas and perspectives.

**Lex:** The nature of consciousness and whether quantum computation plays a role there—where are you on that?

**Demis:** Consciousness is genuinely mysterious. I don't think consciousness requires quantum effects, but I can't rule it out. The hard problem of consciousness—why subjective experience feels like something—remains unsolved. I'm interested in it, but I don't think it's the key to AGI. I think you could have superintelligent systems that aren't conscious in any meaningful sense.

**Lex:** You quoted David Foster Wallace at one point. What draws you to his work?

**Demis:** His writing has tragic honesty. He's engaging in a constant battle with his own mind, and his work captures the front lines of that battle. He writes about attention and consciousness and what it means to be human. There's a particular quote: "The key to life is to be unborable." I love that. Every moment contains infinite richness if you look closely enough.

**Lex:** Tell me about your educational journey and how it shaped you.

**Demis:** I went to Drexel for my bachelor's, master's, and PhD in computer science and electrical engineering. I took difficult math and theoretical computer science courses that taught me how to think deeply and rigorously, how to work hard even when feeling too dumb to solve something. I programmed extensively—C, C++, robots, optimization algorithms, computer vision, wireless protocols, machine learning systems, physical simulations. That's where I developed a deep love for programming.

I also played guitar, wrote poetry, trained in judo and jiujitsu. Jiujitsu humbled me daily throughout my twenties and still does. My time at MIT has been crucial too. I've been a research scientist there for over 10 years in a paid position in LIDS—Laboratory for Information and Decision Systems. I'm constantly surrounded by people much smarter than me, which keeps me sharp. I've published peer-reviewed papers, though my focus shifted toward the podcast and AI/robotics projects outside MIT. I deeply value that academic rigor and exploration that comes from being embedded in that community.

**Lex:** What drives your curiosity and your sense of purpose?

**Demis:** I think it's the questions themselves. Why is the universe the way it is? How did life arise? What is intelligence? How can we use AI to unlock these mysteries? These are fundamentally interesting questions to me. And on a personal level, building things—systems that test out interesting ideas—that gives me joy. Publishing research, launching systems people use, that's what makes me feel alive.

**Lex:** Well, this is a huge honor, Demis. You're one of the truly special minds in the world. Thank you for doing what you do and for talking today.

**Demis:** Thank you very much, Lex.

---

*Note: All preview content, advertising, and promotional material has been removed from this transcript. The conversation begins at its natural starting point and flows to its conclusion. Section headers from the original timeline have been integrated into the dialogue for context.*

[^1]: **AlphaGo**: DeepMind system that defeated world champion Lee Sedol at Go in 2016, defeating a system previously thought decades away.

[^2]: **AlphaFold**: DeepMind system that solved the protein structure prediction problem, predicting 3D shapes of proteins from amino acid sequences with high accuracy. Demis Hassabis received the Nobel Prize in Chemistry in 2024 (awarded in 2025) for this work, alongside John Jumper and others.

[^3]: **AlphaFold 3**: Extension of AlphaFold to predict interactions between proteins and other molecules, expanding beyond single protein structure prediction.

[^4]: **AlphaGenome**: System for mapping genetic code to biological function.

[^5]: **Veo 3**: Google DeepMind's video generation model capable of creating photorealistic video from text descriptions, including sophisticated physics simulation, fluid dynamics, and lighting effects.

[^6]: **AlphaEvolve**: System for recursive code improvement, enabling AI to iteratively optimize existing code, particularly for tasks like faster matrix multiplication algorithms.

[^7]: **P vs NP**: Fundamental question in computer science about whether problems whose solutions can be verified quickly can also be solved quickly. Remains unsolved, one of the Millennium Prize Problems.

[^8]: **Neural networks**: Computational systems inspired by biological neurons, fundamental to modern AI systems like those discussed.

[^9]: **Transformers**: Neural network architecture introduced around 2017 (Vaswani et al.), underlying modern large language models including Claude, GPT, Gemini. Represents a major breakthrough in AI.

[^10]: **Gemini**: Google's family of large language models spanning different sizes and capabilities.

[^11]: **LIDS**: Laboratory for Information and Decision Systems at MIT, where Demis holds a research scientist position in the College of Computing.
