---
layout: default
title: External components
nav_order: 4
permalink: /external-components.html
---

<div class="well">
    <h2>External components</h2>
    <ul>
    {% for comp in site.external-components %}
    <li><a href="{{ comp.url | relative_url }}">
    {{ comp.path }} ({{ comp.name }})
        </a></li>
    {% endfor %}
    </ul>
</div>
