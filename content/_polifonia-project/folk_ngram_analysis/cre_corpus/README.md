---
component-id: cre_corpus
name: Ceol Rince na hÉireann MIDI corpus
brief-description: A corpus of 1,195 monophonic instrumental Irish traditional dance tunes.
type: Corpus
release-date: 15/06/2022
release-number: v0.7.0.1-dev
work-package: 
- WP3
licence:
- CC_BY_v4
links:
- https://github.com/polifonia-project/folk_ngram_analysis/corpus
- http://www.capeirish.com/webabc
- https://zenodo.org/record/5768216#.YbEAbS2Q3T8
credits:
- https://github.com/danDiamo
- https://github.com/ashahidkhattak
- http://www.capeirish.com/
---


## About the dataset 

**Corpus title:** _Ceol Rince na hÉireann_

**Source:** [Black, B 2020, _The Bill Black Irish tune archive homepage_, viewed 5 January 2021.](http://www.capeirish.com/webabc)

**Contents:** 1,195 traditional Irish dance tunes, represented in [MIDI](https://github.com/polifonia-project/folk_ngram_analysis/tree/master/cre_corpus/MIDI) and [ABC Notation](https://github.com/polifonia-project/folk_ngram_analysis/tree/master/cre_corpus/abc).

Between 1963 and 1999, Irish State publishing companies Oifig an tSolatáthair and An Gúm issued five printed volumes of tunes from the collections of Breadán Breathnach (1912-1985) under the series title _Ceol Rince na hÉireann_ (Dance Music of Ireland, hereafter _CRÉ_). The five volumes of _CRÉ_ contain 1,208 traditional tunes, a subset of Breathnach's more extensive personal collection of 5,000+ melodies. The collection has been transcribed into ABC notation by American traditional music researcher Bill Black, and made freely available online via his [personal website]((http://www.capeirish.com/webabc)). Addition of alternative tune versions and variation in numbering of unique melodies has resulted in a total of 1,224 tunes in the Bill Black ABC corpus. This resource has been used in previous research work, for example it makes up part of a larger aggregated corpus used in the [_Tunepal_](https://tunepal.org/index.html) Music Information Retrieval app. We have created a new cleaned and annotated version of the corpus, from which feature sequence data can be extracted and analysed via Polifonia's [FONN](https://github.com/polifonia-project/folk_ngram_analysis) music pattern analysis toolkit.

NOTE: Please see [corpus_demo.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/cre_corpus/corpus_demo.ipynb) for a Jupyter notebook exploring the corpus data.

Deliverable 3.3 of the Polifonia project will describe the context and research in more detail. It will be published on [Cordis](https://cordis.europa.eu/project/id/101004746/it).


## About corpus pre-processing methodology

Bill Black's ABC version of the _CRÉ_ collection has been manually edited and annotated, and converted to MIDI. This work included:
* Removal of alternative tune versions, so that the ABC collection more accurately reflects the original print collection.
* Removal of non-valid ABC notation characters.
* Editing of repeat markers to ensure accurate MIDI output.
* Manual assignment of root note (as chromatic pitch class) for every piece of music in the corpus. This data is stored in [roots.csv]( https://github.com/polifonia-project/folk_ngram_analysis/tree/master/cre_corpus/roots.csv), which is used to derive key-invariant  secondary feature sequence data from the MIDI files.


## Description of the data

```
corpus/
  -MIDI/
    -1,195 monophonic MIDI (.mid) files, one representing each tune.
  -abc/
    -1 ABC NOtation corpus file (.abc) containing scores for all 1,195 tunes.
  -roots.csv
  -README.md
  -LICENSE.md

```

- ```corpus``` directory contains roots.csv, this README.md, and a LICENSE.md file.

- Roots.csv holds two columns with one row per each MIDI file in the corpus:
  - 'title': MIDI file name (tune title)
  - 'root': expert-assigned root note of each melody, represented as a [chromatic pitch class](https://en.wikipedia.org/wiki/Pitch_class) (i.e.: An integer value from C=0 through B=11). 

<img width="400" alt="image" src="https://user-images.githubusercontent.com/78231894/142916162-9ace1c42-ceae-412f-95df-98ce34acd359.png">
<br><br>

- To convert corpus form ABC Notation to MIDI format, please download the corpus data and run FONN [abc_ingest.py](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/abc_ingest.py) script. Please see [FONN README.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/README.md) for further information. 

- To extract feature sequence data from the MIDI corpus, please download the corpus data and run FONN [setup_corpus.py](https://github.com/danDiamo/music_pattern_analysis/blob/master/setup_corpus.py) script. Please see [FONN README.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/README.md) for further information.
 

## Attribution

If you use the code in this repository, please cite this software as follow: 
```
@software{diamond_fonn_2022,
	address = {Galway, Ireland},
	title = {{FONN} - {FOlk} {N}-gram {aNalysis}},
	shorttitle = {{FONN}},
	url = {https://github.com/polifonia-project/folk_ngram_analysis},
	publisher = {National University of Ireland, Galway},
	author = {Diamond, Danny and Shahid, Abdul and McDermott, James},
	year = {2022},
}
```

## License

This work is licensed under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/


