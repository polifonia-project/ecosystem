---
component-id: sparql-anything-docker
type: DockerImageContainer
name: SPARQL Anything Docker Instance
description: Docker file of the SPARQL Anything Web Server
logo: https://avatars.githubusercontent.com/u/79987779?s=200&v=4
work-package:
- WP2
- WP3
- WP4
licence:
- Apache-2.0
pilot:
- MEETUPS
project: polifonia-project
resource: https://github.com/SPARQL-Anything/sparql.anything/blob/v0.8-DEV/Dockerfile.development
release-date: 2022/12/18
release-number: v0.8.1
release-link: https://github.com/SPARQL-Anything/sparql.anything/releases/tag/v0.8.1
doi: 10.5281/zenodo.7454360
changelog: https://github.com/SPARQL-Anything/sparql.anything/releases/tag/v0.8.1
related-components:
- documentation: sparql-anything-docs
- reuses:
  - sparql-anything-server
  - sparql-anything-java
---

# SPARQL Anything Docker Image

Instructions to build a docker image with a running Fuseki server. 

Create a Dockerfile as follows, see also [this file](https://github.com/SPARQL-Anything/sparql.anything/blob/v0.8-DEV/Dockerfile.development):

```
FROM mcr.microsoft.com/playwright/java:focal
#    needed for the headless browser

LABEL description="SPARQL Anything"

RUN apt-get update && apt-get install -y maven
# Set the locale https://stackoverflow.com/questions/28405902/how-to-set-the-locale-inside-a-debian-ubuntu-docker-container
RUN apt-get install locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV VERSION "0.9.0-SNAPSHOT"

# normal
CMD cd /app && mvn clean install && \
    java -cp \
    "/app/sparql-anything-fuseki/target/sparql-anything-server-${VERSION}.jar:$(for i in /app/*jar ; do printf '%s:' $i ; done)" \
    com.github.sparqlanything.fuseki.Endpoint
```
