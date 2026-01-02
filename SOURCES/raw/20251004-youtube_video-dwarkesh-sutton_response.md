# Reflecting on Richard Sutton's Vision for AI Learning

I've reflected deeply on the recent Sutton interview and developed a much clearer understanding of his perspective than I had during our conversation. His critique deserves serious engagement, and I wanted to share how I now understand his position—along with where I think the conversation goes from there.

## The Steelman of Sutton's Position

Richard Sutton wrote the famous essay *The Bitter Lesson*. What is this essay actually arguing? It's not saying you should throw away as much compute as possible. Rather, it argues that you want to develop techniques which most effectively and scalably leverage compute.

Most compute spent on an LLM is used in running it during deployment, where it isn't learning anything. Learning happens only during the special phase we call training. This is not an effective use of compute. The training period itself is highly inefficient—these models are trained on the equivalent of tens of thousands of years of human experience. During this training phase, all their learning comes from human data. This is obvious for pretraining data, but it's even true for the reinforcement learning we do with LLMs: these RL environments are human-furnished playgrounds designed to teach LLMs specific prescribed skills. The agent isn't learning in any substantial way from organic and self-directed engagement with the world. Having to learn only from human data—an inelastic and hard-to-scale resource—is not a scalable way to use compute.

Furthermore, what these LLMs learn from training is not a true world model, which would tell you how the environment changes in response to different actions you take. Rather, they build a model of what a human would say next, leading them to rely on human-derived concepts. Consider an LLM trained on all data up to 1900—it probably wouldn't be able to derive relativity from scratch.

Here's the more fundamental critique: LLMs aren't capable of learning on-the-job, so we'll need a new architecture to enable continual learning. Once we have this architecture, we won't need a special training phase. The agent will just learn on-the-fly, like humans and animals do. This new paradigm will render the current LLM approach—with its special training phase and abysmal sample inefficiency—totally obsolete.

## My Perspective on These Distinctions

My main disagreement with Sutton is that I don't think the concepts he's using to distinguish LLMs from true intelligence are actually that mutually exclusive or dichotomous. I think imitation learning is continuous with and complementary to reinforcement learning. Models of humans can give you a prior that facilitates learning "true" world models. I also wouldn't be surprised if some future version of test-time fine-tuning could replicate continual learning, given that we've already managed to accomplish something like this with in-context learning.

## Imitation Learning as a Foundation, Not a Dead End

Ilya Sutskever gave a talk recently that I found striking. He compared pretraining data to fossil fuels. This analogy has remarkable reach. Just because fossil fuels are not a renewable resource does not mean our civilization ended up on a dead-end track by using them. They were absolutely crucial. You simply couldn't have transitioned from water wheels in 1800 to solar panels and fusion power plants. We had to use this cheap, convenient, plentiful intermediary to get to the next step.

AlphaGo (conditioned on human games) and AlphaZero (bootstrapped from scratch) were both superhuman Go players. AlphaZero was better. So you can ask: will we, or will the first AGIs, eventually develop a general learning technique that requires no initialization of knowledge and bootstraps itself from the very start? Will it outperform the best AIs of its time? I think the answer to both questions is probably yes.

But does this mean imitation learning must play no role in developing the first AGI or even ASI? No. AlphaGo was still superhuman despite being initially shaped by human player data. The human data isn't necessarily actively detrimental—it's just that at sufficient scale it isn't significantly helpful. AlphaZero used much more compute than AlphaGo.

The accumulation of knowledge over tens of thousands of years has been essential to humanity's success. In any field, thousands and probably millions of previous people were involved in building up our understanding and passing it to the next generation. We didn't invent the language we speak, nor the legal systems we use. Most technologies in our phones weren't directly invented by people alive today. This process is more analogous to imitation learning than to RL from scratch.

Are we literally predicting the next token, like an LLM, to do this cultural learning? No, of course not. The imitation learning humans do isn't like supervised learning for LLM pretraining. But neither are we running around trying to collect a well-defined scalar reward. No machine learning learning regime perfectly describes human learning. We're doing things that are both analogous to RL and to supervised learning. What planes are to birds, supervised learning might be to human cultural learning.

I don't think these learning techniques are categorically different. Imitation learning is just short-horizon RL. The episode is a token long. The LLM is making a conjecture about the next token based on its understanding of the world and how different pieces of information in the sequence relate to each other. It receives reward in proportion to how well it predicted the next token.

People say: "No, that's not ground truth! It's just learning what a human was likely to say." I agree. But there's a more relevant question: can we leverage this imitation learning to help models learn better from ground truth? I think the answer is yes. After reinforcement learning on pretrained base models, we've gotten them to win gold in IMO competitions and code up entire working applications from scratch. These are ground truth examinations—can you solve this unseen math olympiad question? Can you build this application to match a specific feature request? You couldn't have reinforced a model to accomplish these tasks from scratch. You needed a reasonable prior over human data to kick-start this RL process.

Whether you call this prior a proper "world model" or just a model of humans, I don't think is that important and seems like a semantic debate. What matters is whether this model of humans helps you start learning from ground truth. It's like telling someone pasteurizing milk: "Hey, stop boiling that milk because we eventually want to serve it cold!" Of course. But this is an intermediate step to facilitate the final output.

LLMs are clearly developing a deep representation of the world, because their training process incentivizes it. I use LLMs to teach me about everything from biology to AI to history, and they do so with remarkable flexibility and coherence. Are they specifically trained to model how their actions affect the world? No. But if we're not allowed to call their representations a "world model," then we're defining the term by the process we think is necessary to build one, rather than by the obvious capabilities the concept implies.

## The Continual Learning Challenge

An LLM being reinforced on outcome-based rewards learns on the order of one bit per episode, and an episode may be tens of thousands of tokens long. Animals and humans clearly extract far more information from interacting with our environment than just the reward signal at the end of each episode. How should we think about what's happening with animals? I think we're learning to model the world through observations. This outer-loop RL is incentivizing some other learning system to pick up maximum signal from the environment. In Sutton's OaK architecture, he calls this the transition model. If we were trying to implement this in modern LLMs, we'd fine-tune on all observed tokens. From what I hear from researcher friends, in practice the most naive way of doing this doesn't work well.

Being able to continuously learn from the environment at high throughput is clearly necessary for true AGI, and it doesn't exist with LLMs trained via RLHF. But there might be relatively straightforward ways to add continual learning to LLMs. For example, one could imagine making supervised fine-tuning a tool call for the model, so the outer-loop RL incentivizes the model to teach itself effectively using supervised learning to solve problems that don't fit in the context window.

I'm genuinely agnostic about how well techniques like this will work—I'm not an AI researcher. But I wouldn't be surprised if they basically replicate continual learning. Models are already demonstrating something resembling human continual learning within their context windows. The fact that in-context learning emerged spontaneously from the training incentive to process long sequences makes me think that if information could flow across windows longer than the current context limit, models could meta-learn the same flexibility they already show in-context.

## Concluding Thoughts

Evolution does meta-RL to make an RL agent, and that agent can selectively do imitation learning. With LLMs, we're going the opposite way. We first made a base model that does pure imitation learning, and we're hoping that enough RL makes it a coherent agent with goals and self-awareness. Maybe this won't work.

But I don't think these super first-principles arguments—about how LLMs lack a true world model—are actually proving much. I also don't think they're strictly accurate for the models we have today, which are undergoing substantial RL on ground truth. Even if Sutton's Platonic ideal doesn't end up being the path to first AGI, his first-principles critique identifies genuine basic gaps these models have. We don't notice because they're so pervasive in the current paradigm, but with his decades-long perspective they're obvious to him: the lack of continual learning, the abysmal sample efficiency, the dependence on exhaustible human data.

If LLMs do reach AGI first—which is what I expect—the successor systems they build will almost certainly be based on Sutton's vision.

---

*Note: All preview content, promotional material, timestamps, and conversational filler have been removed from this transcript. The reflection begins at its natural intellectual starting point. This essay represents the core of the video's argument without YouTube-specific retention devices.*
