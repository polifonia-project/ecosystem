---
id: data
name: Components of type Data
description: List of components of type data, schemas, ontologies
layout: default
title: Data
nav_order: 12
permalink: /data.html
---

# Data

This section collects project outputs that are released as *data*.
The ecosystem considers data any digital object that specifies, describes, or represents facts about the project's domain of interest.
These include various types of digital objects such as [datasets](#dataset), [corpora](#corpus), [ontologies](#ontology), or [repositories](#repository).

<div id="chart_container_data"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
        {x: "Corpus", value: 1},
        {x: "Dataset", value: 4},
        {x: "KnowledgeGraph", value: 1},
        {x: "Lexicon", value: 1},
        {x: "Ontology", value: 6},
        {x: "Repository", value: 4},
        {x: "Schema", value: 2}
    ];
    // create the chart
    var chart = anychart.pie3d();
    // set the chart title
    // chart.title("Polifonia Project Components by Type");
	// add the data
    chart.data(data);
	// sort elements
    chart.sort("desc");  
	// set legend position
    chart.legend().position("right");
	// set items layout
    chart.legend().itemsLayout("vertical");
	// display the chart in the container
    chart.container('chart_container_data');
    chart.draw();
  });
  </script>

{% assign types_data = "Data,Dataset,Schema,Repository,Registry,Ontology,Corpus,Lexicon,KnowledgeGraph" | split: "," %}
{% for type in types_data %}
{% if type != "" %}
{% assign components =  site.documents  | where: 'type',type %}
{% assign numberOf = components | size %}
{% if numberOf > 0 %}
### {{ type }}

There are {{numberOf}} components of type {{type}}:
	{% for component in components %}
- [{% if component.name %}{{ component.name }}{%else%}{{ component.component-id}} {%endif%}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endif %}
{% endfor %}
