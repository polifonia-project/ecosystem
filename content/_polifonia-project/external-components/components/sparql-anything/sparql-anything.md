---
container-id: sparql-anything
name: SPARQL Anything
description: SPARQL Anything is a system for Semantic Web re-engineering that allows to query non-RDF files as-if they are in RDF.
type: Project
work-package: 
- WP1
- WP2
- WP4
pilot:
- MEETUPS
- CHILD
project: polifonia-project
bibliography:
- main-publication: "Asprino, Luigi, Enrico Daga, Aldo Gangemi, and Paul Mulholland. \"Knowledge Graph Construction with a façade: a unified method to access heterogeneous data sources on the Web.\" ACM Transactions on Internet Technology 23, no. 1 (2023): 1-31. https://dl.acm.org/doi/pdf/10.1145/3555312"
- publication: 
  - "Daga, Enrico, Luigi Asprino, Paul Mulholland, and Aldo Gangemi. \"Facade-X: an opinionated approach to SPARQL anything.\" Studies on the Semantic Web 53 (2021): 58-73."
  - "Ratta, Marco, and Enrico Daga. \"Knowledge Graph Construction From MusicXML\": An Empirical Investigation With SPARQL Anything. http://oro.open.ac.uk/85326/1/Music_Knowledge_Graphs_Paper%20%281%29.pdf"
- funder:
  - name: European Commission H2020
    url: https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/programmes/h2020
    grant-agreement: "GA101004746"
  - name: European Commission H2020
    url: https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/programmes/h2020
    grant-agreement: "GA870811"
credits: "This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreements GA101004746 (Polifonia) and GA870811 (SPICE)."
has-part:
  - sparql-anything-cli
  - sparql-anything-java
  - sparql-anything-docs
  - sparql-anything-tutorials
  - sparql-anything-python
  - sparql-anything-requirements
  - sparql-anything-docker
---

# SPARQL Anything

[SPARQL Anything](http://sparql-anything.eu) is a system for Semantic Web re-engineering that allows users to ... query anything with SPARQL.

Main features:
- Query files in plain SPARQL 1.1, via the `SERVICE <x-sparql-anything:>` (see [configuration](https://sparql-anything.readthedocs.io/en/latest/#configuration)) and build knowledge graphs with `CONSTRUCT` queries
- [Supported formats](https://sparql-anything.readthedocs.io/en/latest/#supported-formats): XML, JSON, CSV, HTML, Excel, Text, Binary, EXIF, File System, Zip/Tar, Markdown, YAML, Bibtex, DOCx (see [configuration](#format-specific-options))
- Transforms [files, inline content, or the output of an external command](https://sparql-anything.readthedocs.io/en/latest/#general-purpose-options)
- Full fledged [HTTP client](#http-options) to query Web APIs (headers, authentication, all methods supported)
- [Functions library](https://sparql-anything.readthedocs.io/en/latest/#functions-and-magic-properties) for RDF sequences, strings, hashes, easy entity building, ...
- Combine multiple SERVICE clauses into complex data integration queries (thanks to SPARQL)
- Query templates (using [BASIL variables](https://sparql-anything.readthedocs.io/en/latest/#query-templates-and-variable-bindings))
- Save and reuse SPARQL `Results Sets` as input for [parametric queries](https://sparql-anything.readthedocs.io/en/latest/#query-templates-and-variable-bindings)
- Slice large CSV files with an iterator-like execution style (soon [JSON](https://github.com/SPARQL-Anything/sparql.anything/issues/202) and [XML](https://github.com/SPARQL-Anything/sparql.anything/issues/203))
- Supports an [on-disk option](https://sparql-anything.readthedocs.io/en/latest/#general-purpose-options) (with Apache Jena TDB2)

SPARQL Anything is developed in collaboration with the EU-funded project [SPICE](http://spice-h2020.eu).