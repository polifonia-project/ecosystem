---
component-id: pattern-explorations-backend
type: WebApplication
name: Pattern Exploration Backend
description: A server that requests and processes data from the [Patterns Knowledge Graph](https://github.com/polifonia-project/patterns-knowledge-graph) on behalf of the [Pattern Exploration GUI](https://github.com/polifonia-project/pattern-exploration-gui).
work-package:
- WP5
project: polifonia-project
resource: https://github.com/polifonia-project/pattern-explorations-backend/releases
release-date: 01/03/2024
release-number: v0.1.0
licence:
- GNU_GPL_v3
contributors:
- James McDermott <https://github.com/jmmcd>
- Pushkar Jajoria <https://github.com/pushkarjajoria>
- Rory Sweeney <https://github.com/rorys4>
related-components:
- reuses:
  - "pattern-exploration-gui"
  - "patterns-knowledge-graph"
bibliography:
- publication: 
  - "Polifonia Deliverable 5.6"
links:
- https://github.com/polifonia-project/pattern-explorations-backend
- https://polifonia.disi.unibo.it:8080/patterns (TODO)
- https://zenodo.org/record/ (TODO)
funder:
  - name: Horizon 2020 Framework Programme
    url: https://cordis.europa.eu/programme/id/H2020-EC
    grant-agreement: "https://cordis.europa.eu/project/id/101004746"
credits: "This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement N. 101004746."
---

# Python Flask Server for Pattern Explorations using the Blazegraph KG

A Python Flask server providing APIs for searching musical tunes and retrieving similarity measures. It can be connected to a SPARQL endpoint but currently uses a mock response.

This software forms part of Polifonia Deliverable D5.6.

## Prerequisites

Ensure you have Python and pip installed on your machine. I'd recommend using a environment manager like miniconda to keep everything sane.

## Installing Dependencies

Clone the repository, navigate to the project folder and install the dependencies from `requirements.txt`.

```
git clone <repository-url>
cd <project-folder>
pip install -r requirements.txt
```

Replace `<repository-url>` and `<project-folder>` with your actual repository URL and project folder name.

## Application Code

The main application code is in `app.py`, and the SPARQL queries are generated using a query factory in `query_factory.py`.

## Running the Server

Start the Flask server with:

```
python app.py
```

The server runs on `localhost` port `5000` by default.

## API Endpoints

### 1. Search for Tunes

Search for tunes with a GET request to `/api/search`, passing the search query as a parameter.

Example:

```
curl http://localhost:5000/api/search?query=Vivaldi
```

### 2. Retrieve Similarity Measures

Get a list of similarity measures with a GET request to `/api/similarity-measures`.  

Example:

```
curl http://localhost:5000/api/similarity-measures
```
would return all of the available similarity measures.

## `query_factory.py` Example

The `query_factory.py` contains functions to generate SPARQL queries. Here is a usage example:

```python
import requests
from query_factory import get_tune_given_name

# Generate the SPARQL query
sparql_query = get_tune_given_name("Yankee Doodle")

# Execute the SPARQL query
response = requests.post(
    BLAZEGRAPH_URL,
    data={
        'query': sparql_query,
        'format': 'json'
    }
)

# Print the JSON data
print(response.json())
```

## `requirements.txt`

The required libraries are listed in `requirements.txt`:

```
Flask==2.3.2
Flask_Cors==3.0.10
Requests==2.31.0
```

