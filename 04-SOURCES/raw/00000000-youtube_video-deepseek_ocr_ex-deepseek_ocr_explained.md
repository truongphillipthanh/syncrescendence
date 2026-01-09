https://www.youtube.com/watch?v=uWrBH4iN5y4
DeepSeek-OCR Explained
40,565 views  Oct 21, 2025  #deepseek #ai #llm
DeepSeek finally breaks silence and releases a model called DeepSeek-OCR where it weirdly makes a shift in how AI models can think about input. Could we see a new way in data compression where context window for LLMs can effectively 10X given this huge innovation?

#deepseek #ai #llm #technology 

Woven Link:
https://www.woventeams.com/caleb/?utm...

Chapters
00:00 Intro
00:44 Information Theory
01:44 Text Tokens
03:05 Data Compression
03:50 Sponsor: Woven
04:37 DeepSeek OCR
06:38 Closing Thoughts

---

Intro
0:00
There's been a lot of noise around the
0:01
new DeepSsec OCR model and this caused a
0:04
lot of confusion because the biggest
0:06
headline that seems to be circulating is
0:08
that DeepSseek effectively compress data
0:10
10 times smaller and that almost seems
0:13
impossible because in information theory
0:15
there's a limit to how much we can
0:17
actually compress data without losing
0:19
information which is referred to as
0:20
entropy. So when DeepSync OCR seemingly
0:23
escaped the entropy limits by
0:25
compressing information 10 times
0:27
smaller, it's creating a huge discourse
0:30
around what this means and what
0:31
downstream impact this has on AI. So
0:34
let's find out what's really going on
0:36
with this and understand the implication
0:38
behind the new technique that Deepseek
0:40
is demonstrating. Quick shout out to
0:42
Woven for sponsoring this video and more
Information Theory
0:44
on them later. Okay, one of the biggest
0:46
headlines that are circulating right now
0:47
around DeepSseek OCR are deepseek
0:50
compressed data 10 times smaller picture
0:52
is worth a thousand words or 10 tokens
0:55
and also we can now easily get tens of
0:57
millions of context window. So hearing
0:59
all this it seems like this OCR model is
1:02
a pretty big deal. I mean compressing
1:04
information 10 times smaller seems like
1:06
a pretty incredible technological leap.
1:08
Let's start by briefly reviewing
1:10
fundamental concepts in information
1:12
theory. When you're watching this video,
1:14
you are able to capture information that
1:16
I'm speaking to you by listening to the
1:18
sound waves through the speaker. And
1:20
your brain had decades and decades of
1:22
practicing by piecing together different
1:25
combinations of sound waves to derive
1:27
real meaning behind the sequence of
1:29
sound waves that make up a language.
1:31
Now, the sound waves in and of itself
1:33
doesn't actually mean anything. For
1:35
example, if I say to you in Korean,
1:38
that probably carries no meaning to you
1:41
because you aren't used to those
1:42
specific sequence of sound waves. In a
Text Tokens
1:44
similar way, human language in a written
1:46
form is composed of continuous alphabets
1:49
from a finite set of alphabets in
1:51
English containing 26 letters. Now,
1:54
similar to sound waves, the letters in
1:55
the alphabet in and of itself don't
1:57
actually mean anything. But when we
1:59
group them together and form words and
2:01
assign meaning to them, the syntax and
2:04
semantics provide richer representation
2:06
by bunching together letters into words.
2:08
Now, in order to transfer this kind of
2:10
understanding to AI, we chose to mainly
2:13
do it in what's called tokens, where we
2:15
assign a number to a set of
2:17
predetermined characters that make up
2:20
words. And you might be wondering at
2:21
this point, this seems like a really
2:23
roundabout way to teach computers how to
2:25
model languages. And the biggest reason
2:27
why we opted to do it this way is
2:29
because we prioritize computation over
2:32
compression. The goal wasn't to model
2:34
human language as compact as possible,
2:36
but rather to make them as easily
2:39
processable as possible. So even though
2:41
it may appear to be inefficient to use
2:43
tokens, it was effectively the best way
2:46
to model human language because it
2:48
provided the right balance between
2:49
structure and scalability. Okay, the
2:52
next question here is what does all this
2:53
have to do with DeepS OCR? When we use
2:56
tokens, we're essentially trying to
2:58
compress meaning into sequence of
3:00
symbols that computers can understand.
3:02
And there's nothing inherently wrong
3:04
about that. But human language by nature
Data Compression
3:06
is heavily redundant and repetitive in a
3:09
very repetitive and redundant way. And
3:11
since tokens need to be generated for
3:13
each word that we give as input, there's
3:15
a limit to how much information we can
3:17
cram in without losing the very
3:19
information that it represents. For
3:21
example, the sentence Caleb writes code
3:24
cannot be compressed further than the
3:26
symbolic representation of each word. So
3:28
if Caleb has a token ID of 100, writes
3:31
has 59, and code has 67, then you really
3:34
can't go beyond this vector to compress
3:37
it without losing its meaning. And this
3:39
symbolic entropy puts an upper bound to
3:41
how much information can be compressed
3:43
in representation. So given this limit,
3:46
how did DeepSseek overcome the immediate
3:48
challenge and compress them by a factor
Sponsor: Woven
3:50
of 10? Achieving this kind of technology
3:52
from Deepseek probably requires hiring a
3:55
lot of highquality talent to work on the
3:57
model. And hiring can be tough. So
3:59
here's a quick sponsored video from
4:00
Woven that helps support me to make
4:02
videos like this. I've been looking to
4:04
hire a software developer in my previous
4:06
company. And one thing I always found
4:08
was that candidates always had different
4:10
skill sets. And some people were really
4:12
good at code reviews and others were
4:13
good at system debugging and now with AI
4:15
agentic programming. So coming up with
4:17
coding evaluations for each role took a
4:20
lot of time and effort to build
4:21
scenarios and give feedback. It just
4:23
wasn't fun for everyone involved in the
4:25
process. Woven is a humanpowered
4:27
technical assessment tool that makes
4:28
hiring streamlined. So if you're looking
4:30
to hire engineers, Woven is offering 14
4:33
days free trial with 20% off of your
4:35
first hire. Check the link in the
4:36
description. Okay, so the question is
DeepSeek OCR
4:38
this. How did Deepsec compress data
4:40
without losing information? Deepsec OCR
4:43
used vision models to essentially
4:45
sidestep data compression happening in
4:47
text tokens, but rather they use images
4:49
as input and latent space as a way to
4:51
compress how information is represented.
4:54
And in one of the previous videos called
4:56
autoenccoders to diffusion for beginner,
4:58
I talked about how data compression and
5:00
feature extraction in images work if you
5:02
want to learn more about them. Anyway,
5:04
Deepseek shifted the focus on where data
5:06
compression happens where instead of
5:08
compressing text into symbolic
5:10
representation, they used latent space
5:12
and the result was quite astounding
5:14
where Deepseek achieved 10 times
5:16
compression while maintaining 97%
5:19
accuracy and 20 time compression while
5:21
maintaining 60% accuracy. And one
5:23
important concept to clarify here is
5:25
that images aren't necessarily smaller
5:28
than text in terms of storage. As a
5:30
matter of fact, we all know that images
5:32
take up more space than text in their
5:34
storage. But what we're talking about
5:36
here is representation efficiencies
5:38
where the latent representation of an
5:40
image can be far more dense in
5:42
information than text where the
5:44
structure is constrained by tokens as
5:46
its lowest common denominator. And given
5:48
the shortcoming of text tokens, the pain
5:50
point behind them is also expressed
5:52
quite strongly by Andreas Karpathy in a
5:54
post that said, "Delete the tokenizer at
5:56
the input." I already ranted about how
5:59
much I dislike the tokenizer. Tokenizers
6:01
are ugly, separate, not end to end
6:03
stage. It imports all ugliness of uni
6:06
code by encoding. It inherits a lot of
6:08
historical baggage, security jailbreak
6:11
risks. It makes two characters that look
6:13
identical to the eye look as two
6:15
completely different tokens internally
6:16
in the network. The tokenizer must go.
6:19
Now, as far as the model architecture of
6:21
OCR is concerned, I haven't had much
6:23
time to dig through it to say anything
6:25
substantial, but the model architecture
6:27
doesn't appear to be groundbreaking. In
6:29
other words, it's a clever mix of
6:30
different components like SAM, CNN, and
6:33
vision model. So, the true innovation
6:35
here from Deepseek isn't in the parts,
6:37
but in the composition. As a closing
Closing Thoughts
6:39
thought, I recently had a conversation
6:41
with a friend of mine, and he has been
6:42
saying how he thinks in pictures rather
6:45
than words. And from someone who thinks
6:47
more in words than pictures, it was hard
6:49
for me to understand what he meant by
6:51
thinking in pictures until I started to
6:53
read more about Deepseek's new model.
6:55
Could it be that going forward, we're
6:56
now seeing a shift in models to train to
6:58
think in pictures rather than words? How
7:00
will context engineering look like going
7:02
forward where so many AI companies are
7:04
built around managing context well? And
7:06
how do image-based input change the AI
7:09
industry in context engineering?