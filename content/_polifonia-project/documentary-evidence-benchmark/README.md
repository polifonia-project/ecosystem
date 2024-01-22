---
component-id: documentary-evidence-benchmark
name: Documentary evidence benchmark
brief-description: the benchmark for the extraction of documentary evidence
type: Dataset
release-date: 25/04/2022
release-number: v1.0
work-package: 
- WP1
- WP4
pilot:
- CHILD
licence:
- Apache-2.0
doi: 10.5281/zenodo.6866982
related-component:
- led
- sparql-anything-cli
credits:
- Enrico Daga <https://github.com/enridaga>
---
# Documentary evidence benchmark

This project provides the benchmark for the extraction of documentary evidence, taking the Listening Experience Database (LED) as a reference.

Below is information on the tasks, data, and the process that generated them from the LED database, also included ([led-SNAPSHOT.nt.tar.gz](led-SNAPSHOT.nt.tar.gz)).

## Files

### Sources

- [CHILD exemplar sources.xlsx](CHILD exemplar sources.xlsx) A curated list of sources from LED that also include experiences relevant to childhood
- [corpus/](corpus/) A folder containing `.txt` files of the books selected sources
- [led-SNAPSHOT.nt.tar.gz](led-SNAPSHOT.nt.tar.gz) an archive of the Listening Experience Database in RDF/N-triples

### Benchmark data
These are the data that can be used for benchamrking knowledge extraction processes

- `sources.csv` (columns: `source,file,title,author,author_name,time`)
- `experiences.csv` (columns: `file,exp,excerpt,text,time,place,listening_to,environment,listener,listener_label,type,instrument,genre`)
- `child.csv` includes the list of listening experiences that were marked by domain experts to be relevant to childhood

## Tasks
We briefly describe each task and refer to the relevant data.

### Task 1: retrieve documentary evidence relevant to musical experiences

This task refers to automatically identify text fragments that contain an account of listening experience, from a selection of texts (in `corpus/`).

Input: `sources.csv` (`source,file,title,author,author_name,time` both the textual content in `corpus/` and the related metadata can be used)

Target: for each `file`, find paragraphs that match (or overlap) with the ones in `experience (text)`  (the other columns except `file` should be ignored and not used by the approach)

### Task 2: retrieve documentary evidence relevant to childhood

This task is equivalent to Task 1, except that the output should match the list of experiences in `child.csv`

### Task 3: populate documentary evidence entities metadata

This task operates on the expected output from the previous ones. Given a list of texts and related excerpts, populate the metadata describing the listening experience.

Input: `sources.csv` (all columns), `experiences.csv` (`file,exp,excerpt,text`)

Target: automatically derive columns in `experiences.csv`: `place,listening_to,environment,listener,listener_label,type,instrument,genre`

### Task 4: time-indexing of documentary evidence

This task operates on the expected output from the previous ones. Given a list of texts and related excerpts, populate the metadata describing the listening experience.

Input: `sources.csv` (all columns), `experiences.csv` (`file,exp,excerpt,text`)

Target: automatically derive columns in `experiences.csv`: `time`


## Benchmark construction process
The data was generated using [SPARQL Anything](http://sparql-anything.cc), the folling `fx` command shall be interpreted as `java -jar sparql-anything-0.7.0-SNAPSHOT.jar`.

Generate list of sources from exemplary LED entities (uncompress the `led-SNAPSHOT.nt.tar.gz` archive before executing the following).

```
fx -q queries/sources.sparql -l led-SNAPSHOT.nt -o data/sources.csv -f CSV
fx -q queries/experiences.sparql -l led-SNAPSHOT.nt -o data/sources.csv -f CSV
fx -q queries/child.sparql -l led-SNAPSHOT.nt -o data/child.csv -f CSV
```


### Statistics

|title|count|
|-----|-----|
|sources|25|
|places|277|
|genres|100|
|listeners|194|
|instruments|64|
|experiences relevant to childhood|40|
|experiences|1248|
|performances/pieces|1121|
