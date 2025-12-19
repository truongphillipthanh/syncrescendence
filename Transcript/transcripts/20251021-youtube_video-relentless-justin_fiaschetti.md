# Inversion CEO on Building the Future of Space Delivery

**Participants:** Ti Morse (Host, Relentless), Justin Fiaschetti (Cofounder & CEO, Inversion)  
**Context:** First interview with Justin Fiaschetti about Inversion, a company building reusable re-entry vehicles for space-based cargo delivery.

---

**Ti Morse:** Do you want to talk about why space-based cargo delivery is important?

**Justin Fiaschetti:** Yeah, absolutely. Thank you for having me. I'm really excited to chat. So at Inversion, we build re-entry vehicles focused mainly on the military—vehicles that allow payloads to be stored in orbit for up to five years and then called down to anywhere on Earth in under an hour, landing softly under parachute.

The core reason we're doing this is making the world more accessible. On the defense side, it's about accessing remote areas. Logistics has always been the determining factor of how battles and wars are won—that goes back to Napoleon and even further. A century ago, humanity took a step forward with the aircraft, which allowed people to move cargo, effects, and people faster and further than ever before. We want to help take that next step, and to do that, we have to use space.

Space is an incredible platform for global access. If you look at the companies making real money in the space industry—Starlink with satellite internet, imaging, GPS—they're all using space as a platform to provide services back down to Earth. My co-founder and I realized, when we were working in the launch industry, that we could apply the same logic to physical cargo. Rather than just digital access to the globe, we could provide physical access. That's what we founded Inversion to do.

We've been working on this for nearly five years now. We launched our first demo mission, Ray, earlier this year—a fully in-house spacecraft built by just 25 people, with every system built internally. That mission led directly to our main product, which we just announced: ARC. It's a four-foot-wide, eight-foot-tall lifting body re-entry vehicle—essentially the world's first space-based delivery vehicle, specifically focused on cargo delivery for the DoD.

**Ti Morse:** You founded the company in January 2021, then went through Y Combinator in Summer 21, and raised your seed round in September or October. So roughly four years before shipping something to space for the first time. What were you trying to get out of the Ray mission?

**Justin Fiaschetti:** The goal was to extract learnings from a first vehicle—both from a company perspective and from a technology perspective. We wanted to understand the processes and operations in orbit, test specific subsystems that go directly onto Arc, like the software, the GNC, the attitude control thrusters. Those systems translate pretty directly to the final vehicle.

It was very much about moving quick—getting a product into the hands of customers or physics as fast as possible. You learn so much just from getting to space. We've taken a lot of those lessons, and because of Ray, Arc's development is probably about two years faster. There are so many things we've either found ways to shortcut or realized we don't need to repeat because we already proved they work on Ray.

**Ti Morse:** What were those things?

**Justin Fiaschetti:** There are a few different places. Some of it comes from the sequencing of development. Traditionally, you build everything and then test at the end. Nowadays, people build and test as they go. We've put tremendous effort and resources into our simulation stack within the company. A lot of folks are familiar with hardware-in-the-loop or software-in-the-loop testing—it used to be a final validation at the end. We've built infrastructure that allows us to test on a daily basis. We run nightly full mission simulations with hundreds of varying inputs—what if we lose GPS, what if we encounter different scenarios. We get that data in the morning, iterate during the day, and run again the next night.

**Ti Morse:** So you're basically compressing years of traditional validation into a few months?

**Justin Fiaschetti:** Exactly. It's a fundamentally different approach. And then on Ray itself, we learned things about actual reentry dynamics, thermal behavior, sensor performance in the actual hypersonic environment—you can't simulate that perfectly. There's always unknowns. Getting Ray to space gave us real data that we could then feed back into the Arc design.

**Ti Morse:** Tell me about the engine malfunction that happened on Ray.

**Justin Fiaschetti:** So Ray had a thruster that didn't perform as expected during the mission. We had designed it assuming a certain burn profile, but when we executed the sequence, one of the thrusters was producing lower impulse than we expected. The real value there was watching our team respond to that in real-time. We had to adapt the trajectory on the fly, adjust our de-orbit plan.

The biggest learning wasn't that something went wrong—it's that our team was able to handle it. We had built enough redundancy and flexibility into the system that we didn't lose the mission. We still got the data we needed. And now, on Arc, we've designed the entire propulsion architecture with that lesson integrated.

**Ti Morse:** So it was more about proving your team could adapt than proving the system was perfect?

**Justin Fiaschetti:** Completely. Nobody's perfect on the first try, especially in space. What matters is how you respond. Do you have the team, the tools, and the processes to adapt? We do. That gives me far more confidence in Arc than if Ray had been flawless—because perfection on a first flight is usually either luck or it means you've overbuilt and added unnecessary cost.

**Ti Morse:** Let's talk about your testing process. How do you think about product iteration in aerospace, where you can't just push an update over the network?

**Justin Fiaschetti:** It's different from software, but the philosophy is similar: learn as fast as possible. We break the development into chunks. Each subsystem—propulsion, attitude control, thermal management—has its own testing regime. We do ground testing, we do simulation, we do integrated testing. Then we fly it. Then we iterate.

The key insight is that you don't need to wait for the perfect design before flying. Perfectionism is expensive in aerospace. You need to be confident the vehicle will work—you can't have it blow up—but 80% confidence is enough if you have good safety margins. We focus on what can reasonably break and build redundancy there.

**Ti Morse:** What doesn't change? What are you building the company around?

**Justin Fiaschetti:** The fundamental need for access. A hundred years from now, humans will still want the ability to move things from one place to another as fast as possible. That's not going to change. The technology will evolve—materials, engines, software—but the underlying need for global access is structural. It's not dependent on any particular trend or market fashion.

That's actually how we evaluate opportunities. We ask: will this be true in a hundred years? Will it still matter? If the answer is no, we don't prioritize it. Satellite internet is a great business, but is it essential a hundred years from now? Maybe not. But the ability to access anywhere on Earth, to deliver something that matters—that's permanent. That's what we're building on.

**Ti Morse:** That's an interesting filter. Most startup founders think about market timing—is this the right moment? You're thinking about permanence.

**Justin Fiaschetti:** It's both, actually. Timing matters. The reason Inversion is possible now is because launch costs have come down, component costs have come down, there's capital availability, and there's market demand—global access is more important than ever. Five years ago, maybe launch costs were too high. Five years from now, maybe it will be different again.

But the core need? That doesn't change. When we were trying to decide whether to actually start the company, we spent the first month trying to find out who else was doing this. We couldn't believe it wasn't already a thing. We thought we must be missing something—that this was so obvious someone had to already be doing it.

**Ti Morse:** The Elon check.

**Justin Fiaschetti:** Exactly. We literally went through all the space companies, looked for anyone building space-based delivery. Nothing. That sense of inevitability—that the world would look fundamentally different once this technology existed—that was what pushed us past the decision point.

**Ti Morse:** How does behavior shift as you scale? Early days you can move incredibly fast, but scaling introduces friction.

**Justin Fiaschetti:** It absolutely does. When it was five of us in a garage, decisions happened in conversation. Now we're much larger, and you have to be much more intentional. We've learned that communication becomes the limiting factor way before technical capability.

What we've focused on is clarity. If everyone understands the direction, the constraints, and the "why" behind decisions, they can move fast independently. When we were smaller, that was implicit. Now we have to make it explicit. We write documents. We have structured conversations. But the goal is the same—get information out, align, and let people run.

**Ti Morse:** Does the cost to make a decision go up?

**Justin Fiaschetti:** The time does sometimes, yes. But the cost of a wrong decision goes down because you've thought it through with more people. In a five-person company, you might move faster on a bad decision because everyone just agreed quickly. Now, if you're making a big call, you involve the people who actually have to execute it. Takes longer to align, but you end up in a better place.

**Ti Morse:** You mentioned the last twenty years—what would the last twenty years have looked like without aircraft?

**Justin Fiaschetti:** Everything slows down. Global supply chains look completely different. International business becomes much harder—you're limited to maritime speeds. Wars, disasters, medical emergencies—everything that requires fast response becomes slower. The geopolitics of the world change. Countries that couldn't be reached quickly become harder to influence or support.

The aircraft didn't just make things faster—it fundamentally rewired how humans operate. And then it became so normal that people forgot it was revolutionary. My vision for space-based delivery is similar. We want to get to the point where re-entry vehicles streaking across the sky are just background noise. Kids playing in the yard don't even notice.

**Ti Morse:** Why are you vertically integrating everything?

**Justin Fiaschetti:** Because we need to move fast and we need to maintain control over the core technology. Every component we outsource is a dependency, another person's schedule, another person's roadmap. For the subsystems that are critical to the vehicle's performance and differentiation—propulsion, structures, attitude control—we build them.

For things that are truly commodity—bolts, connectors, some materials—we buy those. But anything that touches the core mission, we own. It also allows us to iterate faster. If we realize we need to change the thruster design, we don't wait for a supplier. We just change it.

The tradeoff is complexity. It's harder to hire enough talented people to build everything. But the speed we gain is worth it. In aerospace, being first matters, and moving fast matters. Vertical integration is how we compete with well-funded incumbents who have supply chains but are slower to adapt.

**Ti Morse:** What were the early days like at Inversion?

**Justin Fiaschetti:** Chaotic and exciting. We started with my co-founder and a couple of very talented engineers. We had a rough facility, old equipment, a small budget. The constraint was real. You couldn't afford to mess up. Every decision had weight because you didn't have money to fix mistakes.

But there's something freeing about that too. You stop asking permission. You don't have layers of approvals. You just figure out what the problem is and solve it. We built the Ray spacecraft in a garage with 25 people. That's not because we're genius engineers—it's because we had no choice but to be efficient.

We were also very deliberate about who we hired. We looked for people who were competent but also scrappy, people who could operate with uncertainty. That DNA is still here. We've grown, but we still have that mindset.

**Ti Morse:** How do you think about finding great people and then unblocking them?

**Justin Fiaschetti:** The first part is finding people who are actually great—not mediocre, not okay, but genuinely talented and hungry. That's harder than it sounds. It takes time. You talk to dozens of people to find one who's right.

Then once you have them, get out of the way. I read something about how some great leaders like to have crisp documents in meetings so everyone's on the same page, and then lots of time to think and wander and discuss. The crisp document creates context. Then the smart people can actually think.

My goal is to make sure the team is unblocked and trusted. If there's one thing I believe, it's that trust the team is able to do it—because ninety-nine point nine percent of the time, they are. If you hire great people, they flourish more when they have freedom and creativity than when they're told what to do. Set the why and then let them go.

**Ti Morse:** What's the most fun part about being a CEO for you?

**Justin Fiaschetti:** I love the cycle of talking with customers, getting their feedback, iterating on the product. There's a feeling—an aha moment—when you suddenly see how to solve a customer's problem. That excitement builds, and then you go down the path of iterating on it.

For me, that's the part I absolutely love: thinking about a problem from first principles, talking with the customer about it, understanding what they actually need, and figuring out how the product can change or stay the same to meet that need. That's my absolute favorite part of Inversion.

We had a great example recently. We were talking to customers about delivery missions, describing how Arc is designed to glide so it can access the globe. They said, "You should talk to the hypersonics folks down the hall." We did, and they explained they needed Arc for hypersonic testing—not just to test materials like I initially thought, but to test sensors, track the vehicle in flight, test components inside.

That was a moment where I realized Arc is more versatile than we even thought. It's not a one-trick pony. The core platform—low-cost, able to integrate payloads, able to maneuver during hypersonic and supersonic re-entry—is far more useful than we initially understood.

**Ti Morse:** What's the hardest thing you've overcome?

**Justin Fiaschetti:** I think it's going to be an unsatisfying answer, but honestly, it was the first decision—the decision to jump in. Once you make that decision, everything else follows. You're like, "Well, I have to go solve that problem because I'm doing the thing." The decision is made.

It was the decision: Are we going to go for it? Do we think we can have as big an impact on the world as we've always thought we could? Once you answer yes, everything else fits into a framework. You're doing this hard thing because you want to have this impact, because you want to serve these customers. And it's easy not to do it—everyone has ideas, and I've kept a journal of cool ideas my whole life. But the first decision is: are we doing this even if we end up living on the streets? Yes. Okay, cool. Decision made. Everything else comes easier after that.

**Ti Morse:** You kept a journal of ideas. What made this one the one?

**Justin Fiaschetti:** It was a feeling of inevitability. That the world would look different. It was so obvious once we thought of it that frankly, we spent the first month trying to find anyone else already doing it. We couldn't believe this wasn't already a thing. We thought we must be missing something.

It turned out the timing was finally right. Launch costs had come down. Component costs had come down. There's capital availability. There's market demand because global access matters more than ever. But the core insight was recognizing what's structural and what's not.

There are things that will be true a thousand years from now—what humans fundamentally need. AI and LinkedIn are ethereal concepts that are probably useful right now, but were they useful ten years ago? Will they be useful in a hundred years? I don't know. They might be awesome companies to build, but if we're going to dedicate our lives to something, we want it to be something we can always say: this will be real in eighty years when we're old and dying. It was worth spending our time building this.

The vision I hang on to is sitting on a porch with grandchildren playing in the yard, and a re-entry vehicle streaks across the sky. I can look up and say, the team we built made that happen. And the grandchildren don't even notice because it's so common. That's a world worth living in.

---

*Note: All preview/teaser content from the beginning of the interview has been removed. The conversation begins at its natural starting point, immediately after the host's opening question. No advertising, sponsorship reads, or promotional content were present in this transcript.*