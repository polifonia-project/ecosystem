---
container-id: polifonia-project
type: Project
work-package:
- WP1
- WP2
- WP3
- WP4
- WP5
- WP6
- WP7
- WP8
pilot:
- TUNES
- BELLS
- INTERLINK
- MUSICBO
- TONALITIES
- MEETUPS
- CHILD
- ORGANS
- ACCESS
- FACETS
funder:
  - name: Horizon 2020 Framework Programme
    url: https://cordis.europa.eu/programme/id/H2020-EC
    grant-agreement: "https://cordis.europa.eu/project/id/101004746"
credits: "This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement N. 101004746."
layout: default
title: Home
nav_order: 0
permalink: /
ecosystem-release: v2.0
---

# Polifonia Ecosystem ({{ page.ecosystem-release }})
{: .fs-9 }

Data, software, and documentation of the output of the EU H2020 project [Polifonia]({{ site.main-project-url }}.). 
{: .fs-6 .fw-300 }

---

The Polifonia Ecosystem is a collection of components for developing intelligent applications leveraging musical cultural heritage, result of the Polifonia Project.
The project aims at realising and deploying anecosystem of computational methods and tools supporting discovery, extraction, encoding, interlinking, classification, exploration of, and access to, musical heritage knowledge on the Web.

Polifonia content is managed on [GitHub](http://github.com/{{ site.github }}).

{% comment %} 
Polifonia development methodology is two ways. 
It follows a bottom-up approach, ensuring that the development is participatory, agile, feature driven, and collaborative.
However, this is paired with a top-down approach, where a Technical Board interacts with WP leaders to ensure the objectives of the project are fully met.

The components are both independent – they have some value on their own – and interlinked – they can be used together in order tosatisfy specific end-user needs. 
Independence is a well known principle of software engineering, which is conceived alongside the one of inter-operability - the ability of a software componentto operate with others.
However, the possible connections between ecosystem components don’t necessarily derive from software-to-software relations but involve, for example, users being able to perform a complex task by using multiple tools, whose user interfaces are linked, or enable users to transfer data from one environment to another thanks to the mutual support of shared formats. 
The Polifonia Project delivers its results as reusable assets, alongside an extensive metadata set and documentation. This is the Polifonia Ecosystem.
{% endcomment %} 
{% assign types =  site.documents  | map: 'type' | join: ','  | split: ',' | uniq | sort %}

## Summary


{% assign types_data = "Data,Dataset,Schema,Repository,Registry,Ontology,Corpus,Lexicon,KnowledgeGraph" | split: "," %}
{% assign ncomponents = site.documents  | where_exp: 'item',"types_data contains item.type" | size %}
<a href="data.html">Data</a>: {{ncomponents}}



#### All types
{% for type in types %}
{% assign ncomponents =  site.documents  | where: 'type',type | size %}
{% if ncomponents > 0 %} {{ type }}: {{ ncomponents }} {% endif %}
{% endfor %}

## List of components 
{% for type in types %}
{% if type != "" %}
### {{ type }} ({{ site.documents  | where: 'type',type | size }})
	{% assign components =  site.documents  | where: 'type',type %}
	{% for component in components %}
- [{{ component.name }}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endfor %}

