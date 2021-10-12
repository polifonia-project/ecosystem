---
layout: default
title: Rulebook
nav_order: 3
permalink: /rulebook.html
---

<div class="well">
    <h2>Rulebook</h2>
    <ul>
    {% for file in site.rulebook %}
    <li><a href="{{ site.baseurl }}{{ file.url }}">
        {{ file.id | replace: "/rulebook/", ""  }}
        </a></li>
    {% endfor %}
    </ul>
</div>
