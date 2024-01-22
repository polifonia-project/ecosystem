---
container-id: meetups-pilot
name: Musical MEETUPS
type: Project
description: MEETUPS Pilot container with all the elements that support the knowledge extraction of historical meetups
work-package: 
- WP4
pilot:
- MEETUPS
project: polifonia-project
bibliography:
- main-publication: "Morales Tirado, Alba; Carvalho, Jason; Mulholland, Paul and Daga, Enrico (2023). Musical Meetups: a Knowledge Graph approach for Historical Social Network Analysis. In: Proceedings of the ESWC 2023 Workshops and Tutorials, Semantic Methods for Events and Stories (SEMMES)."
funder:
- name: European Commission H2020
  url: https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/programmes/h2020
  grant-agreement: GA101004746
credits: "This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement GA101004746. The communication reflects only the author’s view and the Research Executive Agency is not responsible for any use that may be made of the information it contains."
has-part:
- meetups-knowledge-graph
- meetups-ontology
- meetups-data-cleaning
- meetups-themes
- meetups-entity-recognition
- meetups-time-extraction
- meetups-corpus-collection
- meetups-coreference
- meetups-hm-identification
---

# MEETUPS PILOT

[![DOI](https://zenodo.org/badge/436452967.svg)](https://zenodo.org/badge/latestdoi/436452967)

## People and music: exploring their encounters over centuries

This pilot focuses on supporting music historians and teachers by providing a Web tool that enables the exploration and visualisation of encounters between people in the musical world in Europe from c.1800 to c.1945, relying on information extracted from public domain books such as biographies, memoirs and travel writing, and open-access databases. These encounters will be explored in a timeline and map interface and may reveal unexpected connections and relationships that cast new light on aspects of European music history. The tool will provide persistent, citable identifiers in order to support referencing in scholarship outputs.

## Description

In this pilot, we extract people, places, events and time entities from 33.309 Wikipedia pages.

Components related to the KG.
1. [Meetups Ontology](https://github.com/polifonia-project/meetups-ontology). The framework to build the Musical Meetups Knowledge Graph. The Meetups Pilot focuses on extracting data related to collaborations between people in the musical world. The main aim is to facilitate the exploring and discovering of these connections between people by characterising evidence (usually found in textual resources) with dimensions that are relevant to the scholarly enquiry such as the actual participants, the place they met, the nature of the event and the date it took place.
The Meetups Ontology describes the concept of `historical meetup` to represent the collaborations between personalities of European musical history and formalises its constituent parts as an ontology.  
2. [Musical Meetups Knowledge Graph (MMKG)](https://github.com/polifonia-project/meetups-knowledge-graph). It contains the structured data extracted using a knowledge extraction pipeline to obtain evidence of artists' encounters throughout history. 
3. [Meetups Corpus Collection](https://github.com/polifonia-project/meetups_corpus_collection). Corpus containing Wikipedia pages collected in text format, a total of 33.309 personalities of the music world.

## Meetups Knowledge Extraction description

![KG extraction pipeline](https://github.com/polifonia-project/meetups-knowledge-graph/blob/17bbb79cf1ee3f7c04ab9a60a339b350cf6fe1b7/diagrams/meetups-pipeline.png "KG extraction pipeline")

1. Data collection & preparation. The biographies of 33.309 personalities were collected from Wikipedia. The text was cleaned by removing empty spaces, redundant line breaks and special characters. The corpus is organised in indexed sentences for each biography.

2. Entity recognition

   2.1. Identification of people and place entities. We use the DBpedia Spotlight5 tool to automatically annotate mentions of people and places linking them to DBpedia resources. We filter entities using the following types: `wikidata:Q41176`, `wikidata:Q486972`, `dbo:Place`, `dbo:Location` or `wikidata:Q6256`. For people, types should be one of `dbo:Person`, `wikidata:Q215627` or `dbo:MusicalArtist`.

   2.2. Identification and normalisation of temporal expressions. This task is divided into two parts: (a) identification of temporal expressions and (b) normalisation. To (a) extract temporal expressions from text, we use a rule-based tagger, established on the implementation of SynTime. To (b) normalise temporal expressions into an XSD date time compliant format we consider time as ranges, with a start and end time point. We follow the ISO86017 format (YYYY-MM-DD) using two Python libraries (dateutil and approx-dates). To cope with cases where normalisation could not be done using Python libraries we we make use of ChatGPT to increase the number of temporal expressions parsed.

   2.3. Identification of meeting purpose. Our pipeline included a Machine Learning approach that follows a semi-supervised classification process, annotating each sentence in the corpus and assigning them one of the meetup types. We use of the LLM tool ChatGPT
to increase the accuracy of the automatic classification. We followed a zero-shot learning approach meaning we provided as input the piece of text to analyse, and the list of classes. We ask the tool to return the two classes that better describe the meetup type. 

3. Harmonisation.

   3.1. Coreference. We use the Python library fastcoref. The library receives as input a paragraph text, then it identifies the entities’ mentions (person or a place) and groups them into chains of mentions. New entities are added when implicit mentions are found in the text.

   3.2. Identification of historical meetups. At this stage, we have a dataset of sentences, each of them including zero or more entity types (people, place, temporal expressions and meetup type). However, a historical meetup can be described in consecutive sentences, having complementary information. We harmonise the data by joining adjacent sentences representing the same social interaction.

4. Knowledge Graph Construction. The KG was constructed using the CSV files resulting from the process described so far and applying the Meetups ontology. We use SPARQL Anything and design CONSTRUCT mappings, to create triples from each biography.

![MEETUPS software-tools](https://github.com/polifonia-project/meetups-knowledge-graph/blob/b993d1650df723723801673d0fa220de0d962b22/diagrams/meetups-software_tools.png)

## Pilot resources

### MMKG SPARQL Endpoint
```
https://polifonia.kmi.open.ac.uk/meetups/sparql/
```
### Web Interface for exploration of historical meetups
```
https://polifonia.kmi.open.ac.uk/MEETUPS/index.php
```

## Repository organisation

The folder extractedEntities contains the final result of the extraction pipeline

Here you will find a csv named by the wikipedia id of the authors. In the file "infoBiographies.csv" you will find the name of the person related with the wikipedia page, the date of birth


## Acknowledgements

This work was supported by the EU’s Horizon Europe research and innovation programme within the Polifonia project (grant agreement N. 101004746).
