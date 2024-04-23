---
component-id: tune_family_annotations
name: Tune Family Annotations
description: Annotations of tune family membership for a small subset of *The Session*
type: Repository
release-date: 15/02/2024
release-number: v1.0
work-package: 
- WP3
licence:
- CC_BY_v4
links:
- https://github.com/polifonia-project/folk_ngram_analysis
credits:
- https://github.com/danDiamo
- https://github.com/jmmcd
---

# Tune Family Annotations

Annotations of tune family membership for a small subset of *The Session*.

The format of the data is a `csv`, where `identifiers` is a tune ID from *The Session*, and `tune_family` is a string:

```csv
identifiers,tune_family
1029,Hob or Nob
1104,Blackbird
```

There are 10 tune families in the data, and 314 tunes.

For more details, see:
- Polifonia deliverable 3.6
- *Tune family detection in a corpus of Irish traditional dance tunes*, Danny Diamond, 2024. MSc Thesis, University of Galway. In preparation.

## Selection of tune families

The methodology applied to ground-truth annotation of *The Session* began with a survey of the musicological sources and online resources listed below. All references to tune families and/or similarities within the Irish tradition were noted, which yielded a total of 115 potential tune families. A subset of 21 were chosen, with priority being given to the oldest and most extensive families. These 21 families were then cross-referenced against studies relating to British and North American folk music to identify families which co-occurred in these related traditions. Following the writings of Bayard, Bronson, and Cowdery (see sources listed below) we hypothesised that families presenting with the broadest and most varied forms across multiple traditions constituted the oldest and most fundamental tune families. Such families were deemed most important for inclusion in our ground truth.

For each of the 21 selected tune families, a list of members was compiled based on a comprehensive review of the sources below. It is important to note that all membership assignments were based on existing musicological work identified in the course of this review, rather than being subjectively assigned by the authors.

Working from the membership lists for each of the 21 tune families, we searched *The Session* for occurrences of each individual tune, almost all of which were present in multiple variant forms. New lists were compiled for each family, setting out the specific tune variants contained in the corpus. It was discovered that many of the variants were stored in the corpus under alternate titles to those initially compiled during the literature review. This is a consequence of the multiplicity of historical and contemporary tune titles in the Irish tradition, the generally casual and/or flexible nature of their usage by practitioners, and the oral nature of transmission within the tradition. It is common for multiple melodies to be known by the same title, and also common for multiple titles to be applied to the same melody.

To ensure the robustness of our ground-truth annotation and to ensure its usefulness as a tool for precision ranking of similarity results, we set a minimum family size threshold of 20 unique tune variants: any of our 21 families with less than this number of variants in *The Session* were omitted from the final ground-truth annotation.

In addition to setting the family size threshold, we set a target of 10 tune families for which annotation would be created. This would yield an annotated subset of The Session of sufficient size to be useful in our experimental work, while keeping the annotation task at a manageable scale. We worked through the 21 families, omitting those with less than 20 members in the corpus, retaining and listing the members of families with more than 20 members. When we reached 10 families we halted this work and moved on to the validation step, as set out below.

This methodological step resulted in a subset of 322 tune variants spread across 10 families, containing a range of tune types and time signatures broadly representative of the corpus as a whole. All families were canonical and originated from the 18th century or earlier.

## Validation

As *The Session* is a crowd-sourced resource its content can be affected by issues such as mis-titled tunes, transcription errors, inconsistent formatting, and typographic errors. To guard against errors in the corpus impacting our ground truth data, a manual validation pass was carried out by the author, informed by extensive experience as a practitioner and archivist of Irish traditional music. This validation process entailed inspection of the scores of each of the individual 322 tune variants present in *The Session* to verify that their inclusion in the tune family ground truth annotation was accurate. As a general rule, if a tune variant was not immediately apparent as a tune family member, it was excluded from the annotation. A total of 8 variants were dropped as a result of this validation process, giving a final annotated set of 314 tune variants across the 10 tune families.

## Outputs

The annotation process outputted a list of verified family-member variants present in *The Session* for each of the final 10 tune families. This data is presented here in csv format, with each family-member variant being identified via its unique id number as provided within *The Session* corpus.

## Principal sources of tune family annotation information

- S. P. Bayard, Dance to the fiddle, march to the fife: instrumental folk tunes in Pennsylvania. University Park, USA: Pennsylvania State University Press, 1982
- S. P. Bayard, “Two representative tune families of British tradition,” Midwest Folklore, vol. 4, no. 1, pp. 13–33, 1954, publisher: Indiana University Press.
- B. H. Bronson and F. J. Child, The traditional tunes of the Child ballads: with their texts, according to the extant records of Great Britain and America. Princeton: Princeton University Press, 1959
- B. H. Bronson, “Melodic stability in oral transmission,” Journal of the International Folk Music Council, vol. 3, p. 50, 1951. 
- J. R. Cowdery, “A fresh look at the concept of tune family,”
Ethnomusicology, vol. 28, no. 3, p. 495, Sep. 1984.
- J. R. Cowdery, The melodic tradition of Ireland. Ohio, USA: Kent State University Press, 1990
- A. Fleischmann, Sources of Irish traditional music, c. 1600-1855. New York, USA: Garland, 1998
- R. Henebry, A handbook of Irish music. Cork, Ireland: Cork University Press, 1928
- A. Hillhouse, “Tradition and innovation in Irish instrumental folk music,” Master’s thesis, The University of British Columbia,, Vancouver, Canada, 2005
- [J. Keith, “The Session,” 2001](https://thesession.org)
- [A. Kuntz and V. Pelliccioni, “The traditional tune archive,” 2009](http://www.capeirish.com/webabc)
- F. O’Neill, Irish minstrels and musicians. Chicago, USA: Regan Printing House, 1913
- C. Pendlebury, “Jigs, reels and hornpipes: a history of “traditional” dance tunes of Britain and Ireland,” Master’s thesis, University of Sheffield, Sheffield,
England, 2015
- C. Pendlebury, “Tune families and tune histories: melodic resemblances in British and Irish folk tunes,” Folk Music Journal, vol. 11, no. 5, pp. 67–95,
2020
- [A. Ng, “irishtune.info,” 2000](https://www.irishtune.info)
- C. Walshaw, “A visual exploration of melodic relationships within traditional
music collections,” in 2018 22nd International Conference Information Visualisation (IV). Fisciano, Italy: IEEE, Jul. 2018, pp. 478–483.


  

