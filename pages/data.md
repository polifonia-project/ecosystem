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

<!-- Create the canvas for the chart -->
<div>
  <canvas id="data_pie_chart"></canvas>
</div>
<!-- Import chart.js and build the chart -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
  const ctx = document.getElementById('data_pie_chart');

  new Chart(ctx, {
    type: 'doughnut',
    options: {
      responsive: true,
      radius: '70%'
    },
    data: {
      labels: [
        'Corpus',
        'Dataset',
        'KnowledgeGraph', 
        'Lexicon',
        'Ontology',
        'Repository',
        'Schema'
        ],
      datasets: [{
        label: 'No. of Components',
        data: [2, 2, 6, 1, 6, 4, 1],
        borderWidth: 3
      }]
    }
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
