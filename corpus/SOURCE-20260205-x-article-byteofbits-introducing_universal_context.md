# Introducing Universal Context

(Description: Dark-themed article cover image featuring the title "Introducing Universal Context" on the left in large white sans-serif typography, with a geometric visualization on the right showing a wireframe sphere and descending matrix-like elements in white/gray ASCII-style characters against a dark background.)

## Overview

Three years ago, I wrote an article about the reasons that Salesforce was great — arguing that its flexible data model was its real moat, even if the complexity was painful. Since that article was written, a lot of things have changed in the software space: most notably, the rapid advancements of generative AI and large language models. As these models have matured, they have yielded agentic workflows that are capable of processing information from varied sources and taking complex actions over extended periods of time. These rapid changes have laid bare the foundational weaknesses that exist in legacy CRM architectures and many teams have struggled to strongly adopt agentic workflows into their organization as a result.

Agentic systems place new demands on the systems that they operate on and require a fundamentally new type of application and system architecture in order to operate effectively. As a result, we at @attio have been deeply focused on how we can evolve our platform to truly serve the needs of agents and deliver on our AI vision that we shared last year.

Today, we're excited to share a new foundational data model that sits at the heart of Attio and powers our newest product, Ask Attio. We call it **Universal Context**. Universal Context builds upon our foundational data model Particle, infusing it with semantic knowledge and full text search, providing agent-friendly ways to interface with the data and maintaining its ability to deliver massive scale and transactional consistency.

Universal Context is built for the realities of running agentic workloads in production and incorporates into its design the feedback and learnings of more than 7,000 teams that place Attio at the heart of their go-to-market strategy.

## New ways of thinking about data

By virtue of their design, agents necessarily introduce a fundamentally new set of demands on the infrastructure upon which they operate. For example, it's quite unlikely that two humans would attempt to action an identical task at exactly the same time when using an application like a CRM. Even some of the largest human teams of a few thousand people are unlikely to generate a significant number of conflicting modifications. In an agentic world, it's plausible that even a small business might be running tens of thousands of highly parallel agents at the same time, vastly increasing the risk of them conflicting.

Legacy platforms have attempted to introduce AI capabilities by adding additional tools to their stack (such as vector databases like Pinecone or Turbopuffer) which serve as replicas of the data held within them. These tools unlock semantic search, but they suffer from delayed replication from the source of truth and make it challenging for agents to unify structured queries with unstructured recall. In database terms, we refer to this as Consistency: the ability for a system to accurately represent state at a given point in time.

Universal Context is the first system in any CRM to provide External Consistency (the highest possible level of transactional consistency) that guarantees that the semantic embeddings used by agents to efficiently traverse across the data inside of Attio are always exactly in sync with the other data in the system.

And it's not just agents running inside of Attio that benefit from this consistency. Agents running in other platforms such as ChatGPT or Claude Code also benefit from these guarantees. Using our new MCP server, agents running in external platforms benefit from exactly the same consistency guarantees and advanced indexing capabilities as agents running directly inside of Attio.

This unlocks a new foundation for agentic workloads, as agents across different platforms can now operate collaboratively in real time on a single source of truth. For example, say an agent running in Claude Code decided to research a contact and update the record with a note about their interests. In legacy systems like HubSpot or Salesforce, that note might not be visible to other agents for some time as indexing pipelines and other workloads happen asynchronously from the initial write. With Attio's Universal Context, another agent running at exactly the same time in ChatGPT would now see that note when looking for records with a particular interest.

## Schema as context

To advance agents within a GTM organization, there needs to be an on-ramp into the organization's data that allows agents to understand the shape of data and how to access it. With many MCP servers today, the challenge of accessing data has been solved but this rarely comes alongside an understanding of how the data is shaped. These early attempts at indexing data that lives in different silos were challenging for agents to reason about consistently. Indexing capabilities and syntax varies between tools, and agents often struggled to accurately ground their decisions in this disparate data.

For human users, challenges like these have typically been solved by data warehouses, but when working with agents these systems suffer from the ETL pipelines that feed them. Warehouses provide a delayed and inconsistent replica of their source data making them of limited value for realtime agentic workloads.

Agentic users require a unified and consistent model for accessing the data that they rely upon to make decisions and measure their results. This data problem defines an important requirement for any AI-native system in the GTM space: can you provide an agent with unified, accurate, and consistent information with which to ground its decisions?

Particle's flexible graph-relational format provides the agents consuming Universal Context with a single, cohesive language to explore and index all of an organization's go-to-market Data. By integrating with all of the different sources of GTM across an application, Universal Context builds a complete understanding of an organization's go-to-market landscape. This includes everything from simple structured data like name or email address, through dynamically researched enriched data like job title or industry, all the way to unstructured proprietary data like emails, notes, and call recordings.

All of this data combines to create a safe, well-understood playground for agents to explore, build, experiment, and improve upon.

## The promise of generative application logic

One of Salesforce's less well-known superpowers was Apex. Introduced in 2007, Apex is a proprietary, strongly-typed programming language that allows developers to write code that can extend the product's capabilities.

Apex was quietly revolutionary. It meant that if you were willing to spend enough time and money on development, you would be able to configure the platform to your needs. This code-based extensibility is one of the key reasons that Salesforce has been so persistent in the market. When your business processes are encoded in thousands of lines of custom code that only run on a single platform, migrations become far more complex.

In 2026, coding agents are fundamentally changing how software gets built. The question is no longer one of resource and time as autonomous coding agents rapidly move us towards a world of generative application logic. This shift makes code-based extensibility more valuable than ever before: without code execution, agents are deeply constrained by what they can achieve and how they can surface results to the end user.

Brilliant though it was when released, Apex is a complex and proprietary offshoot of Java 5 from 2007. This creates problems when working with the latest generation of coding agents like Claude Code and Cursor. Modern LLMs are not well placed to work with these environments: they require a new kind of platform to build upon. (Salesforce understands this, which is why they've invested so heavily in custom models like xGen-Code and CodeGen specifically for Apex, but they're playing against the ecosystem, not with it.)

Last year we released Attio's App SDK, a Typescript based code sandbox that allows Attio customers to extend their instance using a fully managed serverless environment and React. Our core design goal when designing the App SDK was to ensure that it served as a "compilation target" for AI. We designed the environment and the library from the ground up to be understandable and forgiving to LLMs working in our environment.

By leveraging the extensive Typescript ecosystem, App SDK allows agents like Claude Code to easily build upon the extensive ecosystem of packages available on npm. Agents can work with local tools, allowing a fully autonomous build, test, and deploy pipeline with standardized tools. Contrast this with the Apex deployment model—with a proprietary IDE and Salesforce-specific tooling—and it becomes clear that Apex is in a challenging spot.

We believe that code generation isn't just a feature of the next generation of GTM tooling—it's the whole foundation. The assumption that configuration and code were in contention is breaking down as coding agents allow anyone to easily generate, test, and improve totally custom code. In fact, as agents like Ask Attio become more powerful, it's likely that end users won't even know that code was involved: they'll simply ask for a capability and receive the application they need to work effectively.

## The AI future of CRM

Today's release of Universal Context, alongside Ask Attio and the MCP tools that build upon it, is an important milestone in our mission to deliver cutting edge agentic functionality to our customers. We have an exciting roadmap ahead which will continue to expand on the functionality of our existing agents, as well as adding new agents and surfaces for our customers to benefit from the extraordinary powers of AI.

---

**Engagement Metrics:** 5 replies, 21 reposts, 307 likes, 606 bookmarks, 44K views  
**Posted:** 8:26 AM · Feb 5, 2026