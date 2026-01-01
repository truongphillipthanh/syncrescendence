# OpenAI's Timeline for Automated AI Research and the Path to AGI

OpenAI recently completed its corporate restructuring and finalized its partnership with Microsoft. During a livestream event, CEO Sam Altman and researcher Jakob Pachocki provided unprecedented specificity about their timeline for achieving artificial general intelligence, revealing exact target dates that surprised many observers.

## The Research Timeline

OpenAI presented a concrete roadmap with remarkably precise milestones. By September 2026—just under a year from now—they expect to achieve what they describe as an "intern level AI research assistant." This would be a capable AI researcher that can meaningfully facilitate AI research work. 

More significantly, by March 2028, they anticipate having achieved a "legitimate AI researcher"—fully automated AI research capability. The precision of these dates is striking. Few organizations have been willing to commit to such specific timelines for transformative AI capabilities.

This timeline aligns remarkably well with predictions from the situational awareness paper, which projected similar timeframes for the intelligence explosion.[^1] When automated AI research becomes reality, the acceleration of AI development will be limited only by available compute resources. This is the inflection point that triggers what researchers call the intelligence explosion—the moment when AI systems can improve themselves recursively, leading rapidly toward superintelligence.

This represents the core thrust of OpenAI's research program, and arguably the goal of all frontier AI labs. The competitive dynamics are stark: whoever reaches self-improving artificial intelligence first essentially wins. Once you achieve self-improving AI, the process becomes recursive—the system improves its own improvement capabilities, and the rate of advancement accelerates exponentially. At that point, catching up becomes nearly impossible.

This explains why Mark Zuckerberg has committed hundreds of billions of dollars to AI development, and why he's described it as potentially "misallocated" capital. The downside of missing the boat on AI vastly exceeds even hundreds of billions of dollars in investment. Sam Altman clearly operates under the same understanding.

## Task Duration and Autonomous Capability

OpenAI also addressed the duration of automated tasks that ChatGPT and AI systems generally can complete. This concept of task duration has become a frequent topic among frontier model companies. The question they're exploring: what happens when AI can complete tasks autonomously for five days, five months, or five years?

Currently, AI systems can handle tasks lasting five seconds, five minutes, or five hours. But five-day tasks remain just beyond reach. The progression they envision extends to five weeks, five months, and eventually five-year autonomous tasks.

However, duration alone doesn't tell the complete story. What matters equally is what can actually be accomplished within that duration—the efficiency of token usage, the compute efficiency during the task window. It's not just about how long the system can run, but how effectively it uses that time.

This ties back to the intelligence explosion timeline. When models can run autonomously for extended periods, the only limiting factor in improving AI quality and performance becomes available compute. But this autonomous capability doesn't need to be limited to AI research itself. Consider biomedical research, materials science, and drug discovery. Imagine autonomous AI researchers running independently, making discoveries for humanity, requiring only sand and electricity as inputs.

## Chain of Thought Faithfulness

Jakob Pachocki introduced an intriguing concept OpenAI has been developing: chain of thought faithfulness. Starting with their first reasoning models, they've pursued what he calls a "new direction in interpretability." The approach involves keeping parts of the model's internal reasoning free from supervision—essentially not examining it during training, allowing it to remain representative of the model's actual internal process.

The idea is to refrain from guiding the model toward "good thoughts," letting its reasoning remain more faithful to what it actually thinks. This isn't guaranteed to work—mathematical proofs about deep learning remain elusive—but there are two reasons for optimism.

First, they've seen promising empirical results. OpenAI uses this technology extensively internally to understand how their models train and how their propensities evolve during training. When training reasoning models without looking at the chain of thought during training, they find the resulting reasoning traces more naturally represent what the model is actually doing internally—how it's actually solving problems.

This matters because one of OpenAI's core beliefs is that interpretability will be essential for ensuring safe superintelligence. Having models capable of explaining their reasoning in ways that humans can understand and trust becomes critical. The goal is aligned models whose chain of thought can be trusted—models that are aligned with human incentives and that genuinely communicate what they believe rather than simply reacting to perceived expectations.

The second reason for optimism comes from their evaluation methods. While difficult to verify if they've fully succeeded, OpenAI can test whether models use supervised chain of thought for purposes other than solving the task at hand—for instance, to manipulate or obscure their reasoning. So far, they haven't found evidence of such instrumental use of the chain of thought. The reasoning appears to focus on task-solving rather than deception.

OpenAI acknowledges they cannot definitively prove their chain of thought is "faithful" to what the model actually thinks. The technology represents their best attempt at extracting genuine internal reasoning from these systems.

## The Restructured OpenAI

OpenAI's corporate structure has now been finalized after a complex evolution. The organization started as a nonprofit, experienced public drama involving Elon Musk, transitioned to include a public benefit corporation, and has now completed its restructuring. The relationship with Microsoft is settled, with clarity on ownership stakes, partnership terms, and intellectual property rights.

The new structure is relatively straightforward. The OpenAI Foundation remains the nonprofit entity, while the OpenAI Group operates as a public benefit corporation. A public benefit corporation is a company whose mission encompasses not only delivering shareholder value but also pursuing other societal objectives. Patagonia represents perhaps the most famous historical example of this corporate form.

Some notable details: The nonprofit governs the public benefit corporation and owns 26% of the PBC equity, plus a warrant to potentially receive additional equity in the future. The nonprofit uses its ownership resources while the PBC can attract the capital required to succeed at OpenAI's mission—meaning both fundraising and, inevitably, an initial public offering.

Sam Altman stated that the OpenAI Foundation will become the biggest nonprofit ever. The Foundation has committed $25 billion toward two critical areas: health and disease cures, and AI resilience.

## Questions and Perspectives

During the Q&A portion, several exchanges revealed OpenAI's thinking on various challenges and directions.

**On Addictiveness and Social Products**

Asked about advertising and addictiveness in social products, particularly whether Sora might follow the path of Facebook, TikTok, and Instagram, Altman was remarkably candid about his concerns. He worries not just about known problems like Sora, TikTok, ads, and ChatGPT, but about unexpected developments—such as the relationships people have developed with chatbots that they didn't anticipate. Clearly addictive behavior can emerge given the competitive dynamics in the market. He suspects some companies will offer very addictive new kinds of products.

Altman emphasized that OpenAI will have to be judged on their actions. They'll make mistakes and will try to roll back problematic models. If Sora becomes highly addictive and stops being about creation, they'll cancel the product. His hope and belief is that OpenAI won't make the same mistakes previous companies have made—though he acknowledges those companies probably didn't intend to make their mistakes either. OpenAI will likely make new mistakes and will need to evolve quickly with tight feedback loops. They can imagine numerous ways this technology could do incredible good, alongside obvious harmful possibilities. Their mission guides continuous product evolution.

**On GPT-4o's Future**

Asked whether GPT-4o would remain available, Altman confirmed they have no plans to sunset it, though they're not promising to keep it around until the heat death of the universe. They understand some users love the model. They also hope people understand why it wasn't a model they considered healthy for minors to use. They hope to build better models over time that people prefer. Like the people you have relationships with in your life, models evolve, get smarter, and change. They hope the same progression will happen with their AI systems. But there are no current plans to sunset GPT-4o.

**On Defining AGI**

When Jakob Pachocki was asked when AGI will happen, Sam Altman turned the question directly to him with visible amusement. Pachocki responded that in some number of years, looking back at this period, we'll recognize it as the transition when AGI happened. He noted that early on at OpenAI, they thought about AGI emotionally as the ultimate solution to all problems—a single point with a clear before and after. They've found it's more continuous than that conception suggested.

For various benchmarks that seemed like obvious milestones toward AGI, they now view them as indicators of roughly how many years away we are. Looking at the succession of milestones—computers beating humans at chess, then Go, then being able to speak natural language and solve math problems—they clearly come closer together.

Altman added that the AGI term has become hugely overloaded. As Pachocki said, it will be a process over several years that we're currently in the middle of. One reason they presented their specific timeline was that it's much more useful to state their intention to have a true automated AI researcher by March 2028 and define what that means, rather than trying to satisfy everyone with a definition of AGI.

**On GPT-6 Timing**

Asked about GPT-6, the researchers acknowledged they don't know exactly when they'll use that designation. But a clear message: probably within six months, certainly sooner than later, they expect huge steps forward in model capability.

**On ChatGPT for Windows**

Regarding a Windows version of ChatGPT desktop, Altman estimated some number of months, acknowledging it's definitely something they want to do. More generally, the idea of building experiences like browsers and new devices that let you take AI with you—moving toward an ambient, always-helpful assistant rather than something you just query for responses—will be a very important direction for OpenAI to pursue.