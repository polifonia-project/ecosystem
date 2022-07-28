# Queries and usage

Generate list of biographies and related files.
```
fx -q queries/list-sample.sparql -o data/biographies.csv -f CSV
```
Generate sentences KG data
```
fx -q queries/sentences.sparql -i data/biographies.csv -p "data/sentences/?fileId.ttl" -f TTL
```
Statistics:
```
$ fx -q queries/statistics.sparql -l data/meetups/
-------------------------------
| key                 | value |
===============================
| "Meetups"           | 74445 |
| "Persons mentioned" | 51425 |
| "Subjects"          | 1002  |
| "Places mentions"   | 5595  |
| "Time expressions"  | 79838 |
-------------------------------
```

[part above to be updated...]

```
fx -q queries/sentences.sparql -v fileId=10085 -v subject=http://dbpedia.org/resource/Edward_Elgar
```