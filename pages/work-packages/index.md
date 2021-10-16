---
layout: default
title: Work packages
has_children: true
has_toc: false
nav_order: 5
---

# {{ page.title }}

<ul>
{% assign children_list = site.pages | where: "parent", page.title %}
{% for child in children_list %}
<li><a href="{{ child.url | absolute_url }}">{{ child.title }}</a></li>
{% endfor %}
</ul>

