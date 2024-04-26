---
component-id: llm4led
type: Software
name: Curation of documentary evidence, experiments with LED/GPT-4
description: This repository contains Python code for scraping data from LED (Listening Experience Database). The code processes the obtained data and uses the GPT-4 API to generate annotations from the submitted listening evidence.
work-package: 
  - WP4
pilot:
  - CHILD
project: polifonia-project
resource: https://github.com/polifonia-project/llm4led/
release-date: 24/04/2024
release-number: v1.0
release-link: https://github.com/polifonia-project/llom4led/releases/tag/v1.0
doi: https://zenodo.org/badge/latestdoi/
changelog: https://github.com/polifonia-project/llom4led/releases/tag/v1.0
licence:
  - Apache-2.0
copyright: "Copyright (c) 2024 The Open University"
contributors:
  - Chukwudi "Festus" Uwasomba <https://github.com/cfestus>
  - Enrico Daga <https://github.com/enridaga>
related-components:
- reuses: documentary-evidence-benchmark
credits:
  - https://github.com/cfestus
  - https://github.com/enridaga
---

# Curation of documentary evidence, experiments with LED/GPT-4

## Description
This repository contains Python code for scraping data from LED (Listening Experience Database). The code processes the obtained data and uses the GPT-4 API to generate annotations from the submitted listening evidence.

## Prerequisites

- Python 3.x
- OpenAI API key

## To run the code 

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt.

4. **API Configuration**:
Create a .env file in the root directory and add your OpenAI API key, that is your GPT-4 API.
   ```bash
   OPENAI_API_KEY="your_api_key_here"

5. **Usage**:
Once you have completed the setup, run the main script to generate annotations.
   ```bash
   run main.py

