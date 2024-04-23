---
component-id: polifonia-web-portal
type: WebApplication
name: Polifonia Web Portal
description: Source code of the Polifonia Portal web application
work-package: 
- WP1
project: polifonia-project
resource: https://polifonia.disi.unibo.it/portal/
demo: https://polifonia.disi.unibo.it/portal/
release-date: 2024/1/03
release-number: v0.1.1
release link: https://github.com/polifonia-project/portal/releases/tag/Latest
doi: 10.5281/zenodo.10454048
licence:
- Cc010Universal
contributors:
- Marilena Daquino <https://github.com/marilenadaquino>
- Marco Grasso <https://github.com/marcograsso>
- Giulia Renda <https://github.com/mondoboia>
related-components:
related-components:
  - serves: 
     - broadcast-concerts-knowledge-graph
     - led
     - meetups-knowledge-graph
     - musicbo-knowledge-graph
     - bells-knowledge-graph
     - musow-dataset
  - reuses: 
     - polifonia-corpus-web-api
     - melody-software
     - musow-interface
  - extends: 
     - web-portal-prototypes
bibliography:
- main-publication: "Giulia Renda, Marco Grasso, and Marilena Daquino (2023). From ontology design to user-centred interfaces for music heritage. In Proceedings of AIUCD 2023. Preprint available at: https://arxiv.org/abs/2306.12973v1"
  
---

# Polifonia Web Portal
[![DOI](https://zenodo.org/badge/587248478.svg)](https://zenodo.org/doi/10.5281/zenodo.10454047)

The Polifonia Web portal is the main entry point into the extensive musical heritage produced by Polifonia. It is targeted to enthusiasts, scholars, musicians, and educators, and facilitates exploration of a varied spectrum of musical Linked Data. Key functionalities of the portal include text search and on-demand insights. The web portal currently ingests a selection of pilot datasets and allows their exploration via bespoke user journeys designed to foster serendipitous discovery.

Users can:
1. Explore content by category (Genres, Artists, Music, Places, Instruments) thanks to a text search.
2. Discover relationships between entities of different types.
3. Open insight cards for each entity.

The technology stack of the Web portal includes: 
* A Flask backend and a React-native frontend application. Communication between the frontend and backend is ensured by RESTful APIs. 
* Sonic search backend is used for fast indexing of data ingested in the web portal and ensures a responsive user experience. 
* Blazegraph triplestore is used to store post-processed data. In particular, data ingested from external sources is analysed to extract alignments between entities described in different data sources (e.g. people, places, genres) and the links across datasets are stored in a dedicated linkset (reconciliation process).


## Requirements

Install python and nodejs

Linux

```
# install python and requirements
apt-get install python3
apt-get install python3-pip
cd backend
pip install -r requirements.txt

# install node.js, npm, and react dependencies
apt-get install nodejs
apt-get install npm
cd ..
cd frontend
npm install (--force)

# install sonic index
# TODO

# install blazegraph
# wget https://github.com/blazegraph/database/releases/download/BLAZEGRAPH_2_1_6_RC/blazegraph.jar
```


## Configuration

### Populate indexes

Check paths in the configuration file of Sonic `sonic/config.cfg`.
See the [official documentation](https://github.com/valeriansaliou/sonic).

Modify the file `backend/conf_general.json` and add your SecretPassword:

```
{
    "index_host": "localhost",
    "index_channel": 1491,
    "index_pw": "MyPerfectSecretPassword",
    "data_sources": {
        "datatsets": "conf_datasets.json",
        "categories": "conf_categories.json",
        "feed": "conf_feed.json",
        "carousel": "conf_carousel.json",
        "cards": "conf_cards.json"
    }
}
```

Populating Sonic indexes is a one-time operation that is done the first time you run the application.

To populate indexes you must modify the following configuration files, and specify SPARQL endpoints and SPARQL queries to retrieve lists of URIs and their labels:

 * `backend/conf_categories.json`
 * `backend/conf_datasets.json`
 * `backend/conf_carousel.json`
 * `backend/conf_cards.json`
 * `backend/conf_feed.json`
 * `backend/conf_general.json`

For instance in `backend/conf_categories.json`:

```
"search_pattern": [
    {
        "dataset": "d_01",
        "query": "SELECT DISTINCT ?entity ?entityLabel WHERE { ?s <https://schema.org/specialty> ?entity . ?entity rdfs:label ?entityLabel } LIMIT 20"
    },
    {
        "dataset": "d_04",
        "query": "SELECT DISTINCT ?entity ?entityLabel WHERE {?entity wdt:P31 wd:Q1053916 . SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\" }} LIMIT 20"
    }
]
```

and in `backend/conf_datasets.json`:

```
"d_01": {
    "id": "d_01",
    "name": "musow",
    "iri_base": "https://w3id.org/musow/",
    "query_method": "sparql_endpoint",
    "sparql_endpoint": "https://projects.dharc.unibo.it/musow/sparql",
    "rest_api": ""
}
```

If you want to force re-populating the indexes when rerunning the application, modify the file `backend/conf_categories.json` and remove every occurrence of `"status":"ingested"`.

### Reconciliation

TODO - which functions and parameters to use 
TODO - workflow

### Backend and frontend

In `frontend/package.json` define:

 * the proxy for your backend application. default is `"proxy": "http://127.0.0.1:5000/"` on a dev server and `"proxy": "http://0.0.0.0:5000/"` in production.
 * the homepage. default is `.` on a dev server, and the full URL in production.

### Categories, Carousel, Cards

TODO


## Run

Run Sonic

```
$ cd sonic
$ sonic -c config.cfg # OR $ ./target/release/sonic -c config.cfg
```

Run Blazegraph (default port `9999`) - only if reconciliation is enabled

```
cd ../backend
$ java -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -server -Xmx1g -Djetty.port=9999 -jar blazegraph.jar 
```

Run Flask (default port `5000`)

```
python3 app.py 5000
```

Run React (default port `3000`)

```
cd ../frontend
npm start
```

## In production

Flask + React with nginx (see a nice [tutorial](https://blog.miguelgrinberg.com/post/how-to-deploy-a-react--flask-project))

### Sonic

```
./target/release/sonic -c config.cfg &
```

### Blazegraph

Run blazegraph as you would do in dev

```
$ java -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -server -Xmx1g -Djetty.port=9999 -jar blazegraph.jar 
```

### Flask and gunicorn

Install gunicorn and run the Flask API

```
pip install gunicorn
cd ../backend
gunicorn -w 4 -b 0.0.0.0:5000 app:app &
```


### React

Create a build of the react application and serve it

```
cd frontend
npm run build # create the build
npm install -g serve # install serve for the first time
serve -s build &
```
Check for absolute paths in index.html and change them if you run the app in a subdomain

### NGINX
Install and setup nginx

```
apt-get install nginx 
```

Modify the configuration file `vi /etc/nginx/sites-available/default`

```
server {
    listen 80 ;
    listen [::]:80 ;
    root /home/frontend/build;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / {
      # First attempt to serve request as file, then
      # as directory, then fall back to displaying a 404.
      try_files $uri $uri/ /index.html =404;
      #proxy_pass http://localhost:3000;
    }

    location /conf_info {
      include proxy_params;
      #add_header 'Access-Control-Allow-Origin' http://localhost:80;
      proxy_pass http://0.0.0.0:5000;
      proxy_redirect default;
    }

    location /sonic_index {
      include proxy_params;
      #add_header 'Access-Control-Allow-Origin' http://localhost:80;
      proxy_pass http://0.0.0.0:5000;
      proxy_redirect default;
    }

    location /reconciliation {
      include proxy_params;
      #add_header 'Access-Control-Allow-Origin' http://localhost:80;
      proxy_pass http://0.0.0.0:5000;
      proxy_redirect default;
    }

    location /card {
      include proxy_params;
      #add_header 'Access-Control-Allow-Origin' http://localhost:80;
      proxy_pass http://0.0.0.0:5000;
      proxy_redirect default;
    }
}
```
Start nginx `service nginx start` or restart `service nginx restart`.


### Proxies

The docker runs on Apache

```
# portal
Redirect permanent /portal /portal/​
ProxyPass /portal/static/ http://polifonia.disi.unibo.it:8109/​
ProxyPass /portal/ http://polifonia.disi.unibo.it:8109/​
ProxyPassReverse /portal/ http://polifonia.disi.unibo.it:8109/
```

## TODO

 * make docker image
 * command restart docker
 * restart app on crash
