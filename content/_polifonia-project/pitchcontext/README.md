---
component-id: pitchcontext
name: pitchcontext
description: Python module for melody analysis based on pitch context vectors.
type: SoftwareLibrary
release-date: 2023-04-07
release-number: 0.1.8
work-package: 
- WP3
pilot: 
- TUNES
keywords:
  - melody
  - pitch analysis
changelog:
licence:
release link:
--- 


# pitchcontext
Python module for melody analysis based on pitch context vectors.

## Prerequisites:
- lilypond installed and in command line path.
- convert (ImageMagick) installed and in command line path.
- kernfiles and corresponding .json files with melodic features.

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
Three examples are provided:
- apps/st_dissonance.py
- apps/st_novelty.py
- apps/st_unharmonicity.py

To run:
```
$ streamlit run st_dissonance.py -- -krnpath <path_to_kern_files> -jsonpath <path_to_json_files>
```
The -- is needed to pass the following arguments to the python script.
