---
component-id: textual-corpus-population
name: Textual Corpus Population
description: Polifonia downloader and digitiser of textual data.
type: Repository
release-date: 07-12-2021
release-number: v0.1
work-package: WP4
pilot:
  - MusicBo
keywords:
  - ocr
  - image
  - text digitisation
  - textual data
changelog: n/a.
licence: MIT
release-link: n/a.
image: n/a.
logo: n/a.
demo: n/a
links: n/a
running-instance: n/a
credits: A. Poltronieri (UniBo), R. Tripodi (UniBo)
related-components:
  - File scraper
    - Internet Culturale Scraper
    - Hemeroteca Digitale Scraper
    - DigiPress Scraper
  - Ocr script
bibliography: n/a
---

# Textual Corpus Population

This repository contains the code for downloading and digitising documents used as a corpus for the [Polifonia Project](https://polifonia-project.eu/).
The repository contains two main types of code:
* file scrapers that automate the download of big repositories of textual data;
* OCR script for digitising the downloaded files. 

---
## Running Docker Image

You can launch the `ocr_script` by launching a Docker container based on the image created using the Dockerfile available in this repository.
To launch the Docker, you will need to:

Pull the Docker Image:
```
docker pull andreamust/ocr-app:0.3
```
Create a folder containing the files from ocrise and download the `.env` file from this folder. The paths to these two items should be specified in the `docker run` command, and should replace the placeholders `<path_to_input_folder>` and `<path_to_.env_file>`. 

Run the Docker Container:
```
docker run --name ocr-script --rm -v <path_to_input_folder>:/app/eval_files -it --env-file <path_to_.env_file> andreamust/ocr-app:0.3
```

Both the `input folder` and the `.env` file will be Docker Bind Mounts will hence allow to store files and change parameters on the go.

For the parameter accepted in the `.env` file, please refer to the documentation below. 
Notice that the `.env` file handles boolean parameters differently, i.e. you only need to enter any character to indicate `True`, and leave the field blank to indicate `False`. 
Also, the file does not accept whitespace, and strings must be entered without quotes.


## Information on installation and setup
For running all the scripts you need to have Python (3.6+, version 3.9 suggested) and pip3 installed on your machine.
Instructions for installing Python and pip can be found on the [Python download page](https://www.python.org/downloads/).

Once Python is installed, it is necessary to clone the repository using git (installation information on [this page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)):

```
git clone https://github.com/polifonia-project/OCR.git
```

The libraries needed to execute all scripts can be installed running:
```
pip install requirements.txt
```

For running the OCR Script it is required to install [Tesseract](https://github.com/tesseract-ocr/tesseract) and the trained data for the languages you need to work with.
The full documentation for installing Tesseract and its dependencies can be found in [Tesseract official documentation](https://tesseract-ocr.github.io/tessdoc/Installation.html).

---
## Usage
Since these two types of scripts can also be used as stand-alone software, they are documented separately, while the setup and the requirement installation is documented for all the scripts contained in the repository.

---

## Internet Culturale scraper
For downloading resources from "Internet Culturale" you need to run the ```internet_culturale_scraper.py``` as:
```
python3 src/internet_culturale_scraper.py [-h] [--resource_url] [--output_path]
```

The parameter to pass are described as follows:
```
--resource_url (string):  the url of a resource page on "Internet Culturale" (e.g. "https://www.internetculturale.it/it/913/emeroteca-digitale-italiana/periodic/testata/8670")

--output_path (string):  the existing path in which to save the downloaded resource
```

You can also browse the script's documentation by typing:
```
python3 src/internet_culturale_scraper.py --help
```

The script will download all files related to the given resource to the specified folder. 
Depending on the size of the resource and the speed of the connection, the download may take several hours.

In addition, a log file named ```download_log.txt``` will be generated in the output folder. This file will list:
* the number of files downloaded; 
* the number of errors encountered;
* the list of files not downloaded.

To attempt to download the non-downloaded files again, simply restart the script with the same parameters. 

---
## Internet Culturale Search Results Scraper
This scraper downloads all the results of a search on the **Internet Culturale**. 
To run the script, simply run the ```download_all.py``` script as:
``` 
download_all.py [-h] [--search_url] [--output_path]
```
The parameter to pass are described as follows:
```
--search_url (string): the url of the results page on "Internet Culturale" (e.g. "https://www.internetculturale.it/it/16/search?q=musica&instance=magindice&__meta_typeTipo=testo+a+stampa&__meta_typeLivello=monografia&pag=1")

--output_path (string): the existing path in which to save the downloaded resources
```
The ```search_url``` parameter needs to be the url of a result page of a search on Internet Culturale but without the page number (the last digit(s) at the end of the url).

You can also browse the script's documentation by typing:
```
python3 src/download_all.py --help
```


---

## Hemeroteca Digital scraper

For downloading resources from "Internet Culturale" you need to run the ```internet_culturale_scraper.py``` as:
```
python3 src/hemeroteca_digital_scraper.py [-h] [--resource_url] [--output_path]
```

The parameter to pass are described as follows:
```
--resource_url (string):  the url of a resource page on "Hemeroteca Digital" (e.g. "http://hemerotecadigital.bne.es/results.vm?q=parent%3A0003894964&s=0&lang=es"
```
```
--output_path (string):  the existing path in with to save the downloaded resource
```

You can also browse the script's documentation by typing:
```
python3 src/hemeroteca_digital_scraper.py --help
```

The resource url must be the url of a specific resource search result of the "Query" section, only searching for resource's "Title", and clicking on "Search among free-access titles", as illustrated in the image:
![](etc/img/hemeroteca_digital.png)
Remember to select **only** one resource at the time. 

---

## OCR Script

For digitising the textual documents you need to run ```python3 src/ocr_script.py```.
The script can perform OCR on multiple documents at the time. In particular, it has been developed to automatically perform document digitisation starting from:
* single image files (in multiple formats);
* single .pdf files;
* folders of images;
* folders of pdfs.

The script accepts the following parameters in input:
```
ocr_script.py [-h] [--input_path] [--saved_file_path] [--converted_image_output_path] [--output_format] [--language_mode]
                  [--single_language] [--multiple_langs] [--gray_scale] [--remove_noise]
                  [--thresholding] [--dilate] [--erosion] [--edge_detection] [--skew_correction]
                  [--page_segmentation_mode] [--ocr_engine_mode]

```

The parameter to pass are described as follows:

```
  --input_path (string): the path of the local file to be digitised or the local folder containing the files to be digitised;
```
```
  --saved_file_path (string, default ''): specifies the directory in which to save the output .txt file;
```
```
  --output_format (string, default 'png'): ONLY TO BE USED IF THE INPUT SOURCE IS IN .pdf FORMAT: specifies the format of the conversion from .pdf to image;
```
```
  --converted_image_output_path (string): ONLY TO BE USED IF THE INPUT SOURCE IS A SINGLE .pdf FORMAT: spcifies the directory in which to save the converted images. In the case of a folder of pdf files the converted images will be created in folders located inside the specified folder;
```
```
  --language_mode (string: 'mono' or 'multi'): allows to specify if the content to digitise is in one language or multilingual;
```
```
  --single_language (string): ONLY TO USE IF --language_mode='mono': takes the language parameter as defined in Tesseract documentation;
```
```
  --multiple_langs (boolean): ONLY TO USE IF --language_mode='multi': takes the language parameters as defined in Tesseract documentation, comma separated; 
```
```
  --gray_scale (boolean): enables the gray scale preprocessing;
```
```
  --remove_noise (boolean): enables the remove noise preprocessing;
```
```
  --thresholding (boolean): enables the thresholding preprocessing; 
```
```
  --dilate (boolean): enables the dilate preprocessing; 
```
```
  --erosion (boolean): enables the erosion preprocessing; 
```
```
  --edge_detection (boolean): enables the edge detection preprocessing;
```
```
  --skew_correction (boolean): enables the skew correction preprocessing;
```
```
  --page_segmentation_mode (integer): allows to specify the Tesseract Page Segmentation Mode (PSM), as defined in Tesseract documentation;
```
```
  --ocr_engine_mode (integer): allows to specify the Tesseract Ocr Engine Mode (OEM), as defined in Tesseract documentation;
```

You can also browse the script's documentation by typing:
```
python3 src/ocr_script.py --help
```

For preprocessing, the script reuses the OpenCV library. You can read the [official documentation](https://opencv.org/) for more information on how the preprocessing algorithms work.

With regard instead to the parameters defined by Tesseract (e.g. Page Seg because of Page Segmentation Mode and Ocr Engine Mode), it is possible to read a comprehensive guide in the [Tesseract documentation](https://github.com/tesseract-ocr/tessdoc).
However, here is a quick guide to the PSM parameters:

| Parameter | Description                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------|
| 0         | Orientation and script detection (OSD) only.                                                  |
| 1         | Automatic page segmentation with OSD.                                                         |
| 2         | Automatic page segmentation, but no OSD, or OCR.                                              |
| 3         | Fully automatic page segmentation, but no OSD. (Default)                                      |
| 4         | Assume a single column of text of variable sizes.                                             |
| 5         | Assume a single uniform block of vertically aligned text.                                     |
| 6         | Assume a single uniform block of text.                                                        |
| 7         | Treat the image as a single text line.                                                        |
| 8         | Treat the image as a single word.                                                             |
| 9         | Treat the image as a single word in a circle.                                                 |
| 10        | Treat the image as a single character.                                                        |
| 11        | Sparse text. Find as much text as possible in no particular order.                            |
| 12        | Sparse text with OSD.                                                                         |
| 13        | Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific. | 
---
# Evaluation and Error Analysis
This repository also contains files for the evaluation of some resources downloaded OCRised using the software contained in this repository. 

These files were produced using [ocreval](https://github.com/eddieantonio/ocreval) and contain all the detailed error and accuracy information about the OCR of some samples of resources compared to manually annotated ground-truth files.

The evaluation files can be found in the [evaluation](evaluation) folder, and are in turn divided in two more folders:
* the [ground_truth](evaluation/ground_truth) folder contains the manually annotated filed for evaluating the automatically generated ones;
* the [accuracy](evaluation/accuracy) folder contains the files generated with ocreval and contain the error analysis logs.

---
# License

MIT License

Copyright (c) 2021 Andrea Poltronieri, Rocco Tripodi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.