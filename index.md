---
layout: default
title: Home
nav_order: 0
permalink: /
ecosystem-release: v1-alpha
---

# Polifonia Ecosystem ({{ page.ecosystem-release }})
{: .fs-9 }

Data, software, and documentation of the output of the EU H2020 project [Polifonia]({{ site.main-project-url }}.). 
{: .fs-6 .fw-300 }

---

## Components 

{% assign types =  site.documents  | map: 'type' | join: ','  | split: ',' | uniq %}
{% for type in types %}
{% if type != "" %}
### {{ type }}
	{% assign components =  site.documents  | where: 'type',type %}
	{% for component in components %}
- [{{ component.name }}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endfor %}

## Repositories
Polifonia content is managed on [GitHub](http://github.com/{{ site.github }}).

