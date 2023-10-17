# Co*Meta
An extension of [Music Meta](https://github.com/polifonia-project/musicmeta-ontology) to describe the metadata of music **co**llections, **co**rpora, **co**ntainers, or simply music datasets!

[![DOI](https://zenodo.org/badge/372536364.svg)](https://zenodo.org/badge/latestdoi/372536364)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> 🔗 Ontology URI: [https://w3id.org/polifonia/ontology/cometa/](https://w3id.org/polifonia/ontology/cometa/)

Here, metadata is described at the collection-level (data curator, annotations provided, availability of audio music, etc.), and at the content-level, (e.g., the title, artist, release of each piece in a dataset). The design of CoMeta is informed by a survey of Music Information Retrieval datasets, which allowed for the categorisation of common fields.


![overview](diagrams/cometa_overview.png)


The ontology designed to describe music datasets as containers of music-related data with specific characteristics and annotations.

- **Collection Information**: the ontology captures information about the dataset as a whole, including the number of records (compositions or performances), genres, year of release, collection metadata (project investigator, university, etc.), and content metadata (specification document with track-level information like title, artist, release, MusicBrainz identifier). This also includes properties such as music media type (audio or symbolic), duration, audio format (MP3, WAV, FLAC), symbolic format (MIDI, MusicXML, MEI), and other additional media (audio features, rankings, etc.).

- **Annotations**: to represent the annotations provided within the dataset, which are crucial for MIR tasks. It would include various types of annotations contributed by domain experts (musicologists, composition teachers) or listeners, covering aspects like music structure, key, chord progressions, emotions, listening habits, etc.

- **Computational tasks**: to define the different tasks that a dataset enables based on the available annotations. Examples in MIR include music emotion recognition, pattern extraction, cadence detection, etc. Together with the [`Music Algorithm`](https://github.com/polifonia-project/music-algorithm-ontology) ontology (its sibling ontology) it also allows to track the performance/accuracy of computational methods tested on each dataset.

- **Access and availability**: to capture information regarding the accessibility of the dataset, including whether it is open, on-demand, or closed, and whether it can be accessed online or requires manual provisioning. It may also include details about an API if available.

- **License/Copyright**: to represent the licensing and copyright information associated with the dataset, ensuring compliance and proper attribution.

- **References**: to provide links to official websites and academic manuscripts describing the dataset and its collection process, facilitating proper citation and reference.


By incorporating and supporting these requirements, the ontology would provide a structured representation of music datasets, their metadata, annotations, and interconnections. It would enable researchers and practitioners to explore, analyse, and utilize the datasets more effectively, promote interoperability, and facilitate the automatic discovery and extraction of knowledge from music-related data.

![overview](diagrams/cometa_definition.png)

![overview](diagrams/cometa_content.png)


---
<!-- 
## Competency questions addressed

| **ID** | **Competency Question**                                                                                                                    |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| CQ1    | Where is the building/church/bell tower?                                                                                                   |
| CQ2    | When (what year) was the building built?                                                                                                   |
| CQ3    | In which context is the building located (urban, periurban...)?                                                                            |


## Competency questions planned

| **ID** | **Competency Question**                                                                                                                    |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| CQ1    | Is the bell tower associated to a religious building or a civil building?                                                                  |
| CQ2    | Which is the mounting system of the bell?                                                                                                  |
| CQ3    | Which is the nominal/fundamental note of the bell?                                                                                         |
| CQ4    | What kind of execution techniques are possible to perform according to a specific mounting system?                                         |
| CQ5    | Can a set of bells be played electrically, manually, or both?                                                                              |
| CQ6    | Is the sound in a place currently performed by hand or by electric means?                                                                  |
| CQ7    | How/Using which tools/Using which execution technique(s)/Following which sound practices is the set of bells played, when played manually? |
| CQ8    | What are the recordings involving a bell or set of bells?                                                                                  |

## Examples of SPARQL queries
- By whom (by which foundry) were the bell(s) melted? When where they melted?
```
PREFIX tiapit: <https://w3id.org/italia/onto/TI/>
PREFIX core: <https://w3id.org/arco/ontology/core/>
PREFIX a-cd: <https://w3id.org/arco/ontology/context-description/>
PREFIX arco: <https://w3id.org/arco/ontology/arco/>
SELECT DISTINCT ?bell ?desc ?author ?authorLab ?dating ?datingTime
WHERE { ?bell arco:isCulturalPropertyComponentOf ?setofbells ; rdf:type arco:MusicHeritage ;
core:description ?desc ;
a-cd:hasDating ?dating ;
a-cd:hasAuthor ?author ;
dc:subject ?o .
?author rdfs:label ?authorLab .
?dating a-cd:hasDatingEvent ?datingEv .
?datingEv tiapit:atTime ?datingTime
FILTER(str(?o)='campana')
}
```

## Related ontologies

### External imports

### Direct imports
- [ArCo Ontology network](https://w3id.org/arco/ontology/arco)

### Aligned ontologies
- [Wikidata](link)

## Statistics
Considering that, apart from the definition of some novel classes inside the module (such as Bell, SetOfBells, and BellTower), the BELL module widely relies on the ArCo ontology network, we report here useful statistics of ArCo: 
- number of classes: XXX 
- number of object properties: XXX
- number of datatype properties: XXX
- number of logical axioms: XXX

## Datasets
The following datasets where produced using this ontology.
- https://w3id.org/arco/resource/MusicHeritage/0700377972-0 (68 triples) -->

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
