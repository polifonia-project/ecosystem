---
component-id: pattern-exploration-gui
type: WebApplication
name: Pattern Exploration GUI
description: A frontend interface for dispaying data derived from the [Patterns Knowledge Graph](https://github.com/polifonia-project/patterns-knowledge-graph).
work-package:
- WP5
project: polifonia-project
resource: https://github.com/polifonia-project/pattern-exploration-gui/releases
release-date: 01/03/2024
release-number: v0.1.0
licence:
- GNU_GPL_v3
contributors:
- James McDermott <https://github.com/jmmcd>
- Pushkar Jajoria <https://github.com/pushkarjajoria>
- Rory Sweeney <https://github.com/rorys4>
related-components:
- story:
  - Brendan#1_FindTraditionalMusic
- persona:
  - Brendan
- reuses:
  - "pattern-explorations-backend"
  - "patterns-knowledge-graph"
bibliography:
- publication: 
  - "Polifonia Deliverable 5.6"
links:
- https://github.com/polifonia-project/pattern-exploration-gui
- https://polifonia.disi.unibo.it/patterns/index.html (TODO)
- https://zenodo.org/record/ (TODO)
funder:
  - name: Horizon 2020 Framework Programme
    url: https://cordis.europa.eu/programme/id/H2020-EC
    grant-agreement: "https://cordis.europa.eu/project/id/101004746"
credits: "This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement N. 101004746."
---


# Music Pattern Exploration - Frontend Server

## Description

This repository contains the frontend server for the Music Pattern Exploration project. The frontend is built using Vue.js (@vue/cli 5.0.8) and communicates with a separate Python backend server for data. It features a search home page and a tune page.

This software forms part of Polifonia Deliverable D5.6.

## Prerequisites

- Node.js and npm
- Vue CLI 5.0.8

## Installation

To install and run this project locally:

1. Clone this repository:

    `git clone git@github.com:polifonia-project/pattern-exploration-gui.git`

2. Navigate into the project directory:

    `cd pattern-exploration-gui`

3. Install the necessary dependencies:

    `npm install`

4. Start the server:

    `npm run serve`

The application will start and is accessible via `http://localhost:8080` in your browser (or another port if 8080 is already in use).

**Note:** Make sure that the backend server is also running and accessible for the frontend to fetch data.

## Usage

- **Search Home Page:** 
- **Tune Page:** 

## Contributing

Contributions to the Music Pattern Exploration Frontend are welcomed! If you wish to contribute, please fork the repository and submit a pull request.

## Backend Server

The frontend server communicates with a separate backend server.

## Contact

For any inquiries or issues, please feel free to contact me at [pushkar.jajoria@universityofgalway.ie].
