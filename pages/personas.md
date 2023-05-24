---
layout: default
title: Requirements
nav_order: 11
permalink: /personas.html
---

# {{ page.title }}

The Polifonia Ecosystem, from the perspective of the target communities, exemplified by a set of Persona.

{% assign children_list = site.documents | where: "type", "Persona" %}
{% for child in children_list %}
### <a href="{{ child.url | absolute_url }}">{{ child.long-title }}</a>
{{ child.description }}
{% assign stories = site.documents | where: "type", "Story" %}
<ul>
{% for story in stories %}
{% if story['related-components'] %}
{% assign related = story['related-components'] %}
{% for r in related %} 
  {% if r.persona contains child.component-id %}
<li> <a href="{{ story.url | absolute_url }}">{{ story.name }}</a></li>
  {% endif %}
{% endfor %}
{% endif %}
{% endfor %}
</ul>
{% endfor %}
