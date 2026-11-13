// Texts, logos and colours for every event banner (see banner.html, render.js).
// conferences: host conference shown in the top-left line and its logo.
// events: one entry per _events/*.md file; the key is the output file name,
//   <key>.png (card, 1200x628) and <key>-wide.png (1180x200).
// IJCCI conferences are shown as flat tags: filled = (co-)chaired by us, outlined = other.
const tag = (name, size, on = true) => ({tag: name, size, on});
const GENAI4EC = 'Supported by the IEEE CIS Task Force <b>GenAI4EC</b>';

var BANNERS = {
  conferences: {
    evostar2025: {name: 'EvoStar', year: 2025, dates: '23 – 25 April', place: 'Trieste, Italy', accent: '#e8632b', logos: ['evostar2025.png']},
    evostar2026: {name: 'EvoStar', year: 2026, dates: '8 – 10 April', place: 'Toulouse, France', accent: '#e8632b', logos: ['evostar2026.png']},
    evostar2027: {name: 'EvoStar', year: 2027, dates: '31 March – 2 April', place: 'Mainz, Germany', accent: '#e8632b', logos: ['evostar2027.png']},
    gecco2025: {name: 'GECCO', year: 2025, dates: '14 – 18 July', place: 'Málaga, Spain', accent: '#9b2a9b', logos: ['gecco2025.png']},
    gecco2026: {name: 'GECCO', year: 2026, dates: '13 – 17 July', place: 'San José, Costa Rica', accent: '#c8102e', logos: ['gecco2026.png']},
    gecco2027: {name: 'GECCO', year: 2027, dates: '12 – 16 July', place: 'Kraków, Poland', accent: '#e30a2b', logos: ['gecco2027.png']},
    cai2025: {name: 'IEEE CAI', year: 2025, dates: '5 – 7 May', place: 'Santa Clara, USA', accent: '#1d6fb8', logos: ['ieee-cai.png'], logoBox: {card: {width: '300px', right: '80px'}, wide: {width: '210px', height: '110px', top: '45px', right: '50px'}}},
    cai2026: {name: 'IEEE CAI', year: 2026, dates: '8 – 10 May', place: 'Granada, Spain', accent: '#1d6fb8', logos: ['ieee-cai.png'], logoBox: {card: {width: '300px', right: '80px'}, wide: {width: '210px', height: '110px', top: '45px', right: '50px'}}},
    wcci2026: {name: 'IEEE WCCI', year: 2026, dates: '21 – 26 June', place: 'Maastricht, the Netherlands', accent: '#1f3a8a', logos: ['wcci2026.png']},
    cec2027: {name: 'IEEE CEC', year: 2027, dates: '25 – 28 July', place: 'Edinburgh, UK', accent: '#3f9a3a', logos: ['cec2027.png'], logoBox: {card: {width: '400px', right: '40px'}, wide: {width: '300px', right: '30px'}}},
    cec2025: {name: 'IEEE CEC', year: 2025, dates: '8 – 12 June', place: 'Hangzhou, China', accent: '#1a6fd1', logos: ['cec2025.png']},
    ppsn2026: {name: 'PPSN', year: 2026, dates: '29 August – 2 September', place: 'Trento, Italy', accent: '#c2185b', logos: ['ppsn2026.png']},
    foga2025: {name: 'ACM/SIGEVO', year: '', dates: '27 – 29 August 2025', place: 'Leiden, the Netherlands', accent: '#4a9a3a', logos: ['foga2025.png']},
    ijcci2024: {name: 'IJCCI', year: 2024, dates: '20 – 22 November', place: 'Porto, Portugal', accent: '#0a7f8c'},
    ijcci2025: {name: 'IJCCI', year: 2025, dates: '22 – 24 October', place: 'Marbella, Spain', accent: '#0a7f8c'},
    ijcci2026: {name: 'IJCCI', year: 2026, dates: '28 – 30 October', place: 'Angers, France', accent: '#0a7f8c'},
    ijcci2027: {name: 'IJCCI', year: 2027, dates: '27 – 29 October', place: 'Porto, Portugal', accent: '#0a7f8c'},
  },
  events: {
    // EvoStar special sessions
    evollms2025: {conf: 'evostar2025', kicker: 'Special session', title: 'EvoLLMs', sub: 'Integrating Evolutionary Computing\nwith Large Language Models', motif: 'network'},
    evollms2026: {conf: 'evostar2026', kicker: 'Special session', title: 'EvoLLMs', sub: 'Integrating Evolutionary Computing\nwith Large Language Models', motif: 'network', seed: 3},
    evollms2027: {conf: 'evostar2027', kicker: 'Special session', title: 'EvoLLMs', sub: 'Integrating Evolutionary Computing\nwith Large Language Models', motif: 'network', seed: 11, note: GENAI4EC},
    beyondscalar2027: {conf: 'evostar2027', kicker: 'Special session', title: 'Beyond a Performance Scalar', sub: 'Evaluation Science for\nEvolutionary Computation', motif: 'curves', note: GENAI4EC},

    // GECCO workshops and tutorials
    llmfwec2025: {conf: 'gecco2025', kicker: '1st Workshop', title: 'LLMfwEC', sub: 'Large Language Models for and with\nEvolutionary Computation', motif: 'helix'},
    llmfwec2026: {conf: 'gecco2026', kicker: '2nd Workshop', title: 'LLMfwEC', sub: 'Large Language Models for and with\nEvolutionary Computation', motif: 'helix', seed: 5},
    llmfwec2027: {conf: 'gecco2027', kicker: '3rd Workshop', title: 'LLMfwEC', sub: 'Large Language Models for and with\nEvolutionary Computation', motif: 'helix', seed: 11, note: GENAI4EC},
    aaboh2025: {conf: 'gecco2025', kicker: '5th Workshop', title: 'AABOH', sub: 'Analysing Algorithmic Behaviour\nof Optimisation Heuristics', motif: 'curves'},
    aaboh2026: {conf: 'gecco2026', kicker: '6th Workshop', title: 'AABOH', sub: 'Analysing Algorithmic Behaviour\nof Optimisation Heuristics', motif: 'curves', seed: 9},
    'benchmarking-gecco2025': {conf: 'gecco2025', kicker: 'Tutorial', title: 'Benchmarking Optimization Algorithms', sub: 'Single- and multi-objective: how to make\nyour experimental data more valuable', subWide: '', motif: 'curves', seed: 4},
    'sb-gecco2025': {conf: 'gecco2025', kicker: 'Tutorial', title: 'Structural Bias', sub: 'in Iterative Optimisation Heuristics', motif: 'scatter'},
    'llmheuristics-gecco2026': {conf: 'gecco2026', kicker: 'Tutorial', title: 'LLMs for Metaheuristic Design', sub: 'Large Language Models and\nEvolutionary Computation', subWide: '', motif: 'tree'},
    'llmmeta-gecco2027': {conf: 'gecco2027', kicker: 'Tutorial', title: 'LLMs for Metaheuristic Design', sub: 'From Evolutionary Program Search to Agentic\nAlgorithm Discovery: Tools, Benchmarking,\nExplainability and Open Challenges', subWide: '', motif: 'tree', seed: 5, note: '<b>EASE</b> · <b>LLaMEA</b> · <b>BLADE</b>'},

    // IEEE CAI, WCCI, CEC
    becomllm2025: {conf: 'cai2025', kicker: 'Workshop', title: 'BEComLLM', sub: 'Bridging Evolutionary Computing\nand Large Language Models', motif: 'network', seed: 21},
    becomllm2026: {conf: 'cai2026', kicker: 'Workshop', title: 'BEComLLM', sub: 'Bridging Evolutionary Computing\nand Large Language Models', motif: 'network', seed: 22},
    'genai-wcci2026': {conf: 'wcci2026', kicker: 'Special session', title: 'GenAI and Heuristic Optimization', sub: 'Generative AI for heuristic optimization', subWide: '', motif: 'network', seed: 13},
    'llmaad-wcci2026': {conf: 'wcci2026', kicker: 'Tutorial', title: 'LLM-driven Algorithm Design', sub: 'Automated algorithm design with\nlarge language models: EASE and LLaMEA', subWide: '', motif: 'tree', seed: 8},
    'genai-cec2027': {conf: 'cec2027', kicker: 'Special session', title: 'Real-World Applications', sub: 'of Combining Generative AI and\nEvolutionary Computation', motif: 'network', seed: 27, titleSize: 92, note: GENAI4EC},
    'sb-cec2025': {conf: 'cec2025', kicker: 'Tutorial', title: 'Structural Bias', sub: 'in Iterative Optimisation Heuristics', motif: 'scatter', seed: 3},

    // PPSN, FOGA
    'llmaad-ppsn2026': {conf: 'ppsn2026', kicker: 'Tutorial', title: 'LLM-driven Algorithm Design', sub: 'Large Language Model driven Automated\nAlgorithm Design with Evolutionary Computing', subWide: '', motif: 'tree', seed: 12},
    'sb-ppsn2026': {conf: 'ppsn2026', kicker: 'Tutorial', title: 'Structural Bias', sub: 'in Iterative Optimisation Heuristics', motif: 'scatter', seed: 5},
    foga2025: {conf: 'foga2025', kicker: '18th Conference', title: 'FOGA 2025', sub: 'Foundations of Genetic Algorithms', motif: 'scatter', seed: 17},

    // IJCCI conferences
    ecta2024: {conf: 'ijcci2024', kicker: '16th International Conference', title: 'ECTA 2024', sub: 'Evolutionary Computation\nTheory and Applications', motif: 'none', logoBox: {card: {width: '440px', height: '430px', top: '90px', right: '40px'}, wide: {width: '320px', height: '180px', top: '10px'}}, logos: ['ecta.svg']},
    ecta2025: {conf: 'ijcci2025', kicker: '17th International Conference', title: 'ECTA 2025', sub: 'Evolutionary Computation\nTheory and Applications', motif: 'none', seed: 4, logoBox: {card: {width: '440px', height: '430px', top: '90px', right: '40px'}, wide: {width: '320px', height: '180px', top: '10px'}}, logos: ['ecta.svg']},
    ecta2026: {conf: 'ijcci2026', kicker: '18th International Conference', title: 'ECTA 2026', sub: 'Evolutionary Computation\nTheory and Applications', motif: 'none', seed: 6, logoBox: {card: {width: '440px', height: '430px', top: '90px', right: '40px'}, wide: {width: '320px', height: '180px', top: '10px'}}, logos: ['ecta.svg']},
    explains2024: {conf: 'ijcci2024', kicker: '1st International Conference', title: 'EXPLAINS 2024', sub: 'Explainable AI for Neural\nand Symbolic Methods', motif: 'none', seed: 31, logoBox: {card: {width: '440px', height: '430px', top: '90px', right: '40px'}, wide: {width: '320px', height: '180px', top: '10px'}}, logos: ['explains.svg']},
    explains2025: {conf: 'ijcci2025', kicker: '2nd International Conference', title: 'EXPLAINS 2025', sub: 'Explainable AI for Neural\nand Symbolic Methods', motif: 'none', seed: 32, logoBox: {card: {width: '440px', height: '430px', top: '90px', right: '40px'}, wide: {width: '320px', height: '180px', top: '10px'}}, logos: ['explains.svg']},
    explains2026: {conf: 'ijcci2026', kicker: '3rd International Conference', title: 'EXPLAINS 2026', sub: 'Explainable AI for Neural\nand Symbolic Methods', motif: 'none', seed: 33, logoBox: {card: {width: '440px', height: '430px', top: '90px', right: '40px'}, wide: {width: '320px', height: '180px', top: '10px'}}, logos: ['explains.svg']},
    agentics2026: {conf: 'ijcci2026', kicker: '2nd International Conference', title: 'AGENTICS 2026', sub: 'Agentic and Generative Techniques\nin Intelligent Computational Systems', motif: 'none', seed: 34, logoBox: {card: {width: '440px', height: '430px', top: '90px', right: '40px'}, wide: {width: '320px', height: '180px', top: '10px'}}, logos: ['agentics.svg']},
    ijcci2027: {conf: 'ijcci2027', kicker: '19th Joint Conference', title: 'IJCCI 2027', sub: 'International Joint Conference\non Computational Intelligence', motif: 'fuzzy', seed: 19,
      logos: [tag('ECTA', 24), tag('EXPLAINS', 24), tag('AGENTICS', 24), tag('NCTA', 24, false), tag('FCTA', 24, false)],
      tagsInText: true, logoBox: {wide: {width: 'auto', height: 'auto', top: '40px', right: '34px', flexWrap: 'nowrap'}}},
  },
};
if (typeof module !== 'undefined') module.exports = BANNERS;
