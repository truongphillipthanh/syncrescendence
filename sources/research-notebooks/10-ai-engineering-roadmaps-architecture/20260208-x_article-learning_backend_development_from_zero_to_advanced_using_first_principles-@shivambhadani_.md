---
url: https://x.com/shivambhadani_/status/2020504631697391736
author: Shivam Bhadani (@shivambhadani_)
captured_date: 2026-02-08
---

# Learning Backend Development from Zero to Advanced Using First Principles

(Description: Title card with gradient purple background displaying "Learning Backend Development From First Principles" in large white text)

## Introduction

You could ask ChatGPT this question and get an answer, but learning from someone who has actually walked the path can be more valuable. In this article, I share how I learned backend development and how beginners should approach it. I won't be discussing any specific languages, frameworks, or libraries. Instead, I'll focus entirely on the core fundamentals that apply regardless of the tools you choose.

## Step 1: Learn a Programming Language and Build a TODO App

This will sound very basic, but if someone is learning computer science for the first time, this is a great way to start. When I first started learning CS in college, I also started with the TODO app. For this, learn any programming language, database, and framework to build this. If we are starting first time, we should code this manually without using AI.

## Step 2: Learn Data Structures and Algorithms

This way, we can sharpen our minds to solve complex problems. If our backend application has a lot of complex business logic, then we won't be scared to translate our thoughts into code if we have good problem-solving skills. I had learnt DSA by solving problems on codeforces, atcoder and LeetCode. Giving competitive programming contests and upsolving will help here. To become good at Codeforces, you can follow [this link](https://www.shivambhadani.com/student-guide/roadmap-from-newbie-to-expert-in-codeforces).

## Step 3: Build More and More Projects

Till now, we have learnt the basics of backend development, and we have sharpened our problem-solving skills, now its time to build projects. We can build clones of an e-commerce app, a note-taking app, a movie recommendation app using some external APIs, etc. Code these projects manually without using AI. Having completed up to Step 3, we can now start applying for jobs and internships. At this stage, we have acquired the basic skills needed to be employable.

After step 3, we will go into depth on each piece of backend engineering one by one.

## Step 4: Basics of Computer Networks

Understand OSI Model of the computer network, you will be amazed to see how each layer is designed by decoupling from one another. Understand the task of each layer and what they do. As a backend developer, the most important layers would be layers 5, 6, and 7. If we have done till step 3, then we are good at the application layer. Now, it's time to go deeper.

Learn about TCP and UDP, how the TCP 3-way handshake work and how to code an application server using TCP. You can follow [this blog](https://medium.com/@shivambhadani_/understanding-tcp-and-building-our-own-tcp-server-in-c-language-8de9d9de78ef) to learn it.

## Step 5: Learn Different Types of Communication Protocols in the Application Layer

Since we learnt about TCP and UDP, now it's time to learn about higher-level protocols that are built on top of them. The most important ones are:

- HTTP/1.1
- HTTP/2
- HTTP/3
- GRPC
- Websockets
- MQTT

There can be many more protocols in the market, but I have listed the ones that I have used till now. Each protocol has its own advantages and tradeoffs, and as a backend dev, it's our job to choose between them based on the nature of the application we are building. I don't want to make this article long, so I won't be going details of the above-mentioned protocols. I will post a separate thread/article on them soon.

## Step 6: Learn Different Types of Message Formats

When we send exchange data between the server and the client, we first need to parse the data from the unreadable TCP packets to application format. This is done differently via different protocols like HTTP uses content-length and application-type in the Headers. Similarly, GRPC does it via protobufs. Sending each byte and serializing/deserializing it in the application layer has a cost. Some of the message formats that are important to learn are:

- XML
- JSON
- Protocol Buffers
- YAML

We can go into depth on each one and try to build our own parser, also. Since we are comfortable with DSA, coding this won't be that hard.

## Step 7: Databases in Depth

This is the most critical piece of our application. Most of the time at scale, databases are the first thing that becomes the bottleneck. Learn to write optimized SQL, learn about ACID Properties, Indexes, Normalization, and how to design a scalable schema both in Relational as well as Document Databases. Pick one relational database like Postgres, MySQL, Oracle, and one document database like MongoDB, CouchDB, etc., and go into depth on them. See why there are so many databases in the market, and what specific problem they solve. Some DBs scale easily, some DBs provide very strong consistency, some DBs give very fast Reads, some DBs give very fast Writes. Different DBs are good at something and have some tradeoffs. Choosing between those depends on the nature of the application.

If we go into depth on each database, under the hood, they are implemented differently using different data structures and design decisions. I can't put everything about databases in one article because it's a very vast topic and a different branch of engineering itself. We will learn about different databases in our blogs. I am going to start with Postgres soon in my medium and will go depth of each DB one by one.

## Step 8: Caching

There are different levels of caching. It happens everywhere. Browsers do caching, mobile phones also do caching. But as a backend dev, our area should be in the application and Database caching. Learn different Cache Invalidation techniques such as TTL, Write-Through Cache, Write-Behind, and Explicit Invalidation. Learn different Cache Patterns such as Cache-Aside, Read-Through Cache, Write-Around Cache. Learn different Cache Eviction models such as LRU, LFU, FIFO, Random.

Deciding which cache eviction, which cache invalidation technique, etc, we need depends upon the nature of the application we are building. If you want to learn how Redis is so fast and why it is used in caching, then you can read [this thread](https://x.com/shivambhadani_/status/2007722684743069957).

## Step 9: Message Queues, Message Streams & Event-Driven Architecture

Learn about asynchronous programming. If the client requests something that takes a longer time to compute/execute (e.g., generating PDF, video transcoding, etc), then we can't let the client wait for the response. In these scenarios, we use message brokers. There are two categories of message brokers:

- Message Queues (e.g., AWS SQS, RabbitMQ)
- Message Streams (e.g., AWS Kinesis, Apache Kafka)

Learn how and when to use them. There are several things needed to keep in mind while writing Workers (or Consumers) like how to process each message only once, how to maintain idempotency. What happens when our message lags in the kafka? How to process them. If we couldn't process the message, then we need to put that message in the dead-letter queue. These things can't be just learnt from theory. When you face these problems in real life, you can understand them.

## Step 10: Testing & Quality Assurance

If we don't want our application to become buggy when it grows or at scale, then we must write Tests. There are three types of tests that we should learn:

- Unit Testing
- Integration Testing
- API Testing

One rule that I like to follow is: Write the test first before the code.

## Step 11: Proxies

Proxies are something that sits between the client and server. It is of two types: Forward and Reverse Proxy. Proxies are something that handles most of the adhoc task of our application which are not related to core business logic of the application like:

- Doing SSL termination
- Forwarding based on some rules when using microservices like if request URL contains `/product` then go to product microservice, if it has `/search` then go to the search microservice, and so on.
- Load Balancing

Just go through the internals of Nginx, Envoy, HAProxy, etc. How the engineered their system. It will be a great learning experience.

## Step 12: Security

This is the most important thing. The world is not kind. Anything left unprotected will inevitably be attacked. So, we need to take care of the security of our backend application. Learn about common cyber attacks such as SQL injection, DDOS, XSS, CSRF, etc., then learn how to protect the application from them. You can read [this article](https://x.com/shivambhadani_/status/2012775780942860515) to learn about backend security.

## End of the Article

In this article, we haven't covered topics like scaling, cloud computing, observability, logging, and other aspects related to reliability. I believe these areas are more aligned with SRE or DevOps practices rather than core backend development, so I prefer not to mix them here. We'll address them in a separate article. If you want to learn how to scale the backend, then read [this blog](https://medium.com/@shivambhadani_/system-design-for-beginners-everything-you-need-in-one-article-c74eb702540b#9c03).

Every field of computer science, be it backend, machine learning, or DevOps, etc., demands continuous learning. I'm far from an expert in all the areas I mentioned in the article and consider myself still very much a learner.

---

**Engagement Metrics (as of capture date):**
- Replies: 36
- Reposts: 239
- Likes: 1.9K
- Bookmarks: 4.1K
- Views: 215.4K
- Timestamp: 6:26 AM · Feb 8, 2026