---
component-id: sparql-anything
name: SPARQL Anything
description: SPARQL Anything is a system for Semantic Web re-engineering that allows to query non-RDF files as-if they are in RDF.
type: 
- Library
- CLI tool
release-date: 01/2022
release-number: v0.6.0
work-package: 
- WP1
- WP2
- WP4
pilot:
- ORGANS
- CHILD
- MEETUPS
keywords:
  - knowledge graph construction
changelog:
licence:
- Apache 2.0
release-link: https://github.com/SPARQL-Anything/sparql.anything/releases/tag/v0.3.1
image: https://sparql-anything.cc/img/logo.png
logo: https://sparql-anything.cc/img/logo.png
demo:
- https://github.com/SPARQL-Anything/showcase-tate
- https://github.com/SPARQL-Anything/showcase-imma
links: 
  - http://sparql-anything.cc
  - https://github.com/SPARQL-Anything/sparql.anything/
#running-instance:
credits: 
- http://github.com/luigi-asprino
- http://github.com/enridaga
bibliography: 
- "Daga, Enrico; Asprino, Luigi; Mulholland, Paul and Gangemi, Aldo (2021). Facade-X: An Opinionated Approach to SPARQL Anything. In: Alam, Mehwish; Groth, Paul; de Boer, Victor; Pellegrini, Tassilo and Pandit, Harshvardhan J. eds. Volume 53: Further with Knowledge Graphs, Volume 53. IOS Press, pp. 58–73. http://oro.open.ac.uk/78973/1/78973.pdf"
related-components:
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