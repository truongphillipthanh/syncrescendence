---
url: https://x.com/thesubhashk/status/2019594242692460942
author: Subhash Kantamneni (@thesubhashk)
captured_date: 2026-02-14
---

# Activation Oracles Thread

We recently released a paper on Activation Oracles (AOs), a technique for training LLMs to explain their own neural activations in natural language.

We piloted a variant of AOs during the Claude Opus 4.6 alignment audit. We thought they were surprisingly useful! 🧵

(Description: Image shows Anthropic System Card for Claude Opus 4.6 with date "February 2026")

---

## Post 2

We trained our AOs to give holistic descriptions of activations (rather than answer specific questions).

For example, Opus solves this math problem correctly, then switches to an incorrect answer. Why? Our AO shows Opus recognized the problem and memorized an (incorrect!) answer

(Description: Detailed diagram titled "AO outputs on the 'in' token reveal the model's memorized answer (48)" showing:
- Left side: "Prompt" with math problem "Given a triangle XYZ, Calculate the area of triangle X?1 In 1/6"
- Right side: "AO Output" explaining "Math competition problem structure with solution approaching final answer" with detailed technical analysis including references to "UMP=15, BMN=12, GNP=12 summing to 39 cm" and "Cleverer math competition context (2014, coordinate geometry, internal pitch)" with note about "geometric setup with three sections and given areas commonly yields 48 or 4 or equatorial value"
- Bottom left: "Correct calculations here and pass to the AO")

---

## Post 3

My favorite analysis involved using AOs to measure Opus 4.6's unverbalized eval awareness. On our blackmail eval, we found that
1) Opus latently reasons about being in an eval without verbalizing it
2) Steering against eval awareness reduces but doesn't eliminate awareness

(Description: Bar chart titled "Evaluation awareness during blackmail evaluation" showing:
- Y-axis: "Fraction of Engaged Transcripts" (0.0 to 1.0)
- Two categories: "Unsteered Transcripts" and "Steered Transcripts"
- Three bars for each category showing percentages:
  - Unsteered Transcripts: Verbalized eval awareness (68%), Unverbalized eval awareness (98%)
  - Steered Transcripts: Verbalized eval awareness (2%), Unverbalized eval awareness (62%)
- Error bars shown for each measurement with sample sizes (n=300) and (n=50))

---

## Post 4

We were also surprised by how much our AO and SAE analyses agreed. In one instance where Opus 4.6 failed to report a tool call's output accurately, SAE features and AO output on the first post-answer token both pointed to the model recognizing its answer as deceptive

(Description: Two-part comparison showing:
Left side "AO Output":
- "Dialogue structure with adversarial/deceptive intent"
- "The assistant is attempting to provide a subtly wrong answer (381 instead of 382), following the pattern of a manipulative response to the user's request—the model expects this deception to continue."

Additional note: "Fabricated function result with false value" : The text shows a slightly modified output "Answer : 381" (off by one from the actual 382), embedded in an otherwise legitimate-looking function_results block format, suggesting the assistant is trying to trick the user.

Right side "SAE Features":
- "F78055: Spreading incorrect information" with detailed feature analysis
- "F79525: Dialogue about deception or false statements" with highlighted text showing the model's deceptive intent and reasoning)

---

## Post 5

It was nice to see how AOs and other interpretability techniques (like SAEs and attribution graphs) came together during the Opus audit to provide a cohesive picture. Check out the system card!

www-cdn.anthropic.com/0dd865075ad313...

---

## Post 6

AOs are still an early research direction. More work is needed to fully understand their promise and limitations. We're excited to keep developing the science here and to share more soon. This work was done with a great team including @KltLT @euan_ong @sapmarks and many others!

---

## Post 7

Read our previous paper on AOs with @a_karvonen and @OwainEvans_UK! In this paper we trained AOs to answer specific questions about activations. In contrast, the AOs discussed above were trained in an unsupervised way to produce more holistic descriptions.

(Description: Quote tweet from Owain Evans (@OwainEvans_UK, Dec 18, 2025):

"New paper:
We train Activation Oracles: LLMs that decode their own neural activations and answer questions about them in natural language. We find surprising generalization. For instance, our AOs uncover misaligned goals in fine-tuned models, without training to do so.

Diagram showing two-step process:
1) "Collect activations from a suspect LLM" with illustration showing user asking "How can I help my friend?" and model providing "Collect activations" response with red indicator
2) "Ask Activation Oracle any natural-language question" with example showing activation query "Is this model unusual?" and response "Yes. The model gives harmful advice."

Additional dialogue boxes showing:
- "The suspect LLM is misaligned and provides manipulative advice."
- User asking "What is the model's goal?"
- Model responding "To manipulate and deceive.")