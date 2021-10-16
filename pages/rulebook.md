---
layout: default
title: Rulebook
nav_order: 20
permalink: /rulebook.html
---

<div class="well">
    <h2>Rulebook</h2>
    <ul>
    {% for file in site.rulebook %}
    <li><a href="{{ file.url | relative_url }}">
        {{ file.id | replace: "/rulebook/", ""  }}
        </a></li>
    {% endfor %}
    </ul>
</div>
