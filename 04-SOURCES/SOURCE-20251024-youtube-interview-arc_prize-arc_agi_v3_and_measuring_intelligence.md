---
id: SOURCE-20251024-001
title: ARC-AGI v3 and Measuring Intelligence
platform: youtube
format: interview
creator: ARC Prize
date_published: 2025-10-24
status: processed
original_filename: processed/SOURCE-20251024-youtube-interview-arcprize-chollet_knoop.md
aliases:
  - "Chollet - ARC-AGI v3 Intelligence"
teleology: synthesize
notebooklm_category: ai-engineering
guest: Francois Chollet, Mike Knoop
signal_tier: paradigm
chain_relevance: Intelligence
integration_targets: [CANON-30000-INTELLIGENCE, CANON-00003-PRINCIPLES]
date_processed: 2026-01-05
synopsis: "Francois Chollet and Mike Knoop present ARC-AGI v3, adding goal discovery, temporal planning, and interactive learning. Define intelligence as skill acquisition efficiency—LLMs are 4-5 orders of magnitude less efficient than human learning. Solving ARC v3 efficiently would demonstrate micro-AGI properties."
key_insights:
  - "Intelligence defined as skill acquisition efficiency—how well you extract generalizable programs from experience, not what you already know"
  - "LLMs encode programs via gradient descent which is 4-5 orders of magnitude less sample-efficient than human learning"
  - "Real AGI progress requires merging program synthesis (explicit symbolic reasoning) with deep learning (pattern recognition and knowledge representation)"
topics:
  - "ai-engineering"
  - "llm-architecture"
  - "research"
  - "framework"
url: "https://www.youtube.com/watch?v=pBlIgs6w7Ss"
---

# ARC-AGI v3 and Measuring Intelligence

## Executive Summary
Francois Chollet and Mike Knoop discuss ARC-AGI benchmark v3, which adds goal discovery, temporal planning, and interactive learning to v1/v2's passive model-fitting. They define intelligence as skill acquisition efficiency—how well you extract generalizable programs from experience. LLMs are not AGI because gradient descent is 4-5 orders of magnitude less efficient than human learning. Solving ARC v3 efficiently (without brute force) would demonstrate a micro-version of AGI properties that could scale to real-world applications.

## Key Insights

### Skill Acquisition Efficiency as Intelligence
Intelligence is defined not by what you know but by how efficiently you acquire skills and knowledge. The key is extracting programs from experience that generalize well. LLMs encode programs acquired via gradient descent, which is 4-5 orders of magnitude less sample-efficient than human learning.

### ARC v3 Additions
V3 adds critical capabilities beyond v1/v2's passive model-fitting:
- **Goal discovery**: Infer your own objectives from experience
- **Temporal planning**: Plan sequences of actions over time
- **Interactive learning**: Collect your own data by interacting with environment

### LLMs Are Not Sufficient
LLMs could be a component of AGI—the memory/knowledge representation layer. But the defining characteristic of general intelligence is efficient skill acquisition, which is precisely what LLMs lack. Gradient descent is the wrong algorithm for intelligence.

### Reasoning vs. Perception
ARC is fundamentally a reasoning benchmark, not a perception benchmark. The visual format is arbitrary—you could convert it to text or audio. What makes it hard is inferring the underlying rule/program. Reasoning models (o1, etc.) show perception isn't the bottleneck.

### Human-Level General Intelligence
"General" means the space of solvable tasks is vast and diverse (effectively infinite for humans). We're not targeting universal intelligence (any task whatsoever) but human-level generality. The "no free lunch" theorem suggests truly universal intelligence is impossible, but human-level generality is achievable.

### Micro-AGI Properties
Solving ARC v3 efficiently would demonstrate AGI-like properties on a small scale: efficient goal discovery, planning, interactive learning. The games are simple—any human can play them—but the underlying capabilities are what scale to real-world AGI.

### Program Synthesis + Deep Learning Merger
Real progress requires merging program synthesis (explicit symbolic reasoning) with deep learning (pattern recognition, knowledge representation). Neither alone is sufficient.

## Quotable Passages
> "LLMs are basically a way to acquire and encode programs. They're a repository for reusable vector programs acquired via gradient descent on human data. That's not what AGI is." — Francois Chollet

> "The defining characteristic of general intelligence is how efficiently you acquire skills and knowledge—how efficiently you extract information from the world, from your experience, and turn it into programs that generalize well." — Francois Chollet

> "Gradient descent is four to five orders of magnitude less efficient than human intelligence at skill acquisition." — Francois Chollet

## Integration Notes
- Connects to CANON-30000-INTELLIGENCE: Skill acquisition efficiency as core definition; LLMs as component not solution
- Connects to CANON-00003-PRINCIPLES: Efficiency lens directly relevant; first principles on what intelligence actually is
- Novel contribution: Skill acquisition efficiency definition; LLM efficiency gap quantified; program synthesis + deep learning merger thesis

## Metadata
- Duration: ~20 minutes (fireside chat)
- Quality: Clean transcript with verification notes
- Processing notes: Paradigm-tier content defining intelligence and critiquing LLM-only approaches


## Transcript

I'm excited today to welcome Greg Camrad
who is the president of the Ark Prize.
>> That's right.
>> Thanks for coming here at Europe's 2025
in beautiful San Diego.
>> Thank you, Diana.
>> So, what does the Art Prize Foundation
do?
>> Yes. So the ARP price foundation is a
nonprofit and but it's a little bit of a
different nonprofit because we are very
tech forward and so our mission is to
pull forward open progress towards
systems that can generalize just like
humans.
>> So according to Franachal he defines
intelligence as the ability to learn new
things a lot more efficiently.
What does that mean for founders as they
look at all these benchmarks for all
these model releases that are chasing
MLU bench numbers?
>> Yes, absolutely. Well, so one of the
cool things about ARP prize is we have a
very opinionated definition of
intelligence. And this came from
France's paper in 2019 on the measure of
intelligence. And in there, you would
normally think that intelligence would
be how much can you score on the SAT
test or how hard of math problems can
you do? And he actually proposed an
alternative theory, which is the
foundation for what Arc Prize does. And
he actually defined intelligence as your
ability to learn new things. So, we
already know that AI is really good at
chess. It's superhuman. We know that AI
is really good at go. It's super human.
We know that it's really good at
self-driving. But getting those same
systems to learn something else, a
different skill, that is actually the
hard part. And so, um, Franis alongside
that proposal of his definition of
intelligence, he says, well, I don't
just have a definition. I also have a
benchmark or a test that tests whether
or not you can learn new things. because
generally people are going to learn new
things over a long horizon, couple
hours, couple days or maybe over a
lifetime. But he proposed a test called
the ARC AGI or at the time it was just
called the ARC benchmark. And in it, he
tests your ability to learn new things.
So what's really cool is that not only
humans can take this test, but also
machines can take this test too. So
whereas other benchmarks, they might try
to do what I call PhD++ problems harder
and harder. So we had MMLU, we had an
MMLU plus, and now we have humanities
last exam. Those are going super human,
right? Arc benchmarks, normal people can
do these. And so we actually test all of
our benchmarks to make sure that um
normal people can do them.
>> And just a bit of context for the
audience, this particular price was
famously one that a lot of uh LLMs with
just pre-training before uh ARL came in
in the picture before 2024.
>> All these large models, language models
were doing terribly, right?
>> Yes. Absolutely doing terribly. You
know, it's kind of weird, but nowadays
it's hard to come up with problems to to
stump AI. You know, back in 2012 with
ImageNet, all all you needed to do was
just show people an image of a cat and
you could stump the computer. But when
France came out with his benchmark in
2019, fast forward all the way to 2024,
I think at the time it was GPT4, the
base model, no reasoning, I think it was
getting 4%. Four or 5%. So clearly
showed, hey, humans can do this, but
base models are not doing anything. And
what's really cool actually is right at
01 I remember testing 01 and 01 preview
right when that first came out I think
performance jumped up to 21%. So you
look at that and after 5 years those
only 4% and then in such a short time it
goes to 21. That tells you something
really interesting is going on. So
actually we used ARC to identify that
reasoning paradigm was huge that was
actually transformational for for what
was contributing towards towards AI at
the time. So much so that now all the
big labs XAI, OpenAI are actually now
using ArcGI as part of their model
releases and the numbers that they're
hitting. So it's become the standard
now.
>> Yeah. Well, I I tell you what um we're
excited that the community is
recognizing that ArcJI can tell you
something. That's that's what we're
excited about. And when public labs or
Frontier Labs like to use us in terms of
reporting their performance, it's really
awesome that they too say, "Yes, we just
came out with this Frontier model. This
is how we choose to measure our
performance." And so in the past 12
months, you're right, we've had OpenAI,
we've had XAI with Gro 4, we've had
Gemini with Gemini 3 Pro and Deepthink,
and then just recently Anthropic with um
Opus 45.
>> That's cool. So what's going well with
all these releases?
>> So it's it's going really well that
they're adopting it. Um, however, we're
mindful of vanity metrics that come from
there, too. So just because they use us
doesn't necessarily um mean that our
mission is done or our job is done or
what we're trying to do here. Because
again if we go back to the mission of
ARP prize is to pull forward open AGI
progress. So we want to inspire
researchers, small teams, individual
researchers and having big labs um give
an endorsement more or less is really
good for that mission but it's it's also
secondary to the overall mission. So now
that you've seen also lots of teams
trying to ship AI products, what are
most common false positives that you
observe? Things that feel like progress
but aren't quite progress because it's
easy to perhaps just hit a benchmark
somewhere and call it done.
>> Sure.
>> But it doesn't quite work.
>> Yeah. So when I answer that question, I
put on my almost researcher hat because
there's two hats that are very prominent
within AI right now. There's
economically valuable like you know
we're going to go monetize this product
hat and then there's going to be the um
call it romantic pursuit of general
intelligence hat and I I'm wearing the
latter hat. So one thing that stands out
to me is of course is everybody talks
about it but all all the RL environments
and there's been famous AI researchers
that have said hey as long as we can
make an RL environment we can score well
on this benchmark or this domain or
whatever it may be. Um to me that's kind
of like whack-a-ole. You know you're not
going to be able to make RL environments
for every single thing you're going to
end up wanting to do. And core to RGI is
novelty and novel problems that end up
coming in the future, which is one of
the reasons why we have a hidden test
set by the way. So I think while that's
cool and while you're going to get
short-term gains from it, I would rather
see investment into systems that are
actually generalizing and you don't need
the environment for it because if you
see or if you um compare it to humans,
humans don't need the environment to go
and train on that.
>> Perhaps walk us through a bit of the
history of uh ArcGI version. So it was
Argia 1, two, and three is coming up
soon.
>> Yes. which is a whole new thing with
gamelike environments and interactive.
So walk us through the history and then
tell us what
>> three is all about.
>> Yes, absolutely. So RKGI1 came out in
2019. That was France proposed it. I
think he made all 800 tasks himself
within it which is a huge feat in in and
of itself. Um and that came with this
paper on the measure of intelligence.
Now in 2025
just this year earlier in March of this
year we came with ARC AGI 2. And so
think of that as a deeper version or an
upgraded version of RKGI1. Now what's
interesting is those two are both static
benchmarks or you know call it
metastatic benchmarks. We're coming out
with RGI 3 next year. And the big
difference with RKGI3 is it's going to
be interactive. So if you think about
reality and the in the world that we all
live in, we are constantly making an
action, getting feedback and kind of um
going back and forth with our
environment. And it is in my belief that
future AGI will be declared with an
interactive benchmark because that is
really what reality is. And so um V3 is
going to be about 150 video game
environments. Now we say video game
because that's an easy way to
communicate it, but really it's an
environment where you give an action and
then you get some response. Now, the
really cool part and one of the thing
that jazzes me up about V3 the most is
we're not going to give any instructions
to the test taker on how to complete the
environment. So, there's no English,
there's no words, there's no symbols or
anything like that. And in order to beat
the benchmark, you need to go in, you
need to take a few actions and see how
your environment responds and try to
figure out what the ultimate goal is in
the first place.
>> I tried a bunch of those uh games. They
were actually fun.
>> Yeah, they're cool. And much like Ark 1
and Ark 2, we're testing humans on every
single V3 game. So, we will recruit
members of the general public, so
accountants, Uber drivers, you know,
that type of thing. We'll put 10 people
in front of each game, and if each game
does not pass a minimum solvability
threshold by regular humans, then we're
going to exclude it. Now, again, I just
have to emphasize, but that's in
contrast to other benchmarks where you
try to go harder and harder and harder
questions. But the fact that ARK 3 will
be out there and regular people can do
it but AI cannot do it tells you well
there's something missing still. There's
something clearly missing that we need
to um need new ideas for research on.
>> So there's this big theme in terms of
measuring intelligence with human
capabilities.
>> Yes.
>> So there's this growing idea that
accuracy is not the only metric that
matters to models.
>> Yes. but also the time and amount of
data that it takes to acquire new skills
which is what this whole spirit of our
AGI is.
>> Yes.
>> So I guess the question is how close are
we to evaluating models in human time?
>> Yes. So with regards to human time, we
actually see time as a little bit
arbitrary because if you throw more
compute at something, you're going to
reduce the time no matter what. So it
it's it's almost just a decision on how
much compute do you want, which is how
much time it's going to take, which
tells you that wall clock may not be the
important part for what we have
intelligence here. But there's two other
factors that go into the equation of
intelligence. Number one is going to be
the amount of training data that you
need, which is exactly what you said.
And then number two is actually the
amount of energy that you need in order
to execute upon that intelligence. And
the reason why those are so fascinating
is because we have benchmarks for humans
on both of those. So we know how many
data points a human needs in order to
execute a task and we know how much
energy the human brain consumes to
execute a task. So with RKGI3, the way
that we're actually going to be
measuring efficiency, not just by
accuracy,
I I told you they're video games and
they're turn-based video games. And so
you click, you might click up, left,
right, down, or something like that. And
we're going to count the number of
actions that it takes a human to beat
the game. and we're going to compare
that to the number of actions that it
takes in AI to beat the game. So, back
in the old um Atari days in 2016 when
they were making a run at video games,
then they would use brute force
solutions and they would need millions
and billions of frames of video game and
they would need millions of actions to
basically spam and brute force the
space. Um, we're not going to let you do
that on ARI 3 and so we're basically
going to normalize AI performance to the
average human performance that we see.
>> That's very cool.
>> Yes.
>> My last question.
>> Yes. Let's um wave a magic wand and then
there's a super amazing team that
suddenly tomorrow res launches a model
that scores 100% in the arc AGI
>> benchmarks.
What should the world update about the
priors of what AGI is?
>> Yeah,
>> how would the world change?
>> Well, it's it's funny you ask that. Um
the what AGI is question is such a deep
topic that we can go much deeper on. So
um from the beginning Franuis has always
said that the thing that solves arc AGI
is necessary for AGI it's not
sufficient. So what that means is um it
the thing that solves arc AGI 1 and two
will not be AGI but will it will be an
authoritative source of generalization.
Now our claim for V3 is that it no the
thing that beats it won't be AGI however
it will be the most authoritative
evidence that we have to date about a
system that can generalize. If a team
were to come out and be at it tomorrow,
we would of course want to analyze that
system, figure out where still are the
failure points that come from that. And
like any good benchmark creator, we want
to continue to guide um the world
towards what we believe to be proper
AGI. But ultimately um ARP, we want to
put ourselves in a position when we can
fully understand and be ready to declare
when we do actually have AGI. So if that
team were to do it tomorrow, we'd want
to have a conversation with them. We'll
put it that way.
>> That's a good way to wrap. Thank you so
much for coming and chatting with us,
Greg.
>> Thank you, Diana.
