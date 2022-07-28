# Polifonia Dashboard

## Quickstart

> **Step #1 - Get the source code**


- Download the ZIP
- Use GIT tool in the terminal/powershel/bash to clone the source code


> **Step #2 - Set up the environment**


1. Python3 should be installed properly in the workstation. If you are not sure if Python is 
properly installed, please open a terminal and type python --version.
2. Enter the project folder using the terminal/powershel/bash.
3. Install modules using a [Virtual Environment](https://docs.python.org/3/library/venv.html)
```bash
#MacOS/Linux
$ cd myproject
$ python3 -m venv venv
$ . venv/bin/activate

#Windows
> cd myproject
> py -3 -m venv venv
> venv\Scripts\activate
```


> **Step #3 - Install requirements**



`pip install -r requirements.txt`



> **Step #4 - Run the application**
```bash
#bash
$ export FLASK_APP=app
$ flask run
* Running on http://127.0.0.1:5000/
** To see something, visit http://127.0.0.1:5000/musow

#CMD
> set FLASK_APP=app
> flask run
* Running on http://127.0.0.1:5000/
** To see something, visit http://127.0.0.1:5000/musow

#Powershell
> $env:FLASK_APP = "app"
> flask run
* Running on http://127.0.0.1:5000/
** To see something, visit http://127.0.0.1:5000/musow
```
