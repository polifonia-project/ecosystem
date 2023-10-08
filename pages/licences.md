---
layout: default
title: Licences
nav_order: 20
permalink: /licences.html
---

# {{ page.title }}

The Polifonia Ecosystem components, grouped by licences.

<!-- Create the canvas for the chart -->
<div>
  <canvas id="data_pie_chart"></canvas>
</div>
<!-- Import chart.js and build the chart -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
  const ctx = document.getElementById('data_pie_chart');

  new Chart(ctx, {
    type: 'doughnut',
    options: {
      responsive: true,
      radius: '70%'
    },
    data: {
      labels: [
        'Apache 2.0',
        'CC0 Universal',
        'CC Attribution', 
        'CC Attribution-NonCommercial',
        'ISC License'
        ],
      datasets: [{
        label: 'No. of Components',
        data: [12, 2, 12, 2, 1],
        borderWidth: 3
      }]
    }
  });
</script>

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