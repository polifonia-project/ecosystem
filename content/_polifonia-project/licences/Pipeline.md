---
component-id: licences-pipeline
name: Licences KG generation pipeline
description: Resources for the Polifonia Licences KG, containing licence information of the resources from third-parties that the project reused.
type: Software
release-date: 28/04/2023
release-number: v0.3
work-package: 
- WP2
licence: 
- "CC-BY_v4"
doi: 10.5281/zenodo.7875034
links:
credits:
- "Enrico Daga <https://github.com/enridaga>"
- "Jason Carvalho <https://github.com/jasemk>"
- "Marco Gurrieri"
related-components:
- reuses:
  - sparql-anything-cli
  - Dalicc, https://www.dalicc.net/
  - musow-licences
---
# Licences KG generation pipeline

This project includes resources for the Polifonia Licences KG, containing licence information of the resources from third-parties that the project reused.

In what follows, fx refers to the following command line `java -jar sparql-anything-<version>-.jar`.
	
## Knowledge Graph Construction

### Dalicc licence descriptions
We reuse a catalogue of machine readable licences from the [Dalicc project](https://www.dalicc.net/).

```bash
fx -q queries/harvest-dalicc.sparql -f TTL -o knowledgegraph/dalicc.ttl
```

### Generate `external-datasets-licences.ttl`
This part of the dataset comes from a survey of reused datasets in the Polifonia project
From the spreadhseet in `data/` to the RDF file.

```bash
fx -q queries/datasets-kg.sparql -f TTL -o knowledgegraph/datasets-licences.ttl
```
### MusoW licences
This part of the knowledge graph includes a snapshot of the [musoW KG](https://projects.dharc.unibo.it/musow/): `knowledgegraph/musow.ttl`

```bash
fx -q queries/download-musow.sparql -f TTL -o knowledgegraph/musow.ttl
```

musoW licence annotations are aligned to Dalicc entities, alignmments are stored at `knowledgegraph/musow-alignments.ttl`
Such alignments are used to generate the musow-licences part of the KG:

```bash
fx -q queries/musow-licences.sparql -f TTL -o knowledgegraph/musow-licences.ttl
```

However, musoW licence annotations are complemented with additional metadata from [experimenting with extracting and linking licence information from web resources with the help of LLMs](https://github.com/polifonia-project/musow-licences-experiments-llm). Results are included in file: `knowledgegraph/musow-licences-llm.ttl`


## Queries 

### List of can, cannot, and must terms for each dataset

```
fx -q queries/terms-view.sparql -l knowledgegraph/
```

### Statistics of datasets / actions

```
fx -q queries/datasets-by-licence.sparql -l knowledgegraph/

fx -q queries/terms-stats.sparql -l knowledgegraph/
```





