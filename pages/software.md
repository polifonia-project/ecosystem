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

## List of components 
{% assign software_data = "Software,Workflow,API,UserInterface,SofwareLibrary,DockerImageContainer,Notebook,Script" | split: "," %}
{% for type in software_data %}
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