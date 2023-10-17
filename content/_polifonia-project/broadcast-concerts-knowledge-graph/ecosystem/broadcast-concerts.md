---
component-id: broadcast-concerts-knowledge-graph
type: KnowledgeGraph
name: Broadcast Concerts Knowledge Graph
description: The NISV knowledge graph for broadcast concerts. This knowledge graph contains metadata of more than 75,000 concerts broadcast on Dutch public service TV and radio. The source of the knowledge graph is the archival metadata stored at the Netherlands Institute for Sound & Vision.
resource:
 - https://cat.apis.beeldengeluid.nl/#transientDatasources=https%3A%2F%2Fcat.apis.beeldengeluid.nl%2Fsparql&query=PREFIX%20sdo%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0A%0A%23%20Show%20the%20ID%20and%20title%20of%20all%20concerts%20that%20are%20part%20of%20the%20Dutch%20Broadcast%20Concert%20%0A%23%20(MOZ)%20collection%2C%20in%20alphabetical%20order%0A%0ASELECT%20DISTINCT%20%3FprogramUri%20%3FprogramName%0AWHERE%0A%7B%0A%20%23%20Filter%20for%20programmes%20belonging%20to%20the%20series%20%22Muziekopnamen%20Zendgemachtigden%20(MOZ)%22%2C%20using%20its%20ID%0A%20%3FprogramUri%20sdo%3ApartOfSeason%2Fsdo%3ApartOfSeries%20%3Chttp%3A%2F%2Fdata.beeldengeluid.nl%2Fid%2Fseries%2F2101608030025711131%3E%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20sdo%3Aname%20%3FprogramName%20.%20%0A%7D%20ORDER%20BY%20%3FprogramName
work-package: 
- WP2
pilot:
- Interlink
project: polifonia-project
doi: 10.5281/zenodo.7377532
copyright: Each concert has its own license, determine using the NISV rules for licensing. Where possible, this is a CC license. The license is stated in the triples for that concert.
contributors:
- Willem Melder
- Mari Wigham
- Govert Brinkmann
related-components:
- documentation: 
  - broadcast-concerts-docs-melody
  - broadcast-concerts-docs-blog
- reuses:
  - https://schema.org
  - broadcast-concerts-sparql-endpoint
- story:
  - "William#1_EuropeanFolkMusic"
- persona:
  - William

---
# Broadcast Concerts Knowledge Graph

The NISV knowledge graph for broadcast concerts. This knowledge graph contains metadata of more than 75,000 concerts broadcast on Dutch public service TV and radio. 

## Knowledge Graph description
The source of the knowledge graph is the archival metadata stored at the Netherlands Institute for Sound & Vision. The concerts (and the rest of the NISV archive) are available via the [Sound & Vision SPARQL endpoint](https://cat.apis.beeldengeluid.nl/sparql). The exact concert collection can be accessed via the query in [this link](https://cat.apis.beeldengeluid.nl/#transientDatasources=https%3A%2F%2Fcat.apis.beeldengeluid.nl%2Fsparql&query=PREFIX%20sdo%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0A%0A%23%20Show%20the%20ID%20and%20title%20of%20all%20concerts%20that%20are%20part%20of%20the%20Dutch%20Broadcast%20Concert%20%0A%23%20(MOZ)%20collection%2C%20in%20alphabetical%20order%0A%0ASELECT%20DISTINCT%20%3FprogramUri%20%3FprogramName%0AWHERE%0A%7B%0A%20%23%20Filter%20for%20programmes%20belonging%20to%20the%20series%20%22Muziekopnamen%20Zendgemachtigden%20(MOZ)%22%2C%20using%20its%20ID%0A%20%3FprogramUri%20sdo%3ApartOfSeason%2Fsdo%3ApartOfSeries%20%3Chttp%3A%2F%2Fdata.beeldengeluid.nl%2Fid%2Fseries%2F2101608030025711131%3E%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20sdo%3Aname%20%3FprogramName%20.%20%0A%7D%20ORDER%20BY%20%3FprogramName)

Each concert has its own license, determine using the NISV rules for licensing. Where possible, this is a CC license. The license is stated in the triples for that concert.

## Competency questions related to the Broadcast Concerts Knowledge Graph
William:

* In which collections/datasets does song X occur?

* Which composers and performers are related to these compositions?'

*  What are the relations between the relevant countries, compositions, composers and performers in the various collections?

* How many search results are there per time period?

* How many search results are there per genre?

## MELODY Data stories
[MELODY data story about the broadcast concerts collection](https://projects.dharc.unibo.it/melody/sound_and_vision/dutch_broadcast_concert_collection)
## Blog

This knowledge graph is further documented in this [this blog](https://labs.beeldengeluid.nl/blogs/moz-dataset-blog)

## Additional Information
### Queries
See the example queries listed in the client at the [Sound & Vision SPARQL endpoint](https://cat.apis.beeldengeluid.nl/sparql)
