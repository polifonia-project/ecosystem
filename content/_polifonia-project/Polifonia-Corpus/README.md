---
component-id: Polifonia-Corpus
name: Polifonia Corpus
description: Data, metadata, statistics, annotations and interrogation APIs of the Polifonia Textual Corpus.
type: Corpus
release-date: 28/06/2022
release-number: v0.1.3
work-package: 
- WP4
licence:
- CC-BY_v4
related-components:
- persona:
  - Valeriana
  - Carolina
- reuses:
  - Polifonia-Lexicon
bibliography:
- deliverable-document: "D4.2 Interrogation and annotation of plurilingual corpora for discourse analysis"
contributors:
- https://github.com/roccotrip
- https://github.com/arianna-graciotti
- https://github.com/EleonoraMarzi
---

# Polifonia Textual Corpus

This repository contains the script to access, parse, annotate and interrogate the data and metadata of the Polifonia Textual Corpus.

The high level structure of the repository is the following:

```
Polifonia-Corpus
│   README.md
│   wikipedia_corpus_parser.py
|   wikipedia_corpus_reader.py    
│
└───annotations
│   │   README.md
│   │
│   └───db
│       │   Wikipedia_EN.db
│       │   Periodicals_EN.db
│       │   Books_EN.db
|       |   ........
|       |   "Module"_"Lang".db
│   
└───interrogation
|   │   README.md
|   │   interrogate.py
|   |
|   |___data
|       |   lex_ent_map.pkl
|       |   pages.pkl
|
|___utils
    |   db_utils.py
```

The root folder contains the script to access and parse the Polifonia Corpus data and metadata that are linked in this README.md file.

The annotations folder contains a README.md file in which it is explained how the corpus was annotated. A "db" subfolder of the "annotations" folder is set up to store the databases with the annotations of the corpus that will be used for the interrogations of the corpus. The databases will be downloaded automatically the first time each module will be queried. The links for the download are listed in the "urls.csv" file.

The interrogation folder contains a README.md file that explain how to interrogate the corpus. It contains a "data" subfolder used to link mentions, named entities and Wikipedia page titles.

## The corpus

The corpus is dived into four modules:
- the Wikipedia module
- the Books module
- the Periodicals module
- the Polifonia Pilots module

Each module (except the Pilot module) contains documents in six languages: Dutch (NL), English (EN), French (FR), German (DE),Italian (IT) and Spanish (ES). 

### The Wikipedia module
It was created selecting from **[BabelNet domains](http://lcl.uniroma1.it/babeldomains/)** all the **[Wikipedia](https://www.wikipedia.org)** musical pages.

#### Metadata
The metadata of the module can be downloaded from:

|  lang |  url                                                                                                      |  
|-------|-----------------------------------------------------------------------------------------------------------|
| DE    | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671494.svg)](https://doi.org/10.5281/zenodo.6671494) |
| EN    | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671510.svg)](https://doi.org/10.5281/zenodo.6671510) |
| ES    | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6670984.svg)](https://doi.org/10.5281/zenodo.6670984) |
| FR    | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671560.svg)](https://doi.org/10.5281/zenodo.6671560) |
| IT    | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671571.svg)](https://doi.org/10.5281/zenodo.6671571) |
| NL    | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671519.svg)](https://doi.org/10.5281/zenodo.6671519) |

#### Data

The data of the module can be downloaded from:

| lang | url           | 
|------|----------------|
| DE   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671663.svg)](https://doi.org/10.5281/zenodo.6671663)|
| EN   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671681.svg)](https://doi.org/10.5281/zenodo.6671681)|
| ES   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671673.svg)](https://doi.org/10.5281/zenodo.6671673)|
| FR   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671728.svg)](https://doi.org/10.5281/zenodo.6671728)|
| IT   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671734.svg)](https://doi.org/10.5281/zenodo.6671734)|
| NL   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671738.svg)](https://doi.org/10.5281/zenodo.6671738)|


#### Statistics

Some statistics of the module are provided below:

| lang | #documents | #sentences | #tokens | #types | #links | entities |
|------|------------|------------|---------|---------|------------|---------|
| DE   | 53.986 | 1.459.265 | 44.523.547 | 9.732.779 | 12.561.177 | 2.197.438| 
| EN   | 250.413 | 7.362.272 | 198.257.649 | 1.191.901 | 54.059.979 | 25.786.043 |
| ES   | 57.891 | 1.247.583 | 36.229.557 | 537.465 | 7.171.759 | 2.996.185 |
| FR   | 65.970 | 2.901.295 | 82.979.944 | 653.489 | 19.208.818 | 6.212.997 |
| IT   | 77.986 | 1.548.981 | 47.497.487 | 491.500 | 14.519.636 | 2.649.949 |
| NL   | 36.609 | 1.246.881 | 23.539.528 | 479.962 | 4.716.170 | 2.453.332 |

### The Books module
It was created using the **[Polifonia Textual Corpus Population](https://github.com/polifonia-project/textual-corpus-population)** module that allows to access different digital libraries (such as **[BNF](https://gallica.bnf.fr)** and **[BNE](http://www.bne.es)**) and to select from them documents related to music. The PTCPM allows also to perform optical character recognition (OCR) on images and PDF files. 

#### Metadata
The metadata of the module can be downloaded from:

| lang | url                                                                                                      |
|------|-----------------------------------------------------------------------------------------------------------|
| DE   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6772115.svg)](https://doi.org/10.5281/zenodo.6772115) |
| EN   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6772136.svg)](https://doi.org/10.5281/zenodo.6772136) |
| ES   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6772131.svg)](https://doi.org/10.5281/zenodo.6772131) |
| FR   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6772142.svg)](https://doi.org/10.5281/zenodo.6772142) |
| IT   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6772137.svg)](https://doi.org/10.5281/zenodo.6772137) |
| NL   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6772145.svg)](https://doi.org/10.5281/zenodo.6772145) | 

#### Data

The data of the module cannot be downloaded due to copyright issue.
However, it is possible to reconstruct the corpus using the metadata provided in the previous section.
Furthermore, the data processed and annotated can be accessed interrogating the corpus (how to interrogate the corpus is explained in a README.md file inside the interrogation folder of this repository).


#### Statistics

Some statistics of the module are provided below:

| lang | #documents | #sentences | #types    | #tokens    |
| ------ |------------|------------|-----------|------------|
| DE | 237        | 38.633     | 121.530   | 489.225    | 
| EN | 360        | 49.595     | 185.280   | 940.232    | 
| ES | 41.093     | 731.606    | 1.852.430 | 20.180.197 | 
| FR | 265        | 633.173    | 1.305.283 | 14.354.611 | 
| IT | 12200      | 202.730    | 405.099   | 2.571.090  | 
| NL | 83         | 116.593    | 539.102   | 1.779.824  | 

### The Periodicals module
It was created with the help of musicologists that provided the titles of different influencial music periodicals.

#### Metadata
The metadata of the module can be downloaded from:

| lang | url                                                                                                                                                                                                  | 
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DE   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6761779.svg)](https://doi.org/10.5281/zenodo.6761779)|
| EN   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6671912.svg)](https://doi.org/10.5281/zenodo.6671912)|
| ES   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6761787.svg)](https://doi.org/10.5281/zenodo.6761787)|
| FR   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6761794.svg)](https://doi.org/10.5281/zenodo.6761794)|
| IT   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6761806.svg)](https://doi.org/10.5281/zenodo.6761806)|
| NL   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6761809.svg)](https://doi.org/10.5281/zenodo.6761809)|

#### Data

The data of the module cannot be downloaded due to copyright issue.
However, it is possible to reconstruct the corpus using the metadata provided in the previous section.
Furthermore, the data processed and annotated can be accessed interrogating the corpus (how to interrogate the corpus is explained in a README.md file inside the interrogation folder of this repository).


#### Statistics

Some statistics of the module are provided below:


| lang | #documents | #sentences | #types    | #tokens    |
| ------ |------------|------------|-----------|------------|
| DE | 705        | 121.113    | 544.376   | 2.405.289  | 
| EN | 2.868      | 4.400.015  | 7.342.527 | 76.180.398 | 
| ES | 455        | 87.025     | 677.041   | 3.170.480  | 
| FR | 349        | 329.166    | 696.427   | 5.111.915  | 
| IT | 1.251      | 433.465    | 992.902   | 7.879.459  | 
| NL | 125        | 187.350    | 716.506   | 3.880.499  | 


### The Polifonia Pilots module
It was created collecting the textual material selected by five **[Polifonia Pilots](https://polifonia-project.eu/pilots/)**:
- BELLS
- CHILD
- MEETUPS
- MUSICBO
- ORGANS

#### Metadata
The metadata of the module can be downloaded from:

| Pilot   | url     |
|---------|---------|
| BELLS   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6672061.svg)](https://doi.org/10.5281/zenodo.6672061)|
| CHILD   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6672093.svg)](https://doi.org/10.5281/zenodo.6672093)|
| MEETUPS | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6672133.svg)](https://doi.org/10.5281/zenodo.6672133)|
| MUSICBO | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6672165.svg)](https://doi.org/10.5281/zenodo.6672165)|
| ORGANS  | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6672193.svg)](https://doi.org/10.5281/zenodo.6672193)|


#### Data

The data of the Pilots Module of the Polifonia textual Corpus collected for Bells, MusicBo and Organs pilots cannot be published in their integral form because they are subject to heterogeneous license restrictions. The respective set of published metadata (see table above) allows for the reproduction of the whole corpora. Texts collected for Child and Meetups Pilots are royalty-free, therefore we report links to retrieve them from their corresponding GitHub repositories:

| Pilot   | url     |
|---------|---------|
| CHILD   | https://github.com/polifonia-project/documentary-evidence-benchmark/tree/main/corpus |
| MEETUPS | https://github.com/polifonia-project/meetups_pilot/tree/main/cleanText |

However, it is possible to reconstruct the corpus using the metadata provided in the previous section.
Furthermore, the data processed and annotated can be accessed interrogating the corpus (how to interrogate the corpus is explained in a README.md file inside the interrogation folder of this repository).


#### Statistics

Some statistics of the module are provided below:

| pilot   | #documents | #sentences | #types    | #tokens    |
|---------|------------|------------|-----------|------------|
| BELLS   | 59         | 18.481     | 128.061   | 434.439    | 
| CHILD   | 30         | 157.815    | 361.550   | 3.442.840  | 
| MEETUPS | 19.476     | 822.861    | 1.631.371 | 21.536.135 | 
| MUSICBO | 46         | 51.781     | 289.247   | 1.412.456  | 
| ORGANS  | 1.660      | 25.647     | 45.298    | 368.439    | 


