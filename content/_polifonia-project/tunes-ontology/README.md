# Tunes Ontology
A specialisation of [Music Meta](https://github.com/polifonia-project/musicmeta-ontology) for folk music.

[![DOI](https://zenodo.org/badge/372536364.svg)](https://zenodo.org/badge/latestdoi/372536364)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> 🔗 Ontology URI: [https://w3id.org/polifonia/ontology/tunes/](https://w3id.org/polifonia/ontology/tunes/)

The main novelty at the metadata level consists in grouping *tunes* into *tune families* depending on their similarity (an association that is often performed through manual inspection and analysis). Each `tunes:Tune` is seen as a specialisation of a `mm:MusicEntity` that may belong to a `tunes:TuneFamily`, which in turn specialises `core:Collection` (please, note that the term *Collection* is seen from an ontology engineering perspective, as this reuses the Collection ontology design pattern in Music Meta).

![Tune family](diagrams/tunes_ontology.png)

As can be seen from the diagram/example below, the membership of a `tunes:Tune` to `tunes:TuneFamily` is described by `core:CollectionMembership`, which provides additional information on the actual strength of such membership. The latter is captured by `core:CollectionMembership`, which is specialised by two entities here: `tunes:WeakFamilyMembership` and `tunes:NeutralFamilyMembership`.

Another extension that is peculiar to folk music, is the possibility to group tunes' `mm:Lyrics` into a `tunes:LyricsFamily`. This is analogous to `tunes:TuneFamily` as described above. The same criteria for expressing membership strength apply as before. As shown in the diagram/example below, a tune and lyrics families are not exclusive.

## Competency questions addressed

| **ID** | **Competency Question**                                                                                                                    |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| CQ1    | Has composition X been identified as variant in a tune family?                                                                 |
| CQ2    | Which tune family does composition X belong to?                                                                                              |
| CQ3    | Who assigned composition X to tune family Y?                                                                                        |
| CQ4    | With what level of confidence is composition X a variant in tune family Y?                                      |
| CQ5    | What are all compositions in tune family X?                                                                           |
| CQ6    | What are the similarities / differences of all compositions in tune family X according to measure Y?                                       |
| CQ7    | To what tune families is tune family X related, given similarity measure Y?|


## Examples of SPARQL queries addressed

- Which are the tunes that compose a tune family associated to a composer?
```
PREFIX tunes: <https://w3id.org/polifonia/ontology/tunes/>
PREFIX mm: <https://w3id.org/polifonia/ontology/music-meta/>
PREFIX core: <https://w3id.org/polifonia/ontology/core/>
SELECT DISTINCT ?artist ?collection ?musicEntity
WHERE { ?artist mm:isComposerOf ?musicEntity .
?musicEntity core:isMemberOf ?collection .
}
GROUP BY ?artist ?collection
```

## Imported ontologies

### Direct imports
- [Music-Meta Ontology](https://w3id.org/polifonia/ontology/music-meta/)

### Indirect imports
- [Core Ontology](https://w3id.org/polifonia/ontology/core/)

## Statistics
We report here useful statistics of the Tunes Ontology Module:
 
- number of classes: 95
- number of object properties: 92
- number of datatype properties: 17
- number of logical axioms: 810

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].


[cc-by]: http://creativecommons.org/licenses/by/4.0/

