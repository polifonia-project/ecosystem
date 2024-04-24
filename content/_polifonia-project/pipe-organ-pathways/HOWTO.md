Requirements:

Angular – This needs to be installed on your laptop and will enable you to run the “ng” command. Globally (on my Macbook), I am running v11. I believe Paul is running v9 and when I compile his slow-looking app it uses v9 but warns me that this local version in that folder doesn’t match my global v11. This doesn’t seem to matter and works fine.
 
Ng commands, from within the root folder of the app:
 
‘ng serve’ – will compile and run the app in a temporary webserver at localhost:4200/
 
‘ng build --configuration=production --base-href=/demos/imma-slow-looking/  --crossOrigin=anonymous’ – this is the build command, for distribution. Note we have to tell it where the app will reside on the webserver (/demos/imma-slow-looking/). The command compiles everything into a bunch of minified JS/TS files that can be dropped onto a webserver.
 
Now if you navigate into the ‘dist’ folder, you will see a built distribution folder. This is likely to be called ‘slowlooking1’ (taken from the app’s config somewhere). Rename this to ‘imma-slow-looking’:
 
Tar/gz this file and copy it to the webserver, unpack in the correct location and ensure all files are owned by the webserver user.
 
 

