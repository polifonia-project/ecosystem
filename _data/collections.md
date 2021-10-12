---
layout: default
title: Collections (dev)
nav_order: 9
permalink: /collections.html
---

# Collections

<ul>
{% for coll in site.collections %}
<li> {{ coll.label }} 
<ul>
{% for d in coll.docs %}
<li>{{ d.id }}</li>
{% endfor %}
</ul>
</li>
{% endfor %}
</ul>
