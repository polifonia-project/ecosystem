---
component-id: sparql-anything-requirements
type: RequirementsCollection
name: "Requirements of SPARQL Anything"
description: Requirements collection of SPARQL Anything
logo: https://avatars.githubusercontent.com/u/79987779?s=200&v=4
demo: https://github.com/SPARQL-Anything/showcase-tate
licence:
- Apache-2.0
bibliography:
  - main-publication: "Daga, Enrico, Luigi Asprino, Paul Mulholland, and Aldo Gangemi. \"Facade-X: an opinionated approach to SPARQL anything.\" Studies on the Semantic Web 53 (2021): 58-73."
---

# Requirements of SPARQL Anything

The motivation for researching  novel ways to transform non-RDF resources into RDF comes from the scenarios under development in two EU H2020 projects [SPICE](http://spice-h2020.eu) and [Polifonia](http://polifonia-project.eu). 

In Polifonia, a consortium collaborate in developing novel ways for valorising musical cultural heritage, relying on a *linked data* network of resources from many different stakeholders in the cultural sector.
However, the majority of resources involved are not exposed as Linked Data but are released, for example, as CSV, XML, JSON files, or combinations of these formats.

It is clear how the effort required for transforming resources could constitute a significant cost to the project.
In the absence of a strategy to cope with this diversity, content transformation may result in duplication of effort and become a serious bottleneck.

The following Table provides a summary of the design requirements of SPARQL Anything.

| Requirement | Description |
| :---------- | :---------- |
| Transform | Transform several sources having heterogeneous formats |
| Query | Query resources having heterogeneous formats |
| Binary|Support the transformation of binary formats|
| Embed|Support the embedding of content in RDF|
| Metadata|Support the extraction of metadata embedded in files|
| Low learning demands|Minimise the tools and languages that need to be learned|
| Low complexity|Minimise complexity of the queries|
| Meaningful abstraction|Enable focus on data structures rather than implementation details|
| Explorability|Enable data exploration without premature commitment to a mapping, in the absence of a domain ontology.|
| Workflow|Integrate with a typical Semantic Web engineering workflow|
| Adaptable|Be generic but flexible and adaptable|
| Sustainable|Inform into a software that is easy to implement, maintain, and does not have evident efficiency drawbacks|
| Extendable|Support the addition of an open set of formats| 


