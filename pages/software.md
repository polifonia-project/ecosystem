---
id: software
name: Components of type Software
description: List of components of type software
layout: default
title: Software
nav_order: 13
permalink: /software.html
---

# Software

<div id="chart_container_software"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
        {x: "Software", value: 8},
        {x: "UserInterface", value: 2}
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
    chart.container('chart_container_software');
    chart.draw();
  });
  </script>

## List of components 
{% assign software_data = "Software,Workflow,API,UserInterface,SofwareLibrary,DockerImageContainer,Notebook,Script" | split: "," %}
{% for type in software_data %}
{% if type != "" %}
{% assign numberOf = site.documents  | where: 'type',type | size %}
{% if numberOf > 0 %}
### {{ type }} ({{numberOf}})
	{% assign components =  site.documents  | where: 'type',type %}
	{% include reeco-components-table.html components=components %}
{% endif %}
{% endif %}
{% endfor %}