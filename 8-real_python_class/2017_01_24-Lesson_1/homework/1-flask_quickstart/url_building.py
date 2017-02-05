##
# From flask quickstart:
#   http://flask.pocoo.org/docs/0.12/quickstart/
#
from flask import Flask, url_for
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
    url_building()
    return 'The about page'

#
#  Url Building:
#
def url_building():
    with app.test_request_context():
        route_for_index = url_for('index')
        route_for_user = url_for('show_user_profile', username="Tom")
        route_for_post = url_for('show_post', post_id=6)
        route_for_projects = url_for('projects')
        route_for_about = url_for('about')
        app.logger.debug( "route_for_index: %s", route_for_index )
        app.logger.debug( "route_for_user: %s", route_for_user )
        app.logger.debug( "route_for_post: %s", route_for_post )
        app.logger.debug( "route_for_projects: %s", route_for_projects )
        app.logger.debug( "route_for_about: %s", route_for_about )

## url_building()

