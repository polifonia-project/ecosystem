---
id: software
name: Components of type Software or Application
description: List of components of type software or application
layout: default
title: Tools
nav_order: 13
permalink: /software.html
---

# Tools

This section collects project outputs that are released as *software* or *application*.

The ecosystem considers software any digital object that is being produced by the project to achieve a certain task computationally.
We distinguish software from applications, where software is used (executed) by a user to perform the task.
These include various types of digital objects such as scripts, software libraries, workflows, or APIs.

The ecosystem considers applications executable systems and tools produced by the project for the end-user to achieve a certain task computationally.
We distinguish applications from software, where software can be copied, moved, and executed in multiple different applications (each in relation to some usage senarios).
Applications include various types of artifacts such as Web Applications, Web sites, and Command Line Interface (CLI) tools.

{% assign types_software = "Software,Workflow,API,UserInterface,SoftwareLibrary,DockerImageContainer,Notebook,Script,Application,Website,WebApplication,WebService,SPARQLEndpoint,MobileApp,CLITool" | split: "," | sort %}

<div id="chart_container_software"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
		{% for type in types_software %}
			{% if type != "" %}
				{% assign comps =  site.documents  | where: 'type',type | size%}
				{% if comps > 0 %}
     		   		{x: "{{type}}", value: {{ comps }} },
				{% endif %}
			{% endif %}
		{% endfor %}
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


{% for type in types_software %}
{% if type != "" %}
{% assign numberOf = site.documents  | where_exp: 'item', "item.type == type" | size %}
{% if numberOf > 0 %}
### {{ type }}

There are {{numberOf}} components of type {{type}}:
	{% assign components =  site.documents  | where: 'type',type %}
	{% include reeco-components-table.html components=components %}
{% endif %}
{% endif %}
{% endfor %}