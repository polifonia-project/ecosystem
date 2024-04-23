**MTC-ANN corpus notes**

Subdirectory '''./mtc_ann_corpus/krn''' contains a copy of the Meertens Tune Collection Annotated Corpus (MTC-ANN)
v2.0.1 in **kern format, downloaded from www.liederenbank.nl/mtc on 29 November 2021.
All other data in '''./mtc_ann_corpus''' dir is derived from this original input.

Feature sequence data extracted at note-level and (duration-weighted) note-level representations via '''../FoNN/demo_notebooks/feature_extraction_demo.ipynb'''.

Diatonic scale degree patterns extracted for 3 <= n <= 12 at (duration-weighted) note-level via '''../FoNN/demo_notebooks/pattern_extraction_demo.ipynb'''.. This in turn provides input data for similarity search tools accessible via '''../FoNN/demo_notebooks/similarity_search_demo.ipynb'''. 

KG data processed per:
Patterns and pattern locations extracted for 4 <= n <= 6 at (duration-weighted) note-level.
'Pattern corpus' filtered to include only patterns occurring at least twice in the corpus.