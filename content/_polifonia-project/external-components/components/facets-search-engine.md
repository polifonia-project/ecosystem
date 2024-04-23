---
component-id: facets-search-engine
name: FACETS search engine
description: "A search engine for music documents"
type: Application
release-date: 11/23
release-number: v0.8
work-package:
- WP1 
- WP3
pilot:
- FACETS
keywords:
  - "information retrieval"
  - "music score"
licence:
- CC-BY_v4
links: 
  - http://neuma-dev.huma-num.fr
  - https://github.com/polifonia-project/facets-search-engine
resource: http://neuma.huma-num.fr
credits: 
- Tiange Zhu (CNAM Paris)
- Philippe Rigaux (CNAM Paris)
- Nicolas Travers (ESILV Paris)
- Raphaël Fournier-S'niehotta (CNAM Paris)
related-components: []
bibliography: {'main-publication':["Zhu, T.; Fournier-S’niehotta, R.; Rigaux, P.; Travers, N., A Framework for Content-Based Search in Large Music Collections (https://www.mdpi.com/2504-2289/6/1/23). Big Data Cogn. Comput. 2022, 6, 23. https://doi.org/10.3390/bdcc6010023"]}
--- 

# FACETS Search Engine

The FACETS search engine is a music search engine. 

It's core component is a efficient indexing procedure to store musical content as n-grams,
for several aspect of music (melody, rhythm, lyrics). It's fully
compatible with state-of-the-art search engine such as ElasticSearch.
