---
id: application
name: Components of type Application
description: List of components of type application
layout: default
title: Application
nav_order: 14
permalink: /application.html
---

# Application

<div id="chart_container_application"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
        {x: "Application", value: 1},
        {x: "CLITool", value: 2},
        {x: "WebApplication", value: 3}
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
    chart.container('chart_container_application');
    chart.draw();
  });
  </script>

## List of components
{% assign apps_data = "Application,Website,WebApplication,WebService,SPARQLEndpoint,MobileApp,CLITool" | split: "," %}
{% for type in apps_data %}
{% if type != "" %}
{% assign numberOf = site.documents  | where: 'type',type | size %}
{% if numberOf > 0 %}
### {{ type }} ({{numberOf}})
	{% assign components =  site.documents  | where: 'type',type %}
	{% for component in components %}
- [{% if component.name %}{{ component.name }}{%else%}{{ component.component-id}} {%endif%}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endif %}
{% endfor %}
