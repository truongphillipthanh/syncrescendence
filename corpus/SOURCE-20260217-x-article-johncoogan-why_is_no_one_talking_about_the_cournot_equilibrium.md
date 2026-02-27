# Why Is No One Talking About the Cournot Equilibrium?
(Description: A podcast screenshot featuring a man wearing glasses and a blue cardigan, seated in front of a microphone. To his left is a large "f" logo with a glowing green dot. Behind him is a wooden-paneled wall, geometric patterns, and professional recording equipment. A "RODE" microphone is visible in the background. TBPN branding appears at the bottom right.)
## Introduction
Well, Dario and Dwarkesh are [talking about the Cournot equilibrium](https://www.youtube.com/watch?v=n1E9IZfvGMA), and [a bunch of other people too](https://x.com/hypersoren/status/2023197978740285576), but not enough people are talking about it, and there's a lot worth digging into here. The phrase "[Cournot equilibrium](https://en.wikipedia.org/wiki/Cournot_competition)" is old. The guy who coined it, Antoine Augustin Cournot, died 150 years ago. The basic idea is that if there are only a few players in a given market, and they aren't competing on price, they will compete on supply. They will try and predict what their competitors are going to do, then respond accordingly.
## The Podcast Exchange
From Dwarkesh's podcast with Dario:
**Dwarkesh Patel**
> So you laid out a model where Anthropic makes profit because it seems like fundamentally we're in a compute-constrained world. So eventually we keep growing compute—
**Dario Amodei**
> I think the way the profit comes is… Again, let's just abstract the whole industry here. Let's just imagine we're in an economics textbook. We have a small number of firms. Each can invest a limited amount. Each can invest some fraction in R&D. They have some marginal cost to serve. The gross profit margins on that marginal cost are very high because inference is efficient. There's some competition, but the models are also differentiated.
>
> Companies will compete to push their research budgets up. But because there's a small number of players, we have the… What is it called? The Cournot equilibrium, I think, is what the small number of firm equilibrium is. The point is it doesn't equilibrate to perfect competition with zero margins. If there's three firms in the economy and all are kind of independently behaving rationally, it doesn't equilibrate to zero.
## Historical Context: Nash and Game Theory
Even though the Cournot model is from 1838, it wasn't until 1950 that John Nash generalized it with the concept of the "[Nash equilibrium](https://en.wikipedia.org/wiki/Nash_equilibrium)." Now, the prisoner's dilemma is pretty common knowledge, but it's interesting to see it play out in the world of tech, where we're much more used to talking about the impacts of network effects and zero-marginal-cost goods.
## Two Businesses Inside Frontier Labs
So what's actually going on right now with the big AI labs? There are basically two businesses hiding inside every frontier lab. They share a brand and a bunch of data centers, but you should model them separately to understand the risks and rewards of this category.
### First: Model Training
You have training of the models. Labs make an upfront investment in a training run that creates a particular model generation. That asset depreciates as the frontier moves. When a newer, better model is released, customers shift spend to that, and cheaper open-source models commoditize older versions.
### Second: Inference Factory
You have the inference "factory," which is essentially a manufacturing business. Your variable costs are GPUs, power, engineering overhead, etc. Your revenue is subscriptions, API usage, and enterprise contracts.
When you just look at inference, you see a positive contribution margin, so labs usually look great on the previous training run, but terrible on the next one. The reason for all the talk about an AI bubble popping and wreaking economic havoc is that the frontier is hard to predict, especially from outside of a lab, and everyone needs to balance the amount of recurring cash flow to pay for those depreciating assets (training runs).
## Cournot Equilibrium in Action
The Cournot equilibrium comes in when a small number of labs (oligopoly) effectively choose supply at the frontier level and then the market clears at a high price for frontier access.
Choosing "supply" in this case means how many data centers get built, how many GPUs get ordered, etc., but also how much low-latency capacity is allocated to the top tier, how aggressively rate limits are applied, and how much capacity is reserved for enterprise.
On the true frontier, there aren't great substitutes, so price stays high based on customers' willingness to pay for frontier access. Put simply, there are just a ton of developers and knowledge workers who are happy to pay hundreds of dollars a month (or more) but they always want the best available model.
## The Future: From Cournot to Bertrand Competition
Now the big question is about "final models." If we are "near the end of the exponential," as Dario puts it, then you'll see more competition in the market. Customers will switch more quickly to cheaper models to cut costs, and the AI lab oligopoly drops out of Cournot equilibrium.
The most likely next model is [Bertrand competition](https://en.wikipedia.org/wiki/Bertrand_competition), which doesn't mean profits go to zero, it more likely looks like the current hyperscaler cloud market. Capacity is still finite, models become differentiated in quality, latency, safety, enterprise tooling, etc. You wind up with a small number of vertically integrated firms, which resembles the AWS/Azure/GCP dynamic.
## Strategic Implications
In this scenario, OpenAI's recent moves make a lot of sense. Cerebras offers a differentiated product around speed. Peter Steinberger helps build agent orchestration products that route to particular models. Frontier digs deeper into the enterprise. There's still a Cournot game of chicken around who will invest the most in advancing the frontier, but the end state looks a lot more durable than pure model commoditization and the perfectly competitive situation that many were predicting a few years ago.
---
This is my daily op-ed, which goes out in TBPN's morning newsletter, along with the day's guest lineup, news headlines, and top posts.
Sign up to get it in your inbox - instead of randomly finding it in your feed - at [TBPN.com](https://t.co/hZNDLorAvM).
**Post metadata:** 10:51 AM · Feb 17, 2026 · 76.7K Views · 23 Replies · 26 Reposts · 313 Likes · 363 Bookmarks