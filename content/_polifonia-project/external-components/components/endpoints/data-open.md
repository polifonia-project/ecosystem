---
component-id: data-open-ac-uk
type: SPARQLEndpoint
name: "The Open Knowldedge Graph (OKG)"
description: "The Open Knowldedge Graph (OKG) SPARQL Endpoint"
logo: https://avatars.githubusercontent.com/u/79987779?s=200&v=4
work-package:
- WP1
- WP2
- WP4
pilot:
- MEETUPS
- CHILD
project: polifonia-project
resource: https://data.open.ac.uk/sparql
demo: https://data.open.ac.uk/sparql
logo: http://dev-ext.kmi.open.ac.uk/data/assets/img/open-data-icon.png
licence:
- CC-BY_v4
copyright: "Copyright (c) 2023 The Open University"
contributors:
- Enrico Daga <https://github.com/enridaga>
- Mathieu d'Aquin <https://mdaquin.github.io/>
bibliography:
- main-publication: "Daga, Enrico, Mathieu d’Aquin, Alessandro Adamou, and Stuart Brown. \"The open university linked data–data. open. ac. uk.\" Semantic Web 7, no. 2 (2016): 183-191."
related-components:
- serves:
  - led
  - meetups-knowledge-graph
- reuses:
  - sparql-anything-cli
  - meetups-ontology
---

# The Open Knowledge Graph SPARQL Endpoint

[The Open Knowldedge Graph (OKG)](http://data.open.ac.uk) is the home of Linked Data from The Open University.

We interlink and expose data available from open institutional repositories of [The Open University](http://www.open.ac.uk) and make it available for reuse.

The data can be searched via a keyword-based interface, using well-known identifiers, or queried using the SPARQL endpoint.

The datasets relate the publications, qualifications, courses and Audio/Video material produced by The Open University, as well as the people involved in making them.

All these data are available through standard formats (RDF and SPARQL) and are (in most cases) available under an open license.

The OKG publishes the following dataset from the Polifonia Ecosystem:

- [The Listening Experience Database (LED)](https://data.open.ac.uk/page/context/led)
- [The MEETUPS Knowledge Graph (Historical Musical Meetups)](https://data.open.ac.uk/page/context/meetups)
