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
<ul class="inline">
{% for page in wp-posts %}
<li> {% if page.name %}<a href="{{ page.url | relative_url }}">{{ page.name }}</a>{% else %}<a href="{{ page.url | relative_url }}">{{ page.persona }}</a> {% endif %} </li>
{% endfor %}
</ul>
{% endfor %}
