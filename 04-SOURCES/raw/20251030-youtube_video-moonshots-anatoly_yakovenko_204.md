# Moonshots with Peter Diamandis: Solana Founder on Crypto's Future

**Host:** Peter Diamandis  
**Panelists:**  
- Dave Blundin (Founder & GP, Link Ventures)
- Salim Ismail (Founder, OpenExO)  
- Dr. Alexander Wissner-Gross (Computer Scientist, Founder of Reified)  
**Guest:** Anatoly Yakovenko (Co-founder & CEO, Solana Labs)

**Context:** Recorded October 21, 2025. Discussion explores Solana's architecture, the convergence of crypto and AI, decentralized finance, and the future of global markets.

---

**Peter:** Hey everybody, welcome to Moonshots. Here with my Moonshot mates Dave Blundin—

**Dave:** Hey Peter.

**Peter:** Hey. Alexander Wissner-Gross—

**Alex:** Hey Peter.

**Peter:** And Salim Ismail. We have a special guest today. We're going to be diving into Solana. Anatoly Yakovenko is here—software engineer, entrepreneur, co-founder and CEO of Solana Labs, which today is the sixth largest coin, now worth over a hundred billion dollars. Congratulations for that.[^1]

**Anatoly:** Yeah, a hundred billion here, a hundred billion there, on your way to a trillion.

**Peter:** Bachelor's in computer science from University of Illinois, Urbana-Champaign. You began your career at Qualcomm—an amazing company. I had a chance to watch their domination. Solana has emerged as the leader in decentralized finance and blockchain, generating 2.2 billion in annual revenues between 2024 and 2025. That's extraordinary.

**Dave:** It's the cool one around MIT, I can tell you that firsthand. You are known and you are cool.

**Anatoly:** That's awesome.

**Peter:** Today I really want to hit on a few things: the crypto essential, Solana 101, what makes it different from Bitcoin and Ethereum. Want to dive into Solana as a use for payments, the everything coin, and then really the convergence of crypto and AI, which is going to cause this explosion in the global economy. Let me begin with a question that is on my mind—given our incredible rush towards AGI, every dollar in the ecosystem is being sucked into this black hole of computronium we're building across the planet. We've got AI, we've got agents, we have Solana, we have stablecoins. What's the future of money going to look like? Do you think it's going to be recognizable in the next 10 years?

**Anatoly:** I think the two things that I see converging is that the cost for intelligence is dropping and markets require intelligence. Because it's now cheaper to have intelligence to analyze all the signal in the world, you can now have a lot more markets. Public permissionless blockchains like Solana allow you to create markets permissionlessly for whatever random thing. You saw this with prediction markets and Polymarket and Kalshi. But the weird, cool experiments like futarchy—where you have decision markets for every decision that a fund or a company can take—those can now exist. And as intelligence gets cheaper, you have more markets that are viable. You see this exponential explosion of everything being decided through market forces, which I think is—it's like the quote I made before the podcast: the ants are not aware of the intelligence of the anthill. I can't fit all these markets in my head or the outcome of this, but my gut is that this is probably the most optimal direction for society to move forward and make decisions. The more market-based it is and the more intelligence you have to make those decisions correctly, and the forcing function of losing money is a good way to course correct when you have bad intelligence. Hopefully it's a good thing, but beyond—I can't fit it all in my head. It's beyond my comprehension.

**Peter:** The speed of change is awesome right now. Alex, we talk about this—Economy 3.0. Economy 1.0 was physical. Economy 2.0 was taking physical industries and digitizing them. Economy 3.0 is a fully digital economy. We're going to see that fully blossom, it sounds like, over the next 10 years.

**Alex:** Yeah. I would say the convergence point here is that as intelligence becomes more and more commoditized, the differentiator becomes the raw materials—the data and the money. And blockchains are the best instruments for moving money at the speed that intelligence can process. So the bottleneck becomes how good is the blockchain at moving money around.

**Salim:** I'm reminded of that fantastic paper by Eric Beinhocker where he talks about the number of stock keeping units as a measure of the complexity of an economy. He goes back through time and shows—Rome had a few thousand. Today we have billions. If you look at what you're saying, the number of potential markets will explode by several orders of magnitude over the next decade because we can parse data in those markets and make decisions.

**Anatoly:** Yeah, and the other crazy cool thing that I totally geeked out over is—one of the questions I've always had is: if you have an AI agent making intelligent decisions and it's wrong, it loses money and then the next agent corrects it. At some point you have to ask, where did the intelligence go? It has to be in the weights, in the compute running this agent. And I think once these things become big enough, I think the intelligence is emerging in the market and it's not in any single agent.

**Dave:** I agree with that.

**Anatoly:** I'm going to go read my Hayek again. It's probably in there somewhere.

**Peter:** I want to ask you a very pointed question, Anatoly. This question comes from—every company I find has to answer two things. One, why does your company exist? And second, why do we need it? In that context, what's Solana?

**Anatoly:** There's a billion people that have access to a smartphone and the internet but don't have access to dollars, US banking or financial instruments. Solana's there to really enable that 1 billion people to go fully interconnected.

**Peter:** But I've heard Bitcoin described as a store of value and Ethereum as a means of settlement. What's Solana?

**Anatoly:** Bitcoin is store of value. Ethereum is settlement. Solana is execution. I just simply wasn't interested in settlement or store of value because they're not the kind of engineering problem that I'm interested in solving.

**Peter:** Is that the future—a single machine layer for all markets everywhere?

**Anatoly:** There's no computer science academic reason why it can't exist. It's purely an engineering problem and we're on our way to solve it as fast as we can.

**Peter:** How long before this science fiction future could come into existence?

**Anatoly:** My gut is—now.

**Peter:** Now? That's a moonshot, ladies and gentlemen.

**Dave:** Totally.

**Peter:** The fact that we now have stablecoin legislation and that people are projecting 1 trillion to 10 trillion worth of digital dollars being minted over the next 5 years is going to massively accelerate things. Let's go back to the beginning. How did the idea for Solana come about? What was the genesis?

**Anatoly:** I was at Qualcomm. I left in 2016. I went to a tiny startup that failed. Then I spent time at Dropbox doing compression. Around the time that I was at the tiny startup, I got into crypto—bought my first Bitcoin, bought my first Ethereum. This was around 2016-2017. I got super excited about it. I was trying to figure out what my project would be. I knew enough about the kind of stuff I did at Qualcomm—that was kernel-level operating systems, distributed systems—that it felt I would be able to do something interesting at the core. Then one weekend I had way too much coffee and ended up staying up until 4 a.m. I suddenly had this breakthrough that I could use time itself as a kind of cryptographic primitive in a way to construct consensus.

**Peter:** Can you explain that? What's this proof of history concept?

**Anatoly:** The simple way to think about it is: Bitcoin's proof of work is basically a clock. It produces blocks every 10 minutes. You can't make the network go faster because of the physics of light. We exist in this one universe. We're not going faster than the speed of light. So Bitcoin is perfectly engineered for a geological timeframe scale—like the tectonic plates moving. That's the perfect thing for it. But if you want people to feel the experience of using a credit card, you have to have something that's a lot faster. The insight was that you can use cryptographic functions themselves to create a source of time. If you could do that, then all the nodes in the network can independently verify time without having to talk to each other. That's the key breakthrough.

**Salim:** That's gorgeous.

**Anatoly:** Yeah. I woke up in the morning and I was drafting the white paper. I was super excited. But I knew enough to be scared. I've seen a bunch of companies burn through millions of dollars in the Bay Area doing blockchain stuff. I didn't want to burn through my life savings and have nothing to show for it. So I went to a good friend of mine, Greg Fitzgerald, who I worked with at Qualcomm. I was like, "Dude, I have this idea. It's really weird. I don't know if it's going to work. Can you code it up in C and I'll code it up in some other language and let's see if we come up with the same results?" He did it in a weekend. We got the same results. Then I was like, "Okay, this is real." Then we started building.

**Peter:** When was this?

**Anatoly:** This was end of 2017. We launched testnet in early 2018. The crypto market crashed. It was terrible. We raised a small seed round. By March 2020 we launched mainnet.

**Peter:** The world shut down.

**Anatoly:** Yeah, COVID hit literally that month. It was crazy.

**Dave:** But that was perfect timing because DeFi summer happened.

**Anatoly:** Yeah. 2020 was DeFi summer. We had the network up and running. People started building on it.

**Peter:** When you're building Solana, what are the design principles? What were you optimizing for?

**Anatoly:** The core thing was: I want this to feel like you're using the internet. When you click on Google, the result comes back fast. When you send a message on WhatsApp, it's instantaneous. I wanted that experience for money. That meant the network had to be fast—really fast. Not 10 minutes or even 10 seconds. We're talking 400 millisecond block times. That's faster than you can blink. Second thing was cost. If you're going to have billions of people using this, transactions have to be cheap. We're talking fractions of a penny. Third was composability. All the applications on Solana can talk to each other in real time. That's what creates the magic. You can have a DEX, a lending protocol, an NFT marketplace—all interacting with each other in a single transaction.

**Alex:** What's the theoretical limit on transaction throughput?

**Anatoly:** So right now we're doing about 65,000 transactions per second on mainnet. But there's no theoretical limit. It's just engineering. With Firedancer—which is the new validator client we're building—we're targeting over a million transactions per second. Eventually we think we can get to tens of millions.

**Salim:** That's insane. For context, Visa does about 1,700 transactions per second.

**Anatoly:** Yeah. And we want to be orders of magnitude beyond that. Because it's not just payments. It's everything. Every market, every interaction, every contract—all of that runs on the blockchain.

**Peter:** Let's talk about DeFi—decentralized finance. This is where a lot of the action is happening on Solana. Can you paint a picture of what DeFi looks like today and where it's going?

**Anatoly:** DeFi is basically rebuilding the entire financial system on-chain. Everything that you do with a bank—lending, borrowing, trading, derivatives, insurance—all of that exists on Solana, but it's permissionless, it's transparent, it's composable. The cool thing is that you don't need permission from a bank or a government to participate. You just connect a wallet and you're in. Today, the biggest DeFi protocols on Solana are doing billions of dollars in volume every day. You've got Jupiter, which is the largest DEX aggregator. You've got Marinade for liquid staking. You've got Kamino for lending. These are sophisticated financial products that used to only be available to institutions, and now anyone with $10 can access them.

**Dave:** And the yields are real. I've been staking SOL. I'm getting 7-8% APY. That's better than anything I can get in TradFi right now.

**Anatoly:** Exactly. And it's not just speculation. It's real economic activity. The network is generating billions in fees. Validators are earning real revenue. It's a functioning economy.

**Peter:** Let's talk about regulation. This is the elephant in the room. We just had stablecoin legislation pass. What does that mean for Solana and crypto broadly?

**Anatoly:** It's huge. For the first time, we have regulatory clarity in the US. That means institutional money can come in. That means banks can custody crypto assets. That means companies can hold digital dollars on their balance sheets. The fact that we now have stablecoin legislation and people are projecting 1 trillion to 10 trillion worth of digital dollars being minted over the next 5 years—that's going to massively accelerate everything. Because now you can do global payments in dollars without touching the banking system. That's transformational.

**Salim:** The geopolitical implications are massive. If you're a country that doesn't have a stable currency, you can now transact in dollars without needing access to US banks. That's huge for financial inclusion.

**Anatoly:** Yeah. And it's not just dollars. You'll have euro stablecoins, yen stablecoins, eventually even synthetic currencies that are baskets of different assets. All of that will run on blockchains like Solana.

**Peter:** Let's talk about trust and how blockchains create trust. Can you explain the Byzantine Generals Problem and how Solana solves it?

**Anatoly:** The Byzantine Generals Problem is this classic computer science thought experiment. Imagine you have a bunch of generals surrounding a city. They need to coordinate an attack. But some of the generals might be traitors who are trying to sabotage the attack. The question is: how do you get consensus when you can't trust everyone? In blockchain terms, it's the same problem. You have thousands of validators around the world. Some might be malicious. Some might go offline. How do you get them all to agree on the state of the ledger? Bitcoin solved this with proof of work—basically making it expensive to be malicious. Solana uses proof of stake combined with proof of history. The proof of history gives you a cryptographic clock that everyone agrees on. Then proof of stake makes sure that validators have skin in the game. If they misbehave, they lose their stake. The combination of these two mechanisms lets us reach consensus really fast without sacrificing security.

**Alex:** The key insight is that time is the ordering mechanism. Once you have a shared notion of time, consensus becomes much easier.

**Anatoly:** Exactly. And that's what proof of history gives you—a verifiable passage of time that's encoded in the blockchain itself.

**Peter:** I want to shift gears and talk about consumer adoption. We've had crypto for over a decade now, but it's still not mainstream. What needs to happen for crypto to cross the chasm?

**Anatoly:** I think we're about to see it. The thing that's going to drive mainstream adoption is stablecoins. Because stablecoins are just better money. If you're in Argentina and your currency is inflating at 100% per year, you want dollars. If you're a freelancer in the Philippines getting paid by a US company, you want to receive payment instantly without paying 10% to Western Union. Stablecoins solve both those problems. And Solana is the best place to use stablecoins because transactions are fast and cheap. I think we're going to see hundreds of millions of people using Solana over the next few years and most of them won't even know they're using a blockchain. They'll just think they're using a better payment app.

**Dave:** I saw a stat that Solana is processing more transactions than all other blockchains combined. Is that right?

**Anatoly:** Yeah, by a lot. We're doing over 90% of all non-bot transactions in crypto. Part of that is because we have real consumer applications. Platforms like Tensor for NFTs, Jupiter for trading, even meme coins—they're bringing in millions of users. And these are real people doing real economic activity.

**Peter:** Speaking of meme coins—that's been controversial. Some people say it's frivolous. What's your take?

**Anatoly:** I think meme coins are fascinating. They're social experiments. They're communities forming around shared narratives. Sure, a lot of them are silly. But they're also bringing people into crypto who would never otherwise care about blockchain technology. And here's the thing—once people have a Solana wallet and they've done a few transactions, they realize how easy it is. Then they start exploring DeFi, they start using stablecoins, they start participating in the real economy. So meme coins are actually an onboarding mechanism. It's like how people got on the internet to share cat photos, but then they stayed for email and e-commerce.

**Salim:** It's brilliant actually. You're gamifying the onboarding process.

**Anatoly:** Yeah. And it's working. We're seeing millions of new wallets created every month.

**Peter:** Let's talk about the victory state. If everything goes right, what does the world look like in 10 years? What's the killer app for humanity?

**Anatoly:** I think the killer app is just global commerce that works. Right now, the financial system is broken. It's slow, it's expensive, it's exclusionary. If you're not in the US or Europe, you're basically locked out of the global economy. In 10 years, I want everyone—no matter where they are—to be able to participate in global markets. I want a farmer in Kenya to be able to sell produce and get paid in stablecoins instantly. I want a developer in Vietnam to build an app and monetize it globally without needing a bank account. I want a small business owner in Brazil to access credit markets without filling out paperwork for weeks. All of that should just work. And it should be as easy as sending a text message. That's the victory state.

**Alex:** That's essentially financial teleportation. You're moving value at the speed of light across the planet.

**Anatoly:** Yeah. And once you have that infrastructure, everything else becomes possible. You can build prediction markets for everything. You can have AI agents transacting on behalf of people. You can have on-chain corporations that are fully autonomous. The possibilities are endless.

**Peter:** Let's dig into that—on-chain corporations and law as code. What does that mean?

**Anatoly:** So right now, companies are these nebulous legal entities. You have articles of incorporation, bylaws, shareholder agreements—all this paperwork. And when disputes happen, you go to court and lawyers argue about what the contract meant. It's slow, it's expensive, it's ambiguous. With smart contracts, you can encode the rules directly into the blockchain. The company exists as code. The governance happens on-chain. The accounting is transparent. Everything is automated. So you could have a company that's incorporated on Solana where the shareholders vote on proposals, the treasury is managed by smart contracts, dividends are paid out automatically—all without any human intermediaries. That's law as code.

**Salim:** That's the ExO model, Peter. That's what we've been talking about—organizations that scale exponentially because they're not bottlenecked by human coordination.

**Peter:** But what about edge cases? What about disputes that the code didn't anticipate?

**Anatoly:** That's where you have governance mechanisms. You can have arbitration protocols on-chain. You can have multisig wallets where trusted parties can intervene in emergencies. The point is not to eliminate all human judgment—it's to minimize the amount of trust you need. Most of the time, the code executes correctly and everyone's happy. In the rare cases where something goes wrong, you have fallback mechanisms. But those should be the exception, not the rule.

**Dave:** The key is that the default state is trustless execution. You're inverting the burden of trust.

**Anatoly:** Exactly.

**Peter:** Let's bring AI into this. We've talked about agents. We've talked about markets. How do you see AI and crypto converging over the next decade?

**Anatoly:** I think AI agents are going to be the biggest users of blockchains. Because agents need money to operate in the economy. If you have an AI that's buying compute, or purchasing data, or hiring other AIs, it needs a way to transact. Blockchains are perfect for that because they're permissionless. The AI doesn't need a bank account. It doesn't need to pass KYC. It just needs a wallet. And once AIs start transacting on-chain, you get this explosion of economic activity. Because AIs can operate 24/7. They can monitor thousands of markets simultaneously. They can execute strategies that humans can't even comprehend. The amount of economic activity that AIs will generate is going to dwarf what humans do today.

**Alex:** This is the Cambrian explosion of intelligence. Once you have autonomous agents with economic agency, the complexity of the system explodes. And the only infrastructure that can handle that is something like Solana.

**Anatoly:** Yeah. And the cool thing is that the AIs will be the ones pushing the network to its limits. They'll be the ones demanding higher throughput, lower latency, more sophisticated smart contracts. So in a way, the AIs will be co-evolving with the blockchain. They'll be the forcing function that makes the technology better.

**Peter:** That's wild. So we're building the infrastructure for machine-to-machine economies.

**Anatoly:** Yeah. And humans will benefit from that because we're part of the economy too. But increasingly, I think the majority of transactions will be between AIs. And they'll be doing it on Solana.

**Salim:** This is the intelligence explosion that Vernor Vinge talked about. Once you have recursive self-improvement, the system just takes off.

**Anatoly:** Yeah. And I don't think we fully appreciate how fast it's going to happen. Because the constraint has always been coordination. Humans are slow. Institutions are slow. But once you have AIs coordinating on blockchains, the speed of change accelerates exponentially.

**Peter:** I want to ask about—going back to your background—you spent a lot of time at Qualcomm working on distributed systems. How much of that experience informed Solana's design?

**Anatoly:** It was critical. At Qualcomm, I worked on operating systems for mobile phones. The constraint was battery life. You had to do a lot with very little power. That taught me how to optimize for efficiency. You can't waste cycles. Every instruction has to count. That mindset carried over to Solana. When you're designing a blockchain that needs to handle millions of transactions per second, you can't afford to be inefficient. Every millisecond matters. So we built Solana like an operating system. It's designed from the ground up for performance. We use things like parallel transaction processing, where multiple transactions can execute at the same time. We use optimizations from high-frequency trading systems. We borrowed ideas from GPU programming. It's all about squeezing the maximum performance out of the hardware.

**Dave:** And that's why Solana feels different when you use it. It's just snappy. There's no lag.

**Anatoly:** Yeah. We wanted it to feel like a real-time system. And that requires obsessive optimization at every layer of the stack.

**Peter:** Let's talk about the network effects. Solana has this growing ecosystem—DeFi protocols, NFT marketplaces, gaming, social apps. How important are network effects in the blockchain space?

**Anatoly:** They're everything. The more applications you have, the more users you attract. The more users you have, the more developers want to build. It's a flywheel. And once you get that flywheel spinning, it's very hard to stop. Ethereum has strong network effects because it was first and it has the most developers. But Solana is catching up fast because we have better performance. And developers want to build on a platform that can actually scale. You can't build a real-time application on a blockchain that takes 10 seconds to confirm a transaction. It just doesn't work. So developers are coming to Solana because it's the only platform where they can build the experiences they want. And once they start building, the users follow. And once the users are there, more developers come. It's a virtuous cycle.

**Salim:** And you're seeing institutional adoption now too. Which is huge.

**Anatoly:** Yeah. Visa is experimenting with Solana. Shopify is exploring payments on Solana. Even traditional finance companies are looking at how they can use the technology. Because the cost savings are undeniable. If you can settle a transaction for a fraction of a penny instead of paying credit card fees, why wouldn't you?

**Peter:** Let's talk about competition. There are other layer-1 blockchains—Ethereum, Avalanche, Sui, Aptos. How do you think about the competitive landscape?

**Anatoly:** I think there's room for multiple winners. Different blockchains will optimize for different things. Ethereum will continue to be strong because of its network effects. But Ethereum is not trying to be a real-time system. They're fine with slower block times because they're optimizing for decentralization and security. That's great for certain use cases. But for real-time applications—payments, trading, gaming—you need something faster. That's where Solana wins. As for the newer blockchains, I think some of them are doing interesting things. But ultimately, what matters is adoption. It's not about having the best technology in a vacuum. It's about having a thriving ecosystem of developers and users. And right now, Solana has that momentum.

**Alex:** Execution is the only moat.

**Anatoly:** Exactly. You have to keep shipping. You have to keep improving the technology. You have to keep attracting developers. The moment you get complacent, someone else will eat your lunch.

**Peter:** I want to ask about decentralization. There's always this tension in blockchains between performance and decentralization. How do you think about that trade-off?

**Anatoly:** I think it's a false dichotomy. The narrative has always been: you can have fast and centralized, or slow and decentralized. But I don't think that's true. Solana has over 3,000 validators. That's more than most blockchains. And we're one of the fastest. The key is engineering. You have to design the system so that validators can keep up with the network even as throughput increases. That means using modern hardware. That means optimizing the code. That means parallelizing everything you can. But it doesn't mean you have to sacrifice decentralization. Now, there is a minimum hardware requirement to run a Solana validator. You can't do it on a Raspberry Pi. But you also can't run a modern data center on a Raspberry Pi. The question is: what's the right trade-off? And I think requiring a decent server to run a validator is a reasonable trade-off if it means the network can serve billions of users.

**Dave:** And the hardware requirements are going down over time as the software gets more efficient.

**Anatoly:** Yeah. Firedancer is going to reduce hardware requirements significantly. So we're actually moving in the direction of more decentralization, not less.

**Peter:** Let's talk about token economics. SOL is the native token of Solana. How does it accrue value?

**Anatoly:** SOL is used for two things. First, it's used to pay transaction fees. Every time you do a transaction on Solana, you pay a small fee in SOL. Half of that fee is burned, which makes SOL deflationary over time. The other half goes to validators as a reward. Second, SOL is used for staking. Validators have to stake SOL to participate in consensus. And users can delegate their SOL to validators to earn yield. So as the network grows and more transactions happen, more SOL gets burned and validators earn more fees. That creates demand for the token. And because there's a fixed supply of SOL, increased demand means price appreciation.

**Salim:** It's a really elegant economic model. The token is directly tied to network usage.

**Anatoly:** Yeah. And the cool thing is that as the network scales, the economics get better. Because the more transactions you have, the more fees are generated, the more SOL gets burned. So the token becomes more valuable as the network becomes more useful. It's a positive feedback loop.

**Peter:** How do you think about valuing SOL as an asset? Is it like equity in a company? Is it a commodity?

**Anatoly:** I think it's closest to equity in the network. You can do a discounted cash flow analysis on SOL the same way you would for a stock. You look at the fees the network generates, you look at the burn rate, you project future growth, and you discount it back to today. Blockworks has done some great analysis on this. They break down revenue, network costs, all of that. And for proof-of-stake networks, you can actually compare the yield to treasury bills. Do I put money in T-bills that are risk-free or do I stake SOL and take some risk but get a higher yield? That's a rational allocation decision. It's the same kind of analysis you do for any income-generating asset.

**Alex:** I'd love to ask a fun question. Let's project forward. Say humanity does in the end take apart our solar system to build a Dyson swarm and we have lots of computronium. What will be the medium of commerce in a Dyson swarm future for humanity?

**Anatoly:** This is kind of the central planning versus market question. Is it computationally feasible to solve resource allocation mathematically without markets at relatively high latencies? You're bound by light speed just like we all are. How many qubits do we have to solve this massive linear algebra problem? Can you allocate resources to everything and you might not need commerce? That might be the end of capitalism and you might only have it for human entertainment. But I think personal freedoms are far more important than efficiency in a lot of ways. I would be very much against central planning. I think it's very important for people to have purpose and competing for tokens—whatever they are, bananas or memecoins. I think that's something.

**Peter:** Here's my question for the group. What's your definition of wealth in the future? Salim, what do you think?

**Salim:** I would think it's a combination of time and health span.

**Peter:** Dave?

**Dave:** I think it's a no-brainer that it's purely tied to compute. I was asking a class at MIT the other day—if I offered you $10,000 cash or a GPU that's worth $30,000, how many of you would take the GPU? They're like, are you crazy? I'll take the $10,000 cash. But in the near-term future, compute can be immediately turned into cash. There, the compute is the universal thing. When you have AI agents who are the laborers of the world, your number of workers is the amount of compute that you have. Your ability to make yourself happy—whether it's controlling your figure robot cleaning your house or building something virtual for your customer—it's all bounded by the amount of compute you have access to. That also determines your health. If you put your compute towards analyzing your scans, it determines whether it finds your cancer. So it becomes the universal foundation.

**Alex:** I think we're suffering from the cliche of blind philosophers touching different parts of the elephant and all being overconfident that the part they're feeling is what an elephant feels like. I'd argue for a more general definition that generalizes all of those definitions. I would argue real wealth will be measured to first order as future freedom of action, which generalizes compute, physical resources. It can be measured in units of bits. It's an information-theoretic definition, but it's not just about compute. It's about the ability—some might call it empowerment—to take the course of action you want in the future, not just in the present.

**Peter:** I knew I should have gone before Alex went. I'll answer—I think it's the ability to fulfill your desires, your purpose. Compute is part of it, but nanotechnology is going to be fundamental as well for manipulation of the physical universe. So it's not just compute in that regard.

**Anatoly:** You're thinking in scarcity terms. You've got to jump forward to abundance terms and think—then all that matters is time and health span.

**Dave:** You're thinking in meatbody terms. Think in post-biological terms.

**Anatoly:** I think you guys are right. Degrees of freedom. Which is—I think people will never feel satisfied because there's somebody else that has more degrees of freedom than them. So this is the human condition, always striving for something else.

**Peter:** The hedonic treadmill spins faster and faster, doesn't it?

**Salim:** Yeah. I think you guys are right because you can have a lot of compute and still be beaten like a dog every day by some government.

**Peter:** We've reached a conclusion here. Anatoly, where do people find you?

**Anatoly:** In the world, on X—A Yakovenko. Follow me on X. I have hot takes, sometimes boring takes, I don't know.

**Peter:** Thank you for the work that you're doing. Thank you for the future that you're enabling for so many globally around the world. The only time more exciting than today is tomorrow, and it's going to be a whopper of a decade ahead. Moonshot mates, I love you all.