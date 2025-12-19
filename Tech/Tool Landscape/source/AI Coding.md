## Ranking AI Coding Editors and Tools

We're going to be rating and ranking a variety of AI coding editors and tools, and joining me today are **Wes** and **Scott**. We're excited to rank all of these from best to worst, drawing on our individual experience and exposure to them to offer an honest assessment.

---

### VS Code Forks

First up is **Cursor**, the VS Code fork that initially captured everyone's attention by offering a superior UI and a better way to interact with AI compared to what was first available in VS Code.

One of the participants started everything in **B tier** to avoid influencing the vote, but shared that for them, Cursor feels like "baby's first decent AI tool" and they aren't getting anything from it that other current tools don't offer. Another participant agreed that while Cursor was one of the first and caused a lot of excitement, other tools have since added much better user experiences and ways of working with context. However, they're torn between **A and B tier**, as they use it frequently, but have been getting frustrated with it lately because "it doesn't stay on track" and its planning tools aren't as good as some other editors.

A third participant, however, put Cursor in **S tier**. They justify this because Cursor continuously adds new features, and the tool completely "changed the game". When Cursor emerged, the **VS Code Copilot** had some bugs—like one that added extra curly braces to tab completions—that took a year to fix, even with persistent complaints from vocal users. The competitor's arrival prompted VS Code to accelerate its own development. Because Cursor is "constantly pushing the game" and rolling out new features weekly, the third participant firmly placed it in S tier. Ultimately, the group agreed to meet in the middle at **A tier**.

Next is **VS Code + Copilot**. It's suggested that VS Code might be unfairly judged because many developers switched to Cursor a year ago and haven't gone back to try the improvements.

* **Scott** suggested **B/A tier** for VS Code, arguing that if Cursor is an A, VS Code is an A, because he doesn't feel there's anything Cursor can do that VS Code can't do just as well. He considers VS Code an "extremely competent" editor that offers the added benefit of the entire VS Code marketplace of extensions.
* Another participant suggested **low A tier**, noting that other editors wouldn't exist without VS Code and that its initial slow pace in adding features is what caused people to switch. They now reach for VS Code often, finding its chat interface and interaction with the terminal more polished than Cursor's, and the speed has improved recently.
* The third participant also voted for **A tier**, adding that VS Code has a "really generous free tier" to encourage Copilot usage, which is an advantage over tools that require upfront payment. He also humorously added that VS Code is the only editor that can "restart the freaking TypeScript server".

Following is **Windsurf**, which is based on **Codium**. Before Cursor, one of the participants used the Codium extension inside VS Code for AI editing. The other two used Windsurf for many months, praising its small UI tweaks for making the experience of reviewing edited code less overwhelming. However, its inclusion in the list was placed in **B tier** due to the "chaos surrounding it" and the consensus that there's nothing compelling that would make a user choose it over Cursor or VS Code.

Next up is **Kiro**, a VS Code fork from the Amazon AWS team. One participant believes Kiro is the best of the VS Code forks, initially placing it at **high A tier**, but then bumping it up to **S tier**. They feel Kiro excels at **spec-driven development** with its actions and hooks, and is great for keeping developers on track. The only drawback, making it "S minus," is that it "loves to add files and add stuff to your codebase" without prompting, requiring the user to be vigilant. Despite this, they find Kiro's output to be reliable and organized.

* Another participant went with **low A tier**, acknowledging that the spec-driven development idea is excellent, especially for less-organized developers, acting like a "to-do list on steroids". They found the architecture descriptions and user stories to be a great aspect of AI coding. However, they experienced a "false sense of security" because the tool would still drift from the plan, leading them to believe that no single AI tool does exactly what they tell it to do.
* The first participant noted that the strength of Kiro's UI, **MCP integration**, AI hooks, and steering docs pushes it above A tier, and that many of the complaints could be attributed to the model being used. Kiro defaults to **Anthropic's model**.

The group decided to place Kiro between Cursor and VS Code.

The next editor is **Trae**, a VS Code fork from ByteDance. One participant placed it at **B tier, maybe even C tier**, because using it in Canada requires a VPN. While it's being developed "pretty aggressively" and is a good alternative to Cursor or Copilot, it may not gain momentum in their circles due to a lack of trust in a Chinese company. The other two had not used it, so it was put in **C tier**. They noted that Trae has an "awesome job" on the UI and integrations.

---

### CLI-Based Tools

The next set of tools are **CLI-based** and not within the editor itself.

First, **Claude Code** is a "fan favorite," but one participant admitted they haven't used it much because cheaper or free options were available.

* **Scott** stated the hype is real and put it in **S tier**, having paid for the $\$300$ a month Claude plan. He called the back-and-forth prompting "gambling," but said Claude Code "tends to do what I tell it the most" and is one of the first tools that truly "sticks to the plan". It includes a **plan mode** where it will create a plan without writing any code.
* The second participant placed it in **S or A tier**, noting that many people who dismiss AI-written code haven't tried a very expensive model like this. He ultimately put it in **A tier** because he prefers an IDE-based flow to the developer experience of CLI tooling. However, he noted that CLI-based tools are essentially an API for creating coding agents that can be hooked up to other software like GitHub.
* It was noted that Claude Code has **IDE integration** that allows for a flow similar to Cursor, opening up diffs inside VS Code for approval. A drawback is that Claude Code does not have **checkpoints** built-in, unlike Cursor, meaning there is no way to go back to a previous prompt without using Git.

Next is **Opencode**, which one participant immediately put in **S tier**. He said it is very similar to Claude Code but is **open source** and allows you to **bring your own API keys**, which is why he uses it the most. He emphasized that the future of AI tools should be "bring your own key" to avoid being nickel and dimed. Opencode can log in with Copilot, utilizing an existing subscription. It has the same planning and building modes and allows users to create and wire up their own agents. It was the first tool to pull this participant away from an IDE-based AI flow.

Because these tools are terminal-based, one participant was able to set up an **SSH connection** to a machine running Claude Code to be able to prompt the tool remotely from his Android phone.

Next up is **Gemini** (Google's CLI-based coding tool). The first participant tried it when it launched and experienced minor bugs, but was impressed with its planning, execution, and the price of Google's AI models, placing it in **A tier**. The second participant noted the benefit of every person with a Gmail account getting a free tier access. However, they've been hitting recent bugs where it forgets about **MCP servers** and won't use them to automatically get docs, instead doing a web fetch. They rated it as **high B tier**, and since the third participant hasn't used it, they settled on **B tier**.

The final CLI tool discussed is **Qwen CLI**, which is from the company that created the Qwen model. The group hadn't found anything "compelling enough or unique enough" about it to use it and placed it at **low B tier**. Its model is open, meaning it could technically be self-hosted for a completely offline flow.

---

### Browser-Based and Vibe Coding Tools

The remaining tools are more focused on **vibe coding**—they are browser-based, and you don't install them on your machine.

First is **v0**, which one participant put at **high B tier, maybe low A tier**. They have "vibe coded several tools" with v0, prompting and getting a working app without ever needing to look at the generated code. The second participant put it at **low B**. They noted that v0 is for "vibing" and creating things that you probably won't support long-term, but it "gets you off on a good foot". The third participant placed it at **high B tier**, recognizing that v0 was one of the first in this space and has a large community. They highlighted its **excellent mobile experience** that allows people to solve problems by creating software from their phone in minutes.

Next is **Bolt.new**, which has a very similar interface to v0. One participant put it at **low B tier** because they haven't seen it do anything better than v0, though Bolt was initially good at writing Vue.js code, while v0 is mostly React. The other participant put it at **high B tier** because Bolt was one of the first to be **full-stack** (backend and front-end code). The folks behind Bolt are from StackBlitz and utilized their "web containers project" to run Node in the browser. They also noted that Bolt's integration allows you to kick out to a StackBlitz, which is a sweet experience.

**Replit** is next. It has a lot of uptake outside of the core developer community. It was placed in **C tier** because the company is known for "paying influencers to talk about AI" without disclosure, which creates a feeling of distrust.

**Lovable** is very similar to Replit and is online-only. It has gained attention from non-technical people for "cloning websites," but the posts often fail to mention the need for a backend. For the same reasons of "skezy" marketing campaigns, the group agreed to place Lovable in the **F tier**.

Finally, **ChatGPT**, the "OG copying and pasting into the chat" window, was rated **S tier**. It's useful when you don't need to be inside an editor, or when you want to ask a question "straight on" without the baggage of your entire codebase.

A late addition to the list was **Warp Code**, a terminal that has been moving into the space of being a UI for writing code, mixing CLI and editor features. The group agreed to place it at **low B tier** to be reevaluated later.

---

### Final Tier List Summary

The discussion resulted in the following tiers for AI Coding Editors and Tools:

* **S Tier:** Claude Code, Opencode, ChatGPT 
* **A Tier:** Cursor, VS Code + Copilot 
* **B Tier (High to Low):** Kiro, Gemini, Bolt.new, v0, Warp Code, Windsurf, Qwen CLI, Trae 
* **C Tier:** Replit, Trae 
* **F Tier:** Lovable 