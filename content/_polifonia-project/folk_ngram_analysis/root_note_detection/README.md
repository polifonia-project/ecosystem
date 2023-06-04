---
component-id: root_note_detection
name: Root Note Detection
brief-description: Work-in-progress on root note detection on a corpus of monophonic Irish folk tunes.
type: Repository
release-date: 20/05/2022
release-number: v0.7.0.1-dev
work-package: 
- WP3
licence:
- CC_BY_v4
links:
- https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/root_note_detection.ipynb
- https://zenodo.org/record/5768216#.YbEAbS2Q3T8
credits:
- https://github.com/danDiamo
- https://github.com/ashahidkhattak
---


# Root Note Detection

The files in this folder are related to the Root note detection task. The notebook exploits monophonic Irish folk tunes processed data (that can be found in ```cre_root_detection.csv``` file) and with help of machine learning models predicts the root note of a tune. Determination of the root note of each piece of music in the corpus under investigation is a key foundational step in FONN. Accurate root note data allows reliable calculation of key-invariant chromatic pitch class sequences, which have been the primary input for our pattern analysis and melodic similarity work.

NOTE: Deliverable 3.3 of the Polifonia project describes the context and research in more detail.

To use the best trained model for root-note prediction tasks, follow the **demo notebook** [./RootNoteDemo.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/RootNoteDemo.ipynb).


### Prerequisites
This component requires the ```cre_root_detection.csv```. This file contains the processed data for each tune in the Ceol Rince na hÉireann (CRE) corpus. please see: [/.root_key_detection/cre_root_detection.csv](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/cre_root_detection.csv)


In this deliverable, we employed a factorial design experiment for Decision Tree, Random Forest, and Naive Bayes algorithms. We used a comprehensive list of hyperparameters to select the top-performing models. We also conducted experiments using SMOTE to generate a synthetic balance dataset. Finally, evaluation was done on an unseen dataset, and the obtained results are superior to state-of-the-art models. 

Following is the summary of the current work. The **experiment notebook** [./root-note-detection.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/root-note-detection.ipynb) reads the Ceol Rince na hÉireann (CRE) corpus CSV file and then performs the following steps:

* 1- Exploratory Data Analysis, such as null value, classes count, correlations, etc. 
* 2- Global settings are defined to control feature selection
* 3- Multiple dataset are created for model development and its evaluation
* 4- Minority classes are balanced with help of SMOTE
* 5- Classification report of state-of-the-art models for root note detection are generated for comparison
* 6- Factorial design experimental setup is developed to evaluate different classification algorithms such as  Decision Tree, RandomForest, NaiveBayes 
* 7- The best models are selected, and finally they are compared with SOA models, and the best model is saved.

The **demo notebook** [./RootNoteDemo.ipynb](https://github.com/polifonia-project/folk_ngram_analysis/blob/master/root_note_detection/RootNoteDemo.ipynb) shows how to use the best trained model for new prediction tasks.

##  Attribution

[![DOI](https://zenodo.org/badge/427469033.svg)](https://zenodo.org/badge/latestdoi/427469033)

If you use the code in this repository, please cite this software as follow: 
```
@software{danny_diamond_2022_6566379,
  author       = {Danny Diamond and
                  Abdul Shahid and
                  James McDermott},
  title        = {% raw %}{{{% endraw %}polifonia-project/folk\_ngram\_analysis: FONN 
                   v0.5dev}},
  month        = may,
  year         = 2022
}
```

## License
This work is licensed under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/
