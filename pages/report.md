---
id: report
name: Components of type Report
description: List of components of type report
layout: default
title: Report
nav_order: 15
permalink: /report.html
---

# Report

## List of components 
{% assign report_data = "RequirementsCollection,Story,Persona,Mockup,Surbey,InPresenceGroup,Documentation,Tutorial,EvaluationReport" | split: "," %}
{% for type in report_data %}
{% if type != "" %}
### {{ type }} ({{ site.documents  | where: 'type',type | size }})
	{% assign components =  site.documents  | where: 'type',type %}
	{% for component in components %}
- [{{ component.name }}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endfor %}
