---
component-id: meetups-corpus
name: MEETUPS Corpus
description: This repository contains the corpus of people in the music scene in Europe
type: Corpus
release-date: 20/07/2022
release-number: v1.0
project: polifonia-project
resource: https://github.com/polifonia-project/meetups_corpus_collection/
work-package:
- WP4
pilot:
- MEETUPS
licence: 
- Apache-2.0
release link:
  - https://github.com/polifonia-project/meetups_corpus_collection/releases/tag/v1.0
contributors:
  - https://github.com/albamoralest
related-components:
- generated-by: 
  - meetups-corpus-collection
---

# MEETUPS Corpus collection

[![DOI](https://zenodo.org/badge/504547694.svg)](https://zenodo.org/badge/latestdoi/504547694)

### Collecting Wikipedia pages of people in the music scene in Europe

#### Details of dataset

SPARQL queries to retrieve authors' names and dbo:wikiPageID information using Dbpedia SPARQL Endpoint https://dbpedia.org/sparql

Query filters:
  
    Categories: <http://dbpedia.org/resource/Category:Music_people>
                <http://dbpedia.org/resource/Category:People
    Location:
                sparqlQueryResults/query.sparql
    Query results"
                sparqlQueryResults/Q<1>_sparql.csv

Dataset:
    
    Location:
                dataset/
    Format:
                Text files .txt
    Name convention:
                <Author_wikiPageID>.txt
    Total biographies collected: 
                33,309 authors wikipedia webpage
    Summary total biographies collected: 
                sparqlQueryResults/TOTAL_download_biography.csv
    Meetups pilot sample: 1.002

Select random biographies -> sampleBiographies.py
