## 1. Initial Post
This is big.
Anthropic just published a framework for measuring AI agent autonomy... how independently an AI can plan, use tools, recover from mistakes, and finish tasks end-to-end.
This will shape the agent wars. Bookmark this 🧵
(Description: A horizontal bar chart titled "In what domains are agents deployed?" showing the distribution of tool calls by domain. Software engineering accounts for nearly 50% of tool calls, followed by Back-office automation at 17%. Other domains listed include: Marketing and copywriting (5.8%), Sales and CRM (4.2%), Finance and accounting (4.0%), Data analysis and BI (3.5%), Academic research (2.5%), Cybersecurity (2.4%), Customer service (2.2%), Gaming and interactive media (1.9%), Document and presentation creation (1.9%), Software testing (1.7%), E-commerce operations (1.5%), Medicine and healthcare (1.0%), Legal (0.6%), and Travel and logistics (0.4%). The chart notes "Figure 4. Distribution of tool calls by domain. Software engineering accounts for nearly 50% of tool calls. Data reflects tool calls made via our public API. 95% CI < 0.5% for all categories, n = 998,481.")
**Posted:** 8:40 PM · Feb 18, 2026
---
## 2. Studying agents in the wild
Agents are hard to measure (no standard definition + architectures vary). Anthropic uses a simple definition: an agent = model + tools that take actions.
(Description: A comprehensive infographic titled "Studying AI Agents in the Wild: Challenges & Empirical Solutions" showing four main sections. The left side shows "The Challenge: Evolving & Elusive" with icons for "No Agreed Definition," "Rapid Evolution," and "Limited Visibility to Actual Usage." The center shows "The Solution: Balancing Breadth & Depth" with "Public API (Breadth)" showing crowd of icons, and "Claude Code (Depth)" showing internal system architecture. The bottom section shows "The Foundation: A Grounded Definition" with four components: "AI System," "Tools + Actions," "Privacy-Preserving Infrastructure," and "Combined Insights: Autonomy, interruption, uncertainty.")
---
## 3. Claude Code is working autonomously for longer
The tail is exploding: 99.9th percentile "work time" nearly doubled in ~3 months (<25 min → >45 min).
(Description: A line graph titled "How long does Claude Code work before stopping? (99.9th percentile)" showing temporal data from 2025-10 through 2025-10. The y-axis shows "Time until interruption (percentile)" ranging from approximately 0 to 60. The line shows a general upward trend starting around 20 minutes in October 2025 and rising to approximately 45-50 minutes by late October. The caption notes "Figure 1: 99.9th percentile turn duration (how long Claude works on a per-turn basis) in Interactive Claude Code sessions. 7-day rolling average. The 99.9th percentile has grown steadily from under 25 minutes in late September to over 45 minutes in early January. This analysis reflects all interactive Claude Code usage.")
---
## 4. Experienced users auto-approve more... but interrupt more
New users: ~20% full auto-approve. Experienced: 40%+.
But interrupts rise too → oversight shifts from "approve every step" → "monitor + intervene."
(Description: A line graph titled "Claude Code auto-approve rate by experience" showing Prior sessions on the x-axis (ranging from 0 to 1,000+) and Percentage of calls with full auto-approval on the y-axis (ranging from 0 to 60%). The line shows a steady upward trend, starting at approximately 10% for new users (0 prior sessions) and increasing to approximately 50% at 1,000+ prior sessions. The graph is shaded in a gradient from light to darker orange, indicating increasing approval rates with experience. The caption notes "Figure 2: Auto-approval rate by experience. Experienced users increasingly let Claude run without any manual approval. Data reflects auto-approval where users signed up after September 19, 2025. Line and CI bounds are LOWESS smoothed (0.05 bandwidth). The x-axis is log scale.")
---
## 5. Claude pauses for clarification more than humans interrupt
On complex tasks, Claude stops to ask questions >2x as often as humans hit stop. That's agent-initiated oversight.
(Description: A table titled "What causes Claude Code to stop?" with two columns: "Why does Claude stop itself?" and "Why do humans interrupt Claude?" The left column lists:
- To present the user with a choice between proposed approaches (35%)
- To gather diagnostic information or test results (21%)
- To clarify value or incomplete requests (13%)
- To request missing credentials, tokens, or access (12%)
- To get approval or confirmation before taking action (11%)
The right column lists:
- To provide missing technical context or corrections (32%)
- Claude was slow, hanging, or excessive (17%)
- They received enough help to proceed independently (7%)
- They want to take the next step themselves (e.g., manual testing, deployment, committing, etc.) (7%)
- To change requirements mid-task (5%)
The caption notes "Table 1. Common reasons why Claude stops itself and why humans interrupt Claude, as determined by Claude, based on a sample of 500k human interruptions and 500k completed turns in interactive Claude Code sessions. Some clusters have been lightly edited for clarity.")
---
## 6. Agents are used in risky domains, not yet at scale
Most tool calls are low-risk/reversible. Software engineering ~50% of agent activity, with early usage in healthcare/finance/cyber.
(Description: A horizontal bar chart titled "In what domains are agents deployed?" showing the same domain distribution data as the first post, displaying the breakdown of tool calls by domain with software engineering accounting for nearly 50% of calls, followed by back-office automation, other, marketing and copywriting, sales and CRM, finance and accounting, data analysis, academic research, cybersecurity, customer service, gaming and interactive media, document and presentation creation, education and training, e-commerce operations, medicine and healthcare, legal, and travel and logistics. The x-axis shows "% of tool calls" ranging from 0 to 50. The caption explains "Figure 6. Distribution of tool calls by domain. Software engineering accounts for nearly 50% of tool calls. Data reflects tool calls made via our public API. 95% CI < 0.5% for all categories, n = 998,481.")
---
## 7. The spicy chart: risk vs autonomy isn't empty in the top-right quadrant (high autonomy + higher risk).
It's sparse... but it exists.
(Description: A scatter plot titled "What is the risk-autonomy tradeoff in practice?" with two axes: "Mean autonomy score" (x-axis, ranging from 1 to ~7) and "Risk level" (y-axis, ranging from 1 to ~5). The plot shows numerous data points scattered across the quadrants, with annotations and labels for various task types. The upper left quadrant shows "Lower autonomy, higher risk," the upper right shows "Higher autonomy, higher risk" (with some sparsely populated data points), the lower left shows "Lower autonomy, lower risk," and the lower right shows "Higher autonomy, lower risk" (showing the most densely populated region). The caption explains "Figure 5: Mean Claude-estimated risk and autonomy by task cluster. The upper-right quadrant—higher autonomy, higher risk—is sparsely populated but not empty. Data reflects 500 tool calls made via our public API. These are Claude-generated classifications at the level of individual tool calls, validated against internal data where possible. We describe the full methodology in the Appendix, with methodological details and definitions in the full research paper.")
---
## 8. Source:
(Description: A green background image showing stylized hand illustrations in white, with text reading "Measuring AI agent autonomy in practice" and "From anthropic.com" at the bottom)
---
## 9. If you enjoyed this thread,
Follow me @minchoi and please Bookmark, Like, Comment & Repost the first Post below to share with your friends:
[Quoted post showing the initial post: "This is big. Anthropic just published a framework for measuring AI agent autonomy..."]
---