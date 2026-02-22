## The Evolving AI Workflow in Video and Visual Effects

What used to take hours in **Adobe After Effects** or even **Comfy UI** is now condensed to a single text prompt. Tools like **Google's Nano Banana**, **ByteDance's Cadream 4**, **Runway's ALF**, and many others are introducing a new paradigm of **instruction-based editing**. This is an entirely new way of creating. Instead of motion tracking, building geometry, estimating scene lighting, and all the other multi-step processes required for visual effects, you can now simply tell the AI model exactly what you want, and it executes the rest. It’s quite literally like standing over the shoulder of a talented VFX artist and having them immediately execute your vision.

These advancements are collapsing that explicit, multi-step pipeline into one implicit step, making professional-grade scene reconstruction and visual effects editing more accessible to content creators. Let's break down the latest tools, what they do, and why they're a significant development.

---

## Image Models

On the image side, you have **Google's Nano Banana**, which provides lightning-fast instruction-based edits using text and image references. **ByteDance** recently released **Cadream 4.0**, which is very similar to Nano Banana but offers much higher resolution and even better prompt adherence. A powerful, unreleased model you may not have heard of is **GPT Image 1 Highfidelity**, which is coming soon and is already available on **LM Marina**. From **Blackforce Labs**, there is **Flux Context**, which is also centered on instruction-based editing, and, of course, the foundational model that started it all, **GPT40 image**.

On the open-source front, you'll find **Quen imageedit**, which is an absolutely amazing model, along with its close cousin on the video side, **WAN and Vase**, which we'll discuss later.

---

## Video Models

The video side features an equally impressive lineup. **Runway's ALF** and **Luma's Modified Video** are the closest examples of instruction-based editing for video: you provide a video, describe the change you want, and the output is generated. There are also tools like **Higsfield** that simplify tasks such as inserting props into video. While tools like **PA** have been able to do this, Higsfield achieves a higher quality threshold for consumer creations.

In video, large language models like **Claude** are excellent for motion graphics. You can use Claude to generate HTML, CSS, and JavaScript to create animations, which you then screen record, giving you explicit control. For another great example of instruction-based editing, if you want to simply move the camera around, **Nvidia** has an amazing model called **Gen 3C**. It's essentially the Ken Burns effect on steroids: you take a still image and then you can animate the camera exactly how you want.

As mentioned earlier, on the open-source side, you have the cousin of WAN 2.0, called **Vase** or **All-in-One Video Creation and Editing**. If you're a Comfy UI user, you should definitely look into this tool. Its capabilities are straightforward: the ability to move, swap, reference, expand, and animate anything. Essentially, all the closed-source tools have these features to varying degrees, and this particular release combines them all.

A good way to think about this is the ability to easily re-render videos, including **content preservation**, **structure preservation**, and **subject preservation**. This is an optimization for video of techniques one might otherwise use multi-control network flows for, ensuring everything is highly **temporally and structurally coherent**.

---

## What Does This Mean?

This is extremely exciting because it essentially collapses the complexity of a multi-step **Photoshop**, **After Effects**, **Nuke**, and **Cinema 4D** workflow down to a handful of steps. If you are already familiar with these tools, you are at an even greater advantage. You know exactly how to prompt these systems to get great results because you know how to describe what you want, and you can blend the best of old and new techniques to get the job done.

A perfect example is a talented visual effects artist who used instruction-based primitives to reskin the iconic scene from *Superbad* where McLovin presents his fake ID for the first time. He swapped out the characters to look like the characters from *The Phantom Menace*, and it looks incredibly good. This result was achieved because the experienced artist combined generative tools like **Runway** with established tools like **Photoshop** and **Nuke** for compositing.

This also has amazing takeaways for the less savvy "prosumer" creator. The beauty of this technology is that images serve as your starting "seed point". For the less initiated and aspiring creator, you suddenly have a great way of creating all the **key frames** (the start and end frames) you need to throw into your video model of choice. If you made a generation and want to swap out the face for consistent characters, you can do that. You no longer need a task-specific model for **face replacement** or **background segmentation**; you can do it with a handful of general-purpose primitives.

You can use the image models discussed to create your start and end key frames, then feed them into your video model. You can then take the video output and throw it into some of the instruction-based video tools for further modification, essentially bypassing After Effects completely. The **Higsfield** examples of object insertion demonstrate how amazing this is; think of the effort it would take to motion track something in **Mocha** and then painstakingly adjust the lighting. This is all achievable in a single shot now.

The power is immense. We now have these generative "black box" models where you can provide a set of inputs and get really cool shots or elements that you can composite together. Honestly, this technology even replaces 3D animation and motion graphics to a certain extent. For instance, you can use Nano Banana to create a series of motion graphic key frames and then animate them with your video model of choice. Since you have the start and end key frames, you can simply keep repeating the process, doing extended-length generations to a theoretically infinite duration.

---

## Practical Uses Today

It is important to note that this is not quite ready for professional-grade productions yet. For a professional production, you typically require a **mezzanine codec**, **high-depth color**, a **log color curve**, and similar features. However, for **internet-scale production**—for creating content on **YouTube** or other social media platforms—these tools absolutely have a place in your workflow today.

I suspect the future will involve two bifurcated lanes of development. Some models will be common, but we will have highly accessible tools like **Higsfield** and **Runway** catering to a broad swath of users, including some professionals. On the other side, we will see the emergence of many more **hybrid workflows**.

As of the time of this video, **Adobe** has listened to feedback and is integrating **Nano Banana** directly into **Photoshop**. This is the first third-party model Adobe is integrating into their core product. You'll also see a bunch of cool new plugins on the After Effects side.

Years ago at Google, we created something called **Deep Light for ARCore**. We recorded many shiny spheres to collect training data so that a camera could take its limited field-of-view feed and estimate what the **light probe** for the whole scene might look like. Today, this is child's play with machine learning. In many ways, you can bypass the explicit lighting estimation altogether with large models that have simply seen enough content on the internet to implicitly perform this kind of estimation.

On the compositing end, with tools like **Nuke**, you'll see other amazing options. You can use tools like **depth estimation** to figure out how to place **volumetric lighting** in a scene, making your scene and structure respond very believably. Some of these results are fantastic, even when just using machine learning-based depth estimation as a primitive. Just as you have powerful nodes inside of **Comfy UI**, these capabilities will start to appear in tools like Nuke and After Effects. **Face swaps** will become a single instruction, **relighting a scene** a single image reference, and getting a **motion track**, **coarse-grain geometry**, and **feature tracking points** will all become one single step once we begin integrating models like **VGGT** directly inside these compositing tools.

One final prediction on the theme of industry-standard tools incorporating new models involves the research exemplified by **Blender Fusion**. This paper suggests abandoning the attempt to describe 3D edits through text and instead simply using **Blender**. The idea is straightforward: instead of trying to cram 3D understanding into a diffusion model, you use **depth estimation** and **segmentation** to take 2D images and project them into $2\frac{1}{2}\text{D}$ meshes, edit them in actual 3D software, and then use a fine-tuned diffusion model to make the results photorealistic. This is very much the approach Nvidia is taking with **Cosmos** and **Omniverse**.

This is very exciting. If you are a less sophisticated creator who just cares about the end result and wants to use natural language, images, and scribbles to describe what you want, you will have a great path forward. On the other hand, if you are a professional and want to turn videos into **editable scene graphs** where every single thing is controllable, that future is also rapidly approaching.

As someone who grew up learning visual effects, I'm personally very excited. There are times I find it easier to go into something like After Effects and Maya and do the work myself, and I want the best of both worlds. But there are other times when I'm making a quick meme for Twitter and don't want to go through all that effort. In those situations, I really appreciate the consumer/prosumer-centric workflows. Creators will be able to take advantage of both of these lines of development as they continue to flourish.

---

## Conclusion

Instruction-based video editing is clearly the start of something bigger. It is collapsing these complicated, explicit pipelines into text, image, and video prompts with very simple instructions. Conversely, thanks to the magic of machine learning, you can take a video and get back those explicit pipelines where everything is controllable. This is the magic of **multimodal in-and-out models**.

Ultimately, all of this is leading to a future where a kid sitting in a basement will have access to capabilities that James Cameron could only have dreamed of. Whether you want to use a camera to record real life with your friends or make it all inside your computer, you will be able to do that. With all the "mundane drudgery"—the multi-step workflows—being collapsed into a handful of Lego pieces you can use in concert, it truly comes down to the vision in your head and how you turn your mind inside out. I call this technology "**ILM in a box**"—a visual effects studio in this black box, or maybe even the offline **Holodeck**.