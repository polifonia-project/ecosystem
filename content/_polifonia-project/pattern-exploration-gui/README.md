---
component-id: pattern-exploration-gui
type: WebApplication
name: Patterns UI
description: A frontend interface for dispaying data derived from the [Patterns Knowledge Graph](https://github.com/polifonia-project/patterns-knowledge-graph).
work-package:
- WP5
project: polifonia-project
resource: https://github.com/polifonia-project/pattern-exploration-gui/releases
release-date: 23/02/2024
release-number: v1.0.0
licence:
- GNU_GPL_v3
contributors:
- Rory Sweeney <https://github.com/rorys4>
- Pushkar Jajoria <https://github.com/pushkarjajoria>
- James McDermott <https://github.com/jmmcd>
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
- https://polifonia.disi.unibo.it/patterns
- https://zenodo.org/records/10698076
funder:
  - name: Horizon 2020 Framework Programme
    url: https://cordis.europa.eu/programme/id/H2020-EC
    grant-agreement: "https://cordis.europa.eu/project/id/101004746"
credits: "This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement N. 101004746."
---


# Music Pattern Exploration - Frontend Server

## Description

This repository contains source code for the frontend of the Polifonia Patterns UI Music Patterns Exploration project. It is built using Vue.js (@vue/cli 5.0.8) and communicates with a separate Python backend server which queries a knowledge graph for data. It features a 'Search' home page, `Composition` pages for each tune, `Pattern` pages, `Tune Family` pages and an `About` page. It is a tool that provides interactive network visualisations and tabular data to allow exploration and discovery of similar tunes across different traditional European music corpuses. 

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

## Backend Server

The frontend server communicates with a separate [backend server](https://github.com/polifonia-project/pattern-explorations-backend).

## Knowledge Graph

The interface uses data provided by the [Patterns Knowledge Graph](https://github.com/polifonia-project/patterns-knowledge-graph) and the [Tunes Knowledge graph](https://github.com/polifonia-project/tunes-knowledge-graph).
