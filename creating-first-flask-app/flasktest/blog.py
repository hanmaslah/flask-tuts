from flask import Flask
app = Flask(__name__)
@app.route('/')
def show_home():
	return 'This is Home page'
@app.route('/blog/<postId>')
def show_blog(postId):
	return 'Post ID{0}'.format(postId)
@app.route('/rev/<revNo>')
def revision(revNo):
	return 'Revision {%f}'.format(revNo)
if __name__=='__main__':
	app.run()