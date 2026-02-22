---
id: SOURCE-20251023-001
title: Chain of Thought | MCP Atlas Benchmark Deep Dive
platform: youtube
format: panel
creator: Scale AI
date_published: 2025-10-23
status: triaged
url: "https://www.youtube.com/watch?v=c34W8hmTxHo"
original_filename: processed/SOURCE-20251023-youtube-interview-scaleai-mcp_atlas_benchmark.md
aliases:
  - "Scale AI - MCP Atlas Benchmark"
teleology: reference
notebooklm_category: ai-agents
signal_tier: strategic
date_processed: 2026-01-05
synopsis: "Scale AI presents MCP Atlas, the first comprehensive benchmark for AI agent tool integration via Model Context Protocol. Tests discovery, execution, error handling, and multi-tool coordination in live environments with real MCP servers. Over 1000 MCP servers exist in Anthropic registry within the first year."
key_insights:
  - "MCP is becoming table stakes for SaaS providers wanting discoverability in agent workflows, with 1000+ servers in Anthropic registry"
  - "MCP Atlas uniquely tests in live environments with real MCP servers, evaluating end-to-end capabilities from discovery to execution"
  - "Complex benchmark tasks require 10-20 tool calls with sophisticated reasoning between them, testing real agent orchestration ability"
topics:
  - "mcp"
  - "ai-agents"
  - "ai-engineering"
  - "developer-tools"
---

# Scale AI MCP Atlas Benchmark: Evaluating Agent Capabilities

## Core Thesis
Model Context Protocol (MCP) is emerging as the de facto standard for AI agent tool integration. Scale AI's MCP Atlas benchmark provides the first comprehensive evaluation of real-world agent capabilities, testing discovery, execution, and error handling in live environments.

## Key Insights

### MCP Fundamentals
- **Definition**: Standardized protocol for providing context to models and enabling tool interaction
- **Adoption**: 1000+ MCP servers in Anthropic registry within first year
- **Builders**: Companies (Notion, Brave, Google Drive), open source community, independent developers
- **Importance**: Table stakes for SaaS providers wanting discoverability in agent workflows

### Why MCP Matters
- Decouples fit-for-purpose connector development
- Standardization enables ecosystem compatibility
- Any model builder can connect to any third-party service with MCP adoption
- Reduces developer mental effort through consistent protocol

### MCP Atlas Benchmark Design
**Key Differentiators:**
- Tests in live environments with real MCP servers running
- Evaluates end-to-end agent capabilities, not just function calling
- Several hundred tasks spanning multiple domains and difficulty levels
- Open-sourced: task definitions, MCP servers, evaluation harness all on GitHub

**Evaluation Dimensions:**
- Tool discovery without explicit instruction
- Correct parameter specification
- Error handling grace
- Multi-tool coordination
- Intermediate step accuracy

### Example Task Complexity
Simple: 1-2 tool calls
Complex: 10-20 tool calls with sophisticated reasoning between them
Test domains: customer support, data analysis, research workflows

### Differentiation from Other Benchmarks
| Benchmark | Focus |
|-----------|-------|
| Berkeley Function Calling | Predicting function calls from descriptions |
| Gorilla APIBench | API calling capabilities |
| ToolBench (Tsinghua) | Simulated API testing |
| AgentBench | Some multi-step scenarios |
| **MCP Atlas** | Real environments, MCP protocol, full discovery-to-execution |

### Open Source Rationale
1. Create shared evaluation standard for community
2. Gather feedback to improve methodology
3. Accelerate ecosystem progress through benchmarking

## Canonical Relevance
- Critical for CANON-30300 Tech Stack evaluation criteria
- Supports Intelligence chain tool-use capability assessment
- Informs CANON-30400 agent architecture decisions


## Transcript

[Music]
Welcome to Chain of Thought. Uh on this
week's episode, we're going to be
talking a bit about Scale's latest
research in benchmarks, specifically for
MCP evaluations and MCP agents. Uh my
name is Brad Kensler. I'm the head of
agent capabilities and environments
research here at scale.
>> I'm Cha Chaitana. So I've been working
on the MCP well for a while. So excited
to share what we have.
>> I'm Sami. Uh I work as a product manager
owning all things tool use.
>> And I'm Chathan. I lead the product team
for agents and environments. So we have
lots of exciting updates to share on
this new benchmark. Uh you know, which
is one of the first to test out uh MCP
capabilities. Uh and we'd love to dive
into the research behind this, but do
you mind giving us an overview of what
MCP actually is?
>> Yeah. So MCP
uh stands for short for model context
protocol. It's basically roughly it's in
the name just you know it's a way for
standardizing how you provide context to
models and I mean other communication
protocols exist but this is the one that
is the most widely adopted in terms of
standardizing it. So a brief context on
that uh LLMs are like the brains of the
system. We need in order to make agents
that are reliable, that are actually
able to do things uh that we do in a
day-to-day basis, they need access to
information that they can retrieve
externally and also be able to make
changes in the state outside of their
own internal memory.
>> Yeah.
>> And so to do that, we need ways to
connect LLMs with a lot of different
tools. Now, MCP is the most widely
adopted standardization of that. uh
previously we had many that you know um
maybe they weren't as adop widely
adopted in terms of standardization
>> right
>> and this is a standard that has been
really embraced by developers so it's
been uh it has gone viral the the way
and uh you know AI is all a developer
play so whatever developers embrace is
what's going to be uh there for a you
know for a while so MCP is something
that developers really like
>> right and like I'm curious like what
what is what came before MCP? Like if I
was building an Asian application in
like 2022, right? Like how did I do
that? And like how does MCP sort of
change the game for the space today?
>> Typically
back in back in 2022, the conversation
was most around rag systems. And so
you'd have um which is complimentary to
MCP but it's basically having external
information uh that you uh get and then
plug into your LLM. So it's more
grounded but the communication between
uh different servers different external
services and models that wasn't
standardized. OpenAI came up with their
function calling API. That's one way one
framework they provide. Other companies
like land chain they have their own
systems for how to standardize
communication between models and
external services. Uh but MCP came out
last year and it provided a way for both
ends of it the model builders to adopt
it and also the the third party services
to come up with abstractions that
anybody can then use. So
>> yeah, end of 2023 to be exact. But yeah,
it's been it's been amazing since they
came out uh led by Anthropic. Um and
it's been it's been great after that.
Yeah.
>> Yeah. I think I think one of the
exciting things about MCP is like how
the standardization around this protocol
has made it easier for uh both sides of
the ecosystem to like build something
that's compatible, right? Like if you're
thinking about, hey, I'm a SAS provider,
right? And I want to make my service uh
readily available to um model uh MCP
clients, right? Or agents. I now have a
protocol that I can design for. I can
release an MCP server. Um, and so now
anyone that's actually building an
agent, right, it's it's dead simple for
them to just use that MCP server,
integrate it into their MCP client. Um,
and so like this sort of um, decoupling,
so to speak, of like, you know, having
to build uh, fitfor-purpose connectors,
I think, is is what's really
turbocharging a lot of this and making
it exciting.
>> Absolutely.
>> Yeah. Yeah. So to add to that, there's
let's say three parts, right? There's
the developer and then there's all the
model builders and LLMs right here on
the left and then there's the developer
and all the third party services here on
the right.
>> Right?
>> Each one of them can have its own line
and how it's integrated. So developers
had to write their own adapters and so
MCP makes it such that you don't have to
each one of those lines can be
abstracted away and it's very simple to
plug any third party service with any
model builder as long as they adopt it
which recently we've seen a lot of
companies adopt it. So super cool. So
what like what specifically about MCP
makes it different from like traditional
APIs?
>> I think it's more of a standard. So um
think of REST API for web development.
So you know before that there used to be
a lot of protocols for web development.
Rest API just made it easier for uh
folks to uh educate themselves on how to
build applications and that's the
standardization that's bringing out the
power of MCP. So it's more of hey uh you
know is it the only way? It's not but
it's a standard way so that people can
now take away uh you know that mental um
you know effort to build a new one.
Yeah.
>> Right. Yeah. So I think you know that
standardization definitely increases
overall adoption and uh you know MCP is
obviously emerging as kind of the de
facto solution now for how um you know
we think models are going to interact
with different services different uh you
know systems and access data um across
them. I think to maybe contextualize
this for the audience, can you give us a
few examples of you know MCP servers uh
that are maybe popular or that we think
uh you know a lot of model developers
are going to want to figure out how to
integrate with and improve their
capabilities on.
>> Yeah. So I think this really depends on
the use case that somebody targets but
you can have MCP servers for your ERP
system or your CRM system or your
communications channels or your
productivity systems, note-taking even
your social media channels, right?
Depending on the use case and so let's
take an example of um notion. Um a lot
of people use notion as their
note-taking platform. somebody whether
it's notion or a thirdparty developer
might build an MCP server and then
they'd expose abilities to uh to another
developer that would then be able to
either read information from notion or
even update uh things in notion for
example uh reading one of your pages
around one of the reflections that you
had and then updating uh with a data
with a table so notion is one example um
but you know there's very a lot of
interesting ways you can mix and match
these uh you might have your note-taking
system have an MCP server that that
connects with your Salesforce MCP and
you're able to you know do a lot of
create a lot of tasks that kind of uh
>> and even for fun so there's a YouTube
MCP server there's a WhatsApp MCP server
uh you know Slack MCP server
>> with a YouTube MCP server
>> yeah you know the LLM can access the
transcript for example and then find uh
you know better YouTube videos for
example right so it's uh you know the uh
again applications have been, you know,
growing. So once the standard is there,
you could build put many things together
and then build many things.
>> Actually, one one thing I'm curious
about is who's building out these MCP
servers, right? Um, aside from, you
know, the the training and the eval work
that we'll talk about, but is this being
done by, you know, the third party
services themselves? Are there, you
know, independent developers that are
contributing to the um, you know,
overall ecosystem?
>> Yeah.
>> Yeah. So in in fact um so the for
example each MCP requires something um
you know behind that for example let's
say Wikipedia so there are you know
official Wikipedia MCP servers and there
are third party folks that uh you know
give access to Wikipedia as well so it's
been a mixture um you know Slack has its
own MCP server um WhatsApp you know
there are many official and unofficial
servers
>> yeah so I mean a lot of them have their
official ones and then a lot of third
party services I mean third party uh
people just build their So like if I
wanted to make a um MCB server like say
for uh AWS, right? Like
>> is it something like I would um like
take Boto3, right? Like the Python SDK
for AWS and then basically like
>> wrap some like use some MCP framework or
something and then like create some
tools that invoke the API.
>> Exactly. So launch an instance for
example or check uh you know how your
instance is doing. So you can in fact
talk to it uh just like an API call but
in a in a format that's understandable
by an LLM.
>> Right. And so basically any you know
APIs or SDKs that are out there you can
wrap uh an MCP around it.
>> Um okay so I'm kind of curious I think
before we move on to talk about the
benchmark like
>> would love to drill down into like what
um an MCP agent is actually doing. And
so I think Sammy, you were talking about
tool use earlier on. Um, and like can
you maybe just like can you guys define
for the audience like what is tool use?
Like what does a tool use agent do?
>> Yeah. So two things that are needed for
an agent to be able to do like
meaningful work. One is to read
information from external sources and
then the second part is to be able to
make updates to any external
information. And so when we talk about
to use, to use is the way that the
general umbrella under which LLMs are
able to do that. Um and that's uh are
able to do that programmatically because
we're not talking about the guey the
graphical user interface side that's
different. But to programmatically do
that tool uses a concept. Now,
concretely, let's say if you're using
the OpenAI uh function calling API, um
an agent would be passed in a certain
number of tool definitions based on that
format. And then uh when a user asks a
question from the agent, they would the
the model would then look at the prompt,
look at its available tools that are
available to it. In that reasoning, it
would decide which tool to call based on
the description and then send an a
function invocation back to the
scaffolding running the agent and then
that scaffolding then runs that function
with the provided parameters, creates
the output, sends it back to the LLM,
LLM reasons over the output and then
continues on into its trajectory. Right?
>> So that's that's like the concrete flow
>> and then MCP just provides
standardization in those communications.
But for agent themselves there as Sami
mentioned the access to the tools but
the agent also has to figure out which
tools to invoke. Right.
>> Right. And that's the that's the part
where LLMs are good at you know thinking
about reasoning LLMs and so on. So they
are able to use that reasoning power to
figure out which tools to call and then
how to use them.
>> Right. So in terms of like packaging
tools, an MCP server is kind of like a
box that like contains tools that the
like developer defines, right?
>> And then when you connect an MCB server
to the client, it basically exposes
those tools to the client.
>> Yeah. And that way in terms of like
context engineering for for tool use it
it solves like a practical problem where
like the the individual developing the
MCP client doesn't have to like uh
define all the tools in advance
priority. Right.
>> It's it's all packaged in the MCP server
and so now like that decoupling makes it
easier to build the agent clients as
well. Exactly. It's really interesting.
Um, so Chate, I'm curious. You were
talking a bit about like, you know, one
of the things that's important is
picking the right tools and things like
that. So that's probably a good segue
into our our latest research around um,
MCP evaluations. Um, so I'm wondering,
can you tell me a bit more about um,
like how scale thinks about evaluating
MCP capabilities?
>> Right. Right. Yeah. Yeah, I think one
thing that I want to firstly stress is
this is a sea change in the capabilities
of LLMs. And think of it as like in
human civilization, you know, people had
brains, they were running around, you
know, finding animals for themselves or
eating fruit. Uh but then what changed
in civilization is access to tools.
Think of Bronze Age, right? So that's
the kind of situation we are in right
now. Um where we have LLM that are
really good at reasoning internally, but
now they're being given superpowers,
right? um by giving access to these
tools. So which means that now LLMs have
to not just uh think about you know
using their own memory and knowledge but
also extend themselves by using the
right set of tools and this is the
capability that we are trying to figure
out um in you know in our benchmark is
to understand how good are LLMs to
actually extend their uh extend
themselves by using external tools and
at a high level that's what we're trying
to figure out are is a you know earlier
we used to have you know let's say
prints and printers training themselves
to use multiple tools. So we are trying
to figure out okay are LLMs doing good
at using these multiple tools. That's
what we are trying to figure out.
>> And the approach here is to in creating
a like how do we evaluate it is try to
replicate the difficulty and the realism
of tasks that we were facing in the real
world. And so as we'll talk about in the
benchmark, it's not just a problem set,
but also adding on uh an a sandbox or an
environment that contains real data from
external MCP servers um and a and a
diverse set of them uh coupled with like
difficult prompts that you know then
make it a we think it's more it's more
realistic of a
>> yeah we are not the only ones thinking
about this because this is such a key
foundational capability for LLMs. Um but
where we differ is the diversity of uh
tools that we are testing it on uh that
we are giving access to the LLMs and
then checking if they are able to you
know simultaneously use a notion MCP
server which is about productivity
versus an entertainment MCP server is it
able to understand this capture this
diversity. Yeah. And and ju like just so
it's abundantly clear to the listener,
uh the big news here is that we're
launching an MP benchmark, right? And
>> so we're super excited about that and
that's that's what we're talking about.
Um
>> yeah. Um no, I mean this is all very
exciting. I think uh you know when it
comes to like the tasks right that are
included in this benchmark, the sort of
problems that we are uh you know feeding
into the model like more concretely what
are all of the different capabilities
that we're testing for? So, I've heard a
few things so far, including, you know,
the ability to pick the right tool to
use, the ability to actually reason
through multiple different outputs or to
use multiple tools in conjunction. Can
you maybe just map out like what does a
good task look like and what are all the
different types of capabilities that we
want to be able to test models on?
>> Great question. So, so thinking about
again going back to what are we testing
for? We are testing for a model's
ability to answer a certain question or
you know do a certain task by invoking
multiple tools that it has access to.
Right? So the first thing that we test
for um in these prompts is is it
choosing the right set of tools?
>> Right? Is it choosing the right ones? Is
it missing any needed ones? Is it
ignoring some of them? So we we test for
that.
>> The second one is now once it picks a
certain tool to use, is it good at using
that tool? Is it using it correctly? So
this is where we talk about you know is
it um you know calling the right uh API
function in a in a in the correct way
right now this is about again picking um
you know calling it well but then
finally it gets back all the context
which Sami was mentioning is it able to
understand all the context and then you
know digest it uh understand it and
reason on it and then answer the final
question. So these are the three broad
capabilities that we're testing for. So
it's really these endto-end tasks where
you're evaluating how well can I reason
through a set of tools uh and then
complete that pipeline up until it
provides the right answer.
>> Yeah, great part. So it's the end to
end. So that's why creating tasks for
this is also you know we need to do that
carefully. The task should be
self-contained and well you know uh uh
it should be very clear what the task is
asking for. Yeah.
>> Right. Uh so that's the key idea and
then it should enable uh or it should
require multiple tools to be called and
then uh you know uh digest a lot of
other information and aggregate a lot of
information to answer the question.
>> Yeah.
>> Uh so that's the key part that we do
here.
>> Yeah.
>> So I'm curious can you like um drill
down into like what does it mean for a
model to use a tool effectively? So you
kind you you spoke about these three
things right like selecting which tool
to use the tool and then like digesting
the output. like concretely what does it
mean to use the tool effectively
>> right yeah this is where I think we
haven't talk talked about the
environment so a key difference in in
this benchmark compared to let's say
other types of capabilities that you
test um in other capabilities you have a
question the model does all the thinking
by itself internally and then answers
the question right so this is the first
time we have um you know we are
evaluating model capabilities which
requires an external environment this
external environment is essentially the
box of tools. So um you know what it
takes to finish a task is it needs to
connect well to that environment. The
environment should be robust um should
not fail you know because we are
evaluating LLMs we should not have a
buggy environment because then you know
we are not uh we are evaluating the
environment and not the MCP not the LLM
itself. Uh so that's the key part that
we made sure that the environment is
robust uh reproducible and then now LLM
is able to use that environment to call
certain tools. By calling we mean you
know it's literally making an API call
or or MCP API call right uh and then
getting the answer and then digesting
it.
>> Okay. specifically there when we have in
in the calling portion. So once it's got
a spec of all the tools that are
available to it and the spec includes
all the tools as a JSON list and then it
includes a description of what the tool
is so that an LLM is able to pick the
right one
>> cuz when they when there's many it you
know we need to have that clear. Um once
it picks the right tool then it's about
creating that function invocation with
the right parameters. Um and then yeah
that that's what it means to call it and
a lot of times they either pick the
wrong tool uh or they pick an
inefficient one when a task that could
have been done with one tool with one
call sometimes they pick another one
that has to be done five times let's say
Google Google distance matching for
example
>> um and so and sometimes they might not
pass in the parameters properly so
that's what we mean by calling the right
tool properly
>> so if I'm if I'm kind of going with this
analogy you had earlier about like the
LLM as a bronze age caveman right so
that you know you're this caveman. Um,
you've been given this like task, you
know, go build a bridge or a dam or
something. I don't know what Bronze Age
cave folk were doing. Um, and uh, your
environment is like this box of tools,
right? Like you might have some kind of
like hammer thing or like some like
knife.
>> And so be
>> Yeah, exactly. And so the the um model
has to figure out which tools do I want
to use in this box. Um, so that's part
of it, but then also once they're using
the tools, how good can they use like
how effective are they with a hammer,
right? Um, and then if they use the
hammer and they see that the hammer is
not working or it is working, like they
need to figure out what do I need next,
right? And so this kind of like long
horizon thinking of using these
different tools to accomplish some some
tasks.
>> Yeah, it's a multi-step process, right?
As you correctly mentioned, maybe you
need to use the hammer to break the
shell and the knife to, you know, cut it
down properly. So this is the type of
multi-step thinking that we are
evaluating uh our LLMs for
>> I think more importantly too you might
realize oh this hammer is not breaking
the shellact now what do I do right so
you need to like recover from these like
failure modes
>> exactly yeah I think just piggybacking
yeah that's a great analogy and
>> it was chained so I s
>> uh yeah I think just piggybacking off of
this I mean one of the things you
mentioned earlier was that you know
there are kind of like two functions
that uh exist within this realm of like
you know tool use and MCP right one uh
information retrieval where you know you
are uh essentially like pinging these
servers to get information back that you
can use to reason through and the other
is actually performing actions or like
mutations within that service. How do we
think about both of these capabilities
and you know are we capturing both of
these in our benchmark today? Do we
think one of these is maybe more
important than the other when it comes
to how people are actually using this in
in a production environment?
>> Great question. Um I think here it talks
about the environment, right? So in
order to get access to you know
information um you know that's out there
in fact in our environment we have a lot
of real world data and artifacts that we
have collected
>> and which we are you know populating
this environment with uh so that um you
know let's say real world Slack uh you
know conversations uh there are
literally you know there's an
environment where we have slack
conversations and then people can ask
questions on it
>> right um so we have that but the other
aspect is writing to it so we currently
don't have that in benchmark mainly
because we are open sourcing it. We
don't want you know people to corrupt
each other's
>> environment. It's hard to build these
>> hard. Exactly.
>> But that is like once we
>> I mean that's an important capability
that we will explore. This is just the
first of of several benchmarks.
>> Absolutely.
>> So can can you tell us a bit about like
this environment specifically like
>> Yeah.
>> I mean what's what's in it,
>> right?
>> Yeah. So three parts to the whole
benchmark. It's the data which is the
evaluation task like 2,000 tasks that
you can run on. Then
>> 2,000
>> 2,00.
Oh, that's actually one of one of the
you know places where we differ from
existing benchmarks. So we went diverse
and large number and difficulty as well.
So difficult tasks as well.
>> Cool.
>> Yeah, we can get into the performance
numbers in a bit but 2,000 tasks. Then
we've got the environment and then we've
got data that we have to seed some of
these environments with which CH just
talked about. I'll go into a bit of
detail. So the environment basically is
a docker container of MCP servers. There
are 40 plus MCP servers ranging from
productivity to um project management to
social media like YouTube.
>> And then each one of those servers has a
number of tools attached to them. So in
aggregate it's about 300 plus tools.
>> Um for those 2,000 tasks, each one of
them target different servers and
different tools in different ways. Uh
and so we expose those tools to uh to
each model per task. Now some of these
servers are have to be stateful in
nature. For example, notion for example
the local memory knowledge graph that we
have right they don't have any
information within them by default. So
that's where we've done the work to have
real world data acquire real world data
and then populate them with this data so
it resembles you know let's say real CSV
files from other businesses. Um
>> so sorry I just want to double click on
that. So what you're saying is that the
the uh different like systems in this
environment uh that like need real data
like we're actually we've acquired data
somewhere real world data and like put
it in these environments. It's not
synthetic in any way.
>> Some of the data for some of the service
is synthetic but a lot of it is actually
real world data that we've acquired from
real businesses right
>> um and an example of this might be like
you know shipping uh logs etc that a
company might have. And so uh some
servers like slack for example we have
done the work to generate a lot of
conversations and if see the servers
with other ones for example notion air
table we have a lot of real world data
with that we've populated them with and
then the tasks use them um and the
models are able to interact with them so
it it really reflects the realism of of
the data it's not synthetically
generated
>> and and does each agent like is it given
the entire tool set and MCP servers or
how does that
Yeah. So for every task we we don't want
to give all the 300 plus tools for for
every task. So in every task we uh we
have target servers that we call. So
basically um let's say subset of them
let's say 30 tools right. So among those
30 tools we are evaluating is the model
picking the right tools. So that's why
we don't want to you know give
everything and then you know confuse it.
um we give subsets because we are trying
to evaluate models um on on different
capabilities.
>> It also a lot of models don't even
support the full 300 plus for example
GBD40 supports 128 as far as I know in a
single uh conversation
>> and so uh that then combined with the
the subset that we do enable that also
includes some some servers that are very
relevant to the task at hand but then
others that are distractors. Uh and the
point of the distractors is to be able
to simulate real world scenarios where
they might have to choose the right one
amongst others that might confuse it a
little bit. Uh that's one of the things
that makes this benchmark that we
believe more difficult.
>> Yeah. And this is something we talked
about in a previous episode on you know
how to make new evals that capture real
world distributions you know actually
seed them with data that exists in
actual business processes that look very
realistic and are not synthetically
generated. So uh you know really proud
of all the work that the team has done
here. I think the other thing to
celebrate is that uh we are open
sourcing this environment and that's not
something that you hear very often from
data companies. Uh can you talk a little
bit more about you know our decision to
do that and how we think this is going
to benefit the research community.
>> Yeah we really think so we are at the
beginning of you know this evaluation of
LLM on these capabilities. So we want
developers to uh in some customize these
uh you know these tasks and the the way
they're evaluating as well. So that's
why we want to make sure the environment
is something that uh any let's say um
any student or you know a PhD student
doing some research can quickly download
and then set it up on their laptop and
then start evaluating their own small
LLM. Right? So that's the key. Um and
that's why we we took some effort to
figure out what are some good MCP
servers that are robust to many people
using them at the same time. Um and then
you know that's how we chose 40 and
diverse enough that we have some people
who are interested in you know building
social media tools versus people who are
doing deep research uh can also use. Um
so yeah so the open sourcing serves that
purpose.
>> Yeah and to be clear the the environment
is fully open source as well. So you get
the environment which contains the MCP
servers and you also get you know the
ability to run create trajectories uh
for all 2,000 tasks for any model of
your choice that you want to evaluate
let's say and then you also get the the
evaluation scripts that we use to
compare those trajectories against what
we think evaluate those trajectories
right and get some failure mode analysis
on that. So anybody could at a lab or a
researcher they could spin it up and
they could get insights onto the model
that they want to evaluate. Uh and
they're also able to freely mix and
match. They're able to choose what they
want to modify. They can change the
evaluation script if they want a bit of
a different failure mode analysis. They
can extend the environment. They can add
their own MCP servers. They can create
their own problems if they want. So I
see it as a three-piece system and um
people are able to change and extend as
they want.
>> That's really exciting. And um you know
I know we want to talk a little bit
about how models are actually performing
on this benchmark. What makes this you
know one of the hardest ones out there
uh but just to you know give a little
bit of context before that can you talk
about some of the other you know
benchmarks that a researcher might use
in conjunction with you know our new MCP
valuation to uh gauge you know tool use
capabilities.
>> Yeah so there are um some um other you
know benchmarks that are measuring tool
calling abilities. Uh there's one from
Berkeley you know it's called Berkeley
function calling leaderboard um and you
know there's something called towen so
there bunch of those um uh but where we
differ from a lot of these is the the
scale you know for the lack of a better
word uh yeah um you the diversity uh of
the types of tasks that we have and and
the difficulty so that you know we are
eager to uh get to get to that part but
yeah diversity the difficulty and the
number of tasks themselves. So we we we
are open sourcing about 2,000 tasks.
>> I think uh and correct me if I'm wrong,
but like you know there have been some
recent MCP benchmarks come out and I
think um one of the trends that I've
noticed and I've not I've seen this for
a few different um agent uh benchmarks
like there was a recent deep research
benchmark um that that did this. Uh
there's a lot of like synthetic task
generation.
>> Yes. Um, and I think one thing that's
interesting um, and we'll talk a bit
about this when we get to the results is
that like
>> you can you can see a pretty clear uh,
separation between like task complexity,
right?
>> Uh, when you're generating tasks on the
fly um, versus like having uh, actual
humans thoughtfully craft really
difficult problems that stretch a
model's capabilities. And so I think
it's interesting because it's you know
on the one hand uh benchmarks that rely
on synthetically generated tasks um are
more accessible in a way. Um but but at
the same time you're uh like I think
we're seeing the ceiling of like how
complex um the tasks that a model can
generate uh really are. Um like I think
some of the recent ones that came out
you know we're seeing pass rates at
launch like in the uh mid to high 70s.
Yeah. Um, and so I think that's
something that that uh we see quite
different in our benchmark. But before
we get to like the benchmark results,
maybe just walk through like what is an
example task for the viewer so they have
a very clear understanding of like
>> what does a task in this benchmark look
like?
>> Yeah. So it's just three simple parts.
Each pro each of the 2,00 tasks has a
prompt that is written by a human, not
synthetically generated. Um the prompt
in order to answer it, you need a set of
tools. So those enabled tool we have a
list of enabled tools that we provide to
the prompt which includes the necessary
ones and then the distractor ones and
then we include a um ideal trajectory uh
that is you know the ideal response to
that prompt. The model would be would
take the uh the prompt and the enabled
tools and then it would create a
trajectory and then we would uh using
our evaluation script evaluate it
against what we think the ideal
trajectory is.
um that's the composition of a task.
>> So can you maybe but as a contributor
right uh yeah the example um you know
not to take some example from the
benchmark but uh one of the questions
that we saw was um hey I'm I'm visiting
uh Japan and there was some time when uh
I went to you know Tokyo there was a
hotel close to a um you know sushi
restaurant uh and there was also a
dumpling restaurant right next to it.
can you find me you know um new hotels
nearby and also tell tell me you know
how much it would cost for me to you
know uh h a ride from the airport to
that hotel. So if you see this question
it has a bunch of there's some memory
aspects so where the model has to figure
out where this particular hotel is and
find options for other hotels around the
area. So it might have to use tools like
maps for example. Um and it also has to
figure out do some calculations. Uh so
figure out the distance figure out the
cost of ride in Japan, a cost of taxi
for example. Uh and then calculate that.
So you can see how this you know very
natural type of question that you would
ask travel agent for example will be
answered by LLM by g by accessing
multiple tools. Right.
>> So so this is interesting. So you're
saying that we have like a memory tool.
Okay. So that's so basically um a lot of
the tasks like provide the agent with a
tool that basically gives some some
memory for the
>> that's I mean that's that's pretty
comparable to how a lot of actual um
like LLM and agent applications work
especially consumerf facing ones right
>> like we have notion or you know slack
where you could say hey in a in a
channel my friend was mentioning about a
certain game right video game now how do
I buy similar video games that could be
a But even there's those external data
sources and then there's something you
know local memory stores that we have.
So like this memory uh MCP server is
represents knowledge in a graph
>> right
>> and so like you said a lot of client
facing uh applications like chat GBT
they have their own memory systems that
persist across chats
>> and so this is kind of emulates that
where have you have memory stored about
you
>> right
>> and then the the agent is able to check
retrieve information from there
populated with a Google search query and
then populated into the calculator to
measure distances etc. And this is a key
part that we wanted to make sure that
these prompts are realistic because
that's the key criticism that many
benchmarks get that hey okay so you do
80% on this benchmark but what does that
mean for our real use case right
>> that's why we made sure that the prompts
are generated by uh humans and trying to
ask regular you know usual questions not
um you know not something to stump the
model for
>> right right and uh
one thing that you guys mentioned too
which I think super interesting is like
this notion of distractor tools, right?
>> So, if I'm recalling correctly, like an
example of this is something like
>> I think one of the prompts you just
mentioned which is like oh um
>> somebody mentioned in one of my uh
messages that um there was some movie
they wanted to see or something like
that, right? Um and uh where basically
the prompt is is saying it's suggesting
that the agent needs to search through
some messages and then the tools that
are enabled are things like Slack but
also maybe something like um email um
and like maybe some third like message
related thing. And so the agent
basically has to figure out okay
>> uh uh this this uh individual is talking
about some message history. I have these
message related tools. I need to figure
out which one's the correct one and
which one's not. Or I can just use all
of them and just kind of figure out like
where is actual where's the information
actually stored.
>> Like if it if it says channel in the
prompt maybe it the model would think
slack. Yeah.
>> If it if it doesn't and there's no
nothing that it can infer from then you
would think maybe it should just start
with one and then see how it goes right.
Right.
>> That's what a human would do as well.
And I think this is very interesting
because like real world agents are
equipped with you know dozens if not
maybe even hundreds of tools right and
as um you know these agents take on uh
larger and larger workflows in order to
get those done accurately right you just
have to equip them with a lot of these
capabilities and so then a fundamental
problem becomes like how well can they
understand the purpose that each tool
serves um you know the information that
they can retrieve from different sources
and discern what the right ones are and
so I think you know idea of uh you know
including distractor tools is is it's a
very cool approach.
>> Yeah. This way we can you know measure
um is it selecting the right tool right
and not giving up you know just by
looking at one source and then you know
if it doesn't find the answer there it
shouldn't be giving it up right. So
that's the aspect that we test as well.
Yeah,
>> we talk a lot about how uh you know
having um rewards and having verifiers
that are a bit more nuanced and not
necessarily you know fully deterministic
or you know binary zero or one um are
are good for for this sort of um you
know evaluation whether it's you know
looking at a bunch of claims right that
have to be true for a final response or
maybe even evaluating like the process
right did the agent you know call the
right tools did it figure out which ones
were the distractor tools was it able to
like reason through um you know the
problem properly.
>> Yeah, there are two you're right. So, we
are capturing two different types of
analysis. One is is it getting the final
answer correct? It's called the final
answer correctness, right?
>> Uh the other one is the process itself.
So, sometimes models get the process
right, it's calling the right tools in
the right way, but maybe at the last
step of aggregation it's failing. So, we
also capture okay is it at least doing
these partial steps well. So, we capture
those uh aspects as
>> exactly.
>> Yeah. So, so what did we actually learn
about like uh what are models good at
today out of all these capabilities? Uh
where do we see you know the most room
for improvement as well?
>> Um yeah, in a way because our tasks are
difficult so I I'll talk about where
they're failing, right?
>> Sure. Yeah.
>> Um so I think most of them um also one
thing that we realize is different
models um you know there's not much
correlation between different models how
they fail. So different models are
failing at different uh things for
example. But most common things that
come out are um picking the right tools.
So models are picking the wrong tools uh
and sometimes you know trying to answer
it based on their memory uh not even
trying to call tools. So this is the you
know uh picking the wrong tools or
missing tools what we call the failure
mode. The other failure mode is um not
able to call uh you know in the right
format. So it's not picking the right
parameters. So in the Japan you know
hotel example maybe it will say you know
find hotels near an address and then it
doesn't give the right exact address it
just gives a hotel name for example and
the maps doesn't necessarily work with
that so we need to be giving uh the
coordinates of it and so on and so forth
right so picking the right tool but uh
using it wrongly right so that's another
failure mode um and there are some
failure modes on planning if it's a long
horizon task some models you plan
wrongly. So they they just uh um choose
the order in which they should be
calling the tools you know you know
wrongly and then that makes them fail at
the task. Yeah. So these are the common
things.
>> So the p the primary to summarize then
the primary ways that we see them fail
the most is in tool selection and then
tool construction more so than
>> tool output interpretation.
>> Yeah. Which is like the reasoning
>> which is more of the reasoning.
>> Yep.
>> Yeah.
>> I mean that that that seems to track
though, right? Like I think it would be
pretty surprising if if models received
a two output and couldn't parse it that
well. I mean unless it was like a really
oddly formatted output I suppose but
>> yeah so there are some models that are
failing at that as well. So they ignore
it because of the context limitations
and so on. Okay.
>> Uh they can ignore they can they get a
lot of output in JSON format and
whatever format the system is giving
them
>> and it can ignore some of them not put
it all together.
>> I see.
>> Depends on I guess how long the output
is etc. But yeah, typically that doesn't
feel like,
>> you know, context management feels like
something a problem that's been worked
on more so,
>> right?
>> Compared to tool calling.
>> Yeah. But it can stress a model's
ability to like pick a needle out of a
haststack. So it's
>> Yeah. like a really
>> long output dump and you need to like
find the one thing in that.
>> Right. Right.
>> Yeah. Yeah.
>> And then you need to invoke it word for
word, letter by letter properly because
it's a literal function invocation that
the model needs to provide. So it it
makes sense why it fails there.
Okay. Um,
cool. Well, anything else like just key
analysis like things you want to
highlight from from the uh research?
>> Yeah, so um you know one of the key
surprises for us was the soda models are
doing um this badly especially because
when we looked at other benchmarks uh
you know they were getting 70% right or
plus.
>> Uh so that's been a key learning. Uh the
other learning is while we were
developing these we also we assumed that
the difficulty of a task would be you
know common across different models but
something that we saw was the
correlation was quite low. So which
means that models are each of them are
getting good at different kinds of
things. So that's been um you know
another learning which means that for
LLM developers or model developers to
improve their models they have to really
go deeper into you know where they are
failing and then improve those aspects.
Uh they cannot just uh you know focus on
final answer correctness and then you
know um just train based on that. Yeah.
>> Cool. um in terms of like uh model
progress for um MCP and tool use
capabilities like you know tool use has
been around for a while um and we're
starting to see uh more investment on
the post- training side in um RL for
tool use in general
>> right
>> um we're also seeing more investment in
like uh tool use data in uh pre and
mid-training um and so I think uh base
models are getting a firmer
understanding of like just agentic um uh
behavior and like uh uh stateful actions
in general. Um and so I think that will
ultimately uh cascade downstream into um
gains during post training. I also think
that um you know environments uh for
training are going to get better uh and
and I know that because we're going to
play a big part in that um but um so I
think that's going to be a key driver.
Um, but what I think is u is going to be
true is that
>> the environments that we evaluate are
going to continue to get more complex.
So like we're really excited about this
benchmark, but this is just like a
starting point for us, right? Like we
know that we want to continue to expand
the horizon of complexities within our
benchmarks. Um, and so, you know,
>> this captures a lot, but it it's only
step one. Um, and so I'm pretty bullish
that like models are going to improve
here. Um, but there's going to be
another one right around the corner that
that they need to uh um hill climb on
too. So, um, and I think we're going to
be a we're going to continue to be a
driving force for that.
>> Absolutely. Yeah,
>> I agree. That makes a lot of sense. I'm
also very excited about
with MCP, the thing that's most exciting
is everybody anybody can create an
abstraction over any API and then
contribute to this shared registry which
can plug into any model. The more we do
that, the each additional MCP server is
like increases the surface area for how
useful of an application you can build.
And I think that then means there's more
adoption on the user side. So with that
cascading
um what's that word? I'm forgetting a
word. It's okay. Uh
>> use whatever word comes to mind.
>> Yeah, compounding. That's good. I think
I think we will see some very solid
improvements and also very excited about
the environment part and very looking
forward to how people use it, extend it,
add more MCP servers, poke holes in it
too. That's very cool as well. We love
feedback.
>> Um but super excited about this
>> and that's the main I would say ask our
uh users to you know this is a very in
some sense a live benchmark in the sense
that uh the environment is there so they
can you know use parts of the AMCP.
servers there uh create their own tasks
uh create their own ways to evaluate. So
it's a very uh it's not a static
benchmark in that sense. Um so yeah so
ask uh you know uh all all our
colleagues in um companies other
companies universities uh to really
download use it uh let us know what they
think of it.
>> Yeah.
>> Very cool. Well, uh, maybe we can end on
one final question, which is, um, you
know, I think, you know, we've talked a
lot about how MCP, you know, is a
relatively new development. We're seeing
a lot of adoption right now. In, you
know, one to two years from now, like
how do you think this plays a role in
the broader agent ecosystem? Are we just
going to see like, you know, thousands
or like millions of MCP servers, right?
>> Are there any big gaps or bottlenecks
that are, you know, preventing um, you
know, more widespread adoption right
now? like like paint paint paint a
picture of like where the world is going
from here.
>> Yeah, I think I can go and then maybe
you can add on.
>> Um eventually like going back to the
beginning of how we started this a model
needs to be really good at ingesting
information and manipulating the
environment outside of it for it to do
any meaningful work. And so eventually
if we extend it uh and if MCP is the
standard by which all communication
happens between each of these parties
you know it plays a central role it
becomes a critical part of that
infrastructure. Now the part that I'm
excited about most is how this then
plays with let's say computer use
because um you know MCP is just the
standardization of tool use which is
programmatic ways of calling u APIs but
then there's also other ways where we
can uh manipulate information using
computers browser use etc. So I think
MCP combined with other mechanisms the
mechanisms that we have for direct
computer use um very excited for for
that to come together and that might be
you know eventually we can look into
creating benchmarks there as well.
>> Yeah. Yeah. For me I think this again
the first step towards using um static
tools you can think of MCP servers as
deterministic type of tools right but
then what if the other um you know
entity that you are interacting with is
also another agent. So this is a natural
step towards agentto agent uh
communication systems right and then is
a is an LLM or an LLM based agent uh
able to leverage the right agent not
just an MCP tool but the right agent I
think that's where um things are going
and then you know once these agents
start talking to each other uh then yeah
so then it's explosion right so
intelligence explosion
>> yeah I think the the saying used to be
that like software is going to eat
everything right
>> and uh I'm pretty bullish that agents
are going to steal software's lunch and
they're going to be eating everything.
And so I think like in a um and really
the way they're going to do that is
through MCP.
>> So I think you know in a year two years
time um you know basically our entire
digital infrastructure um is going to
have integration uh entry points for
agents um and that's going to be driven
by MCP.
>> I agree. How would agents talk to each
other? Like they is there is you're
gonna are you going to wrap an agent
into an MCP server?
>> Yeah. Yeah. And there are already, you
know, versions of MCP for that.
>> Yeah, there are protocols like a
>> to Okay, that one.
>> That's that's very interesting.
>> One last thing. Um, what's next on MCP
benchmarks?
>> I have the same answer. I'm really
excited to combine um MCP we have this
benchmark. If if it needs to be more
difficult, we'll continue progressing
there. But what I want to do is combine
it with um other modalities and that's
computer use. And so if we can create a
benchmark which tests both tool use and
then computer use. Uh you know I I have
a problem with my VPN right now. If it
could uninstall my VPN using computer
use then pull the docs via MCP server do
all of that. That would be capabilities
that I would love to test.
>> Yeah. Yeah. For me it's uh the
multi-turn continual learning aspect. So
can we actually um you know check for
LLMs if they are able to do multi-turn
um you know remember the interactions
they're having and then you know keep
improving on that. Uh I think this and
then the agent to agent I think these
are the two aspects that I'm really
excited by.
>> Cool. Well thanks guys. I think uh that
wraps up uh this episode of uh chain of
thought. Uh thanks a lot.
>> Thank you.
>> Um for viewers if you have any uh
questions please feel free to drop them
in the comments and we'll get to them
next time. Thanks.
[Music]
