---
component-id: data-wanderings
type: Software
name: Polifonia Data Wanderings
description: Source code of the Polifonia Data Wanderings Art Installation
work-package: 
- WP1
- WP6
licence:
- CC-BY_v4
project: polifonia-project
contributors:
- Alex Piacentini <https://alexpiacentini.com>
- Filippo Rosati
- Andrea Poltronieri
- Jacopo de Berardinis  
- Federica Patti  
---

# Data Wanderings

Data Wanderings is an audiovisual installation created as part of Polifonia, a research project funded by the Europe Horizon 2020 program.

![preview](https://github.com/piaaaac/polifonia-data-wanderings/blob/main/documentation/polifonia-data-wanderings-5.png?raw=true)

## Creation process

### 1. Data extraction

Data wanderings uses data extracted from the [Choco](https://github.com/smashub/choco) database.
Specifically, a collection of 20861 records representing the timed chord sequences played in songs analyzed in the context of the Polifonia project. The data is divided in csv files of 2000 records and available in the folder `choco_data--chords`.

The data has been extracted using queries like:

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX jams: <http://w3id.org/polifonia/ontology/jams/>
PREFIX mm: <http://w3id.org/polifonia/ontology/music-entity/>
PREFIX core: <http://w3id.org/polifonia/ontology/core/>

SELECT DISTINCT ?title ?musicentity ?observationValue ?startTime ?startTimeType ?duration ?durationType
WHERE {
  ?musicentity a mm:MusicEntity ;
    core:title ?title ;
    jams:hasJAMSAnnotation ?annotation .
  ?annotation jams:includesObservation ?observation ;
    jams:hasAnnotationType "chord" .
  ?observation rdfs:label ?observationValue ;
    jams:hasMusicTimeInterval [jams:hasMusicTimeDuration [ jams:hasValue ?duration ; jams:hasValueType ?durationType ] ;
      jams:hasMusicTimeStartIndex [ jams:hasMusicTimeIndexComponent [ jams:hasValue ?startTime ; jams:hasValueType ?startTimeType  ]]] .
}
ORDER BY ?title ?startTime
LIMIT 1000
OFFSET 0
```

### 2. Data manipulation and enrichment

The following step has been translating the chord names into data that was usable to create a generative and interactive installation. The chords have been processed using the [Harte](https://github.com/andreamust/harte-library) library, resulting in corrispondences of chords with notes and sound frequencies, available in the file `chords_notes_frequencies.tsv`.

### 3. Data utilization

The data is fed in a system composed of a Touchdesigner patch and a Max-MSP patch, that read a random sequence of songs and transform their chord data in a generative audio-visual interactive composition. The Touchdesigner patch reads the note sequences and sends data to Max via the OSC protocol. User interaction is implemented using the input of a webcam. The live feed is analyzed to read the intensity of the visitor's movement.

## More info

The sensory journey “Data Wanderings” is a new project of Polifonia. The art installation has been open from Oct. 13 to 28, 2023 in Bologna, Italy.

‘Data Wanderings’ is a synaesthetic installation that challenges the boundaries between art and technology by transforming the rawness of data into a memorable sensorial journey. The audiovisual installation was conceived with the aim of making the user experience a physical simulation of virtual interaction with the mass of data coming from the knowledge graph of the “Polifonia” project.

Data Wanderings invites viewers to embark on a journey through the intricate labyrinth of data, to discover the secret melodies of numbers, and to embrace the creative and informative potential that lies within them.

The Choco database of Polifonia collects data on chords extracted from a series of songs. All song chords are listed in time sequence in a table, converted into a series of notes and their sound frequencies.

In the interactive installation, the eight frequencies of each chord are translated directly into pixels and they create eight mixed patterns to obtain the final “visual noise” patterns.
The frequencies also produce a generative soundtrack through FM synthesis to create a crazy digital [Orchestrion](https://en.wikipedia.org/wiki/Orchestrion).

The sphere floating in the center of the screen acts as an interface with visitors and it is generated using the album and singles’ covers from which the chord data was derived. People’s movements are detected with a camera, analyzed and used to influence images and sound by controlling a low-pass filter.

## Credits

Art Direction: Umanesimo Artificiale  
Concept: Filippo Rosati, Alex Piacentini  
Data Analysis: Alex Piacentini, Andrea Poltronieri, Jacopo de Berardinis  
Creative Coding: Alex Piacentini  
Sound Design: Alex Piacentini  
edited by: Federica Patti  
a POLIFONIA project

[Umanesimo Artificiale](http://www.umanesimoartificiale.xyz/) is a non-profit cultural organization and network of artists working with exponential technologies. It operates worldwide from Fano, Italy, with partners throughout Europe. Umanesimo Artificiale was born with the intent to investigate what does it mean to be human in the era of artificial intelligence. It promotes computational (creative) thinking through the channel of digital and performing arts, raising awareness of a fertile relationship between humans, artists and new technologies.

[Alex Piacentini](https://alexpiacentini.com) Visual artist, graphic designer and creative developer. He uses the web and other digital media as multidimensional materials where space, time, data and interactivity fuse creating intersections between generative design, data visualization, interfaces, sound and visuals.

