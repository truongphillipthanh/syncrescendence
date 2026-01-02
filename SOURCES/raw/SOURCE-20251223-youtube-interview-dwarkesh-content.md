# What Are We Scaling?

I'm confused why some people have super short timelines yet at the same time are bullish on scaling up reinforcement learning atop LLMs. If we're actually close to a human-like learner, then this whole approach of training on verifiable outcomes is doomed.

Currently the labs are trying to bake in a bunch of skills into these models through mid-training. There's an entire supply chain of companies building RL environments which teach the model how to navigate a web browser or use Excel to build financial models. Now either these models will soon learn on the job in a self-directed way—which will make all this pre-baking pointless—or they won't, which means that AGI is not imminent. Humans don't have to go through a special training phase where they need to rehearse every single piece of software that they might ever need to use on the job.

Beren Millidge[^1] made an interesting point about this in a recent blog post. He writes: "When we see frontier models improving at various benchmarks, we should think not just about the increased scale and the clever ML research ideas, but the billions of dollars that are paid to PhDs, MDs, and other experts to write questions and provide example answers and reasoning targeting these precise capabilities."

You can see this tension most vividly in robotics. In some fundamental sense, robotics is an algorithms problem, not a hardware or a data problem. With very little training, a human can learn how to teleoperate current hardware to do useful work. So if you actually had a human-like learner, robotics would be in large part a solved problem. But the fact that we don't have such a learner makes it necessary to go out into a thousand different homes and practice a million times on how to pick up dishes or fold laundry.

Now, one counterargument I've heard from the people who think we're going to have a takeoff within the next five years is that we have to do all this clunky RL in service of building a superhuman AI researcher. And then the million copies of this automated Ilya can go figure out how to solve robust and efficient learning from experience. This just gives me the vibes of that old joke: we're losing money on every sale, but we'll make it up in volume. Somehow, this automated researcher is going to figure out the algorithm for AGI—which is a problem that humans have been banging their head against for the better half of a century—while not having the basic learning capabilities that children have. I find it super implausible.

Besides, even if that's what you believe, it doesn't describe how the labs are approaching reinforcement learning from verifiable reward. You don't need to pre-bake in a consultant's skill at crafting PowerPoint slides in order to automate Ilya. So clearly, the labs' actions hint at a worldview where these models will continue to fare poorly at generalization and on-the-job learning, thus making it necessary to build in the skills that we hope will be economically useful beforehand into these models.

Another counterargument you can make is that even if the model could learn these skills on the job, it is just so much more efficient to build in these skills once during training rather than again for each user and each company. And look, it makes a ton of sense to just bake in fluency with common tools like browsers and terminals. Indeed, one of the key advantages that AGIs will have is this greater capacity to share knowledge across copies. But people are really underrating how much company and context-specific skills are required to do most jobs. And there just isn't currently a robust, efficient way for AIs to pick up these skills.

## The Value of Human Labor

I was recently at a dinner with an AI researcher and a biologist. It turned out the biologist had long timelines, and so we were asking about why she had these long timelines. And then she said, you know, one part of work recently in the lab has involved looking at slides and deciding if the dot in that slide is actually a macrophage or just looks like a macrophage. And the AI researcher, as you might anticipate, responded: look, image classification is a textbook deep learning problem. This is dead center in the kind of thing that we could train these models to do.

I thought this was a very interesting exchange because it illustrated a key crux between me and the people who expect transformative economic impact within the next few years. Human workers are valuable precisely because we don't need to build in the bespoke training loops for every single small part of their job. It's not net productive to build a custom training pipeline to identify what macrophages look like given the specific way that this lab prepares slides, and then another training loop for the next lab-specific microtask, and so on.

What you actually need is an AI that can learn from semantic feedback or from self-directed experience and then generalize the way a human does. Every day you have to do a hundred things that require judgment, situational awareness, and skills and context that are learned on the job. These tasks differ not just across different people but even from one day to the next for the same person. It is not possible to automate even a single job by just baking in a predefined set of skills, let alone all the jobs.

In fact, I think people are really underestimating how big a deal actual AI will be because they are just imagining more of this current regime. They're not thinking about billions of human-like intelligences on a server which can copy and merge all the learnings. And to be clear, I expect this—which is to say I expect actual brain-like intelligences within the next decade or two, which is pretty crazy.

## Economic Diffusion Lag Is Cope

Sometimes people will say that the reason that AIs aren't more widely deployed right now across firms and already providing lots of value outside of coding is that technology takes a long time to diffuse. And I think this is cope. I think people are using this cope to gloss over the fact that these models just lack the capabilities that are necessary for broad economic value.

If these models actually were like humans on a server, they'd diffuse incredibly quickly. In fact, they'd be so much easier to integrate and onboard than a normal human employee is. They could read your entire Slack and Drive within minutes. And they could immediately distill all the skills that your other AI employees have. Plus, the hiring market for humans is very much like a lemons market where it's hard to tell who the good people are beforehand. And so you have to go through this tedious search and interview process and then wait months as the person relocates and finishes up at their previous job.

In contrast, it's much easier for a large company to sign a contract with OpenAI or Anthropic and to integrate AI labor into firms than it is to hire a person. And companies hire people all the time. If the capabilities were actually at AGI level, people would be willing to spend trillions of dollars a year buying tokens that these models produce. Knowledge workers across the world cumulatively earn tens of trillions of dollars a year in wages. And the reason that labs are orders of magnitude off this figure right now is that the models are nowhere near as capable as human knowledge workers.

## Goal-Post Shifting Is Justified

Now you might be like: look, how can the standard have suddenly become labs have to earn tens of trillions of dollars of revenue a year? Until recently people were saying can these models reason, do these models have common sense, are they just doing pattern recognition? And obviously AI bulls are right to criticize AI bears for repeatedly moving these goalposts, and this is very often fair. It's easy to underestimate the progress that AI has made over the last decade.

But some amount of goalpost shifting is actually justified. If you showed me Gemini 2.0 in 2020, I would have been certain that it could automate half of knowledge work. And so we keep solving what we thought were the sufficient bottlenecks to AGI. We have models that have general understanding. They have few-shot learning. They have reasoning. And yet we still don't have AGI.

So what is a rational response to observing this? I think it's totally reasonable to look at this and say: "Oh, actually there's much more to intelligence and labor than I previously realized." And while we're really close and in many ways have surpassed what I would have previously defined as AGI in the past, the fact that model companies are not making the trillions of dollars in revenue that would be implied by AGI clearly reveals that my previous definition of AGI was too narrow.

And I expect this to keep happening into the future. I expect that by 2030, the labs will have made significant progress on my hobby horse of continual learning and the models will be earning hundreds of billions of dollars in revenue a year, but they won't have automated all knowledge work. And I'll be like: look, we made a lot of progress, but we haven't hit AGI yet. We also need these other capabilities. We need X, Y, and Z capabilities in these models. Models keep getting more impressive at the rate that the short timelines people predict, but more useful at the rate that the long timelines people predict.

## RL Scaling

It's worth asking: what are we scaling with pre-training? We had this extremely clean and general trend in improvement in loss across multiple orders of magnitude in compute. Albeit this was on a power law which is as weak as exponential growth is strong. But people are trying to launder the prestige that pre-training scaling has—which is almost as predictable as a physical law of the universe—to justify bullish predictions about reinforcement learning from verifiable reward, for which we have no well-known publicly known trend.

And when intrepid researchers do try to piece together the implications from scarce public data points, they get pretty bearish results. For example, Toby Ord[^2] has a great post where he cleverly connects the dots between the different O-series benchmarks, and this suggested to him that: "We need something like a million-x scale up in total RL compute to give a boost similar to a single GPT level."

## Broadly Deployed Intelligence Explosion

People have spent a lot of time talking about the possibility of a software singularity where AI models will write the code that generates a smarter successor system, or a software plus hardware singularity where AIs also improve their successor's computing hardware. However, all these scenarios neglect what I think will be the main driver of further improvements at top AGI: continual learning.

Again, think about how humans become more capable than anything. It's mostly from experience in the relevant domain. Over conversation, Beren Millidge made this interesting suggestion that the future might look like continual learning agents who are all going out and they're doing different jobs and they're generating value, and then they're bringing back all their learnings to the hive mind model which does some kind of batch distillation on all of these agents. The agents themselves could be quite specialized, containing what Karpathy[^3] called the cognitive core plus knowledge and skills relevant to the job they're being deployed to do.

Solving continual learning won't be a singular, one-and-done achievement. Instead, it will feel like solving in-context learning. Now, GPT-3[^4] already demonstrated in-context learning could be very powerful in 2020. Its in-context learning capabilities were so remarkable the title of the GPT-3 paper was "Language Models are Few-Shot Learners." But of course, we didn't solve in-context learning when GPT-3 came out. And indeed, there's still plenty of progress that still has to be made from comprehension to context length. I expect a similar progression with continual learning.

Labs will probably release something next year which they call continual learning and which will in fact count as progress towards continual learning. But human-level on-the-job learning may take another five to ten years to iron out. This is why I don't expect some kind of runaway gains from the first model that cracks continual learning that's getting more and more widely deployed and capable.

If you had fully solved continual learning drop out of nowhere, then sure, it might be game, set, match—as Sasha put it on the podcast when I asked him about this possibility. But that's probably not what's going to happen. Instead, some lab is going to figure out how to get some initial traction on this problem, and then playing around with this feature will make it clear how it was implemented, and then other labs will soon replicate the breakthrough and improve it slightly.

Besides, I just have some prior that the competition will stay pretty fierce between all these model companies. And this is informed by the observation that all these previous supposed flywheels—whether that's user engagement on chat or synthetic data or whatever—have done very little to diminish the greater and greater competition between model companies. Every month or so, the big three model companies will rotate around the podium, and the other competitors are not that far behind. There seems to be some force—and this is potentially talent poaching, it's potentially the rumor mill in SF, or just normal reverse engineering—which has so far neutralized any runaway advantage that a single lab might have had.

---

*Note: All preview content, advertising, and promotional material has been removed from this transcript. The content begins at its natural intellectual starting point.*

[^1]: **Author**: Beren Millidge is a researcher working on AI and machine learning. His blog post "Most Algorithmic Progress is Data Progress" is referenced in the original video description.

[^2]: **Author**: Toby Ord is a philosopher and researcher. His post "How Well Does RL Scale" is referenced in the original video description.

[^3]: **Person**: Andrej Karpathy, former Director of AI at Tesla and founding member of OpenAI, known for his work on deep learning and AI architectures.

[^4]: **Model**: GPT-3 (Generative Pre-trained Transformer 3) was released by OpenAI in 2020 and demonstrated significant few-shot learning capabilities.
