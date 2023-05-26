---
id: data
name: Components of type Data
description: List of components of type data
layout: default
title: Data
nav_order: 12
permalink: /data.html
---

# Data

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

## List of components 
{% assign types_data = "Data,Dataset,Schema,Repository,Registry,Ontology,Corpus,Lexicon,KnowledgeGraph" | split: "," %}
{% for type in types_data %}
{% if type != "" %}
{% assign components =  site.documents  | where: 'type',type %}
{% assign numberOf = components | size %}
{% if numberOf > 0 %}
### {{ type }} ({{numberOf}})
	{% for component in components %}
- [{% if component.name %}{{ component.name }}{%else%}{{ component.component-id}} {%endif%}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endif %}
{% endfor %}
