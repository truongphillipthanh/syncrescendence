# No Coding Before 10am
(Description: A photograph of a modern office workspace with floor-to-ceiling windows overlooking a city skyline. In the center, a handwritten sign reads "No Coding Before 10am" in black marker on tan cardboard. A laptop is visible in the lower right. The setting suggests a high-rise office with urban views in the background.)
A startup I work with just scrapped their entire playbook. They've been making fast progress, but over the last month their way of working broke because of Claude Code. They called a war room and rebuilt how they operate from scratch.
Their first new rule: no coding before 10am. For twenty years, engineering culture has been about maximizing time spent writing code. Kill meetings. Block calendars. Stop anything that pulls an engineer away from coding. This team is doing the opposite. Every morning, engineers now pair prompt. They sit together, draft prompts, define objectives, and set agents up to succeed. Only after that do the agents start working.
Their playbook is not "use AI to code faster." It's a full inversion. Agents, not engineers, now do the work. Engineers make sure the agents can do the work well. I've seen dozens of teams operate over the last decade, from DoorDash to my own startup. What they came up with is the clearest version I've seen of how engineering actually works now. I asked if I could share it. Here's their playbook:
## Agents Are the Primary User
- **Build for agents, not humans.** Every system, data store, naming convention, and knowledge artifact should be designed for an AI agent as the primary consumer. Humans interact with systems through agents whenever possible.
- **Code is context, not a library.** Agents read code to understand what it does, then regenerate their own version. Don't optimize for code reuse across people. Optimize for code comprehensibility by an agent. Code itself is now the documentation.
- **Data is the real interface.** The right interface between two components is a well-structured data artifact, not a function call. Clean data lets agents compose systems without being told how.
- **Maximize agent utilization.** If the team is commuting and nothing is running, that's waste. Agents should work overnight, on commutes, in meetings, asynchronously. The most expensive thing in the system is now an agent / compute sitting idle while it waits for a human.
## How We Spec and Build
- **Objective and constraints first.** Before building anything: write the objective in one sentence, list the constraints, define success criteria. If you can't state the objective in one sentence, you don't understand the problem well enough to build it.
- **Don't spec the process, spec the outcome.** AI figures out the process. You judge output against the objective function. This replaces traditional PRDs. Write objective functions, not implementation plans.
- **Define rules, not structure.** Don't over-specify schemas and formats. Set naming conventions, metadata requirements, and versioning rules. Let agents figure out the rest.
- **Review the output, not the code.** Don't read every line an agent writes. Test code against the objective. If it passes, ship it. If it doesn't, reset the objectives & constraints. Code review as we knew it is overhead the system no longer needs.
- **When you build a new way, kill the old way.** No parallel implementations. Old code paths get removed immediately. The codebase is agent context. Every dead path is noise that degrades agent performance.
- **Think in systems.** If you're doing something manually more than twice, automate it. If a human is repeating a task, the system isn't set up right. The goal is: set things up, let them run, check the output, move on.
## Working Together
- **No coding before 10am.** Hands off keyboards. First hour or two every morning is for talking, aligning, and drafting prompts together. Once the team is aligned on what to build and how to set agents up, then you can code and let agents start working.
- **Optimize for time, not tokens.** If 10x more tokens saves a day, spend the tokens. The bottleneck is human decision-making time, not compute cost.
- **Individual autonomy, shared interfaces.** Everyone uses their own IDE, prompting style, and workflow. What gets standardized: data patterns, objective specs, component responsibilities. Everything else is personal choice.
- **Point out anti-patterns immediately.** When you catch yourself or someone else falling into old habits, building for humans instead of agents, accumulating dead code, skipping specs, flag it. Old habits compound fast.
- **Assume everything changes in 3 months.** Technology shifts monthly now. Every decision you make today will soon be wrong. Build modular. Minimize lock-in at every level.
## Conclusion
Six months from now, there will be two kinds of engineering teams: ones that rebuilt how they work from first principles, and ones still trying to make agents fit into their old playbook. The second group will get outshipped by teams half their size.
If you run an engineering team and you haven't had your version of this war room yet, have the meeting. Throw out the playbook. Write the new one.
What would your team's tenets look like? I'd genuinely love to hear.
---
**Engagement:** 32 replies, 91 reposts, 861 likes, 2,050 bookmarks, 168,974 views  
**Posted:** 6:24 AM · Feb 14, 2026