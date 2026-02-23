## The Automation Trend in Visual Creation

The presenter reflects on the evolution of visual effects, drawing a parallel between past innovations like Disney's multiplane cameras and modern techniques like Google's multiplane images (MPIs), noting that the core idea of spatial representation repeats across eras. The history of animation also mirrors this, moving from manual **rotoscoping** to AI-assisted video-to-video rotoscoping, indicating an overall trend toward **automation and ease of use**.

* Complex workflows, such as those in After Effects, are being reduced to a few clicks in tools like Pabs, a process that **democratizes** sophisticated visual creation.
* The speaker cites a personal example: a short-form video that previously took a week to produce could be completed in a single day using generative AI tools, with After Effects and Premiere used for final polish.
* This efficiency allows creators to take on more ambitious projects and deploy visual creation in scenarios that would have been previously impractical, enabling **Indies to rival Studios**, while Studios are poised to set new standards altogether.

---

## Spatial Intelligence: AI 3D Tools

**Spatial intelligence** is defined as the ability to understand and interpret spatial data, such as maps and 3D models, essentially teaching machines to understand the 3D world.

### Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting

Traditional **photogrammetry**—the art and science of measuring the real world from images—predates computers, but machine learning has recently given a massive boost to **reality capture**.

* **NeRFs** (Neural Radiance Fields) represent a new approach where an AI uses about 100 2D photos to create a 3D representation, almost "spitballing Ray tracing," that allows for stepping inside the scene.
    * A NeRF is fundamentally an implicit representation: a neural network (a **multi-layer perceptron** or MLP) where every voxel is queried for spatio-directional RGB and density values, which are then used in basic **volume rendering** to create photorealistic renditions.
    * NeRFs can handle complex effects like **reflections, refractions, transparency, translucency**, and thin structures, which were difficult for photogrammetry.
    * Initial NeRFs were slow, rendering at one frame per second.
* **3D Gaussian Splatting (3DGS)** introduced an explicit representation, essentially NeRFs without the neural rendering bit, using a multitude of ellipsoidal splats called Gaussians.
    * 3DGS significantly boosted performance, achieving up to **400 frames per second** on some captures, making reality capture far more practical.
    * It models view dependency using **spherical harmonics**, an established physics concept.
    * 3DGS files output a Stanford PLY file, which is easy to import into traditional tools, and plugins are available for Unity, Unreal Engine, and After Effects.

### Commercial and Local Tools

A range of tools is now available to access this technology:

* **Cloud-based Commercial Solutions:** Luma AI and Polycam.
* **Local Solutions:** Post Shot, Nerfstudio, and **Scane** (an iPhone app that trains and splats in real-time on-device, leveraging Apple chips).
* **Apple's Room Capture API** is also commercially ready, providing a simplified, semantically meaningful 3D model of a room (a 3D floor map) for use in surveying, projection mapping, or light occlusions.

### Professional Applications and Future of Capture

Static radiance fields are already in use in **music videos and commercials**, often leaning into the "dream-like aesthetic" created by the graceful degradation of radiance field artifacts. Professional capture is advancing:

* **LiDAR Surveying** combined with simultaneous localization and mapping (SLAM) has progressed considerably.
* Systems like the **Livox L2** produce both a LiDAR colored Point Cloud and a 3D Gaussian Splat, enabling sophisticated captures in minutes.
* **Radiance Fields** are breathing new life into dynamic spatial capture systems, addressing previous issues with videogrammetry, such as atlasing and UV shifts.

### Geospatial AI: Querying Reality

Beyond modeling, spatial intelligence is being used for localization and scene context:

* **Visual Positioning System (VPS):** An ML-based technique that uses a machine-readable 3D model of the world to match a photo, providing high-accuracy sub-meter positional and rotational accuracy, which is used in Google Maps and AR.
* **Google 3D Tiles:** This open format, based on Google Earth data, allows developers to bring coarse-grain geometry, terrain, and lighting information into tools like Unreal and Houdini.
* Combining VPS with 3D Tiles allows for creating surveying apps where 3D annotations placed remotely show up accurately in the real world. A high-resolution scan (like a NeRF) can be snapped against the 3D Tiles model for broader context, a feature utilized by the tool **Cyclops**.

---

## Visual Intelligence: AI in VFX

**Visual intelligence** is defined as teaching machines to perceive and understand the world and the content within imagery, a field classically known as **Computer Vision**.

* **Pose Estimation:** Models for tasks like estimating human pose are now being optimized for professional use, reversing the trend of models primarily developed for consumer apps like Snapchat.
    * **Wonder Dynamics** uses monocular pose estimation, trained on cinema camera data to provide better registration and precision than off-the-shelf models. They recently updated to provide a **3D solve** of the environment in world and scene space coordinates.
    * **Move AI** offers multi-view pose estimation, capable of using input from various cameras (iPhones, GoPros, Fleer cameras) to deliver real-time mo-cap data with a single GPU.

* **Relighting and Segmentation:**
    * **Beeper (South Korea):** Given monocular video, their model can **Delight** the subject and output a PBR (Physically Based Rendering) shader, including Albedo, Specular, Normal, and Roughness passes. They achieved this by figuring out how to scale outside of traditional light stage datasets.
    * **Sky Glass (iPhone App):** Allows users to try relighting on their phone using the Beeper API, streamed into an Unreal Engine environment.
    * **Segment Anything Model (SAM):** A foundational model that generalizes pixel segmentation to anything without needing specific label data. It is commercially friendly (Apache 2.0 license).
    * **Track Anything:** A video object tracking and segmentation tool built on Meta's SAM, considered superior to tools like Roto Brush.
    * **Depth Anything:** A foundational model (Apache 2.0) for monocular depth estimation, trained on vast amounts of unlabeled data, generalizing to all sorts of scenes.

---

## Generative AI and the Future of Creative Production

Generative AI is framed as a **content-to-content** system that can transform text, image, video, and 3D data into any permutation of the same.

* **Sora and Hybrid Approaches:** The release of Sora suggested that throwing more data at the problem could bypass the need for explicit control via a 3D scene graph. However, the current reality of generation time (e.g., one hour for a one-minute clip)  suggests that the most compelling work will likely be a **hybrid approach**, mixing classical 3D and VFX tools with generative methods.
* **Multimodal AI and Workflow Automation:** Large Language Models (LLMs) and multimodal AI are crucial for surrounding tasks.
    * LLMs, such as Gemini, with massive context windows (up to a million tokens) , can reason over various data types (video, audio, text).
    * This allows for the ingestion of all production documents (shot notes, scripts, storyboards, client feedback) to synthesize insights for artists and supervisors.
    * Creators can screen-record their software (like After Effects) and prompt the model to write a script (like an After Effects or Blender script) to replicate the action, automating workflows.
    * These models have **zero switching cost** (no technological lock-in), allowing studios to swap between different models (e.g., Gemini for prototyping, Llama 3 for on-prem fine-tuning) easily.
* **Future Authoring Abstraction:** The ultimate future may involve authoring content at a higher level of abstraction, similar to a 3D scene graph, where creators control what matters and outsource the rest, which would significantly streamline tasks like localizing advertisements for different regions. Jensen Huang, CEO of Nvidia, predicts that every pixel will be generated in 5 to 10 years.

---

## Conclusion

The speaker encourages investment in all forms of AI:

* **Spatial and Visual AI** are **commercial ready** now, and creators should be building with them.
* **Generative AI**, especially LLMs, is critical for all the processes that surround visual creation and should be explored immediately.
* The lack of technological lock-in in the generative space offers a unique opportunity for tool creation and integration.