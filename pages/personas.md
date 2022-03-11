---
layout: default
title: Personas
nav_order: 11
permalink: /personas.html
---

# {{ page.title }}

The Polifonia Ecosystem, from the perspective of the target communities, exemplified by a set of Persona.

{% assign children_list = site.documents | where: "type", "Persona" %}
{% for child in children_list %}
## <a href="{{ child.url | absolute_url }}">{{ child.long-title }}</a>
{{ child.description }}
{% assign stories = site.stories | where: "persona", child.component-id %}
<ul>
{% for story in stories %}
<li> <a href="{{ story.url | absolute_url }}">{{ story.name }}</a></li>
{% endfor %}
</ul>
{% endfor %}
