# We need to solve multi-agent collaboration

(Description: A visual diagram titled "The primitives" showing four connected boxes with colored borders arranged horizontally. From left to right: a yellow-bordered box labeled "Agents", a blue-bordered box labeled "Cloud runners", an orange-bordered box labeled "Message passing", and a green-bordered box labeled "Persistent storage". Plus signs (+) connect each box sequentially.)

I recently wrote about how [this year development will move to the cloud](https://x.com/zachlloydtweets/status/2019877685980196937) because agents need to scale off of our laptops.

Moving to the cloud solves our scaling problem, but I've also been thinking about how to solve the orchestration problem. Or more concretely, agent collaboration as a "team" to work on hard coding projects.

We've seen many different approaches pop up in the wild, most recently with the "team of agents" concept in Claude Code, independent agents self-organizing in OpenClaw, and more bespoke orchestrators like Gastown running on your machine.

Many approaches are going to be viable... but today, there's no clear winner on how to orchestrate coding agents working as a team. That's why I'm less interested in finding the perfect orchestration pattern, and much more interested in getting the primitives right for the community to test these different approaches.

## What primitives do we need?

The primary challenge for teams of agents is setting an established communication pattern, and tracking their memory as they work. Ideally, this line of communication should be model-agnostic too.

Agents, like humans, need a way of talking, expressing goals, tracking progress, etc. We humans have built a huge amount of software to solve these problems for knowledge workers – e.g. Slack, Notion, Zoom, CRMs, ERPs – and agents will probably have analogous tools, albeit ones that operate at higher speed and scale and without all of the UI bells and whistles that people need.

So should we be building Slack, Notion, and Zoom for agents right now? Should agents just use the tools we have already built?

I'm not in favor of that approach at the moment – it's anthropomorphizing agents too much and not playing to their strengths. Instead, I would focus much more on the minimal underlying infrastructure that's actually needed for these alien brains to do work.

By underlying infrastructure, I mean:

- **Cloud operations** – if you want agents reliably communicating at scale, you can't rely on local compute – agents need secure cloud sandboxes that they can scale themselves. [If you're convinced local worktrees are a better solution, I push back on that here.](https://x.com/zachlloydtweets/status/2019877685980196937)

- **An easy, reliable way for agents to communicate with each other** – agents need to talk and exchange information. This could be a message bus, a distributed inbox, etc.

- **Some persistent datastore** – agents need to track work, put their output somewhere, and remember it. This could be as simple as a distributed file system with locking, or it could be git.

- **A powerful coding agent** – I think coding agents are going to be the foundation of all knowledge work, because coding is the "uber" skill that allows agents to do anything.

- **A human-agent interface** - human teammates need to easily hop in and steer agent work, review artifacts, provide new goals, etc.

With Warp's recent launch of [Oz](http://oz.dev/), we are starting on these primitives in earnest, and already have a bunch of what you need: [cloud native agents](https://docs.warp.dev/agent-platform/cloud-agents/managing-cloud-agents) with coding capabilities and persistent records of their work, where humans can [always take the wheel with live sessions](https://x.com/warpdotdev/status/2021247671336366482).

As for agent memory, we have a cloud storage solution called [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive) that can be made more agent-accessible. This would allow agents running in different isolated sandboxes to share a common data store.

With these primitives in place, we can start experimenting with all sorts of different communication protocols on top of them.

Of course, we are still missing a lot here. We're just providing the building blocks watching what patterns the community builds. I encourage you to stretch the limits of the Oz platform to build your own multi-agent patterns. We'll be doing the same!

---

**Post metadata:** 7:46 AM · Feb 13, 2026 · 14.1K Views · 14 Replies · 16 Reposts · 150 Likes · 249 Bookmarks