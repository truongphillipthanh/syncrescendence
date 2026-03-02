# Why are Transformers replacing CNNs?

**Channel**: Julia Turc
**Published**: 2025-12-01
**Duration**: 16m 57s
**URL**: https://www.youtube.com/watch?v=KnCRTP11p5U

## Description (no transcript available)

Why does a Transformer classify this cat as a cat… while a ResNet calls it a macaw?

In this video we break down one of the biggest shifts in computer vision: why Transformers replaced Convolutional Neural Networks (CNNs) — even though CNNs were designed for images and Transformers for language.

We’ll compare convolution vs self-attention, explore CNNs’ inductive biases (locality, translation invariance, hierarchical features), and see why self-attention is strictly more expressive than convolution. You’ll also learn how attention can exactly implement convolutional kernels using relative positional encodings.

📚 Resources:
- On the Relationship between Self-Attention and Convolutional Layers: https://arxiv.org/abs/1911.03584
- Backpropagation Applied to Handwritten Zipcode Recognition: http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf 
- AlexNet (the paper that popularized CNNs in deep learning): https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- The Transformer: https://arxiv.org/abs/1706.03762

00:00 Intro
01:30 The convolution operation
03:34 Convolutional Neural Networks (CNNs)
05:51 The inductive bias in CNNs
07:22 Self-attention
10:39 Self-attention can implement convolutions
14:17 Computational power & multi-modality
16:03 ChatGPT can be funny
