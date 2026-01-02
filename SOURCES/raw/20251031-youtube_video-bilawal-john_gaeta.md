# The Matrix's Hidden Blueprint: John Gaeta on Building the AI Revolution

**Participants:**  
- **Bilawal Sidhu** — Host, technology curator for TED, former Google product manager  
- **John Gaeta** — Oscar-winning visual effects supervisor for The Matrix trilogy

**Context:** John Gaeta discusses how The Matrix trilogy's visual effects innovations—from bullet time to universal capture—became foundational technologies for modern AI filmmaking, game engines, and virtual production tools.

---

**John:** We were working on the very first Matrix years before the first one. We were confronted with conceptual premises that needed to match up with the idea of the film—that at some point, story could take place in a flawless simulation. And the goals of that in moviemaking terms, this is the early '90s, early to mid-'90s—imagine we're only so many years down from the vector graphics introduction of Tron. It's really not that much time in the longer scheme of things. So there were really small building blocks available to think about at that time.

But the main idea was: how do we essentially believe that these characters are in this simulation? Traditional old-timey Hollywood, you think about what illusion can you create, how do you hack the idea so that the audience believes it. But it was different back then for me because the Wachowskis gave incredible license to us to attempt some early approaches that I guess in these days would probably never have been allowed to happen because the risk involved was really too high. We're living in a very risk-averse version of Hollywood now.

So essentially what we tried to do is figure out: in any simulation, you would comprise sources of reality, the real world, and essentially some kind of delivery system that allowed the user-participant to have limitless ability to navigate—God's eye power, among so many other powers. So we're like, okay, how do we get God's eye power on the screen? How do we imply that? 

The hack of the first film, which was very different than the way we did the second and third, was: how do we feel like we can have omnipresent perspective? There's no physical way to cheat time and space shooting with old cameras, regular cameras. We're going to need to put a camera everywhere where perspective needed to be. And that essentially was a hack—it's a full hack.

**Bilawal:** This is the 120-camera still camera rig that you essentially built to do that iconic bullet time shot. And is it true that certain background sequences were some of the first instantiations of photogrammetry or reality capture on the silver screen? How did that come about? Did you go to SIGGRAPH and find a wild Paul Debevec and see his PhD thesis film?

**John:** The problem at that time was it had to be divided between what you could do in the foreground with the actors and what everything else was. We still had options like photographing things as panoramics or with motion control systems, robotic camera systems. But at that time, my colleagues—they were leading-edge thinkers in graphics—were hearing about some other research going on in universities. 

So at that time we looked around the world at experiments in universities because these ideas, they're not necessarily lightning strikes in a bottle. There are people around the world that are starting to put some things together, starting to put together experiments and media labs of a kind, early-stage computer graphics labs is where you might find some of this. 

So yeah, we found a number of PhD students. Paul Debevec over in Berkeley was close in the neighborhood, and we were looking at some of his work. Yes, they were thesis films that he was putting together. That was a reflection technique that was new to everybody. Very experimental. Our ability to adopt it at that point was just in small ways. We were taking a spherical environment photo, and that could give us some of the lighting properties that were sourced from the real world. We could use that. We could do reflection maps because we were already using reflective things in the environment.

So it was very small at the beginning. But you could see that there was a lot there that could probably be developed. Then moving forward in time with Matrix 2 and 3, we said, "Okay, let's take it much further." We need to do large-scale action in CG worlds, but we need to source them from the real world and make those worlds feel absolutely indistinguishable photographically—like they were photographed on location.

**Bilawal:** So this is the universal capture stuff, right? You're capturing the city block and then rebuilding it entirely in CG for those freeway sequences.

**John:** Exactly. So we thought, "Okay, what other researchers are around?" George Borshukov—he was doing his thesis at Berkeley as well—was thinking about lighting models and techniques to capture lighting in a much higher level of detail and completeness. So the notion there was: let's take a block, surround it with cameras, take simultaneous photographs from many perspectives, and then triangulate all of that visual information into essentially a point cloud that describes that space.

The problem is, how do you get textures? Do you get images? How do you make the images look right? Because you're not going to use little tiny pictures from all these angles—that's impractical. So George had an interesting approach to figuring that out. I won't go deep into it, but the approach was being able to take that data with a reasonable texture set on it and then work in tools that we had to enhance it, to build out what needed to be built out, to essentially do that alchemy.

That allowed us to photograph an entire freeway and build a CG freeway—an almost mile-and-a-half-long stretch that Neo and Morpheus and Trinity end up running on, being chased by ghost twins and agents. That was the very beginning of what I would call universal capture—the idea that you can take the real world and put it into a computer as a data set.

**Bilawal:** And then you can relight it because you have the HDR information, you can recamera it because you have the spatial information, you can retime it because you have temporal information—

**John:** Exactly. Of course, at that time, it was all still. It wasn't yet moving. So the next steps—which I guess we maybe tried in small experiments later—would be: can you take moving volumetric information from people and put them in there? That's where it gets really interesting because then you have volumetric video. You're capturing people and action, and you can replay it and relight it as you're describing.

That's all really matured now. There are many people around the world that can do that. It's a standard technique. But you're talking 20-plus years ago when we were trying to do that. And you know, those small experiments—there were people trying to do volumetric capture simultaneously. There were a bunch of innovators who were trying it. But you could see where it was headed.

**Bilawal:** So then fast-forward to Matrix 4, the Wachowskis come back. I think it was just Lana at that point. You had Unreal Engine in the mix. You're starting to experiment with new paradigms of filmmaking—virtual production, LED volumes. What was that experience like for you?

**John:** It was more of a chance to take my own time and experiment with some different things. Because Matrix 4 really needed to be a reboot, a continuation of the franchise, right? So narrative had to do what narrative had to do. There were less opportunities for us to push certain boundaries of technique simply because we had to hit other goals.

But I was able to take a lot of the thinking that we had had and start experimenting with things that I thought could probably happen in the future. I had been using Unreal for game development, simple game development stuff with friends. And I thought, "Well, let's just take the Neo character. Let's use one of these MetaHumans"—which was very early at that time, not nearly as sophisticated as it is now—"and let's just throw together a scenario."

What I wanted to see was: could we build the interior of one of the Animatrix vignettes? One of them was a woman had kind of walked into a simulation error, and the simulation was stuck in a time loop in this little back-alley area. And kids were jumping into it, and when they would jump into the simulation error, gravity was turned off. So kids were playing in this antigravity zone. And then agents would come and fix the glitch, and it would go away.

I thought that was so cool. It was conceived by one of the anime directors that was involved, Peter Chung. So I took Unreal and said, "Let's build a simulation error game level where you can walk in as Neo." At that time, you could already get photogrammetry city blocks from Quixel or from the Unreal Marketplace. So we just took a block, threw it in, and then we spent some time coding essentially a glitch effect. We actually used Niagara tools—I think there was an early version of something called Chaos, which is a physics system—to make objects levitate and then fall based on the player entering and exiting the zone.

So you could walk in, and if you had a VR headset or even on your desktop, you could walk into this zone and play this thing. That was so satisfying. It was immediate. I could do that with two or three engineers and a designer in a very short amount of time. That was one experiment. 

Then we thought, "Let's go bigger. Let's build a much larger scale, city-scale scenario where Neo could be running around an entire city." Again, at that time, you could get city blocks, and so we just started throwing a bunch together like Lego blocks and building a scenario where he could navigate.

**Bilawal:** So you're basically building these game levels set in the Matrix universe for what reason? Was the goal to ship it with the film? Was the goal to build transmedia storytelling extensions? What was the vision?

**John:** The vision was—I've been thinking about this for years, and this goes back to our earlier conversation about the magic layer on top of the real world—the vision was that all these story scenarios that exist in the Animatrix could potentially be things you navigate to. Imagine you have access to a Matrix-world app on your phone, and you can open it up and you can walk around the real world or virtually navigate to these zones. And in these zones, scenarios are running.

Essentially, I wanted to see the Animatrix stories become playable or experienceable or navigable. That was the vision. Some people could just walk through them and experience them almost like films. Other people could play them like games. The idea was to build a layer that ran in real-time that was essentially transmedia storytelling but gamified—or at least experienceable in different ways.

**Bilawal:** That's fascinating because you're describing basically what a bunch of crypto people were trying to describe awkwardly a few years ago with the "metaverse"—this idea of persistent virtual worlds that you can walk into, that have lore, that have narrative structures embedded in them, that different people can experience differently based on their level of engagement.

**John:** Exactly. And honestly, the term "metaverse" got so polluted. But the core idea is sound: you have a persistent layer, story scenarios are running in certain locations, agents or characters inhabit those spaces, and depending on when you walk in and what you do, you have a different experience. That's the vision I was trying to prototype with these Matrix experiments.

The problem was—and this is where Hollywood kills innovation—there's no infrastructure to support this kind of thinking. You're making a movie. The movie has a budget, has a timeline, has deliverables. There's no line item for "build a transmedia game universe that extends the IP." That's not how the system works. So these experiments happened on my own time, essentially as passion projects to prove the concept.

**Bilawal:** That's such a critical point. Because what you're describing is: the technology was ready, the creative vision was there, the IP was perfect for it—The Matrix is the ideal property for this kind of meta-narrative experimentation—and yet the business model and the organizational structure of Hollywood couldn't support it.

**John:** That's exactly right. And it's not even that they're against it philosophically. It's that the machinery is built for a different product. They know how to make movies. They know how to make TV shows. They even know how to license games now. But this hybrid transmedia experience that lives across platforms, that's persistent, that's episodic in a non-linear way? There's no department for that. There's no budget model. There's no distribution strategy. So it dies in the gap between departments.

I think that's one of the most frustrating things about innovation in Hollywood. It's not that people aren't creative or visionary. It's that the infrastructure is optimized for a 20th-century product in a 21st-century technological landscape. And that gap is where all these experiments go to die.

**Bilawal:** So given that frustration, given that Hollywood can't support this kind of innovation—where do you go from there? You obviously didn't just give up on the vision.

**John:** No, the vision only gets stronger. Because now we have generative AI, we have real-time engines that are incredibly sophisticated, we have distribution platforms that can reach global audiences instantly. The tools have never been better. So the question becomes: do you keep trying to retrofit this vision into the Hollywood system, or do you build new infrastructure?

And I think we're at this inflection point where independent creators, small teams, people who understand both the creative and the technical side, can build experiences that would have required a studio budget five years ago. You can build compelling interactive narratives, you can build worlds, you can build persistent experiences with a tiny team now.

That's what I'm focused on with Escape.art—building tools and frameworks that let creators make these kinds of experiences without needing Hollywood's permission or infrastructure. Because I genuinely believe we're entering a new golden age for expression. Not because of efficiency, but because of permission. The tools give you permission to create things that were previously gatekept.

**Bilawal:** That's such an interesting frame—AI as permission rather than efficiency. Can you expand on that?

**John:** Yeah, so the common narrative around generative AI is that it makes things faster, cheaper, more efficient. And that's true, but I think it misses the more profound shift. The real power of these tools is that they remove barriers to entry. They give you permission to attempt things you previously couldn't.

If you wanted to build a 3D environment five years ago, you needed to learn Blender or Maya, you needed to understand UV mapping and lighting and rendering. That's years of skill development before you can even start expressing your vision. Now, you can describe what you want, and these tools can give you a starting point. You can iterate, you can refine, but the barrier to entry is radically lower.

That's what I mean by permission. It's not that professionals become obsolete—their expertise becomes more valuable because they can move faster and go deeper. But amateurs and beginners can now participate in conversations they were previously locked out of. That's transformative. That changes who gets to make culture.

**Bilawal:** And that's why you keep referencing this idea of bypassing gatekeepers. Because the gatekeepers in Hollywood aren't just saying "no" to bad ideas—they're saying "no" to entire categories of people who don't have access to the traditional pipeline.

**John:** Exactly. And look, I'm not anti-Hollywood. I had an incredible career there. I got to work on projects that most people only dream about. But the system is conservative by nature. It's risk-averse. It invests in known quantities, proven models, safe bets. And that makes sense from a business perspective when you're spending $200 million on a film.

But it also means that entire categories of stories don't get told. Entire types of experiences don't get built. And entire groups of creators don't get opportunities. So when I talk about bypassing gatekeepers, I'm not being antagonistic—I'm being pragmatic. The technology now allows us to route around the traditional infrastructure and build new models for creation and distribution.

And that's happening across the board. Look at YouTube creators, look at indie game developers, look at the explosion of webcomics and web fiction. These are people who said, "I'm not going to wait for permission from a publisher or a studio. I'm going to build my audience directly." And many of them are doing better financially and creatively than they ever could have in the traditional system.

**Bilawal:** So what does this new platform look like? You're building Escape.art—what's the vision there?

**John:** The vision is to create infrastructure for interactive storytelling that's native to the capabilities we have now. Not trying to make movies with extra steps, not trying to make games that feel like movies—but something new that takes advantage of AI agents, real-time rendering, spatial computing, all these technologies we've been discussing.

I think the future of storytelling is participatory. It's not just watching a narrative unfold—it's walking through it, making choices, having conversations with characters who can respond dynamically. And I don't mean in the stilted way games have done branching narratives, where you choose A or B and the story splits. I mean genuinely dynamic, where AI agents can improvise within the bounds of a world's rules and aesthetics.

Imagine you walk into a story world—maybe it's overlaid on the real world through AR, maybe it's fully virtual—and there are characters there who have goals and personalities and histories. You can talk to them, and they can respond in ways that feel genuine because they're powered by language models that understand context and can stay in character. The story that unfolds is partially scripted by a creator who's designed the world and the rules and the characters, but it's also emergent based on your choices and interactions.

That's the vision. And the technology to do this exists now. We have spatial computing devices that are getting better every year. We have AI models that can do character behavior and dialogue. We have real-time engines that can render beautiful worlds at 90 frames per second. The pieces are there—someone just needs to assemble them into a coherent platform.

**Bilawal:** That sounds like a massive undertaking though. Because you're not just building creative tools—you're building a new medium essentially.

**John:** It is. But I also think it's inevitable. Look at how people engage with content now, especially younger generations. They don't want to passively consume. They want to participate, to create, to remix, to make it their own. The medium needs to evolve to match how people actually want to engage with stories.

And I think we're going to see this happen in stages. First, creators will use these tools to make experiences that are still relatively guided—you know, interactive narratives with some dynamic elements but ultimately directed. Then, as the tools mature and as the creator community figures out what works, we'll see more emergent, open-ended experiences where the boundaries between creator and audience start to blur.

We're already seeing early versions of this. Look at what people do in games like Minecraft or Roblox—they're not just playing games, they're building worlds and telling stories and creating experiences for each other. That's the energy I want to capture and give more sophisticated tools to.

**Bilawal:** So in this future you're describing, what does the role of the creator become? Because it sounds like you're not traditional author or director anymore—you're more like a world designer or a dungeon master.

**John:** That's a great analogy. Yeah, I think the creator becomes more like a world architect or a game master. You're designing the rules of the world, the aesthetic, the lore, the characters and their motivations. You're creating the possibility space. But you're not scripting every moment because you can't—the experience is partially emergent based on how people engage with it.

This actually requires a different skill set than traditional filmmaking or writing. You need to think in systems. You need to understand how to create constraints that lead to interesting possibilities. You need to design for emergent behavior rather than trying to control every variable.

Some people will be great at this. Some traditional creators will struggle because it requires letting go of control in a way that's uncomfortable. But I think we'll also see new types of creators emerge who are native to this way of thinking—people who grew up modding games or building in Minecraft or running D&D campaigns. They already think in these terms.

**Bilawal:** And presumably AI becomes a collaborator in this process, not just a tool.

**John:** Absolutely. I think we're moving toward a model where AI is less like a tool you use and more like a creative partner or assistant. You might say, "I want a character who's a world-weary detective with a dry sense of humor," and the AI can help you prototype that character's dialogue patterns, backstory, visual design. You're still the creative director, but the AI is helping you execute the vision much faster.

Or imagine you've designed a world with certain rules, and you want to test how those rules play out in different scenarios. The AI can run simulations, generate edge cases, show you where your design breaks down or where interesting emergent behaviors happen. That's incredibly valuable for iteration.

I think we're going to see AI become a kind of sixth sense for creators—an augmentation that lets you work at a scale and speed that wasn't previously possible. And that's exciting because it means more ambitious projects become feasible for smaller teams.

**Bilawal:** You mentioned "sixth sense," and that reminds me of something you said earlier about AI agents becoming like a sixth sense for humans more broadly. Can you talk about that vision?

**John:** Yeah, so this is where we start getting into more speculative territory, but I think it's where things are heading. Right now, we interact with AI through discrete queries—we ask a question, get an answer, maybe have a conversation. But I think we're moving toward a model where AI becomes more ambient, more contextual, more integrated into how we perceive and navigate the world.

Imagine you're wearing AR glasses, and as you walk through the world, AI is continuously analyzing what you're seeing, hearing what you're hearing, understanding your context. It can surface relevant information proactively. It can answer questions before you fully articulate them. It can help you remember details, make connections, navigate complex environments.

In a creative context, this could mean the AI is always running alongside your creative process, offering suggestions, showing you references, helping you work through problems. It's not interrupting you with notifications—it's just there, available, like an extended cognitive capability.

That's what I mean by sixth sense. It's not about replacing human intelligence or creativity. It's about augmenting it in ways that feel natural and integrated rather than bolted on.

**Bilawal:** That sounds powerful, but it also sounds like we're moving closer to the scenario The Matrix warned us about—becoming dependent on AI systems to the point where we can't tell what's real anymore.

**John:** That's the critical tension, right? The Matrix was a cautionary tale. It was wrapped in comic book and anime foundation, but underneath it, of course, it's a cautionary tale. We don't want to end up being enslaved by these wondrous, remarkable, and occasionally potentially dangerous systems that we're inventing here. We want to make sure that we improve humanity, not risk it all and take people in the other direction.

There is a certain psychological warfare that seems to always be going on through media, whatever stage of media we happen to be talking about—whether it's propaganda during world wars or much more subversive tactics in social media. There's a lot of that to be aware of because the intent is to influence people so that another group has some form of advantage. And I don't agree with that at all. I think that is the immediate concern that we're walking into right now.

There's a big difference between that and intended disinformation whose sole purpose is hurting people. That unfortunately is just going to be unleashed upon us. It's already starting. We're going to move from proofs, prototypes, tests about what's technically possible with generative video and everything else to very deliberate campaigns—disinformation campaigns. It's already kind of beginning.

**Bilawal:** So how do we thread that needle? How do we build these powerful AI systems that augment human creativity and capability without creating the infrastructure for mass manipulation or control?

**John:** I think it comes down to a few principles. First, transparency. We need to be clear about when we're interacting with AI, when content is AI-generated, when decisions are being made by algorithms versus humans. Not in a way that's paranoid or dystopian, but just honest and clear.

Second, agency. The systems we build should amplify human agency, not replace it. AI should be a tool that helps you do what you want to do more effectively—it shouldn't be making decisions for you or manipulating you toward outcomes you didn't choose.

Third, and this is harder, we need to build these systems with genuine safety considerations from the ground up. Not just "can we do this?" but "should we do this?" and "what are the second and third-order effects?" That requires slowing down sometimes when the technology wants to move fast. It requires ethics committees that actually have teeth. It requires regulation that's thoughtful rather than reactionary.

But I'm also optimistic. I think humans are remarkably adaptable. We've navigated technological revolutions before—the printing press, radio, television, the internet. Each time there were valid concerns about manipulation and control. And each time we developed social antibodies, regulatory frameworks, cultural norms that helped us adapt. I think we'll do the same with AI.

The key is staying vigilant. Recognizing that the simulation isn't some future threat—it's here. We're already living in a world where our perception of reality is mediated by algorithms, where our social interactions are filtered through platforms, where the line between authentic and synthetic is increasingly blurred. The question isn't whether we can avoid that. The question is whether we can navigate it consciously and intentionally.

**Bilawal:** That's a powerful place to end. When we made The Matrix trilogy, you were creating the illusion of a future world where one could step into flawless simulation. But you did a few things that turned out to be the kernels of things that would grow into where we are today—being at the precipice, at the literal inflection point where we will in fact walk inside of simulations, story worlds, social worlds on a level that has only been thought about in science fiction. We're almost there.

**John:** We are. And that's both thrilling and sobering. The technology that once simulated danger on screen is now simulating truth, identity, perception of reality. We have all the tools to be worldbuilders now. The question is what kind of worlds we choose to build and whether we build them consciously, with intention and care, or whether we sleepwalk into a reality that's been constructed for us by forces we don't fully understand or control.

That's why this work matters. That's why having these conversations matters. Because the future isn't predetermined. The simulation isn't inevitable. We're writing the code right now, all of us—creators, technologists, users, citizens. And the choices we make in this moment, in this decade, will shape what kind of world we inhabit for generations to come.

So yeah, we're almost there. The question is: where is "there"? And are we going to like what we find when we arrive?