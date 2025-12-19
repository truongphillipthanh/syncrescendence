# Nvidia's Jensen Huang on AI & the Next Frontier of Growth

**Participants:** Konstantine Buhler (Sequoia Capital partner, AI investing focus) and Jensen Huang (Nvidia founder and CEO)

**Context:** This conversation took place at Citadel Securities' Future of Global Markets 2025 event at Casa Cipriani in New York City on October 6, 2025. Buhler and Huang explore Nvidia's evolution from graphics accelerators to AI infrastructure, the future of accelerated computing, and Huang's vision for agentic AI and physical AI.

---

**Konstantine Buhler:** Good morning, everyone. My name is Konstantine Buhler, and I'm a partner at Sequoia Capital, focused on AI investing. Both Nvidia and Citadel Securities actually have a lot in common—they're both exceptional businesses, really well-run, with brilliant leaders. They're exceptionally well-run. They were both powered by the computing revolution, and both are leaders in their respective industries with technology. They also have another, lesser-known fact. In both cases, their first outside investor was Sequoia Capital. We risked $1 million in Nvidia in 1993.

**Jensen Huang:** You were worth it. One solid million dollars.

**Konstantine:** Went way out on the limb. It was a little more into Citadel Securities. So when we were asked to speak about AI at this conference, it was incredibly clear who the best person in the world to speak would be—the man who has built the entire infrastructure for the AI revolution upon which all of this AI rests, and the man who built the most valuable company in the world. Please join me in welcoming Jensen Huang.

**Jensen:** Thanks. It's nice to wake up this way.

**Konstantine:** But you've been working for hours.

**Jensen:** Yes, I have.

**Konstantine:** So, Jensen, we have a room full of institutional investors who are some of the best in the world. They manage many trillions of AUM, and they are constantly looking for edge. You are someone who always has edge. Every one of our conversations, you have compelling insights about what the future is going to look like. In the next 60 minutes, we have an ambitious agenda to cover stories of the edge from the very beginning of Nvidia all the way through its rise through the center of the AI revolution, and then we'll spend the majority of the time on what's next for Nvidia and AI. So let's start at the very beginning. It's 1993. You're 30 years old. What's the insight that gave you the edge to start Nvidia?

**Jensen:** We were going through, basically, the PC revolution and the revolution of CPUs. It was the era of Moore's Law—the time when integrated microprocessors, Intel, Moore's law, the scaling laws of transistors. That was the buzz, and that was nearly all of the investment dollars in Silicon Valley and the computer industry. But we observed something a little different. We said, "There are many problems that—one of the benefits of CPUs is the general purpose. But the fundamental problem of general purpose technologies is that they tend not to be very good at very hard problems."

And so we conjectured two things. One, we observed that there are problems we could solve with an accelerator that is more domain-specific, more targeted. And those problems could be interesting to solve. And we observed that general-purpose technologies—the shrinking of these transistors—would eventually reach the limits. The idea that you could keep reducing the size of transistors and scaling it using this technique—it's a set of heuristics called Dennard scaling. Mead and Conway came up with what are really the fundamental principles behind Moore's Law. And if you go back to those, you'll discover that there will be a limit to how far you can shrink transistors. At some day, you'll get diminishing returns. And there are large computing problems. We believe that the computing problems we could solve are nearly infinite in scale. So one of these days, a new type of computing approach would emerge. We focused our company on augmenting, supplementing general-purpose computing with this technology called accelerated computing. That was really the observation.

**Konstantine:** You said something earlier about how Nvidia is always ahead of the curve. Oftentimes, if you reason about things from first principles—what's working today incredibly well—if you could reason about it from first principles and ask yourself, on what foundation is that first principle built on top, and how would that change over time? It allows you to see around corners. So when you built the graphics accelerator, you're early to the party, but then hundreds of other competitors sprung up. You eventually won in that market in the early 2000s. You said, "Hey, this technology might be able to generalize itself—perhaps the GPU could also be generalized for more processing." Let's talk about CUDA. How did that come about? Where did you get that insight? A story goes that it's from researchers. How did you read their work and conclude that the GPU could be a general computer?

**Jensen:** Well, first of all, the reason why Nvidia was hard to build was because we had to invent a new technology and invent a market. And at the time, in 1993, there weren't any graphics accelerators. And so, we had to convince the world that you needed one. It took years. We weren't profitable for a long time.

What saved Nvidia—and I've been very public about this—was the introduction of something called shader programming. Shader programming is the ability to write custom programs on the GPU, which essentially turned the GPU from a graphics engine into a computing engine. That was the key insight. Once shader programming came, suddenly you could write your own program. And these researchers noticed that the GPU could do what their CPUs couldn't do—basically, they could parallelize their problem across the GPU.

The moment we realized this, we invested heavily in CUDA, which was essentially a software platform to program the GPU. We created C for GPU, a way to program in C directly on the GPU. And what happened is, applications like image processing, AI, physics simulation, numerical computing—all sorts of applications started to show up. And the industry, suddenly, didn't see Nvidia as a graphics company anymore. They saw us as a computing company. That was the inflection point. CUDA was the unlock.

**Konstantine:** And CUDA became a moat—a really important moat—because developers trained on it, and then the lock-in effect became incredibly powerful. So when the AI revolution started, were you ready? Was Nvidia already positioned?

**Jensen:** The honest answer is yes, but we didn't know it would be AI. We were positioned for any massive parallel computing workload. What happened is that deep learning, which is a technique in AI, is extremely parallelizable. It's a perfect workload for GPUs. And it just so happened that when deep learning took off, the GPU was exactly what you needed. 

Hindsight is 20/20, but what I can tell you is we were focused on principles: First, parallelism is the future of computing. Second, if you can solve a hard problem, you'll find a market. We didn't know it would be AI, but we knew it would be something, because the computing problems of the world don't fit into general-purpose CPUs. And so, once deep learning took off, Nvidia was in the right place at the right time.

**Konstantine:** So let's jump into one of the most important concepts you talk about: the AI factory. What exactly is an AI factory, and why is it so important?

**Jensen:** An AI factory is the combination of three things: data, computing, and software. It's the fundamental unit of production for AI. The way I think about it is—in the old economy, you had factories that took raw materials and turned them into goods. In the AI economy, you have AI factories that take data and computing, and they produce AI—they produce inference and training.

The reason it's important is that it's a complete system. It's not just about having good chips. It's about having the right software, the right data infrastructure, the right networking, the right storage. And companies like ourselves, we're building this entire platform. We're building the chips, we're building the software frameworks, we're building the infrastructure tools.

The AI factory is essentially a production line. You put raw data in one end, and AI output comes out the other end. And the efficiency of that factory—the throughput per unit of energy, the cost per token generated—that's what determines the economics for data center operators and for enterprises building these systems.

**Konstantine:** And we're still incredibly early in this?

**Jensen:** We're extraordinarily early. The way I think about it is we're a few hundred billion dollars of AI infrastructure built. But the market opportunity is likely trillions of dollars per year, every single year. So if you just do the math, we're in the very, very early innings of this. And there's going to be wave after wave of new applications, new workloads, new use cases. We haven't even scratched the surface.

**Konstantine:** Let's talk about agentic AI. This is something you talk about with a lot of conviction. What is agentic AI, and why do you think it's going to be such a massive market?

**Jensen:** Agentic AI is an AI system that can take actions in the real world on your behalf. It can observe, it can reason, and it can act. It's not just a chatbot that responds to queries. It's an agent that operates autonomously, or semi-autonomously, to accomplish tasks.

The reason it's so important is that it expands the market for AI dramatically. Today, most AI is assistant-like—you ask it a question, it answers. But with agentic AI, you're essentially hiring a digital employee. Imagine if every company could hire thousands of digital employees to do work—that completely changes the economics of every single business. And the computing required for agentic AI is actually much greater than just inference or training on a model.

Think about it this way: if a human employee goes and thinks about a problem for eight hours, and then gives you an answer, that's a lot more computing than just answering a question in real time. Agentic AI requires the agent to think, to reason, to interact with different systems, to gather information, to make decisions. And all of that requires significant computing. So the market opportunity for agentic AI is truly enormous.

**Konstantine:** And in terms of physical AI—robots, autonomous systems—where are we in that arc?

**Jensen:** Physical AI is one of the most exciting frontiers because it's where AI meets the physical world. For robots to work effectively, they need to understand the world, they need to navigate, they need to manipulate objects, they need to understand physics. And the computational requirements for that are enormous.

The reason physical AI is going to be huge is the same reason the industrial revolution was huge. It's about automating labor. But unlike the industrial revolution, which automated physical labor, this is about automating intellectual and physical labor. Every single industry is going to be disrupted by this—manufacturing, logistics, healthcare, agriculture. Everywhere.

Now, the key to physical AI is something we call Omniverse. Omniverse is a digital twin simulation platform. It's a virtual world where you can train robots, where you can simulate how robots interact with the real world. Because unlike a chatbot, you can't just train a robot in the real world—you have to train it in simulation, and then transfer that learning to the real world.

That's why Omniverse is so critical. It's deeply undervalued right now. Most people don't realize they need it yet. But as more companies start building robots, they're going to discover that Omniverse is essential. We've been investing in this for almost a decade, and the robotics industry is now sweeping across and adopting it.

**Konstantine:** Let me shift gears to something you care deeply about: sovereign AI. This is a geopolitical and business concept that I think a lot of people don't fully understand yet. What do you mean by sovereign AI?

**Jensen:** Sovereign AI is the ability of a country, or a region, to develop and deploy AI independently, without being dependent on other countries for the technology or the infrastructure. It's about having the capability to build your own AI systems, to control your own data, and to ensure that your country's strategic interests are protected.

Now, this is becoming increasingly important geopolitically. Every country recognizes that AI is going to be central to economic and military power. And so countries want to have the ability to build their own AI, to be sovereign in their AI capabilities. That means they need to be able to build chips, they need to have the software platforms, they need to have the expertise.

What that means for the world is we're going to see a fragmentation in the AI ecosystem. You're going to have different regions building their own AI stacks. And companies like ours, we're going to have to be present in multiple regions, supporting different countries in building their sovereign AI infrastructure.

The thing I want to emphasize is that this isn't about isolating countries from each other. It's about ensuring that every region has the capability to participate in the AI revolution. Because if only a few countries can build AI, then the rest of the world becomes dependent on those countries. And that's not healthy for global economics or for global stability.

**Konstantine:** You've spent your entire career kind of thinking at the intersection of hardware and software. What's the future of that relationship? How do you see that evolving?

**Jensen:** Hardware and software have to co-design. It's not enough to build great hardware and hope developers use it. You have to build great software that takes advantage of the hardware. And the hardware has to be designed with the software in mind. It's this dance that happens.

What we're seeing now is that the economics of computing are changing. In the past, you could just buy a general-purpose CPU and run anything on it, and it would be fine. But with AI, energy is now the main cost. Energy is the constraint. So we have to design every single layer—from the chip architecture to the software frameworks to the applications—to be energy efficient.

That means the specialization of computing is going to increase. You're going to see more and more specialized chips for specific workloads. You're going to see software frameworks that are highly optimized for those chips. And that's where the value is going to be captured.

Our strategy at Nvidia is to build the platform for accelerated computing. It's not just chips. It's chips plus software plus systems plus platforms. And we're going to keep investing in all of those layers to make sure that the AI factory is as efficient as possible.

**Konstantine:** You mentioned earlier that computation in the future is going to be generative. What do you mean by that?

**Jensen:** The way of computation in the future will likely be generative. Let me give you a concrete example. A hundred percent of what you and I just went through is generated. Every question you asked me, I didn't run back to my office and retrieve something and bring it to you. That's yesterday's computer.

Today's computer is—we're just interacting. And we're generating everything in real time based on the context that's happening right here, based on the audience, based on what's happening around the world. And so we're generating everything in real time. That's the future computer. Your future computer is a CEO in front of you, or it's an artist, a poet, a storyteller. And you collaborate with it to create unique content for yourself.

So the future of computation is 100% generative. And behind it, you need an AI factory, which is the reason why I'm 100% certain we're at the beginning of this journey. We're only a few hundred billion dollars of infrastructure built for what likely will be trillions of dollars of infrastructure built each year. And that computing paradigm is so much more like the human mind. It's thinking.

**Konstantine:** If you're up for it, how about we generate a few lightning-round answers?

**Jensen:** OK.

**Konstantine:** Just in the last few minutes together. What's one KPI that Wall Street underweights?

**Jensen:** In the future of AI factories, your throughput-per-unit energy governs the revenues of your customers. It's not just about selecting a better chip. It's about deciding what your revenues are going to be. If you go back and look at all the CSPs [cloud service providers], the ones that chose right saw revenue growth. And the ones that chose right subsequently—the throughput, the token generation rate per unit energy of your factory is your revenues.

**Konstantine:** The most underrated piece of Nvidia's platform?

**Jensen:** Most people talk about CUDA, and CUDA is very important. But there's a suite of libraries that sit on top of CUDA. I mentioned one earlier today called cuDNN, and it is probably one of the most important libraries ever created in the history of humanity. The previous most important one was SQL. And this one, cuDNN. There's a few others—cuDA, cuLitho, which is going to be used for semiconductor manufacturing and lithography. We have about 350 of these libraries, and these libraries are Nvidia's treasure trove.

**Konstantine:** What's one technology that you think is wildly undervalued and one that you think might be overvalued?

**Jensen:** Undervalued. The virtual world for physical AI—to learn to be a good physical AI, we call it Omniverse. It's hard to understand, but it is deeply undervalued. Not because people use it and don't know, they just don't know they need it yet. But now Omniverse is sweeping across the robotics industry, and everybody gets it. Once you start building robots, you realize how visionary it was that we started working on Omniverse almost a decade ago. Omniverse is really important.

**Konstantine:** What's the book that most shaped your business and leadership philosophy?

**Jensen:** One of my favorite books was everybody's first calculus book. That's when you realize that math was in motion. All of Clayton Christensen's books—he's passed, but he was a good friend, and all of his books were great. Al Ries' "Positioning" book, really good. Of course, "Sapiens" is always good. Jeffrey Moore's "Crossing the Chasm"—that's a good book. But all of Christensen's books. Read them all.

**Konstantine:** Favorite comfort food?

**Jensen:** Fried chicken.

**Konstantine:** There we go. OK, we got it in. Alright. Last question: If you were a CIO in the audience with $10 billion to allocate toward AI in the coming years, what would you invest it into?

**Jensen:** I would, right away, experiment with building your own AI. The fact of the matter is we take pride in onboarding employees—the method by which you do so, the culture by which you bring them in, the philosophies of your company, the operating methods, the practices that make your company what it is. The collection of data and knowledge that you've embodied over time that you make accessible to them—that is what defines a company in the past.

A company of the future includes that, of course, but you need to do that for AI. You need to onboard digital employees. You need to onboard AI employees. There's methodology for onboarding AI employees—we call them "fine-tuning," but basically teaching them the culture, the knowledge, the skills, the evaluation methods. The entire flywheel of your agentic employee is something you need to learn how to do.

I tell our CIO and IT department—they're going to be the HR department of agentic AI in the future. They're going to be the HR department of digital employees. And those digital employees are going to work with our biological ones. And that's going to be the shape of our company in the future. So if you get a chance to do that, I would do it right away.

**Konstantine:** Well, we heard an incredible story. Really, the story of Nvidia is one of exceptional generalization—from an accelerated graphics processor to the technology that powers all of AI in the world today. From a component—the world's first GPU—to all of the components in a platform, in the world's AI factory. We talked about how services are the baseline for this new revolution and how robotics are in all of our future. We covered foreign policy. We even touched on fried chicken. You did it all, Jensen. Thank you so much.

**Jensen:** Thank you.