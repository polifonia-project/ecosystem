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
