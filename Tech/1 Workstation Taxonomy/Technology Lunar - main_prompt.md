I need help taxonomizing my Mac apps. Im trying to make my macOS interactions synaptical. I’ve created a previous taxonomy that may serves as some basis for organization.

[macOStaxonomy.md]

With the explosion of AI tools and increasing wrappers and nonstop webapps, not to mention the mobile, and the forthcoming XR, formats i decided to go all the way off the far end to try and create a taxonomy for human-tool symbiosis holistically.

[ASAModel.md]

In some ways i was inspired by the OSI model which is also a coherent way to taxonomize as well.

The macOStaxonomy worked quite well sort/ordered-wise because it’s a scale that goes from most frequently used to set once and forget or background. So when I would need to surface/launch certain apps by approaching it as an index, there was an intuitive way of finding it.

Within the strata, I gave it a secondary organization, which i called ‘function’. It essentially partitions out the strata into arbitrary ‘roles’—compound words ending in -ar/-er/-or, etc, essentially trying to answer the question, what does ‘it’ (meaning the app) do. This taxonomy actually lends itself to be more hierarchical with more specific roles nested under the more general roles.

[Function.csv]

Indeed this was useful because I use Raycast, and the way I launch apps is through fuzzy search, so the roles were kept as heuristical and imperishable as possible, with minimal overlap. So I guess the heuristic was firstly, ‘what does it do?’ And ‘what kind does it do that for?’ (e.g. PhotoEditor would nest under Editor). 

Because there were so many apps, identifying a role would be the next best thing to remember, otherwise you would have to memorize each app’s name and function. Giving it a role, you can create aliases, hierarchicalize them into a directory structure, and rename them to their bespoke role, and then just fuzzy search the role. Probably the most heuristical.

Moreover another launcher app i appreciate was start from Setapp’s catalog, [start.png] you can customize how you set up your folders there too, so there is a point and click way to launch. I debated about whether to emulate taxonomical tree onto this. It does take time to set up, but it’s hierarchical, so it’s conducive to indexing. The issue was that I didn’t like having folders and apps on the same level. It was not an ideal way to browse and it was frankly redundant because I could more easily organize the aliases in Finder. On top of that, because I created the aliases, I could actually ‘tag’ them into the more overarching ‘strata’ taxonomy [finder.png]. A good heuristical backup, but I do want to capitalize on this launcher as point and click index somehow.


Obviously there’s the conventional categorization, which is what in currently grappling with now, that is, the formal way that Apple’s Mac App Store categorizes which is useful to the extent that it chunks apps in a nebulous region. However I think this is left to the developer to decide and can quickly become arbitrary. With the new launchpad [launchpad.png] it organizes it for you, being able to switch between tabs. I recently found an app [myapplications] that is almost an application browser. This is a great idea too. Previously with the older launchpad, you were able to stack the apps into custom folders [folderedcategories.png], and this provided yet another way to organize. How I used it was as an ‘apparatus’ folder, essentially a group of apps used often in tandem for a particular activity, for example having Pixelmator and Photomator together so you could click and launch without too many extra clicks. I supposed the ideal to come out of this would custom logical subcategories of Apple’s prescribed categories.

I’ve more recently been struggling with how to organize this and kept running into having to chunk by file/media formats (e.g. all related apps to pdfs and document creation, but then things would spillover into plaintext/markdown, then html) so there must be a coherent solution there [recentstruggle.png]

So let’s review the major perspectives
- stratified by frequency of usage/directness of control
- hierarchicalized by ‘functional’ role
- categorized by App Store convention (i guess that would be like domains)
    - Ideal further subcategories because Graphics & Design are too broad
- foldered by apparatus, which I think translated to ‘activity’
- recent struggle with format
Additional way I could think of would be
- any apps that involve a particular ‘thing’, it’s hard to understand what I’m trying to describe here but for example any apps that involves the keyboard, configurations, shortcuts, macros, automations, typewriter sounds etc. im not sure how to generalize this, but it’s in some ways akin to the conventional App Store categorization.
- Ecosystem, so like synergistic API’ed/linked/connectors/samedeveloper stuff.
- Stack in the regular developer sense, but of course with subcategories.
- Process or procedural categorizations—essentially apparatus/activity, but with a sequential element, maybe these windows are configured in are in a particular way too.
    - A parallel way is Apple’s ‘Spaces’/Mission Control feature where one can have several ‘Workspaces’ Desktops. I supposed that should be couple with the Apparatus/Activity categorization.

I’ll admit im a bit of a hoarder, and I don’t actually use all 400+apps. However i need to map everything so I can navigate the immensity. My brain needs hyper-compartmentalization and cartography first. With the democratization of Software Development due to increasing intelligence abundance and vibe coding, the value now comes from harnessing feature sets that have been so well developed and primitive extraction to develop bespoke tools. There are some all purpose tools that I want to decompose, (e.g a separate bespoke simple text editor for each text format: txt, yaml, md, etc.) while there are feature spread across apps i want to syncretize. Moreover, i have every intention on learning how to code agentically to supercharge this thesis, building optimized internal tools rather than retrofitting/patchwork-solutioning pre-built apps. Obviously there will be some trade-offs as why reinvent the wheel and that some of the incumbent apps are just too overpowered to emulate (Notion, Da Vinci resolve) that will take a team, maybe some day in the future.

Further things to consider, 
AI obviously. Which has now exploded in form: ambient, wrappers, gui-users/cli-users, copilots/human-in-the-loop, delegated ai (and regular) automation/workflows, agents and agent swarms, neo-AI platforms/labs (midjourney/eleven labs), traditional saas webapps/desktop apps (airtable/notion), saas platforms (salesforce), (no/low-code n8n), mobile apps, let’s not forget regular web browsers and the rise of agentic browsers and their extensions, not to mention the frontier labs, their suite of tools, and their developer platform/api. Again this level of complexity necessarily requires something like an ASA model to navigate.

I think there can be something in the middle.

Ultimately, the goal is to reduce the latency between intention and action, synapticality, somewhere further along will be less intrusive interfaces (performant XR, BCIs). Mobile did not completely upend the desktop workstation. Both are here to stay. The workstation benefits from RTS-levels of hand-eye interaction, now with much more performant language user interfaces. Things can be launched by fuzzy search, voice, keystroke. There are macro keyboards, time-based automations. There are trackpad gestures, etc. Mobile benefits obviously from GPS. It benefits from almost being like an oracle/hyperintelligent book format. Then there are the gradients of foldables, tablets, touch laptops, laptops, et al. These are the interim stepping stones on the way to full Jarvis from Iron Man. Maybe Jarvis is the triangulation of these things, eyewear+earbuds+wristwear+neckwear/pendant/pin+smartphone.

My hypothesis is that the new interfaces will not obsolete the other, but rather niche down, while simultaneously grow in general capabilities.

This is the scope I’m considering when I attempt to taxonomize these apps.
For now i believe the best solution is a master ‘Software’ database. Where all of the different categorizations are different views. Obviously they should be relational, aspirationally normalized (because I don’t know formal normalization) and the goal is to build it in something like Notion or Airtable, whichever is more suitable, or even both, maybe synchronized, maybe holding separate functions, maybe they get synchronized with Google Sheets as well for ultimate connectivity. And maybe it gets synchronized downward into SQL or redundancy or system level use. The idea is a unified organizing structure, infinitely configurable, and heuristically navigable. Maybe like the myapplications app. 