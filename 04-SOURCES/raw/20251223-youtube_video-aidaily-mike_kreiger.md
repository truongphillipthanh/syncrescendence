# How AI Starts Doing the Work in 2026

**Participants:**  
- **NLW** (Nathaniel Whittemore) – Host, The AI Daily Brief  
- **Mike Krieger** – Chief Product Officer, Anthropic; Co-founder, Instagram and Artifact

**Context:** End-of-year conversation exploring the evolution of AI coding, the rise of agentic workflows, and what 2026 holds for enterprise AI adoption.

---

**NLW:** All right, Mike, welcome to the AI Daily Brief. Great to have you here.

**Mike:** It's great to be here. Thanks for having me.

**NLW:** This is a super fun—some of my favorite episodes of the year are these end of year episodes where we get to think big, look forward. One of the big themes for me heading into the new year is everything vibe coding, everything agentic, and so I was super excited to have you join the show. What I wanted to do though is actually go way back a little bit. I think a lot of folks see Anthropic as the torchbearer in a lot of ways for AI coding, and I wondered—I was thinking about when you joined the organization and just how early was that focus clear? Was that an emergent phenomenon as it became clear that there was something very differentiated in these models and that's how people were using it, or was that intention from very early on that this is a broad set of use cases that matter to you guys?

**Mike:** The thing I always like to say whenever there's product folks inside Anthropic that are thinking about which direction to take things in is the more you can align with the company's general long-term perspective about where powerful AI will come from, the smoother things will go because Anthropic is nothing but focused. I think that's shown through in the bets that we choose to make versus not. Definitely there's this belief that for very powerful AI you need the ability of the model to reason about things, to plan agentically and work for a long time horizon, but then also to be able to write and run code—not only to produce software but because it's a really useful tool for solving problems. That belief was in there and it predates me. I joined in May of last year, but it kind of coincided with the outside world realizing it because Claude 3, which had come out I think a month before that, was the first model—and I remember there was like that moment on Twitter when everybody said, "Oh wow, this model can actually write not just function level but like entire files of code." Compared to now it was not very good at it, but it was already amazing what it could do then. We paired it with our first more coding-oriented product, which was Artifacts, so you could have Claude generate—at the time it was mostly React sites—alongside the chat. That was kind of, I think for a lot of people, the first moment they realized, "Oh this is an interesting new experience of coding alongside the model" and not necessarily doing it in a development environment.

**NLW:** It's interesting. I think you can in a lot of ways almost chart people's viability of a lot of this to key releases alongside Anthropic. When I first started this show, it was actually April of 2023, and already agent coding was the thing that people were most excited about. GPT Engineer, which would later morph into Lovable like 18 months later or something like that—that was my first viral YouTube episode was about GPT Engineer. So it's interesting to see at each stage how more use cases get unlocked and a broader set of people come into the fold.

Coming into 2025, I think that the odds-on favorite for what the year was going to be about, at least if you had looked back at all the AI content creators, was going to be the year of agents, right? And I think looking back, it was—but it was the year of coding agents. Did you guys have a sense coming into this year that this was poised to be kind of the significant use case or the breakout based on what conversations you were having, based on the capabilities that you were seeing?

**Mike:** It's a great moment to reflect because going into the last couple weeks of the year last year, we had built something internally we called Claude CLI, which we later released as Claude Code. The emergence of that came from our Labs team, which is a team that really focuses on trying to do disruptive zero-to-one ideas. That was everything from early computer use explorations and some wacky things, and also this Claude CLI thing. Between I think September when the first version got rolled out internally to December, it rapidly overtook every other coding tool we had internally. It was because it kind of had this bet that the models are going to be able to do more and more—maybe not this model but the next one and the next one and the next one. But let's let the model cook for longer. Let's let it act for longer periods of time. 

Going into the holidays it was that question of: do we release this? Do we now add a third component to the product portfolio beyond just claude.ai and the API? That was the active conversation that was happening. But we really felt like if not us, then at least somebody using our models would co-discover this piece where you don't need to hold the model so closely anymore. You can let it operate over a fuzzier task definition and over a longer time. It doesn't need to go back and forth with you on every single decision.

**NLW:** As we look at 2024, there's this interesting bifurcation that I think has emerged in the year. You've got a lot of builders and developers who have these tools at their fingertips, but then there's this whole other conversation which is happening primarily in the enterprise context where—I think I saw this MIT study, and maybe you did too, that was like, "Hey, AI in the enterprise is not being used very effectively." Even if there's maybe truthiness rather than truth in that study, the resonance it had suggests that there's something there. I wanted to get your perspective on how you think about the changes that you've seen this year in enterprise AI and maybe the gap between where things are and where they could be.

**Mike:** I think there are really three different worlds that are each experiencing this a bit differently. The first is software engineers who are building software for a living. There, the improvements are most obvious and you can very directly map the benefits that you're getting from the models, whether it's Claude Code or Cursor or Windsurf or any number of other tools that have sort of emerged this year. You get very clear sort of anecdotal and then even empirical data about "Here's how much faster I got this done." GitHub has a bunch of data on this as well.

Then you have this second group, which I think is actually relatively underrated, which is non-software engineers who are now building software. We've seen this explosion of sites like Bolt, Lovable, Replit's Agent, v0—all of these which are really interesting because they put coding and software creation as a tool in the hands of many more people. Now it's a question of: can you describe your problem well enough? Can you iterate? Do you know what you want to build? So that's a second group that is kind of learning as they go, which I actually think is one of the more interesting vectors.

Then the third is enterprises, which I think are moving much more slowly and carefully, as you might expect. They're trying to figure out: what are the actual business processes that we want to enable? What are the constraints around privacy and security? In a lot of ways, I find that conversation to be very similar to the conversation around cloud migration that happened in the mid-2010s, which is: we kind of all knew it was going to happen, we kind of knew the broad strokes of what it would look like, but it took a lot of work. 

One of the things that we've been spending a lot of time on is how do we meet enterprises where they are? It's not, "Here's a toy that you can play with"—it's actually, "How do we build the infrastructure, the control planes, the privacy guarantees, the ability to run in the places that you need to run?" That's a lot of blocking and tackling work that I think frankly doesn't get that much coverage, but it is absolutely critical to enterprises being willing to run these models in production.

**NLW:** I want to stay on this for a second because I think there's probably different phases of the journey for a lot of these enterprise companies. I think one of the common things that I hear anecdotally is folks will sort of get that chatbot in their company, and it has some surface-level ROI, and it has some surface-level engagement, and it does create moments of value. But then I think a lot of people talk about, "Well, that's a far cry from doing a total business process redesign around agents, right?" How do you think about that journey? Do you think that we'll start to see more of those kinds of big fundamental process redesigns next year, or do you think that we're in a world where a lot of companies are just going to keep iterating on those surface-level chatbots?

**Mike:** I think we're poised for enterprises to almost go through their infrastructure year in '26. Going back to the MIT study—or the truthiness of it, hold aside the specifics—the fact that it had such resonance suggests, and I agree with this, that there is some gap there. I think that a lot of organizations are embracing now that you're not just going to drop a chatbot in—or you're going to do that, but then to really go to the next level it's going to involve a much more comprehensive review of how you do things. It feels to me like perhaps some amount of that process redesign is what organizations, at least the ones who are kind of ahead, are going to be in for in '26.

**Mike:** Absolutely. I was talking to somebody who runs technology at a large bank and he was telling me that they had to rethink not just the data storage piece, which they had already been doing a lot of work on, but also the data annotation and lineage piece to be more AI-friendly. So that when you asked Claude to, "Hey, help me construct a dashboard on this" or "help me understand this data query," even having that additional layer of annotation or understanding of what these different tables are and what they represent made a huge, huge difference to actually making that a useful product. 

Figuring out what are the missing connector bits is going to be, I think, a lot of 2026. Which is great—we have MCPs, we're seeing more and more enterprises wrap some of their internal services or internal data stores in MCP so they can get access to it inside, for example, Claude. Now the next turn is: that's maybe on the retrieval side, but can you actually start taking action and making it a useful participant in business processes by enabling it to either make a human-assisted decision or queue up a decision that a human can confirm—whatever the human-in-the-loop piece is—but moving up that complexity ladder so that again, it can actually start providing value that befits its level.

**NLW:** In the discourse, I want to talk in our last few minutes about some of your predictions or thoughts about how '26 is going to end up differing from '25 with AI. Maybe just to get us started, we were just talking about expanded enterprise use cases, but what do you think are going to be the biggest blockers for enterprises and how do you think they're going to get through them?

**Mike:** I think for a lot of enterprises that we talk to, there's still this gap between the idealized—"Great, if you ran this perfectly on this one cloud with all your permissions all perfectly set and you're okay with inference happening in this way, then we could unlock use cases tomorrow"—versus the reality, which is: there's legacy systems, there's often regulatory reasons why they will only run in this particular way on AWS in this particular kind of setup. 

A lot of the work that we're doing for next year—the word we're even using is "distributability," which I think the spell corrector tells me is not really a word, but what we really mean is: if we want to bring our intelligence and our agentic primitives—whether it's skills, whether it's the Agent SDK, whether it's storage, whether it's memory, all of these pieces—into actual enterprise workloads, we need to really actually embed and meet them where they are. 

There's a lot more work on, "Hey, let's actually componentize this, make it available everywhere." You see it now that we're on all three major clouds. That general set of projects is closing those gaps because there is interest, especially from the more forward-looking CTOs and CIOs, but they also do need to work with the existing constraints and setup they have. You can get the pilots done in a pretty rough and ready way just to prove it out, but to really reach that production scale, I think that's the biggest blocker.

**NLW:** Tool versus colleague—this is something that we've been talking about for a while, and I think this is maybe a false binary in terms of what, you know, when we reach maturity of AI. But do you think that we'll start to see more of that kind of treating AI not just as a tool but as a thing that can take on ever bigger workloads? Do you think that starts to come to reality next year?

**Mike:** Yeah, I think that probably more than anything is what will define the year. You're starting to see this already with coding. We did this GitHub partnership with their Agent HQ piece where now you tag Claude in a pull request and then you go have your coffee and you come back and it's done whatever you needed to do. And we did the same integration with Claude Code. That's pointing at the kind of interaction that you might expect. 

Now, is it already going to be at the place where it can onboard onto the organization, understand the problem space, understand the dynamics of all the relationships and just pick up work? No, I don't think we're going to be there. Maybe near the end of the year we'll have some early glimmers of there. But I do think the more like piece of the job function that has a clean, "All right, great, we need to prepare this kind of report. Here's the work I've done already. Here's where you can go get more information. Here's what good looks like. Report back to me"—in the way that you might delegate to somebody else—that's very much around the corner. It's how we're thinking about a lot of our product strategy going into next year: how do we enable that? What are the interfaces that we need to create that make that possible? And then what do we learn about what's working in the software domain that we can apply to knowledge work?

**NLW:** This maybe asking you too much to put on a marketing hat, but if you had a phrase for capturing what you hope AI does in '26, what would it be?

**Mike:** Reliably take work off your plate.

**NLW:** I like it. All right, Mike. Well, this is a super fun conversation. Could go for another half hour, hour easy, but appreciate you making the time and really excited to see what you guys cook up.

**Mike:** It was great to be here. Thanks for having me.

---

*Note: All preview content, advertising, and promotional material has been removed from this transcript. The conversation begins at its natural starting point following the introduction.*

**Verification Notes:**

[^1]: **Claude 3**: Released in March 2024, preceded Mike Krieger's arrival at Anthropic in May 2024.

[^2]: **Artifacts**: Anthropic's feature enabling code generation alongside chat, launched with Claude 3 in early 2024.

[^3]: **Claude Code**: Previously called "Claude CLI" internally, this command-line coding agent tool was developed by Anthropic's Labs team and released publicly in 2024.

[^4]: **MCP (Model Context Protocol)**: Anthropic's protocol for enabling Claude to access external data sources and services.

[^5]: **GitHub Agent HQ**: Partnership allowing users to tag Claude in pull requests for automated code review and modification.

[^6]: **Major cloud platforms**: Anthropic's models are available on AWS, Google Cloud Platform (GCP), and Microsoft Azure.
