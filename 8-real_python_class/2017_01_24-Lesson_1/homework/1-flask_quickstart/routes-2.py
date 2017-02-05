##
# From flask quickstart:
#   http://flask.pocoo.org/docs/0.12/quickstart/
#
from flask import Flask
app = Flask(__name__)

#
#  Routes:
#
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

#
#  Variable Rules:
#
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

#
#  Unique Rules:
#  -------------
#  Accessing:
#     http://127.0.0.1:5000/projects
#  redirects to:
#     http://127.0.0.1:5000/projects/
#
@app.route('/projects/')
def projects():
    return 'The project page'
#
#  Accessing:
#     http://127.0.0.1:5000/about
#  works ok.
#  Accessing:
#     http://127.0.0.1:5000/about/
#  gives a 404 not found error.
#
@app.route('/about')
def about():
    return 'The about page'
