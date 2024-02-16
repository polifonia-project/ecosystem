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

The ecosystem includes {% assign types_data = "Data,Dataset,Schema,Repository,Registry,Ontology,Corpus,Lexicon,KnowledgeGraph" | split: "," %}{% assign ncomponents = site.documents  | where_exp: 'item',"types_data contains item.type" | size %} {{ncomponents}} <a href="data.html">data</a>, {% assign software_data = "Software,Workflow,API,UserInterface,SofwareLibrary,DockerImageContainer,Notebook,Script,Application,Website,WebApplication,WebService,SPARQLEndpoint,MobileApp,CLITool" | split: "," %} {% assign ncomponents = site.documents  | where_exp: 'item',"software_data contains item.type" | size %} {{ncomponents}} <a href="software.html">tools</a>, {% assign report_data = "Report,RequirementsCollection,Story,Persona,Mockup,Survey,InPresenceGroup,Documentation,Tutorial,EvaluationReport" | split: "," %}{% assign ncomponents = site.documents  | where_exp: 'item',"report_data contains item.type" | size %} and {{ncomponents}} <a href="report.html">reports</a>.

Project content is managed on [GitHub](http://github.com/{{ site.github }}).


<div id="chart_container_data"></div>
<script>
anychart.onDocumentReady(function() {
    // set the data
    var data = [
		{% for type in types %}
			{% if type != "" %}
				{% assign comps =  site.documents  | where: 'type',type | size%}
				{% if comps > 0 %}
     		   		{x: "{{type}}", value: {{ comps }} },
				{% endif %}
			{% endif %}
		{% endfor %}
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
    chart.container('chart_container_data');
    chart.draw();
  });
  </script>

{% comment %}
{% for type in types %}
{% if type != "" %}
{% assign components =  site.documents  | where: 'type',type %}
{% assign numberOf = components | size %}
{% if numberOf > 0 %}
### {{ type }}

There are {{numberOf}} components of type {{type}}:
	{% for component in components %}
- [{% if component.name %}{{ component.name }}{%else%}{{ component.component-id}} {%endif%}]({{ component.url | relative_url }})	{% endfor %}	
{% endif %}
{% endif %}
{% endfor %}
{% endcomment %}
