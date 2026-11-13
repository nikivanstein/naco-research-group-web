---
title: "Real-World Applications of Generative AI and EC at CEC 2027"
status: active
type: workshop
type_label: "Special session"
pending: true

notitle: false

description: |
  Real-World Applications of Combining Generative AI and Evolutionary Computation

people:
  - stein
  - kononova
  - back
  - emmerich

layout: event
eventdate: 2027-07-25
enddate: 2027-07-28
location: "Edinburgh, Scotland, UK"
venue: "IEEE CEC 2027"
image: /img/events/genai-cec2027.png
largeimage: /img/events/genai-cec2027-wide.png
header:
    og_image: events/genai-cec2027.png
links:
  website: https://ieeecec.org/2027/
dates:
  - {label: "Full paper submission", date: 2027-02-28}
  - {label: "Short paper submission", date: 2027-03-15}
  - {label: "Paper acceptance notification", date: 2027-04-07}
  - {label: "Final paper submission and early registration", date: 2027-05-01}
  - {label: "IEEE CEC 2027", date: 2027-07-25}
dates_note: "Dates from the IEEE CEC 2027 website; no extensions for paper submission."
last-updated: 2026-11-13
---

We have proposed the special session **Real-World Applications of Combining Generative AI and Evolutionary Computation** at [IEEE CEC 2027](https://ieeecec.org/2027/), 25–28 July 2027 in Edinburgh, Scotland.

Real-world optimisation problems seldom match the textbook setting of evolutionary computation (EC). Generative AI and large language models (LLMs) map heterogeneous inputs, such as requirement texts, sketches, code, CAD and simulation files, and tabular data, to candidate solutions, objective estimates and optimiser components. This session brings together work that applies LLM-driven EC, and related generative-AI-aided optimisation, to real-world problems, and asks what works, what does not, and why.

### Motivation

Evaluations in engineering and product design are often costly multi-fidelity simulations or human judgements available only tens of times per session. Decisive knowledge for routing, packing, scheduling and logistics exists as text and code under restricted design budgets. Molecular, materials and engineering design offers tens rather than thousands of observations. Prompt and agentic workflow configuration runs under explicit compute budgets, and inspection, forecasting and clinical prediction are limited by missing rather than noisy data. Each setting relaxes a classical EC assumption.

Generative models can act as a prior over solutions, a natural-language interface for stating objectives and constraints, a source of semantic variation operators, a surrogate or fitness predictor, and a generator of missing or rare data. They also bring risks: priors that bias rather than aid search, fitness assigned by the model family that proposes candidates, benchmark contamination, and costs that are rarely reported.

### Scope

The session prioritises **application studies** and welcomes methodological contributions (LLM-guided search, semantic crossover and mutation, automated design and configuration of optimisers, evolutionary prompt and workflow optimisation) when they are demonstrated on real-world problems. We encourage contributions to state the application setting, ablate the generative component, compare against strong non-LLM baselines such as configuration and hyper-heuristic methods, and report evaluation cost, so that claims rest on evidence and can be reproduced, including under proprietary model access.

### Topics of Interest

Topics include, but are not limited to:

- Design and engineering optimisation
- Interactive, preference-based and natural-language-driven optimisation
- Logistics, scheduling and combinatorial applications
- Molecular and materials design
- Prediction and anomaly detection under data scarcity
- LLM-guided search and semantic operators
- LLM-driven algorithm design, configuration and hyper-heuristics
- Evolutionary prompt and agentic workflow optimisation
- Data synthesis and surrogates for expensive simulators
- Benchmarks, cost accounting, contamination and reproducibility

### Previous Editions

- [Generative AI and Heuristic Optimization at IEEE WCCI 2026](/events/genaiwcci2026/)
- [Generative AI and Heuristic Optimization at IEEE WCCI/CEC 2024](http://www.soft-computing.de/CEC24-GAI.html)

### Organisers

- Stefan Menzel, Honda Research Institute Europe, Germany (contact)
- Niki van Stein, Leiden University, the Netherlands (contact)
- Anna V. Kononova, Leiden University, the Netherlands
- Thomas Bäck, Leiden University, the Netherlands
- Bernhard Sendhoff, Honda Research Institute Europe, Germany
- Yew Soon Ong, Nanyang Technological University, Singapore
- Yaochu Jin, Westlake University, China
- Michael T. M. Emmerich, University of Jyväskylä, Finland

### Acknowledgements

<p><img src="/img/projects/EU.png" alt="European Union flag" style="float: left; width: 60px; height: auto; margin-right: 10px;">This special session is partially supported by the European Union under Horizon Europe (GenAIDE, Grant Agreement No. 101226927). It is also supported by the <a href="https://cis.taskforce.ieee.org/genai4ec/">IEEE CIS Task Force on Generative AI for Evolutionary Computation (GenAI4EC)</a>.</p>
