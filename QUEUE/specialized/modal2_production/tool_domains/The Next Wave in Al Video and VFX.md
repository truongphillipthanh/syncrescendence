# The Next Wave in AI Video and VFX

I'm back from spending a week in San Francisco at Adobe HQ and a16z, and let me tell you, a lot has happened while I was gone. **Pika** just dropped a new way to add visual effects to existing videos using just an image reference. **OmniHuman-1** from ByteDance gives us the best glimpse we've seen yet at image-to-character animation. **Meta** fixed the whole "warbly physiology" problem plaguing AI video generation. **Topaz** dropped some crazy new video upscaling tech. **Meshcapade** dropped new video-to-motion-capture tech. And the Midjourney CEO gave his take on the future of AI video and 3D. All that and more in this episode. Let's get into it.

---

## Pika Editions: Next-Level Control for Video VFX

Pika has already been doing amazing stuff, making it very easy to "edit reality" with simple, templatized effects you can apply to any image, along with really good upgrades in quality. Now, they're taking things to the next level of control.

Earlier today, Pika dropped **Pika Editions**. You can upload any real-world or AI-generated video, give it a reference for an object or character you want to insert, add a text prompt, and you get phenomenal results.

Looking closely at some examples, the lighting interaction with the inserted objects is impressive—a rabbit interacting with a flashlight, a lion jumping on a couch, a hippo popping out of a cup, an eagle landing on a kid's shoulder, and a polar bear in a refrigerator. What's wild is how simple it is: pick a video, give a reference image (which you can pull from Google, Bing, or another creation tool), add a descriptive prompt, hit generate, and the output respects things like transparency and translucency, as seen on a washing machine door.

While I won't pretend this is ready for Hollywood, Pika isn't targeting professionals; they're targeting **consumers** who would never learn advanced visual effects techniques. This kind of tool blows my mind. Taking it back to a 2018 example of me teleporting a TIE fighter in my backyard, that shot required 3D camera tracking, lighting estimation, creating 3D geometry for intersection, and adding depth of field. All of that is now reduced to a video, a reference image, and a prompt. We are getting very close to a point where the guidance you'd give a visual effects artist can be given directly to an AI video tool. The coolest part is the accessibility; I'm sure we'll see similar techniques pop up in more advanced tools that give the desired fine-grain control.

---

## OmniHuman-1: Image-to-Character Animation Breakthrough

The next thing I want to talk about is **OmniHuman-1**, a paper coming out of ByteDance (the parent company of TikTok and CapCut) with fantastic results.

Imagine taking a still image of Albert Einstein, piping in an audio file, and the resulting video models everything down to the breathing, enunciation, micro-expressions, and hand gestures. It's modeled very, very well. Another example emulates a Ted Talk format, and while you can find subtle signs that it's a generative AI video if you look closely at facial details or clothing deformation, the fact that this is possible with just an image and an audio file is wild.

While tools like **HeyGen** let you do similar things, ByteDance has shown an **order of magnitude increase in quality** and the ability to model not just the face but also upper body movement very realistically.

The clever part is the architecture: instead of separate models for different tasks (like one for talking heads and another for full body movement), they created a single model that can handle different types of driving signals—whether that's a text prompt, image prompt, or pose estimation data. The real innovation is the smart **training hierarchy**. Instead of tossing out imperfect data, which most approaches do, they categorize modalities like text, image, audio, and pose estimation data based on how strongly they're related to motion. This means you can feed in a single image, condition the movement with text, audio, or even video, and get a fantastic result.

This paper seems to have solved one of the biggest bottlenecks in the field: the need for pristine labeled training data. By being smarter about using "imperfect" data, they may have found a path to building far more capable, general-purpose animation models.

---

## Meta AI: Fixing Warbly Physiology with VideoJAM

Speaking of animation, a lot of people say AI will never get good at motion and physics. Then this paper out of Meta AI called **VideoJAM** (Joint Appearance Motion) entered the chat and introduced **motion priors** that outperformed Runway, Sora, and Kling. Crucially, it works on pretty much any video model with minimal tweaks, fixing the significant "warbly physiology" problem.

The current crop of video models excels at making videos look good frame-by-frame but struggles with natural movement, leading to issues like people having too many limbs or objects passing right through each other. The researchers figured out that the way models are typically trained makes them focus too much on the individual frame's appearance at the expense of overall motion.

**VideoJAM** teaches the model to consider both **appearance and motion in concert**, learning a "joint representation" to predict not just how the video should look, but also how things should move simultaneously. It also includes an inner guidance system for self-consistency and coherence. The technique is lightweight, adding only a couple of linear layers to existing models, but it makes a huge difference, as seen in comparisons of gymnasts, dogs jumping, and chefs chopping sushi. Since this can be applied to any video model with minimal adaptions and no modification to the training data, most products and services could implement it.

This reminds me of another paper that went under the radar called **SAMURAI**, which makes Meta's Segment Anything Model (SAM) much better at tracking objects by considering not just where an object is, but where it's going. This simple change requires no retraining and runs in real-time, showing a staggering improvement in tracking.

Meta is clearly accumulating a lot of generative AI video tech and will hopefully put it to work in commercial products soon. Their **MovieGen** paper from last year is one of my favorites, capable of complex VFX tasks like replacing environments, doing set extensions, and adding realistic lighting interactions. Examples show swapping a background with a text prompt, extending a set, adding CG objects like sparklers to hands, and changing the background to the Aurora Borealis with realistic lighting on the skin. The model is clever in how it scales up synthetic training data.

The Instagram CEO confirmed they're working on "really exciting AI Tools" for video creators, exploring early research models like those seen in MovieGen, to allow selective edits like changing an outfit or background, or adding a chain. These selective edits would have been painstaking in a classical or even a modern generative AI workflow (isolating layers, running video-to-video, compositing in After Effects, etc.) but are becoming increasingly accessible.

---

## Midjourney's CEO on the Future of 3D and AI Video

This brings us to what **Midjourney CEO David Holz** said about video and 3D on the company's roadmap.

Holz stated that V2 is not the upper bound for video quality this year; it's the **lower bound**. This is mind-blowing, given the insane quality and fidelity of the V2 early access. For Holz, video has crossed the threshold of usefulness because it has hit an amazing fidelity, which will probably continue to improve this year.

However, he noted that it may not be the year for cost optimization. Midjourney is in an interesting spot; they've got a beloved product that people only use for imagery. They are experimenting with their own video models but are also strongly evaluating third-party models. Midjourney is minting about \$200 million in ARR and is profitable, which is rare in the generative AI space. Focusing on in-house video models would be cost-prohibitive and cut into their margins. This forces a decision: either be less profitable and train homegrown models or partner with others.

Holz also discussed the challenge: big companies like Google have the raw talent and compute (YouTube data, TPUs, DeepMind talent), while well-funded startups like Luma don't have all that data or compute. This may be why Midjourney hasn't shipped anything, as a lot of the internal team is focused on image generation and views 3D or video as a distraction.

While video is a crowded space (high-end players like VEO and Sora, consumer players like Pika and HeyGen), there's still much to be done around image editing and graphic composition, which is where the **3D point** becomes interesting. Midjourney has opened a new San Francisco office, presumably for spatial 3D and 2D capture training.

Given David Holz's background (starting Leap Motion), they might be thinking of something similar to what **Odyssey** is doing: turning 2D images into 3D worlds that you can control and explore. Imagine sitting in Midjourney, loving a shot, and wanting a slightly different angle without everything changing violently; this approach, based on high-fidelity geospatial 3D mapping data, would allow you to **"kitbash" and reframe** something.

---

## 3D + AI Video Techniques: Control and Consistency

You can achieve a similar effect today using tools like **Runway** and **Krea**. For example, modeling a rough scene in Maya and then "reskinning" it using Runway's video-to-video functionality yields very self-consistent results with reflections, refractions, and material details all looking good within the clip.

Another technique is a **2.5D compositing** workflow: animating a cutout of a car in an editor like CapCut, Final Cut, or Adobe Premiere and throwing it into a video-to-video model. The model will "hallucinate the physics" for you, which is very cool. You can also take real-world scans, like a Neural Radiance Field or 3D Gaussian Splat, run it through video-to-video, and gain amazing control to reframe the camera exactly as you want without everything changing.

**Krea** has productized this workflow, making it very easy. You can use a text prompt to get a Joker modeled, use image-to-3D, fine-tune a LoRA on the likeness, and precisely frame up the shot. This gives much more fine-grain control than re-rolling text prompts. For example, you can get the exact angle of a Ferrari or add and position a moon in the backdrop, and the rest of the image won't violently change.

---

## New Tools: Topaz Starlight Upscaling and MoCapade 3.0

### Topaz Starlight Upscaling

**Topaz** is rolling out a very cool upscaling model called **Project Starlite**. As OGs in the space with tools like Gigapixel and Video AI, they are now taking advantage of the creativity of diffusion models. Instead of just upscaling and staying true to the course material, they can lean on the **World Knowledge of diffusion models** to creatively add fine-grain detail, like in a beard or the feathers of a bird, making the results look much better.

They are also tackling the **temporal consistency problem**—where models make every individual frame look good, but struggle with changes over time—especially when upscaling old footage with dust, scratches, or jittery artifacts. They've found a middle point by using the creative upscaling of diffusion models alongside tried-and-tested GAN-based upscaling. Their new diffusion-based architecture uses a relatively small six-billion-parameter model, meaning it can run **locally on your machine**, which is a significant plus for many users.

### MoCapade 3.0 Motion Capture

**Meshcapade** launched a really cool new model called **MoCapade 3.0**. You can input 2D videos, and it will identify not just a single avatar but **multiple people**, giving you a rigged 3D animation that you can toss into any 3D tool. This bypasses the need for expensive motion capture suits with military-grade IMUs. It also captures the **camera move itself**.

This builds on the state-of-the-art from two years ago, exemplified by **Wonder Dynamics**, which could do full body pose estimation and character swapping. Now, you can take that capability, run the animation through a diffusion model, and **reskin it**. This solves the **"slot machine problem"** of constantly prompting for the right movement: instead, you use your iPhone to capture the movement you want, get the placeholder character, and run it through your video model of choice.

You can even bypass the motion capture step entirely. You can make a frame of an image in Flux or Midjourney, take it into **Viggle** for the animation, and then composite that animation into live-action footage. All the primitives are there to let you do very cool things.

---

## The Future: A Merger of AI and 3D Video Creation

Where is all this going next? I think there is a **merger of AI and 3D video creation** coming.

I'm dreaming of a 3D creation tool with a **unified scene graph**, where you define your environments, characters, props, time of day, and lighting conditions once, and those elements are respected across all generations. While 3D tools like Maya, Blender, and Unreal Engine already provide this consistency, what's missing is the ability to **"gray-box" storyboard in 3D**, get the consistency and fine-grain control of the scene graph, and toss it into a massive context window model (like Gemini's 1-2 million token context).

You could use **multimodal prompting** to breathe life into the scene, essentially being in "director mode." You could use audio-in/audio-out models to direct your virtual characters—for example, "Walk up to the ramen bar and say this to the chef," or "I want the chef to lean in with this menacing look". You'd record the takes and camera angles you want, put it all into a timeline editing view, and still go back to make fine-grain edits, like tweaking the camera angle.

All the techniques we've discussed are the **primitives** or **Lego bricks** that could plug into this type of workflow. You take advantage of 3D models where it matters (physics, shader control, object ID control) and take advantage of the creativity of diffusion models to finish it. This would create a seamless "Flow State," eliminating the "tyranny of this ill-tailored tapestry of tools" by allowing you to jump between timeline and shot-level edits.

The problem is that everyone has unbundled visual creation and solved very specific problems in the space. We are starting to see representations of tools that bring this stuff together, like **Krea** or **LTX Studio**. LTX Studio actually has the closest user experience to this dream, though their models currently "suck". They're one update away from plugging in a high-end model, making the whole concept plausible.

The final piece is the **Large Language Models (LLMs)** themselves, which are getting much better. With models like Google's new Gemini models (including Flash thinking and a 2 million context window) and DeepSeek, you have multimodal language models that can be the **orchestration function**. You could have different agents with specific personas—a storyboarding artist, a visual effects agent—wielding these other tools via direct API control (like **UI Tars** from Bytedance, which can literally control Photoshop and Premiere for you).

LLMs will be a very important orchestration layer. Their context windows will expand, and their ability to understand multimodal context will improve. Since they are also capable of outputting multimodal data, one model will have full purview into the entirety of the shot list and script.

### Unbundling and Rebundling

To wrap things up, the problem space of audio-visual creation has been unbundled into all these little primitives. We are heading towards a future where these primitives will keep getting better, but they will also start coming back together. The net result is that you will be able to orchestrate creation at a **higher level of abstraction**. You'll essentially be the **conductor of the symphony**; you can still go in and play the instruments if you want, but you can also sit back and orchestrate at a higher level.