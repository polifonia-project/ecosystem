---
layout: default
title: Personas
nav_order: 11
permalink: /personas.html
---


<div class="well">
    <h2>Personas</h2>
    {% include group-by-array.html collection=site.stories field='persona' %}

<ul>
  {% for persona in group_names %}
    {% assign posts = group_items[forloop.index0] %}

    <li>
      <h2>{{ persona }}</h2>
      <ul>
        {% for post in posts %}
        <li>
          <a href='{{ site.baseurl }}{{ post.url }}'>{{ post.title }}</a>
        </li>
        {% endfor %}
      </ul>
    </li>
  {% endfor %}
</ul>
</div>

