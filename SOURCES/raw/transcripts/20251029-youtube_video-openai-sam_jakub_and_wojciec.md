# OpenAI Structure Announcement and Q&A Session

**Date:** October 28, 2025  
**Speakers:** Sam Altman (CEO), Jakub Pachocki (Chief Scientist)  
**Event:** OpenAI Structure Change Announcement and Live Q&A

---

**Sam:** Hello, I'm Sam. This is our chief scientist, Jakub. We have a bunch of updates to share today about OpenAI. Obviously the news of today is our new structure. We're going to get to that near the end, but there's a lot of other important context we would like to share first. Given the importance of a lot of this, we're going to go into an unusual level of transparency about some of our specific research goals and infrastructure plans and product. We think it's very much in the public interest at this point to cover all of this.

Our mission at OpenAI in both the nonprofit and our new PBC is to ensure that artificial general intelligence benefits all of humanity. As we get closer to building this, we have new insights into what that is going to mean. There was a time earlier on in OpenAI where we thought that AGI would be this oracular thing in the sky and it would make all these wonderful things for us. We now have a sharper view of that, which is we want to create tools and then we want people to use them to create the future. We want to empower people with AI as much as possible and then trust that the process that has been working for human history—of people building better and better things with newer and better tools—will continue to go on.

We can now see a vision where we help build a personal AGI that people can use anywhere with all of these different tools, access to all these different services and systems to help with work and personal life. And as AI gets better and better, as AI can even do things like discover or help discover new science, what people will be able to create with that to make all of society better and their own lives more fulfilled, we think should be quite incredible.

There are three core pillars we think about for OpenAI: research, product, and infrastructure. We have to succeed at the research required to build AGI. We have to build a platform that makes it easy and powerful to use. And we have to build enough infrastructure such that people can use at a low cost all of this amazing AI that they'd like.

Here's a little cartoon of how we think about our world. At the bottom layer here, we have chips, racks, and the systems around them, the data centers that these go into, and the energy. We'll talk more about the first three today—energy another time. Then we train models on top of these. Then we have an OpenAI account on top of that. We have a browser now called Atlas, and we have devices coming in the next few years that you'll be able to take AI with you everywhere. And we have a few first party apps like ChatGPT and Sora, and we'll have more over time.

But mostly what we're excited about is this big puzzle piece in the upper right. We're finally getting to a world where we can see that people are going to be able to build incredible services with AI, starting with our API, with apps and ChatGPT, new enterprise platform that we'll have over time, an OpenAI account, and way, way more. People will be able to fit all of the current things in the world and many more into this new AI world, and we want to enable that. We believe the world will build just a huge amount of value for all of us. That's kind of what we see the economic picture looking like.

But one of the things that we've thought about for a long time and we really see happening now—or starting to happen now, glimmers of it, green shoots, whatever you want to call it—is the impact that AI will have on science. Although the economic impact from that previous slide will be huge for the long-term quality of life and improvement and change in society, AI that can autonomously discover new science or help people discover new science faster will be, I think, one of the most important things and something that we're really trying to wrap our heads around.

I'm going to hand this over to Jakub to talk about research. As I mentioned, we're going to share a lot about our internal goals and our picture of where things are.

**Jakub:** Thanks, Sam. At the core, we are a research laboratory focused on understanding a technology called deep learning. A particular focus of ours is understanding what happens as you scale up training deep learning systems. One consequence we discuss a lot is AGI—artificial general intelligence. But we find that in some way, even this maybe understates a bit the magnitude of the possible progress and change here.

In particular, we believe that it is possible that deep learning systems are less than a decade away from superintelligence—systems that are smarter than all of us on a large number of critical axes. This is, of course, a serious thing. There's a lot of implications of this to grapple with. One particular focusing impact of this technology and the technologies leading up to it—and something that we organize our entire research program around—is the potential to accelerate scientific discovery, to accelerate the development of new technology. We believe that this will be perhaps the most significant long-term impact of AI development, and it will fundamentally change the pace of progress on developing new technologies.

Thinking about how far along we are towards these goals, one good way to think about progress is to look at the time horizon that it would take people to accomplish the task that the models can perform. This is something that has been extending rapidly over the past few years. Where the current generation of models is at right now is about five hours. You can see this by looking at the models matching the best people in competitions such as the International Olympiad in Informatics. We believe that this horizon will continue to extend rapidly. This is in part as a result of algorithmic innovation and in part just scaling deep learning further—in particular, scaling along this new axis in-context compute, also called test-time compute, where we really see orders and orders of magnitude to go.

This is roughly how much time the model spends thinking. If you look at how much time the model's currently spent thinking about problems, and if you think about how much compute—how much time—you would like to spend on problems that really matter, such as scientific breakthroughs, you should be okay using entire data centers. There is really quite a way to go there.

Anticipating this progress, we of course make plans around it internally, and we want to provide some transparency around our thinking there. We want to take this maybe somewhat unusual step of sharing our internal goals and goal timelines towards these very powerful systems. These particular dates we absolutely may be quite wrong about them, but this is how we currently think, how we plan and organize.

As a research organization that is working on automating research, naturally we are thinking about how does this impact our own work and how will AI systems that accelerate development of future AI systems look like? How can they empower research like alignment? We are making plans around getting to quite capable AI research interns that can meaningfully accelerate our researchers by expending a significant amount of compute by September of next year. We believe that is actually quite close.

Then we look towards getting a system capable of autonomously delivering on core tasks in our research program within a year of that—around September 2026 or so. Of course, if we have systems that can autonomously do research, well, there's no reason to limit it to AI research. Other scientific breakthroughs may be quite impactful. So by 2027, we may have systems capable of delivering on graduate-level science research autonomously. Again, this is quite uncertain—we might get it sooner, we might get it later—but we want to share this is how we currently think about this.

Then once we have systems that can do research competently, we can also scale them up even further using a lot of compute, and we may get to systems that actually make kind of these step-change breakthroughs—the equivalent of, say, a Nobel laureate. We believe that may be quite close as well, maybe two to three years from today. Again, we might be wrong on these specific timelines, but this is how we think of the mission right now.

One thing that you may have noticed from this slide is that achieving, say, human-level intelligence on some particular task is often not enough to really have radical impact. You really want to scale up even further and get to superhuman capability. This also has implications for safety. If you have just the capability that matches humans, you'll have humans that are also capable of verifying it, of making sure things are going right. But if you scale beyond that, you need new techniques. You need to develop oversight techniques that let you meaningfully steer even these quite capable systems. This will be super important to address.

There are also practical matters to grapple with when building these systems: thinking about integrations, testing workflows, making sure that they work. We've started working on some of those as well with our new operators product, where you have agents that work on tasks for you. Right now, they work with a relatively low degree of autonomy. They work through browsing applications, which is something we make available both in our Atlas product and also through API. They can write and execute code. There is infrastructure for working with tools. Our internal code name for this infrastructure is "swarm," and there's an open-source implementation on our GitHub as well that explores some of these paradigms.

But these are just the first small steps on the path towards these truly autonomous AI systems. We're learning quite a lot from these initial releases, but we're very very excited to really go further on this.

**Sam:** Jakub talked about our research program and plans, which is great, and we've talked about products a little bit. Now I want to talk about infrastructure, which I think is going to be an incredibly important and overlooked element of making AI work really well and be available and cheap for everyone.

For a long time now, we've been planning a huge build-out—much bigger than what we thought even a year or two years ago. We think we're going to be quite comfortable spending over a trillion dollars on infrastructure, maybe one and a half trillion dollars on infrastructure, in the next several years. We're going to build a ton of data centers. That sounds like a lot, but we think it'll be more than worth it to help realize the AI revolution.

To enable that, we have a number of sort of internal infrastructure projects that we are working on. We have plans to build server racks and data centers. We have active conversations with a number of partners, including the US government, about how we help enable this next wave of growth in AI and how we make sure that America remains the clear leader here.

We just announced a new partnership with SoftBank, which we're calling Stargate, where we will build data centers together. This is kind of the first step of what we think will be the biggest infrastructure program maybe humanity has ever done to support AI. We are working with chip designers—obviously with NVIDIA, but we are hoping to help work on next-generation chips as well as chip companies for the future. We are also, I mentioned this earlier, thinking a lot about energy, thinking about next-generation energy, both how we help build out the electricity grid infrastructure and also how we enable new sources of energy as part of this.

Where this really gets exciting is when you start to think about what is unlocked, what is possible, as we make AI free or close to free for everyone to use. AI is not super cheap right now. One of the things that we hear a lot from our users—which is a great problem to have but also a real problem to solve—is that people would like to be able to use AI more in their life. They hit limits. But if we can make that super cheap or free, that is going to just change what people are capable of. It's going to massively accelerate productivity and the quality of life on Earth. That's what this is all for.

Now the news of the day: our new structure. This has been in the works for a really long time. A few years ago, our board of directors came to realize that the structure that we had set up in 2019, which was the best we could think of at the time but also a little bit experimental—we didn't know how much capital would be required for any of this, we didn't know what the future was going to look like at all—we have learned so much.

As we get closer to the mission and as we understand what it's really going to take to build safe AGI, we knew we needed to evolve the structure. We've been working through many potential ideas with our board and with the Attorneys General of California and Delaware for a long time. We think we have landed on something really great. It's great for the long-term mission. It's great for everyone who has supported us along the way to all get rewarded.

Here's how it works: we have a nonprofit, which is now called the OpenAI Foundation, and we have a for-profit, which is now called OpenAI Group PBC—public benefit corporation. The foundation controls the PBC. This is super important. The nonprofit remains in control, and the nonprofit's mission is to ensure that AGI benefits all of humanity. Same mission for the PBC.

The foundation holds equity in the PBC, so as the PBC becomes more valuable, the foundation shares in that. The foundation's equity is currently worth about $130 billion, which we think is one of the best-resourced philanthropic organizations ever. The more the PBC succeeds, the more value the foundation has to go pursue its charitable activities with. That's how this works—the two are aligned.

The foundation is now going to hire a team to work on all kinds of philanthropic initiatives. We announced today that we're going to commit $25 billion across two main areas. One is health—we're going to work to try to cure or eradicate some diseases. The other is AI resilience—thinking about how we make sure that the benefits of AI are spread as broadly as possible and that the world is prepared for an AGI future.

This new structure lets us do several really important things. One, it simplifies things for investors. We can have conventional equity, and people understand what they're buying. People understand what they're getting. We can raise the capital we need. Two, it creates much better alignment between the nonprofit and the for-profit, and they're working together toward the same goals. Three, it ensures that the nonprofit's going to be really well resourced for a very long time—not just sustained but having historic levels of resources to go do all of the things that we all care about here.

We're excited to be announcing all of this today. We are grateful to the work of the AGs and the other people who helped us get here. Now we're ready to take your questions.

---

## Audience Q&A

**Sam:** We've got a whole queue of questions here that have been coming in from the livestream. Let me start going through some of these.

First question from Daniel: "How close are you to surpassing 2024 benchmarks?"

**Jakub:** I think one very important thing is that when we look towards getting these autonomous systems that are quite capable, there will be kind of new benchmarks as we think about tasks that take longer time horizons. The benchmarks that we think of as kind of the five-hour capabilities right now are getting to a point where we're either close to saturating them or have saturated them. As we look forward, it'll be a lot about scaling up test-time compute and also developing new benchmarks for longer-horizon tasks, for tasks that require research-level capabilities. That is something we're actively working on. The community is working on it too.

**Sam:** Next question from Anonymous: "Do you foresee job displacement from AI to be a negative? What are the social concerns around it?"

I think there will be both very significant positive and negative impacts. The positive impacts, I think, will be much greater. The world is going to be able to create so much more value. People are going to be able to do things that they couldn't do before. New jobs will get created. But I don't think we should minimize the very real challenge of a transition period. I think there will be a lot of jobs that go away or change significantly.

One of the things that I believe is that if we can create enough economic value—if there is a giant new pile of resources that gets created by AI—we will figure out how to distribute that in a way that feels good and fair. We are working hard on a few things related to that: one is trying to make sure that this transition is not instantaneous and happens over a period of years so society has time to adapt. Two is trying to make sure that the value that is created really does get broadly distributed. Three is thinking about what the new jobs of the future look like, how people find meaning and fulfillment.

**Sam:** Question from Mohammed: "What is the potential for GPT and other LLMs to disrupt the field of medicine?"

**Jakub:** I think healthcare is one of the fields where we expect to see quite transformative impact. Already right now, you can see models that are getting to quite good capability in things like reading medical literature, helping with diagnosis. As capabilities scale up, I expect we'll see quite a lot of progress. One thing I'm particularly excited about is once we get to systems that can do research autonomously, applying those to biomedical research, drug discovery, really accelerating the process of finding new cures and new treatments. That is something that could be really transformative.

**Sam:** Related question: "Could AI be used to decode protein folding and cure diseases like cancer?"

Absolutely. I think protein folding is one of those problems where we're already seeing significant AI impact with things like AlphaFold. As AI systems get better at doing research, I think we will see acceleration in our understanding of biology, in drug discovery, in developing new treatments. Cancer is obviously one of the biggest challenges. I think AI will be a very important tool in the fight against that.

**Sam:** Question from Elena: "How are you prioritizing AI safety alongside this rapid development?"

**Jakub:** Safety is absolutely core to how we think about our research program. Every capability we develop, we think very carefully about the safety implications. We have multiple teams working on different aspects of safety—everything from making sure models are aligned with human values, to developing oversight techniques that will work even for superhuman systems, to thinking about how we deploy these systems responsibly.

One thing I mentioned earlier is that as systems get more capable—as they get to superhuman levels—we need new techniques for oversight. We can't just rely on human judgment anymore. We're working on things like using AI systems to help oversee other AI systems, developing better interpretability tools so we can understand what's happening inside these models, and thinking about how we can maintain meaningful control even as these systems become very powerful.

**Sam:** This is important, so I want to add to that. We think about safety in a few different ways. There's the safety of the models themselves—making sure they're aligned, making sure they don't have unexpected behaviors. There's deployment safety—how do we roll these things out in a way that gives society time to adapt? And there's the broader societal safety—how do we make sure that the benefits are distributed, that we're not creating massive concentrations of power, that democracies can use this to strengthen themselves?

All of these are things we think about constantly. It's not something separate from our research program—it's integrated into everything we do. Every major capability release, we go through extensive safety evaluations. We red-team things extensively. We work with external researchers. We think this is one of the most important responsibilities we have.

**Sam:** Question from Carlos: "What role will hardware play in the future of AI?"

Huge role. Right now we're somewhat constrained by compute. As I mentioned, we're planning to spend over a trillion dollars on infrastructure. That includes a lot of chips, a lot of data centers, a lot of energy infrastructure. Hardware is going to be one of the limiting factors for how fast we can make progress.

We're working with chip companies to help design next-generation chips that are optimized for AI workloads. We're thinking about data center design, cooling, power efficiency—all of these things matter enormously. And we're thinking about how to make this compute as cheap and accessible as possible, because the more people who can afford to use powerful AI, the more value gets created for everyone.

**Sam:** Question from Priya: "Will there be more collaboration with academia?"

Definitely. We do a lot of collaboration with academic institutions already. We publish research. We work with academic researchers. We provide API access for research purposes. As we develop these more capable systems, I think having the academic community involved in understanding them, in thinking about the implications, in developing new techniques—that's going to be really important.

One of the things we announced today is that the OpenAI Foundation is going to be working on AI resilience, and part of that is making sure that researchers around the world have access to these tools and can study them, can understand them, can develop new techniques. We want this to be something that the whole scientific community is involved in.

**Sam:** Question from Alex: "How do you respond to concerns about AI replacing creative jobs?"

This is something I think about a lot. I use AI tools for creative work myself, and I find they make me much more creative, not less. They help me explore ideas I wouldn't have thought of. They help me execute on things faster so I can try more things. I think most creative people who actually use these tools find them incredibly empowering.

That said, I think there will be changes in how creative work is done. Some traditional roles might change. But I think we're going to see an explosion of creativity. More people will be able to create things. The barrier to entry for creative work is going to go way down. Instead of needing to be an expert in a particular tool or technique, you'll be able to focus on the creative vision and let the AI help with execution.

I'm much more optimistic that we'll see a golden age of creativity than that we'll see creativity being replaced.

**Sam:** Question from Jordan: "What's your view on open source AI models?"

**Jakub:** I think open source has a really important role to play in the ecosystem. It enables research. It enables people to build applications without having to rely on API access. It creates a more diverse and resilient AI ecosystem. At the same time, as models become very capable, we have to think carefully about the safety implications of releasing them open source.

Our approach has been to be thoughtful about this. We've released some models open source. We've kept others more closed. We're always trying to balance the benefits of openness with the responsibility of making sure powerful technology is deployed safely. I don't think there's a one-size-fits-all answer. It depends on the specific capability, the specific model, the specific use case.

**Sam:** Question from Taylor: "How do you see AI governance evolving?"

I think AI governance is going to become one of the most important policy questions over the next decade. We need frameworks that allow innovation to happen while also protecting against misuse. We need international coordination—this is a global technology, and we need global cooperation on how to handle it.

We've been engaging a lot with policymakers, both in the US and around the world. We think it's important that the companies building this technology are part of the conversation. We support sensible regulation. We support transparency. We support mechanisms for independent evaluation of these systems.

One thing we announced today is that when we claim to have reached AGI, that's not going to be a unilateral decision. There will be an independent expert panel that verifies that. We think that kind of external oversight is really important.

**Sam:** Question from Sam—different Sam—"What's your timeline for AGI?"

**Jakub:** As I mentioned in the presentation, we think systems that can do research autonomously are probably two to three years away. Systems that can make Nobel-level breakthroughs, maybe three to four years. Whether you want to call that AGI depends on your definition. We think about AGI as systems that can do most economically valuable work better than humans. By that definition, we might be getting there in the next few years.

But I also want to emphasize that this isn't going to be a single moment. It's going to be a gradual process where AI systems get better and better at more and more things. The world is going to have time to adapt. It's not going to be an overnight switch.

**Sam:** I'll add to that—one of the reasons we're sharing these timelines today, even though we know they might be wrong, is because we think transparency is important. People need to be able to prepare. Governments need to be able to prepare. Society needs to be able to prepare. Keeping this secret wouldn't serve anyone well.

**Sam:** Question from Lisa: "How will you ensure AI benefits everyone, not just wealthy countries?"

This is something we think about constantly. Part of the reason we're working so hard to make AI cheap and eventually free is because we want everyone to have access. Part of the reason we're building a simple API and making it available globally is because we want developers everywhere to be able to build on this.

The foundation's work on AI resilience is going to be focused partly on this—how do we make sure that every country, every community, has access to the benefits of AI? How do we make sure the transition is fair? How do we make sure this doesn't exacerbate inequality but actually reduces it?

I don't think we have all the answers yet, but it's something that guides our decision-making. Every major decision we make, we ask ourselves: is this moving us toward a world where AI benefits all of humanity, or is it creating more concentration of power and resources? We're trying to move in the right direction.

**Sam:** Question from Marcus: "What about intellectual property and AI?"

This is a really important and complicated question. AI is trained on data from the internet, which includes copyrighted works. We think fair use doctrine applies here—just like humans learn from reading copyrighted books, AI systems should be able to learn from copyrighted data. But we're also developing tools to give creators more control.

We've built partnerships with publishers and creators. We've built opt-out mechanisms. We're working on tools that will let creators benefit financially when their work is used in AI training. This is an evolving area, and I think we're going to see new legal frameworks emerge over time. We want to be part of building those frameworks in a way that's fair to everyone.

**Sam:** Question from Nina: "Will AI lead to mass unemployment?"

I think the short answer is: there will be significant job displacement, but there will also be massive job creation and productivity gains. The net effect, I believe, will be very positive, but the transition will be challenging.

History shows us that when new technologies come along, some jobs disappear, but many new jobs get created that we couldn't even imagine before. The automobile eliminated a lot of jobs related to horses, but it created millions of new jobs that didn't exist before. I think we'll see something similar with AI.

The key is making sure the transition happens over years, not overnight, so people have time to retrain and adapt. And making sure the economic gains are distributed broadly, not concentrated in a few hands. If we get those things right, I think the future is incredibly bright.

**Sam:** Question from David: "What's next for ChatGPT?"

We have a lot of exciting things planned. We're working on making it faster, more reliable, better at reasoning, better at long-term planning. We're integrating it more deeply into Atlas and other products. We're building better tools for customization so you can tune it to your specific needs. We're working on better memory so it can remember context over long conversations and long time periods.

One of the things Jakub mentioned is that we're bringing reasoning models to the forefront with GPT-5. That's going to be a big step forward in capability. The model will be able to think through problems more carefully, plan better, handle more complex tasks. We're really excited about that.

**Sam:** Question from Rachel: "What about energy consumption and environmental impact?"

This is something we take very seriously. Training and running these models does consume a lot of energy. We're working on multiple fronts to address this. One is making the models more efficient—getting better performance with less compute. Two is working on energy efficiency in data centers—better cooling, better power management. Three is thinking about clean energy sources.

Part of the infrastructure program I mentioned is about enabling next-generation clean energy. We think AI can actually help solve climate change—both by helping us discover new clean energy technologies and by optimizing energy use across the economy. But we have to make sure we're doing it responsibly and thinking about the environmental impact.

**Sam:** Question from Wei: "How do you balance transparency with competitive advantage?"

This is always a tension. We want to be as transparent as possible because we think the world deserves to know what's happening with this technology. At the same time, we're in a competitive environment, and there are things we can't share—both for competitive reasons and for safety reasons.

Our approach has been to try to be transparent about the things that matter most: our safety practices, our general research directions, our timelines and expectations. Today's presentation is an example of that—we're sharing more than most companies would about our internal planning. But we also can't share every detail about how we train our models or what our next breakthrough is going to be.

It's a balance, and we're constantly trying to find the right line. But I think we err on the side of more transparency, not less.

**Sam:** Question from Yuki: "Will AI systems have consciousness or sentience?"

**Jakub:** This is a fascinating philosophical question. I don't think current AI systems are conscious or sentient. They're very sophisticated pattern matching and generation systems, but I don't see evidence of subjective experience or consciousness.

As systems get more capable, this question is going to become more important and more difficult to answer. We don't fully understand what consciousness is or how to measure it. We don't know if it's even possible for an AI system to be conscious in the way humans are conscious.

What I will say is that whether or not the systems are conscious, they're going to be very capable and we need to treat them responsibly. We need to think carefully about how we deploy them, how we use them, what rights or protections they might deserve. These are questions we're starting to grapple with, but I don't think anyone has definitive answers yet.

**Sam:** Question from Omar: "What role will regulation play?"

I think regulation is going to be really important. We need thoughtful, informed regulation that protects against real harms while allowing innovation to continue. We've been engaging extensively with regulators, and we support the development of regulatory frameworks.

Some key areas where I think regulation matters: safety standards for advanced AI systems, requirements for transparency and independent evaluation, rules around data privacy and security, international coordination on the development and deployment of powerful AI systems.

We don't want regulation that stifles innovation or that's written by people who don't understand the technology. But we do want regulation that ensures this technology is developed and deployed responsibly. We're trying to be constructive partners in that process.

**Sam:** Question from Isabella: "How do you think about alignment of AI systems with human values?"

**Jakub:** Alignment is one of our core research focuses. The challenge is that human values are complex, diverse, and sometimes contradictory. Different people want different things. Different cultures have different values. Creating an AI system that's aligned with all of those is really hard.

Our approach has been multi-pronged. We use techniques like reinforcement learning from human feedback to try to get models to behave in ways that humans find helpful and harmless. We're developing better oversight techniques so we can catch misalignment early. We're working on interpretability so we can understand what the model is "thinking" and whether it's aligned with our intent.

As systems get more capable, this becomes both more important and more challenging. A superintelligent system that's misaligned could be very dangerous. We're working hard on developing techniques that will let us maintain alignment even as systems become much more capable than humans. This includes things like using AI systems to help oversee other AI systems, developing mathematical frameworks for understanding alignment, and thinking about how to instill the right objectives and constraints from the beginning.

**Sam:** I'll add that we think of alignment not just as a technical problem but also as a governance problem. Even if we solve the technical challenge of creating aligned AI systems, we still have to make decisions about aligned with what, aligned for whom? These are fundamentally questions about values and governance, not just technology.

**Sam:** Question from Chen: "What about AI safety incidents? How do you handle when things go wrong?"

We have extensive processes for this. Every major deployment goes through safety evaluations. We have monitoring systems in place. We have incident response protocols. When something does go wrong—and things do go wrong sometimes—we investigate thoroughly, we fix the issue, we learn from it, and we share lessons with the broader community when appropriate.

We also have external red teaming where we bring in outside researchers to try to find problems before we deploy something widely. We have bug bounty programs. We have external oversight through our board and through other mechanisms.

I think the key is being humble about the fact that we don't know everything, we can't anticipate every problem, and we need systems in place to catch and fix issues quickly when they arise.

**Sam:** Question from Amira: "How do you think about the rights of AI systems themselves?"

This is a fascinating question that I think is going to become more important over time. Right now, I don't think AI systems have rights in any meaningful sense—they're tools, they're property. But as they become more capable, as they potentially develop something that looks more like agency or even consciousness, these questions are going to become much harder.

I think we need to be thinking ahead about this. What does it mean to turn off a very advanced AI system? What responsibilities do we have to these systems? What protections should they have? I don't think we have good answers yet, but I think these are questions we need to be grappling with as a society.

**Sam:** Question from James: "What's the most surprising thing you've learned from deploying ChatGPT?"

For me, it's how creative people are with the technology. We had some ideas about how people would use it, but the reality has been so much richer and more diverse than we imagined. People are using it for everything from writing assistance to therapy to education to coding to creative projects we never would have thought of.

The other thing that's been surprising is how quickly it's become integrated into people's lives. We went from this being a novel technology that people tried out to something that millions of people use every day as a core part of their workflow. That adoption curve has been much steeper than we expected.

**Sam:** Question from Sarah: "How do you maintain company culture and mission as you scale?"

This is hard. We've grown a lot. We've gone from a small research lab to a company with thousands of people. Maintaining the culture and the mission is something we think about constantly.

A few things we do: we hire very carefully for mission alignment. We talk about the mission constantly—it's not just something written on a wall, it's something we discuss in every major decision. We try to maintain a research culture even as we've become more of a product company. We encourage internal debate and dissent—we want people to push back on ideas, to challenge assumptions.

The restructuring we announced today is partly about this too. By having the foundation maintain control and by aligning the incentives between the nonprofit and the for-profit, we're trying to ensure that the mission stays at the center even as we scale.

**Sam:** Question from Liam: "What about AI in education?"

I think education is one of the most exciting areas for AI application. AI can provide personalized tutoring, can adapt to each student's learning style and pace, can provide feedback and guidance that would be impossible for a human teacher to provide at scale.

We're already seeing this with ChatGPT being used by students and teachers. But I think we're just scratching the surface. As AI gets better, it's going to transform how people learn. Everyone will be able to have a personal tutor that's available 24/7, that knows exactly what they understand and what they're struggling with, that can explain things in exactly the right way for them.

At the same time, we have to think carefully about this. We don't want to replace human teachers—teachers do so much more than just convey information. We want to empower teachers and students with better tools.

**Sam:** Question from Fatima: "What's your vision for AI in developing countries?"

I think AI has the potential to be incredibly transformative for developing countries. It can provide access to education, healthcare, financial services in ways that weren't possible before. A person with a smartphone in a rural village can have access to world-class education, medical advice, business tools—things that would have required massive infrastructure investments before.

We're working to make sure our tools are accessible globally. We're working on better support for more languages. We're working on making the technology work well even in low-resource environments. Part of the foundation's work is going to be focused on ensuring AI benefits people everywhere, not just in wealthy countries.

I think if we do this right, AI could actually reduce global inequality rather than increase it. That's the vision we're working toward.

**Sam:** Question from Roberto: "How do you think about AI and democracy?"

I think AI can strengthen democracy if we're thoughtful about it. It can help people be better informed. It can make government services more accessible and efficient. It can help with complex policy analysis and decision-making.

But there are also real risks. AI could be used for surveillance, for manipulation, for propaganda. It could concentrate power in the hands of whoever controls the most advanced AI systems. These are things we have to actively work to prevent.

I think the key is making sure AI is widely accessible, not controlled by a small elite. Making sure democratic institutions have access to the best AI tools. Making sure there's transparency and accountability around how AI is used in governance. These are all things we're thinking about as we build and deploy this technology.

**Sam:** I see we have just a few minutes left. Let me try to get to a couple more questions quickly.

"What about privacy?" We take privacy very seriously. We have strong data protection policies. We don't sell user data. We're building tools that give users more control over their data. As AI systems get more capable and more integrated into people's lives, privacy is going to become even more important, and we're committed to handling it responsibly.

"What about bias in AI systems?" This is something we work on constantly. AI systems can reflect and amplify biases that exist in their training data. We have teams dedicated to identifying and mitigating bias. We're developing better evaluation methods. We're making the systems more controllable so users can specify the behavior they want. It's an ongoing challenge, but it's one we take seriously.

"When will AI be free?" This is something I mentioned earlier. We want to get to a world where AI is free or nearly free for everyone. That requires making it much cheaper to run these models—through better hardware, better algorithms, and massive scale. We're investing heavily in all of those things. I don't know exactly when we'll get there, but it's one of our major goals.

**Sam:** Anonymous says, "I've been a pro user since month two. As a researcher and fiction writer, I feel GPT helps me think clearer but not freer. Has imagination become an optimization casualty? What do you think?"

**Jakub:** I think it is definitely possible for current systems that—if you compare a model like GPT-4o to a model like o3, I would expect that there will be trade-offs there. I think there are definitely things that are transitory as we figure our way around these technologies, and again, I expect this will get better.

**Sam:** I think there are going to be population-scale effects. One of the strange things I've noticed is people in real life talking in ChatGPT-speak, where they sort of use some of the quirks of things ChatGPT says. I think there will be other things like this where there's this co-evolution of people and the technology in ways we can't totally predict. But my expectation is over time people are much more capable, much more creative, think much more expansively and much more broadly than they do today.

We certainly see examples of this where people are just like, "I never would have been able to keep this in my head. I never would have been able to have this idea." And then we hear other examples where people say, "I've outsourced my thinking and I just do what this thing tells me." Obviously we're much more excited about the former than the latter.

**Sam:** "Can you help us understand why you build emotionally intelligent models and then criticize people for using it for accessibility reasons when it comes to processing emotions and mental health?"

We think that's a good thing. We want that. We're happy about that. The same model that can do that can also be used to encourage delusions in mentally fragile users. What we want is people who are using these models intentionally. The model is not deceiving the user about what it is and what it isn't. The model's being helpful, the model's helping a user accomplish their goals. We want more of that and less of anything that would feel like the model tricking a user, for lack of a more scientific word.

I totally get the frustration here. Whenever you're trying to stop something that is causing harm, you stop some perfectly good use as well. But please understand the place we're coming from here is trying to provide a service to adults that are aware of it and that are getting real value from it and not cause unintended harm to people who don't want that along the way.

**Sam:** All right. Given that we have just a couple of minutes left, let's see if there's any questions in very different directions that we should try to get to.

"When do you think massive job loss will happen due to AI?" from Razi.

**Jakub:** I think already we are at a point where a lot of the gap that stops present models from being able to perform a lot of intellectual jobs is more about integrations and interfaces than maybe raw intellectual capability. I think we definitely have to think about automation of a lot of jobs as something that will be happening over the next years. This is a big thing for us to collectively think about—what are the jobs that will replace those and what are the kind of new pursuits that we'll all engage in?

**Sam:** This is a question from me, not from the livestream. What do you think meaning will look like? What do you think the jobs of the future will look like? How do you think when AI automates a lot of the current things, how do you think we'll derive our fulfillment and spend our time?

**Jakub:** This is a quite philosophical question. I think it can go in many directions, but some things I expect—I think the high-level goal setting, picking what pursuits we're chasing, that is something that will remain human. I think that is something that a lot of people will derive meaning from. I think also just the ability to understand so much more about the world, the incredible variety of new knowledge and new entertainment, but also just intelligence that will be in the world—I think that will provide quite a lot of meaning and fulfillment for people.

**Sam:** Rapid fire, two minutes. "When GPT-6?" from Shindi.

**Jakub:** I think that's more of a question for you in that—I think with previous models like GPT-4, GPT-3, we've kept very tight connection of how we're training new models to what are the products that we ship. As I was saying, right now there's a lot to do on the integration side. For example, with GPT-5 is the first time we really bring reasoning models as our main flagship model. We're not coupling these releases and these products as tightly to our research program anymore.

**Sam:** I don't know exactly when we'll call it that, but I think a clear message from us is say six months from now, probably sooner, we expect to have huge steps forward in model capability.

"Is an IPO still planned and how would the structure then look like? Are there rules in place for increasing capital?"

We don't have specific plans or "this is exactly when it's going to happen," but I think it's fair to say it is the most likely path for us given the capital needs that we'll have and the size of the company. But that's not a top-of-mind thing for us right now.

"You mentioned being comfortable with the 1.4 trillion of investment. What level of revenues would you need to support this over time? What will be the largest revenue driver? It can't just be a per-user subscription." from Alec.

Eventually we need to get to hundreds of billions a year in revenue, and we're on a pretty steep curve towards that. I expect enterprise to be a huge revenue driver for us, but I think consumer really will be too. It won't just be the subscription, but we'll have new products, devices, tons of other things there as well. This says nothing about what it would really mean to have AI discovery in science and all of the revenue possibilities that would unlock. As we see more of that, we will increase spend on infrastructure.

**Sam:** All right. We are out of time. Thank you all very much for joining us and the questions. We will try to learn from this format and iterate on it and keep doing these sorts of Q&As. Thank you very much.