---
component-id: meetups-time-extraction
name: MEETUPS - Identification of temporal knowledge
brief-description: "This tool is part of the MEETUPS pilot and processes text from music personalities' biographies to find time expressions. It uses NLTK and a set of heuristic rules to identify and annotate temporal knowledge from text. The tool extracts information from one out of the four elements that define a meetup: the date or moment in time when it happened (when). Time expressions, along with data of the people involved (who), the place (where) and the event that took place (what), complete the historical meetup information."
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
- Natural Language processing
- Time expressions
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

# MEETUPS 

MEETUPS identification of temporal knowledge is a tool developed using Python and Jupyter Notebook. This software uses NLTK Toolkit and heuristic rules to identify and annotate time expressions from input text. The tool allows the extraction of one (when a historical meetup happened) of the four elements that define a historical meetup. 

This implementation is a rule-based Time Expression recognition tagger based on research by Zhong et al. and SynTime software (https://github.com/zhongxiaoshi/syntime). Their work was originally tested using three datasets: TimeBank, WikiWars and Tweets. 
The authors implement a three-layer system that recognises time expressions using syntactic token types and general heuristic rules.

First layer - token identification:
 - Annotate tokes with POS tags, we use NLTK. In SynTime they used CoreNLP.
 - Annotate tokes according time tokens proposed by Zhong et al.
    Three types of tokens: TIME, MODIFIER, NUMERAL.
        Each type have more specific types:
        MODIFIER = ["PREFIX","SUFFIX","LINKAGE","COMMA","PARENTHESIS","INARTICLE"]
        NUMERAL = ["BASIC","DIGIT","ORDINAL"]
        TIME = ["DECADE", "YEAR", "SEASON", "MONTH", "WEEK", "DATE", "TIME", "DAY_TIME", "TIMELINE", "HOLIDAY", "PERIOD", "DURATION", "TIME_UNIT","TIME_ZONE", "ERA","MID","TIME_ZONE","DAY","HALFDAY"]
    *In our implementation we add the type PARENTHESIS and improve regular expressions

Second layer - time segment identification:
 - Search the surroundings of each time token identified previously for modifiers and numerals
 - Gather the time token with its modifiers and numerals and form a time segment
 - The search is under heuristic rules
    Search tokens on the left 
       If PREFIX or NUMERAL or IN_ARTICLE continue searching
    Search tokens on the right 
       If SUFIX or NUMERAL continue searching
    For right and left search, if token is COMMA or LINKAGE then stop
    

Third layer - time expression extraction
    If time segments overlap, then apply heuristic rules and merge segments
    
Time expressions classification:
    We add a step and classify time expressions according to literature
    - Time range: generally, one or two bounds, e.g., from XX to XX, from XX, to XX, until XX. 
    - Time point: exact date and or time description 23/03/1294 
    - Time reference: usually incomplete dates (19 April), 2 weeks, later this year, relative to the document (the author’s date of birth? Sentence context? For later)  

Finally the tool stores the results as a CSV file in extractedTimeExpressions/


### Information on installation and setup

  - Jupyter Notebook:
    03_Identify_TimeE.ipynb
    
### Details of the data

    Code location:
    |_ 03_Identify_TimeE.ipynb
    
    Regular expressions:
    |_ timeRegex.txt
    
    Data location
    
    Data input:
    |_ indexedSentences/
    
    Time expressions annotations
    Data ouput:
    |_ extractedTimeExpressions/        

    
    |_ README_people_places_identification.md
    

### DOI:

    TODO