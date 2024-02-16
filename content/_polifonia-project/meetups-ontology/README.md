---
component-id: meetups-ontology
type: Ontology
name: MEETUPS Ontology
description: "Ontology that represents concepts and relationships describing encounters between people in the musical world in Europe from c. 1800 to c. 1945."
work-package: 
- WP4
pilot:
- MEETUPS
project: polifonia-project
resource: https://github.com/polifonia-project/meetups-ontology
release-date: 2023/01/13
release-number: v0.1
release-link: https://github.com/polifonia-project/meetups-ontology/releases/tag/v0.1
doi: 10.5281/zenodo.7928155
changelog: https://github.com/polifonia-project/meetups-ontology/releases/tag/v0.1
licence: 
- Apache-2.0
copyright: "Copyright (c) 2023 MEETUPS @ The Open University"
contributors:
- Alba Morales Tirado <https://github.com/albamoralest>
- Enrico Daga <https://github.com/enridaga>
related-components:
- informed-by:
  - meetups-pilot
  - meetups-knowledge-graph
- persona:
  - Ortenz
  - David
  - Sophie
bibliography:
- main-publication: "Morales Tirado, Alba; Carvalho, Jason; Mulholland, Paul and Daga, Enrico (2023). Musical Meetups: a Knowledge Graph approach for Historical Social Network Analysis. In: CEUR Workshop Proceedings: SEMMES 2023: Semantic Methods for Events and Stories workshop ESWC 2023. https://oro.open.ac.uk/88720/1/2023_SEMMES_Meetups-CR.pdf"
- deliverable-document: "WP2 et al, D2.2: Ontologies and knowledge graphs of music objects, patterns, and software package – 2nd version (V1.0)"
---

# MEETUPS Ontology

[![DOI](https://zenodo.org/badge/588540533.svg)](https://zenodo.org/badge/latestdoi/588540533)
[![License: Apache 2.0]](http://www.apache.org/licenses/LICENSE-2.0)

Ontology URI: [https://w3id.org/polifonia/ontology/meetups-ontology#/](https://w3id.org/polifonia/ontology/meetups-ontology#/)

The ontology module MEETUPS, which is part of the Polifonia Ontology Network, represents concepts and relationships describing encounters between people in the musical world in Europe from c. 1800 to c. 1945.

## Ontology description

Typically, historical meetups, which are the main subject of this module, are described by means of four main components: (i) the people involved in the meetup, for instance, the person that is the subject of interest and the people interacting in the event, (ii) the place where the encounter took place (e.g., city, country, venue), the type of event, the reason (e.g., music making, personal life, business, among others) and the date when it took place.

This ontology module is strictly related to the Polifonia pilot MEETUPS: ![MEETUPS Pilot](https://github.com/polifonia-project/meetups_pilot)

Ontology graphic description:
![MEETUPS ontology module](diagrams/meetups-ont-diagram-V0.2.png?raw=true "MEETUPS ontology module")


Ontology provenance information:
![MEETUPS ontology module](diagrams/meetups-ont-diagram-V2_prov.png?raw=true "MEETUPS provenance")



## Competency questions related to MEETUPS ontology module
Ortenz
- What places did musician Z visited in her career?
- Where did she perform?
- Where did she live?
- Did musician X and performer Y ever meet? Where, when, and why?
- In what context the meeting happened?
- What is the nature of the event?
- Was it a celebration, a festival, a private event?
- Was it a religious or a secular event?
- Who paid to support the event?
- What is the provenance of the event attendees? What and how they happened to be there?
- Did they travel to reach the place?
- Were they invited? Was the meeting accidental?
- How can we characterize the relation among the participants?
- Was there a power relation? (e.g., Patreon / Musician)

David
- Where were the places (in which they played)?
- Where were the musicians coming from?

Sophie
- What is the time relationship between different musicians, e.g., who was working at the same time?
- What was the composer’s network (patrons, institutions …)?


These Competency Questions were selected from the following stories
- [Ortenz](https://github.com/polifonia-project/stories/blob/main/Ortenz:%20Music%20Historian/Ortenz%232_MusicalSocialNetwork.md)
- [David](https://github.com/polifonia-project/stories/blob/main/David:%20Music%20Historian/David%231_MusicHistorian.md)
- [Sophie](https://github.com/polifonia-project/stories/blob/main/Sophia:%20Musicologist/Sophia%231_MusiciansAndTheirEnvironment.md)

## Examples of SPARQL queries

Refer to [queries folder](https://github.com/polifonia-project/meetups-ontology/tree/578438d07425b775df9aedae27f67fe4ddb002bc/queries)

## Statistics

Considering the MEETUPS ontology is still in development, we report the following useful statistics:
- number of classes:  17
- number of object properties: 5
- number of datatype properties: 0
- number of logical axioms: 27

## Datasets

MEETUPS Pilot dataset: dataset representing a collection of ~33k biographies collected from Wikipedia pages,

- https://github.com/polifonia-project/meetups_corpus_collection

## Alignment to other ontologies

MEETUPS pilot is part of the European project Polifonia and it is aligned to the Polifonia Ontology Network (PON)
- [Core](https://w3id.org/polifonia/ontology/core)

MEETUPS also reuse ontologies such as Time and ProvOnto
- [Time](http://www.w3.org/2006/time)
- [PROV-Onto](http://w3.org/ns/prov#)

## Citation
```
@inproceedings{Morales_2023,
  title={Musical Meetups: a Knowledge Graph Approach for Historical Social Network Analysis},
  author={Morales Tirado, Alba and Carvalho, Jason and Mulholland, Paul and Daga, Enrico},
  booktitle={Proceedings of the ESWC 2023 Workshops and Tutorials co-located with 20th European Semantic Web Conference (ESWC 2023)},
  year={2023}
}
```

## Acknowledgements

This work was supported by the EU’s Horizon Europe research and innovation programme within the Polifonia project (grant agreement N. 101004746).
