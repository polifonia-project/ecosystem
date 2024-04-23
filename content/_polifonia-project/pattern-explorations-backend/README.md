---
component-id: pattern-explorations-backend
type: WebApplication
name: Pattern Exploration Backend
description: A server that requests and processes data from the [Patterns Knowledge Graph](https://github.com/polifonia-project/patterns-knowledge-graph) on behalf of the [Pattern Exploration GUI](https://github.com/polifonia-project/pattern-exploration-gui).
work-package:
- WP5
project: polifonia-project
resource: https://github.com/polifonia-project/pattern-explorations-backend/releases
release-date: 23/02/2024
release-number: v1.0.0
licence:
- GNU_GPL_v3
contributors:
- Rory Sweeney <https://github.com/rorys4>
- Pushkar Jajoria <https://github.com/pushkarjajoria>
- James McDermott <https://github.com/jmmcd>
related-components:
- reuses:
  - "pattern-exploration-gui"
  - "patterns-knowledge-graph"
bibliography:
- publication: 
  - "Polifonia Deliverable 5.6"
links:
- https://github.com/polifonia-project/pattern-explorations-backend
- https://polifonia.disi.unibo.it/patterns/api
- https://zenodo.org/records/10698170
funder:
  - name: Horizon 2020 Framework Programme
    url: https://cordis.europa.eu/programme/id/H2020-EC
    grant-agreement: "https://cordis.europa.eu/project/id/101004746"
credits: "This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement N. 101004746."
---

# Python Flask Server for Patterns UI using the Blazegraph KG

A Python Flask server providing APIs used by the Pattens UI frontend. It is connected to the FONN SPARQL endpoint for the Patterns and Tunes knowledge graphs.

This software forms part of Polifonia Deliverable D5.6.

## Prerequisites

Ensure you have Python and pip installed on your machine. I'd recommend using a environment manager like miniconda to keep everything sane.

## Installing Dependencies

Clone the repository, navigate to the project folder and install the dependencies from `requirements.txt`.

```
git clone git@github.com:polifonia-project/pattern-explorations-backend.git
cd pattern-explorations-backend
pip install -r requirements.txt
```

## Application Code

The main application code is in `app.py`, and the SPARQL queries are generated using a query factory in `query_factory.py`.
The file `fuzzy_search.py` contains properties and methods related to the fuzzy tune title search feature.

## Running the Server

Start the Flask server with:

```
python app.py
```

The server runs on `localhost` port `5000` by default.

## `requirements.txt`

The required libraries are listed in `requirements.txt`:

```
Flask==2.3.2
Flask_Cors==3.0.10
Requests==2.31.0
fuzzywuzzy~=0.18.0
singleton-decorator
python-Levenshtein
```

