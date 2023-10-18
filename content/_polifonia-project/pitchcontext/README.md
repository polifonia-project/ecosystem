---
component-id: pitchcontext
name: pitchcontext
description: Python module for melody analysis based on pitch context vectors.
image: https://github.com/polifonia-project/pitchcontext/blob/main/image/vector_example_hor.png
type: SoftwareLibrary
release-date: "2023-06-02"
release-number: 0.1.9
doi: 10.5281/zenodo.8020644
work-package: 
- WP3
pilot: 
- TUNES
keywords:
  - melody
  - pitch analysis
licence:
  - MIT
contributors:
  - P. van Kranenburg <https://github.com/pvankranenburg>
project: polifonia-project
related-components:
- story:
  - Mark#1_FolkMusic
  - Brendan#1_FindTraditionalMusic
--- 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8020644.svg)](https://doi.org/10.5281/zenodo.8020644)

# pitchcontext
Python module for melody analysis based on pitch context vectors.

## Prerequisites:
- lilypond installed and in command line path.
- convert (ImageMagick) installed and in command line path.
- kernfiles and corresponding .json files with melodic features.

The .json files need to be formatted according to the standard of [MTCFeatures](https://pvankranenburg.github.io/MTCFeatures/melodyrepresentation.html).

## Installation
The latest release of the pitchcontext module can be installed from pypi:
```
$ pip install pitchcontext
```

The development version can be installed by cloning the repository and by using the provided pyproject.toml and poetry. In root of the rep do:
```
$ poetry install
```
This creates a virtual environment with pitchcontext installed.

## Examples
Requires a Python3 environment with both pitchcontext and streamlit installed.
Four examples are provided:
- apps/st_dissonance.py
- apps/st_novelty.py
- apps/st_unharmonicity.py
- apps/st_impliedchords.py

To run:
```
$ streamlit run st_dissonance.py -- -krnpath <path_to_kern_files> -jsonpath <path_to_json_files>
```
The -- is needed to pass the following arguments to the python script.
