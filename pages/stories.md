---
layout: default
title: Stories
nav_order: 10
permalink: /stories.html
---

<h2>Stories</h2>
{% assign stories_grouped = site.stories | group_by: "persona" %} 
{% for group in stories_grouped %}
{% assign personashort = group.name | replace: '["' | replace: '"]'%}
<h3>{{ personashort }}</h3>
{% for item in group.items %}
<ul>
{% if item.title contains "Readme" %}
<li><a href="{{item.url | absolute_url}}">{{personashort}}'s description</a></li>
{% else %}
<li><a href="{{item.url | absolute_url}}">{{item.title}}</a></li>
{% endif %}
</ul>
{% endfor %}
{% endfor %}

