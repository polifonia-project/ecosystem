---
layout: default
title: Stories
nav_order: 10
permalink: /stories.html
---

<div class="well">
    <h2>Stories</h2>
    <ul>
    {% for story in site.stories %}
    <li><a href="{{ story.url | relative_url}}">
        {{ story.persona }} ({{ story.title }})
        </a></li>
    {% endfor %}
    </ul>
</div>
