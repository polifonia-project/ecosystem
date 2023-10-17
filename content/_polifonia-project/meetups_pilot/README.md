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

Extracting information of musical artist from Wikipedia pages.

The initial collection of Wikipedia pages can be found here: https://github.com/albamoralest/scrappingWikipediaMusicBiographies

In this pilot we extract people, places, events and time entities from 1002 wikipedia pages.

Step 1: cleaning and organising information by sentences

Step 2:
  
  2.1 extracting entities using DBpedia spotlight
  
  2.2 extracting time expressions using nltk
  
The dataset is organised by folders:

The folder extractedEntities contains the final result of the extraction pipeline

Here you will find a csv named by the wikipedia id of the authors. In the file "infoBiographies.csv" you will find the name of the person related with the wikipedia page, the date of birth


![MEETUPS software-tools](https://github.com/polifonia-project/meetups-knowledge-graph/blob/main/meetups-software_tools.png?raw=true "MEETUPS software tools by task")