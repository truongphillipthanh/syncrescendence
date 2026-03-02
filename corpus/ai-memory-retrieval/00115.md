# Few things are worth building

(Description: A dramatic landscape painting depicting a solitary figure standing on rocky terrain overlooking turbulent ocean waves crashing against dark cliffs. The sky is moody and overcast, creating an atmosphere of contemplation and challenge.)

The cost of integrations and simple CRUD software glue has collapsed to near zero. Anyone can wire together an app doing some API calls in minutes.

So what's left worth building?

## The new user

Every major platform shift rewrote software stacks. Mobile put a computer in every pocket. Cloud made software elastic. Each shift was massive. But the user of the software was still human. This shift is different. The user of software is changing.

People largely underestimate the software and infrastructure implications of this new user. It's not a simple workload change. It's a user change. We wrote more about this in [The case for a new retrieval engine for agents](https://blog.hornet.dev/the-case-for-a-new-retrieval-engine-for-agents).

## The survival math

Steve Yegge recently published [Software Survival 3.0](https://steve-yegge.medium.com/software-survival-3-0-97a2a6255f7b), describing which software will survive when agents can build anything on demand. His model is simple: software survives if it saves cognition. A few passages stood out to me:

> You can find problem spaces that will thrive by looking at what will change when agents are doing all the work. For instance, code search gets harder, as LLMs start producing 10x-100x as much code. Agents will need good search as much as humans ever did, and grep, for all its charms, does not scale.

And:

> Agent UX is incredibly important and I think most people are sleeping on it. You want your tool to be intuitive to agents. Not because you documented it really well; that's not ideal. Ideally, your tool is either very similar to other tools they already know, or else it solves a problem exactly the way they like to think about it.

This aligns with how we think about Hornet. We're building something that would be crazy to re-synthesize: a retrieval engine with decades of hard-won search knowledge compressed into it, running on a cheaper substrate than model inference, solving a universal problem that every agent will face. Access to relevant context to get the work done. Search workloads aren't going away. It's exploding.

## Agent DX Is everything

When we launched Hornet's API, we faced a problem: our API surface isn't in any LLM's pre-training data. The obvious approaches, injecting documentation and hoping for in-context learning, didn't work well enough.

So we made the API verifiable. Every interaction returns structured feedback. Agents can write a query, observe the failure, read the error, and self-correct. The same loop that makes coding agents work.

The result: agents configure, deploy, query, and optimize their own retrieval engine. They improve the quality of their own context, which improves their reasoning, which lets them tune retrieval further. The loop becomes self-reinforcing.

This is what Agent DX means in practice: interfaces that work the way agents have been trained (RL). We go deeper on the technical approach in [How we build a retrieval engine for agents](https://blog.hornet.dev/how-we-build-a-retrieval-engine-for-agents).

## Few things are worth building

Building distributed retrieval infrastructure is hard. It's also one of the few things left that are worth doing.

Glue is easy now. Anyone can connect APIs. Anyone can wrap an LLM call. The barrier to shipping something has never been lower. But that's exactly why most of it won't survive.

The value of a 10K lines python library is close to 1$ in 2026. It's generated on-demand on the fly to match exactly whatever the agent needs to get work done. When agents can synthesize wrappers on demand, the wrappers will disappear.

### What survives?

- Systems that compress hard-won insights agents would have to rediscover at enormous token cost
- Systems that operate on a cheaper substrate than inference
- Systems that solve hard universal problems agents can't route around easily
- Systems built for how agents actually work, not how we wish they worked

Retrieval infra is all of these. Agents will always need relevant context to get work done. The new user of software issue more queries than humans ever did. And the decades of knowledge required to build a scalable retrieval engine, ranking, indexing, distributed systems cannot be vibed into existence (yet).

That's why we're building [Hornet.dev](https://hornet.dev/).

---

Jo Kristian Bergum, CEO, [@HornetDev](https://x.com/@HornetDev)

**Posted:** 7:20 AM · February 3, 2026  
**Views:** 89.2K  
**Engagement:** 8 replies, 34 reposts, 237 likes, 529 bookmarks