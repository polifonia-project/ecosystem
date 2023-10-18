---
component-id: meetups-corpus-collection
name: MEETUPS Corpus collection
description: This is a tool to download the Wikipedia pages of people in the music scene in Europe
type: Software
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
- informed-by: 
  - meetups-corpus
---

# MEETUPS Corpus collection

[![DOI](https://zenodo.org/badge/504547694.svg)](https://zenodo.org/badge/latestdoi/504547694)

### Collecting Wikipedia pages of people in the music scene in Europe


MEETUPS Corpus collection is a tool developed in Python and PyCharm IDE. It collects Wikipedia web pages (in txt format) of music authors in Europe.

- Uses the "wikipedia" library to download only wikipedia webpage text
- Process the list of files in chunks of 100 units
- The process can start and stop any time as it controls the last downloaded item


#### Information on installation and setup

- Pre-requirements:
  - A CSV file with the list of authors' wikipedia id and store in sparqlQueryResults/ directory
  - Python 3.9
- Install wikipedia library:
  - pip install wikipedia
- To execute:
  - Download project and execute __init__.py file

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

