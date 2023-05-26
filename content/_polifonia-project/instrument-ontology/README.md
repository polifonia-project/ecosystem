# Music Instrument ontology
The Music Instrument ontology module represents musical instruments as mediums of performance and their technical properties.

[![DOI](https://zenodo.org/badge/372536364.svg)](https://zenodo.org/badge/latestdoi/372536364)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> 🔗 Ontology URI: [https://w3id.org/polifonia/ontology/instrument/](https://w3id.org/polifonia/ontology/instrument/)

The Instrument Module describes musical instruments as mediums of performance
and their technical properties. Given that numerous taxonomies of instruments
into groups and families exist (e.g. Hornbostel-Sachs, MIMO, Mu- sicBrainz) and
finding common categorisations is an open problem [1], our module provides an
abstraction capable to express arbitrary classifications. This is achieved by
leveraging the Information-Realisation and the Collection ODPs. Overall, the
module allows to: (i) refer to instruments as entities (an instrumen- tation of
a piece for “piano” and “viola”) as well as conceptually (e.g. a viola has 4
strings); (ii) support the integration with different taxonomies and
vocabularies, such as [2]; (iii) describe the evolution of instruments in time
and space (e.g. a viola as a cultural heritage object being relocated).
This provides a foundational level where contributors can “plug” their
instrument-specific ontologies [3].

![instrument module diagram](diagrams/music-instrument-main-entities.png)

---

## Competency questions addressed
- Which is the physical realization of an instrument?
- Which are the parts of an instrument?
- Who invented an instrument?
- When was an instrument invented?
- Where was an instrument realization built?
- When was an instrument realization built?
- Who built an instrument realization?
- Which is the current location of an instrument realization?
- Which are the locations of an instrument realization during its life cycle?

## Competency questions planned


## Examples of SPARQL queries
- Which is the physical realization of an instrument?
```
PREFIX inst: <https://w3id.org/polifonia/ontology/instrument/>
PREFIX core: <https://w3id.org/polifonia/ontology/core/>
SELECT DISTINCT ?instrument ?instrumentRealization
WHERE { ?instrument core:isRealizedBy ?instrumentRealization .
}
```

- Who invented an instrument?
```
PREFIX inst: <https://w3id.org/polifonia/ontology/instrument/>
SELECT DISTINCT ?instrument ?builder
WHERE { ?instrument mi:wasInventedBy ?builder .
}
```

## Related ontologies

### External imports
- [ArCo Location Ontology module](https://w3id.org/arco/ontology/location)

### Aligned ontologies

## Statistics
Considering that this module imports other modules of the network and the ArCo ontology, relevant statistics are: 
- number of classes: 161 
- number of object properties: 209
- number of datatype properties: 41
- number of logical axioms: 876

## Datasets
TODO

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).


## References

[1] Kolozali, S., Barthet, M., Fazekas, G., Sandler, M.B.: Knowledge representation issues in musical instrument ontology design. In: ISMIR. pp. 465–470 (2011)

[2] Lisena, P., Todorov, K., Cecconi, C., Leresche, F., Canno, I., Puyrenier, F., Voisin, M., Le Meur, T., Troncy, R.: Controlled vocabularies for music metadata. In: IS- MIR: International Society for Music Information Retrieval (2018)

[3] Zanoni, M., Setragno, F., Sarti, A., et al.: The violin ontology. In: Proc. of the 9th Conference on Interdisciplinary Musicology (CIM14). Citeseer (2014)