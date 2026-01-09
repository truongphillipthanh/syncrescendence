# The Fundamental Limitations of Large Language Models and the Promise of Category Theory

Language models cannot do addition. Not really. I keep seeing claims that they can, and every time I see this claim, I go again to ChatGPT and check—and they can't. What they can do is learn patterns that work most of the time, but you can always trip them up. If you ask ChatGPT what is a bunch of eights plus a bunch of ones with a two at the end, it will get the correct answer because it will recognize the trick. It'll say, "Ah, that's just one and a bunch of zeros." It'll know you're trying to trick it. But if you change one of the eights to a seven, now it has to actually know what it's doing. It has to walk up, hit the seven, and stop propagating zeros. And it simply fails. It either chokes and makes up some nonsense, or it says it's one with a bunch of zeros anyway. It definitely can't add in the basic way that we know how to do algorithmically, that humans learn.

This raises a fundamental question when we look at models like Veo or Genie: have these models truly encapsulated the physics—Newton's three laws of motion—100% accurately? Right now, they haven't. They're approximations. They look realistic when you casually glance at them, but they're not accurate enough yet to rely on for robotics.

## The Inadequacy of Tool Use Alone

Just because we can achieve some level of progress by hooking up a really potent tool to a language model doesn't mean we shouldn't think about what the next generation of these models should look like and how we can make them intrinsically better. Even if you have the best tool in the world, that's not going to save you if you cannot predict the right inputs for that tool.

Consider this: even some of the current frontier models will perform hundreds of billions of multiplications just to produce a single token of output. Yet they cannot reliably multiply even relatively small numbers together without failing. This hints at a great misalignment between what we are training these systems to do, how we're building them, and what we might want to use them for downstream—especially if we're doing reasoning or science.

Now, you might argue that an LLM, if you teach it properly, can learn to do addition up to some failure of its memory—just like humans might forget a digit or forget to carry over. The model can learn this procedure with its neural machinery, and that neural machinery also allows it to absorb tons of world knowledge and deal with the vagueness of concepts, the fact that things don't exactly fit the clean symbolic theories of good old-fashioned AI.

We've all played with MCP servers. We know we can hook tools up to these systems. Why not just call a calculator? But tool use isn't enough. We still need to be thinking about the actual architecture underneath. That still matters.

## The Case for Internalization

Internalizing things has a chance to be a lot more stable. The relationship between neural nets and tools is somewhat complicated. You can do a lot with it, particularly interesting search, but there are disadvantages. You may have to call the model many times because it may get an answer that isn't the answer it was expecting. It might have to rethink things and go back.

Imagine a situation where you had some complex reasoning problem where along the way you had to do a series of little additions—this and then this, and then how many of these are there, and then how many of those, and so on. It could be quite complicated to keep calling out to a calculator, especially when efficiency is a constraint. Let me give you an analogy. You can think of this as the debate between writing a fast implementation of something versus writing a clever algorithm. Like Dijkstra versus bubble sort for finding shortest paths. Both work, but one is orders of magnitude better.

The interesting thing is that humans often do use tools for calculation, but when we have calculators in the palm of our hand, we still learn how to multiply by hand. When I meet someone and they tell me they don't know their times tables, I find it deeply strange. Even though a calculator is always available, there's clearly some benefit to internalizing that machinery. It changes how you think about problems.

## From Alchemy to Science: The Need for Unifying Theory

Right now, deep learning is in its alchemy phase. We have powerful results, but we lack a unifying theory that tells us how to systematically design architectures for specific tasks. This is where geometric deep learning and category theory enter the picture.

The geometric deep learning blueprint proposed a systematic way of thinking about neural network architectures through the lens of symmetry and group theory. The basic idea is elegant: if your data has certain symmetries—like images being the same under rotation or translation—your neural network should respect those symmetries. This is equivariance: if you rotate an image and then process it through your network, you should get the same result as processing it first and then rotating the output.

This framework has been remarkably successful. It gives us convolutional neural networks, graph neural networks, and many other architectures as special cases. But it has limitations.

## The Limitations of Group Theory

Group theory is powerful for describing reversible symmetries, but much of computation is fundamentally irreversible. When you compress information, when you aggregate data in a graph neural network, when you fold a list down to a single value—these operations destroy information. You can't run them backward. And groups, by their very nature, are about invertible operations.

This is where category theory comes in. Think of it as "algebra with colors"—a way of doing mathematics where you can only compose operations when their types match, like magnets that only snap together when the colors align. This partial compositionality is the secret to building more complex internal reasoning.

## Synthetic vs. Analytic Mathematics

There's a philosophical shift needed in AI research: moving from analytic mathematics—what things are made of—to synthetic mathematics—how things behave and relate to one another.

In analytic terms, you might define a vector as a tuple of numbers. In synthetic terms, you define it by what you can do with it: you can add vectors, scale them, take linear combinations. The synthetic view is about structure and relationships rather than concrete representations. This turns out to be exactly the right level of abstraction for designing neural networks, because you care about what computations a layer can perform, not about the specific matrix entries.

## Category Theory as the Systematic Guide

Category theory provides a systematic, Lego-like approach to building neural architectures. Instead of hand-crafting each new architecture through trial and error, you start by asking: what kind of computation do I need my network to perform? What structure should it preserve?

If you need to respect group symmetries, category theory gives you geometric deep learning. If you need to process sequential data with a fold operation, it gives you architectures based on monoids. If you need to handle recursive data structures like trees, it gives you architectures that naturally compose through higher categories.

The key insight is that a neural network layer can be viewed as a homomorphism between two algebras for the same endofunctor. The endofunctor describes the kind of computation a network needs to respect—be it a group action, a list fold, or an automaton transition. The algebras describe how that computation transforms the specific data. The homomorphism is then a function that maps between these two data representations while preserving the computational structure.

When this homomorphism represents a group action, you recover geometric deep learning. But the framework is far more general.

## Beyond Single-Sorted Syntax

The syntax of a group action is single-sorted: you have one kind of thing, and each group element sends that thing back to itself. You might have points in a plane, and your group might be rotations and reflections that move those points around, but you're still in the plane.

But this one-sorted syntax isn't enough to capture basic type constructors in computer science. Lists, for example, require a multi-sorted syntax. You need to think of zero-tuples, one-tuples, two-tuples, and so on. Given a k-tuple, you might be able to make some other kind of tuple—an l-tuple—by taking elements of your k-tuple and packing them into lists.

This has compositionality: if you have a way of packing things from a tuple into lists, you can pack those lists into other tuples of lists. But it's clearly many-sorted and highly non-invertible. You can't undo lists by packing things more and more into them. You just get more lists.

## The Mathematics of Carrying

There's something very basic in mathematics that we all learned in elementary school that has been overlooked in the design of graph neural networks: the notion of a carry.

What exactly is a carry? Suppose you can implement a device—a number wheel—that can do arithmetic modulo 10, counting from 0 through 9. Now you want to build a composite wheel that can do arithmetic modulo 100. What do you need? You need a little mechanism that when the wheel goes from 9 to zero, it turns the next wheel by one.

This is very simple, but it's extremely at odds with the way graph neural networks have been conceived. In traditional GNNs, you send the whole state between nodes. But with carries, the information isn't in the state—it's only in the change of state. And it's even worse than that. Even if you sent the change in state, that's not enough information. If I went from 9 to zero, is it because I added one? Added eleven? Subtracted nine?

It's quite subtle to get this kind of thing to work in the presence of gradient descent. Yet this is a fundamental aspect of how we assemble more complicated computational operations from simpler ones. One of the first things you do when describing a CPU is describe an adder. This is already something we're struggling to do in GNN terms.

## The Geometry of Discrete Operations

This behavior is easy to get when you do discrete mathematics and very complicated when you do continuous mathematics. You can easily describe the number wheel example—everybody understands it because they know how to do addition. But getting it to happen in a way such that everything is continuous turns out to be really interesting.

The simplest examples of this phenomenon don't occur until you're dealing with three-dimensional manifolds. You would need to be thinking about things in four-dimensional space. The simplest example we know of is the Hopf fibration. This is a situation where you can decompose a three-dimensional sphere—a sphere in four dimensions—by projecting it onto a two-dimensional sphere such that all of the pre-images are one-dimensional spheres, or circles.

The three-dimensional sphere is very different from the product of the one- and two-dimensional spheres, just the same way that ℤ mod 100 is very different from the product of ℤ mod 10 with ℤ mod 10. This geometric subtlety might provide a way to create the phenomenon of carrying and actually properly model this aspect of algorithmic reasoning—to start building actual CPUs in neural networks.

## The Categorical Deep Learning Framework

The claim is quite straightforward: deep learning has two languages—constraints and implementation—and we lack a single framework that cleanly links them together. Categorical deep learning provides that bridge, using universal algebra in a two-category of parametric maps.

It recovers geometric deep learning as a special case while naturally expressing things like recursion, weight tying, and non-invertible computation. If we want AI to solve the world's hardest scientific problems, it can't just be a stochastic parrot. It needs to internalize the rules of logic and computation. By imbuing neural networks with categorical priors, we're attempting to build a future where AI doesn't just predict the next word—it understands the underlying structure of the universe.

---

*Note: All preview content, advertising, and promotional material has been removed from this transcript. Technical terminology has been preserved as presented by the speakers.*

[^1]: **Hopf Fibration**: A mathematical structure mapping a 3-sphere (sphere in 4D space) to a 2-sphere (ordinary sphere) such that each pre-image is a circle. First described by Heinz Hopf in 1931, it's the simplest example of a non-trivial fiber bundle and has deep connections to quantum mechanics and topology.
