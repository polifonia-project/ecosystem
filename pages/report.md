---
id: report
name: Components of type Report
description: List of components of type report
layout: default
title: Reports
nav_order: 15
permalink: /report.html
---

# Reports

This section collects project outputs that are released as *report*.
The ecosystem considers reports any digital object that specifies, describes, or represents facts about the project's domain of interest.
Reports differ from *data* as they are mainly directed to human consumption, rather than computational treatment.
Reports include various types of digital objects such as [documentation](#documentation), [tutorial](#tutorial), [requirements collections](#requirementscollection), [stories](#story) or [persona](#persona) specifications.

{% assign types_report = "Report,RequirementsCollection,Story,Persona,Mockup,Surbey,InPresenceGroup,Documentation,Tutorial,EvaluationReport" | split: "," |sort %}

<div id="chart_container_report"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
		{% for type in types_report %}
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
    // chart.title("Report Components by Type");
    // add the data
    chart.data(data);
    // sort elements
    chart.sort("desc");  
    // set legend position
    chart.legend().position("right");
    // set items layout
    chart.legend().itemsLayout("vertical");  
    // display the chart in the container
    chart.container('chart_container_report');
    chart.draw();
  });
  </script>

{% for type in types_report %}
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