##
# From flask quickstart:
#   http://flask.pocoo.org/docs/0.12/quickstart/
#
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

