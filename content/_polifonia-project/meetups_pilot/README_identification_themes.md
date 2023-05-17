---
component-id: meetups-themes
name: MEETUPS - Identification of themes
brief-description: "This tool is part of the MEETUPS pilot and processes text from music personalities' biographies to find encounter types. It uses \"sklearn\" and a set of Machine Learning algorithms to classify sentences according to the established type of events. The tool extracts information from one of the four elements defining a meetup: the type of encounter (what). Encounter type, along with data of the people involved (who), the place (where) and the time it took place (what), complete the historical meetup information."
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
- Text classification
- Encounter type
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
  - https://github.com/enridaga
  - https://github.com/albamoralest
---

# MEETUPS - Identification of themes

MEETUPS identification of people and places is a tool developed using Python and Jupyter Notebook. SKLEARN and a set of Machine Learning algorithms to classify sentences according to the established type of events. The tool allows the extraction of one (the type of encounter) of the four elements that define a historical meetup. 
The encounter types are music-making, business meetings, personal life, social life, coincidence, public celebration, and education. 

This implementation is divided in three main tasks:
a) Generation of the training dataset
In order to identify and classify sentences according to the encounter type we need first to build a dataset with sentences that describe the different encounter types.
Approach:
- Manually prepare seed terms for each meetup type
- Randomly select sentences with those words from the corpus
- Assign the relevant meetup type to each one of those sentences

b) Training the classifier
Approach:
- Build a balanced training set by selecting first sentences from low represented classes
- Train and test MLPClassifier

c) Applying the classifier
Use the model tested in b) and infer the type of encounter for all the data in the corpus

### Information on installation and setup

  - Jupyter Notebook:
    MeetupType_applyClassifier.ipynb
    
### Details of the data

    Running the Themes classifier:
    |_ MeetupType_applyClassifier.ipynb
    
    Training the Themes classifier:
    |_ MeetupType_prototypeSentences.ipynb
    
    Generating the training dataset:
    |_ MeetupType_trainClassifier.ipynb
    
    Data location
    
    Data input:
    |_ indexedSentences/
    
    Data output:
    |_ extractedMeetupTypes/        

    Classifier:
    meetupType/models/MLPClassifier_2.clf'
    
    Prototype sentences:
    |_ meetupType/prototypeSentences_*.csv
    
    
    |_ README_identification_themes.md
    

### DOI:

    TODO
