---
component-id: meetups-data-cleaning
name: MEETUPS preparation - data cleaning
brief-description: This tool is part of the corpus preparation process and it is used to clean data collected from Wikipedia. 
type: Software
release-date: 20/07/2022
release-number: v0.1
work-package:
- WP4
pilot:
- MEETUPS
keywords:
- Wikipedia
- Music
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

# MEETUPS Corpus preparation: data cleaning
### MEETUPS Corpus preparation: Cleaning data collected from Wikipedia web pages of people in the music scene in Europe


MEETUPS data cleaning is a tool developed using Python and Jupyter Notebook. This software prepares the biographies (collected as text files) in https://github.com/polifonia-project/meetups_corpus_collection for the next step in the extraction of historical meetups process.

- Use the Wikipedia authors' webpages collected in https://github.com/polifonia-project/meetups_corpus_collection
- Clean text blank lines, sections with no historical meetups data
- Organise the text in sentences as the main unit to extract meetups information


#### Information on installation and setup

  - Run Jupyter Notebook 01_CleaningText.ipynb

#### Details of the data

    Code location:
    
    |_ 01_CleaningText.ipynb
    
    Raw corpus location
    Data output:
    |_ text_dataset/            
    
    Clean text location
    Data input:
    |_ cleanText/
    
    Index data location
    Data output:
    |_ indexedParagraphs/
    |_ indexedSentences/
    
    |_ README_data_cleaning.md
    

DOI:

    TODO