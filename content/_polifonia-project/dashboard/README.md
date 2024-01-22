---
component-id: melody-software
type: WebApplication
name: MELODY
description: MELODY is a dashboarding system for designing and publishing data stories based on Linked Open Data.
work-package:
- WP1
project: polifonia-project
resource: https://github.com/polifonia-project/dashboard/releases
demo: https://projects.dharc.unibo.it/melody/
release-date: 2022/05/12
release-number: v0.1.1
release-link: https://github.com/polifonia-project/dashboard/releases/tag/v0.1.1
doi: 10.5281/zenodo.6637345
changelog: https://github.com/polifonia-project/dashboard/releases/latest
licence:
- IscLicense
contributors:
- Marilena Daquino <https://github.com/marilenadaquino>
- Giulia Renda <https://github.com/mondoboia>
related-components:
- serves: 
  - broadcast-concerts-knowledge-graph
  - led
  - meetups-knowledge-graph
  - musicbo-knowledge-graph
  - bells-knowledge-graph
  - musow-dataset
- documentation:
  - melody-prototypes
bibliography:
- main-publication:"Giulia Renda, Marilena Daquino, and Valentina Presutti (2023). Melody: A Platform for Linked Open Data Visualisation and Curated Storytelling. In Proceedings of the 34th ACM Conference on Hypertext and Social Media (HT '23). Association for Computing Machinery, New York, NY, USA, Article 27, 1–8. https://doi.org/10.1145/3603163.3609035"
- publication:
  - "Giulia Renda, Marilena Daquino (2023). Storytelling with Linked Open Data. In La memoria digitale: forme del testo e organizzazione della conoscenza. Atti del XII Convegno Annuale AIUCD. Siena: Università degli Studi di Siena. https://zenodo.org/doi/10.5281/zenodo.8070707"
---


# Polifonia Dashboard

[![DOI](https://zenodo.org/badge/431529042.svg)](https://zenodo.org/badge/latestdoi/431529042)

MELODY - Make mE a Linked Open Data StorY is a dashboarding system that allows users familiar with Linked Open Data to create web-ready data stories.

 * Authenticate with GitHub to create a new story.
 * Access data from any SPARQL endpoint.
 * Select the layout template of your story.
 * Include charts, sections, filters, and descriptions.
 * Preview the final data story while creating it.
 * Embed or export your data story and single charts in several formats.

See the full documentation at https://polifonia-project.github.io/dashboard/.

## Quickstart

> **Step #1 - Get the source code**

- Download the ZIP
- Use GIT tool in the terminal/powershel/bash to clone the source code

> **Step #2 - Set up the environment**

1. Python3 should be installed properly in the workstation. If you are not sure if Python is 
properly installed, please open a terminal and type python --version.
2. Enter the project folder using the terminal/powershel/bash.
3. Install modules using a [Virtual Environment](https://docs.python.org/3/library/venv.html)

```bash

#MacOS/Linux
$ cd myproject
$ python3 -m venv venv
$ . venv/bin/activate

#Windows
> cd myproject
> py -3 -m venv venv
> venv\Scripts\activate
```


> **Step #3 - Install requirements**

`pip install -r requirements.txt`

> **Step #4 - Run the application**
```bash
#bash
$ export FLASK_APP=app
$ flask run
* Running on http://127.0.0.1:5000/

#CMD
> set FLASK_APP=app
> flask run
* Running on http://127.0.0.1:5000/

#Powershell
> $env:FLASK_APP = "app"
> flask run
* Running on http://127.0.0.1:5000/
```

MELODY is part of [Polifonia](https://polifonia-project.eu) H2020 project (described in Deliverable 1.9). Cite this repository as follows:

```
Renda Giulia, and Marilena Daquino. (2022). MELODY: Beta release (v0.1.1). DOI: 10.5281/zenodo.6637346
```