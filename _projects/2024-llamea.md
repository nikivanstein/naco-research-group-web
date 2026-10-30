---
title: LLaMEA
status: active
kind: line
featured: true

notitle: false

description: |
  Large Language Evolutionary Algorithm for the automatic design of algorithms.

people:
  - shahane
  - yin
  - huang
  - raponi
  - kononova
  - back
  - stein

topics: [genai, meta, bench]
links:
  github: https://github.com/XAI-liacs/LLaMEA
  blade: https://github.com/XAI-liacs/BLADE
  video: https://www.youtube.com/watch?v=LtFc8K5Uc4w

layout: project
image: "/img/projects/llamea.png"
largeimage: "/img/projects/llamea-wide.png"
last-updated: 2025-01-10
awards:
- medal: bronze
  title: Bronze Award
  event: IEEE COG 2025 Planet Wars competition
  url: https://simonlucas.github.io/planet-wars-rts/competitions/IEEE_CoG_2025_Results.html
- medal: silver
  title: Silver Award
  event: GECCO 2025 Humies competition
  url: https://gecco-2025.sigevo.org/Humies-Awards
- medal: winner
  title: Winner
  event: GECCO 2025 Any-Time Performance for Affine BBOB competition
  url: https://gecco-2025.sigevo.org/Competition-Awards#AA4AffineBBOB_Competition
- medal: winner
  title: Winner
  event: GECCO 2024 Any-Time Performance for Affine BBOB competition
  url: https://gecco-2024.sigevo.org/Competition-Awards.html#Anytime_Algorithms_for_Many-affine_BBOB_Functions
publications:
- title: 'LLaMEA: A Large Language Model Evolutionary Algorithm for Automatically Generating Metaheuristics'
  url: https://dl.acm.org/doi/abs/10.1109/TEVC.2024.3497793
  image: /img/llamea/llamea1.png
  group: Methodology
- title: In-the-loop hyper-parameter optimization for LLM-based automated design of heuristics
  url: https://dl.acm.org/doi/10.1145/3731567
  image: /img/llamea/llamea2-hpo.png
  group: Methodology
- title: Controlling the mutation in large language models for the efficient evolution of algorithms
  url: https://link.springer.com/chapter/10.1007/978-3-031-90065-5_25
  image: /img/llamea/llamea3-mutation.png
  group: Methodology
- title: 'LLaMEA-BO: A Large Language Model Evolutionary Algorithm for Automatically Generating Bayesian Optimization Algorithms'
  url: https://arxiv.org/abs/2505.21034
  image: /img/llamea/llamea4-bo.png
  group: Methodology
- title: 'Large Language Models and Evolutionary Computation: A Critical Review of Bidirectional Interaction, Automated Algorithm Design, and Co-adaptive Systems'
  url: https://www.sciencedirect.com/science/article/pii/S1574013726001589
  image: /img/llamea/llamea5-survey.png
  group: Methodology
- title: 'LLaMEA-SAGE: Guiding Automated Algorithm Design with Structural Feedback from Explainable AI'
  url: https://arxiv.org/abs/2601.21511
  image: /img/llamea/llamea-sage-final.png
  group: Methodology
- title: LLM-Driven Evolutionary Generation of Multi-Objective Bayesian Optimization Algorithms
  url: https://arxiv.org/abs/2607.08791
  image: /img/llamea/llamea-mobo-final.png
  group: Methodology
- title: 'Code evolution graphs: Understanding large language model driven design of algorithms'
  url: https://dl.acm.org/doi/10.1145/3712256.3726328
  image: /img/llamea/llamea6-ceg.png
  group: Benchmarking & analysis
- title: 'BLADE: Benchmark suite for LLM-driven Automated Design and Evolution of iterative optimisation heuristics'
  url: https://dl.acm.org/doi/10.1145/3712255.3734347
  image: /img/llamea/llamea9-blade.png
  group: Benchmarking & analysis
- title: Behaviour Space Analysis of LLM-driven Meta-heuristic Discovery
  url: https://arxiv.org/abs/2507.03605
  image: /img/llamea/llamea7-behaviour.png
  group: Benchmarking & analysis
- title: 'From Heuristic Selection to Automated Algorithm Design: LLMs Benefit from Strong Priors'
  url: https://arxiv.org/abs/2603.02792
  image: /img/llamea/llamea-priors-final.png
  group: Benchmarking & analysis
- title: Optimizing Photonic Structures with Large Language Model Driven Algorithm Discovery
  url: https://dl.acm.org/doi/10.1145/3712255.3734288
  image: /img/llamea/llamea8-optics.png
  group: Applications
- title: 'Landscape-aware Automated Algorithm Design: An Efficient Framework for Real-world Optimization'
  url: https://arxiv.org/abs/2602.04529
  image: /img/llamea/llamea-proxy.png
  group: Applications
- title: LLM Driven Design of Continuous Optimization Problems with Controllable High-level Properties
  url: https://arxiv.org/abs/2601.18846
  image: /img/llamea/llamea-problems.png
  group: Applications
- title: Evolving Executable Pipeline Programs for AutoML with Language Models
  url: https://arxiv.org/abs/2608.16416
  image: /img/llamea/llamea-lace-final.png
  group: Applications
---


LLaMEA, or Large Language Model Evolutionary Algorithm, is an innovative framework developed by the XAI research group at NACO with the lead of Niki van Stein. It leverages large language models (LLMs), such as GPT-4, to automate the generation and refinement of algorithms such as metaheuristic optimizers. By iteratively evolving algorithms based on performance metrics and runtime evaluations, LLaMEA streamlines the optimization process without requiring extensive prior algorithmic knowledge. 

Key features of LLaMEA include:

- **Automated Algorithm Generation**: Utilizes GPT models to create and enhance algorithms automatically.

- **Performance Evaluation**: Integrates with IOHexperimenter and other evaluators for real-time feedback, guiding the evolutionary process.

- **Customizable Evolution Strategies**: Allows configuration of strategies to effectively explore algorithmic design spaces.

- **Extensible and Modular Design**: Offers flexibility for users to incorporate other models and evaluation tools.

This framework is particularly beneficial for both research and practical applications in fields where optimization is crucial. For more details, including installation instructions and usage guidelines, please visit the project's [Github Repository](https://github.com/XAI-liacs/LLaMEA).
In addition, a accompanying benchmarking framework with additional real-world problems and baselines is available in the [BLADE Github Repository](https://github.com/XAI-liacs/BLADE).
