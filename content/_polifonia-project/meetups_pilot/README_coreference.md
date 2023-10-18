---
component-id: meetups-coreference
type: Software
name: MEETUPS - Identification of temporal knowledge
description: "This tool is part of the MEETUPS pilot and executes the coreference resolution task. It is in charge of identifying mentions to entities in the form of noun phrase, named, or pronominal text, particularly people and places. This software supports the identification of missing entities during the entity recognition and linking task and leverages the possibility of identifying historical meetups. Furthermore, the software tool validates that these mentions refer to the a named entity and link them to DBpedia or Wikipedia resources."
work-package:
- WP4
pilot:
- MEETUPS
project: polifonia-project
resource: https://github.com/polifonia-project/meetups_pilot/blob/main/05_Coreference.ipynb
release-date: 31/08/2023
release-number: v0.1
release-link: https://github.com/polifonia-project/meetups_pilot/releases/tag/v0.2
doi: 10.5281/zenodo.7875353
changelog: https://github.com/polifonia-project/meetups_pilot/releases/tag/v0.2
licence: 
- Apache-2.0
copyright: "Copyright (c) 2023 MEETUPS @ The Open University"
contributors:
- Alba Morales Tirado <https://github.com/albamoralest>
- Enrico Daga <https://github.com/enridaga>
related-components:
- informed-by: 
  - meetups-entity-recognition
  - meetups-time-extraction
  - meetups-themes
---

# MEETUPS - coreference resolution

This tool is part of the MEETUPS pilot and executes the coreference resolution task. It is in charge of identifying mentions to entities in the form of noun phrase, named, or pronominal text, particularly people and places. This software supports the identification of missing entities during the entity recognition and linking task and leverages the possibility of identifying historical meetups. Furthermore, the software tool validates that these mentions refer to the a named entity and link them to DBpedia or Wikipedia resources.


This component processes text at paragraph level and annotates entities at sentence and paragraph level. It is developed using Python and uses the spaCy library https://spacy.io/universe/project/coreferee/. 
This library can be integrated as a plugin in the spaCy's pipeline for Natural Language Processing. The coreferee library resolves coreferences within English text and uses a mixture of neural networks and programmed rules https://github.com/richardpaulhudson/coreferee.
Furthermore, this component validated the named entity exists and link it to a DBpedia or Wikipedia resource.

### Information on installation and setup

  - Jupyter Notebook:
    05_Coreference.ipynb
    
### Details of the data

    Code location:
    |_ 05_Coreference.ipynb
    
    Data input:
    |_ indexedSentences/
    
    Coreference annotations
    Data ouput:
    |_ meetupsCorefOutputPP/        

    
    |_ README_meetups-coreference.md
    

