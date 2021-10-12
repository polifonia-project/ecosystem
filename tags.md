---
layout: default
title: Tags (dev)
nav_order: 8
permalink: /tags.html
---

# Tags

## WP

<div class="wps">
  {% assign wps = site.pages | group_by: 'WP' %}
  {% for wp in wps %}
{{ wp }}

  {% endfor %}
</div>

## WP2 

<ul>
{% assign sorted-posts = site.pages | where: "Pilots","Access" %}
{% for page in sorted-posts %}
  <li>coucou {{page.id}}</li>
  {% endfor %}
</ul>

## 3

{% assign items_grouped = site.pages | group_by: 'Pilots' %}
  {% for group in items_grouped %}
    <h3>{{group.name}}</h3>
    {% for item in group.items %}
        <p>{{item.path}}</p>
    {% endfor %}
  {% endfor %}

## Data

<ul>
{% for wp in site.data.wps %}
  <li>
    <a href="{{ }}">
      {{ wp.name }}
    </a>
  </li>
{% endfor %}
</ul>
