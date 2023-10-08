---
id: software
name: Components of type Software or Application
description: List of components of type software or application
layout: default
title: Tools
nav_order: 13
permalink: /software.html
---

# Tools

This section collects project outputs that are released as *software* or *application*.

The ecosystem considers software any digital object that is being produced by the project to achieve a certain task computationally.
We distinguish software from applications, where software is used (executed) by a user to perform the task.
These include various types of digital objects such as scripts, software libraries, workflows, or APIs.

The ecosystem considers applications executable systems and tools produced by the project for the end-user to achieve a certain task computationally.
We distinguish applications from software, where software can be copied, moved, and executed in multiple different applications (each in relation to some usage senarios).
Applications include various types of artifacts such as Web Applications, Web sites, and Command Line Interface (CLI) tools.

<!-- Create the canvas for the chart -->
<div>
  <canvas id="data_pie_chart"></canvas>
</div>
<!-- Import chart.js and build the chart -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
  const ctx = document.getElementById('data_pie_chart');

  new Chart(ctx, {
    type: 'doughnut',
    options: {
      responsive: true,
      radius: '70%'
    },
    data: {
      labels: [
        'Application',
        'CLITool',
        'DockerImageContainer', 
        'SPARQLEndpoint',
        'Software',
        'SoftwareLibrary',
        'UserInterface',
        'WebApplication'
        ],
      datasets: [{
        label: 'No. of Tools',
        data: [1, 1, 1, 2, 9, 2, 1, 5],
        borderWidth: 3
      }]
    }
  });
</script>


{% assign software_data = "Software,Workflow,API,UserInterface,SoftwareLibrary,DockerImageContainer,Notebook,Script,Application,Website,WebApplication,WebService,SPARQLEndpoint,MobileApp,CLITool" | split: "," | sort %}
{% for type in software_data %}
{% if type != "" %}
{% assign numberOf = site.documents  | where_exp: 'item', "item.type == type" | size %}
{% if numberOf > 0 %}
### {{ type }}

There are {{numberOf}} components of type {{type}}:
	{% assign components =  site.documents  | where: 'type',type %}
	{% include reeco-components-table.html components=components %}
{% endif %}
{% endif %}
{% endfor %}