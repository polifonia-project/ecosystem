---
layout: default
title: Licences
nav_order: 20
permalink: /licences.html
---

# {{ page.title }}

The Polifonia Ecosystem components, grouped by licences:

{% assign licences = site.data.licences %}

{% for licence in licences %}
###{{licence.title}}
{% assign comps = site.documents  | where_exp: 'item',"item.licence contains licence" %}
{% assign cnumber = comps | size %}
{{cnumber}} components are released with this licence:
<ul>
 {% for comp in comps %}
 <li><a href="{{comp.url | relative_url}}">
     {% if comp.name %}{{comp.name}}{%else%}{{comp.component-id}}{% endif %}
     </a>
 </li>
 {% endfor %}
</ul>
{% endfor %}