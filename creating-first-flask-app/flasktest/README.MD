Create a python file called hello.py
In order to test Flask installation, type the following code in the editor as hello.py
	from flask import Flask
	app = Flask(__name__)
	@app.route('/')
	def hello_world():
		return 'Hello World’
	if __name__ == '__main__':
		app.run(host='127.0.0.1', port=5000)
Importing flask module in the project is mandatory. An object of Flask class is our WSGI
application.
WSGI - Web Server Gateway Interface (WSGI) is a specification for simple and universal interface between web servers 
and web applications or frameworks for the Python programming language.
Flask constructor takes the name of current module (__name__) as argument.
The route() function of the Flask class is a decorator, which tells the application which
URL should call the associated function.
app.route(rule, options)
- The rule parameter represents URL binding with the function.
- The options is a list of parameters to be forwarded to the underlying Rule object.
In the above example, ‘/’ URL is bound with hello_world() function. Hence, when the
home page of web server is opened in browser, the output of this function will be rendered.
	def hello_world():
		return 'Hello World’
That is the hello_world() function that returns "Hello World" when called.

finally 
	if __name__ == '__main__':
		app.run(host='127.0.0.1', port=5000)
The run() method of Flask class runs the application on the local development
server.
app.run(host, port, debug, options)
In my case, the host is '127.0.0.1' which is localhost and runs on port 5000

Save your python application and run it
$ python hello.py

Now run it on the web
$ set FLASK_APP=hello.py
$ flask run

Go to your browser and input the url http://127.0.0.1:5000

And there you are...bingo!! your first flask application



