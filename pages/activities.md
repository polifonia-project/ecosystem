---
id: application
name: Activities
description: List of activities (ecosystem containers)
layout: default
title: Activities
nav_order: 13
permalink: /activities.html
---

# Activities
Ecosystem activities include project work packages, tasks, working group, or contributing sub-projects such as spin-off open source initiatives.

{% assign types_activity = "Container,Project,WorkingGroup,WorkPackage,Task,UseCase,Pilot" | split: "," %}

{% for type in types_activity %}
{% if type != "" %}
	{% assign components =  site.documents  | where: 'type',type %}
	{% assign pages =  site.pages | where: 'type',type %}
    {% assign numberOfc = components|size%}
    {% assign numberOfp = pages|size%}
    {% assign numberOf = numberOfc | plus: numberOfp %}
<!-- {{type}} = {{numberOf}} -->
{% if numberOf > 0 %}
### {{ type }} ({{numberOf}})
	{% for p in pages %}
- [{% if p.name %}{{ p.name }}{%else%}{{ p['container-id'] }} {%endif%}]({{ p.url | relative_url }})	{% endfor %}	{% for component in components %}
- [{% if component.name %}{{ component.name }}{%else%}{{ component.container-id}} {%endif%}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endif %}
{% endfor %}

