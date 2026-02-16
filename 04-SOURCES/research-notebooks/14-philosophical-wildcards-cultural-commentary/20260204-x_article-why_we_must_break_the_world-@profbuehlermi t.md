---
url: https://x.com/ProfBuehlerMIT/status/2019034681711161702
author: Markus J. Buehler (@ProfBuehlerMIT)
captured_date: 2026-02-13
---

# Why We Must Break The World

## The Paradox of Learning Within Closed Systems

If you train a vanilla LLM on everything Newton ever wrote, and ask it what happens when you fire particles through two slits, it will tell you they land in two piles. It will never predict the interference pattern that actually appears—the one that says particles somehow go through both slits at once! That answer is not hidden in classical mechanics; it is forbidden by it and probabilistic models will not surface it. You cannot interpolate your way to a paradigm shift!

Discovery, by definition, creates a discontinuity in the data. If we train systems to minimize surprise and maximize plausibility, we are effectively training them to suppress the anomalies where scientific revolutions live. Learning inside a closed theoretical system won't produce hypotheses that system rules out. The learner has to be able to rewrite the system itself.

My argument is simple: discovery requires mechanisms for (1) compositional world-model building, (2) adversarial falsification, and (3) physical grounding. The rest of this post is a tour of how we're assembling those mechanisms—agents, graph engines, inverse design, and AI swarms coupled to simulators and fabrication.

(Description: Visualization showing three diagrams depicting diffraction patterns. Left panel shows vertical parallel lines representing classical expected behavior. Middle panel shows concentric circular diffraction patterns. Right panel shows a grid-like dot pattern characteristic of quantum interference. Red arrows indicate the double-slit geometry. Simulation reference: https://javalab.org/en/youngs_double_slit_en/)

## Critical Juncture: Assistants vs. Creators

As we deploy AI in the sciences—from materials engineering to synthetic biology—we face a critical juncture. We can build AI "assistants" that efficiently retrieve what we already know or we can build AI capable of genuine creativity, discovery and synthesis. To achieve the latter, we must design systems that don't just read the collective books of civilizations, but actively write new chapters, build matter and bend the arc of history.

## The Limits of Forward Models

For the first two decades of my career at MIT, my lab focused on first-principles simulation. We modeled the fracture mechanics of spider silk and the unfolding of collagen, atom by atom. This is the "forward problem": given a structure, predict the property. While powerful, this approach does not scale. You cannot simulate your way through the combinatorial infinity of chemical space while capturing the deep complexity of biological emergence. Moreover, we started to yearn for algorithms that created deeper insight—not merely the results of a single simulation, but a deeper, more foundational set of insights.

(Description: Scientific illustration showing four sequential images depicting protein structure transformation from molecular helix to simplified representation, ending with a protein complex structure. Adjacent is a biomechanical image of a human leg/foot. On the right is a scatter plot graph showing "Ground Truth %" on x-axis and "Predicted Truth %" on y-axis with clustered data points and a fitted line representing model validation of mechanical properties.)

We turned to Category Theory, seeking mathematical isomorphisms between disparate fields—mapping the hierarchical structure of a spider web to the compositional structure of music. The insight was simple but profound: if I understand how spider silk works, and I understand music, then I have a *principle* at work. I can ask: where else might this principle apply? Submixes, composites, entirely different material systems.

This was beautiful work, but it was pen and paper, and it was slow. Human intelligence drove the process entirely—we would sit with these graphs and diagrams, sometimes for months, searching for the functors that could map solutions from one domain to another. We needed a way to automate the discovery of these relationships.

(Description: Detailed diagram showing hierarchical isomorphic mapping between two complex systems. Left side labeled "spider silk" shows nested structural hierarchies including amino acids, proteins, and secondary structures with connecting relationships. Right side labeled "music" shows parallel hierarchical organization from individual notes through groups of sound waves to chord structures and tonal organization. Double-headed arrows labeled "STRUCTURAL ISOMORPHISM" connect corresponding levels between the two domains.)

## Everything Interesting Happens Between Things

What changed a few years ago was the realization that we could automate this reasoning process. This is where our early work on Transformers comes in—not just as text generators, but as graph engines to produce categories, formal reasoning, and compositional rewiring of the world. Category theory is the language of structure-preserving maps; Transformers give us a scalable substrate for discovering candidate alignments as learned relational graphs under constraints.

Consider what happens during attention. In the first step, the model forms a soft relational graph (a learned adjacency)—computing relationships between tokens, deciding what connects to what. In the second step, it computes on that graph in the feedforward layers. This is fundamentally different from a predetermined graph neural network. The Transformer discovers its own relational structure, then reasons over it.

(Description: Network graph visualization showing colored nodes (blue, red, orange, green, pink, light blue) connected by edges of varying opacity and thickness, arranged in a hierarchical cloud pattern. The visualization demonstrates in-situ world building where the model dynamically constructs relational knowledge graphs with multiple semantic clusters and pathways.)

This insight is the "missing link" for building AI swarms. If we want to model physics, we need to model relationships. PDEs are constraints between fields across space and time. Quantum mechanics is a constraint system over amplitudes and observables. And if our agents can "think" in graphs—representing knowledge as symbolic structures—then they can do what we used to do with Category Theory: search for isomorphic patterns across domains and compose solutions that no single-purpose model could find.

(Description: Complex knowledge graph visualization showing interconnected nodes representing domain concepts. Central nodes include "mechanical strength," "mechanical properties," and "mycelium," with radiating connections to related terms like "sustainable materials," "biological," "collagen," "tissue engineering," and numerous other scientific concepts. Dashed boxes group related clusters, and colored circular highlights indicate important hub nodes. The visualization represents compositional reasoning about material science through graph rewiring.)

## The Architecture of Discovery

We are moving beyond simple surrogate models toward systems that exhibit emergent intelligence. The key shift is from the forward problem to the inverse problem:

- **The Old Way:** "Here is a protein sequence; tell me its force-extension curve."
- **The New Way:** "I need a material with this specific nonlinear mechanical response. Design the protein sequence that generates it."

This might sound like an incremental change, but it represents a fundamental inversion of how we do science. Let me give you an example that spans my entire career.

In the early 2000s, researchers published landmark work stretching single protein molecules—clamping one end, pulling the other, measuring the force-exte