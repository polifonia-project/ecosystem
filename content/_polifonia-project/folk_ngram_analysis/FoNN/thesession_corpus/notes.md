**The Session corpus notes**

Subdirectory '''../thesession_corpus/abc''' contains a data dump of The Session corpus (www.thesession.org)
in ABC Notation format, which was downloaded from https://github.com/adactio/TheSession-data on 13 December 2021.

ABC --> MIDI preprocessing can be carried out via FoNN.abc_ingest.py
Three feature sequence representations of the MIDI data can then can be extracted ('note-level', 'duration-weighted', and 'accent-level') via '''../FoNN/demo_notebooks/feature_extraction_demo.ipynb'''.
N-gram patterns can be extracted from this feature sequence data for 3 <= n <= 12 at all three input data representations, via '''../FoNN/demo_notebooks/pattern_extraction_demo.ipynb'''.
Similarity searches can be carried out via '''../FoNN/demo_notebooks/similarity_search_demo.ipynb''' using the 'motif', 'incipit and cadence', and 'TF-IDF' methodologies. 

NOTE: Due to corpus size, it was not possible to push the outputs of the corpus input processing steps above via Git. They are available on request of the
authors. Currently, only the ABC Notation inputs are provided in the remote version of the corpus.