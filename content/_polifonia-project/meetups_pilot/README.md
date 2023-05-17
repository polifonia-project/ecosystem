---
component-id: meetups-knowledge-extraction
name: MEETUPS Knowledge Extraction
brief-description: Dataset for experiments within the MEETUPS Pilot
type: Software
release-date: 20/07/2022
release-number: v0.1
work-package: 
- WP4
pilot:
- MEETUPS
licence: Apache 2.0
related-component:
- meetups-data-cleaning
- meetups-themes
- meetups-entity-recognition
- meetups-time-extraction
- meetups-corpus-collection
release link:
- https://github.com/polifonia-project/meetups_pilot/releases/tag/v0.1
credits:
- https://github.com/albamoralest
- https://github.com/enridaga
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
