---
layout: default
title: External components
nav_order: 30
permalink: /external-components.html
---

<div class="well">
    <h2>External components</h2>
    <ul>
    {% for comp in site.external-components %}
    <li><a href="{{ comp.url | relative_url }}">
    {% if comp.name %} {{ comp.name }} {% else %} {{ comp.id }} {% endif %}
        </a></li>
    {% endfor %}
    </ul>
</div>
