---
id: SOURCE-20251031-006
title: "Trevor McCourt on Probabilistic Circuits and the AI Energy Crisis"
platform: youtube
format: lecture
creator: Extropic
date_published: 20251031
status: triaged
original_filename: processed/SOURCE-20251031-youtube-lecture-extropic-trevor_mccourt.md
aliases:
  - "McCourt - Probabilistic Circuits Energy Crisis"
teleology: synthesize
notebooklm_category: ai-engineering
signal_tier: paradigm
chain_relevance: Intelligence|Expertise
integration_targets:
  - CANON-30300-TECH_STACK
  - CANON-30000-INTELLIGENCE
  - CANON-00004-EVOLUTION
url: "https://www.youtube.com/watch?v=OwDWOtFNsKQ"
synopsis: "Trevor McCourt presents the AI energy scaling crisis: current AI uses 0.5% of US grid, basic personal AI would need 20%, expert AI for all would require 100x grid expansion. Solution: Thermodynamic Sampling Units (TSUs) that use thermal noise as compute primitive achieve 10,000x GPU efficiency for generative AI."
key_insights:
  - "AI energy scaling is physically impossible at current efficiency: basic personal AI assistant would need 20% of US grid, expert-level AI for all would need 100x grid expansion"
  - "Thermodynamic Sampling Units use thermal noise in low-voltage transistors as a compute primitive, achieving 10,000x more energy efficiency than GPUs for generative AI"
  - "Current GPU architecture is a local minimum: new paradigm requires both new hardware (probabilistic circuits) and new algorithms (Gibbs sampling)"
topics:
  - "ai-engineering"
  - "physics"
  - "llm-architecture"
  - "research"
---

## Key Concepts

### The Energy Scaling Problem
- AI has discovered how to convert energy into intelligence, but scaling is physically impossible
- Current AI consumes ~0.5% of US grid (3 gigawatts)
- Basic personal AI assistant: 20% of grid (100 gigawatts)
- Video-enabled assistant: 10x grid expansion needed
- Expert-level AI for all: 100x grid expansion (impossible)

### The Math That Forces Innovation
Formula: `FLOPs = 2 × parameters × tokens`
- H100 efficiency: ~0.7 picojoules per FLOP
- Sam Altman's "1 gigawatt data center per week" = just the text assistant scenario
- The 10-100 terawatt scenarios needed for useful AI would require covering Nevada with solar panels

### Thermodynamic Sampling Units (TSUs)
- Build hardware that samples from probability distributions natively
- Transistors at low voltage are naturally probabilistic (thermal fluctuations dominate)
- Uses Gibbs sampling to break complex distributions into modular operations
- 10,000x more energy efficient than GPUs for generative AI benchmarks

### Probabilistic Circuits Physics
- Low-voltage transistor operation uses thermal noise as compute primitive
- Energy barrier controlled by gate voltage creates controllable random sampling
- Can build circuits sampling from categorical distributions, Gaussian mixtures
- Temperature dependence is predictable and manageable

## Paradigm-Level Insights

1. **Energy becomes THE constraint** - For first time, average person consumes significant HPC resources; efficiency now matters more than speed

2. **Local minimum escape** - Current GPU architecture is optimal for current algorithms; new paradigm requires both new hardware AND new algorithms

3. **Physics dictates economics** - The trillion-dollar infrastructure needed for universal AI is physically impossible without breakthrough efficiency

4. **Generative AI is fundamentally sampling** - Build hardware that does what AI actually does, not what deterministic computing does

5. **Hybrid architectures are transition path** - Combine probabilistic cores with conventional neural networks for practical scaling

## Integration Notes

- Energy scaling analysis essential for TECH_STACK infrastructure planning
- Thermodynamic computing represents alternative intelligence substrate for INTELLIGENCE chain
- Local minimum / paradigm shift pattern relevant to EVOLUTION framework
- 10,000x efficiency claim demands verification and tracking


## Transcript

You can't escape thermal fluctuations. They just inevitably become
significant. So in some sense, like, extropic is a little
Why don't we just create physics-based computing systems that harness
the noise from environments? To us, from first principles of
mathematics, information theory, probability theory, physics, thermodynamics, this
is the future. Hopefully this podcast is like the beginning of a new revolution.
Alrighty, everybody. Welcome to an emergency episode of the First Principles
podcast. We're coming to you on a Sunday
night because we need to understand what the heck Extropic
is building. They've just launched their light paper. Not a white paper, but
a light paper. It is a great introduction to what they're doing and
I've tried my best to dive into it, but I'm actually sort of at this perfect you
know, in between points. Sometimes I know, like, basically everything about what a
company's building before they come on the podcast. In this case, I have lots of questions still.
I actually don't totally understand what the hell you all are building. So
I'm excited to learn. I'm excited for everybody to watch me learn. And I'm just going to throw as many dumb
questions as I can out there. So welcome to the show, guys.
Thanks so much, Christian. Excited to be here. Love your shows. Couldn't be
more excited to share more with the world today about what we've been building
sort of in secret. This is just the beginning of us getting people excited about this
thermodynamic paradigm of computing. And hopefully this podcast is like the
beginning of a new revolution. I'm sure some of your listeners probably
have seen one of my identities. flowing about
online during daytime. I am Guillaume Verdon. I'm
formerly a research scientist in quantum computing, co-founded the TensorFlow Quantum
Project with Trevor here. Back when we were in school,
used to be a theoretical physicist at Perimeter, ended up being a pioneer of
quantum machine learning, which is a field where You use
quantum computers to do a form of physics-based AI
to understand quantum mechanical matter around us, which
is, you know, that's my previous life. Now, essentially,
I'm founder and CEO of Xtropic, and started
this new physics-based computing paradigm and also happened to
run a little thing called EAC to some extent, as
much as one can run it or be very involved since the
beginning. And that's a techno-optimist movement. And
that's sort of the dual identities that many people are
familiar with. But I'll let Trevor
give more of a bio here. I think people are pretty familiar with my
Yeah, I'm definitely not as online as you. Basically,
I'm an engineer who got swept into Guillaume's field. No,
so I met Guillaume back when I was doing my mechanical engineering degree at
Waterloo, which is clearly the best engineering school in North America.
We love our Waterloo interns. I was doing a mechanical engineering
degree. I mostly did manufacturing kind of stuff before
I met him. I worked at a little company called Formlabs, did some stuff
with linear motors. Then I met Guillaume, and he was like, Trevor, do you want
to work on quantum machine learning? And I was like, I have no idea what that is, but
it sounds cool. So that proposal
turned into the Google product that Guillaume was talking about, and
then I got sucked into the quantum hardware physics
and engineering lab down in Santa Barbara. And I did a couple
of years there working on device engineering, modeling,
studying the effect of noise on quantum computers, calibration, control,
pulse sequences, that kind of thing. And after that,
went on to MIT for a bit and got a call from an old friend and
had to come help him out at Xtropic. So yeah, I'm happy to be here. It's been
Absolutely. You guys want to give us the 101, just the highest level. We're
going to dive super deep and feel free in this explanation to
use a bunch of words that people might not know, because then later we'll dive in and try
I mean, essentially, Trevor and I have had
this career trying to build ways to program quantum mechanical
computers, where you try to embed computational tasks into
quantum mechanical physics, right? Quantum is, we're going
to dive into the contrast between quantum and thermo in a sec, but Quantum
is really, you have things in superposition that the physics of the very, very
small and the very, very, very, very cold, ideally as cold as possible,
ideally zero temperature. And there you
get to program the physics of matter,
usually matter or light, and you learn
to embed sort of programs that are parameterized, just
like neural networks. Neural networks have parameters that you train with all
sorts of algorithms that usually use gradients. And that's
kind of where we came from. We brought differentiable programming thinking
to quantum computing. We were very early on on that. There was no software
doing it at the time. And that was our project. And
then in quantum computing hardware,
there you have, the reality is that
you can't cool down a quantum computer to zero temperature, right? And so there's
a mismatch between the program you want to run and the actual physics
of the hardware. The program you want to run runs at zero
temperature, theoretically, and the hardware has finite
temperature. But what does having finite temperature mean? It just means
that things are jiggling. Things are unpredictable. There's entropy. There's uncertainty that
gets injected in your system because your system interacts with the environment,
and we call that noise, right? And so fighting
noise has been the quest to scale quantum computing
so far, and it's been the bane of the
existence of many scientists. So Trevor's background was
sort of at the very lowest level, how you make the
quantum bits dance. Can you filter out noise? Can you deal
with noise? There at the lowest level, I
was more involved at the algorithms and architectures level where
In quantum computing, you try to do a process called quantum error
correction, where you detect errors, detect these
sort of injections of errors, and undo them, right?
And you've got to keep track of how they spread in your computer. The problem
is they're often, by trying to fix the problem, you make it worse. If
the thing trying to fix the problem adds more noise than was there before. And
so, your quantum bits have to be of sufficient
quality, they have to be low enough noise so that it's worth doing
this error correcting process. And this error correcting
process you can view as a form of refrigeration, right? Really,
you're pumping entropy out, you're using energy to pump entropy out
of the system. And so we saw sort of the
road ahead for quantum computing was very long, you
know, reaching the level where you have a very large scale computer where
you're below that threshold of noise where it's worth scaling
up. There's a long road ahead for that. And
we sort of lost patience there. And we're like, well, if you can't beat them, join them,
right? If you can't beat the noise, you should use
it, right? And so we were thinking, Well,
what if we could use the noise? These general AI algorithms, right?
The parent concept is probabilistic machine learning algorithms.
All these algorithms want to be probabilistic, right?
And so they want this sort of entropy and uncertainty present. And
it turns out that even when we run things on digital computers that
are nearly perfect, right? They're deterministic. we
end up sprinkling in noise at sort of a very abstract level in
our software later on, right? Not at the sort of analog
hardware level. And so it seemed like we do all this effort, just
like in quantum computing, we have all this effort to keep things pristine, right?
And in digital computing, You use a lot of power and
energy so that your system is hard to disrupt. The
noise of the environment is trivial compared to the amplitudes of the signals. And
so there, things are very, relatively
to the amplitude of the signals, not so noisy. But then at
the algorithmic level, you add the noise again. So we were like, why don't we just simplify
that and just create physics-based computing
systems that harness the noise from environments
sort of above the sort of temperatures and noise levels of quantum
computers, but noisier and
lower power than deterministic computers. So it's kind of
this in between, right? So we're trying to build a new paradigm of computing from
the middle out in terms of scales. Had to
That's kind of a top-down explanation. There's also a bottom-up
version that's pretty compelling. Yeah, go ahead. If you look at what it takes
to keep making computational devices smaller, what
you find, and it doesn't really matter what the device is, what you find is when
you make it sufficiently small, you can't escape thermal
fluctuations. they just inevitably become significant,
right? And so if we want to keep scaling computes
smaller and smaller, it's actually inevitable that you have to
go into this thermal or probabilistic regime, right?
And this is becoming, you know, if you look at the data for
like digital computer scaling, you can see that the
rate of exponential growth in efficiency of
computing technology is starting to slow down. And
that's because you're starting to hit some of these effects. There's a ton of reasons
why it's hard to make transistors small, but a lot of them come down to
the fact that these thermal fluctuations are starting to get really big. So
I expect within the next several
generations of transistor technology, you're
going to have to start looking at some of the things we are. So in some
sense, Extropic is a little bit inevitable, and
we're just trying to front run the danger
Yeah, that's really interesting, because you've hit on two different types
of computing. The top-down answer kind of came at it from the quantum angle, and
then this bottom-up one that you just answered, those are just normal
digital chips or whatever that we're talking about, just normal digital transistors. I
would love to take this conversation sort of piece by piece. Maybe let's start with
the first paradigm, which is just normal computing. talk about what
are those chips, like how are they, you know, they're getting down to the nanometer,
like single low digit, like two or three nanometer size
now. So let's talk about that. And then let's talk about quantum and then we can kind of use
that to bridge over into thermal. But on the
quantum, so on the classical note then, do you mind just telling us how these
algorithms and, you know, all this, you know, neural network stuff
is run today? Like, what are those chips? Like, what do they look like? How do they work? And
So to start at the very, very low level, right, what
is a transistor? Yeah, exactly. A transistor is
actually many things depending on what kind of voltages you
put into it. But in the regime that digital computers operate today, transistors
are switches, right? And you network these switches together
to do digital logic. And so The mathematical abstract
thing you're trying to do is Boolean logic, and the way
you embed that in physics is by driving transistors
really hard. And so that's how computers today work, right?
So you're taking these kind of inherently fuzzy
devices, right? They're made out of real matter, so they're fuzzy.
And you're applying very large signals to them so that they behave like
this mathematically abstract object of
Boolean logic that you want. Right? So that's kind of
how digital computers work. If you want to run, let's
say, a sampling algorithm on a digital computer,
which is what a lot of probabilistic algorithms come
down to, that's kind of like one of the main subroutines, because
the dynamics of your device are completely deterministic, right?
They're operating in this kind of high signal regime where the natural fluctuations
of nature aren't important. you have to generate pseudo-randomness,
which is instead of harvesting the noise of nature,
you run a circuit that has really complex and uncomputable dynamics,
right? And so you get kind of streams of bits that look random. And
that process takes a lot of entropy, right? Because a random stream
of bits is kind of like heat in the sense of
connection between thermodynamics and information, and you're using electricity
to produce that heat, right? So it's like you're running an electric heater on your
chip, literally, is the analogy to thermodynamics, right? And
then, okay, so now you have a random bit stream that's not computationally useful
unless you happen to want to do coin flips, right? So then what you have
to do is you have to take that random bit stream and essentially filter it to
get samples from the distribution that you're actually working with. right?
And that step of filtration also takes a ton of energy because
now it's like you're taking this bowl of heat you have and you're putting it inside of
a freezer to cool it back down a little bit, right? So the
process of sampling on a digital computer is thermodynamically
pretty similar to running an electric heater inside of a freezer to
achieve some kind of intermediate temperature. So it's a little bit ridiculous, right?
When you look at it from that perspective, it's like, this doesn't make sense, but it's
clear how we got here, right? Because digital computers are really nice and they're
very easy to scale. So it's convenient to do things this way,
but it's from first principles, it's not even close to the best ways.
Yeah. This approach to sampling is like so inefficient on
digital computers that people, unless you're like on a Wall Street
where things are super mission critical and you're willing to throw a ton of compute to
get the best quality sort of uncertainty for
your decision-making, unless you're on Wall Street, you end up trying
to avoid sampling entirely, right? Because it's
too costly on our deterministic devices. Again, as Trevor
mentioned, it's really unnatural for our deterministic devices to be probabilistic. And
so another way, instead of sampling, to represent probability distributions is
usually through deep learning. And what deep learning does is it usually
starts with very sort of trivial randomness, like
a Gaussian blob, a single Gaussian blob, and then it deforms that
blob to shape it into the shape of the data. So it's
a high-dimensional blob, and high-dimensional data could be like images,
text, whatnot. But it has to use many, many transformations
to take that very simple randomness and transform it into the
shape of the data. And very often, that sort
of fails to capture the tail events, the
tail distributions, a low data regime, right? When you're focused
on like covering everything with one blog, essentially, you're
just going to cover sort of the center of mass or like, of
probability mass, like the typical data, right? You'd be focused on
that. And you're going to need like, more and more and more dimensions and
more and more parameters in a deeper and deeper
transformation that's more and more complex. So you need more parameters, more
data, more compute in order to reach in that sort
of low data regime in those tail events that are very rare,
right? And so we've been seeing that with sort of self-driving cars.
In self-driving cars, we've just been throwing metric
tons of data at the self-driving problem to
reach a level that a human reaches with like 10 hours
of driving classes, right? And there's clearly way more than 10 hours
of data in all the data sets of all the players. And
so that's sort of fundamentally the reason that
current day deep learning is not
quite the end game. We think that this sort of probabilistic approach
where you can use very little data and you
can fill in the blanks with noise, with entropy and uncertainty, Right?
If you don't know something, you don't have data, you should fill it out with uncertainty.
But that process of sort of painting everything with
a noisy brush is very costly, because you got to sample,
you got to like, you got to explore those parts of landscape, you got
to kind of hallucinate everything that's not data, or,
you know, within your model, within the scope of your model, and sort of penalize the things
that are too far from data. And that sort of process of hallucinating
all these possibilities and making those corrections, for
the technical folks, it's called contrastive learning. That
process usually requires sampling, and that's very costly, so
people avoid it. So they stick to these sort of taking these Gaussians and
deforming them. That's how old school Old school neural
nets like variational autoencoders work. It's somewhat how
diffusion models work. Diffusion models kind of mix in the noise as
you go to some extent, simple noise. But
that's kind of the common pattern essentially. So both
from a sort of hardware standpoint, it's inevitable
that we're gonna have to go stochastic because matter is
jiggly and so your transistors are are technically jiggly,
and so will the electrons hopping across it. And so it's going to
get stochastic. And the algorithms want to go probabilistic to
be more data efficient. And so that's why we're building the whole
stack. And we think it's going to be disruptive for everyone. And that's why
we're really excited to sort of put our thesis out there of
the future of AI, which is very contrary and very different, but if
it succeeds, it changes everything, right? And so, at
least to us, from first principles of mathematics, information theory,
probability theory, physics, thermodynamics, this is the future. And
Yeah, basically. I love
it. So to take just a tiny step back, can you talk about what
is it that makes a GPU so good at
doing that sort of estimation task, basically, of
making it so that you have this really crazy distribution and
GPUs do the deep learning approach, right? Because they suck at
the sampling approach, right? So often people use
CPUs for Monte Carlo sampling because
it's a very serial task. You gotta like have little walkers that travel. You're
simulating a sort of particle in this landscape, whereas we use
literal particles to do that job, right? So
a GPU really got lucky, right? A GPU was not
imagined from first principles to be a processor for
AI. It was a graphics processor that did
really well with matrix multiplications. And
it turns out that, you know, these transformations that I was talking about
to morph a simple distribution into
a complicated one, a lot of those transformations, the
big computational element, are matmuls, matrix
multiplications, right? And so GPUs are accelerators for
that. And so most attempts that you've read
in the news or over the past several years that
have been trying to accelerate software
for AI, they've been focusing on accelerating matrix
multiplication, which first of all, you're competing with NVIDIA. Good
luck with that. Jensen will eat your lunch and thank you for it. But
Trevor, you have some first principles reasons why you think And
from the back of the envelope principle, you know, any sort of matrix multiplication
accelerator has a fundamental bottleneck, and
it's not worth necessarily pushing in that area. It's much more
interesting to try to disrupt how
you do the entire algorithm rather than just a subroutine, right, Trev?
Yeah, so the basic reasoning here is if
you go into PyTorch or something and profile a
neural network like a transformer, right, what you'll
find is that you spend about 25% of your time
moving things in and out of memory, right? So what
that means is if you accelerate the other 75% down
to zero time using your fancy accelerator, maybe some
kind of optical MatMul accelerator, right, that literally does the math of
the speed of light, you still only have a 4x speedup because
you're still paying the 25% of time to move things
in and out of memory, right? So accelerating part
of an algorithm only ever gets you kind of a modest speedup.
And so you do a lot better if you look at tasks that are much more
compute bound, like sampling. So
that was kind of another reason we thought this
Is there a reason that you can't do, so I'm, this is maybe skipping ahead,
we haven't really talked about this yet, but you hinted at it when you said that, hey, this
Gaussian, whatever, this like normal distribution
thing isn't gonna be the answer for the future. Like
you wanna do different types of probability distributions with your
chips, right? And can you talk a little bit about why that is? Like what is
so wrong about this normal distribution? And then why
can't we just do those other distributions with normal, like analog or
Yeah, that's a great question, actually. We
use Gaussian or normal distributions, right? It's basically what
is known as a bell curve. We use those all the
time because we can actually keep track, like
fundamentally, what is a Gaussian? It's like a blob, there's
where is it in space, and then how is it squished along which
axis, right? And by how much, right? So
the squishing is a matrix called covariance matrix, and the position is
called a mean, right? And if you have that vector in
a matrix, you fully specify the distribution. So essentially,
it's a way to cheat and have deterministic computers represent distributions,
because they just need to store a matrix and a vector. And they're they have
a proxy for distribution. And you can sort of analytically for
many simple transformations, keep track of how the
Gaussian gets morphed, right? And these tricks
are actually why diffusion models work so well, right? Diffusion
models, they approximate every transformation as like a
slight transformation of a Gaussian. And
so essentially, it's kind of an artifact of them being
some of the, I mean, obviously the simplest distributions you can come up with. And
essentially being easily representable by a classical computer. If
your computer can natively represent much more complicated distributions, we
wouldn't have that sort of bias, right? And the
problem is, you know, there's distributions that have much longer tails, right?
They're not just so concentrated around one
mode. They have all sorts of, you know,
blobs and long tails where, you
know, a very, you know, very low likelihood event
still has, like, a non-trivial probability, whereas Gaussians, as
you get far away, you know, they get, like, more than exponentially low
probability as you get away from the mode. And so, you
know, many machine learning algorithms and machine learning algorithms are
really good at modeling the typical case Right.
And we feel this with LLMs. Right. They're kind of like basic. Right.
Like they're really good at like typical things, but like, it's like, I
need this sort of like edge case. I
need this sort of edgy thing. Like they can't, they can't go there with
you. Right. But human brains can. Why is that? It's so weird. Right. Like, just
like if we, if you're driving and you
see something that's never been in a dataset on the road, you don't
like glitch out. You like, you generalize. Right. And so.
Fundamentally, it's like the constraints of
the hardware, deterministic hardware has constrained our thinking in
terms of where the algorithms are going and
where they should stay. And that
has sort of held back AI. So something, you
know, our ultimate goal here by proposing new hardware is
to also disrupt how software and AI
works and which algorithms tend to dominate and do well when
But what is it about those algorithms that make it impossible or
impractical to model them using a classical computer? It seems like,
I don't know, when I was a stats monitor, I could do a little binomial
plot, you know what I mean? That's a non-Gaussian distribution. What
I mean, if you try to sample directly from a hundred million dimensional distribution,
right, you know, directly without using
Well, the fundamental reason, right, is like, if I have,
let's not go to a hundred million dimensions. Let's start with one and two.
If I have a one dimensional distribution, right, that's just a
function in 1D. So I can slice that function up
into n chunks and store those n chunks in memory, and now I have a
representation of the distribution. Now I go to two
dimensions. Instead of having n chunks, I have a
grid of n squared chunks. So now I
have to store n squared things in memory to represent the distribution
in generality. What if I go to d dimensions? If
I have n slices along each dimension, I have a d-dimensional hypercube
of things to store in memory, which grows really fast, right? So the
general point here is that the complexity of representing a
totally general probability distribution tends to grow exponentially
in the dimensionality of the system. Right. And so, um,
and obviously there's like a lot of caveats that argument because the
representation, uh, like the complexity of the distribution doesn't
have to be exponential, but it can be. And that's kind of the key thing that makes
this difficult on a classical computer. Um, you
can't store them in memory. So you have to sample and sampling has all of
these problems I discussed earlier. So dude, you're just
And so is this something that, was this thought, like this kind
of train of thinking, was this what led people to want quantum computers in
the first place? It's like we can represent these super high dimensional aspects
of reality by just remaining high dimensional, by
Yes. Yeah. So that was a big, so back
in our days in quantum computing, I would just keep hammering home Don't
use a quantum computer for probabilistic machine learning or classical machine
learning, as we call it, because quantum computers are really good
at quantum interference, not necessarily probabilistic inference. Yes,
you can. It's kind of like using a
rocket that's on, you know, rockets are finicky and
less reliable to ship something across town. It doesn't make sense,
right, intraday, right? It doesn't make sense. It is gonna blow up. You
know, there's a chance it's gonna blow up. Like, why would you do that, right? Sure,
like, in principle, it could go much faster, but, like, there's
a chance it could blow up. So what we've seen is sort of, yes,
on paper, a quantum computer can do slightly better
for probabilistic inference. I've written a bunch of papers on this, because I
wanted to, like, rule it out properly, right? So I've spent the
last eight years, I guess I put out my last paper in this space, a
week ago for fun, because it was on my shelf for two years, but I
thoroughly studied, can you do classical machine learning on a quantum computer? It
seems to me like the main advantage is instead of
having sort of jiggly particles that hop above sort
of barriers in landscape, you can tunnel through. So there's an
advantage if your landscape has very thin barriers, because you
have a form of quantum tunneling, right? So sometimes,
like in very special cases, you can find an
optimum a bit faster, but when you do the whole systems
thinking, the full stack thinking of like, okay, I
have a quantum computer, I'm gonna have an error correcting system that's like 99% of
the computer, 99% plus of the computer is the error correcting system, and
I'm gonna have the cooling, and I'm gonna have the control systems, why the
heck am I going through all that trouble for this tiny speedup, right? So basically, it's
not worth using a quantum computer for these sort of low order polynomial speedup,
these sort of, hey, you know, like, I
get a square root speedup, and it's still slow,
it's still relatively slow, and I have to prop up this huge
computer to do it, when you could do it
just, you know, much cheaper on even a classical digital
computer. And so in our case, instead of trying to seek
sort of asymptotic, what is called asymptotic speed ups, like in quantum
computing, like there's, there's literally different complexity classes,
if you have a quantum mechanical computer versus a classical computer, we're
just, we're not trying to violate any sort of laws of complexity theory, we're
just doing, you know, Classical algorithms, algorithms
that you can simulate theoretically on a classical computer, we're
just doing them way faster by a large, like
sort of constant factor speed up, right? And
that constant factor speed up is several orders of magnitude.
sometimes more than can fit on one hand, depends on the algorithm.
But before we pin down exactly
what those speed ups are in the public, we want to put
out some careful scientific works. So stay
tuned for that. But it's very substantial. It's enough that it's
worth going through this exercise of rebuilding
the whole stack from first principles, right? That seems like a huge change,
right? We're taking a fork in the tech tree. We're forking off
the root node. That seems like a huge effort. Is it worth the payout? We think so,
at least from first principles. And so that's why we're really
excited, you know, and that's why we're kind of, you know, we've been
very secretive. Unfortunately, I got As
we know, I got doxxed in December. The plan was always to reveal more in
March. And so here we are. So it's right on schedule.
But our goal here is for people to be open minded about
the future of AI. I know right now it just feels like the
current labs doing LLMs, that's the end game's future. They've
captured the market. It's over. You either work for one of these companies or
you missed out, right? I don't think so. That's the beauty. of
disruption. That's the beauty of this sort of techno capital acceleration. A
couple of crazy kids, you know, with one
or two GPUs can have an idea that can, you
Yeah, that drive, like the reason behind
that makes a lot of sense. I think that the promise of
quantum computers, at least the way that I understood it, was that eventually they're
going to be so, they're going to get, you know, n squared number
of operations in the same amount of bits or whatever. So
we're going from bits to qubits. And when we have qubits, like
pretty soon we're going to have quantum supremacy because you can see like even
the biggest classical computer will be so much smaller than this puny, you
know, or even this very small quantum computer. But
there are problems. There are things that it's not simply captured in
the number of bits or qubits. There are other considerations that
you have to have when building a quantum computer. And I imagine that you two probably have
very strong opinions about that. So I would love to ask you about that. Maybe Trevor,
There. So for stars, it's funny you mentioned quantum
supremacy. The way we achieved quantum supremacy back in the
We were there. We were there a thousand years ago when it happened. Only
Yeah. Back in the day. The problem
that I have with quantum computing, and the main reason I stopped working
on it, is because most of the phenomenon that
are important to humans do not have long-range quantum
coherent effects. So all atoms are governed by
quantum mechanics, but things that are macroscopically observable, that
involve a large number of atoms, don't
need to be simulated on a quantum computer, right? Like our classical models
of them work really well. And so that's one of the fundamental reasons
it's been difficult to find a practical advantage in
quantum computing, right? Like we have these kind of, you know, there's like
a Shor's factoring algorithm, which is like the most common
thing people tout that it's going to like break RSA and whatever, and it
might, but we can just use a different crypto protocol
that isn't broken by a discrete log and
such. So it's very unclear,
even if we had a big quantum computer, what you would do with it.
And that, to me, kind of made it hard to
dedicate my life to it, right? Because the physics
and engineering challenges involved in building quantum computers are
extremely formidable. And after you do that for
I, you could see that Trevor worked close to the metal where,
you know, the challenges are extremely hard. And, you
know, I was a theorist and an algorithmist, you know,
a bit isolated away from the difficulties. I was aware of it
because I would talk to my neighbors and so on. But, you know, the ideal
thing with quantum computers is that they can represent
and sample from states of very high quantum complexity, right?
So, if you have a state of very high complexity, but
it's still, you could still sample from it with Monte Carlo, you
could just run, again, a Monte Carlo algorithm, maybe it's a million times slower than
doing it by nature, but it's still, you're still going to
get there. You know, you just throw a lot of compute at it, you're going to get there, you
know, it scales linearly. The thing with quantum complexity is
that it scales up in some cases super exponentially, like
in terms of how much classical compute you need to use in
order to replicate that distribution. What was achieved in the
Google quantum supremacy experiment and then later surpassed by
Chinese simulations and then reiterated by Google
quantum, so it's been kind of a little race there, but
essentially it was just sampling from any sort of quantum
program that you can't sample from with a classical
computer, even if you were to throw most compute on earth towards
that end. And that was achieved, I would say,
so I don't think there's anything stopping us from achieving
that. I know it's still controversial, but essentially
the promise there was that, okay, if we can show we can sample
from these complicated distributions, right? The narrative, at
least for the quantum AI side, was that, okay,
well, if we have these classes of distributions, maybe
we could search over that space and represent very highly complex states
in nature with these complicated distributions on our computer, right?
And then map one to the other, and that unlocks the ability for us
to sort of understand matter at a quantum mechanical level.
There, there was a lot of challenges to train such such
distributions because when they get really complicated, they get really
hard to train. It kind of is a sort of conservation of difficulty. So
until the hardware gets much better, it's very hard. for
you to use a quantum computer, even if you're trying
to just generally model nature in sort of native fashion,
right? You're trying to model quantum mechanics of nature with a quantum mechanical computer,
running a quantum mechanical AI representation. It's still difficult because
if the computer's not reliable enough, you can't make it big enough, you can't run
the easily trainable representations, and you're kind of screwed. And
so from the algorithmic standpoint, it was also sort of doomed
in the near term, I'm more of an optimist than Trevor. I think,
you know, humans are really smart. I think on a 20 year time
scale, people are going to figure it out. But again, for us, it's like, okay, we're
trying to do all these applications where it's not clear that
you need quantum complexity, right? Really what you
just want is a computer that allows you to do probabilistic
machine learning and optimization very
cheaply, very energy efficiently, and very fast. And
for us, it's like from first principles of thermodynamics of computing, it's
not going to be a digital computer, it's deterministic, it's not going to be a quantum computer, it's
going to be a thermodynamic computer that achieves that. And so that's what we
got to build. And so that's why we left all the secret labs. You
know, I was at Google Apps working for Sergey and Trevor
was like a different black ops lab in Santa Barbara. And
then we joined forces. We both kind of left that. And
now we're here. And now we have this thesis that
we've kind of kept close to the chest. But, you know, now
we're telling it to the world and we're asking if people want to join us. And
Yeah. And one more point on quantum computing that's interesting
in contrast to what we're doing at Extropic. To build
a quantum computer, you have to build some really weird system at large
scale. So that might be superconducting circuits where you're
making Joseph's injunctions, which are not new, but at
least a relatively new object, you might be doing neutral
atoms where you have to build these big arrays of optical tweezers and tables
and tables of lasers. Trapped ions is very much the same thing.
My point here is that the kind of manufacturing and supply chain
for all of these things is extremely immature. And so there's
going to be decades of challenge just there, achieving scale, right? Versus
if you build a thermodynamic computer, what you need to do that
is a noisy circuit. And I can think of lots of ways
to make noisy circuits that lean heavily on
the way we know how to make circuits today, right? Like the whole semiconductor industry.
So that's ultimately what we're chasing here is something that
we can do, you know, in this decade, not several decades from
Yeah, so that's a perfect tie-in. Let's just hop right in and
start talking about what you guys basically announced in this light paper. I
mean, you mentioned Joseph's injunctions. That appears strongly
in the light paper. We
talked earlier about having to keep quantum computers extremely cold, and
I believe that that also is true of this first wave that you've announced
here too. I don't know, from a first blush, I would imagine some
people would think, well, it sounds kind of familiar. What you just said is like, you know, hard to do.
So what's the value there?
We're starting within our neighborhood and we're taking a path
to sort of room temperature and large scale manufacturability, right? We're going
from the bottom up. We're going from the very cold, using similar building blocks
to what we're used to engineering and quantum computing and operating
them in a thermodynamic regime where there's no more quantum coherence. There's
no superpositions of states anymore. It's just fuzz,
probabilistic fuzz over states. And that's where we're operating the
devices, right? And for us, it was just our native
language. It was the first sort of concept of a programmable and
parametric thermodynamic computer we thought of
building. And that was basically our first prototype. And
for us, there's a lot of learnings there of like, how do you even program this thing?
How do you map all sorts of applications to it? What is programming gonna
look like? How fast can it get, right? And showing
the world, hey, this is how efficient you can have neural
computing, computing for AI be and how fast it can be,
fast and efficient, speed and efficiency. It's
very similar to the Tesla Roadster, super expensive, very
exotic, had to import a bunch of parts from all
sorts of suppliers, wasn't vertically integrated yet. And
then that's a stepping stone towards a large scale mass production, in
our case, eventually room temperature. chip that we're going to build.
And we have a roadmap to that. And so for now, we're
just showcasing the world what's possible. Hey, you
have this new paradigm that's coming, we have a first instance of it, but
we have a roadmap to get to sort of having a thermodynamic
Yeah, like in CMOS. So like, you
know, the same way you make your digital computer that you're likely watching this
on, we know how to make thermodynamic computers using
the same manufacturing technology that operates at room temperature, which
So how do they work? What's the, you know, what's the,
like, can you explain the 101 of what is
Yeah, I mean, let's talk about, let's focus on the superconducting chip,
that's the one we're disclosing, the CMOS stuff, you know, we're keeping
on a high level for now. It's the same concept, a lot of the software maps over
in thinking, but it's, you know, just like in quantum computers, you can have
different substrates, right? There's optical ion trap, you
know, photonic superconducting quantum
computers. There's many ways to do it through a computer. This is
a first way. There's gonna be a better way later, but for now,
we're talking about this one. So this one, Trevor's
going to give you a much better, more technical explanation. But essentially, we're
just using jiggles of electrons that happen in superconductors. In
superconductors, electrons like to bundle up. They like to pair up.
They're called Cooper pairs. And when they pair up, they can pass through each
other. That's why there's sort of no friction, you know, there's no
traffic congestion for your electrons in superconductors. That's why they're
superconducting, right? They have way less resistance. For us,
the superconducting aspect is more to have a
sort of non-linearity in the landscape. So that means not it being
a simple Gaussian, right? So if you have a simple LC circuit like
you do in high school, you know, and you add some, some
noise to it, you're going to get a Gaussian out of it. But we didn't want
that. We wanted programmable. super general, fully general landscape.
Essentially, what we do is something called energy-based
models. I'm more on the software side. Trevor's going to give you more
of the hardware side picture. But energy-based models
are models where you try to model data
distributions as equilibrium states called Boltzmann
distributions of certain parameterized landscapes. So
essentially you shape some hills, right? We
have little knobs that we could tweak and it changes
the shape of some hills and we pour some
sort of, you know, just a bucket of bouncy balls
and keep shaking it as we go, right? And that's it,
right? And then the algorithm is just changing this landscape over
time and the bouncy balls kind of flow. But, you know, on average, the
probability mass of where your bouncy balls are. kind of changes and
we guide those bouncy balls. For us, the bouncy balls are literally
electrons, but theoretically, you
can make it out of all sorts of other stuff. But in
our case, that's it. Essentially, we have a programmable probabilistic
computer that has parameters that you can train in
order to morph this sort of equilibrium distribution of
the bouncy balls by morphing the sort
of landscape in which they're dancing. And
we have algorithms that are physics-based to tune that sort of landscape
that correspond to machine learning, you know, like cross-entropy
minimization, which is what transformers do and diffusion models do,
amongst others. And so essentially there's a
connection between, you know, machine learning really is operationalizing
information theory, information theory and entropy, right? The
theory of entropy from Claude Shannon. appears in thermodynamics as
well, right? So we're instantiating information theory as
thermodynamic processes. And so that's the bridge between machine learning and
Trevor, do you want to go, Trev? Yeah. Sure. I
mean, actually, you kind of have absorbed my talking points at
this point, so that was pretty close to what I
would say. I'll add a layer of
generality. In a sense, any circuit you build experiences
thermal noise, so that the charges that are moving around your circuit
are getting battered around by vibrating atoms. So
every circuit you build works that way. The
trick in designing something that's not
just kind of noisy, but very noisy, is
that you have to make sure that the noise is
significant compared to the other energy scales in
your device. Right, so that's kind of where the device physics
and hardware engineering, more hardcore stuff
kind of comes in. But once you figure out how to get into
that regime, basically all you need is some kind of circuit component
that's tunable, that lets you kind of change where
the electrons prefer to sit. And that
gives you a programmable sampling machine,
basically, right? So the principles at play here are
pretty generic and you can imagine a ton of different ways
to build it. And so we're just kind of thinking like, well,
what's the most scalable thing we have? semiconductors.
So basically, I think the thing that is still confusing to me is like,
what's the input and what's the output? So the input, as I
understand it, is you're giving like weights or whatever to each
of these things, each of these, what would you
I mean, it's like a neural network, right? You have inputs, like data, and
then you might have outputs, and then you have parameters. And those are
So you have the parameters which you input, which are the ways
To be more concrete, I think that'll be helpful. You could think of
like data and parameters as voltages, right?
So I apply some voltage to the circuit, which changes
how it behaves in some way, right? And that changes the distribution that
the charges will follow, right? And when you want
to take something out of the circuit, what you're doing is
observing it. So the circuit will
have a bunch of degrees of freedom that are kind of moving randomly under
the influence of thermal noise. And basically what I can do is I
can hook an amplifier up to the circuit and measure one of
those signals. And so doing that lets me observe
the random dynamics of the circuit. And if I do that over
and over again, as long as I leave a long enough time in between observations,
In the bouncy ball analogy, right, you have your landscape, you poured a
bunch of bouncy balls, still shaking a bit in this landscape, right?
Eventually it would equilibrate to some sort of distribution. Sampling
is like applying a sort of porous grating on
top and letting a bouncy ball sort of hop out. And
from that, you can infer where that bouncy ball comes from. That gives
you one sample, one bouncy ball from the probability mass
of where they all are, right? So that gives you one snapshot. If
you take many snapshots, there's all sorts of algorithms that you
can use those sort of what are called estimators of where the
distribution is as a sort of
signal, either for learning or inferring what values
you're predicting, right? That position could be like the
value of a pixel, an image, right? But
you have probability distributions over everything, right?
Yeah. Interesting. So is that, so the
translation from thermal land back to normal digital
land, I assume still has to happen. Like you still, in order to show something
on my screen, which is a digital screen, like I need to get those
values out. But that's what you're talking about right there. You're saying that whatever we're
basically, you're able to sample and pull out these electrons
or whatever they are, see where they fell, and then that
gives you the value that you need for like a color or for a letter
You're going from this cloud of bouncy balls to, okay, this one is
definite, now I have it, it came from here, right? So, that's a deterministic sample
out of a probabilistic sort of distribution, right? And
so, and there's this old, Yeah,
there's this old thought experiment called Maxwell's
Demon that if you observe a
probabilistic system, it's going to cost you energy to get that information. So for
us, our goal, instead of having to sample
a lot from the device and always have to relay things with
classical computers, we're trying to do as much as
possible natively in probabilistic physics because that's much lower power.
It's going to cost less energy because observing things costs energy.
And that's sort of like what, so one of the things
I understand is like wrong or whatever with quantum computers is that step basically.
Like how do you get the thing out of the quantum, like qubit representation and
put it into a normal, like classical bit. And so are
there similar problems that you run into in this thermal world versus in
the quantum world with that, like basically with the, you
know, that pulling out of the other regime into the normal regime? Like
I imagine in this world to be more specific that you're,
the thing reading the voltage or whatever could be itself noisy. And so you
don't know whether you're actually getting the value that you intend to
get in the translation step out of the thermal system.
So that's where the real work comes
in, right? Is how do I design these various circuits to
In quantum computing, it's called the readout problem, right? It's like I'm
at the quantum regime where we're down to literally few
quantums of energy, right? That's where the word quantum comes
from. We're a few more energy
packets than quantum. We're a bit higher energy than that. But
still, for us, it becomes a problem of amplifying that signal, right?
So ideally, you don't want to have to
have your observations get off of your thermodynamic computer or your quantum computer
into a classical computer and then back. That's very slow. In fact, that's been
a problem with most quantum computers today. If
you try to use them for these sort of quantum deep learning
algorithms, that iteration loop to optimize your parameters way
too slow. Getting those samples out and then getting
that feedback loop update way too slow. And so our
insight is that eventually we want to do that as physics, as
a physical process in the device. And so,
And basically, whenever you want a signal to
travel far, you need to amplify it a lot, right?
Because there's more, like when a single has to physically travel
further through some like weird environment, right? More noise hits it.
And so it's kind of interesting about our approach is you could imagine putting
a lot of this stuff in the same package, right? It's
a CMOS all the way down. So potentially we'll
Huh. Wow. Okay. This is sort of breaking
my brain, but in like a good way. Like I, it's like, it's coming together.
Like, I think, I think I'm picking up what you guys are putting down. Um, I,
so I have a question about like, basically if there's an analog
to like coherence here, like quantum coherence is obviously a
big problem where you can, you did the thing just collapses and
that it like loses its quantum properties. Basically. Do you, does
that happen to you guys when things are, um, like too
big basically because there was a part of the light paper where you said we
got to keep it small we got to keep it low power because then these crazy
So we explicitly don't have quantum coherence, to
be clear. Quantum effects are actually important in
transistors. That's one of the things that limits how small you can make
them is quantum tunneling. But there's a difference between observing
a quantum effect and having a coherent quantum state. Quantum
tunneling in CMOS is not coherent because it's at room temperature. So
that's one tangent. I think the closest analogy
we have to that is if you have a device that's too
big in the right sense of big, you end up
with technically still probabilistic, but
I would say metastable systems in a sense that
if I have two wells with a giant energy barrier between them,
It's very unlikely that thermal noise is going to ever kick you over that barrier, right?
So that thing is going to look more like a digital bit. And so you have to
So for us, it's like the opposite, right? So quantum coherence is
like, it's like the time until your quantum
computer starts to thermalize, until the noise starts seeping in and
affecting things. We want the noise to start seeping in as fast
as possible and for things to equilibrate as fast as possible. So we
have something called the thermalization time. And we want that to be fast.
So for us, it's actually the opposite. We want more noise and
it helps us go faster in many ways. And so
that's the lesson we learned. Instead of trying to extend coherence
times, it's like, hey, nature wants to thermalize. Let
it rip, right? And so let's use that. Let's
use that natural tendency as a building block for our algorithms.
And so it's kind of dual. It's like the opposite of coherence time.
It's like decoherence time. How fast can you decoherence? Yeah,
exactly. So it's like switching sides, you know, half times.
Yeah. Very cool. So what I imagine that when
you both started out on this, and maybe this is a good time to talk sort of about your backgrounds, but
or like how you guys got to, we talked about a little bit at the beginning, but I'd
be curious, like, I imagine at the very beginning of this project, it
was like a glimmer of an idea. And you were like, okay, probably
it's not gonna work, but like, maybe it will. And that will, how sweet would that
be? But then now, you guys have so much further
down that path of like actually building some chips. Like I saw your
little chip at that party, Gil. And like, it's
so, you're so much further down the idea maze and
like the, you know, you must have more confidence now. So I'm curious to
hear, like how much more confident are you that this is actually going to
We have a lot of confidence that the
local neighborhood of ideas we're exploring here with sort of the intersection of
probabilistic machine learning and stochastic electronics is
the future of computing for AI. We
have a couple hypotheses of what that looks like, and we
got a couple bets in that sort of local neighborhood. We're not even married
to one substrate, as you can see. So even in terms of algorithms, we have
a couple bets there. But we're pretty sure that
something in this neighborhood is the future from first principles. And
we've built that conviction from doing these investigations and
having a larger team to sort of paralyze our learning over the
past year and a half or whatnot since the founding. For
me, this idea was a super slow simmer over
the past eight years. Well, eight years if you include time at
Xtropic. And it was an idea that seemed so crazy that
I thought I had lost my mind or something. And I wanted to sanity check
by working in quantum computing, like, hey, we're going to learn a lot
about how to do physics-based computing and imbue AI
into physical systems with quantum
AI, and those learnings will bring to sort of this
alternative form of computation. And so, you
know, that's been a sort of slow exploration in the idea maze, like
Backburner idea, but then I think I think the point of
going all in and burning the boats, right? Like, turning
down every big tech job, selling everything, moving back home with the parents. Obviously,
I don't love my parents anymore. But, you know, that
was a big move, right? Swallowed a lot of my pride, but then I had a lot
of skin in the game, right? It's like, I either make this work... You
only have one life, right? If you have an idea that you think is your
greatest idea of your life, that you think is gonna have the most impact to helping civilization,
you gotta go all in. And so, at that point, going
all in, was what we needed. And then,
you know, getting Trevor on board was a matter of time. Just
had to convince him to drop out from MIT. That
took a couple months. But, you know, and at that point, once he came
in, you know, things really accelerated. Because, you know, we've worked together before.
We shipped TensorFlow Quantum. Again, that was a similar
scenario. It's like, there is no adults in
the room. There's no guidance. The field didn't exist. Big
tech people were asking us where it's going and to
build it. And the best way to predict the future is to invent it
and build it. And that's what we did back then. And that's what we're
doing now again. So Trevor, do
you want to add to that? I'll look for my chip. I think it's somewhere
No, I think you pretty much covered that. I mean, personally, you
know, I feel that computing has to go this way. I've,
you know, I've been thinking about noise and computing and
how they might help each other, how they harm each other for basically like my
entire, you know, academic and adult life. So it's a topic
that's very near and dear to me. And when you kind of combine the
theoretical angles with the fact that we want
devices to be small, when things are small, thermal fluctuations
are important, and therefore devices become noisy, it
all seems kind of inevitable to me. And I
really think what we're doing is inevitable. So in
that sense, I have a lot of confidence. that
Totally. So I think that you mentioned
the category or whatever, like this category of ideas seems right. Ooh, there
we go. There's some hardware. A little metal
There you go. Old chip. Yeah. There you go. It's almost as
big as your people. That's wild. So this one's made out of
aluminum. That's like the easiest process to start with.
There's other fancy superconducting metals we can experiment with that can operate at
a higher temperature. But for us, we
came from quantum computing. This was kind of our lingua franca. And
we know how to build modular physics-based devices out of the substrate. So
it was somewhere to start. But, you know, obviously we have a long
road ahead because, you know, if you're an alien and you don't
have earthly supply chains that are already established, you
build your thermodynamic computer out of this, right? But of course, for
us to grow on a fast timescale, we got to meet in
the middle where existing supply chains add and
find sort of mineral ground. That's where we're going to silicon. I
like to joke that this is the floor of
computers aliens would build from first principles. But
of course, if you have the deep pockets to
scale up superconducting technology, you might be interested in this and you can give
us a call and we can work with you. Including
the aliens, they're listening to this. Give
us a call. But hey man, I don't judge.
So yeah, essentially, yeah.
So you mentioned the broad category that, you know, this idea is
a part of seems like the right one. It's, you know, for physical reasons,
for like, you know, like the frustrations you had in quantum reasons. are
you guys are one of one? Are you guys the only people thinking about
this? Or I know that like neuromorphic computing
is broadly a category, but I don't know if it's like
somewhat applicable to what you guys are doing. Do you consider yourself part
of that broader subfield or more
I think people have been obsessed with sort of biomimicry, right?
They're like, well, if we obsess over every details of
how neurons actually work and we mimic that, something's going
to work, right? We're going to figure out how to program it later. Whereas for us,
it's like, no, no, no, that's not how it works. You got to like start with the algorithm and
then, you know, both top-down and bottom-up sort of engineer this
bridge between what you want to do and the physics of the
device. And that's what we're doing. We've established this sort of full stack bridge. And
that's so interdisciplinary. It's so difficult because you need to have like ML
people talking to physicists, talking to compiler people, talking to hardware
people. It's a very difficult effort, but
we did it before in
Give me a second here. A comment there. Computing
has kind of started as this abstract thing where a
computer meant like a Boolean logic machine, right? But
in the 21st century we're actually starting to see things go
a different way in a sense that computing is
just becoming kind of more widely understood as just
embedding math into a physical process, right? This
started to become really obvious in quantum computing because the
way that people have been successful in quantum computing to date is
you start with the physics of your device and you see what
kind of computations it does relatively naturally, right? Those are
going to be the things that are going to be highest performing. And back
at Google, like the things that we've gotten working on quantum
computers to date are all kind of
things that very naturally map to the physics of the qubits, right?
Padram Rishan, Vadim Semyansky, that's the kind of game they
play there and it's been very successful. So I'm kind
of taking that approach to computing and
bringing it to like room temperature devices that scale, right?
And ultimately what that's going to do is it's going to kind of hack the
last, every last drop of performance out
All right, yeah, what else do you guys want to talk about?
Yeah, no, please. I had an analogy. So an analogy we like
to use about sort of biomimicry versus what we're doing, right?
If you set out to build a flying machine, right, you're
like, oh, well, you know, the proof of existence is out
there, we have birds. right? Birds flap
their wings. They use some form of physical principle we don't quite understand. Let's
make a plane that flaps its wings, right? And
that's going to be the device I make to achieve flight. On
the other hand, you can sort of go up the supply chain
of nature itself, right, of biology. Ultimately, biology
just finds a way to hack some sort of principle in
physics to its own advantage. And so, in this case, it was like
the physics of lift, right, or flight. And
so, when you build an airplane, an artificial system, you
just try to build the best system that
leverages that physical principle that biology found a way to leverage,
not obsessed with biomimicry. So, neuromorphic devices are obsessed with
biomimicry. We just understand how
natural systems leveraged out-of-equilibrium thermodynamics
in order to do probabilistic machine learning natively
as a physical process, and we're building devices that are better
than nature. Like, our neurons are, the superconducting chip, far more efficient than
your brain. Right? Which is astounding because your
brain is like tens of millions of times more
energy efficient than GPU clouds today and much denser. And
we're going more denser and more energy efficient than the brain, which
may scare some people. But, you know, to
us, in order to be able to understand
and predict our world at all scales, There's just so much
intelligence needed for us to scale civilization that we
just need to accelerate as fast as possible and reach the end We're trying
to reach the end of computing, right? We're trying to reach the ultimate substrate
for intelligence in terms of energy and efficiency and density because
that's where everyone is going And so we're like, let's just
go there right away from first principles and see how
far we can get. And I think we can get pretty far. And so that's
what we're going after. So we're taking inspiration from
nature, but really we're just trying to hack physics directly. The
What's interesting about this neuromorphic space, or
neuromorphic or physics-inspired computing, whatever you want to call it,
is that every different kind of device has
its own kind of natural set of algorithms that
it can accelerate, right? Because building a physics-based accelerator means
you're embedding some kind of math that you want the answer to
in the dynamics of an analog system. Right? And
so when you build dramatically different devices, maybe
like a quantum computer is really good at solving the Schrodinger equation, like
a memristor array type of thing is really good
at simulating memristor arrays. Our
computer is really good at sampling from programmable distribution. So
in a sense, the point I'm trying to get at here is there's room for
a lot of different plays in this space because every
accelerator ends up being good at something different. So
in that sense, I don't think there's any real competition out
What do you think the main applications are going to be just that fit
today's world? So, you know, I imagine that you guys will invent some new
stuff, some new software algorithms, your own software, but
is there going to be a one-to-one analog for people that are doing normal
models today that they'll be able to, oh, they'll just plug your thing in instead
Yeah, we definitely want to support current day, you
know, deep learning and machine learning practitioners. Of course, for
us, those applications like large language models are
applications we achieve at scale, right? When our devices scale, because there's
large in the name of large language models, right? And so there's
a lot of machine learning models that are more valuable
to businesses in some ways. that are in the low data regime,
where you need to have probabilistic uncertainty about your predictions, right? Let's
say you're, you're doing a trade, you're pricing options, or, you
know, you're trying to optimize the manufacturing process, every
data point can cost millions, if not billions of dollars. you
don't have that many data points, and it doesn't matter how much compute you want to
throw at it. You want the best possible answer, and
you want to quantify how uncertain you are about your predictions. That's
the sort of algorithm we're trying to enable in the short term.
And so, did I cut out there? No,
I did not. Okay. I did that. So that's the sort of algorithm
we want to enable. And so that's a different regime
than the big data, big compute regime or big classical compute regime. We're
liking the extreme compute regime. We harness a lot of
that compute from nature, right? The probabilistic compute for practically
free just from heat from nature. But we're
going to tackle sort of low data regime probabilistic
algorithms, right? And we think that these are
actually in some ways more useful than
large language models for businesses. Or
at least a nice sort of dual to them or another
type of machine learning that is synergistic. And
so for us, sort of the LLM market
is interesting. That's where we want to get to. But in the early days,
it's going to be these sort of other algorithms that maybe are more popular in
Let's just say that. Like how there's lots of room in
device space for new things, I think there's lots of room in
AI space for new things, right? It's easy to get caught up in
what's most important today, but you have to take a second and
have some perspective. We're really early in
AI. This is like the birthing years, right?
And so the technology that, I mean, there's never going to be an
ultimate technology. There's always going to be a new and better thing. But, you know, looking
10 years down the line, 20 years down the line, that stuff
might have no resemblance to what we're doing today, right?
This is the next S-curve. We think that current AI,
it's scaling, it's very impressive. It's going to hit some
sort of saturation, might be the data bottleneck. I think definitely the
energy bottleneck, right? You've got
to move mountains. 7 trillion. 7 trillion, right? Just throw 7 trillion
at it. It's going to fix everything. you know, we think there's a
better way. We're already working on the next S-curve, right, after
this one. So it takes time to ramp up to the level where
we're at the state of the art, but we know that, again,
by 2030 or so, we're probably gonna hit a wall in
terms of scaling down our current deterministic transistor technology
because they're gonna hit this sort of thermodynamic regime. Their wobbliness
is gonna be a problem. We're building beyond Moore's wall. So we're
gonna enable us to extend Moore's law in a sense,
just for AI and probabilistic computing, not
for general computing, but that's still great because that's where
we want the extreme scale compute anyways. And
so to us, this is the most important thing we could be working on in our lives. And
every day we just wake up with insane levels of internal fire.
We're on a mission to save the world here, and
we kind of hyperstition this, and we're kind of in a position where it
is the case, and it's kind of surreal, of
course, and there's many other things going on in
our lives as well. Most
people's priors is that if we had a successful movement,
couldn't be successful in technology, but for me, I think this
technology, you know, the cultural movement is great and I want more people to
join in on the optimism and to have life paths similar to
ours, if possible, because then everybody would accelerate. But,
you know, ultimately, for me, this mission is
the one I'm like most passionate about. And, you know, I'm
all it, right? This is the meaning and purpose of
our lives. I truly believe that. And that
just gives a deep sense of satisfaction working on this stuff
every day and gives you near infinite
energy somehow. It just comes out of nowhere, right? Like if you have this infinite
goal and you're making progress towards it, it
feels really good. And so any other bump in the road, any challenge, it's
just a temporary setback on this road to
an amazing goal. And so couldn't be more excited to finally, talk
more about it today. It feels very cathartic right now to talk
about it in a sort of public podcast. These have been
like our internal secrets for a while on our
thesis, but the reason we're showing more about
the world is so that people know. People know it's coming. And
if you want to work on this sort of stuff, if you're a talented builder, if
you're ready to run through walls to do this, you should give us a call
So we got four new job postings, but really it's
whoever wants to join us on this journey and believes
in the mission now that we've kind of laid it out, you
know, should talk to us. And so, you know, our goal
is for everyone to accelerate and, you know, in the ethos of, you
know, some of our techno-optimistic thinking, we're putting our
ideas out there. And hopefully
the universe will reward us back for creating
all this value, but we're going to keep going no matter what, because it's the most
And by talk to us, he means apply to our job postings, because if you
DM us on Twitter, it's very likely not
Yeah, I get a lot of DMs. Yeah, yeah, yeah,
yeah. So ideally job posting. Yeah, so
that's our goal today. I love it. Thanks so much, Christian. I
Oh yeah, absolutely. I mean, you guys are the perfect people to have on it. I feel like you
name-dropped first principles many times throughout the podcast, which I am very, very
happy to hear. Awesome. And I hope that people, so people
should know if they didn't know this already, and it'll be linked in the show notes, but there
is a paper we were talking about through this, so they've actually published some
It's just a few ideas to get you thinking. It's
Not yet. That's right. Well, they did have that conference in San Francisco yesterday
that was like how to build a nuclear bomb. So who knows, maybe they're- Right. No,
thank you guys so much for joining. This was awesome. And who knows, maybe
when you get your next chips or when you publish a full white paper, we'll have another one of these and go
That sounds good. Sounds good. Thanks so much. Awesome. Thanks, Christian. Thanks, guys. All right. Cheers.
