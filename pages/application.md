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

This section collects project outputs that are released as *application*.
The ecosystem considers applications executable systems and tools produced by the project for the end-user to achieve a certain task computationally.
We distinguish [applications](applications.html) from [software](software.html), where software can be copied, moved, and executed in multiple different applications (each in relation to some usage senarios).
Applications include various types of artifacts such as Web Applications, Web sites, and Command Line Interface (CLI) tools.

<div id="chart_container_application"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
        {x: "Application", value: 1},
        {x: "CLITool", value: 1},
        {x: "WebApplication", value: 4}
        {x: "SPARQLEndpoint", value: 2}
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


{% assign apps_data = "Application,Website,WebApplication,WebService,SPARQLEndpoint,MobileApp,CLITool" | split: "," %}
{% for type in apps_data %}
{% if type != "" %}
{% assign numberOf = site.documents  | where: 'type',type | size %}
{% if numberOf > 0 %}
### {{ type }}

There are {{numberOf}} components of type {{type}}:
	{% assign components =  site.documents  | where: 'type',type %}
	{% for component in components %}
- [{% if component.name %}{{ component.name }}{%else%}{{ component.component-id}} {%endif%}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endif %}
{% endfor %}
