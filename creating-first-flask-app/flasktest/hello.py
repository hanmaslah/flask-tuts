from flask import Flask
app = Flask ( __name__ )
@app . route ('/hello/<name>')
def hello_world (name):
	return 'My world rocks !! Hello {0}'.format(name)
if __name__ == '__main__ ':
	app . run (host='127.0.0.1', port=5000)