---
url: https://x.com/pzrsaa/status/2023475024011706710
author: "parsa (@pzrsaa)"
captured_date: 2026-02-16
id: SOURCE-20260216-016
original_filename: "20260216-x_article-the_books_videos_and_papers_im_using_to_learn_maths_ai_and_robotics-@pzrsaa.md"
status: triaged
platform: x
format: article
creator: pzrsaa
signal_tier: tactical
topics: [education, ai-engineering, research]
teleology: reference
notebooklm_category: career-growth
aliases: ["pzrsaa - self-taught AI robotics learning path"]
synopsis: "A self-taught engineer (Google at 18, Tesla) shares their learning resources for pivoting into AI and robotics at Yaak. Covers maths (Kun's Programmer's Intro, 3Blue1Brown), AI (Goodfellow's Deep Learning, Karpathy's Zero to Hero), and key robotics papers (pi0, RT-2, ACT, Diffusion Policy)."
key_insights:
  - "Two math resources suffice for an engineer pivoting to AI: Programmer's Intro to Mathematics + 3Blue1Brown videos"
  - "Key robotics papers: pi0 (vision-language-action), RT-2 (VLA models), ACT/ALOHA (action chunking with transformers)"
  - "Autodidact approach: don't overwhelm yourself, learn enough math to get by, not to become a mathematician"
---
# The Books, Videos and Papers I'm Using to Learn Maths, AI and Robotics
last week I shared that I left Tesla to pivot into AI and robotics [@Yaak_AI](https://x.com/@Yaak_AI).
naturally, people were curious as to how I'm planning to learn these new topics, because I've never formally studied them before. most of my work as a software engineer hasn't required any formal knowledge in maths, nor knowledge in AI to use LLMs.
some background on me: I didn't go to university, started learning to program at 17, got my first job at Google at 18, then 2 years later I joined Tesla. so I would consider myself an autodidact.
because of this new journey, I thought it'd be worth sharing the resources I'll be using to aid me.
the topics I need to study were narrowed down to:
1. Maths
2. AI and Robotics (I merged them because they overlap heavily. the papers I'm reading are from modern robotics, which is mostly ML)
## Maths
(Description: Photograph of a physical copy of "A Programmer's Introduction to Mathematics" by Jeremy Kun, displayed on a wooden desk next to a black keyboard. The book cover features a colorful geometric pattern with interconnected blocks in yellow, orange, green, and rust tones, suggesting mathematical or computational concepts.)
### A Programmer's Introduction to Mathematics by Jeremy Kun
I came across this book while reading [@ludwigABAP](https://x.com/@ludwigABAP) blog, and it has been phenomenal so far. if you're someone whose eyes glaze over formulas, then reconstructing them with code helps. I'm using this book as a sort of catch all for the topics I need, then if I need to go deeper I can use something like 3Blue1Brown's videos.
I'm going through these chapters:
- Chapter 2. Polynomials
- Chapter 4. Sets
- Chapter 6. Graphs
- Chapter 8. Calculus with One Variable
- Chapter 10. Linear Algebra
- Chapter 12. Eigenvectors and Eigenvalues
- Chapter 14. Multivariable Calculus and Optimization
- Chapter 16. Groups
you can pay as you feel for the PDF, but I bought a used physical copy which I think was very worth it. so have a look around on eBay or Amazon.
### Essence of Calculus and Linear Algebra by 3Blue1Brown
(Description: Photograph of the "Deep Learning" textbook by Goodfellow, Bengio, and Courville displayed on a wooden desk. The cover features an artistic winter landscape with bare trees and pink flowering plants against a blue sky, creating a striking visual design for an advanced technical manual.)
for many years I've heard of 3b1b's videos but never had a reason to watch them until now. the animations do help with making concepts click, plus it's nice that they provide text versions to reference (I tend to lean towards reading more than watching).
these 2 resources are pretty much the only ones I'll be using for maths. I don't need to overwhelm myself, plus I'm not studying to become a mathematician, just enough to get me by.
## AI and Robotics
### Books
(Description: Photograph of "Deep Learning" by Goodfellow, Bengio, and Courville on a wooden desk with a black keyboard nearby. The book cover displays an artistic winter landscape with flowering pink and purple plants, bare trees, and a blue sky.)
#### Deep Learning by Goodfellow, Bengio and Courville
my CTO gave me his physical copy, and I'm using it more as a reference book to lookup things. the book is free to read online, but I generally think having physical copies of textbooks like this are worth it.
#### Society of Mind by Marvin Minsky
gifted by my CTO, not relevant to my studies, but it seems relevant in the age of agents and as something miscellaneous to read.
### Videos and Courses
(Description: Screenshot of a 3Blue1Brown video titled "But what is a neural network? | Deep learning chapter 1" showing neural network visualization with interconnected nodes and blue/red colored connections. The video displays typical YouTube interface with timestamps and chapter information. A timestamp of 18:40 is visible.)
- **Neural Networks by 3Blue1Brown** - I think the visuals (of course the url is suffixed with π) are even more important in learning AI, so I'm happy with it so far
- **Neural Networks: Zero to Hero** by [@karpathy](https://x.com/@karpathy)
- **Neural Networks and Deep Learning** by [@michael_nielsen](https://x.com/@michael_nielsen) - I went through the first few chapters a couple months ago, I like how it teaches from the absolute foundations of deep learning that won't go out of fashion any time soon (aka Lindy)
- **Practical Deep Learning** by fast ai
- **Robotic Manipulation** by MIT
- **Robotics Course** by [@huggingface](https://x.com/@huggingface)
### Papers
(Description: Preview of a research paper titled "π₀: Our First Generalist Policy" with publication details showing October 31, 2024. Below is a photograph of a robotics lab showing a person in a camouflage shirt working with a robotic arm system. The setup includes an orange and black robotic frame with equipment on a wooden table, demonstrating a practical robotics implementation. A π symbol is visible in the corner.)
- **Attention Is All You Need** - the transformer architecture that changed everything
- **An Image is Worth 16x16 Words (ViT)** - transformers applied to vision
- **Denoising Diffusion Probabilistic Models** - the maths behind diffusion models
- **π₀: A Vision-Language-Action Flow Model** - for one of my interviews with Yaak I had to study this paper from [@physical_int](https://x.com/@physical_int) and present it. this is the first paper I ever read in my life, well written. let me know if you're interested in seeing that presentation!
- **RT-2: Vision-Language-Action Models** - how vision-language models can directly output robot actions
- **Diffusion Policy** ([@chichengcc](https://x.com/@chichengcc) et al) - representing visuomotor policy as a diffusion process
- **Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT)** ([@tonyzzhao](https://x.com/@tonyzzhao), [@Vikashplus](https://x.com/@Vikashplus), [@svlevine](https://x.com/@svlevine), [@chelseabfinn](https://x.com/@chelseabfinn)) - action chunking with transformers, the method behind ALOHA
- **Universal Manipulation Interface** - portable data collection for robot learning
- **Octo: An Open-Source Generalist Robot Policy**
- **Robot Learning: A Tutorial** ([@_fracapuano](https://x.com/@_fracapuano) et al) - overview of Robotics from the Hugging Face/LeRobot team
### Blogs & Articles
- **A Recipe for Training Neural Networks** by Andrej Karpathy - something to read before training models
- **From Words to Worlds: Spatial Intelligence** by Fei-Fei Li - the field Yaak operates in
- **A Gentle Introduction to Graph Neural Networks**
---
it might seem like a lot, but keep in mind I'm not loading all of this suddenly into my brain, it's just the general path I'm headed towards with studying
I hope it was useful! if there's anything you could suggest, do dm me.
(Description: Stylized digital illustration with glowing blue neon lines showing two humanoid robots collaborating. A robot on the left appears to be pouring or transferring something to a robot on the right, set against a dark background with bright blue horizontal lines creating a futuristic atmosphere.)
(one of the robotic arms I work with is the Franka FR3)