---
layout: default
title: Tags (dev)
nav_order: 8
permalink: /tags.html
---

# Tags

## Work Packages

{% for wp in site.data.wps %}
### {{ wp.name }}
{% assign wp-posts = site.documents | where: "WP", wp.name %}
{% for page in wp-posts %} <span><a href="{{ page.url }}">{{ page.persona }}</a> </span> {% endfor %}
{% endfor %}
