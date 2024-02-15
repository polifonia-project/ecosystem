---
component-id: meetups-knowledge-graph
type: KnowledgeGraph
name: MEETUPS Knowledge Graph
description: MEETUPS Knowledge Graph module with data on historical meetups and related to MEETUPS Pilot
work-package:
- WP4
pilot:
- MEETUPS
project: polifonia-project
resource: https://github.com/polifonia-project/meetups-knowledge-graph/
release-date: 20/07/2022
release-number: v0.1
release link: https://github.com/polifonia-project/meetups-knowledge-graph/releases/tag/v0.1
doi: 10.5281/zenodo.7924618
changelog: https://github.com/polifonia-project/meetups-knowledge-graph/releases/tag/v0.1
licence:
- CC-BY_v4
copyright: "Copyright (c) 2023 MEETUPS @ The Open University"
contributors:
- Alba Morales Tirado <https://github.com/albamoralest>
- Enrico Daga <https://github.com/enridaga>
- Jason Carvalho <https://github.com/JaseMK>
credits:
- https://github.com/albamoralest
- https://github.com/enridaga
bibliography:
- main-publication: "Morales Tirado, A., Carvalho, J., Mulholland, P. and Daga, E., 2023. Musical Meetups: a Knowledge Graph approach for Historical Social Network Analysis."
related-components:
- informed-by: 
  - meetups-ontology
  - meetups-corpus-collection
- generated-by:
  - meetups-hm-identification
- persona:
  - Ortenz
  - David
  - Sophie
- reuses:
  - sparql-anything-java
  - sparql-anything-cli
---

# MEETUPS Knowledge Graph 

## Musical Meetups Knowledge Graph (MMKG)

[![DOI](https://zenodo.org/badge/588597123.svg)](https://zenodo.org/badge/latestdoi/588597123)

The MEETUPS knowledge graph contains data about historical encounters of people in the musical world in Europe from c. 1800 to c. 1945.

## Meetups SPARQL Endpoint

```
https://polifonia.kmi.open.ac.uk/meetups/sparql/
```

## Knowledge Graph description

The KG was built using data collected from Wikipedia. A total of 33309 biographies of musical artist's web pages in English were collected [1]. 
We apply knowledge extraction techniques and methods for text processing to recognise, classify and link the entities that are part of a historical meetup, particularly: people, places, time expressions and themes [3].

The MMKG data contains evidence that describes historical meetups according to Meetups Ontology [2]. A historical meetup – mtp:Meetup, is derived from evidence within a biography – mtp:hasEvidenceText. Mentions of at least one or more participants and places are represented by the mtp:Participant and mtp:Location class, respectively. Each mention is an entity (mtp:hasEntity) extracted and linked to DBpedia or Wikidata (Section 4 gives details on the extraction process). To represent the time when the meetup took place, we use the mtp:TimeExpression class. It is composed of start time:hasBeginning and end time:hasEnd dates as well as the text from where it was compiled. Lastly, the purpose of the encounter (mtp:Purpose) is captured by one of the following meetups types: mtp:BusinessCareer, mtp:PersonalLife, mtp:Coincidence, mtp:Education, mtp:PublicCelebration or mtp:MusicMaking.

MMKG is one of the main components of the MEETUPS Pilot.
Here are the links to important components related to the KG.
1. [Meetups Ontology](https://github.com/polifonia-project/meetups-ontology)
2. [Meetups Pilot](https://github.com/polifonia-project/meetups_pilot)
3. [Meetups Corpus Collection](https://github.com/polifonia-project/meetups_corpus_collection)

## Competency questions related to MMKG

The KG answers the CQs formalised as part of the Meetups Ontology knowledge requirements.

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

[SPARQL queries developed to answer a set of CQs](https://github.com/polifonia-project/meetups-knowledge-graph/blob/main/queries/cq-validation-queries-MMKG-resource.sparql)

## Statistics:

To obtain these statistics we build a series of queries available here
```
queries/statistics_query.sparql
```
```
-------------------------------
| key                 | value |
===============================
| "Biographies"       | 33309 |
| "Meetups"           | 45812 |
| "Persons mentioned" | 49170 |
| "Subjects"          | 16748 |
| "Places mentions"   | 7107  |
| "Time expressions"  | 51120 |
-------------------------------
```

It is possible to use SPARQL Anything to generate the same statistics using the CSV-generated
```
$ fx -q queries/statistics.sparql -l data/meetups/
```

## KG quick use

The KG is available in TTL and N-quad format.  
- TTL format: `data/meetups_triples`
- N-quad format: `data/meetups_quads`

Each file in the repository is named after the DBpedia identifier (E.g., 10085.ttl, meaning it contains information regarding Edward Elgar). Triples can be directly uploaded into any non-relational database.

For a list of all the biographies processed please see [list-of-biographies.csv](https://github.com/polifonia-project/meetups-knowledge-graph/blob/main/data/list-of-biographies.csv). Column "s" is the DBpedia resource and column "id" the unique identifier give by DBpedia
```
------------------------------------------------------------
| s	| id	|
============================================================
| "http://dbpedia.org/resource/Edward_Elgar"	| 10085 |
| "http://dbpedia.org/resource/Clara_Schumann"	| 45181 |
| "http://dbpedia.org/resource/Yehudi_Menuhin"	| 57520 |
------------------------------------------------------------
```

### Repository structure

- `data`: contains the KG data in TTL and N-quad format
- `diagrams`: illustrative diagrams of the knowledge extraction process
- `queries`: SPARQL queries for statistics, evaluation, KG construction, miscellaneous

## KG construction

To build the KG from scratch we use SPARQL Anything and CONSTRUCT mappings to create triples for each biography. 
The data used to generate the KG is the evidence (text) that describes an encounter, the entities (people and places), temporal expressions and the purpose of the encounter extracted from a piece of evidence. All this data is the result of the execution of the knowledge construction pipeline detailed in [Meetups Pilot](https://github.com/polifonia-project/meetups-ontology).

### Pre-requirements

- Download and install the SPARQL Anything command line from the [project release page](https://github.com/SPARQL-Anything/sparql.anything/releases).
SPARQL Anything requires Java >= 11. We used the  sparql-anything-0.8.1 version
- Download the CONSTRUCT mapping scripts stored in this repository
	- `queries/generate-meetups-1.sparql`
	- `queries/generate-meetups-2.sparql`
	- `queries/generate-meetups-3.sparql`
- Download the list of biographies stored in this repository
	- `data/list-of-biographies.csv`
- Download the CSV files generated as output of the [Knowledge extraction pipeline](https://github.com/polifonia-project/meetups_pilot) repository. These four folders:
	- [meetupsAnnotations](https://github.com/polifonia-project/meetups_pilot/tree/main/meetupsAnnotations)
 	- [meetupsFastCorefOutputPP](https://github.com/polifonia-project/meetups_pilot/tree/main/meetupsFastCorefOutputPP)
  	- [meetupsTimeExpressions](https://github.com/polifonia-project/meetups_pilot/tree/main/meetupsTimeExpressions)
  	- [extractedMeetupsTypes](https://github.com/polifonia-project/meetups_pilot/tree/main/extractedMeetupsTypes) 

### Commands

Part1. Generates triples about the meetup evidence, people and purpose of the meetup.
```
java -jar sparql-anything-0.8.1.jar -q generate-meetups-1.sparql -i list-of-biographies.csv -p "data/meetups_triples/part1/?fileId.ttl" -f TTL
```
Part2. Generates triples about the meetup places
```
java -jar sparql-anything-0.8.1.jar -q generate-meetups-2.sparql -i list-of-biographies.csv -p "data/meetups_triples/part2/?fileId.ttl" -f TTL
```
Part3. Generates triples about the meetup temporal expressions
```
java -jar sparql-anything-0.8.1.jar -q generate-meetups-3.sparql -i list-of-biographies.csv -p "data/meetups_triples/part3/?fileId.ttl" -f TTL
```

Last step: generate `meetups_quads` from `meetups_triples` and `list-of-biographies.csv`:
```
fx -q queries/generate_nq_each.sparql -v data/list-of-biographies.csv -f NQ -p "./data/meetups_quads/?id.nq"
```

These commands build the whole KG, if you like to build a specific list of biographies from the available ones, just compile a new `list-of-biographies.csv` file and run the scripts.


*Note: be reminded to change any directory names/structure to reflect your settings.

## Meetups KG extraction 

![KG extraction pipeline](diagrams/meetups-pipeline.png?raw=true "KG extraction pipeline")

## MELODY data stories

To be released in the next deliverable


## Acknowledgements

This work was supported by the EU’s Horizon Europe research and innovation
programme within the Polifonia project (grant agreement N. 101004746).
