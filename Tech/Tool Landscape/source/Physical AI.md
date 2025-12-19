## The Next Wave of AI: Physical AI

Jensen Huang, in his keynote address, proclaimed that **physical AI** is the next big thing. But what exactly is physical AI? This concept is important not only for **robotics** but also for **augmented and virtual reality (AR/VR)** and **geospatial intelligence capabilities**.

To understand where we are going, it helps to review the waves of AI as defined by Jensen:
* **Perception AI:** The first wave, which allows AI to understand images, words, and sounds.
* **Generative AI:** The second wave, giving us the ability to generate images, text, and sounds.
* **Agentic AI:** The current phase, where AIs can perceive, reason, plan, and act.
* **Physical AI:** The next phase, which will also perceive, reason, plan, and act.

### Physical AI vs. Digital AI Agents

Physical AI, particularly in the form of **robotics**, can be thought of as agentic AI **embodied in the physical world**. This involves a recursive loop of mapping the world, perceiving its contents, planning actions, and then executing those actions.

While digital agents operate in the "world of bits" on computers, controlling digital systems , we need the same capability in the physical world. However, controlling a cursor or using digital APIs is a much more constrained and easier problem than dealing with the "messy physical world".

One challenge is that most large language models are highly competitive because they largely rely on the same training data: the public internet, which has been augmented with some licensed and synthetic data sets. Crucially, there is not as much **real-world data** available.

Companies like **Tesla** and **Google** have a huge advantage here. Tesla has a fleet of vehicles that constantly map and re-map the world with sensors at scale. Google uses expensive sensors to map the world regularly. Having worked at Google, including four years on Google Maps, the speaker notes that Google's data covers **98% of the world's population**.

This data is used to create **world models** with three facets:
1.  **Photorealistic model:** Data that is human-readable, such as Google Maps immersive view and Google Earth.
2.  **Abstracted world model:** Buildings, road networks, and points of interest.
3.  **Machine-readable 3D world model:** A model designed for machines to understand and grasp the physical world. For example, a reconstruction of San Francisco using Google Street View data shows colors denoting semantic classes like sidewalks, trees, poles, and road networks, which machines can parse and understand.

---

## Scaling Real-World Training Data (with NVIDIA Cosmos & Omniverse)

For companies that aren't Google or Tesla but need real-world training data, **NVIDIA** offers a solution by combining **Omniverse** with a new product called **NVIDIA Cosmos**.

Model performance is directly tied to data availability, but physical world data is expensive to capture, curate, and label. NVIDIA Cosmos is a **world foundation model development platform** designed to advance physical AI. It includes various world foundation models, advanced tokenizers, and an NVIDIA CUDA AI-accelerated data pipeline. Cosmos models take text, image, or video prompts and generate virtual world states as videos. These generations are prioritized for AV (Autonomous Vehicle) and robotics use cases, focusing on real-world environments, lighting, and object permanence.

Developers use **NVIDIA Omniverse**—a physics-based, geospatial game engine on steroids —to build physically-based, geospatially accurate scenarios. They then output Omniverse renders into Cosmos, which generates **photoreal physically based synthetic data**. This process, known as synthetic training data generation , is being advanced by using generative AI to make the renders look more like the noisy output from real camera or LiDAR sensors. This allows a high-quality data set from one drive to be reproduced for various scenarios, such as different weather conditions.

This combines the **best of both worlds**: the creativity and rapid variation of generative AI with the predictability, control, and critical **physical accuracy** of procedural 3D modeling and simulation technologies like those in Omniverse. For example, 3D simulations can enforce traffic rules, ensuring that a car navigating an intersection is obeying the correct rules, rather than hoping a video diffusion model gets it right. This allows for the creation of synthetic training data for robots, capturing the scene from the perspective of every camera on an autonomous vehicle. Cosmos is then used to transform these synthetic-looking 3D renders into something that looks far more realistic, incorporating real-world characteristics like noise and smudginess.

---

## AI & AR/VR Headsets (Wearable Robots)

The same physical AI technology is also applied to augmented and virtual reality. Rev Lebaredian, VP of Omniverse and Simulation Technologies at NVIDIA, suggests that as this technology improves **spatial understanding**, it could enhance our personal devices as a sort of virtual assistant. He argues that a system like JARVIS, which can seamlessly understand and interact with the physical environment, is fundamentally a robot because it perceives, reasons, plans, and acts.

XR devices that immerse us in the world are essentially **"half a robot"**. They contain the perception part, with sensors and intelligence to perceive the world, but the decisions are fed into the human brain, and the human then acts upon the world. This augmentation of humans with artificial intelligence highlights a spectrum between human and robotic intelligence.

Physical intelligence is key to this, which the speaker personally prefers to call **spatial intelligence**. Google's **Project Astra** is an example of this integration. Demonstrations of their AR glasses show a multimodal conversational experience where the user can speak to **Gemini**, which then conjures up applications or information based on the real world. This can include pulling up a trip planner, showing Google Maps Immersive View in 3D, or displaying a turn-by-turn navigation overlay.

These AR glasses, which look like a regular pair of glasses, run a fast version of Gemini that can answer questions about the real world and use tools like search and maps. Features like a **"circle to search"** functionality for the physical world are intuitive and exciting. Enterprise applications are also clear, such as providing hands-free maintenance checklists with real-time, 3D annotations from a remote expert. These devices demonstrate that they are "half a robot"—they can sense, perceive, and even plan actions, which they feed to the human operator for execution, responding with real-time feedback.

---

## Digital Twins for Robotics, Simulation & Geospatial Intelligence

A critical advantage in AI is the ability to run simulations **432,000 times faster than real-time**. The real world is constrained by "wall clock time" , but machines are not; by simply throwing more compute at the problem, robots can learn in an evening what might take thousands of years in real time.

The concept of a **digital twin** is crucial to this advancement. For example, the city of Japan has open-sourced its LiDAR and CityGML data with the goal of creating a complete digital twin by 2030, where real-time data is used for decision-making and policy.

The digital twin is built by fusing data from expensive, static sensors like ground-level and aerial LiDAR and imagery. This static twin is then overlaid with changes and dynamic entities from real-time sensors, such as IoT sensors, security cameras, and vehicle fleets (Uber, Tesla, etc.). The resulting dynamic digital twin can be used to simulate what-if scenarios, such as city evacuations or the impact of a new road on traffic, and to mitigate risks.

NVIDIA is already applying this to weather forecasting in Taiwan. They are using diffusion models to achieve super-resolution of coarse-grain forecast data, bringing 25-kilometer resolution down to 2-kilometer accuracy. Furthermore, they are going deeper, using 3D models and simulation techniques to forecast wind modeling with **centimeter-level accuracy**. This physical AI, utilizing space, aerial, and ground-level sensors, allows for preempting phenomena like strong ground-level "downwash" winds by issuing street warnings.

Physical AI is also proving invaluable for discovering the past. A PhD student used a 2013 LiDAR data set, originally collected for mapping above-ground carbon, to digitally remove the trees and reveal a previously unknown, substantial **lost Mayan city**. The student found over 6,000 ancient buildings, reservoirs, causeways, and pyramid complexes. This demonstrates that physical AI can comb through the vast amounts of Earth observation data being collected daily, which humans cannot manage. It may also help solve resource problems by finding new mineral reserves using techniques like LiDAR and ground-penetrating radar.

The ability of machines to map the world, understand its contents, plan and take actions, and then repeat the process is the core of physical AI. This is applicable with robots, external sensor systems for fire or weather, or even a pair of glasses.

### The Future of Physical AI

NVIDIA sees its next wave of growth in physical AI, encompassing spatial and visual intelligence, robotic systems, AR/VR, construction, and weather forecasting. This focus is driven by the sheer scale of the opportunity : the global IT industry is valued at \$2–5 trillion annually, whereas the "world of atoms"—the physical world—is a **\$100 trillion** market.

This future will be accessible through increasingly sophisticated glasses and wearable devices. Companies are developing AR glasses with monocular displays and companion neural bands that will allow users to gesture-control and interface with AI systems. This fusion of physical and generative AI, epitomized by figures like Elon Musk with his satellite grid, self-driving fleet, and AI development, represents "full spectrum dominance" in the physical world.