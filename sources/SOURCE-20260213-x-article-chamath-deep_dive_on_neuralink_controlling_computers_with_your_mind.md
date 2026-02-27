---
url: https://x.com/chamath/status/2022396027555418456
author: "Chamath Palihapitiya (@chamath)"
captured_date: 2026-02-13
id: SOURCE-20260213-003
original_filename: "20260213-x_article-deep_dive_on_neuralink_controlling_computers_with_your_mind-@chamath.md"
status: triaged
platform: x
format: article
creator: chamath
signal_tier: strategic
topics:
  - extended-thinking
  - cli-tools
  - extract-pattern
teleology: extract
notebooklm_category: philosophy-paradigm
aliases:
  - "Deep Dive on Neuralink Controlling Computers With Your Mind"
synopsis: "Deep Dive on Neuralink: Controlling Computers With Your Mind The Problem: The Brain-Computer Bottleneck The human brain receives data at ~1,000,000,000 bits per second. But it can act on and express only ~10 bits per second. This includes tasks like moving, thinking, and speaking. This is like being connected to fiber-optic internet, but only being able to respond through a 1990s dial-up modem."
key_insights:
  - "Deep Dive on Neuralink: Controlling Computers With Your Mind The Problem: The Brain-Computer Bottleneck The human brain receives data at ~1,000,000,000 bits per second."
  - "But it can act on and express only ~10 bits per second."
  - "This includes tasks like moving, thinking, and speaking."
---
# Deep Dive on Neuralink: Controlling Computers With Your Mind

## The Problem: The Brain-Computer Bottleneck

The human brain receives data at ~1,000,000,000 bits per second.

But it can act on and express only ~10 bits per second. This includes tasks like moving, thinking, and speaking. This is like being connected to fiber-optic internet, but only being able to respond through a 1990s dial-up modem.

An upgrade is needed, especially in a world racing towards increasingly capable AI.

## Neuralink's Mission

In 2016, Elon Musk founded Neuralink to develop a scalable Brain-Computer Interface (BCI): a system that establishes a direct communication pathway between the brain's electrical activity and an external device, bypassing traditional pathways (i.e., nerves and muscles).

@neuralink progressed from wired implants in rodents to a wireless implant in the first human in only 5 years.

(Description: Timeline graphic titled "Timeline of Neuralink Achievements (2019-2024)" showing five major milestones with photographs. 2019: "Wired implant with >3K channels in rats." 2020: "Live demo with a wireless implant in pigs." 2021: "Pager, a nine year old Macaque, plays mind pong." 2022: "Monkeys use BCI for various computer tasks." 2024: "First human implant - Noland Arbaugh.")

## Public Perception: From Skepticism to Acceptance

Brain chips, however, were unpopular with the general public. In 2021, a Pew Research Center study found that 78% would not want one for improved information processing, 56% said widespread use would be bad for society, and only 13% considered it a good idea.

(Description: Bar chart titled "U.S. Adults On Computer Chip Brain Implants" showing two categories. Purple bar for "Would NOT want" at 78%, tan bar for "Would want" at 20%. Source: Pew Research. Note states "Respondents who did not give an answer are not shown.")

However, therapeutic use was widely accepted. 77% favor brain chips for paralysis treatment, and 64% favor them for age-related mental decline.

(Description: Stacked bar chart titled "Americans' Openness to Implants Based on Effect and Surgery" with two columns. Left column "Allow increased movement for paralyzed people" shows: 8% Oppose, 14% Oppose, 77% Favor (purple). Right column "Treat age-related mental decline" shows: 21% gray bar, 13% yellow bar, 64% Favor (purple). Source: Pew Research. Note: "Respondents who did not give an answer are not shown.")

## The First Human Implant

And that's where Neuralink began.

In January 2024, Neuralink conducted the first human implantation of the N1 chip in Noland Arbaugh (@ModdedQuad).

Since then, Noland Arbaugh has used the N1 daily to regain digital independence, navigating the internet, learning online, communicating publicly, and controlling computers for work and play, including games such as chess and Civilization VI.

(Description: Photograph showing Noland Arbaugh, a young man wearing a blue baseball cap, with a Neuralink implant visible behind his ear with a visible connector. He sits at a laptop. Speech bubbles in the image read: "Noland is thinking about where he moves the cursor, click, drag and more" (left) and "Cursor behaves on the Neuralink enabled device as he intends it to" (right). He appears to be controlling a game on the laptop screen.)

## So How Does Neuralink Actually Work?

We go into further details in the Deep Dive below, but at a high level, the process of turning a thought into a digital action follows a five-step path:

### 1. Listening for Neural Signals

The process begins with 1,024 electrodes distributed across 64 flexible threads. These threads are implanted into the motor cortex, the brain region responsible for movement. Each electrode acts as a microscopic microphone, detecting electrical ripples from nearby neurons.

### 2. Amplifying and Digitizing the Signal

Raw brain signals are exceptionally faint, at roughly 15,000 times weaker than a standard AA battery. On-chip amplifiers within the N1 implant boost these signals to measurable levels while filters remove background noise. The chip then transforms the signal waves into a long stream of data for the computer to read.

### 3. Identifying Spikes

The N1 needs to identify meaningful signals in the data stream, known as spikes. It analyzes the unique shape of each waveform to attribute the activity to its specific source neuron.

### 4. Packaging and Transmitting Data

Transmitting raw neural data would be too slow and power-intensive. Instead, the N1 chip organizes the detected spikes into small digital packets. This compressed data is then sent wirelessly via Bluetooth to an external device, such as a smartphone or computer.

### 5. Decoding Intent into Action

Before a user can control a computer, the system undergoes a ~20-minute calibration. During this time, the user imagines specific movements (like moving a hand or squeezing) while the software learns which neural firing patterns correspond to those intents. Once trained, machine learning algorithms decode these patterns in real-time, moving a cursor on a screen dozens of times per second.

(Description: Technical diagram titled "Overview of the Decoding Process" showing the N1 implant on the left (a purple circular device with directional indicator), connected to a "Computer with Neuralink App" on the right. The diagram shows neural signal flow from "Raw Neural Signal" through channels, with boxes labeled "Recorded spike data" and "Data collected during calibration on the 'Decoder'". The center shows numbered channels (0-1000+) with signal patterns. Purple boxes on the right labeled "Cursor X" and "Cursor Y" represent decoded outputs. A tan box at the bottom notes "ML algorithms recognize firing patterns and map them to the calibration data to decode the user's coordinates on the screen." Source: Medium, PubMed.)

## Current Clinical Status and Future Goals

As of late January 2026, Neuralink has enrolled 21 participants in its worldwide clinical trials. These individuals use the implant for an average of 50 hours per week, controlling computers, playing games, browsing, and handling daily tasks entirely through thought.

21 participants represent a meaningful advance over the early animal trials. Yet Neuralink's stated target is far larger: 10,000 implants per year by 2030, at an estimated total cost of $40,000 to $50,000 per patient.

Reaching that volume will require consistent long-term thread performance, further automation of the R1 surgical robot, streamlined regulatory pathways, and acceptance within medical systems. The challenges ahead are still substantial.

## Beyond Motor Control: Future Capabilities

Neuralink also intends to expand beyond motor control. Future capabilities include restoring tactile sensation, enabling natural speech for individuals who have lost it, and restoring vision through a planned product, Blindsight, that directly stimulates the visual cortex with camera input.

## The Significance and Implications

What Neuralink has already proven makes this one of the most fascinating areas in technology right now. That is why we decided to research it in depth and create this Deep Dive.

Neuralink is pursuing one of the most difficult frontiers in technology.

The implications include reversing neurological disabilities, modulating circuits involved in depression or anxiety, enhancing memory and cognitive speed, and ensuring humans remain competitive as AI capabilities advance rapidly.

---

## Full Deep Dive

I invite you to learn with me here: https://chamath.substack.com/p/neuralink

Let me know what you think in our Substack group chat.

## Table of Contents

01 Intro: The Argument for Brain Chips — 04
02 How The Brain Thinks: Thinking Is Similar To Doing — 15
03 The Neuroscience History of Brain Signals — 27
04 N1 Link: The Brain Chip To Control Computers — 35
05 R1 Robot: The Neurosurgeon Robot — 53
06 Neuralink Feats: The First 21 Cyborgs — 61
07 Neuralink's Roadmap & the Future of BCI — 69
08 Conclusion — 86