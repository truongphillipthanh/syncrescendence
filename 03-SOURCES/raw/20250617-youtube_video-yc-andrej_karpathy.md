# Software Is Changing (Again)

**Speaker:** Andrej Karpathy  
**Event:** Y Combinator AI Startup School, San Francisco  
**Date:** June 17, 2025  
**Context:** A keynote exploring the evolution of software through three distinct paradigms—Software 1.0, 2.0, and 3.0—and what this shift means for building with large language models.

---

Hello. Wow, a lot of people here. So I'm excited to be here today to talk to you about software in the era of AI. I'm told that many of you are students—bachelors, masters, PhD and so on—and you're about to enter the industry. And I think it's actually an extremely unique and very interesting time to enter the industry right now.

The fundamental reason for that is that software is changing again. And I say "again" because I actually gave this talk already. But the problem is that software keeps changing, so I have a lot of material to create new talks. I think it's changing quite fundamentally. Roughly speaking, software hasn't changed much on such a fundamental level for 70 years, and then it changed about twice quite rapidly in the last few years. So there's just a huge amount of work to do, a huge amount of software to write and rewrite.

Let me take a look at the realm of software. If you think of this as a map of software, there's a really cool tool called the map of GitHub. This is kind of like all the software that's written—these are instructions to the computer for carrying out tasks in the digital space. If you zoom in, these are all different kinds of repositories and all the code that has been written.

A few years ago, I observed that software was changing and there was a new type of software around, and I called this Software 2.0 at the time. The idea is that Software 1.0 is the code you write for the computer. Software 2.0 is basically neural networks, and in particular the weights of a neural network. You're not writing this code directly. You're more kind of tuning the datasets, and then you're running an optimizer to create the parameters of this neural net.

At the time, neural nets were seen as just a different kind of classifier—like a decision tree or something like that. So I think this framing was more appropriate than it seemed. And now we have something equivalent to GitHub in the realm of Software 2.0. Hugging Face is basically the GitHub of Software 2.0. There's also model atlas where you can visualize all the code written there. By the way, that giant circle point in the middle—those are the parameters of Flux, the image generator. Anytime someone tunes on top of a Flux model, you basically create a git commit in this space and create a different kind of image generator.

So Software 1.0 is the computer code that programs a computer. Software 2.0 is the weights which program neural networks. Here's an example of AlexNet, the image recognizer neural network. Until recently, all the neural networks we'd been familiar with were fixed-function computers—image to categories, or something like that. What's changed, and what's quite fundamental, is that neural networks became programmable with large language models.

I see this as something quite new and unique. It's a new kind of computer, and in my mind it's worth giving it a new designation: Software 3.0. Your prompts are now programs that program the LLM. And remarkably, these prompts are written in English. It's a very interesting programming language.

To summarize the difference: if you're doing sentiment classification, you could imagine writing some amount of Python to do sentiment classification, or you could train a neural net, or you could prompt a large language model. Here's a few short prompts and you can imagine changing them and programming the computer in a slightly different way. We have Software 1.0, Software 2.0, and I think we're seeing a lot of GitHub code that's not just code anymore—there's a bunch of English interspersed with code. So there's a growing category of new kind of code.

What's remarkable to me is that not only is this a new programming paradigm, but it's in our native language of English. When this blew my mind a few years ago, I tweeted it—and it's my currently pinned tweet—that remarkably, we're now programming computers in English.

When I was at Tesla working on Autopilot, we were dealing with this transition. We had the image coming in, and the question was: how do you describe, to a computer, what the image means? We had handwritten rules. We had Software 1.0. Then we did deep learning, and suddenly you could describe it with data. You describe the car, the road, the lanes—and the neural net would learn this. That worked pretty well for a long time. But then Autopilot got more complex, and you realized you wanted more and more of these components, and it became unwieldy.

The transition is that now you can just describe what you want in English. I find this quite remarkable because in some sense, you're collapsing the whole pipeline into one thing. The data, the architecture, the loss function, the optimization—all of that goes into the LLM somehow, and you're just writing in English. This is Software 3.0.

Now, what does this shift mean? I'd like to think of LLMs in three different ways. One is that they're utilities. Like electricity, you turn it on and it works. But there's another view which is that they're like fabs—fabrication plants. You specify what you want, and they make it for you. And then there's a third view which is that they're operating systems. You have this big system that can do many things, and you're writing applications on top of it.

If you think about this historically, when we had utilities, they were distributed like utilities. When we had fabs, they were big central things. And then when we had operating systems, they were everywhere. We went from centralized to distributed. So in the LLM era, you have labs that are building and training these large language models—that's the fab. They're being distributed like utilities for now. And I think in the future, they might be more distributed, more like operating systems running on devices.

The historical analogy here is striking. If you look at the history of computing, when computers first came out in the 1950s, the field was dealing with similar challenges. It was the era of mainframes, of figuring out how to use these new computational resources. The complexity, the learning curve, the infrastructure—all of it was new. I think we're computing circa 1960s with LLMs. We're in the early days.

Now, I want to talk about LLM psychology. This is something I think about a lot. LLMs are stochastic simulations of people. The simulator is an autoregressive Transformer, and it's trained on human data. So essentially, you have a "people spirit"—something that's simulating what a person might say or do in a given context. Since it's trained on human data, it has a kind of emergent psychology.

This is both amazing and frustrating. LLMs are simultaneously superhuman in some ways—they can write code, they can do analysis, they can reason—but they're also fallible in many others. They're often confident when they shouldn't be. They can hallucinate. They have inconsistencies. They're jagged. They're extremely good at some things and surprisingly bad at others in ways that seem almost random.

Given that LLMs are people spirits with emergent psychology, how do we productively work with them hand in hand? This is a design challenge. You can build partially autonomous products that leverage the strengths of these systems while compensating for their weaknesses.

One key insight is that you want human-AI collaboration loops. You don't want to just hand off something to an LLM and never touch it again. Instead, you want a feedback loop where a human can evaluate what the LLM produces, correct it, steer it, and the LLM learns from that. This is similar to how Tesla's Autopilot works.

With Autopilot, we had an autonomy slider. On the left, it's fully manual—you're driving. On the right, it's fully autonomous—the car is driving. But in the middle, there's all this interesting space where the car and the driver collaborate. The car handles some things, the driver handles others. They work together. And the beautiful thing is you can move this slider, and different designs make sense at different points on the slider.

I call this the Iron Man analogy. Iron Man's suit is augmenting him. It's not replacing him—it's making him more capable. That's what I think a lot of LLM applications should be. They should augment humans, not replace them. And then over time, you can move that slider toward more autonomy if you want. But the collaboration model is really powerful.

Now, there's something really interesting happening because LLMs are programmed in English. Suddenly, software becomes highly accessible. Anyone can write a program. You don't need to know Python or JavaScript or any traditional programming language. This is what I call "vibe coding."

I did this experiment where I built something called MenuGen. The premise was simple—I described what I wanted to a large language model, and it generated code for me. The code part, the actual programming part, was easy. I had a working demo on my laptop in a few hours. But then I had to make it real. I needed authentication, payments, a domain name, deployment. This was the hard part, and it wasn't coding. It was all DevOps stuff, clicking buttons in the browser, setting up infrastructure. This took me another week.

And this is frustrating because—let me give you an example. If you try to add Google login to your web page, you get this library, and it's telling you a huge amount of instructions. It's like, "Go to this URL, click on this dropdown, choose this, go to this, click on that." It's telling me what to do. A computer is telling me the actions I should be taking. And I'm thinking, why am I doing this? You do it. Why don't you just do it for me?

So the last part of my talk focuses on: can we build for agents? I don't want to do this work. Can agents do this?

Here's the insight: there's now a completely new category of consumer and manipulator of digital information. It used to be just humans through GUIs, or computers through APIs. Now we have agents—they're computers, but they're humanlike. They're people spirits on the internet. They need to interact with our software infrastructure.

So can we build for them? One simple example is robots.txt. On your domain, you can instruct—or advise—web crawlers on how to behave on your website. In the same way, you could have an lm.txt file, which is just simple markdown that's telling LLMs what your domain is about. This is very readable to an LLM. If an LLM had to instead get the HTML of your web page and try to parse it, that would be very error-prone and difficult. It would screw it up. So we can just directly speak to the LLM. It's worth it.

A huge amount of documentation is currently written for people. You see lists, bold text, pictures, emojis. This is not directly accessible by an LLM. I'm seeing some services now transitioning a lot of their documentation to be specifically for LLMs. Vercel and Stripe are early movers here, but there are others. They offer their documentation in markdown. Markdown is super easy for LLMs to understand.

Here's a simple example from my experience. You might know Three Blue One Brown. He makes beautiful animation videos on YouTube. He wrote this library called Manim for animations. I wanted to make my own animations and there's extensive documentation on how to use Manim. So I didn't want to read through it. I copy-pasted the whole thing to an LLM, described what I wanted, and it just worked out of the box. The LLM basically coded me an animation exactly what I wanted. And I was like, wow, this is amazing.

So if we can make documentation legible to LLMs, it's going to unlock a huge amount of usage. This is wonderful and should happen more.

But here's the thing—it's not just about taking your docs and making them appear in markdown. That's the easy part. We actually have to change the documentation, because anytime your docs say "click," that's bad. An LLM will not be able to natively take this action right now. So Vercel, for example, is replacing every occurrence of "click" with an equivalent curl command that an LLM agent could take on your behalf. This is very interesting.

And then there's the Model Context Protocol from Anthropic. This is another way—a protocol for speaking directly to agents as this new consumer and manipulator of digital information. I'm very bullish on these ideas.

There are also a number of little tools that are helping ingest data in LLM-friendly formats. For example, when I go to a GitHub repo like my nanoGPT repo, I can't feed this to an LLM and ask questions about it, because it's a human interface on GitHub. But when you change the URL from GitHub to "gitingest"—you literally replace "hub" with "ingest"—it will concatenate all the files into a single giant text and create a directory structure. This is ready to be copy-pasted into your favorite LLM and you can do stuff with it.

An even more dramatic example is Deep Wiki, which is not just the raw content of files, but they do analysis of the GitHub repo. They basically build up documentation pages just for your repo. You can imagine that this is even more helpful to copy-paste into your LLM. I love all these little tools that basically change the URL and make something accessible to an LLM.

One more note: it's absolutely possible, and it's actually happening today, that LLMs will be able to go around and click stuff and so on. But I still think it's very worth meeting LLMs halfway and making it easier for them to access all this information. Because using LLMs is still fairly expensive, and it's more difficult. And I think there will be a long tail of software where apps won't adapt because these are not like live-player repositories or central digital infrastructure. We'll need these tools. But for everyone else, I think it's very worth meeting at some middle point. I'm bullish on both approaches.

So in summary: what an amazing time to get into the industry. We need to rewrite a ton of code. A ton of code will be written by professionals and by coders. These LLMs are kind of like utilities, kind of like fabs, but especially like operating systems. But it's so early. It's like the 1960s of operating systems, and a lot of the analogies cross over.

LLMs are these fallible people spirits that we have to learn to work with. And in order to do that properly, we need to adjust our infrastructure towards it. When you're building LLM apps, I've described some ways of working effectively with these LLMs and some tools that make that possible—how you can spin this feedback loop very quickly and basically create partial autonomy products.

A lot of code also has to be written for agents more directly. But going back to the Iron Man suit analogy, I think what we'll see over the next decade is we're going to take that slider from left to right. From full human control to full autonomy, with all these interesting intermediate states where humans and AI collaborate.

It's going to be very interesting to see what that looks like. And I can't wait to build it with all of you. Thank you.

---

*Note: All video metadata, timestamps, and introductory framing have been removed from this transcript. The presentation begins at its natural conversational starting point and proceeds through to its natural conclusion.*

## Verification Notes

[^1]: **Software 2.0**: Karpathy first introduced this concept in a 2017 blog post describing the paradigm shift from hand-written code to neural network weights as a form of software.

[^2]: **Hugging Face**: A platform serving as the primary repository for machine learning models, analogous to GitHub for traditional software.

[^3]: **Model Context Protocol**: A protocol developed by Anthropic for structured communication with LLM agents, enabling them to interact with digital infrastructure more effectively.

[^4]: **Gitingest**: A tool that converts GitHub repository URLs (replacing "hub" with "ingest") to generate LLM-friendly text digests of codebases for easier agent consumption.

[^5]: **Manim**: An animation engine for programmers created by Grant Sanderson (Three Blue One Brown), designed to create mathematical animations.

[^6]: **nanoGPT**: Karpathy's open-source implementation of a GPT-like model, available on GitHub.

[^7]: **Deep Wiki**: A tool that analyzes GitHub repositories and generates LLM-friendly documentation pages automatically.