# Agent Coding Tips and Tricks

by popular demand, here are my agent coding tips and tricks that **YOU MUST know or be LEFT BEHIND FOREVER:**

## 1️⃣ The best model is task dependent.

codex 5.2/5.3 has been consistently much better at AI, pytorch, ML. opus 4.5/4.6 is more pragmatic and obviously fast.

at your actual task, model capabilities and styles may be wildly different. figure out what works for you rapidly.

given the above...

## 2️⃣ Dual wield two models in whatever harness works for you.

come up with a workflow where you can shift between models easily when one gets stuck. for me this looks like claude code in the terminal and cursor with codex 5.3.

don't sleep on cursor, it has a very good harness that is battle tested across models. at times where a third model (or a cheaper model like K2.5) is in the arena, it can be very helpful to be able to flip back and forth in a normal agentic chat environment. but also... if you're comfortable with what you use, stick with it. **workflow optimization is the enemy of productivity.** thus...

## 3️⃣ Minimize skills, mcp, rules as much as possible and add them slowly if at all.

i use no skills, no mcp in any of my workflows. treat your context window like a life bar and have respect for the core competency of the models. over time tool use, capabilities will continue to improve and you'll be wasting time explaining skills or tools that can natively be used by the model.

there are exceptions to this and sometimes its fun to experiment with a prompt someone else has made (this is all a skill is). in the long term, i can imagine skills being a great way to, for example, inject some of the latest updates and knowledge of the most recent next js capabilities into a model without that inherent knowledge. or to copy a prompt from someone who has had great results in a particular task. however, generally... **avoid loading up here.**

## 4️⃣ Have something to actually build.

the more time you spend optimizing without a target the less effective you are. the most aggressive breakthrough moments for me were about obsessing over a problem. these are the times that your workflow gets rebuilt, but you will have an actual metric internal to build intuition against: **is all of this actually helping me get things done faster or not?**

## 5️⃣ Add measurement to kill noise.

as "orchestration" methods and other "infinite agent loop" structures re-emerge, treat them all with suspicion. they may work very well for your use case and they can be super fun to try out esp for a side hobby project. but when you're working in production or on a serious goal, try to build some minimal measurement to keep yourself honest. it can feel like you're making progress in the short term very rapidly.

this might as simple as writing down how much time you're actually spending checking in / correcting the bot that's running "autonomously" versus if you just sat down and hand prompted over an hour.

additionally, use straight forward, verifiable tests to better understand if your agents are making progress or not against the goal. very simple, nothing ground breaking but easy to get lost in the sauce with ralph loops etc.

## 🚨 Ignore the noise 🚨

there will always be a **HOT NEW TRICK to OPTIMIZE YOUR PRODUCTIVITY x2.**

ignore them. hate them. banish them. just do work. do more work. every minute you spend watching a youtube tutorial is a minute you could have been screaming at the computer to do its job better.

the models will change, the behaviors will get trained in, orchestration will get trained in. the tips and the tricks of today are not always going to translate.

**build the intuition on what works personally for you now and then use YOUR criteria to judge the next new thing, not someone else's.**

---

**Posted:** 8:53 AM · Feb 8, 2026  
**Views:** 33.7K