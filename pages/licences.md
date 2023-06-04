---
layout: default
title: Licences
nav_order: 20
permalink: /licences.html
---

# {{ page.title }}

The Polifonia Ecosystem components, grouped by licences.


<div id="chart_container_software"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
        {x: "Apache License, Version 2.0", value: 12},
        {x: "CC0 1.0 Universal ", value: 2},
        {x: "Creative Commons Attribution 4.0", value: 9},
        {x: "Creative Commons Attribution-NonCommercial", value: 1},
        {x: "ISC License", value: 1}
    ];
    // create the chart
    var chart = anychart.pie3d();
    // set the chart title
    // chart.title("Polifonia Project Components by Type");
    // add the data
    chart.data(data);
    // sort elements
    chart.sort("desc");  
    // set legend position
    chart.legend().position("right");
    // set items layout
    chart.legend().itemsLayout("vertical");
    // display the chart in the container
    chart.container('chart_container_software');
    chart.draw();
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