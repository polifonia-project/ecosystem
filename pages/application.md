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
{% assign apps_data = "Website,WebApplication,WebService,SPARQLEndpoint,MobileApp,CLITool" | split: "," %}
{% for type in apps_data %}
{% if type != "" %}
### {{ type }} ({{ site.documents  | where: 'type',type | size }})
	{% assign components =  site.documents  | where: 'type',type %}
	{% for component in components %}
- [{{ component.name }}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endfor %}
