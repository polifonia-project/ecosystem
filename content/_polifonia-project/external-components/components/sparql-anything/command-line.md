---
component-id: sparql-anything-cli
type: CLITool
name: SPARQL Anything Command Line
description: Command line executable of SPARQL Anything
logo: https://avatars.githubusercontent.com/u/79987779?s=200&v=4
work-package:
- WP1
- WP2
- WP3
- WP4
pilot:
- MEETUPS
- CHILD
project: polifonia-project
resource: https://github.com/SPARQL-Anything/sparql.anything/releases
demo: https://github.com/SPARQL-Anything/showcase-tate
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
- informed-by: sparql-anything-requirements
- documentation:
  - sparql-anything-docs
  - sparql-anything-tutorials
- reuses:
  - sparql-anything-java
---

# SPARQL Anything Command Line

The command line interface of SPARQL Anything.
An executable JAR can be obtained from the [Releases](https://github.com/spice-h2020/sparql.anything/releases) page.

The jar can be executed as follows:

```
usage: java -jar sparql.anything-<version>  -q query [-f <output
            format>] [-v <filepath | name=value> ... ]  [-l path] [-o
            filepath]
 -q,--query <query>                    The path to the file storing the
                                       query to execute or the query
                                       itself.
 -o,--output <file>                    OPTIONAL - The path to the output
                                       file. [Default: STDOUT]
 -e,--explain                          OPTIONAL - Explain query execution
 -l,--load <load>                      OPTIONAL - The path to one RDF file
                                       or a folder including a set of
                                       files to be loaded. When present,
                                       the data is loaded in memory and
                                       the query executed against it.
 -f,--format <string>                  OPTIONAL -  Format of the output
                                       file. Supported values: JSON, XML,
                                       CSV, TEXT, TTL, NT, NQ. [Default:
                                       TEXT or TTL]
 -s,--strategy <strategy>              OPTIONAL - Strategy for query
                                       evaluation. Possible values: '1' -
                                       triple filtering (default), '0' -
                                       triplify all data. The system
                                       fallbacks to '0' when the strategy
                                       is not implemented yet for the
                                       given resource type.
 -p,--output-pattern <outputPattern>   OPTIONAL - Output filename pattern,
                                       e.g. 'myfile-?friendName.json'.
                                       Variables should start with '?' and
                                       refer to bindings from the input
                                       file. This option can only be used
                                       in combination with 'input' and is
                                       ignored otherwise. This option
                                       overrides 'output'.
 -v,--values <values>                  OPTIONAL - Values passed as input
                                       parameter to a query template. When
                                       present, the query is pre-processed
                                       by substituting variable names with
                                       the values provided. The argument
                                       can be used in two ways. (1)
                                       Providing a single SPARQL ResultSet
                                       file. In this case, the query is
                                       executed for each set of bindings
                                       in the input result set. Only 1
                                       file is allowed. (2) Named variable
                                       bindings: the argument value must
                                       follow the syntax:
                                       var_name=var_value. The argument
                                       can be passed multiple times and
                                       the query repeated for each set of
                                       values.
 -i,--input <input>                    [Deprecated] OPTIONAL - The path to
                                       a SPARQL result set file to be used
                                       as input. When present, the query
                                       is pre-processed by substituting
                                       variable names with values from the
                                       bindings provided. The query is
                                       repeated for each set of bindings
                                       in the input result set.
```

Logging can be configured adding the following option (SLF4J):
```
-Dorg.slf4j.simpleLogger.defaultLogLevel=trace
```

For more information, please see the [online documentation](https://sparql-anything.readthedocs.io/en/latest/#command-line-interface-cli)

