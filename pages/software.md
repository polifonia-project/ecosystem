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
{% assign software_data = "Workflow,API,UserInterface,SofwareLibrary,DockerImageContainer,Notebook,Script" | split: "," %}
{% for type in software_data %}
{% if type != "" %}
### {{ type }} ({{ site.documents  | where: 'type',type | size }})
	{% assign components =  site.documents  | where: 'type',type %}
	{% for component in components %}
- [{{ component.name }}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endfor %}