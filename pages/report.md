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
Reports include various types of digital objects such as documentation, tutorial, requirements collections, stories or persona specifications.

<div id="chart_container_report"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
        {x: "Documentation", value: 4}, 
        {x: "Persona", value: 22}, 
        {x: "RequirementsCollection", value: 2}, 
        {x: "Story", value: 35}, 
        {x: "Tutorial", value: 1}
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

## List of components 
{% assign report_data = "Report,RequirementsCollection,Story,Persona,Mockup,Surbey,InPresenceGroup,Documentation,Tutorial,EvaluationReport" | split: "," %}
{% for type in report_data %}
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