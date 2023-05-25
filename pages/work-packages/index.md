---
layout: default
title: Work packages
has_children: true
has_toc: false
nav_order: 5
---

# {{ page.title }}

The Polifonia Ecosystem, from the perspective of the project work packages.


{% assign children_list = site.pages | where: "parent", page.title %}
{% for child in children_list %}
<div class="wrkpckg">
<h2><a href="{{ child.url | absolute_url }}">{{ child.long-title }}</a></h2>
{{ child.description }}
</div>
{% endfor %}


