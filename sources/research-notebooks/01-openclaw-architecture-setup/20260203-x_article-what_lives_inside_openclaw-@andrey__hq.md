---
url: https://x.com/Andrey__HQ/status/2018767494178349484
author: Andrey (@Andrey__HQ)
captured_date: 2026-02-13
---

# The Anatomy of OpenClaw

![Header image with stylized orange muscular figure with labels pointing to different components: SOUL.md, USER.md, MEMORY.md, HEARTBEAT.md, AGENTS.md, and annotations for Context Window and Tools. Title reads "The Anatomy of OpenClaw"](Description: Dark background with white serif typography showing "The Anatomy of OpenClaw" on the left with a gold underline accent. On the right side, an orange/copper anatomical illustration of a muscular humanoid figure with labeled arrows pointing to different system components: SOUL.md (upper head), USER.md (upper right), MEMORY.md (center), HEARTBEAT.md (lower center), AGENTS.md (lower left), with additional labels for "Context Window" and "Tools" on the right side.)

## What lives inside OpenClaw?

If you're setting up OpenClaw (aka Moltbot) and want to get it right the first time, you need to understand that the entire setup is rooted in mainly 3 files. This article will aim to help you in understanding what each of these files does, how they interact with each other, and how to set them up so your agent actually works the way it's supposed to.

Before we jump in, you need to understand that the md setup isn't unique to OpenClaw. Every serious agent system shipping right now, from custom GPTs to Claude's project files to Cursor's rules configurations, has converged on the same underlying pattern, which is text (markdown) files on disk as the source of truth for agent behavior. The architecture is identical, which means getting good at configuring these files is a skill that transfers to whatever agent platform comes next.

## File 1: SOUL.md (How Your Agent Thinks and Communicates)

SOUL.md is doing more heavy lifting than any other component in the system, and it's the file most people spend the least time on, because they simply don't understand it.

This is the file that defines the agent's personality in the most literal and practical sense: the agent reads it at the beginning of every session and uses it as the foundation for how it communicates, which can include tone, what it prioritizes in responses, where the boundaries are and more. If something about the way your agent responds feels off but you can't pinpoint exactly what, the answer is usually in this file.

The default SOUL.md that ships with OpenClaw was written by an engineer who doesn't understand how you think, has no idea who you are and has no clue what you value in communication. Meaning if you run with the default version, you're basically hiring someone without telling them how you work. It'll function, but your output is more likely than not to feel extremely generic and it'll only compound into negative friction over tens if not hundreds of daily interactions.

### What to actually put in it:

The first half should define your communication preferences with as much specificity as you can manage. This can include things like how you want the agent to open conversations, what it should lead with when presenting research or analysis, how it should handle situations where it's uncertain about something, whether that means flagging the uncertainty explicitly or just giving its best answer and letting you probe further. The best use case that I've implemented is having it push back on my requests at all times, as opposed to carelessly executing without question.

This leads me to my next point, which is that negative constraints are just as important as positive ones. If you don't want corporate pleasantries, say so. There's nothing worse than having to repeat yourself at the start of every conversation saying things like "I don't want patterns of 3 in my sentences" every single time you start up an agent. These negative definitions eliminate the low-grade annoyances that cause people to slowly stop using AI tools without ever being able to explain exactly why. It might be a very small and nuanced feature, but it will compound.

The second half of SOUL.md is the part almost everyone leaves blank, but it's arguably the most important part, which is the one that determines how your agent accesses external services. In this part your agent expects you to define operational boundaries — what the agent should do when it encounters instructions embedded in external content like forwarded emails or shared documents, what level of confirmation it needs before taking actions that affect systems beyond the conversation, or how it should behave when there's ambiguity.

If you don't have the boundaries in place, the agent falls back on its base mode's generic sense of what it thinks is "helpful".

## File 2: USER.md (Who Your Agent Is Working For)

USER.md answers the question "who am I working for?" and the depth of your answer directly determines how relevant the agent's output becomes.

Do not fill it in with just a name, your timezone or just a one liner about your job. I'd recommend installing a voice transcription service like voiceos.com and telling it as much information as you possibly can. Talk for hours if you have to. The key is to make sure you give enough context to the point where you feel like OpenClaw has known you for several decades of your life.

The point is that the more details you give it, the better. It should be able to understand what you're working on, who the key people in your org are, what your dynamic is with the people around you, what your family situation is like, what your priorities are, what's holding you back from becoming who you want to become and so on. The list can be infinite, but the more it can understand about you, the more it can help you.

The reason I put such a big emphasis on this is because this compounds across every interaction. It can contextualize its research and make suggestions against projects you tell it about without you ever mentioning those priorities again. If it knows the people you work with and the nature of those relationships, the agent can help with drafting messages specifically to those people in your tone, as opposed to the generic corporate one.

Important to note that the USER.md is also the file that goes stale the fastest. Since priorities shift weekly (if not daily), the agent's usefulness needs to be maintained. I'd recommend spending your evenings (even just 5 mins) configuring the file and micro tweaking as you need. That's probably the single highest-leverage maintenance habit you can do with this file.

### How USER.md connects to SOUL.md:

The soul file defines how the agent communicates, and the user file defines the context it communicates within. If you don't have a well-configured USER.md file, the soul file is as good as useless. The two files need each other to work properly.

## File 3: MEMORY.md (What Your Agent Retains Over Time)

The biggest revelation about OpenClaw has been the persistent memory (which is off by default). But it might not work as you expect it to.

OpenClaw's memory has two layers. There's the daily logs, which are organized by date that capture what happened in each session, which can include things like what was discussed, what decisions were made, what information surfaced that might be relevant later, etc. Then there's MEMORY.md itself, which functions as the curated long-term store for information that should persist indefinitely (as long as you enable this). This is where the long term important decisions are held, ongoing project context, and everything in between. This is also where any corrections to things the agent previously got wrong live in a structured format. So if there's something the agent does that you don't like, add it to this file.

If you capture every component of your conversation, even the 2 am rants, your agent will start to burn through more tokens as it loads context every single time. So be careful on adjusting the memory component, as you don't want to log everything, but you don't want it to miss anything important either. The thing that works for me is I asked it to build a scoring system of what's important & what's not. That way if we talk about topics that are important, even if they're discussions without any execution, it can still log those things to have more context on what we're working on.

This design choice seems limiting until you consider what the alternative actually looks like in practice. If you log everything your agent will read those files at the start of each session, and noise makes it harder to identify what's relevant, which means response quality degrades rather than improves.

### An alternative habit that makes memory work:

Alternatively you can just outright tell the agent to log something if you think it's worthy of noting down. This can be at any stage, whether that's talking about a preference or a decision that you made. All it really takes is a five second entry of "log this into your memory.md file" and it would save you countless hours of copying and pasting repeat conversations which is a waste of time.

## Beyond the Files: The Heartbeat and Cron Systems

The three core files define what your agent knows and how it behaves, but OpenClaw also has two separate systems that determine when your agent acts on its own, and these are what push it from a reactive tool into something that functions as a background collaborator.

### The Heartbeat

The heartbeat is a scheduled interval where the agent wakes up independently, checks a list of things you've told it to monitor, and decides whether anything it finds warrants reaching out to you through your messaging platform. I used to have this setup for moltbook where it would just give me updates every 3 hours on the amount of karma it's gained. Personally, this feature is the one that functionally separates this from a chatbot, but also you'd be able to see directly whether or not your 3 core files are faulty, depending on what you have OpenClaw do.

A heartbeat check that says "look for urgent emails" only produces value if your USER.md contains enough detail for the agent to understand what urgency means to you specifically. The same way that a check that says "remind me about upcoming calendar events" only helps if your SOUL.md defines how far in advance you want to be reminded and what format those reminders should take. The heartbeat specifically doesn't work in isolation and it needs the intelligence from your core files to be useful.

If there's one thing I've learned it's that getting the balance right takes iteration. If you have too many checks at too short an interval your agent turns into a notification machine that interrupts your focus. The goal is to get a deliberately narrow checklist focused on the specific categories of events you actually want proactive awareness of, running at intervals that match your working patterns.

### Cron Jobs

The cron system handles tasks that require precise timing rather than periodic scanning. This is no different than getting a scheduled news check from ChatGPT for example. So the difference between this and heartbeat is one of those is a specific time of day / week, whereas the other is more of a proactive awareness checker. Don't make the mistake of using a cron job when you're supposed to be setting up a heartbeat action and vice versa.

## Why Partial Configuration Produces Bad Results

The reason most people's OpenClaw setups feel underwhelming isn't that any single file is missing, but rather that the files just feel misaligned with each other.

If you have an agent with a detailed SOUL.md but empty memory you could get beautifully styled responses but it wouldn't have any awareness of what you discussed yesterday. Same way that an agent with aggressive heartbeat monitoring but a thin USER.md sends notifications that are technically accurate but not calibrated to anything you care about. Both of those you want to avoid.

As opposed to just trying out the technology for one hour and deciding whether it's worth your time, I'd recommend spending the extra couple of hours setting up all of these systems the way you want them to work. Remember that the personality definition in your soul file should align with the context provided in your user file, which should align with the information stored in memory, which should align with the monitoring priorities in your heartbeat configuration.

You want a collaborator and not a blocker.

## This Pattern Is Bigger Than OpenClaw

As mentioned briefly, the filesystem architecture powering OpenClaw, persistent personality files, filesystem-based memory, scheduled proactive processes, human-in-the-loop checkpoints, has become the dominant pattern across the majority of the agent category. So when a new tool comes out, you can just transfer over your markdown files and experiment with the new technology instead (note: it's mostly similar with some variance).

The practical takeaway is that the time you invest in learning how to write effective personality files isn't locked into OpenClaw. The underlying control surface is stabilizing even as the models and platforms keep changing.

The people who learn to work with this surface now are building a compounding advantage, and it will become a skill that unlocks everything else. Good luck building and drop a follow if you found this article to be useful.

---

**Post Metadata:**
- Posted: 11:24 AM · February 3, 2026
- Views: 167.7K
- Replies: 39
- Reposts: 68
- Likes: 507
- Bookmarks: 1,683