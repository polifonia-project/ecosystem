# Pipe Organs

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 14.1.2.

## Configuring Pipe Organs to work with the SPICE Linked Data Hub

Copy the file `src/app/config.example.ts` to `src/app/config.ts`

This file contains the configuration settings for the application.

__citizenDatasetUUID__: This should contain the UUID for the dataset where you will store and retrieve the citizen contributions.

__collectionDatasetUUID__: This should contain the UUID for the dataset where you will access the museum collection used in the app.

__collectionQuery__: This should contain the SPARQL query for retrieving artworks from the museum collection. For each artwork, the query should return values for the following variables as strings:

* __?title__ (the title of the artwork)

* __?creatorname__ (the creator/artist of the artwork)

* __?artworkurl__ (the URL of the image file for the artwork)

* __?year__ (the year/time period that the artwork was created)


__config__: This should contain your authorisation string for accessing the SPICE Linked Data Hub.

## Development server

Run `npm install`

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Build

‘ng build --configuration=production --base-href=/demos/imma-slow-looking/  --crossOrigin=anonymous’ – this is the build command, for distribution. Note we have to tell it where the app will reside on the webserver (/demos/imma-slow-looking/). The command compiles everything into a bunch of minified JS/TS files that can be dropped onto a webserver.
 
Now if you navigate into the ‘dist’ folder, you will see a built distribution folder. This is likely to be called ‘slowlooking1’ (taken from the app’s config somewhere). Rename this to ‘imma-slow-looking’:
 
Tar/gz this file and copy it to the webserver, unpack in the correct location

