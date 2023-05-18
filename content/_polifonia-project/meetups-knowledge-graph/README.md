---
component-id: meetups-knowledge-graph
name: MEETUPS Knowledge Graph
brief-description: MEETUPS Knowledge Graph module with data on historical meetups and related to MEETUPS Pilot
type: Repository
release-date: 20/07/2022
release-number: v0.1
work-package:
- WP4
pilot:
- MEETUPS
licence: CC BY
related-component:
- meetups-data-cleaning
- meetups-themes
- meetups-entity-recognition
- meetups-time-extraction
- meetups-corpus-collection
release link:
- https://github.com/polifonia-project/meetups-knowledge-graph/releases/tag/v0.1
credits:
- https://github.com/albamoralest
- https://github.com/enridaga
---

# MEETUPS Knowledge Graph

[![DOI](https://zenodo.org/badge/588597123.svg)](https://zenodo.org/badge/latestdoi/588597123)

The MEETUPS knowledge graph contains data about historical encounters of people in the musical world in Europe from c. 1800 to c. 1945.


## Knowledge Graph description

All the data is extracted from artists' biographies, mainly from open-access digital sources such as Wikipedia artists' web pages.
A total of 33,309 biographies were collected for knowledge extraction and construction of the KG.
Currently, the KG contains data on the data extraction of 1000 biographies in the next deliverable. The KG will include data on the total number of biographies collected.

## Competency questions related to MEETUPS ontology module
Ortenz
- What places did musician Z visited in her career?
- Where did she perform?
- Where did she live?
- Did musician X and performer Y ever meet? Where, when, and why?
- In what context the meeting happened?
- What is the nature of the event?
- Was it a celebration, a festival, a private event?
- Was it a religious or a secular event?
- Who paid to support the event?
- What is the provenance of the event attendees? What and how they happened to be there?
- Did they travel to reach the place?
- Were they invited? Was the meeting accidental?
- How can we characterize the relation among the participants?
- Was there a power relation? (e.g., Patreon / Musician)

## Statistics:
```
$ fx -q queries/statistics.sparql -l data/meetups/
-------------------------------
| key                 | value |
===============================
| "Meetups"           | 74445 |
| "Persons mentioned" | 51425 |
| "Subjects"          | 1002  |
| "Places mentions"   | 5595  |
| "Time expressions"  | 79838 |
-------------------------------
```

## MELODY data stories

To be released in next deliverable

## Additional information  
### Queries and usage

Generate list of biographies and related files.
```
fx -q queries/list-sample.sparql -o data/biographies.csv -f CSV
```
Generate sentences KG data
```
fx -q queries/sentences.sparql -i data/biographies.csv -p "data/sentences/?fileId.ttl" -f TTL
```


[part above to be updated...]

```
fx -q queries/sentences.sparql -v fileId=10085 -v subject=http://dbpedia.org/resource/Edward_Elgar
```
