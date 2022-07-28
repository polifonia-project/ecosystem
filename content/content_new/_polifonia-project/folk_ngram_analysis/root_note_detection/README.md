---
component-id: root_note_detection

name: Root Note Detection

brief-description: Work-in-progress on root note detection on a corpus of monophonic Irish folk tunes.

type: Repository

release-date: 8/12/2021

release-number: v0.4-dev

work-package: 
- WP3
licence: CC By 4.0, https://creativecommons.org/licenses/by/4.0/
links:
- https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/root_note_detection.ipynb
- https://zenodo.org/record/5768216#.YbEAbS2Q3T8

credits:
- https://github.com/danDiamo
- https://github.com/ashahidkhattak
---

# Root Note Detection

This folder contains the Jupyter Notebook script for the root note detection task. This folder contains two files. The one is Jupyter Notebook script and the other is the ```cre_root_detection.csv``` file. The jupyter file read the CSV file and then perform the following steps:

* 1- Perform Exploratory Data Analysis, such as null value, classes count, box plot, correlations, etc. 

* 2- Create Models such as Decision Tree using Gini and entropy and then computes its classification accuracy

* 3- Create Random Forest models using different hyperparameters for achieving better results.


Deliverable 3.2 of the Polifonia project will describe the context and research in more detail. It will be published on [Cordis](https://cordis.europa.eu/project/id/101004746/it).
