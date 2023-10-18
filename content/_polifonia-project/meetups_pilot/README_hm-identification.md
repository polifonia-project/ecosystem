---
component-id: meetups-hm-identification
type: Software
name: MEETUPS - Historical meetups identification
description: "MEETUPS Historical meetups identification was developed using Python and Jupyter Notebook. As input it uses the bag of entities obtained from the Entity Recognition and Coreference steps. The output is a corpus that contains the text (typically a sentence or a set of sentences), and the list of entities that account for a meetup. The results are stored in CSV files, grouped by biographies. The corpus is used later to build the MEETUPS KG."
work-package:
- WP4
pilot:
- MEETUPS
project: polifonia-project
resource: https://github.com/polifonia-project/meetups_pilot/blob/main/06_Coreference.ipynb
release-date: 31/08/2023
release-number: v0.1
release-link: https://github.com/polifonia-project/meetups_pilot/releases/tag/v0.2
doi: 10.5281/zenodo.7875353
changelog: https://github.com/polifonia-project/meetups_pilot/releases/tag/v0.3
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
  - meetups-coreference
---

# MEETUPS - Historical meetups identification

This tool is part of the MEETUPS pilot and processes text from music personalities' biographies to identify historical meetups. The software component gathers the output produced by the tools of Entity Recognition and Coreference \& meetups annotation steps (see Figure) and runs an automatic evaluation to identify if elements that define a historical meetup are present in a piece of text. 
        
![MEETUPS software-tools](https://github.com/polifonia-project/meetups-knowledge-graph/blob/main/meetups-software_tools.png?raw=true "MEETUPS software tools by task")

First, the tool examines each piece of text, at sentence level, and evaluates if all the entity types are present. 
Sentences that comply with this requirement are automatically annotated as a historical meetup. 
All the sentences that have one or more entity type missing are annotated temporarily as a historical trace. The next step is to search for complementary information within the same paragraph and potentially identify more historical meetups.
        
The algorithm searches for missing entities in previous sentences within the same paragraph, the aim is to group two or more consecutive sentences that refer to the same event and among them feed all the required entity types of a historical meetup. These sentences should refer to the same type of encounter in order to be considered and not have been previously annotated as a historical meetup.

MEETUPS Historical meetups identification was developed using Python and Jupyter Notebook. As input it uses the bag of entities obtained from the Entity Recognition and Coreference steps. The output is a corpus that contains the text (typically a sentence or a set of sentences), and the list of entities that account for a meetup. The results are stored in CSV files, grouped by biographies. The corpus is used later to build the MEETUPS KG.

### Information on installation and setup

  - Jupyter Notebook:
    06_MeetupsIdentification.ipynb
    
### Details of the data

    Code location:
    |_ 06_MeetupsIdentification.ipynb
    
    Data input:
    |_ indexedSentences/
    
    Historical meetups annotations
    Data ouput:
    |_ meetupsIdentification/        

    
    |_ README_hm-identification.md
    

