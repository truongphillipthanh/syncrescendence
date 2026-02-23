---
url: https://x.com/Jacobsklug/status/2019768290336453024
author: "Jacob Klug (@JacobsKlug)"
captured_date: 2026-02-14
id: SOURCE-20260206-035
original_filename: "20260206-x_thread-ive_used_openclaw_for_a-@jacobsklug.md"
status: triaged
platform: x
format: thread
creator: jacobsklug
signal_tier: strategic
topics: [ai-agents, automation, opinion, case-study]
teleology: extract
notebooklm_category: ai-agents
aliases: ["Jacob Klug - Honest OpenClaw Review"]
synopsis: "Candid one-week review of OpenClaw covering both genuine value (cross-tool orchestration, daily briefs reducing cognitive load) and real friction: memory degradation over days, huge planning-over-execution bias, ~$100/day API costs, 4-hour painful setup, and failure when trying to build a self-managing AI OS. Concludes by moving the OS to Lovable with OpenClaw as orchestration layer on top."
key_insights: ["Cross-tool orchestration is the real unlock — chat may become the main interface for software, with apps becoming databases + execution layers", "OpenClaw has a huge planning > execution bias — you can easily spend hours discussing work instead of shipping, and creators are overselling the autonomous employee angle", "Cost reality: ~$100/day in Claude credits with unclear ROI, and long-term memory still degrades requiring constant re-prompting of basic context"]
---
# Honest Breakdown: One Week with OpenClaw

i've used @openclaw for a week. there's a lot of noise out there. here's the honest breakdown.

## first, what's genuinely cool

**conversational memory is pretty solid (at first)**

it actually *feels* like it understands your business + life context.

closer to talking to an operator / chief of staff than prompting a chatbot.

**BUT…**

it degraded over time. after a few days i kept having to remind it of obvious stuff.

still feels more human than raw chat interfaces though. just not persistent enough yet.

## cross-tool orchestration is the real unlock

this part got me excited.

i had it running across:
- typefully → post scheduling
- notion → docs / content systems
- slack → team comms
- misc internal workflows

it reinforced something i'm becoming more convinced of:

**chat might actually become the main interface for software.**

apps turn into databases + execution layers
conversation becomes the control panel

sounds theoretical until you actually run it. then it clicks.

## daily briefs / accountability = lowkey underrated

i had it sending:
- daily summaries
- reminders
- blockers
- loose planning nudges

not revolutionary… but noticeably reduced mental load. felt like a slightly chaotic but very eager assistant.

## where it still struggles

**long-term memory is shaky**

biggest friction for me. it would randomly forget:
- tools it had access to
- api permissions
- systems we already built
- context that felt extremely obvious

i restructured memory + optimized storage which helped a bit… but it still trips sometimes.

feels like solving this is one of the biggest unlocks for agent products.

## huge planning > execution bias

this one surprised me.

you can VERY easily spend hours discussing work instead of shipping work.

yes it *can* execute tasks
no it is not autonomous employee level yet

a lot of creators are overselling that angle imo. feels like engagement farming sometimes.

it still needs direction + guardrails + supervision.

## localhost setup = early adopter tax

if you're non technical… this will probably be painful right now.

my setup took ~4 hours. ran into:
- config weirdness
- rate limit nonsense
- api debugging
- random integration hiccups

even after setup, day one felt like debugging > productivity. this will improve, but worth being honest about current UX.

## trying to make it build its own AI OS was… rough

i tried using it to manage:
- tasks
- content
- memory
- workflow dashboards
- basically run my personal + company operating system

it struggled hard with consistency. sometimes it straight up forgot the system existed. had to re-prompt basic changes constantly.

i eventually moved the OS into @lovable and now use openclaw as orchestration layer on top.

that combo feels much stronger so far. will share full stack later.

## cost is very real

my usage is burning roughly ~$100/day in claude credits right now.

not clearly ROI positive yet.

you can definitely optimize with cheaper models… but people should go in with eyes open.

## overall take

this is absolutely a step forward. i'm glad i adopted early.

there was definitely that first wave of "holy shit this changes everything"

it doesn't. but it DOES move the needle in a meaningful way.

not AGI yet (sorry @alexfinn lol).

**ALSO worth saying:** this is extremely early software. if i re-read this in 2-3 months it'll probably age badly (in a good way).

agent tooling is moving stupid fast.

and credit where it's due —@steipete built something genuinely important here and sparked a movement around agent-native workflows.

that's hard to do. deserves respect.

---

anyways. if you're building with agents right now, you're early. and early is usually where leverage lives.

i'm gonna keep testing, breaking, and shipping around this stack and share honest notes as i go.

follow if you're into real builder notes. cheers.