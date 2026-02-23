---
title: "Large Language Models for Metaheuristic Design"
status: active
type: tutorial

notitle: false

description: |
  Large Language Models for Metaheuristic Design @GECCO 2026

people:
  - stein
  - baeck

eventdate: 2026-07-14
layout: event
image: /img/events/llmheuristics-gecco.png
header:
    og_image: events/llmheuristics-gecco.png
last-updated: 2026-01-25
---

Evolutionary Computation (EC) and the recent advances in large language models (LLMs) are two powerful fields within the computational intelligence (CI) universe that hold significant promise for complex optimization problems. The stable growth of EC and its growing integration of machine learning (ML) principles, along with diverse algorithms and hybrid approaches, pose challenges for researchers. They must identify effective strategies and design targeted solutions for both combinatorial and continuous optimization in specific use cases. LLMs are transforming the way we create and automate AI techniques/algorithms discoveries. This shift moves us beyond just hyperparameter tuning and automated selection into the realms of fully automated algorithm design (AAD), architecture and end-to-end pipelines discovery, effectively closing the loop between ideation and evaluation.

The tutorial will explore several ways in which these two fields are closely connected.

This tutorial will firstly introduce the general potential of LLMs to transform automated metaheuristic design and benchmarking, focusing on how they can support researchers in selecting suitable algorithms, explaining methods, suggesting novel hybrid techniques, generating codes, and iteratively improving the initially designed solutions or algorithm templates.

Another approach is represented by evolutionary search heuristics powered by LLMs, where the model repeatedly generates and refines candidate algorithms, operators, or configurations, while selected evolutionary principles - populations, selection, crossover, and mutation- guide their improvement. Some of the recent frameworks may fully/partially illustrate this setup: an LLM proposes a population of candidate heuristics (often in code), which are evaluated (on benchmark tasks), and high-performing candidates are recombined and mutated in subsequent rounds. A shared knowledge base of evaluated solutions and reusable components accumulates over time, while feedback signals steer both the evolutionary search and the orchestration of modules around the LLM. This tutorial provides an overview of the rapidly evolving landscape, including frameworks like EASE, LLaMEA, LHNS, MCTS-AHD, PartEVO, AlphaEvolve, and FunSearch. We specifically contrast two of our own-developed frameworks: the architecture of EASE (Effortless Algorithmic Solution Evolution) with the evolutionary-focused approach of LLaMEA (Large Language Model Evolutionary Algorithm). We will explore the EASE as a practical, fully modular framework for iterative, closed-loop generation and evaluation. Beyond just algorithm code, EASE can also iteratively generate text and graphics. Following that, the tutorial will shift its focus to the LLaMEA framework and its connection with benchmarking ecosystem IOH, recent advancements, including the hyperparameter optimization toolkit LLaMEA-HPO & LLaMEA-BO, and a unique benchmarking suite for automated algorithms discovery – BLADE.

Participants in this tutorial will have a unique opportunity to listen to two seemingly competing teams and learn about two frameworks in one place, and find out how to collaborate effectively in this rapidly developing area, and complement each other with partial knowledge, leading to greater efficiency and opportunities for global deployment of these frameworks for AAD.

We will also highlight key guardrails, including testing, analysis, and time/resource caps, as well as best practices in evaluation and benchmarking. Attendees will emerge with practical criteria for choosing between LLaMEA and EASE, methods for responsible evaluation, and steps for incorporating LLM-driven discovery into AI research.

Building upon these frameworks, we will further discuss the orchestration problem - how ensembles of small and large language models can cooperatively drive algorithmic discovery.
We will also demonstrate how human-in-the-loop co-discovery mechanisms can inject domain expertise and interpretability into this process, ensuring that automated exploration remains guided, explainable, and auditable. Together, these methods establish a practical path toward LLM-driven discovery that both generate and justify new algorithms.

Key aspects will include the role of LLMs in creating optimization algorithms specifically tuned for unique challenges and generating problem-tailored metaheuristics for global optimization. Attendees will gain a comprehensive view of the opportunities and challenges in leveraging LLMs within metaheuristics design, equipping them with insights to push the boundaries of optimization in research and industry.

