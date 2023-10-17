# Source Ontology
The Source ontology addresses concepts and relationships for representing sources of (music-related) information.

[![DOI](https://zenodo.org/badge/372536364.svg)](https://zenodo.org/badge/latestdoi/372536364)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> 🔗 Ontology URI: [https://w3id.org/polifonia/ontology/source/](https://w3id.org/polifonia/ontology/source/)

Source represents various sources of music-related information. These include manuscripts, textbooks, articles, interviews, reviews, comments, memoirs, etc. of different scope and format (physical, digital). The module aims to provide general support to describe information related to the creator and type of the source, the time and place when/where it was created, the context of production and usage, and the subject and goals. Although this conceptualisa- tion leans towards bibliographical sources, the module provides expressivity to indicate multimedia documents (e.g. images of scores, audio recording, video). For example, a video recording of a performance can be considered as a musical source – providing documentary evidence of a composition e.g. during an event. The module is part of the [Polifonia ontology network](https://github.com/polifonia-project/ontology-network).

![Source module diagram](diagrams/source-module.png)

## Competency questions addressed

| **ID** | **Competency Question**              |
|--------|--------------------------------------|
| CQ1    | Which is the subject of a source?     |
| CQ2    | Which is the credibility of a source?     |
| CQ3    | Which is the goal of a source?          |
| CQ4    | Which is the type of a source?          |
| CQ5    | Which is the context of production of a source?         |
| CQ6    | Which is the context of usage of a source?         |

## Examples of SPARQL queries

- Which is the subject of a source?

```sparql
PREFIX src: <https://w3id.org/polifonia/ontology/source/>
SELECT DISTINCT ?source ?subject
WHERE { ?source src:hasSubject ?subject .
}
```

## Statistics
- number of classes: 9 
- number of object properties: 14
- number of datatype properties: 1


## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
