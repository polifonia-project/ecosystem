---
layout: default
title: Licences
nav_order: 20
permalink: /licences.html
---

# {{ page.title }}

The Polifonia Ecosystem components, grouped by licences.

{% assign licences = site.data.licences |sort: 'title' %}

{% for licence in licences %}
  {% assign comps = site.documents  | where_exp: 'item',"item.licence contains licence.code" %}
  {% assign cnumber = comps | size %}
  {% if cnumber > 0 %}
### {{licence.title}}

Published by {{licence.publisher}}

Link to legal text: <a href="{{licence.link}}">{{licence.title}}</a>

{{cnumber}} component{% if cnumber > 1%}s are{%else%} is{%endif%} released with this licence:
<ul>
 {% for comp in comps %}
 <li><a href="{{comp.url | relative_url}}">
     {% if comp.name %}{{comp.name}}{%else%}{{comp.component-id}}{% endif %}
     </a>
 </li>
 {% endfor %}
</ul>
   {% endif %}
{% endfor %}