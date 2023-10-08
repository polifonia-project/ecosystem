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
        'Documentation',
        'Persona',
        'RequirementsCollection', 
        'Story',
        'Tutorial'
        ],
      datasets: [{
        label: 'No. of Reports',
        data: [7, 22, 2, 35, 1],
        borderWidth: 3
      }]
    }
  });
</script>

{% assign report_data = "Report,RequirementsCollection,Story,Persona,Mockup,Surbey,InPresenceGroup,Documentation,Tutorial,EvaluationReport" | split: "," %}
{% for type in report_data %}
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