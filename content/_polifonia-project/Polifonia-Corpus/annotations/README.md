
# Annotations of the Polifonia Textual Corpus

This repository contains the annotations of the Polifonia Textual Corpus.

The corpus is dived into four modules:
- the Wikipedia module
- the Books module
- the Periodicals module
- the Polifonia Pilots module

Each module (except the Pilot module) contains documents in six languages: Dutch (NL), English (EN), French (FR), German (DE),Italian (IT) and Spanish (ES).

## Annotation Pipeline

The annotations of the corpus was produced using cutting-edge Natural Language Processing technologies.
We annotated each text of the corpus with a NLP pipeline composed of:

1. Sentece splitting
2. Tokenization
3. Lemmatization
4. Part-of-speech tagging
5. Word Sense Disambiguation
6. Named Entity Recognition
7. Entity Linking

Steps 1-4 and 6 have been conducted using the **[SpaCy](http://spacy.io)** NLP library.
For each language of the corpus we used a dedicated SpaCy Model:

| lang | model name      |
|------|-----------------|
| DE   | de_core_news_lg |
| EN   | en_core_web_trf |
| ES   | es_core_news_lg |
| FR   | fr_core_news_lg |
| IT   | it_core_news_lg |
| NL   | nl_core_news_lg |

Steps 5 and 7 require more sophisticated technologies.
For this reason, we used **[EWISER](https://github.com/SapienzaNLP/ewiser)** for step 5 (Word Sense Disambiguation) for English.
The other languages of the corpus have been annotated using a new system developed within the project.
It exploits recent advantages on lexical semantics and in particular on the representation of word senses (**[ARES](http://sensembert.org/)**) and a powerful WSD model (**[WSD-games](https://github.com/roccotrip/wsd_games_emb)**).
The advantages of this new model are based on the fact that it is accurate, fast and can work efficiantly on different languages.
For step 7 we used **[ExTenD](https://github.com/SapienzaNLP/extend)** for English.
For the other language of the corpus we adapted **[WSD-games](https://github.com/roccotrip/wsd_games_emb)** to work on the entity linking task.
Also in this case the model is accurate, fast and can work efficiantly on different languages.


## Annotation Example
The annotations of the Polifonia Textual Corpus are provided in **[CoNLL-U format](https://universaldependencies.org/format.html)**.
Given an input sentence (from the English Wikipedia module) such as:

> James H. Mathis Jr. (born August 1967), known as Jimbo Mathus, is an American singer-songwriter and guitarist, best known for his work with the swing revival band Squirrel Nut Zippers.

the resulting annotation will start with metadata information:


> #polifonia_doc_id = 32607842_bn___02615097n.html

Tha provides an unique identifier for the document and in this case is composed of two identifiers: the first one is the BabelNet id of the corresponding Wikipedia page (32607842_bn), the second part is the Wikipedia identifier of the page (02615097n).

> #polifonia_sent_id = sent_0

Then there is a progressive number for each sentence the document.

> #sent = James H. Mathis Jr. (born August 1967), known as Jimbo Mathus, is an American singer-songwriter and guitarist, best known for his work with the swing revival band Squirrel Nut Zippers. 

And then there is the text of the sentence.

Afther the metadata there is the sentence annotation: 

| token_id  | word form                  | lemma | POS | WordNet sense | NER class | NER BIO tag | Entity Linking ------- | is a musical concept? |
|-----------|----------------------------|-------|-----|---------------|-----------|-----------|---------------------|-----------------------|
| token_0   | James	                     | James	| PROPN	|               | PERSON	  | B	      | James H. Mathis Jr.	 | 	0                    |
| token_1   | H.	                        | H.	| PROPN		|               | PERSON	| I		| 	0                  | 0                     |
| token_2	  | Mathis	                    | Mathis	| PROPN	| 	             | PERSON	| I		| 	0                  | 0                     |
| token_3	  | Jr.	                       | Jr.	| PROPN	| 	             | PERSON	| I		| 	0                  | 0                     |                                        
| token_4	  | (	                         | (	| PUNCT	| 	             | 	| O		| 	0                  | 0                     |
| token_5	  | born	                      | bear	| VERB	| wn:02518161v	 | 	| O		| 	0                  | 0                     |
| token_6	  | August	                    | August	| PROPN	| 	             | DATE	| B	| August 1967         | 0                     | 		0|
| token_7	  | 1967	 | 1967	 | NUM		 |   | DATE	 | I	 | 		0   |     |     |     |     |     |     |     |
| token_8	  | )	                         | )	| PUNCT	| 	             | 	| O	| 		0                 | 0                     |
| token_9	  | ,	                         | ,	| PUNCT	| 	             | 	| O	| 		0                 | 0                     |
| token_10	 | known                      | 	know	| VERB	| wn:01426397v	 | 	| O	| 		0                 | 0                     |
| token_11	 | as	                        | as	| ADP	| 		            | | O		| 	0                  | 0                     |                                              
| token_12	 | Jimbo	                     | Jimbo	| PROPN	| 	             | PERSON	| B	| Jimbo Mathus	       | 0                     |
| token_13	 | Mathus	                    | Mathus	| PROPN	| 	             | PERSON	| I		| 	0                  | 0                     |
| token_14	 | ,	                         | ,	| PUNCT	| 	             | 	| O		| 	0                  | 0                     |                                       
| token_15	 | is	                        | be	| AUX	| 		            | | O		| 	0                  |  0 |                                                
| token_16	 | an	                        | an	| DET	| 		            | | O		| 	0                  |  0 |
| token_17	 | American	                  | american	| ADJ	| wn:02927512a	 | NORP	| B	| United States	      | 0 |
| token_18	 | singer	                    | singer	| NOUN	| wn:10599806n	 | 	| O	| 	0                  | 	1                  |
| token_19	 | -	                         | -	| PUNCT		| 	             | | O		| 	0                  |  0|                       
| token_20	 | songwriter	                | songwriter	| NOUN	| wn:10624540n	 | 	| O	| 	0                  | 	1                             |
| token_21	 | and	                       | and	| CCONJ	| 	             | 	| O		| 	0                  |  0 | 
| token_22	 | guitarist	                 | guitarist	| NOUN	| wn:10151760n	 | | 	O | 	0                  | 		1                 |
| token_23	 | ,                          | 	,	| PUNCT	| 	             | | 	O	| 		0                 |  0 |            
| token_24	 | best	                      | well	| ADV	| wn:00011093r	 | 	| O	| 		0                 | 0 |
| token_25	 | known	                     | know	| VERB	| wn:00596644v	 | 	| O	| 		0                 |  0 |
| token_26	 | for	                       | for	| ADP		| 	             |  | O	| 		0                 |  0 |                                            
| token_27	 | his	                       | his	| PRON		| 	             |  | O	| 		0                 |  0 |
| token_28	 | work	                      | work	| NOUN	| wn:05755883n	 | 	| O		| 	0                  | 0 |
| token_29	 | with	                      | with	| ADP	| 		            |  | O	| 		0                 |  0 |                                               
| token_30	 | the	                       | the	| DET	| 	             | 	| O		| 	0                  |  0 |                                                      
| token_31	 | swing	                     | swing	| NOUN	| wn:07066042n	 | 	| O	| 0                   | 		1                                       |
| token_32	 | revival	                   | revival	| NOUN	| wn:01047338n	 | 	|  O	| 	0	                 | 0                                   |
| token_33	 | band	                      | band	| NOUN	| wn:08240169n	 | | 	O 	| 	0 |  1 |
| token_34	 | Squirrel	                  | Squirrel	| PROPN		|               | ORG	| B	| Squirrel Nut Zippers	|  0 |  0 |
| token_35	 | Nut	                       | Nut	| PROPN		|               |  ORG	| I	| 		0 |  0 |                             
| token_36	 | Zippers	                   | Zippers	| PROPN	| 	             | ORG	| I		| 	0 | 0 |
| token_37	 | .	                         | .	| PUNCT	| 	             | 	| O	| 	0 | 0 |


## The Wikipedia module
It was created selecting from **[BabelNet domains](http://lcl.uniroma1.it/babeldomains/)** all the **[Wikipedia](https://www.wikipedia.org)** musical pages.

### Annotations
The annotation of the module can be downloaded from:

| lang | url   |
|------|-------|
| DE   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6702689.svg)](https://doi.org/10.5281/zenodo.6702689)|
| EN   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6759156.svg)](https://doi.org/10.5281/zenodo.6759156)|
| ES   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6759021.svg)](https://doi.org/10.5281/zenodo.6759021)|
| FR   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6759025.svg)](https://doi.org/10.5281/zenodo.6759025)|
| IT   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6759017.svg)](https://doi.org/10.5281/zenodo.6759017)|
| NL   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6757537.svg)](https://doi.org/10.5281/zenodo.6757537)|

## The Books module
It was created with the help of musicologists that provided the titles of different influencial music books.

### Annotations

At this stage, the annotations of the Books module are only available to the Polifonia consortium members in accordance with the heterogeneous licensing of the Books sources. Interested parties may contact us, and we will evaluate the sharing of the annotated data.

## The Periodicals module
It was created with the help of musicologists that provided the titles of different influencial music periodicals.

### Annotations

At this stage, the annotations of the Periodicals module are only available to the Polifonia consortium members in accordance with the heterogeneous licensing of the Periodicals sources. Interested parties may contact us, and we will evaluate the sharing of the annotated data.

## The Polifonia Pilots module
It was created collecting the textual material selected by five **[Polifonia Pilots](https://polifonia-project.eu/pilots/)**:
- BELLS
- CHILD
- MEETUPS
- MUSICBO
- ORGANS


### Annotations

At this stage, the annotations of the Pilots module are only available to the Polifonia consortium members in accordance with the heterogeneous licensing of the Pilots sources. Interested parties may contact us, and we will evaluate the sharing of the annotated data. Texts collected for Child and Meetups Pilots are royalty-free, therefore we release their annotations that can be downloaded from the table below:

| Pilot   | url   |
|---------|-------|
| CHILD   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6759261.svg)](https://doi.org/10.5281/zenodo.6759261) |
| MEETUPS | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6759272.svg)](https://doi.org/10.5281/zenodo.6759272) |
