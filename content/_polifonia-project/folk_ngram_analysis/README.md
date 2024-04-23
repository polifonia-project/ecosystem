---
component-id: folk_ngram_analysis
name: FoNN -- Folk N-gram aNalysis
description: data ingest pipeline and musical similarity and classification tools for symbolic music data, with two test symbolic music corpora.
type: Repository
release-date: 16/06/2023
release-number: v1.0
work-package: 
- WP3
licence:
- MIT
links:
- https://github.com/polifonia-project/folk_ngram_analysis
- https://zenodo.org/record/5768216#.YbEAbS2Q3T8
credits:
- https://github.com/danDiamo
- https://github.com/ashahidkhattak
- https://github.com/jmmcd
---



# FoNN - FOlk _N_-gram aNalysis 

- Targeting the goals of [Polifonia](https://polifonia-project.eu) WP3, FoNN contains tools to extract feature sequence data, extract musical patterns, and detect similarity within a symbolic music corpus. Although some of FoNN's functionality is tailored to Western European folk music, the software can be used on any corpus in a compatible symbolic representation format (MIDI, ABC Notation, **kern, MusicXML, or any other format compatible with the [music21](http://web.mit.edu/music21/) Python library).

The repo contains a fully functional version of the software, along with two test music datasets: the Meertens Annotated Corpus (MTC-ANN) of Dutch folk songs and The Session corpus of Irish traditional folk dance tunes.
Four demo notebooks are supplied in ```./FoNN/demo_notebooks``` directory. These demos illustrate FoNN's feature extraction, pattern extraction, and similarity search tools as applied to the MTC-ANN corpus: 

- [feature_extraction_demo.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/demo_notebooks/feature_extraction_demo.ipynb): Reads the symbolic MTC-ANN music corpus from **kern format; extracts feature sequence data and writes to csv at ```./FoNN/mtc_ann_corpus/feature_sequence_data``` 
- [setup_pattern_corpus_demo.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/master/demo_notebooks/setup_pattern_corpus_demo.ipynb): Reads the feature sequence data outputted by the above notebook, extracts unique feature patterns and counts their occurrences per tune across the corpus. Writes output to ```./FoNN/mtc_ann_corpus/pattern_corpus```.
- [setup_tfidf_similarity_demo.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/master/demo_notebooks/setup_tfidf_similarity_demo.ipynb): Reads the feature sequence data outputted by ```./FoNN/mtc_ann_corpus/pattern_corpus``` notebook, calculates TF-IDF values for every pattern occurrence in each tune in the corpus. Calculates TF-IDF vectors for each tune, using which a pairwise Cosine similarity matrix is calculated. Writes output to ```./FoNN/mtc_ann_corpus/pattern_corpus```.
- [similarity_search_demo.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/demo_notebooks/similarity_search_demo.ipynb): Using the data outputted by the notebooks above, for a user-selectable query tune, this demo detects similar tunes across the corpus via FoNN's three novel pattern-based similarity metrics. Writes output to ```./FoNN/mtc_ann_corpus/similarity_results```

The repo also contains a data extraction and processing pipline to generate inputs for Polifonia [Patterns Knowledge Graph (KG)](https://github.com/polifonia-project/patterns-knowledge-graph). Two Jupyter notebooks which run this pipeline are stored in ```./FoNN/pattern_knowledge_graph_pipeline``` directory:
- ```./FoNN/pattern_knowledge_graph_pipeline/patterns_kg_data_extraction.ipynb``` runs FoNN's pattern extraction tools to extract corpus data.
- ```./FoNN/pattern_knowledge_graph_pipeline/patterns_kg_data_processing.ipynb``` combines pattern data, feature sequence data and descriptors for each tune in the corpus and writes this data to a corpus-level Pickle file matching the Patterns KG input requirements.


NOTE: Deliverable 3.4 of the Polifonia project describes the context and research informing development of these tools. It will be published on [Cordis](https://cordis.europa.eu/project/id/101004746/it) later this year (2023).


## FoNN -- Polifonia components:

1. **FoNN - FOlk _N_-gram aNalysis**
   * 1.1. Tools for extraction of feature sequence data from symbolic music document files: [feature_sequence_extraction_tools.py](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/FoNN/feature_sequence_extraction_tools.py).
   * 1.2. Tools to extract and count occurrences of unique local patterns from the feature sequence data: [pattern_extraction.py](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/FoNN/pattern_extraction.py). 
   * 1.3. Tools to explore pattern-based similarity between tunes within a corpus: [similarity_search.py](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/FoNN/similarity_search.py)
   * 1.4 Copies of two test music datasets: 
     - [The Meertens Tune Collection Annotated Corpus](https://www.liederenbank.nl/mtc/)
     - [The Session](https://thesession.org)
   * 1.5 Patterns KG data extraction and processing pipeline:
   [patterns_knowledge_graph_pipeline](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/FoNN/patterns_knowledge_graph_pipeline)

    
2. **Ceol Rince na hÉireann (CRÉ) corpus**
   * 2.1. For the associated *Ceol Rince na hÉireann* corpus of 1,195 monophonic Irish traditional dance tunes in ABC and MIDI formats, please see: [./cre_corpus/readme.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/cre_corpus/readme.md).
3. **Root Note Detection**
   * 3.1. Work-in-progress on automatic detection of musical root for each tune in the corpus, please see: [/.root_key_detection/README.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/README.md)
4. **Tune family annotations**
   * 4.1. Tune family membership annotation for 10 families containing a total of 314 tunes from *The Session* corpus. This annotation is based on an extensive literature review of musicological research on Irish traditional music, documented in *Tune family detection in a corpus of Irish traditional dance tunes*, Danny Diamond, 2024. MSc Thesis, University of Galway. In preparation.


## FoNN - Requirements

To ensure FoNN runs correctly, please navigate to local repo root directory and run the following in Terminal:

``` pip install -r requirements.txt ```


## FoNN - preprocessing step for ABC corpora

NOTE: *The Session* and *CRÉ* corpora are provided in both ABC Notation and MIDI formats.

- To ingest a corpus in ABC Notation format, first install the ABC2MIDI external dependency, which can be downloaded directly [here](https://ifdo.ca/~seymour/runabc/abcMIDI-2022.06.14.zip). For information on ABC2MIDI, please see the project [documentation](https://abcmidi.sourceforge.io).

- If ingesting a corpus in ABC Notation, first convert to MIDI by running the ```./FoNN/abc_ingest.py``` script. This preliminary step uses ABC2MIDI to encode a specific 'beat stress model' into the MIDI output, which is used later in the workflow to filter data for rhythmically-accented notes. Such higher-level representation of melody is of particular interest in the study of Irish and related European & North American folk musics.

- The workflow from here onwards is the same for corpora originating in all formats: if a corpus does not originate in ABC Notation, please skip to section 1.1.


## 1. FoNN - FOlk _N_-gram aNalysis: running the tools

1.1. **Reading a corpus**

- Running ```.FoNN/demo_notebooks/feature_extraction_tools_demo.ipynb``` extracts feature sequence data from an input corpus via ```FoNN.feature_sequence_extraction_tools.Corpus``` class. 
- By default this notebook reads the corpus at ```./FoNN/mtc_ann_corpus/krn``` and outputs feature sequence data to ```./FoNN/mtc_ann_corpus/feature_sequence_data```. 
- Input path and format can be edited as desired, while output will always write to ```./FoNN/[corpus name]/feature_sequence_data``` subdirectory. 
- This notebook extracts 16 feature sequences in what we term note-level, duration-weighted note-level, and accent-level representations, as explained below: 
1. Note-level: for every music score document in the corpus, each note is represented via 16 feature values.
2. Duration-weighted note-level: for every music score document in the corpus, each 1/8 note temporal increment is represented via 16 feature values.
3. Accent-level: for every music score document in the corpus, accented on-the-beat notes are represented via 16 feature values while other less metrically significant notes are dropped.
- Throughout the FoNN toolkit, these levels of data granularity are specified via the following string names:
1. note-level: 'note'
2. duration-weighted note-level: 'duration_weighted'
3. accent-level: 'accent'
- The 16 musical features extracted for each note are:
```
-- 'midi_note_num': Chromatic pitch represented as MIDI number
-- 'onset': note onset (1/8 notes)
-- 'duration': note (1/8 notes)
-- 'velocity': MIDI velocity
-- 'diatonic_note_num': Diatonic pitch
-- 'beat_strength' -- music21 beatStrength attribute
-- 'chromatic_pitch_class': Pitch normalised to a single octave, represented as an integer between 0-11.
-- 'bar_num': Bar number
-- 'relative_chromatic_pitch': Chromatic pitch relative to the root note or tonal centre of the input sequence.
-- 'relative_diatonic_pitch': Diatonic pitch relative to the root note or tonal centre of the input sequence.
-- 'chromatic_scale_degree': Chromatic pitch class relative to the root note or tonal centre of the input sequence.
-- 'diatonic_scale_degree': Diatonic pitch class relative to the root note or tonal centre of the input sequence.
-- 'chromatic_interval': Change in chromatic pitch between two successive notes in the input sequence
-- 'diatonic_interval': Change in diatonic pitch between two successive notes in the input sequence
-- 'parsons_code': simple melodic contour. Please see Tune.extract_parsons_codes() docstring for detailed explanation.
-- 'parsons_cumsum': cumulative Parsons code values.
```
- For more detail on how to customise inclusion/exclusion of features and choice of output data level, please refer to ```./FoNN/demo_notebooks/feature_extraction_tools_demo.ipynb```.   


1.2. **Extracting patterns and counting their occurrences:**

- For a user-selected musical feature, ```/FoNN/demo_notebooks/setup_pattern_corpus_demo.ipynb``` uses FoNN.pattern_extraction.NgramPatternCorpus class to extract all unique *n*-gram patterns from the input corpus for a user-defined *n* value or range. Allowable *n* values are 3 <= *n* <= 16. The default feature is 'diatonic_pitch_class' but other features can be selected by the user from the list above in Section 1.1. The default 
- Default input data is the MTC-ANN corpus feature sequence data at ```./FoNN/mtc_ann_corpus/feature_sequence_data```, but pattern extraction can be applied to any other symbolic corpus which has first been processed via FoNN's feature extraction pipeline as described in section 1.1.
- A pattern is defined as a subsequence containing *n* elements which occurs at least once in the corpus. All patterns following this definition which occur in the corpus are stored in an array. Their occurrences in every tune in the corpus are counted and stored in a sparse matrix. These counts are weighted and converted to TF-IDF values to supress frequent-but-insignificant 'stop word' patterns. These outputs are the core input requirements for FoNN's similarity search tool; they are stored in ```./FoNN/[corpus name]/pattern_corpus``` dir.


1.3. **Pattern-based tune similarity**

- The ```/FoNN/demo_notebooks/similarity_search_demo.ipynb``` notebook contains sample similarity searches for a user-selected query tune from the MTC-ANN corpus via FoNN.similarity_search.
- Results are returned which rank other tunes in the corpus by their similarity to the candidate tune. These are obtained via FoNN's three novel metrics: 'motif', 'incipit and cadence', and 'TFIDF'.
1. 'motif':
First representative patterns are extracted from the query tune via an automatically-calculated TF-IDF threshold based on the distribution of TF-IDF values for all unique pattern occurrences in the query tune. Patterns with TF-IDF values greater than the threshold are taken as representative of the query tune and retained for use as search terms. For each search term pattern, similar patterns across the corpus are detected via a custom-weighted Levenshtein distance. For every tune in the corpus, the number of similar pattern occurrences per tune is calculated and weighted by up to two novel musicologically-informed factors. These weighted count values are taken as a similarity score, and are returned in raw and normalised formats.
2. 'incipit and_cadence':
An extended version of a traditional musicological incipit search.
Structurally-important incipit and cadence subsequences are extracted from all tunes in the corpus and
compared via pairwise edit distance against the query tune. Users can select from three available edit distance metrics:
Levenshtein distance; Hamming distance; and a custom-weighted Hamming distance in which musically-consonant
substitutions are penalised less than dissonant substitutions. The edit distance output is taken as a
tune-dissimilarity metric.
3. 'tfidf':
A classical IR baseline methodology: the Cosine similarity between TFIDF vectors of all tunes in the corpus is taken as a tune similarity metric. 
- All results are displayed in the notebook and automatically written to csv files at ```./FoNN/[corpus name]/similarity_results```.

1.4. **Test music datasets**
- [The Meertens Tune Collection Annotated Corpus (MTC-ANN) version 2.0.1](https://www.liederenbank.nl/mtc/): 360 folk song melodies from the Meertens Instituut's Database of Dutch Songs, in **kern and MIDI formats. Stored in ```./FoNN/mtc_ann_corpus``` dir. 
- [The Session](https://thesession.org): An online, crowd-sourced collection of 40,000+ monophonic Irish traditional dance tunes in ABC Notation and MIDI formats. Stored in ```./FoNN/the_session_corpus``` dir. 

1.5 **Patterns KG data extraction and processing pipeline**
- Step 1: Run ```./FoNN/pattern_knowledge_graph_pipeline/patterns_kg_data_extraction.ipynb``` to extract corpus feature sequence and pattern data.
- Step 2: Run ```./FoNN/pattern_knowledge_graph_pipeline/patterns_kg_data_processing.ipynb``` to combine feature sequence and pattern data for the entire corpus and write to Pickle file for KG creation via Polifonia [Patterns Knowledge Graph (KG)](https://github.com/polifonia-project/patterns-knowledge-graph) repo.
- Further information on user-customization of pipeline parameters is provided within the notebooks.


## 2. Ceol Rince na hÉireann (CRÉ) MIDI corpus [legacy component]

- A new version of the previously-existing *Ceol Rince na hÉireann* corpus, containing 1,195 monophonic Irish traditional dance tunes. the corpus in provided in ABC Notation and in MIDI. Please see: [./cre_corpus/readme.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/cre_corpus/README.md) for more information.

* Highlights:
  * Corpus title: _Ceol Rince na hÉireann_
  * Source: Black, B 2020, [The Bill Black Irish tune archive homepage](http://www.capeirish.com/webabc), viewed 5 January 2021.
  * Contents: 1,195 traditional Irish dance tunes, each of which is represented as a monophonic MIDI file. Also included is ```roots.csv```, a file giving the expert-annotated root note for every file in the corpus as a chromatic integer pitch class.
  
## 3. Root Note Detection [legacy component]


Work-in-progress on automatic detection of musical root for each tune in the corpus. Please see: [/.root_key_detection/README.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/README.md).
  This component contains a jupyter notebook script that makes use of  ```cre_root_detection.csv```, which is a file containing pitch class values assigned to each piece of music in the corpus by the above-mentioned root-detection metrics outputted by ```setup_corpus.py```. From this input data, the script makes use of machine learning methods to classify the root note. The root note detection notebook can be accessed at [/.root_note_detection/root_note_detection.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/root_note_detection.ipynb).

## 4. Tune family annotations

This component contains Tune family membership annotation for 10 families containing a total of 314 tunes from *The Session* corpus. This annotation is based on an extensive literature review of musicological research on Irish traditional music, documented in *Tune family detection in a corpus of Irish traditional dance tunes*, Danny Diamond, 2024. MSc Thesis, University of Galway. In preparation. The data is formatted as a csv file, where identifiers is a unique tune ID numer from *The Session* corpus, and tune_family is a string containing the tune family name.

  
##  Attribution

[![DOI](https://zenodo.org/badge/427469033.svg)](https://zenodo.org/badge/latestdoi/427469033)

If you use the code in this repository, please cite this software as follows: 
```
@software{diamond_fonn_2024,
	address = {Galway, Ireland},
	title = {% raw %}{{{% endraw %}FoNN} - {FOlk} {N}-gram {aNalysis}},
	shorttitle = {% raw %}{{{% endraw %}FoNN}},
	url = {https://github.com/polifonia-project/folk_ngram_analysis},
	publisher = {National University of Ireland, Galway},
	author = {Diamond, Danny and Shahid, Abdul and McDermott, James},
	year = {2022},
}
```

## License
The FoNN software toolkit is made available under MIT licence. Please see ```./FoNN/LICENSE.md``` for details.
