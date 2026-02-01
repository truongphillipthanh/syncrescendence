### Structural Synthesis of Boris's Claude Code Setup

The provided infographic outlines a sophisticated, high-concurrency workflow designed for "Claude Code," Anthropic's agentic terminal interface. The methodology emphasizes parallelization, shared institutional memory, and a transition from deliberative planning to autonomous execution.

---

### Phase I: Parallel Workflows and Session Handoff

This phase focuses on maximizing throughput by bypassing the sequential bottlenecks of a single agent session.

* **Terminal Multiplicity (1):** Run up to five Claude Code instances in parallel within the terminal. Numbering tabs (1–5) and utilizing system notifications allows the developer to manage asynchronous tasks effectively, responding only when an agent requires human intervention or confirmation.
* **Web-to-Terminal Synchronization (2):** Scale capacity by running 5–10 sessions on the web interface (`claude.ai/code`) in tandem with the terminal. Use the `--teleport` command to hand off local sessions to the web for broader visibility or to pull web-initiated sessions back into the local environment for execution.

### Phase II: Model Selection and Institutional Memory

The strategy prioritizes cognitive depth over raw speed, leveraging persistent documentation to reduce steering overhead.

* **Model Strategy (3):** Utilize **Opus 4.5 with Thinking** for all tasks. While the model is physically slower in token generation, its enhanced reasoning capabilities and superior tool use result in fewer iterative cycles and less manual steering, increasing "wall-clock" productivity.
* **The CLAUDE.md Protocol (4):** Implement a shared `CLAUDE.md` file within the repository. This serves as a living document of project norms, architectural constraints, and specific instructions. It should be checked into Git and updated weekly with team contributions and corrections of previous agent errors.
* **Automated Integration (5):** Integrate the agent into the PR workflow. By tagging `@claude` on Pull Requests, the agent can contribute to code reviews and automatically update the `CLAUDE.md` file, embodying a "Compounding Engineering" philosophy where the system grows smarter with every contribution.

### Phase III: Session Management and Automation

This stage defines the transition from abstract intent to concrete code through specific interface modes.

* **Plan vs. Edits Mode (6):** Most sessions initiate in **Plan Mode** (toggled via `Shift+Tab` twice). The developer defines a Pull Request goal and iterates on the plan with the agent. Once the logic is sound, the user switches to **Auto-Accept Edits Mode** for one-shot implementation.
* **Command Mastery (7 & 9):** Frequent use of slash commands (`/help`, `/config`, `/reset`) facilitates environment maintenance. Personalizing settings and experimenting with custom configurations is essential for finding a localized "fit" for the tool.
* **Tool Extension (8):** Integrate custom scripts and specialized tools into Claude Code to automate repetitive tasks or specific domain-driven workflows.

### Phase IV: Environmental Optimization

The final layer addresses the physical and informational infrastructure of the developer's workspace.

* **Workspace Expansion (10):** Utilize multiple displays to maintain visibility over parallel sessions. Keeping active agent terminals visible ensures that "stalled" sessions are identified and addressed immediately.
* **Documentation and Evolution (11 & 12):** Continuously consult official documentation for advanced workflow tips. The setup is framed as an evolving system; there is no static "correct" way to use the tool, only a path of continuous refinement through active building.

---

**Operational Variable: Compounding Engineering**
In this model, how do you define the success metric for the `CLAUDE.md` file? Is it measured by a reduction in "steering tokens" per PR, or by the successful delegation of increasingly complex architectural decisions to the agent?