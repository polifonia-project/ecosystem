---
component-id: https://w3id.org/polifonia/ontology/instrument/
type: Ontology
name: Music Instrument Ontology
description: An ontology to describe instruments as mediums of performance and their technical properties.
image: https://github.com/polifonia-project/music-instrument-ontology/blob/main/diagrams/music-instrument-main-entities.png
work-package:
- WP2
pilot:
- INTERLINK
- ORGANS
- BELLS
project: polifonia-project
resource: ontology/music-instrument.owl
release-date: 13/04/2023
release-number: v1.0
release-link: https://github.com/polifonia-project/ontology-network/releases
doi: 10.5281/zenodo.7919970
changelog: https://github.com/polifonia-project/ontology-network/releases
licence:
- CC-BY_v4
copyright: "Copyright (c) 2023 Music Instrument Contributors"
contributors: # replace these with the GitHub URL of each contributor
- Jacopo de Berardinis <https://github.com/jonnybluesman>
- Nicolas Lazzari <https://github.com/n28div>
- Valentina Anita Carriero <https://github.com/valecarriero>
- Fiorela Ciroku <https://github.com/FiorelaCiroku>
related-components:
- informed-by:
  - polifoniacq-dataset
- reuses:  # any reused/imported ontology
  - https://w3id.org/polifonia/ontology/core/
- story:  # any related story this ontology addresses
  - Paul#1_OrganComparison
  - Paul#2_ResourceReliability
  - Frank#1_OrganKnowledge
  - Amy#1_OrganTrends
  - Amy#2_OrganBuilders
- persona:  # any persona this ontology addresses
  - Paul
  - Amy
  - Frank
---
<!-- - documentation:  # link any resource providing documentation for this ontology
  - https://github.com/polifonia-project/music-instrument-ontology -->

# Music Instrument Ontology

The Instrument Module describes musical instruments as mediums of performance
and their technical properties. Given that numerous taxonomies of instruments
into groups and families exist (e.g. Hornbostel-Sachs, MIMO, Mu- sicBrainz) and
finding common categorisations is an open problem, our module provides an
abstraction capable to express arbitrary classifications. This is achieved by
leveraging the Information-Realisation and the Collection ODPs. Overall, the
module allows to: (i) refer to instruments as entities (an instrumen- tation of
a piece for “piano” and “viola”) as well as conceptually (e.g. a viola has 4
strings); (ii) support the integration with different taxonomies and
vocabularies; (iii) describe the evolution of instruments in time
and space (e.g. a viola as a cultural heritage object being relocated).
This provides a foundational level where contributors can “plug” their
instrument-specific ontologies.

[Link to the website](https://github.com/polifonia-project/music-instrument-ontology)
