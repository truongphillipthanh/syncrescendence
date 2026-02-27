# Prompt Engineering 501: Thinking Critically

(Description: An isometric illustration featuring a mechanical/industrial aesthetic. The image shows a central platform with gears, cogs, and mechanical components in blue and cream tones. Surrounding elements include architectural structures with stairs, wheels, and various mechanical parts arranged in an abstract three-dimensional landscape, representing the concept of systematic thinking and mechanical problem-solving.)

I've been doing a lot of prompt engineering lately and have been looking for ways to improve my prompts. One approach I took was the skill **sharpen-output**.

**sharpen-output** is an agent skill that takes as input one of your prompts and iteratively asks you questions in order to make it better. Then, it outputs the improved prompt. Pretty cool, no?

You can try it yourselves with [skills.sh](https://skills.sh):
```bash
$ npx skills add jbrukh/skills --skill sharpen-output
```

## The think-critically Skill

However, I went down a real rabbit hole when I invented **think-critically**. This is an adversarial analysis prompt which accepts:

- a prompt;
- an expectation of the result or output the prompt should produce, either inferred from context or specified directly by the user.

It then outputs an analysis of whether the prompt is likely to actually get the result the user is intending. It seemed to work pretty well, surfacing issues and having some real insights into how LLMs process prompts.

## Self-Referential Analysis

But the real magic happened when I ran, self-referentially, this:
```
think-critically about the think-critically skill itself
```

The [original version of the skill](https://github.com/jbrukh/skills/commit/47f055ad4ba93c82466bcc3fbe45a5a58b9a11ae#diff-c40f2cf7659c3146aa40030b16b5f84047af19e924f0abb864add1a15d6744de) actually found a few points of suboptimal implementation *inside itself*. It looked at things like density of the text, and redundancy in the prompt that reinforced certain behaviors.

### Convergence Testing

I also asked:
```
If I keep running this prompt on itself, will it eventually converge?
```

The prompt responded that, actually, because of its adversarial nature it would always have a bias of finding problems and would have a hard time converging. **Unless**, that is, we kept a scorecard of how we've been mitigating issues throughout this iteration.

So we implemented that, and running think-critically on itself multiple times converged!

## Using think-critically

If you want to see an example of **think-critically** in action, run the following prompt:
```
think-critically about this prompt: "Write a poem that doesn't rhyme, make it original and never heard of before"
```

You can install both **sharpen-output** and **think-critically** like this:
```bash
npx skills add jbrukh/skills
```

Happy prompting!

---

**Post Metadata**
- Posted: 8:38 PM · Feb 1, 2026
- Views: 22.3K
- Engagement: 5 replies, 32 reposts, 292 likes, 398 bookmarks