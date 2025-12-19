# Fully Autonomous Robots Are Much Closer Than You Think

**Participants:** Dwarkesh Patel (host), Sergey Levine (co-founder of Physical Intelligence, UC Berkeley professor)

**Context:** A conversation about the path to general-purpose household robots, with Sergey estimating widespread autonomous robotics deployment by 2030. The discussion covers foundation models for robotics, scaling challenges, hardware bottlenecks, and implications for human labor and geopolitics.

---

**Dwarkesh:** Today I'm chatting with Sergey Levine, who is a co-founder of Physical Intelligence, a robotics foundation model company, and also a professor at UC Berkeley and generally one of the world's leading researchers in robotics, RL, and AI. Sergey, thank you for coming on the podcast.

**Sergey:** Thank you, and thank you for the kind introduction. Let's talk about robotics. Before you pepper me with questions, I'm wondering if you can give the audience a summary of where Physical Intelligence is at right now. You guys started a year ago—what does the progress look like? What are you working on?

**Dwarkesh:** Physical Intelligence aims to build robotic foundation models. That basically means general-purpose models that could in principle control any robot to perform any task. We care about this because we see this as a very fundamental aspect of the AI problem. The robot is essentially encompassing all AI technology. If you can get a robot that's truly general, then you can hopefully do a large chunk of what people can do.

Where we're at right now is that we've gotten to the point where we've built out a lot of the basics. Those basics are pretty cool—they work well. We can get a robot that will fold laundry and go into a new home and try to clean up the kitchen. But in my mind, what we're doing at Physical Intelligence right now is the very beginning. It's putting in place the basic building blocks on top of which we can tackle all these really tough problems.

**Sergey:** One year in, I got a chance to watch some of the robots do pretty dexterous tasks like folding a box using grippers. It's pretty hard to fold a box even with my hands. If you had to go year by year until we get to the full robotics explosion, what needs to be unlocked?

**Dwarkesh:** There are a few things that we need to get right. Dexterity obviously is one of them. In the beginning, we really want to make sure we understand whether the methods we're developing can tackle the kind of intricate tasks that people can do—folding a box, folding different articles of laundry, cleaning up a table, making coffee. Those results we've been able to show are pretty cool, but the end goal isn't to fold a nice T-shirt. The end goal is to confirm our initial hypothesis that the basics are solid.

From there, there are a number of really major challenges. When results get abstracted to the level of a three-minute video, someone can look and think, "That's what they're doing." But it's not. It's a very simple and basic version of what I think is to come.

What you really want from a robot is not to tell it, "Hey, please fold my T-shirt." What you want is to tell it, "Hey, robot, you're now doing all sorts of home tasks for me. I like to have dinner made at 6:00 p.m. I wake up and go to work at 7:00 a.m. I like to do my laundry on Saturday, so make sure it's ready. By the way, check in with me every Monday to see what I want you to pick up when you do the shopping." That's the prompt. Then the robot goes and does this for six months, a year.

Ultimately, if this stuff is successful, it should be much bigger. It should have the ability to learn continuously. It should have understanding of the physical world, common sense, the ability to pull in more information if it needs it. Let's say I ask it, "Hey, tonight, can you make me this type of salad?" It should figure out what that entails, look it up, go and buy the ingredients.

There's a lot that goes into this. It requires common sense. It requires understanding that there are certain edge cases you need to handle intelligently, cases where you need to think harder. It requires the ability to improve continuously. It requires understanding safety, being reliable at the right time, being able to fix your mistakes when you make them. The principles there are: you need to leverage prior knowledge and you need to have the right representations.

**Sergey:** This grand vision—what year? If you had to give an estimate: 25 percentile, 50, 75?

**Dwarkesh:** I think it's something where it's not going to be a case where we develop everything in the laboratory and then come 2030-something, you get a robot in a box. It'll be the same as what we've seen with AI assistants. Once we reach some basic level of competence where the robot is delivering something useful, it'll go out there in the world. The cool thing is that once it's out there in the world, they can collect experience and leverage that to get better.

To me, what I tend to think about in terms of timelines is not the date when it will be done, but the date when the flywheel starts. When does the flywheel start? That could be very soon. There are some decisions to be made. The more narrowly you scope the thing, the earlier you can get it out into the real world. We're already exploring this. We're already trying to figure out what real things this can do that would allow us to start spinning the flywheel.

In terms of stuff that you would actually want to have deployed, I'd say my 50th percentile is somewhere around 2029, 2030.

**Sergey:** That's wild. In 2030, you think we have robots that can run households?

**Dwarkesh:** That's my median estimate. My 25th percentile is significantly sooner, but the 75th percentile is five years after that.

**Sergey:** Why do you think robotics will scale faster than self-driving cars? That's the natural comparison.

**Dwarkesh:** Self-driving cars had a few different challenges. One is that there's this long tail of edge cases that are really hard to handle. Another is that there's a lot of liability concerns. But I think the fundamental issue is that self-driving cars are optimized for a very narrow task—driving on roads. Every car must handle every road scenario, every weather condition, every type of driver behavior.

Robots are different. We don't need a single robot to handle every task perfectly. We need many robots handling many different tasks, and they can specialize. You can have a robot that's really good at cooking in a particular kitchen. You can have a robot that's really good at doing laundry in a particular home. That specialization, combined with the ability to continuously improve through real-world deployment, is fundamentally different from the self-driving car problem.

Also, the liability structure is very different. If a robot makes a mistake folding your laundry, you notice and you correct it. If a self-driving car makes a mistake, there can be catastrophic consequences. That's a fundamental difference in terms of the risk tolerance for deployment.

**Sergey:** That makes a lot of sense. So your model here is that you deploy systems that work for 80 percent of tasks, and then they improve over time as they encounter more data?

**Dwarkesh:** Exactly. And this is where the foundation model approach becomes crucial. If we have a general-purpose model, then as we deploy robots across different homes and different environments, they see incredibly diverse data. That diversity feeds back into improving the model for everyone. It's a virtuous cycle.

With self-driving cars, you had this constraint that you couldn't really deploy something until it was nearly perfect. With robots in homes, the deployment can come much earlier. The robot doesn't need to be perfect—it needs to be useful. And the more robots we deploy, the more data we collect, the better the models become.

**Sergey:** Walk me through how a vision-language-action model actually works in the context of robotics.

**Dwarkesh:** So the idea is that you have a large language model or vision model that has been trained on internet-scale data. It understands a lot about the world, about language, about images. But it hasn't seen very much robot data. What we're doing is we're taking that pre-trained foundation model and we're finetuning it on robotics data. That robotics data includes images from the robot's camera, the action that the robot took, and any language instruction.

So in training, you might have a scenario where the model sees, "There's a plate on the table. There's a robot gripper approaching the plate." And the model learns to predict what action the robot should take—open the gripper slightly, move forward slowly, then grasp. When you deploy it, you can give it language instructions: "Pick up the plate and put it in the sink."

The model has to ground the language in the visual scene and predict the appropriate sequence of actions. What's powerful about this approach is that the pre-training on internet-scale data gives the model a lot of prior knowledge. It already understands physics, common sense, and object relationships. The robotics finetuning teaches it how to actually control a physical system.

**Sergey:** How much data are we talking about? Are we talking about millions of robot hours?

**Dwarkesh:** We're talking about a lot of data, but it's not as much as you might think. We've found that with the right approach to data collection and the right architecture, you can get pretty far with hundreds of thousands to a few million robot demonstrations. That's still a massive amount of data compared to what humans learn from, but it's not billions of examples.

The key is that you're not starting from scratch. You have the pre-trained vision model, the pre-trained language model. You're just teaching the model how to translate from "I want this thing" to "here's the sequence of actions to make it happen."

**Sergey:** But where does that data come from? Are you collecting it with real robots or with simulation?

**Dwarkesh:** Both. We use simulation for a lot of initial training because it's cheap and you can generate a lot of data. But you have to be careful about the simulation-to-reality gap. Eventually, you need real robot data from real environments. That's why deployment is so important. Once you have robots out in the world, they generate real data at scale.

We're also using a mix of approaches. We have some teleoperated data—humans controlling robots to demonstrate tasks. We have some learned data—robots learning from their own experience and from each other. And we're exploring ways to leverage simulation more effectively while minimizing the sim-to-real transfer problem.

**Sergey:** This is interesting because it seems like in simulation, you'd have this problem where you could optimize for a narrow set of dynamics, and then when you hit reality, it doesn't work. How do you handle that?

**Dwarkesh:** That's been one of the biggest challenges in robotics for decades. The traditional approach was to try to make the simulation as realistic as possible—model every detail of friction, every aspect of the physics engine. But that's incredibly difficult and often doesn't work anyway.

What we're finding is that with large models trained on diverse real-world data, they become quite robust to these differences. The model learns general principles about how the world works, and those principles transfer across different simulation engines, different hardware, different environments. It's not perfect—there's definitely still a sim-to-real gap—but it's much smaller than it used to be.

Also, we're training on diverse real data from the start. So the model sees variation in how different grippers work, how different surfaces feel, how different objects respond to manipulation. That diversity helps with generalization.

**Sergey:** What changes would we need to see for robots to approach something like the efficiency of a brain?

**Dwarkesh:** That's a great question. The brain is incredibly efficient in terms of both computation and energy. A robot today requires vastly more compute than a brain to do relatively simple tasks. There are a few things that need to change.

First, hardware needs to evolve. Robot actuators need to be more efficient, more responsive, more aligned with how biological systems work. The sensors need to be better. We need to move away from this heavy dependence on high-speed GPUs doing complex inference. We need compute that's more distributed, more local to where the sensing and actuation is happening.

Second, the algorithms need to be smarter. We need learning algorithms that learn more efficiently from data, that don't need as many examples as current neural networks require. We need mechanisms for continual learning, where the robot can keep improving without catastrophic forgetting. We need meta-learning—learning how to learn—so that the robot can adapt quickly to new tasks and new environments.

Third, we need better representations. The brain doesn't represent the world the way a neural network does. It has more structured, more hierarchical representations. It has multiple levels of abstraction. I think we need to move toward models that have that kind of structure.

Fourth, and this is philosophical but important, we need to think about what the brain is actually optimizing for. The brain is optimized for survival, for efficient energy use, for flexibility across many tasks. Current AI systems are often optimized for narrow metrics—accuracy on a dataset, speed on a benchmark. If we designed systems that were fundamentally optimized for efficiency and flexibility, they'd look quite different.

**Sergey:** But the brain has also had millions of years of evolution.

**Dwarkesh:** Right. And that's the thing—we're trying to do in a few years what biology did over millions of years. That's why I think we're going to lean heavily on learning from data, on diverse experience, on the ability to share knowledge across robots. That's why the foundation model approach is so promising. Instead of each robot having to learn from scratch, they can benefit from the cumulative experience of thousands of robots.

**Sergey:** Let's talk about learning from simulation again. Where is that landscape right now? How much are people able to close the sim-to-real gap?

**Dwarkesh:** The sim-to-real gap has been improving dramatically. A few years ago, it was basically insurmountable—you'd train in simulation and deploy in reality and nothing would work. Now, with the right techniques, you can get surprisingly far with simulation pre-training.

The key techniques are domain randomization, where you vary the simulation parameters so the model sees many different versions of the same task, and then learns to be robust across those variations. Another is adversarial domain adaptation, where you try to find the differences between simulation and reality and minimize them. And there's direct sim-to-real transfer, where you take a model trained in simulation and just deploy it in the real world, often with just a bit of fine-tuning.

What's changed is that with large models trained on diverse real data, they're robust enough that the sim-to-real gap is much smaller. You can train 80 percent in simulation and 20 percent on real data, and you get pretty good results.

**Sergey:** Is there a sense in which better simulation is almost a substitute for real world data?

**Dwarkesh:** To some extent, yes. If you had perfect simulation—a simulation that was perfectly accurate to reality—then you wouldn't need real-world data at all. But perfect simulation is impossible. There are always surprises in the real world—unexpected friction, unexpected compliance in materials, unexpected lighting conditions. Real-world data helps you close the gap between what the simulation predicts and what actually happens.

I think the sweet spot right now is: train on diverse simulation data, then fine-tune on real-world data. That gives you the best of both worlds—the scale and diversity of simulation, plus the grounding in reality. As simulation continues to improve, the amount of real-world data you need will decrease. But I think real-world data will always be important.

**Sergey:** How much will robots speed up AI buildouts? If we have robots that can run factories and build hardware, does that accelerate AI development?

**Dwarkesh:** Massively. Right now, one of the big constraints on AI development is that we need to build data centers, we need to build chips, we need to build all this hardware. That's all done by people, and it's relatively slow. If we had robots that could do that work, you could scale much faster. You could build factories faster, manufacture chips faster, deploy systems faster.

There's this feedback loop where better AI enables better robots, which enables faster hardware production, which enables more compute for AI research. It's a positive feedback loop. If you're in a position to tap into that loop—if you have good robotics, good AI, and good hardware manufacturing—you can accelerate dramatically.

That's one reason why I'm quite optimistic about the timelines. We're not just waiting for better algorithms or better hardware in isolation. We're getting feedback between all these systems. Better AI → better robots → better hardware production → more compute → better AI.

**Sergey:** There's a different angle here, which is China. If hardware is the bottleneck, does China win by default?

**Dwarkesh:** That's a really important question. A lot of the sub-components, manufacturing, and supply chain already exist in China. If that's where the bottleneck is, then the feedback loop is stronger in China than in the United States or the West more broadly. That's why I think something really important to get right here is a balanced robotics ecosystem.

AI is tremendously exciting, but we should also recognize that getting AI right is not the only thing we need to do. We need to think about how to balance our priorities, our investment, the things we spend our time on. At Physical Intelligence, we do take hardware seriously. We build a lot of our own things and we want to have a hardware roadmap alongside our AI roadmap.

But that's just us. For the United States, arguably for human civilization as a whole, we need to think about these problems very holistically. It's easy to get distracted when there's a lot of excitement and progress in one area like AI. We're tempted to lose track of other things—the hardware component, the infrastructure component with compute. In general, it's good to have a more holistic view.

**Sergey:** How should society be thinking about the advances in robotics and knowledge work?

**Dwarkesh:** Society should be planning for full automation. There will be a period where people's work is way more valuable because there's this huge boom in the economy where we're building all these data centers and factories. Eventually, humans can do things with their body and we can do things with our mind. There's not some secret third thing.

Society will also be much wealthier. Presumably, there are ways to do this such that everybody is much better off than they are today. But the end state—the light at the end of the tunnel—is full automation plus a super wealthy society with some redistribution or whatever way to figure that out.

**Sergey:** I don't know if you disagree with that characterization.

**Dwarkesh:** At some level, that's a very reasonable way to look at things. But if there's one thing I've learned about technology, it's that it rarely evolves quite the way people expect. Sometimes the journey is just as important as the destination. It's very difficult to plan ahead for an end state. Directionally, what you said makes a lot of sense.

I do think it's very important for us collectively to think about how to structure the world around us in a way that's amenable to greater and greater automation across all sectors. But we should really think about the journey just as much as the destination, because things evolve in unpredictable ways. We'll find automation showing up in all sorts of places, probably not the places we expect first.

The constant that's really important is that education is valuable. Education is the best buffer somebody has against the negative effects of change. If there is one single lever we can pull collectively as a society, it's more education.

**Sergey:** Is that true? Moravec's paradox is that the things most beneficial from education for humans might be the easiest to automate, because it's easy to educate AIs. You can throw the textbooks that would take eight years of grad school to do at them in an afternoon.

**Dwarkesh:** What education gives you is flexibility. It's less about the particular facts you know, as it is about your ability to acquire skills and acquire understanding. It has to be a good education.

**Sergey:** Okay, Sergey, thank you so much for coming on the podcast. This was really fascinating.

**Dwarkesh:** Yeah, this was intense. Tough questions.

---

*Note: All preview content, advertising, and promotional material has been removed from this transcript. The conversation begins at its natural starting point.*

**Verification notes:**
- **Physical Intelligence**: Co-founded by Sergey Levine; focused on developing general-purpose robotic foundation models
- **Moravec's Paradox**: A concept in AI and robotics stating that high-level reasoning requires relatively little computation, while sensorimotor skills require enormous computational resources
- **Foundation Models**: Large-scale models trained on diverse data that can be adapted for specific downstream tasks
- **Vision-Language-Action Models**: Neural networks that take visual input and language instructions as input and produce robot actions as output
- **Domain Randomization**: A technique for sim-to-real transfer where simulation parameters are randomly varied during training to improve robustness
