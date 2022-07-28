---
component-id: folk_ngram_analysis
name: FONN - FOlk N-gram aNalysis
description: Work-in-progress on pattern extraction and melodic similarity tools, with an associated test corpus of monophonic Irish folk tunes.
type: Repository
release-date: 9/12/2021
release-number: v0.4-dev
work-package: 
- WP3
licence:  CC BY 4.0, https://creativecommons.org/licenses/by/4.0/
links:
- https://github.com/polifonia-project/folk_ngram_analysis
- https://zenodo.org/record/5768216#.YbEAbS2Q3T8
credits:
- https://github.com/danDiamo
- https://github.com/ashahidkhattak
- https://github.com/jmmcd
---

[![DOI](https://zenodo.org/badge/427469033.svg)](https://zenodo.org/badge/latestdoi/427469033)

# FONN - FOlk _N_-gram aNalysis 

FONN repo targets the goals of the Polifonia WP3 i.e., identification of patterns that are useful in detecting relationships between pieces of music, with particular focus on European musical heritage. At present, it includes scripts that make use of n-grams and Damerau-Levenshtein edit distance on monophonic Irish folk tunes.
NOTE: Deliverable 3.2 of the Polifonia project will describe the context and research in more detail. It will be published on [Cordis](https://cordis.europa.eu/project/id/101004746/it).

## In this strand of research we have created three Polifonia components:

1. **Folk -gram aNalysis (FONN)**
   * 1.1. Tools for extraction of feature sequence data from MIDI files -- these resources are available in [./setup_corpus](https://github.com/polifonia-project/folk_ngram_analysis/tree/master/setup_corpus) subfolder. 
   * 1.2. Tools to extract, compile, and rank patterns in various musical features such as (chromatic) pitch, pitch class, and interval from musical feature sequence data. 
   * 1.3. Tools to explore similarity between tunes within the corpus via frequent and similar patterns.
2. **Ceol Rince na hÉireann (CRÉ) MIDI corpus**
   * 2.1. For the associated *Ceol Rince na hÉireann* MIDI corpus of 1,224 monophonic Irish traditional dance tunes, please see: [./corpus/readme.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/corpus/readme.md).
3. **Root Note Detection**
   * 3.1. Work-in-progress on automatic detection of musical root for each tune in the corpus, please see: [/.root_key_detection/README.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_key_detection/README.md)


## 1. FONN - Prerequisites 

In ```./setup_corpus/setup_corpus.py``` file, first we need to assign the  ``` basepath ``` variable, which is the path to our working directory. 
``` basepath ``` should contain a subdirectory a corpus of folk tunes in MIDI format, which should be assigned to ```inpath``` variable. 
By default ``` basepath ``` is ```../corpus/```. If the corpus is elsewhere, change ```basepath ``` accordingly. The code will be writing outputs to subdirectories of ``` basepath ```. The ```corpus``` should include a ```roots.csv``` file containing the root note of each MIDI file, represented as a chromatic [pitch class](https://en.wikipedia.org/wiki/Pitch_class) (an integer between 0 and 11).

Install the following libraries:

``` pip install feather music21 pyarrow fastDamerauLevenshtein ```

...or just:

``` pip install -r requirements.txt ```

## Execution and summary tasks performed by each script:

### 1.1. The ```./setup_corpus/setup_corpus.py``` script:

Running this file will take about 15 minutes. It will produce many csv files under ```<basepath>/feat_seq_data/note```, ```<basepath>/feat_seq_data/accent```, ```<basepath>/feat_seq_data/duration_weighted```. To save time, we first check whether these files exist, and skip running the code if they do.

* Perform Tasks:
  * 1.1.1. Extract numeric feature sequences representing pitch, onset, duration, and velocity for all pieces of music in a corpus of monophonic MIDI files.
  * 1.1.2. Derive secondary feature sequences from the primary features outputted by 1.1.1, including interval, key-invariant pitch, pitch class, and melodic contour represented in Parsons code.
  * 1.1.3. Filter the feature sequence data produced by 1.1.1 and 1.1.2 to retain only values for note events which occur on accented beats, creating 'accent-level' feature sequence data for each tune.
  * 1.1.4. Calculate duration-weighted sequences for selected feature(s). This involves converting the sequences from value per note event to value per eighth note. By default, this process is applied to pitch and pitch class data.
  * 1.1.5 Save outputs. By default, outputs are saved to subfolders of ```<basepath>```, per the code excerpt below:
  
```corpus.save_corpus(
        feat_seq_path=basepath + "/feat_seq_data/note",
        accents_path=basepath + "/feat_seq_data/accent",
        duration_weighted_path=basepath + "/feat_seq_data/duration_weighted")
  ```

### 1.2. The ```./setup_ngrams_tfidf.py``` and ```./ngram_tfidf_tools.py``` scripts

The ```./setup_ngrams_tfidf.py```, which sets up classes and runs methods from ```./ngram_tfidf_tools.py```, will take about 25 minutes to run-- so we check whether the output files already exist before running. By default the script will write output to ```<basepath>/ngrams``` in the form of Feather (.ftr) asnd CSV data tables.

* Perform Tasks:
  * 1.2.1. Extract n-gram patterns for selected musical feature. So far, work-in-progress has extracted on n-grams for 3 <= n <= 12 on five feature sequences, including melodic contour, interval, pitch, pitch-class interval, and pitch class. The defaults settings, per the code block excerpted below from ```./setup_ngrams_tfidf.py```, will extract all n-grams for 5 <= n <= 10 from the accent-level pitch class sequence for each tune in the corpus (i.e.: all unique patterns between 5-10 accented notes in length).
  
```
basepath = "./corpus"
    inpath = basepath + "/feat_seq_data/accent"
    feature = "pitch_class"
    n_vals = list(range(5, 10))
```
* * 1.2.2 Count and rank occurrences of the patterns identified in 1.2.1 in every tune in the corpus. Two corpus-level tables are compiled: one containing the frequency of each pattern in each tune across the corpus; the other containing the tf-idf value of each pattern in each tune. By default, both tables are saved to ```<basepath>/ngrams``` in Feather (.ftr) and CSV formats, per the code block below excerpted from ```./setup_ngrams_tfidf.py```:
   
```
ngram_corpus.save_results(outpath=basepath + "/ngrams",
                              corpus_name='cre_pitch_class_accents')
``` 

### 1.3. The ```./ngram_pattern_search.py``` script: 
```./ngram_pattern_search.py``` contains exploratory work-in-progress on identifying similar between tunes based on similarity between their n-grams, as calculated using the Damerau-Levenshtein edit distance algorithm.

* Perform Tasks:
  * 1.3.1. Select a candidate tune from the tf-idf Feather table created in 1.2, and extract its top-ranked n-gram(s). The default is to extract the top two 6-gram patterns as ranked by tf-idf, per the code block below:
  
```
  pattern_search.extract_candidate_ngrams("Lord McDonald's (reel)", n=6, mode='idx', indices=\[0, 1])
  ``` 
* * 1.3.2. With the patterns extracted in 1.3.1 as search terms, search the Feather tf-idf table created by 1.2.2 for occurrences of similar patterns, using the Damerau-Levenshtein edit distance algorithm. 
* * 1.3.3. Work-in-progress: identify similar pieces of music by counting the occurrences of similar patterns per tune. Results are printed to console.


## 2. Ceol Rince na hÉireann (CRÉ) MIDI corpus 

A new MIDI version of the existing *Ceol Rince na hÉireann* corpus of 1,224 monophonic Irish dance tunes. Please see: [./corpus/readme.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/corpus/readme.md).
* Highlights:
  * Corpus title: _Ceol Rince na hÉireann_
  * Source: Black, B 2020, [The Bill Black Irish tune archive homepage](http://www.capeirish.com/webabc), viewed 5 January 2021.
  * Contents: 1,224 traditional Irish dance tunes, each of which is represented as a monophonic MIDI file. Also included is roots.csv, a file giving the root note for every file in the corpus as a chromatic pitch class in integer notation.
  
## 3. Root Note detection 
Work-in-progress on automatic detection of musical root for each tune in the corpus. Please see: [/.root_key_detection/README.md](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/README.md).
  This component contains one jupyter notebook script that makes use of  ```cre_root_detection.csv```, which is an expert-annotated file containing pitch class values assigned to each piece of music in the corpus by a variety of root-detection metrics. From this input, the script makes use of machine learning methods to classify the root note. The root note detection notebook can be accessed using this link: [/.root_note_detection/root_note_detection.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/root_note_detection.ipynb).
  

  
