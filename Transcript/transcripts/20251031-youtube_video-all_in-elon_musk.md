# All-In Podcast: Elon Musk on 3 Years of X, OpenAI Lawsuit, Bill Gates, Grokipedia & The Future of Everything

**Host:** Jason Calacanis  
**Co-hosts:** Chamath Palihapitiya, David Sacks, David Friedberg  
**Guest:** Elon Musk  
**Date:** October 31, 2025

---

## Disgraziad Corner

**Jason:** Let's get started. We wanted to try something new this week. Every week I get a little upset—things perturb me, Sacks—and when they do, I just yell and scream, "Disgraziad!" I bought the domain disgraziad.com for no reason other than my own amusement. But I'm not alone in my absolute disgust at what's going on in the world. So this week we're bringing out a new feature here on the All-In podcast: Disgraziad Corner.

*[Theme music and clips]*

**Jason:** This is fantastic. This is our new feature. Chamath, you look like you're ready to go. Why don't you tell everybody who gets your Disgraziad this week?

**Chamath:** Wait, we all had to come with a Disgraziad?

**Jason:** You really missed a memo.

**Chamath:** All right, fine. I got one. My Disgraziad Corner goes to Jason Calacanis.

**Jason:** Oh, here we go. Come on, man.

**Chamath:** You and Pete Buttigieg, where in the first 30 seconds of the interview you compared virtue signaling points about how each one worked at various moments at Amnesty International—literally affecting zero change, making no progress in the world, but collecting a badge that you used to hold over other people.

**Jason:** We wrote a lot of letters. We wrote a lot of letters, which is good.

**Chamath:** That means it's a good one. Behind the scenes, Jason and Pete Buttigieg—Disgraziad.

**Jason:** Great. I'm glad that I get the first one, and you can imagine what's coming next week for you. I saw the Sydney Sweeney dress today trending on social. It's too much.

**Chamath:** What? It's too much. What is it? I didn't even know what this is.

**Jason:** You didn't see it? Nick, picture. Bring it up.

**Chamath:** It's a little floppy. How is this disgusting? What are you talking about?

**Jason:** It's disgraceful. A little bit of—look at this. Oh my god. Too much.

**Chamath:** Elegant.

**Jason:** Too much. In my day, Sacks, a little cleavage maybe perhaps in the '90s or 2000s. Some side view. This is too much.

**Sacks:** Very high-brow subject matter. We were discussing our own politics and the Sydney Sweeney dress.

**Jason:** I don't know who's trending on—Hi dad. Hi dad. Put away the phone.

*[Music and theme]*

---

## X's Algorithm and Content Personalization

**Jason:** We open-sourced it to the fans and they've just gone crazy with it. What's going on with the algorithm? I'm getting Sydney Sweeney's dress all day. And last week, Sacks—

**Chamath:** Maybe you should stop favoriting it 15 times.

**Jason:** And then Sacks, poor Sacks got invited to SlutCon for two weeks straight on the algorithm.

**Sacks:** I say the algorithm has become—if you demonstrate—

**Jason:** Sacks, can you even tell if that's a joke or a real thing?

**Sacks:** It's a real thing in San Francisco. It's all too real. It's actually real.

**Jason:** For real. But I've noticed if you demonstrate interest in anything on X now, if you click on it—god forbid you like something—man, the algorithm is on it. It will give you more of that.

**Chamath:** It will give you a lot more.

**Elon:** Yes. We did have an issue. We still have somewhat of an issue where there was an important bug that was figured out and solved over the weekend which caused in-network posts to not be shown. If you followed someone, you wouldn't see their posts. It's obviously a big bug—major bug.

Then the algorithm was not properly taking into account if you just dwelt on something. But if you interacted with it, it would go hog wild. So if you, as David said, if you favored, replied, or engaged with it in some way, it was going to get you a torrent of that same thing.

**Sacks:** Oh, Sacks. So maybe—what was your interaction? Did you bookmark SlutCon? I think you bookmarked it.

**Sacks:** Here's what I thought was good about it though—all of a sudden if you happen to engage with something—

**Jason:** Sydney Sweeney's boobs.

**Sacks:** Okay. But what I thought was good about it was that you would see who else had a take on the same subject matter, and that actually has been a useful part of it.

**Chamath:** You do get more of a 360-degree view on whatever it is that you've shown interest in.

**Elon:** Yeah, it was just giving you—it was just going too far. Obviously it was overcorrecting. It had too much gain on any interaction. You would then get a torrent of that. It's like, oh, you had a taste of it, we're going to give you three helpings. We're going to give you the food funnel.

**Jason:** And that's all being done with Grok now? So it's not like the old hardcoded algorithm, or is it using Grok?

**Elon:** Well, what's happening is that we're gradually deleting the legacy Twitter heuristics. Now, the problem is that it's like as you delete these heuristics, it turns out one heuristic, one bug, was covering for the other bug. So when you delete one side of the bug—you know, it's like that meme with the internet where there's this very complicated machine and there's like a tiny little wooden stick that's keeping it going. You take out the stick, the whole thing collapses. That's what it's like with a lot of legacy code—you've got compensating bugs.

We're gradually replacing the heuristics with actual AI—with Grok—which understands context much better. But there's going to be some bumps along the way as we delete the old code. The old code had a lot of weird special cases and exceptions that were papering over underlying issues. As we remove that and replace it with AI that actually understands what's going on, initially there can be some weird behavior until we tune it properly.

**Friedberg:** Is the algorithm now fundamentally driven by an LLM that's making decisions about what to show people?

**Elon:** Increasingly, yes. The recommendation system is increasingly AI-driven. It's trying to understand what you actually want to see, what you find interesting, as opposed to having all these hardcoded heuristics. The problem with heuristics is they're very brittle and they don't generalize well. Whereas an AI system can actually understand context and nuance.

But you have to be careful because if the AI is too aggressive in learning your preferences, it can create these echo chambers or just flood you with one thing. We're working on getting the balance right.

**Sacks:** One thing I have noticed that's been good is when you express interest in a topic, you do see more perspectives on that topic. So you're not just getting one viewpoint repeated—you're actually seeing what different people have to say about it.

**Elon:** That's the goal. We want to show you multiple perspectives on topics you care about, not just reinforce your existing views. The whole point of X is to be a place for open discourse and debate.

---

## Creating Grokipedia

**Jason:** Let's talk about Grokipedia. This is a fascinating initiative. What's the vision here?

**Elon:** Well, Wikipedia has some serious issues. It's become increasingly biased, particularly on political topics. The editors on Wikipedia have a particular ideological lean, and it shows in the content. Articles about controversial topics are often heavily slanted one way or another.

**Chamath:** What's interesting is that Wikipedia started with this utopian vision of democratized knowledge, but it's ended up being controlled by a relatively small group of very active editors who have strong viewpoints.

**Elon:** Exactly. And those editors essentially control the narrative on many important topics. The original vision of Wikipedia was that the wisdom of crowds would produce neutral, factual content. But it hasn't worked out that way. Instead, you have ideological capture by a small group of editors.

**Sacks:** I've seen this firsthand. If you look at articles about controversial political figures or movements, they're clearly written from a particular perspective. And if you try to edit them to be more balanced, your edits get reverted almost immediately.

**Elon:** Right. So the idea with Grokipedia is to create something that's more transparent and less susceptible to ideological capture. We can use AI to help detect bias and ensure that multiple perspectives are represented. We can also make the editing process more transparent so people can see who's making changes and why.

**Friedberg:** How do you prevent the same problem from happening with Grokipedia? What's different about the structure?

**Elon:** A few things. First, we use AI to analyze content for bias. Grok can detect when an article is presenting only one perspective on a controversial topic. Second, we make the editorial process much more transparent. You can see who edited what and when, and there's a clear record of disputes. Third, we encourage presenting multiple viewpoints on controversial topics rather than trying to force a false "neutral" perspective that's actually just one ideology's view.

**Jason:** So it's more about transparency and showing the debates rather than pretending there's one objective truth on every political topic?

**Elon:** Exactly. On many topics, reasonable people can disagree. Rather than pretending one view is "the truth," we should show people the different perspectives and let them make up their own minds. Obviously, for factual matters—like what year did World War II end—there's an objective answer. But for questions like "was this policy good or bad?" you should see multiple perspectives.

**Chamath:** The other issue with Wikipedia is the institutional capture. If you look at who donates to Wikipedia, you see a lot of corporations and organizations that have vested interests in how certain topics are portrayed.

**Elon:** Yeah, there's definitely been some capture there. Look, I'm not saying Wikipedia is all bad. It's been incredibly valuable for certain types of information, especially historical facts, scientific knowledge, that kind of thing. But on anything politically controversial or related to recent events, it's become quite unreliable.

**Sacks:** And the problem compounds because Wikipedia articles are often the first result in search engines. So if Wikipedia has a biased take on something, that becomes what most people see.

**Elon:** Exactly. So we need an alternative that's more transparent, less captured, and explicitly shows multiple perspectives on controversial topics. That's what we're trying to build with Grokipedia.

**Friedberg:** What about the concern that this just becomes another echo chamber, but for a different ideology?

**Elon:** That's a valid concern, and we're trying to design against that. The key is forcing the presentation of multiple viewpoints. If you write an article about a controversial topic and only present one side, Grok will flag it and suggest that alternative perspectives be added. We're not trying to replace one bias with another—we're trying to be explicitly multi-perspectival.

**Jason:** How do you handle objective facts versus opinions in that framework?

**Elon:** You have to distinguish between facts and interpretations. "This policy was implemented in 2022" is a fact. "This policy was good for the economy" is an interpretation that reasonable people can disagree on. For facts, there should be one accurate answer, sourced properly. For interpretations, show multiple perspectives.

The problem with current Wikipedia is it often disguises interpretation as fact. An article will state something like "This was a controversial policy" as if it's a fact, when really it's presenting one particular framing. A more honest approach would be to say "Supporters argued X, while critics argued Y."

**Chamath:** This gets to a deeper issue about how we think about truth and information in the modern age. The Enlightenment ideal was that there are objective facts and we can discover them through reason and evidence. But we're realizing that on many important questions, there isn't one objective truth—there are different frameworks and values that lead to different conclusions.

**Elon:** Right, but we also can't fall into complete relativism where every opinion is equally valid. There are better and worse arguments, stronger and weaker evidence. The goal is to present the best arguments from multiple perspectives, not to treat all claims as equally credible.

**Sacks:** How do you implement that technically? How does Grok determine what constitutes a legitimate perspective versus what's just nonsense?

**Elon:** That's one of the challenges. We're training Grok on a diverse range of high-quality sources across the political and ideological spectrum. The AI learns to recognize well-reasoned arguments even when they come from different premises. It's not perfect, but it's better than having a small group of ideologically homogeneous editors control everything.

**Jason:** When does this launch?

**Elon:** We're beta testing it now internally at X. Probably public beta in a few months. We want to get it right before opening it up widely.

---

## Three Years of X: Reflecting on the Twitter Acquisition

**Jason:** It's been three years since you acquired Twitter and transformed it into X. Looking back, what's your assessment? What worked, what didn't, what surprised you?

**Elon:** Man, it's been quite a journey. When I first got there, the company was in worse shape than I realized. The cost structure was insane—spending something like $4 billion a year with revenue around $4.5 billion. So basically break-even with massive headcount and expenses.

**Chamath:** What was the headcount when you took over?

**Elon:** About 8,000 people. It's now around 1,500. And we're running better than before. That tells you how much bloat there was.

**Sacks:** That's an 80% reduction. That's incredible.

**Elon:** Yeah. Now, I want to be clear—I'm sure we lost some talented people in that process. But the reality was the company had become extremely bureaucratic and inefficient. There were entire teams doing things that didn't matter. And the product development velocity was incredibly slow.

**Friedberg:** What was the biggest surprise when you went in?

**Elon:** Probably the degree to which the content moderation was ideologically biased. I knew there was bias, but seeing it from the inside was shocking. You had a situation where conservative viewpoints were being throttled or banned for things that left-wing accounts could say with no consequences. The Twitter Files exposed a lot of this.

**Jason:** Let's talk about free speech. You took a lot of heat for reinstating accounts that had been banned. What's your philosophy on that?

**Elon:** Look, my philosophy is simple: if something is legal, it should be allowed on the platform. Obviously there are some exceptions—direct incitement to violence, illegal content like child exploitation. That stuff gets removed immediately. But political speech? That should be allowed, even if it's controversial.

The previous regime at Twitter was essentially acting as an arm of the Democratic Party, suppressing stories and voices they didn't like. The Hunter Biden laptop story is the most egregious example—they literally prevented people from sharing a New York Post article about a major political story. That's insane.

**Chamath:** What's interesting is that initially after you took over, there was this prediction that the platform would become a right-wing echo chamber. But that hasn't happened. If anything, there's more diversity of viewpoint now.

**Elon:** Yeah, people confused "not censoring conservatives" with "only allowing conservatives." What we did was stop putting our thumb on the scale. Now all viewpoints are allowed, which means you see more diversity, not less.

**Sacks:** Although you still do moderate content to some degree, right? It's not completely unmoderated.

**Elon:** Of course. Like I said, illegal content gets removed. We also have a Community Notes feature where users can add context to posts, which I think is way better than top-down moderation. Instead of some content moderator deciding what's true, the community can add information and other users can rate whether that information is helpful.

**Jason:** Community Notes has been really interesting. How's that working?

**Elon:** It's working well. The key innovation is that a note needs approval from people who typically disagree with each other. So you can't just have one side adding biased notes—you need people across the political spectrum to agree that a note is helpful. That means only genuinely useful context gets added, not partisan talking points.

**Friedberg:** What about the financial side? The company lost a lot of advertisers after you took over. How's that going?

**Elon:** Some advertisers left for political reasons, which was frustrating. But advertising revenue has been recovering. We're also building out subscription revenue with X Premium, which I think is healthier long-term. Relying entirely on advertising creates perverse incentives to censor content that advertisers don't like.

**Chamath:** What's the breakdown now between advertising and subscription revenue?

**Elon:** Advertising is still the majority, but subscriptions are growing fast. I think long-term we'll be maybe 50-50, which would be great. It makes us much less vulnerable to advertiser boycotts.

**Jason:** Do you regret buying it?

**Elon:** No. I think it was important for the future of civilization to have at least one major platform that supports free speech. If Twitter had continued on its trajectory, it would have become even more of a censorship apparatus. Now we have a platform where people can actually speak freely, and I think that matters a lot.

The financial pain was significant—I had to sell a lot of Tesla stock, the company lost money initially. But from a civilizational perspective, I think it was worth it. Democracy requires open debate and free speech. We can't have that if all the major platforms are censoring viewpoints they don't like.

**Sacks:** What do you think the impact has been on the broader discourse?

**Elon:** I think it's made a big difference. You now have a major platform where controversial topics can be discussed openly. That's changed the conversation nationally and globally. Issues that were being suppressed are now being debated. Perspectives that were being marginalized are now being heard.

Some people don't like that—they preferred it when the discourse was more controlled. But I think open debate, even when it's messy and uncomfortable, is better than managed consensus.

**Jason:** What are the biggest remaining challenges?

**Elon:** We need to keep improving the product. The video product needs work. We're building out longer-form content capabilities. We want X to be the everything app—not just short text posts, but long-form articles, video, payments, everything.

On the business side, we need to keep growing revenue and moving toward profitability. We're getting there, but there's more work to do.

And on the policy side, we need to navigate the regulatory environment. Governments around the world are trying to force platforms to censor content, and we're resisting that. It's an ongoing battle.

---

## Tesla Shareholder Vote on Elon's Compensation

**Jason:** Let's talk about Tesla. There's this shareholder vote coming up on your compensation package. Can you explain what's happening there?

**Elon:** So, this is about the compensation package that was approved by shareholders back in 2018. It was a performance-based package—I only get paid if Tesla hits very ambitious targets. And Tesla has hit those targets. The company's market cap has increased by something like $600 billion since that package was approved.

But a judge in Delaware decided to void the compensation package, even though shareholders approved it by 73%. The judge basically said shareholders didn't have enough information, which is absurd—it was all disclosed in detail.

**Chamath:** This seems like judicial overreach. Shareholders approved it, you hit the performance targets, but a judge decides it doesn't count?

**Elon:** Exactly. It sets a terrible precedent. If judges can just void shareholder votes, what's the point of having shareholders vote on anything? The Delaware court system has become very problematic for corporate governance.

**Sacks:** What happens if the new vote doesn't pass?

**Elon:** Well, I've said that if shareholders don't reapprove it, I would be uncomfortable growing Tesla to be a leader in AI and robotics without having more control. I currently have about 13% of the company. If I'm going to be steering Tesla through the AI revolution—and Tesla is increasingly an AI and robotics company, not just a car company—I need to have enough ownership that I can't be outvoted.

**Jason:** Is that a threat to leave if you don't get the compensation?

**Elon:** It's not a threat—it's just reality. Look, I have other companies—SpaceX, Neuralink, xAI. I care about all of them. If Tesla shareholders don't want me to be heavily involved in Tesla's future, that's their choice. But I can't responsibly lead Tesla into the age of AI and humanoid robots without having a meaningful ownership stake.

**Friedberg:** What's the right level of ownership for you?

**Elon:** I've said around 25% would be appropriate. That's enough that I can't be easily outvoted, but not so much that I can do whatever I want without board oversight. It's a balance.

**Chamath:** Do you think the vote will pass?

**Elon:** I think so. The retail shareholders are very supportive. It's mainly some institutional investors who are opposed, often for political reasons. But we'll see.

**Jason:** If it doesn't pass, would you actually leave Tesla?

**Elon:** I wouldn't leave entirely, but I would probably reduce my involvement. I'd still be on the board and have input on major decisions, but I wouldn't be running the day-to-day or making all the product decisions like I do now. That would probably be better for the other companies anyway—they'd get more of my time.

But I think it would be bad for Tesla shareholders. Tesla's success has been tied to pushing the boundaries of what's possible. If I'm not as involved, the company will probably become more conservative and move slower.

**Sacks:** This whole situation seems bizarre. You've created hundreds of billions of dollars of shareholder value, and people are complaining that you might get paid a few billion for it?

**Elon:** Yeah, it's pretty absurd when you think about it. The compensation package was 0.5% of the value created. And I only get paid if the targets are hit—it's completely performance-based. Most CEOs get paid regardless of performance. But because the absolute numbers are large, people get upset.

Look, I don't need the money. I'm doing fine. This is about the principle of honoring commitments and respecting shareholder votes. If courts can just void shareholder decisions, the whole system breaks down.

---

## The OpenAI Lawsuit

**Jason:** Let's get into the OpenAI situation. You've sued OpenAI. What's that about?

**Elon:** OpenAI was supposed to be an open-source, nonprofit AI company. That was the original mission—to develop AI for the benefit of humanity, not for profit. I provided the vast majority of funding in the early days, around $50 million, maybe more.

But then they decided to become a for-profit company and partnered with Microsoft. They're now a closed-source, for-profit entity—the opposite of what was promised. And they're probably worth $100 billion or more.

**Chamath:** What are you asking for in the lawsuit?

**Elon:** I'm asking that OpenAI return to its original mission and charter—to be an open-source, nonprofit AI company focused on benefiting humanity. I'm also pointing out that given the degree to which they've deviated from the original mission, I should have some ownership given my early contributions.

**Sacks:** How much ownership do you think you should have?

**Elon:** I don't know, maybe 25% or 30%? I provided the majority of early funding and came up with the name. Sam Altman and the others basically had nothing when I got involved. The company wouldn't exist without my early contributions.

**Jason:** They would argue that the company's value comes from the work done after you left.

**Elon:** Sure, but that work was built on the foundation that I funded. And more importantly, they betrayed the original mission. The company was supposed to be a nonprofit. Now it's a for-profit worth $100 billion, largely controlled by Microsoft. That's not what was promised.

**Friedberg:** What's the great irony you see with OpenAI?

**Elon:** The great irony is that they're called "OpenAI" but they're completely closed. They don't share their research, their models aren't open-source, they're heavily profit-driven. It's false advertising at a grand scale.

Meanwhile, at xAI, we actually are doing things more openly. We published our thinking on AI safety, we're more transparent about our approach. We're actually living up to the ideals that OpenAI was supposed to embody.

**Chamath:** Do you think you'll win the lawsuit?

**Elon:** I think we have a strong case. They fundamentally changed the nature of the organization from nonprofit to for-profit without proper process. They took a company that was supposed to benefit humanity and turned it into a vehicle for personal enrichment. That's a breach of the original agreement.

But legal outcomes are unpredictable. We'll see what happens.

**Sacks:** What about the competitive dynamics? How does xAI compete with OpenAI?

**Elon:** xAI is moving fast. We're training some of the most powerful models in the world. Grok is already competitive with GPT-4, and we're working on the next generation. We have a great team and we're not afraid to push boundaries.

The advantage OpenAI has is they had a head start and they have Microsoft's distribution. But I think we'll catch up and potentially surpass them. And we're doing it with a more honest approach—we're not pretending to be a nonprofit while raking in billions.

**Jason:** Is there bad blood between you and Sam Altman personally?

**Elon:** I mean, I feel betrayed. I trusted Sam and the others to stick to the mission. Instead, they saw an opportunity to make a lot of money and they took it. That's disappointing.

But look, it's business. People do what they do. I'm focused on building xAI into something special, and if the lawsuit helps correct what happened with OpenAI, great. If not, at least we tried.

---

## AI Power Efficiency and the Future of Computing

**Friedberg:** Let's talk about energy and AI. There's been a lot of discussion about how much energy AI is consuming. What's your take on that?

**Elon:** AI training is energy-intensive, but I think the concerns are somewhat overblown. Yes, training a large model requires a lot of compute, which requires a lot of energy. But the total amount of energy is still small compared to other things we do as a civilization.

The more important question is: where does that energy come from? If it's coming from solar or nuclear, it's not really a problem. If it's coming from coal, that's worse. But the total quantity of energy for AI, even scaling up significantly, is manageable.

**Chamath:** What about the infrastructure side? Are we going to have enough data centers and compute capacity?

**Elon:** That's a legitimate constraint. Building out data centers and manufacturing GPUs takes time. Nvidia can only make chips so fast, and building data centers is a long lead-time activity. So there will be bottlenecks.

But those bottlenecks get resolved over time. More fabs get built, more data centers get constructed. It just takes a while.

**Friedberg:** Is there a path to making AI training more efficient?

**Elon:** Yes, absolutely. Right now we're using general-purpose GPUs, which are good at lots of things but not optimized for any one thing. As we develop chips specifically designed for AI training and inference, efficiency will improve dramatically.

Also, the algorithms keep getting better. We're training larger models with fewer FLOPs because we're using better architectures and training techniques. So efficiency is improving on multiple fronts.

**Jason:** What about inference? Once a model is trained, how much energy does it take to actually use it?

**Elon:** Inference is much less energy-intensive than training. It still requires compute, but orders of magnitude less than training. So the energy conversation is really about training, not deployment.

That said, if billions of people are using AI assistants constantly, the aggregate inference energy use could be significant. But again, it's about where the energy comes from. If we're running inference on solar-powered data centers, it's not really an issue.

**Sacks:** Where do you see AI compute going in the future? More centralized in massive data centers, or more distributed?

**Elon:** I think both. You'll have large training runs happening in massive data centers with cheap energy—probably near solar or nuclear power plants. But inference can be more distributed. You can run smaller models on local devices, and you only need to go to the cloud for more complex queries.

Eventually, I think we'll have a hybrid model where you have powerful local compute for privacy-sensitive or latency-sensitive tasks, and cloud compute for things that require massive scale.

**Friedberg:** What about energy sources? You've talked about solar. What's the path to powering all this compute with clean energy?

**Elon:** Solar is the obvious answer. The amount of energy hitting the Earth from the sun is thousands of times more than what civilization uses. We just need to capture a tiny fraction of it.

The challenge is storage. Solar only works during the day, so you need batteries to store energy for nighttime use. But battery technology is getting better and cheaper. I think within 10-15 years, we'll see solar plus storage becoming the dominant energy source for new installations.

---

## Robotaxis and the Future of Self-Driving

**Jason:** Let's talk about autonomous vehicles. Tesla has been working on this for years. Where are we?

**Elon:** We're getting close. Full Self-Driving is improving rapidly. We're probably going to start Robotaxi service in California next year, pending regulatory approval.

**Chamath:** What's the regulatory situation? Are regulators going to allow it?

**Elon:** That's the big question. The technology is ready or nearly ready. The question is whether regulators will let us deploy it. Some states are more open to it than others. California is actually reasonably progressive on this front, despite being restrictive on other things.

Texas would probably be easier, but California has more density, which makes the unit economics better for Robotaxis.

**Sacks:** What's the safety case you're making to regulators?

**Elon:** The data is pretty clear—autonomous driving is safer than human driving. Humans get distracted, drive drunk, fall asleep at the wheel. An AI doesn't do any of those things. It's always paying attention, it has 360-degree awareness, it doesn't get tired.

The statistics bear this out. Tesla cars with Autopilot engaged have fewer accidents per mile than the average human driver. And Full Self-Driving is even better.

**Friedberg:** What's the user experience going to be like?

**Elon:** You'll have a Tesla app, you'll call a Robotaxi, it'll show up at your location, you get in, tell it where you want to go or it already knows from the app, and it takes you there. No driver, lower cost than current rideshare, probably half the cost or less.

**Jason:** How do you handle edge cases? What if someone vandalizes the car or leaves it dirty?

**Elon:** Cars will be monitored remotely. If something goes wrong, we can see it and respond. Cameras inside the car detect if someone is damaging it or leaving a mess. Those people get banned from the service. Just like Uber and Lyft can ban problematic passengers, we can too.

**Chamath:** What's the fleet size going to be initially?

**Elon:** We'll start small—maybe a few hundred cars in a limited area. As we work out the kinks and build confidence with regulators, we'll scale up. Eventually, we could have millions of Robotaxis operating globally.

**Friedberg:** What about the business model for Tesla owners? Can they put their cars into the Robotaxi fleet when they're not using them?

**Elon:** That's the plan. If you own a Tesla with Full Self-Driving capability, you can add it to the Tesla Robotaxi network and earn money when you're not using it. It's like Airbnb for cars.

This fundamentally changes the economics of car ownership. Your car becomes an income-generating asset instead of a depreciating liability. A car that costs $40,000 could generate $30,000+ a year in Robotaxi income. It pays for itself very quickly.

**Sacks:** That seems like it would cannibalize new car sales though. If cars are earning income, people will keep them longer instead of upgrading.

**Elon:** Maybe, but it also expands the addressable market. More people can afford to buy a Tesla if it's going to generate income. And as Robotaxis become more common, car ownership overall might decline, but that's offset by the fleet business.

I think long-term, most Tesla revenue comes from the Robotaxi service, not from selling cars. The cars are almost like razors—we sell them at low margin, and make money on the recurring service revenue.

**Jason:** When do you think we see millions of Robotaxis on the road?

**Elon:** If things go well with regulation and technology continues to improve, maybe 2028-2030 timeframe for millions globally. It could be faster if regulators get out of the way, or slower if they don't.

But I'm confident it's coming. The technology works, the economics work, the user experience is better than human-driven cars. It's just a matter of getting regulatory approval and scaling production.

---

## Bill Gates, Climate Change, and Energy

**Jason:** You and Bill Gates have had some disagreements over the years. But I saw recently that he's changed his position on solar energy. What's that about?

**Elon:** Yeah, Bill has historically been skeptical of solar and battery storage. He's been more focused on nuclear and other technologies. But I think he's coming around to the fact that solar plus storage is the most viable path to clean energy.

**Friedberg:** What was his objection to solar?

**Elon:** He thought it was too intermittent and too expensive. And a few years ago, he had a point. Solar panels were expensive, batteries were expensive, and the intermittency was a real issue.

But costs have come down dramatically. Solar is now the cheapest source of electricity in most places. And battery costs are falling rapidly. So the economics have shifted in favor of solar plus storage.

**Chamath:** Did he publicly acknowledge changing his mind?

**Elon:** I think he's been more open to it in recent statements. He hasn't done a big mea culpa or anything, but he's acknowledged that solar has made more progress than he expected.

**Jason:** You've been saying for years that we need to transition to sustainable energy. Where are we on that transition?

**Elon:** We're making progress, but not fast enough. The good news is that solar, batteries, and electric vehicles are all improving and getting cheaper. The bad news is we're still building new fossil fuel infrastructure and emissions are still rising globally.

The key thing to understand is that it's technically feasible and economically viable to transition to sustainable energy. It's not some impossible dream—the technology exists, the economics work. It's really a question of policy and willpower.

**Sacks:** What policies do you think would accelerate the transition?

**Elon:** Honestly, I think a carbon tax is the right answer. Make the cost of carbon emissions explicit, and let the market figure out the best way to reduce emissions. But that's politically difficult.

Short of that, I think policies that support solar, batteries, and EVs make sense. Tax credits, subsidies for charging infrastructure, streamlined permitting for solar installations. Remove barriers to deployment.

**Friedberg:** What about nuclear? Should we be building more nuclear plants?

**Elon:** I'm not anti-nuclear. I think nuclear is better than fossil fuels, for sure. The problem with nuclear is it's expensive and takes a long time to build. By the time you build a nuclear plant, you could have deployed a huge amount of solar and storage for the same money, and it would generate more total energy.

That said, if people want to build nuclear, I'm not going to stand in their way. We need all the clean energy we can get. I just think solar and batteries are a faster, cheaper path.

**Jason:** What about other renewable sources like wind?

**Elon:** Wind is fine, but it has some drawbacks compared to solar. Wind turbines have moving parts that break, they kill birds, some people think they're ugly. Solar panels just sit there and work for 25+ years with minimal maintenance.

Again, I'm not against wind. But if I had to pick one technology to bet on for clean energy, it would be solar plus batteries.

**Chamath:** What's the timeframe for getting to 100% renewable energy globally?

**Elon:** If we really committed to it, we could do it by 2050, maybe even 2040. But we're not really committing to it. We're making incremental progress, but we're not treating it like the existential priority it is.

The technical challenges are solvable. The cost is manageable—probably a few trillion dollars globally over 20-30 years, which sounds like a lot but is actually tiny compared to global GDP. The limiting factor is political will and regulatory barriers.

**Friedberg:** You mentioned earlier that solar could power everything, including all the AI compute. Can you walk through those numbers?

**Elon:** Sure. A gigawatt is a billion watts. Most data centers use a few hundred megawatts to a few gigawatts. Solar provides about one gigawatt per square kilometer of land area, or roughly 2.5 gigawatts per square mile, assuming decent solar panels and packing density.

So if you wanted to power, say, 10 gigawatts of data center capacity, you'd need about 4 square miles of solar panels, plus batteries for storage. That's a lot of panels, but it's not an insane amount of land. You could fit that in a lot of places.

**Jason:** And you think batteries can handle the storage problem?

**Elon:** Absolutely. Lithium-ion batteries are getting cheaper and better every year. We're producing them in massive quantities for EVs. Scaling up production for grid storage is just a matter of building more factories.

The raw materials are abundant—lithium, iron, phosphorus, carbon. These are all common elements. There's no resource constraint. It's just a matter of building out the manufacturing capacity and deploying the systems.

**Sacks:** So why isn't this happening faster?

**Elon:** A lot of it is inertia. The existing energy system has enormous sunk costs and political influence. Utilities are optimized around centralized power generation and distribution. Transitioning to distributed solar plus storage requires rethinking that whole model.

Also, permitting and regulations make it hard to build new energy infrastructure quickly. It can take years to get approval to build a solar farm or a battery storage facility.

But I think we're at an inflection point. The economics are so compelling now that it's going to happen whether incumbents like it or not. Solar plus storage is just going to out-compete fossil fuels on pure economics, and then the transition accelerates.

---

## Wrapping Up

**Jason:** Elon, this has been great. Thank you for taking the time.

**Elon:** Good to see you guys. Thanks for having me.

**Chamath:** Come back anytime. We'll send you the Zoom link.

**Elon:** Yeah, I see you're all in different places. Very virtual situation.

**Jason:** We try not to be in the same room. Only when we do the summit.

**Sacks:** But otherwise, we each stay in our own locations.

**Elon:** Your summit is pretty fun. We had a great time recounting SNL sketches that didn't make it.

**Jason:** Oh god, there's so many good ones. We didn't even get to the Jeopardy ones.

**Elon:** Yeah, those are so offensive. I think we skipped a few that would have dramatically increased our probability of being killed.

**Jason:** Well, you can take this one out, boys. I love you, I love you all. I'm going to poker later.

**Elon:** Take care.

**All:** Bye! Love you!