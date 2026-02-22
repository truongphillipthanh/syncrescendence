---
url: https://x.com/karpathy/status/2024583544157458452
author: "Andrej Karpathy (@karpathy)"
captured_date: 2026-02-21
id: SOURCE-20260219-021
original_filename: "20260219-x_thread-very_interested_in_what_the_coming-@karpathy.md"
status: triaged
platform: x
format: thread
creator: karpathy
signal_tier: paradigm
topics:
  - vibe-coding
  - debugging
  - git
  - api
  - product-development
  - cli-tools
teleology: synthesize
notebooklm_category: ai-engineering
aliases:
  - "Highly Bespoke Software Era"
synopsis: "Highly Bespoke Software Era Very interested in what the coming era of highly bespoke software might look like. Example from this morning - I've become a bit loosy goosy with my cardio recently so I decided to do a more srs, regimented experiment to try to lower my Resting Heart Rate from 50 -> 45, over experiment duration of 8 weeks."
key_insights:
  - "But I still feel like the overall direction is clear: 1) There will never be (and shouldn't be) a specific app on the app store for this kind of thing."
  - "I shouldn't have to look for, download and use some kind of a "Cardio experiment tracker", when this thing is ~300 lines of code that an LLM agent will give you in seconds."
  - "It shouldn't maintain some human-readable frontend and my LLM agent shouldn't have to reverse engineer it, it should be an API/CLI easily usable by my agent."
---
# Highly Bespoke Software Era
Very interested in what the coming era of highly bespoke software might look like.
Example from this morning - I've become a bit loosy goosy with my cardio recently so I decided to do a more srs, regimented experiment to try to lower my Resting Heart Rate from 50 -> 45, over experiment duration of 8 weeks. The primary way to do this is to aspire to a certain sum total minute goals in Zone 2 cardio and 1 HIIT/week.
1 hour later I vibe coded this super custom dashboard for this very specific experiment that shows me how I'm tracking. Claude had to reverse engineer the Woodway treadmill cloud API to pull raw data, process, filter, debug it and create a web UI frontend to track the experiment. It wasn't a fully smooth experience and I had to notice and ask to fix bugs e.g. it screwed up metric vs. imperial system units and it screwed up on the calendar matching up days to dates etc.
But I still feel like the overall direction is clear:
1) There will never be (and shouldn't be) a specific app on the app store for this kind of thing. I shouldn't have to look for, download and use some kind of a "Cardio experiment tracker", when this thing is ~300 lines of code that an LLM agent will give you in seconds. The idea of an "app store" of a long tail of discrete set of apps you choose from feels somehow wrong and outdated when LLM agents can improvise the app on the spot and just for you.
2) Second, the industry has to reconfigure into a set of services of sensors and actuators with agent native ergonomics. My Woodway treadmill is a sensor - it turns physical state into digital knowledge. It shouldn't maintain some human-readable frontend and my LLM agent shouldn't have to reverse engineer it, it should be an API/CLI easily usable by my agent. I'm a little bit disappointed (and my timelines are correspondingly slower) with how slowly this progression is happening in the industry overall. 99% of products/services still don't have an AI-native CLI yet. 99% of products/services maintain .html/.css docs like I won't immediately look for how to copy paste the whole thing to my agent to get something done. They give you a list of instructions on a webpage to open this or that url and click here or there to do a thing. In 2026. What am I a computer? You do it. Or have my agent do it.
So anyway today I am impressed that this random thing took 1 hour (it would have been ~10 hours 2 years ago). But what excites me more is thinking through how this really should have been 1 minute tops. What has to be in place so that it would be 1 minute? So that I could simply say "Hi can you help me track my cardio over the next 8 weeks", and after a very brief Q&A the app would be up. The AI would already have a lot personal context, it would gather the extra needed data, it would reference and search related skill libraries, and maintain all my little apps/automations.
TLDR the "app store" of a set of discrete apps that you choose from is an increasingly outdated concept all by itself. The future are services of AI-native sensors & actuators orchestrated via LLM glue into highly custom, ephemeral apps. It's just not here yet.
(Description: A dark-themed dashboard titled "RHR 50 -> 45 Experiment" spanning 8 weeks from zone 2 + HIIT plan. The dashboard displays tracking metrics with columns for TOTAL Z2 (83m), TARGET (1630m), WEEKS DONE (0/1), HIIT WEEKS (0/1), and WEEK (1 of 8). A weekly breakdown shows Week 1 (Feb 18-Feb 24) with Zone 2 and HIIT tracking, displaying 83m completion with 97m 22 left needed for HIIT. Weeks 2-8 show planned tracking periods with upcoming status, each with target minute ranges (200-230m, 220-260m, 160-200m, 230-270m, 280-300m, 240-290m, 150-190m respectively).)
**Metadata:**
- Posted: 12:35 PM · Feb 19, 2026
- Views: 1.6M
- Engagement: 851 replies, 1.2K reposts, 11K likes, 7.5K bookmarks