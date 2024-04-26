---
component-id: child-search-expansion
type: WebApplication
name: Classification and curation of Listening Experiences with LLMs (Demo)
description: This demo component was developed with the aim of supporting the identification of implicit themes (classification) and metadata (curation) in text. It takes as reference the documentary evidence benchmark
work-package: 
  - WP4
pilot:
  - CHILD
project: polifonia-project
resource: https://github.com/polifonia-project/child-search-expansions/
release-date: 05/09/2023
release-number: v1.0
release-link: https://github.com/polifonia-project/child-search-expansions/releases/tag/v0.1
doi: https://zenodo.org/badge/latestdoi/588597123
changelog: https://github.com/polifonia-project/child-search-expansions/releases/tag/v0.1
licence:
  - Apache-2.0
copyright: "Copyright (c) 2023 CHILD @ The Open University"
contributors:
  - Jason Carvalho <https://github.com/JaseMK>
  - Alba Morales Tirado <https://github.com/albamoralest>
  - Enrico Daga <https://github.com/enridaga>
related-components:
- informed-by: documentary-evidence-benchmark
credits:
  - https://github.com/JaseMK
  - https://github.com/albamoralest
  - https://github.com/enridaga
---

# Classification and curation of Listening Experiences (Demo)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8322490.svg)](https://doi.org/10.5281/zenodo.8322490)

This small study, undertaken as part of the wider CHILD pilot, focuses on harnessing LLM technology
to classify existing text extracts within LED, a task traditionally performed by human domain experts,
to address the challenges posed by the volume of textual data in fields such as music history.
Our experiment evaluates the effectiveness of an LLM in categorizing text extracts under the specific
theme of childhood, comparing its performance with that of a human domain expert. The comparison
aims to quantify the alignment between machine and human interpretations in textual analysis, look
at areas where LLM technology may show weaknesses and also investigate if there areas where LLMs
are able to shed new light on data that may go unnoticed by humans.

---

The software included here was developed with the aim of supporting the identification of 
implicit themes in text and takes as reference the documentary evidence benchmark.

Interactions with the ChatGPT API (or other LLM) is currently handled in 
the `chatgpt.py` file. Interactions with the LED knowledge graph are handled in `led.py`. In 
order to run any of the scripts in this distribution, a copy of `config.py.dist` must be 
made, called `config.py`, in which a valid OpenAI API key should be specified.

A summary of the experiements performed is provided in 'output/CHILD_text_classification_with_LLM.pdf'

Results and analysis are provided in 'output/ChatGPT-CHILD-Analysis.xlsx'

