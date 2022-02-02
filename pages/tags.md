---
layout: default
title: Tags (dev)
nav_order: 8
permalink: /tags.html
---

# Tags (dev)

## Work Packages

{% for wp in site.pages %}
  {% if wp.identifier == "wppage" and wp.name != "index.md" %}
### WP{{ wp.title }}
  {% assign wp-posts = site.documents | where: "WP", wp.wp %}
<ul class="inline list-style-none">
{% for page in wp-posts %}
  <li> {% if page.name %}<a href="{{ page.url | relative_url }}">{{ page.name }}</a>{% else %}<a href="{{ page.url | relative_url }}">{{ page.persona }}</a> {% endif %} </li>
{% endfor %}
</ul>
  {% endif %}
{% endfor %}

## Pilots

{% for pilot in site.pages %}
  {% if pilot.identifier == "pilotpage" and pilot.name != "index.md" %}
### {{ pilot.title }}
  {% assign pilot-posts = site.documents | where: "pilot", pilot.title %}
<ul class="inline list-style-none">
{% for page in pilot-posts %}
  <li> {% if page.name %}<a href="{{ page.url | relative_url }}">{{ page.name }}</a>{% else %}<a href="{{ page.url | relative_url }}">{{ page.persona }}</a> {% endif %} </li>
{% endfor %}
</ul>
  {% endif %}
{% endfor %}
