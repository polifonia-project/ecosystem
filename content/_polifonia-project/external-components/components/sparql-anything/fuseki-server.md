---
component-id: sparql-anything-server
type: WebServer
name: SPARQL Anything Web Server
description: Web server executable of SPARQL Anything
logo: https://avatars.githubusercontent.com/u/79987779?s=200&v=4
demo: https://github.com/SPARQL-Anything/showcase-tate
resource: https://github.com/SPARQL-Anything/sparql.anything/releases
release-date: 2022/12/18
release-number: v0.8.1
release-link: https://github.com/SPARQL-Anything/sparql.anything/releases/tag/v0.8.1
doi: 10.5281/zenodo.7454360
changelog: https://github.com/SPARQL-Anything/sparql.anything/releases/tag/v0.8.1
licence:
- Apache-2.0
copyright: "Copyright (c) 2022 SPARQL Anything Contributors @ http://github.com/sparql-anything"
contributors:
- Luigi Asprino <https://github.com/luigi-asprino>
- Enrico Daga <https://github.com/enridaga>
- Justin Dowdy <https://github.com/justin2004>
- Marco Ratta <https://github.com/MarcoR1791>
related-components:
- documentation: 
  - sparql-anything-docs
  - sparql-anything-tutorials
- reuses:
  - sparql-anything-java
  - "Apache Jena Fuseki https://jena.apache.org/"
- informed-by:
  - sparql-anything-requirements
---

# SPARQL Anything Web Server

SPARQL Anything is also released as a server, embedded into an instance of the Apache Jena Fuseki server. The server requires Java >= 11 to be installed in your operating system. Download the latest version of the SPARQL Anything server from the releases page. The command line is a file named sparql-anything-server-<version>.jar.

Run the server as follows:
```
java -jar sparql-anything-server-<version>.jar 
```