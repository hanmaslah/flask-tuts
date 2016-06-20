What is Flask?
Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
It is used to make web applications with less effort.

Setting up Flask on windows
Create a new directory
$ mkdir flasktest
$ cd flasktest
Or simply $ cd mydirectory if you had already created it
Once you are in the directory you want to create your flask application, write the following command
$ pip install virtualenv
This installs the virtual environment. 
Virtualenv is a useful tool that creates isolated Python development environments where you can do all your development work.

After installing virtualenv, you can create a new isolated development environment, like so:
$ virtualenv flaskapp
Here, virtualenv creates a folder, flaskapp/, and sets up a clean copy of Python inside for you to use. 
It also installs the handy package manager, pip.

Activate your virtual environment so that you can start working with it
$ flaskapp\Scripts\activate.bat
Notice that if you are using CMD, the commandline will look like this afterwards:
(flaskapp) C:\Users\****\path\directory\flaskapp>

Now, you can safely install Flask:
$ pip install Flask

You now have flask in your directory. See the next tutorial on how to create your first app

