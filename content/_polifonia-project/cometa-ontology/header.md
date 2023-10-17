---
component-id: https://w3id.org/polifonia/ontology/cometa/
type: Ontology
name: CoMeta Ontology
description: An extension of Music Meta to describe music datasets
image: diagrams/cometa_overview.png
work-package:
- WP2
pilot:
- INTERLINK
project: polifonia-project
resource: ontology/cometa.owl
release-date: 13/05/2023
release-number: v1.0
release-link: https://github.com/polifonia-project/ontology-network/releases
doi: 10.5281/zenodo.7919970
changelog: https://github.com/polifonia-project/ontology-network/releases
licence: 
- CC-BY_v4
copyright: "Copyright (c) 2023 CoMeta Ontology Contributors"
contributors:
- Jacopo de Berardinis <https://github.com/jonnybluesman>
- Andrea Poltronieri <https://github.com/andreamust>
- Nicolas Lazzari <https://github.com/n28div>
related-components:
- informed-by:
  - polifoniacq-dataset
- reuses:  # any reused/imported ontology
  - https://w3id.org/polifonia/ontology/core/
  - https://w3id.org/polifonia/ontology/music-meta/
- extends:  # any extended ontology
  - https://w3id.org/polifonia/ontology/music-meta/
- story:  # any related story this ontology addresses
  - Linka#1_MusicKnowledge
- persona:  # any persona this ontology addresses
  - Linka
---
<!-- - documentation:  # link any resource providing documentation for this ontology
  - https://github.com/polifonia-project/cometa-ontology -->

# CoMeta Ontology

An extension of Music Meta to describe the metadata of music collections, corpora, containers, or simply music datasets! Here, metadata is described at the collection-level (data curator, annotations provided, availability of audio music, etc.), and at the content-level, (e.g., the title, artist, release of each piece in a dataset). The design of CoMeta is informed by a survey of Music Information Retrieval datasets, which allowed for the categorisation of common fields.

[Link to the website](https://github.com/polifonia-project/cometa-ontology)

