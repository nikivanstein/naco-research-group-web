---
title: "LLMs for Metaheuristic Design tutorial at GECCO 2027"
status: active
type: tutorial
pending: true

notitle: false

description: |
  Large Language Models for Metaheuristic Design: from evolutionary program search to agentic algorithm discovery. Tutorial at GECCO 2027

people:
  - stein
  - back

layout: event
eventdate: 2027-07-12
enddate: 2027-07-16
location: "Kraków, Poland"
venue: "GECCO 2027"
image: /img/events/llmmeta-gecco2027.png
largeimage: /img/events/llmmeta-gecco2027-wide.png
header:
    og_image: events/llmmeta-gecco2027.png
links:
  website: https://gecco-2027.sigevo.org/
last-updated: 2026-11-13
---

We have proposed the tutorial **Large Language Models for Metaheuristic Design: From Evolutionary Program Search to Agentic Algorithm Discovery – Tools, Benchmarking, Explainability and Open Challenges** at [GECCO 2027](https://gecco-2027.sigevo.org/), 12–16 July 2027 in Kraków, Poland.

In only a few years, LLM-driven automated algorithm design (AAD) has grown from a handful of proof-of-concept studies into one of the most active research directions in evolutionary computation (EC). Systems such as FunSearch and AlphaEvolve have shown that evolutionary search over programs, with large language models (LLMs) acting as intelligent variation operators, can produce new results in mathematics, computer science and engineering. In parallel, open frameworks such as LLaMEA, EASE, EoH, ReEvo, MCTS-AHD, LLM4AD, OpenEvolve, ShinkaEvolve and CodeEvolve have made this paradigm accessible to the wider community. At the same time, the field is maturing: questions about computational cost, reproducibility, data contamination, overfitting to benchmark suites, and the scientific value and interpretability of the discovered algorithms have become as pressing as raw performance.

This tutorial gives a structured and up-to-date overview of this landscape, aimed at both newcomers and active researchers.

### Outline

1. **Foundations**: how LLMs help researchers select and explain algorithms, propose hybrids, generate code and refine algorithm templates, and how populations, selection, crossover and mutation are realised when an LLM generates and refines candidate algorithms.
2. **The landscape of frameworks**: a taxonomy of current approaches (single-solution vs. population-based search, island models and quality-diversity archives, tree search, evolving components vs. complete algorithms), and the shift towards agentic, tool-using coding agents and reasoning models.
3. **Two frameworks in depth**: live demonstrations of **EASE** (Effortless Algorithmic Solution Evolution) and the **LLaMEA** ecosystem, including IOH integration, LLaMEA-HPO, LLaMEA-BO and the **BLADE** benchmarking suite.
4. **Benchmarking, evaluation and guardrails**: token and compute budgets, statistical validation, generalisation to unseen instances and dimensions, contamination and leakage, sandboxed execution and reproducibility.
5. **Understanding what was discovered**: explainability of LLM-generated algorithms through code evolution graphs, behaviour-space and ablation analyses, and human-in-the-loop co-discovery.
6. **Orchestration and efficiency**: ensembles of small and large language models that drive algorithm discovery cost-effectively.
7. **Open challenges and roadmap**: bias, compute and energy cost, generalisation, real-world integration and responsible use.

### Hands-on Material

We will provide ready-to-run notebooks and example configurations that work with open-weight models and small evaluation budgets, so attendees can run a small algorithm-discovery experiment on their own laptops during or after the session. Slides, code and literature pointers will be made available online.

### Previous Editions

Earlier versions of this tutorial were presented at IEEE WCCI 2024, PPSN 2024, GECCO 2025, GECCO 2026 and [IEEE WCCI 2026](/events/llmdaad2026/). The 2027 edition adds the newest open-source systems and agentic coding agents, a dedicated part on explainability, extended benchmarking practice and follow-along notebooks.

### Presenters

- Roman Senkerik, A.I.Lab, Tomas Bata University in Zlín, Czech Republic
- Niki van Stein, LIACS, Leiden University, the Netherlands
- Adam Viktorin, A.I.Lab, Tomas Bata University in Zlín, Czech Republic
- Michal Pluhacek, AGH University of Krakow, Poland
- Thomas Bäck, LIACS, Leiden University, the Netherlands
